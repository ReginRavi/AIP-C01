import requests

url = "http://127.0.0.1:8200/v1/database/roles/payment-service-role"
headers = {"X-Vault-Token": "root"}
payload = {
    "db_name": "ecommerce-postgres",
    "creation_statements": [
        'CREATE ROLE "{{name}}" WITH LOGIN PASSWORD \'{{password}}\' VALID UNTIL \'{{expiration}}\' INHERIT;',
        'GRANT CONNECT ON DATABASE ecommerce_db TO "{{name}}";',
        'GRANT USAGE ON SCHEMA public TO "{{name}}";',
        'GRANT SELECT ON accounts TO "{{name}}";',
        'GRANT SELECT, INSERT ON payment_transactions TO "{{name}}";',
        'GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO "{{name}}";'
    ],
    "revocation_statements": [
        "SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE usename = '{{name}}';",
        'REASSIGN OWNED BY "{{name}}" TO postgres;',
        'DROP OWNED BY "{{name}}";',
        'DROP ROLE IF EXISTS "{{name}}";'
    ],
    "default_ttl": "2m",
    "max_ttl": "10m"
}

resp = requests.post(url, headers=headers, json=payload, timeout=5)
print("Role update status:", resp.status_code, resp.text or "SUCCESS")
