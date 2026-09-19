# Dynamic Database Credentials Workflow

> [!NOTE]
> This sequence illustrates how HashiCorp Vault manages dynamic secrets for a database (such as PostgreSQL), including administrative configuration, root rotation, on-demand credential generation with leases, and automatic/manual revocation.

---

## 1. Sequence Diagram

```mermaid
sequenceDiagram
    autonumber
    actor Admin
    actor Client as Vault Client
    participant Vault
    participant DB as PostgreSQL Database

    %% Configuration Phase
    Note over Admin, DB: Phase 1: Configuration & Role Definition
    Admin->>Vault: Configure DB connection (URL, username, password)
    Admin->>Vault: Define allowed roles (e.g., hcvop-demo-role)
    Admin->>Vault: Create database role with default/max TTLs & creation statements
    
    %% Root Credential Rotation
    Note over Admin, DB: Phase 2: Root Credential Rotation
    Admin->>Vault: Execute database/rotate-root/hcvop-DB
    Vault->>DB: Log in with static credentials & rotate root password
    Note over Vault, DB: Static credentials invalidated.<br/>Only Vault and DB know the new root credentials.

    %% Dynamic Credential Generation
    Note over Client, DB: Phase 3: Dynamic Credential Generation
    Client->>Vault: Request credentials for hcvop-demo-role
    Vault->>DB: Execute SQL creation statements to create user/password
    DB-->>Vault: Temporary database user created
    Vault-->>Client: Return dynamic credentials and Lease ID

    %% Revocation & Cleanup
    Note over Admin, DB: Phase 4: Revocation & Cleanup
    Admin->>Vault: Revoke specific lease ID or all leases via prefix
    Vault->>DB: Delete temporary user account associated with lease(s)
    Note over DB: Temporary access is terminated and cleaned up
```

---

## 2. Process Breakdown

### 1. Configuration Phase
- **Database Engine Setup:** Admin mounts the database secrets engine and configures connection parameters (host, port, initial credentials).
- **Role Definition:** Admin defines role templates specifying SQL statements for user creation, credential renewal, revocation, and TTL limits (`default_ttl`, `max_ttl`).

### 2. Root Credential Rotation (`rotate-root`)
- Vault logs into the database using initial static administrative credentials, randomly generates a new strong password, and updates it on the database.
- Static credentials are invalidated. No human operator retains access to the root database password, eliminating static root credential leakage.

### 3. Dynamic Credential Generation
- Applications/clients authenticate with Vault and request credentials for a role (e.g., `database/creds/hcvop-demo-role`).
- Vault dynamically connects to PostgreSQL, generates a unique ephemeral username/password, and returns them to the client with a **Lease ID**.

### 4. Revocation & Cleanup
- When a lease reaches its TTL without renewal or when an administrator executes a revocation (`vault lease revoke <lease_id>`), Vault runs the cleanup statements on the database to drop the temporary user.

---

## 3. Vault CLI Implementation Code & Line-by-Line Breakdown

### Step 1: Enable the Database Secrets Engine

```bash
vault secrets enable database
```

#### Line-by-Line Explanation:
| Token / Parameter | Explanation |
| :--- | :--- |
| `vault` | Invokes the Vault CLI executable. |
| `secrets enable` | The CLI subcommand instructing Vault to mount and initialize a secrets engine. |
| `database` | The engine type. By default, Vault mounts it at the matching path `database/`. |

---

### Step 2: Configure the Database Connection

```bash
vault write database/config/hcvop-DB \
    plugin_name="postgresql-database-plugin" \
    allowed_roles="hcvop-demo-role" \
    connection_url="postgresql://{{username}}:{{password}}@postgres.service.consul:5432/mydb?sslmode=disable" \
    username="vaultadmin" \
    password="InitialStaticPassword123!"
```

#### Line-by-Line Explanation:
| Line / Parameter | Purpose & Internal Behavior |
| :--- | :--- |
| `vault write database/config/hcvop-DB` | Performs an HTTP POST/PUT write to store configuration for a database connection named `hcvop-DB`. |
| `plugin_name="postgresql-database-plugin"` | Specifies the built-in database driver plugin to use for connecting to PostgreSQL. |
| `allowed_roles="hcvop-demo-role"` | Security boundary: explicitly lists which Vault roles are allowed to generate credentials through this connection. |
| `connection_url="postgresql://{{username}}:{{password}}@..."` | Connection string URI. The `{{username}}` and `{{password}}` templates are dynamically populated by Vault using the values below or rotated credentials. |
| `username="vaultadmin"` | The initial static database administrator account Vault uses to connect and execute user management SQL. |
| `password="InitialStaticPassword123!"` | The initial static password for `vaultadmin`. This will be rotated in Step 4. |

---

### Step 3: Create the Dynamic Database Role

```bash
vault write database/roles/hcvop-demo-role \
    db_name="hcvop-DB" \
    creation_statements="CREATE ROLE \"{{name}}\" WITH LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}'; \
        GRANT SELECT ON ALL TABLES IN SCHEMA public TO \"{{name}}\";" \
    revocation_statements="REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM \"{{name}}\"; \
        DROP ROLE IF EXISTS \"{{name}}\";" \
    default_ttl="1h" \
    max_ttl="24h"
```

#### Line-by-Line Explanation:
| Line / Parameter | Purpose & Internal Behavior |
| :--- | :--- |
| `vault write database/roles/hcvop-demo-role` | Registers a dynamic secrets role named `hcvop-demo-role` under the database secrets engine. |
| `db_name="hcvop-DB"` | Binds this role to the specific database connection configured in Step 2 (`hcvop-DB`). |
| `creation_statements="..."` | Semicolon-delimited SQL commands Vault executes on PostgreSQL whenever credentials are requested. |
| `CREATE ROLE \"{{name}}\" WITH LOGIN...` | Creates a new ephemeral database login user with a temporary password and timestamp expiration. |
| `GRANT SELECT ON ALL TABLES...` | Applies least privilege permissions (read-only queries on the public schema). |
| `revocation_statements="..."` | SQL commands Vault automatically executes on PostgreSQL when the lease expires or is revoked. |
| `REVOKE ALL PRIVILEGES...` | Revokes table permissions to prevent orphaned permissions. |
| `DROP ROLE IF EXISTS \"{{name}}\";` | Permanently deletes the temporary database user account. |
| `default_ttl="1h"` | The initial validity period of issued credentials (1 hour) if not specified by the client. |
| `max_ttl="24h"` | The absolute maximum ceiling for renewals (24 hours). Even with renewals, credentials expire at 24 hours. |

#### Key Template Variables:
| Variable | Description |
| :--- | :--- |
| `{{name}}` | Automatically replaced by Vault with an ephemeral, unique username (e.g., `v-token-hcvop-dem-abc123...`). |
| `{{password}}` | Automatically replaced by Vault with a high-entropy, random password. |
| `{{expiration}}` | Automatically replaced with a formatted timestamp marking lease expiration. |

---

### Step 4: Rotate Root Credentials

```bash
vault write -f database/rotate-root/hcvop-DB
```

#### Line-by-Line Explanation:
| Token / Parameter | Purpose & Internal Behavior |
| :--- | :--- |
| `vault write` | Executes a write operation against the Vault HTTP API. |
| `-f` (force) | Required because this endpoint takes **no request body parameters**. The `-f` flag instructs the CLI to send an empty POST request. |
| `database/rotate-root/hcvop-DB` | Triggers immediate rotation for the admin credentials on connection `hcvop-DB`. Vault generates a random 32+ character password, changes it in PostgreSQL (`ALTER USER vaultadmin WITH PASSWORD '...'`), and updates its own internal storage. |

> [!IMPORTANT]
> Once rotated, **no human operator knows the root password**. The original static password is completely invalidated, preventing backdoor database access.

---

### Step 5: Generate Dynamic Credentials (Client / Application)

```bash
vault read database/creds/hcvop-demo-role
```

#### Line-by-Line Explanation:
| Token / Parameter | Purpose & Internal Behavior |
| :--- | :--- |
| `vault read` | Executes an HTTP GET request to retrieve a dynamic secret. |
| `database/creds/hcvop-demo-role` | Endpoint that triggers Vault to execute the role's `creation_statements` against PostgreSQL and return temporary credentials. |

#### Example Output Breakdown:
```text
Key                Value
---                -----
lease_id           database/creds/hcvop-demo-role/c29tZS1sZWFzZS1pZA
lease_duration     1h
lease_renewable    true
password           A1b2C3d4_E5f6G7h8!
username           v-token-hcvop-dem-o7w3r5t8y2u1-1689234857
```
- **`lease_id`**: The tracking ID used for renewing or revoking this specific set of credentials.
- **`lease_duration`**: Time remaining before automatic revocation occurs (3600 seconds / 1 hour).
- **`lease_renewable`**: `true` indicates the client can request a lease extension up to `max_ttl`.
- **`username` & `password`**: Ephemeral database credentials created directly inside PostgreSQL.

---

### Step 6: Manage Leases (Renew & Revoke)

#### 1. Renewing an Active Lease:
```bash
vault lease renew database/creds/hcvop-demo-role/c29tZS1sZWFzZS1pZA
```
- `vault lease renew`: Subcommand that extends the TTL of an active lease.
- `database/creds/...`: The target lease ID. Extends lifetime by `default_ttl`, bounded by `max_ttl`.

#### 2. Revoking a Single Lease:
```bash
vault lease revoke database/creds/hcvop-demo-role/c29tZS1sZWFzZS1pZA
```
- `vault lease revoke`: Subcommand that terminates a lease ahead of schedule.
- Triggers Vault to run the `revocation_statements` (`DROP ROLE`) immediately on PostgreSQL.

#### 3. Revoking All Leases by Prefix (Incident Response):
```bash
vault lease revoke -prefix database/creds/hcvop-demo-role
```
- `-prefix`: Directs Vault to find **every active lease** matching the path prefix.
- Drops all temporary users created under `hcvop-demo-role` in a single command.

---

## 4. Vault ACL Policies (Least Privilege)

### Client Application Policy (`client-db-policy.hcl`)
```hcl
path "database/creds/hcvop-demo-role" {
  capabilities = ["read"]
}
```
- `path "database/creds/hcvop-demo-role"`: Restricts the application strictly to this dynamic role.
- `capabilities = ["read"]`: Grants permission to generate dynamic credentials; blocks modifying configurations or creating roles.

### Database Admin Policy (`admin-db-policy.hcl`)
```hcl
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
  capabilities = ["read", "update", "delete", "list"]
}
```
- `database/config/*`: Full CRUD permissions on database connections.
- `database/roles/*`: Full CRUD permissions on database roles and creation statements.
- `database/rotate-root/*`: `update` capability required to trigger root rotation.
- `sys/leases/*`: Capabilities to inspect, renew, and revoke active leases.