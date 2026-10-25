storage "file" {
  path = "/vault/data"
}

listener "tcp" {
  address     = "0.0.0.0:8200"
  tls_disable = 1
}

# ------------------------------------------------------------------------------
# Transit Auto-Unseal Block
# ------------------------------------------------------------------------------
seal "transit" {
  address            = "http://vault-transit:8200"
  token              = "transit-autounseal-token"
  disable_renewal    = "false"
  key_name           = "autounseal"
  mount_path         = "transit/"
  tls_skip_verify    = "true"
}

ui = true
disable_mlock = true
api_addr = "http://127.0.0.1:8220"
