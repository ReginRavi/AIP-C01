-- Database initialization for Dynamic Secret Injection PoC
-- Note: PostgreSQL entrypoint already connects to the database defined in POSTGRES_DB (ecommerce_db)

-- Create sample business tables
CREATE TABLE IF NOT EXISTS accounts (
    account_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    balance NUMERIC(12, 2) DEFAULT 0.00,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS payment_transactions (
    transaction_id SERIAL PRIMARY KEY,
    account_id INT REFERENCES accounts(account_id),
    amount NUMERIC(12, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    status VARCHAR(20) NOT NULL,
    transaction_ref VARCHAR(64) UNIQUE NOT NULL,
    processed_by_role VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Seed initial test data
INSERT INTO accounts (customer_name, email, balance) VALUES
('Alice Johnson', 'alice.j@example.com', 2500.00),
('Bob Smith', 'bob.smith@example.com', 4850.50),
('Charlie Brown', 'charlie@example.com', 120.00)
ON CONFLICT (email) DO NOTHING;

-- Create dedicated administrative user for HashiCorp Vault with privileges to create and drop temporary roles
-- In production, Vault root rotation ensures even this password is immediately rotated out.
DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'vaultadmin') THEN
        CREATE ROLE vaultadmin WITH LOGIN SUPERUSER PASSWORD 'VaultAdminInitialSecurePass123!';
    END IF;
END
$$;

-- Grant required permissions
GRANT ALL PRIVILEGES ON DATABASE ecommerce_db TO vaultadmin;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO vaultadmin;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO vaultadmin;
