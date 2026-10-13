# Least-Privilege Policy for Rundeck Cloud Provisioning Orchestrator
# CPITS-II 2024 Reference: Martseniuk et al.

# 1. Read static configuration from KV v2 engine
path "secret/data/cloud/config" {
  capabilities = ["read"]
}

# 2. Generate dynamic AWS credentials for cloud provisioning
path "aws/creds/cloud-provisioner-role" {
  capabilities = ["read"]
}

# 3. Lease management: inspect, renew, or revoke credentials post-job
path "sys/leases/renew" {
  capabilities = ["update"]
}

path "sys/leases/revoke" {
  capabilities = ["update"]
}

path "sys/leases/lookup" {
  capabilities = ["update"]
}
