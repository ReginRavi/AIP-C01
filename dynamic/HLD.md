# High-Level Design (HLD): Dynamic Secret Injection for Microservices in Cloud Environments

> [!NOTE]
> This High-Level Design (HLD) specifies the system architecture, component interactions, threat models, and operational frameworks for **Dynamic Secret Injection** in cloud-native microservice architectures. It integrates **HashiCorp Vault**, **Kubernetes Workload Attestation**, **PostgreSQL Target Data Stores**, and an **Unsupervised AI/ML Anomaly Defense Subsystem**.

---

## 1. Executive Summary & Problem Context

In traditional distributed environments, application microservices rely on **static, long-lived credentials** (API tokens, database credentials, TLS certificates) provisioned via environment variables, Kubernetes ConfigMaps, or static secret vaults. This paradigm introduces critical security vulnerabilities:
1. **Unbounded Blast Radius:** Compromised static credentials remain valid indefinitely until manual administrative intervention.
2. **Secret Sprawl:** Secrets leak into build logs, source control repositories, container images, and monitoring dumps.
3. **Operational Overhead:** Rotating static database credentials requires coordinated microservice restarts and risks application downtime.

### The Solution: Dynamic Secret Injection
This architecture replaces static secrets with **short-lived, ephemeral, on-demand credentials** generated dynamically at runtime:
* Credentials have strict, deterministic **Time-To-Live (TTL)** limits (e.g., 2 minutes to 1 hour).
* Every secret is cryptographically tied to a tracked **Lease ID**.
* Access enforces the **Principle of Least Privilege (PoLP)** via fine-grained role templates.
* Expired or anomalous credentials are **automatically and immediately dropped** from the target database without human intervention.

---

## 2. High-Level System Architecture

```mermaid
flowchart TD
    subgraph K8sCluster ["1. Cloud Kubernetes Cluster / Workload Infrastructure"]
        subgraph AppPod ["Microservice Pod (e.g., Payment Gateway)"]
            App["Application Container\n(FastAPI / Python Runtime)"]
            Sidecar["Vault Agent Injector Sidecar\n(Runs alongside App)"]
            TmpFs[("In-Memory Volume\n/vault/secrets (tmpfs)")]
            
            App <-->|"Reads in-memory credentials"| TmpFs
            Sidecar -->|"Injects & updates credentials"| TmpFs
        end
        
        K8sAPI["Kubernetes API Server\n(TokenReview & Admission Webhook)"]
        K8sSA["Kubernetes ServiceAccount\n(payment-service-sa)"]
        Sidecar -.->|"Presents projected SA JWT"| K8sAPI
    end

    subgraph VaultControlPlane ["2. Centralized Security Control Plane (HashiCorp Vault HA)"]
        subgraph CoreSubsystems ["Vault Core Services"]
            AuthMethod["Auth Engines\n• /auth/kubernetes\n• /auth/approle"]
            PolicyEngine["Policy & Token Engine\n(Granular ACL Enforcer)"]
            DBSecretsEngine["Database Secrets Engine\n(postgresql-database-plugin)"]
            LeaseManager["Lease & Revocation Manager\n(Active Lease Table & Expiration Timer)"]
            AuditBroker["Audit Broker (/sys/audit)\n(HMAC-Masked Event Logger)"]
        end
        
        StorageRaft[("Integrated Raft HA Storage\n(Encrypted Consensus Logs)")]
        CoreSubsystems <--> StorageRaft
    end

    subgraph DataTier ["3. Managed Target Data Stores"]
        PostgresDB[("PostgreSQL 16 Engine\n(ecommerce_db)\n• accounts\n• payment_transactions")]
        PostgresCatalog["PostgreSQL Internal Catalog\n(pg_roles, pg_authid, pg_stat_activity)"]
        PostgresDB --- PostgresCatalog
    end

    subgraph AIObservabilityTier ["4. AI/ML Observability & SOAR Remediation"]
        LogShipper["Audit Stream Collector\n(Fluentbit / Filebeat)"]
        MLAnomalyEngine["Unsupervised ML Anomaly Detector\n(Isolation Forest Engine)"]
        SOARDispatcher["Automated Incident Response\n(SOAR Controller)"]
        
        AuditBroker -->|"Encrypted Audit Log"| LogShipper
        LogShipper -->|"Structured Telemetry"| MLAnomalyEngine
        MLAnomalyEngine -->|"Anomaly Flag / Score"| SOARDispatcher
    end

    %% High-level Interaction Paths
    Sidecar -->|"1. Authenticate with SA JWT"| AuthMethod
    AuthMethod -->|"2. Verify JWT with TokenReview"| K8sAPI
    AuthMethod -->|"3. Issue Short-Lived Vault Client Token"| Sidecar
    Sidecar -->|"4. Request Credentials (database/creds/payment-service-role)"| DBSecretsEngine
    DBSecretsEngine -->|"5. Connect as Root & Execute CREATE ROLE"| PostgresDB
    DBSecretsEngine -->|"6. Return Ephemeral User, Password & Lease ID"| Sidecar
    App -->|"7. Execute Business Transactions with Dynamic User"| PostgresDB
    
    %% Lifecycle / Remediation Paths
    LeaseManager -.->|"TTL Expired: Execute DROP ROLE"| PostgresDB
    SOARDispatcher -.->|"Trigger Emergency Revocation (/v1/sys/leases/revoke)"| LeaseManager
```

---

## 3. Core Architectural Subsystems

### 3.1 Workload Identity & Attestation Subsystem
* **Zero Secret Zero:** The microservice starts with **no embedded secrets**, certificates, or passwords.
* **Kubernetes Projected Tokens:** Authentication leverages short-lived Kubernetes Service Account OIDC tokens mounted directly by the kubelet into the pod.
* **TokenReview Verification:** Vault validates the ServiceAccount JWT against the Kubernetes API Server TokenReview API (`/apis/authentication.k8s.io/v1/tokenreviews`), confirming pod namespace, service account name, and pod UID before issuing a Vault token.

### 3.2 Vault Dynamic Database Secrets Engine
* Acts as an authenticated proxy and database role provisioning broker.
* Connects to target database instances (PostgreSQL, MySQL, Oracle, MongoDB) using dedicated administrative credentials.
* **Root Password Rotation (`rotate-root`):** Upon initial setup, Vault randomizes the root database administrator password. The password is never stored in human-accessible vaults, effectively eliminating administrative compromise vectors.
* **Role Templating:** Generates transient usernames matching pattern:
  $$\text{Username} = \text{v-token-} + \text{RoleName} + \text{-RandomHash-} + \text{Timestamp}$$

### 3.3 Sidecar Injection & Memory Safety
* **Vault Agent Injector:** Operates as a Mutating Admission Webhook controller in Kubernetes.
* **Sidecar Deployment:** Automatically injects `vault-agent` alongside the application container in target pods based on pod annotations (`vault.hashicorp.com/agent-inject: "true"`).
* **In-Memory `tmpfs` IPC:** The agent fetches dynamic credentials and writes them to an in-memory `tmpfs` volume shared only within the pod boundaries. Secrets are **never written to disk or container storage layers**.
* **Automatic Renewal:** The agent proactively renews active leases at half the lease duration ($T_{\text{renew}} = \frac{1}{2} \text{TTL}$).

### 3.4 AI/ML Anomaly Detection & SOAR Remediation
* Implements an automated feedback loop between security monitoring and active credential control.
* **Telemetry Source:** Vault audit broker logs (`/sys/audit/file`), capturing all authentication, credential requests, lease renewals, and revocation attempts.
* **Machine Learning Pipeline:** An unsupervised `IsolationForest` model evaluates rolling 60-second telemetry windows against a trained baseline.
* **Autonomous SOAR Intervention:** When an anomaly score indicates credential abuse or mass exfiltration, the system triggers real-time lease revocation (`/v1/sys/leases/revoke`), dropping active database connections in $< 350\text{ ms}$.

---

## 4. End-to-End Dynamic Credential Lifecycle

```mermaid
sequenceDiagram
    autonumber
    participant App as Microservice Container
    participant Sidecar as Vault Agent Injector
    participant Vault as Vault Core Server
    participant K8s as Kubernetes API Server
    participant DB as PostgreSQL Database
    participant AI as AI Anomaly Engine

    Note over App, DB: Phase 1: Workload Identity & Dynamic Generation
    Sidecar->>K8s: Retrieve projected ServiceAccount token
    Sidecar->>Vault: Authenticate: POST /v1/auth/kubernetes/login
    Vault->>K8s: TokenReview validation of SA token
    K8s-->>Vault: Validation OK (ServiceAccount: payment-service-sa)
    Vault-->>Sidecar: Return Vault Client Token (Scoped via payment-service-policy)
    
    Sidecar->>Vault: GET /v1/database/creds/payment-service-role
    Vault->>DB: Execute creation_statements (CREATE ROLE ... VALID UNTIL ...)
    DB-->>Vault: Ephemeral role created
    Vault-->>Sidecar: Return {username, password, lease_id, lease_duration: 120s}
    Sidecar->>Sidecar: Write credentials to in-memory /vault/secrets/db-creds

    Note over App, DB: Phase 2: Microservice Business Execution
    App->>App: Read /vault/secrets/db-creds
    App->>DB: Connect as dynamic user (e.g., v-token-payment-...)
    App->>DB: Execute SELECT/INSERT on accounts & payment_transactions
    DB-->>App: Query results returned

    Note over App, AI: Phase 3: Lease Lifecycle & Anomaly Monitoring
    Vault->>AI: Stream audit log event (Request logged)
    AI->>AI: Evaluate telemetry window against Isolation Forest baseline
    
    alt Normal Operation (Lease Renewal)
        Sidecar->>Vault: PUT /v1/sys/leases/renew (at TTL / 2)
        Vault-->>Sidecar: Lease renewed for additional duration
    else Exfiltration Anomaly Detected (SOAR Intervention)
        AI->>Vault: POST /v1/sys/leases/revoke (Target Lease ID)
        Vault->>DB: Execute revocation_statements (REASSIGN OWNED, DROP OWNED, DROP ROLE)
        DB-->>Vault: Ephemeral user eliminated
        Note over DB: Active connections terminated. Attacker credential access severed!
    end
```

---

## 5. Security & Threat Modeling (STRIDE Analysis)

| Threat Category | Attack Vector | Mitigation in Dynamic Secret Architecture |
| :--- | :--- | :--- |
| **Spoofing** | Compromised pod masquerading as payment service | Kubelet-projected ServiceAccount token validation via Kubernetes TokenReview API prevents arbitrary workload identity spoofing. |
| **Tampering** | Modifying database credentials in transit or rest | Mutual TLS (mTLS) across all Vault and database channels; credentials stored strictly in non-persistent `tmpfs` RAM. |
| **Repudiation** | Denying who performed database mutations | Vault audit device logs every dynamic credential generation, linking the exact ephemeral user to the Vault token and pod identity. |
| **Information Disclosure** | Secret leakage via container image or Git repo | Elimination of static credentials. Ephemeral usernames expire within minutes; zero hardcoded secrets exist in repository or images. |
| **Denial of Service** | Exhausting database connections via credential spam | Vault role limits (`max_ttl`, connection pooling constraints) and AI Anomaly Detector rate-limiting rogue requesting pods. |
| **Elevation of Privilege** | Compromised microservice attempting DB drop/alter | Strict Least-Privilege creation statements: dynamic role is only granted `SELECT, INSERT` on specific tables and cannot alter schema. |

---

## 6. Non-Functional Requirements (NFRs) & Resilience

```mermaid
graph LR
    subgraph Reliability ["High Availability (HA)"]
        Raft["3 or 5 Node Raft Quorum\nAutomatic Leader Election\nSub-second Failover"]
    end
    
    subgraph Latency ["Latency & Performance"]
        Cache["In-Memory tmpfs Caching\nLease Pre-fetching\nConnection Pooling"]
    end
    
    subgraph Observability ["Telemetry & Compliance"]
        Audit["JSON Audit Log Broker\nPCI DSS & SOC2 Ephemeral Audit Trail\nPrometheus Metrics (/v1/sys/metrics)"]
    end
```

* **Availability Target:** 99.99% uptime via multi-node Vault cluster operating Integrated Raft Consensus Storage across multiple cloud availability zones.
* **Latency Overhead:** Secret acquisition occurs out-of-band via the background Vault Agent sidecar; application database transactions experience **0 ms additional network latency** during query execution.
* **Compliance Posture:** Satisfies PCI-DSS 4.0 Requirement 8.3 (strong authentication and ephemeral privilege control) and NIST SP 800-207 Zero-Trust Architecture guidelines.
