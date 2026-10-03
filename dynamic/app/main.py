"""
Microservice: Cloud Payment Gateway (Demo for Dynamic Secret Injection)
Demonstrates:
  1. Ephemeral credential acquisition via HashiCorp Vault AppRole
  2. Dynamic least-privilege DB role usage (pg8000)
  3. Automatic Lease management, TTL renewal, and graceful error handling on revocation
"""

import os
import time
import uuid
import logging
from typing import Optional, Dict, Any
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
import requests
import pg8000.native

# Configure Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("payment-service")

# Environment Configurations
VAULT_ADDR = os.getenv("VAULT_ADDR", "http://127.0.0.1:8200")
VAULT_ROLE_ID = os.getenv("VAULT_ROLE_ID", "")
VAULT_SECRET_ID = os.getenv("VAULT_SECRET_ID", "")
VAULT_TOKEN = os.getenv("VAULT_TOKEN", "root") # Fallback to token if AppRole not provided
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_NAME = os.getenv("DB_NAME", "ecommerce_db")
DYNAMIC_ROLE_PATH = os.getenv("DYNAMIC_ROLE_PATH", "database/creds/payment-service-role")

class DynamicSecretManager:
    """Manages ephemeral credentials obtained from HashiCorp Vault."""

    def __init__(self):
        self.vault_token = VAULT_TOKEN
        self.current_creds: Optional[Dict[str, Any]] = None
        self.lease_id: Optional[str] = None
        self.lease_duration: int = 0
        self.lease_expires_at: float = 0

    def authenticate_approle(self) -> str:
        """Authenticate with Vault using AppRole credentials to retrieve client token."""
        if not VAULT_ROLE_ID or not VAULT_SECRET_ID:
            logger.info("Using standard VAULT_TOKEN auth (AppRole credentials not supplied).")
            return self.vault_token

        url = f"{VAULT_ADDR}/v1/auth/approle/login"
        payload = {"role_id": VAULT_ROLE_ID, "secret_id": VAULT_SECRET_ID}
        resp = requests.post(url, json=payload, timeout=5)
        if resp.status_code != 200:
            raise RuntimeError(f"Vault AppRole authentication failed: {resp.text}")

        token = resp.json()["auth"]["client_token"]
        self.vault_token = token
        logger.info("Successfully authenticated to Vault via AppRole.")
        return token

    def get_dynamic_db_credentials(self, force_refresh: bool = False) -> Dict[str, Any]:
        """Fetch short-lived database credentials from HashiCorp Vault."""
        now = time.time()
        # Return cached credentials if they are still valid with at least 15s buffer
        if not force_refresh and self.current_creds and (self.lease_expires_at - now > 15):
            return self.current_creds

        logger.info(f"Requesting new dynamic credentials from path '{DYNAMIC_ROLE_PATH}'...")
        headers = {"X-Vault-Token": self.vault_token}
        url = f"{VAULT_ADDR}/v1/{DYNAMIC_ROLE_PATH}"
        resp = requests.get(url, headers=headers, timeout=5)

        if resp.status_code == 403:
            # Token might be expired, re-authenticate and retry once
            logger.warning("Vault token unauthorized. Attempting AppRole re-authentication...")
            self.authenticate_approle()
            headers["X-Vault-Token"] = self.vault_token
            resp = requests.get(url, headers=headers, timeout=5)

        if resp.status_code != 200:
            raise RuntimeError(f"Failed to fetch dynamic secrets: status {resp.status_code}, error: {resp.text}")

        data = resp.json()
        self.lease_id = data.get("lease_id")
        self.lease_duration = data.get("lease_duration", 60)
        self.lease_expires_at = now + self.lease_duration
        self.current_creds = {
            "username": data["data"]["username"],
            "password": data["data"]["password"],
            "lease_id": self.lease_id,
            "lease_duration": self.lease_duration,
            "expires_in_seconds": round(self.lease_expires_at - now, 1)
        }
        logger.info(f"Acquired dynamic credential: username='{self.current_creds['username']}', "
                    f"lease_duration={self.lease_duration}s, lease_id='{self.lease_id}'")
        return self.current_creds

    def renew_lease(self, increment_seconds: int = 120) -> Dict[str, Any]:
        """Renew lease for the current dynamic secret."""
        if not self.lease_id:
            raise ValueError("No active lease to renew.")

        headers = {"X-Vault-Token": self.vault_token}
        url = f"{VAULT_ADDR}/v1/sys/leases/renew"
        payload = {"lease_id": self.lease_id, "increment": increment_seconds}
        resp = requests.put(url, headers=headers, json=payload, timeout=5)

        if resp.status_code != 200:
            raise RuntimeError(f"Lease renewal failed: {resp.text}")

        data = resp.json()
        self.lease_duration = data.get("lease_duration", self.lease_duration)
        self.lease_expires_at = time.time() + self.lease_duration
        if self.current_creds:
            self.current_creds["lease_duration"] = self.lease_duration
            self.current_creds["expires_in_seconds"] = self.lease_duration
        return data

    def revoke_current_lease(self) -> Dict[str, Any]:
        """Explicitly revoke the lease, triggering Vault to drop the temporary DB user immediately."""
        if not self.lease_id:
            return {"status": "no_active_lease"}

        target_lease = self.lease_id
        headers = {"X-Vault-Token": self.vault_token}
        url = f"{VAULT_ADDR}/v1/sys/leases/revoke"
        resp = requests.put(url, headers=headers, json={"lease_id": target_lease}, timeout=5)

        # Invalidate internal state
        self.current_creds = None
        self.lease_id = None
        self.lease_expires_at = 0

        if resp.status_code not in (200, 204):
            raise RuntimeError(f"Lease revocation failed: {resp.text}")

        logger.info(f"Successfully revoked lease '{target_lease}'. Database user dropped.")
        return {"status": "revoked", "lease_id": target_lease}


secret_manager = DynamicSecretManager()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Authenticate
    try:
        secret_manager.authenticate_approle()
    except Exception as exc:
        logger.warning(f"Could not initialize AppRole on startup: {exc}")
    yield
    # Shutdown
    logger.info("Shutting down payment microservice.")

app = FastAPI(
    title="Cloud Payment Service - Dynamic Secret Injection PoC",
    description="Microservice demonstrating ephemeral on-demand credentials via HashiCorp Vault.",
    version="1.0.0",
    lifespan=lifespan
)

# Request Models
class PaymentRequest(BaseModel):
    account_id: int = Field(default=1, description="Account ID for payment")
    amount: float = Field(default=49.99, gt=0, description="Payment amount")
    currency: str = Field(default="USD", max_length=3)

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "payment-microservice", "vault_addr": VAULT_ADDR}

@app.get("/credentials/current")
def get_current_credentials():
    """Inspect current active ephemeral credentials and remaining TTL."""
    try:
        creds = secret_manager.get_dynamic_db_credentials()
        remaining = max(0.0, round(secret_manager.lease_expires_at - time.time(), 1))
        return {
            "ephemeral_username": creds["username"],
            "lease_id": creds["lease_id"],
            "lease_duration_seconds": creds["lease_duration"],
            "seconds_until_expiry": remaining,
            "expired": remaining <= 0
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))

@app.post("/payments/process")
def process_payment(req: PaymentRequest):
    """
    Demonstrates business transaction execution using dynamic database credentials.
    1. Fetches ephemeral credential from Vault.
    2. Connects to PostgreSQL as dynamic user.
    3. Verifies account balance and registers payment transaction.
    """
    try:
        creds = secret_manager.get_dynamic_db_credentials()
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Dynamic credential failure: {exc}")

    db_user = creds["username"]
    db_pass = creds["password"]
    tx_ref = f"PAY-{uuid.uuid4().hex[:12].upper()}"

    # Connect to PostgreSQL using ephemeral dynamic user
    try:
        conn = pg8000.native.Connection(
            user=db_user,
            password=db_pass,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            timeout=5
        )
    except Exception as db_err:
        logger.error(f"Database connection failed with dynamic user '{db_user}': {db_err}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Database authentication failure using ephemeral user '{db_user}': {db_err}"
        )

    try:
        # 1. Read account balance (Least privilege SELECT allowed)
        account_rows = conn.run(
            "SELECT customer_name, balance FROM accounts WHERE account_id = :acc_id",
            acc_id=req.account_id
        )
        if not account_rows:
            raise HTTPException(status_code=404, detail=f"Account {req.account_id} not found.")

        customer_name, current_balance = account_rows[0]

        # 2. Insert transaction record (Least privilege INSERT allowed)
        conn.run(
            """
            INSERT INTO payment_transactions (account_id, amount, currency, status, transaction_ref, processed_by_role)
            VALUES (:acc_id, :amt, :curr, 'COMPLETED', :ref, :role)
            """,
            acc_id=req.account_id,
            amt=req.amount,
            curr=req.currency,
            ref=tx_ref,
            role=db_user
        )

        return {
            "status": "SUCCESS",
            "transaction_reference": tx_ref,
            "account_id": req.account_id,
            "customer_name": customer_name,
            "amount": req.amount,
            "currency": req.currency,
            "security_context": {
                "dynamic_db_user": db_user,
                "lease_id": creds["lease_id"],
                "lease_duration": creds["lease_duration"],
                "least_privilege_enforced": True
            }
        }
    finally:
        conn.close()

@app.post("/credentials/renew")
def renew_credentials(increment_seconds: int = 120):
    """Renew the active dynamic credentials lease."""
    try:
        res = secret_manager.renew_lease(increment_seconds)
        return {"status": "renewed", "details": res}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))

@app.post("/credentials/revoke")
def revoke_credentials():
    """
    Simulate manual revocation or incident response.
    Drops the temporary user from the database immediately.
    """
    try:
        res = secret_manager.revoke_current_lease()
        return res
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
