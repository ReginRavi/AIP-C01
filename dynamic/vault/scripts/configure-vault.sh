#!/usr/bin/env bash
# ==============================================================================
# Script: configure-vault.sh
# Purpose: Automated initialization and configuration of HashiCorp Vault
#          for dynamic PostgreSQL secret injection in microservices.
# ==============================================================================

set -euo pipefail

VAULT_ADDR="${VAULT_ADDR:-http://127.0.0.1:8200}"
VAULT_TOKEN="${VAULT_TOKEN:-root}"
DB_HOST="${DB_HOST:-postgres}"
DB_PORT="${DB_PORT:-5432}"
DB_NAME="${DB_NAME:-ecommerce_db}"

echo "[*] Connecting to HashiCorp Vault at $VAULT_ADDR..."
export VAULT_ADDR
export VAULT_TOKEN

# 1. Enable audit device for security logging and AI anomaly detection
echo "[1/6] Enabling Vault audit logging device..."
vault audit enable file file_path=/vault/logs/vault_audit.log || echo "Audit log already enabled."

# 2. Enable database secrets engine
echo "[2/6] Enabling database secrets engine..."
vault secrets enable database || echo "Database secrets engine already enabled."

# 3. Configure PostgreSQL connection endpoint
echo "[3/6] Configuring PostgreSQL connection in Vault..."
vault write database/config/ecommerce-postgres \
    plugin_name="postgresql-database-plugin" \
    allowed_roles="payment-service-role" \
    connection_url="postgresql://{{username}}:{{password}}@${DB_HOST}:${DB_PORT}/${DB_NAME}?sslmode=disable" \
    username="vaultadmin" \
    password="VaultAdminInitialSecurePass123!"

# 4. Rotate root database credentials to establish Zero-Trust
echo "[4/6] Rotating root administrative credentials (Zero-Trust enforcement)..."
vault write -force database/rotate-root/ecommerce-postgres

# 5. Define Dynamic Role with Least-Privilege Creation & Revocation Statements
echo "[5/6] Creating dynamic database role 'payment-service-role'..."
vault write database/roles/payment-service-role \
    db_name="ecommerce-postgres" \
    creation_statements="CREATE ROLE \"{{name}}\" WITH LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}' INHERIT; \
        GRANT CONNECT ON DATABASE ${DB_NAME} TO \"{{name}}\"; \
        GRANT USAGE ON SCHEMA public TO \"{{name}}\"; \
        GRANT SELECT ON accounts TO \"{{name}}\"; \
        GRANT SELECT, INSERT ON payment_transactions TO \"{{name}}\"; \
        GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO \"{{name}}\";" \
    revocation_statements="SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE usename = '{{name}}'; \
        REASSIGN OWNED BY \"{{name}}\" TO postgres; \
        DROP OWNED BY \"{{name}}\"; \
        DROP ROLE IF EXISTS \"{{name}}\";" \
    default_ttl="2m" \
    max_ttl="10m"

# 6. Configure AppRole Authentication for Microservices
echo "[6/6] Configuring AppRole authentication and policies..."
vault policy write payment-service /vault/policies/payment-service-policy.hcl || \
vault policy write payment-service policies/payment-service-policy.hcl

vault auth enable approle || echo "AppRole already enabled."
vault write auth/approle/role/payment-service \
    token_policies="payment-service" \
    token_ttl="1h" \
    token_max_ttl="4h"

ROLE_ID=$(vault read -field=role_id auth/approle/role/payment-service/role-id)
SECRET_ID=$(vault write -force -field=secret_id auth/approle/role/payment-service/secret-id)

echo "======================================================================"
echo " [SUCCESS] Dynamic Secret Injection PoC Initialized!"
echo " Role ID:   $ROLE_ID"
echo " Secret ID: $SECRET_ID"
echo " Dynamic Endpoint: database/creds/payment-service-role"
echo " Default TTL: 2 minutes | Max TTL: 10 minutes"
echo "======================================================================"
