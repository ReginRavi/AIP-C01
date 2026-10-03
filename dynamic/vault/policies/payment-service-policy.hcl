# Granular Least-Privilege Policy for Payment Microservice
# Grants access ONLY to read ephemeral dynamic database credentials

path "database/creds/payment-service-role" {
  capabilities = ["read"]
}

# Allow service to inspect and renew its own lease
path "sys/leases/renew" {
  capabilities = ["update"]
}

path "sys/leases/lookup" {
  capabilities = ["update"]
}
