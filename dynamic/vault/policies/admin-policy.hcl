# Security Administrator Policy
# Enables database secrets engine, configures connections, and defines role mappings

path "database/config/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}

path "database/roles/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}

path "database/rotate-root/*" {
  capabilities = ["update"]
}

path "sys/leases/*" {
  capabilities = ["create", "read", "update", "delete", "list", "sudo"]
}

path "sys/audit*" {
  capabilities = ["create", "read", "update", "delete", "list", "sudo"]
}
