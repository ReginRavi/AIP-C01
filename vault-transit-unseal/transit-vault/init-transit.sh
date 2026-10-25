#!/bin/sh
set -e

echo "[Transit Init] Waiting for Transit Vault to be ready..."
until vault status > /dev/null 2>&1; do
  echo "  Waiting for Transit Vault API..."
  sleep 1
done

echo "[Transit Init] Enabling Transit secrets engine..."
vault secrets enable transit || echo "Transit engine already enabled."

echo "[Transit Init] Creating transit key 'autounseal'..."
vault write -f transit/keys/autounseal || echo "Transit key already exists."

echo "[Transit Init] Creating autounseal policy..."
cat <<EOF > /tmp/autounseal-policy.hcl
path "transit/encrypt/autounseal" {
   capabilities = [ "update" ]
}

path "transit/decrypt/autounseal" {
   capabilities = [ "update" ]
}
EOF

vault policy write autounseal /tmp/autounseal-policy.hcl

echo "[Transit Init] Creating dedicated periodic token for Target Vault..."
vault token create \
  -id="transit-autounseal-token" \
  -policy="autounseal" \
  -period="720h" \
  -orphan \
  -display-name="target-vault-autounseal" || echo "Token already exists or regenerated."

echo "[Transit Init] Transit Auto-Unseal Key & Policy successfully configured!"
