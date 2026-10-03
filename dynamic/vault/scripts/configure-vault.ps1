<#
.SYNOPSIS
    Configures HashiCorp Vault on Windows for Dynamic Secret Injection with PostgreSQL.
#>
param(
    [string]$VaultAddr = "http://127.0.0.1:8200",
    [string]$VaultToken = "root",
    [string]$DbHost = "127.0.0.1",
    [int]$DbPort = 5432,
    [string]$DbName = "ecommerce_db"
)

$ErrorActionPreference = "Stop"

$env:VAULT_ADDR = $VaultAddr
$env:VAULT_TOKEN = $VaultToken

Write-Host "[*] Checking Vault connection at $VaultAddr..." -ForegroundColor Cyan
vault status

Write-Host "[1/5] Enabling database secrets engine..." -ForegroundColor Cyan
try { vault secrets enable database } catch { Write-Host "Database engine may already be enabled." }

Write-Host "[2/5] Configuring database connection..." -ForegroundColor Cyan
vault write database/config/ecommerce-postgres `
    plugin_name="postgresql-database-plugin" `
    allowed_roles="payment-service-role" `
    connection_url="postgresql://{{username}}:{{password}}@$($DbHost):$($DbPort)/$($DbName)?sslmode=disable" `
    username="vaultadmin" `
    password="VaultAdminInitialSecurePass123!"

Write-Host "[3/5] Rotating root administrative credentials..." -ForegroundColor Cyan
vault write -force database/rotate-root/ecommerce-postgres

Write-Host "[4/5] Creating dynamic database role 'payment-service-role'..." -ForegroundColor Cyan
vault write database/roles/payment-service-role `
    db_name="ecommerce-postgres" `
    creation_statements="CREATE ROLE ""{{name}}"" WITH LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}' INHERIT; GRANT CONNECT ON DATABASE $DbName TO ""{{name}}""; GRANT USAGE ON SCHEMA public TO ""{{name}}""; GRANT SELECT ON accounts TO ""{{name}}""; GRANT SELECT, INSERT ON payment_transactions TO ""{{name}}""; GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO ""{{name}}"";" `
    revocation_statements="SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE usename = '{{name}}'; REASSIGN OWNED BY ""{{name}}"" TO postgres; DROP OWNED BY ""{{name}}""; DROP ROLE IF EXISTS ""{{name}}"";" `
    default_ttl="2m" `
    max_ttl="10m"

Write-Host "[5/5] Configuring AppRole and Least-Privilege Policies..." -ForegroundColor Cyan
$policyPath = Join-Path $PSScriptRoot "..\policies\payment-service-policy.hcl"
vault policy write payment-service $policyPath

try { vault auth enable approle } catch { Write-Host "AppRole auth method already enabled." }
vault write auth/approle/role/payment-service `
    token_policies="payment-service" `
    token_ttl="1h" `
    token_max_ttl="4h"

$roleId = vault read -field=role_id auth/approle/role/payment-service/role-id
$secretId = vault write -force -field=secret_id auth/approle/role/payment-service/secret-id

Write-Host "`n========================================================" -ForegroundColor Green
Write-Host " [SUCCESS] Vault Dynamic Database Secrets Configured!" -ForegroundColor Green
Write-Host " Role ID:   $roleId" -ForegroundColor Yellow
Write-Host " Secret ID: $secretId" -ForegroundColor Yellow
Write-Host " Dynamic Endpoint: database/creds/payment-service-role" -ForegroundColor Yellow
Write-Host "========================================================`n" -ForegroundColor Green
