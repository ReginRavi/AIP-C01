#!/usr/bin/env python3
"""
Vault Bootstrap & Provisioner Engine Setup
Automates setup of HashiCorp Vault for Automated Cloud Provisioning:
1. Mounts & configures KV v2 secrets engine
2. Mounts & configures AppRole authentication
3. Writes least-privilege ACL policy for Rundeck
4. Creates AppRole credentials (role_id & secret_id)
5. Mounts & configures AWS Secrets Engine (targeting LocalStack or real AWS)
6. Configures dynamic IAM role 'cloud-provisioner-role' with short TTL
"""

import os
import sys
import json
import time
import requests

VAULT_ADDR = os.getenv("VAULT_ADDR", "http://127.0.0.1:8210")
VAULT_TOKEN = os.getenv("VAULT_TOKEN", "root")
AWS_ENDPOINT = os.getenv("AWS_ENDPOINT", "http://localstack:5000")
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID", "test")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "test")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

HEADERS = {
    "X-Vault-Token": VAULT_TOKEN,
    "Content-Type": "application/json"
}

def log(msg: str):
    print(f"[Vault-Setup] {msg}")

def wait_for_vault(max_retries: int = 30, delay: int = 2):
    log(f"Checking Vault readiness at {VAULT_ADDR}...")
    for i in range(max_retries):
        try:
            r = requests.get(f"{VAULT_ADDR}/v1/sys/health", timeout=3)
            if r.status_code in [200, 429]:  # 200 = active, 429 = standby
                log("Vault is online and ready!")
                return True
        except Exception:
            pass
        time.sleep(delay)
    raise RuntimeError(f"Vault did not become healthy after {max_retries * delay}s")

def enable_secrets_engine(path: str, engine_type: str, options: dict = None):
    url = f"{VAULT_ADDR}/v1/sys/mounts/{path}"
    payload = {"type": engine_type}
    if options:
        payload["options"] = options
    
    # Check if already mounted
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 200:
        log(f"Engine '{path}' already mounted ({engine_type}).")
        return
    
    r = requests.post(url, headers=HEADERS, json=payload)
    if r.status_code in [200, 204]:
        log(f"Successfully mounted '{path}' engine ({engine_type}).")
    else:
        log(f"Note on mounting '{path}': {r.status_code} - {r.text}")

def enable_auth_method(path: str, auth_type: str):
    url = f"{VAULT_ADDR}/v1/sys/auth/{path}"
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 200:
        log(f"Auth method '{path}' already enabled.")
        return
    
    r = requests.post(url, headers=HEADERS, json={"type": auth_type})
    if r.status_code in [200, 204]:
        log(f"Successfully enabled auth method '{path}' ({auth_type}).")
    else:
        log(f"Note on enabling auth '{path}': {r.status_code} - {r.text}")

def configure_kv_v2():
    log("Configuring KV v2 static configurations...")
    enable_secrets_engine("secret", "kv", options={"version": "2"})
    
    # Write static configuration
    config_url = f"{VAULT_ADDR}/v1/secret/data/cloud/config"
    data = {
        "data": {
            "environment": "localstack-poc",
            "region": AWS_REGION,
            "project": "cpits-2024-provisioning",
            "bucket_prefix": "cpits-poc-bucket",
            "orchestrator": "rundeck-ansible"
        }
    }
    r = requests.post(config_url, headers=HEADERS, json=data)
    if r.status_code in [200, 204]:
        log("Wrote static cloud config to 'secret/data/cloud/config'.")
    else:
        log(f"Error writing KV config: {r.status_code} - {r.text}")

def configure_policy_and_approle():
    log("Setting up ACL policy and AppRole for Rundeck...")
    enable_auth_method("approle", "approle")
    
    # Policy content
    script_dir = os.path.dirname(os.path.abspath(__file__))
    policy_path = os.path.join(script_dir, "..", "policies", "rundeck-provisioner.hcl")
    if os.path.exists(policy_path):
        with open(policy_path, "r", encoding="utf-8") as f:
            policy_rules = f.read()
    else:
        policy_rules = """
        path "secret/data/cloud/config" { capabilities = ["read"] }
        path "aws/creds/cloud-provisioner-role" { capabilities = ["read"] }
        path "sys/leases/*" { capabilities = ["update", "read"] }
        """
    
    # Upload policy
    policy_url = f"{VAULT_ADDR}/v1/sys/policies/acl/rundeck-provisioner"
    r = requests.put(policy_url, headers=HEADERS, json={"policy": policy_rules})
    if r.status_code in [200, 204]:
        log("Policy 'rundeck-provisioner' saved successfully.")
    
    # Configure AppRole
    approle_url = f"{VAULT_ADDR}/v1/auth/approle/role/rundeck-provisioner"
    approle_payload = {
        "token_policies": ["rundeck-provisioner"],
        "token_ttl": "1h",
        "token_max_ttl": "4h",
        "secret_id_ttl": "24h"
    }
    requests.post(approle_url, headers=HEADERS, json=approle_payload)
    
    # Fetch Role ID
    r_id = requests.get(f"{approle_url}/role-id", headers=HEADERS).json()["data"]["role_id"]
    
    # Generate Secret ID
    s_id = requests.post(f"{approle_url}/secret-id", headers=HEADERS).json()["data"]["secret_id"]
    
    log(f"AppRole generated successfully! RoleID: {r_id}")
    return r_id, s_id

def configure_aws_engine():
    log("Configuring AWS dynamic secrets engine...")
    enable_secrets_engine("aws", "aws")
    
    # Root credentials configuration pointing to LocalStack / Moto
    root_cfg_url = f"{VAULT_ADDR}/v1/aws/config/root"
    root_payload = {
        "access_key": AWS_ACCESS_KEY,
        "secret_key": AWS_SECRET_KEY,
        "region": AWS_REGION
    }
    # If using custom endpoint (LocalStack / Moto)
    if AWS_ENDPOINT:
        root_payload["endpoint"] = AWS_ENDPOINT
        root_payload["iam_endpoint"] = AWS_ENDPOINT
        root_payload["sts_endpoint"] = AWS_ENDPOINT
    
    r = requests.post(root_cfg_url, headers=HEADERS, json=root_payload)
    if r.status_code in [200, 204]:
        log(f"Configured AWS root credentials with endpoint '{AWS_ENDPOINT}'.")
    else:
        log(f"Warning setting AWS root: {r.status_code} - {r.text}")
    
    # Configure Role for dynamic IAM credentials
    role_url = f"{VAULT_ADDR}/v1/aws/roles/cloud-provisioner-role"
    policy_doc = json.dumps({
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:*",
                    "ec2:Describe*",
                    "ec2:RunInstances",
                    "ec2:TerminateInstances"
                ],
                "Resource": "*"
            }
        ]
    })
    
    role_payload = {
        "credential_type": "iam_user",
        "policy_document": policy_doc,
        "default_ttl": "300s",
        "max_ttl": "900s"
    }
    
    r = requests.post(role_url, headers=HEADERS, json=role_payload)
    if r.status_code in [200, 204]:
        log("Configured AWS dynamic role 'cloud-provisioner-role' (TTL: 300s).")
    else:
        log(f"Error configuring AWS role: {r.status_code} - {r.text}")

def main():
    wait_for_vault()
    configure_kv_v2()
    role_id, secret_id = configure_policy_and_approle()
    configure_aws_engine()
    
    bootstrap_info = {
        "vault_addr": VAULT_ADDR,
        "role_id": role_id,
        "secret_id": secret_id,
        "aws_role": "cloud-provisioner-role",
        "configured_at": time.time()
    }
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    out_file = os.path.join(script_dir, "..", "vault_bootstrap.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(bootstrap_info, f, indent=2)
    
    log(f"Setup complete! Bootstrap parameters saved to {out_file}")

if __name__ == "__main__":
    main()
