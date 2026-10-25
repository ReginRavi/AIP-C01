# PowerShell orchestrator to launch Vault Transit Auto-Unseal lab
$ErrorActionPreference = "Stop"

Write-Host "`n=== Launching HashiCorp Vault Transit Auto-Unseal Lab ===" -ForegroundColor Cyan

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

Write-Host "Starting Docker containers..." -ForegroundColor Yellow
docker compose up -d

Write-Host "`nWaiting for containers to initialize..." -ForegroundColor Yellow
Start-Sleep -Seconds 5

Write-Host "`nRunning verification test..." -ForegroundColor Green
python test_autounseal.py
