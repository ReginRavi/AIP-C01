# REST API vs. WebSocket API Architecture: AWS SAP-C02 & AIP-C01 Exam Guide

> [!NOTE]
> **Core Exam Concept**: In API Gateway, **REST APIs are STATELESS** (independent HTTP request/response cycles), whereas **WebSocket APIs are STATEFUL** (persistent, full-duplex communication connection). Understanding the distinction between **Stateful Communication** and **Stateless Compute** is a frequent requirement on the AWS Solutions Architect Professional (SAP-C02) and AI Practitioner (AIP-C01) exams.

---

## 1. Problem Statement & Exam Scenario Analysis

### The Core Distinctions

```
REST API       ──> Stateless Communication (HTTP)     ──> Request-Response Only
WebSocket API  ──> Stateful Communication (WSS)      ──> Full-Duplex / Bidirectional / Push
```

### Exam Question Matrix: Identifying the Correct Pattern

| Scenario Requirement | Communication Pattern | API Gateway Choice | Statefulness |
| :--- | :--- | :--- | :--- |
| Standard CRUD Operations / Web APIs | Request / Response | REST API / HTTP API | **Stateless** |
| Real-time IoT Sensor Telemetry & Remote Control | Bidirectional Push | WebSocket API | **Stateful** |
| Chat Applications / Live Sports Scores | Server-Initiated Push | WebSocket API | **Stateful** |
| Financial Market Data Feeds | Persistent Streaming | WebSocket API | **Stateful** |

---

## 2. Why REST API is Stateless

REST (Representational State Transfer) relies on standard HTTP/HTTPS protocols where every request is executed independently.

```mermaid
sequenceDiagram
    autonumber
    actor Client
    participant APIGW_REST as API Gateway (REST API)
    participant Backend as AWS Lambda / Backend Service

    Client->>APIGW_REST: 1. HTTP GET /device/123 (Request 1)
    APIGW_REST->>Backend: Invoke Lambda
    Backend-->>APIGW_REST: 200 OK + Payload
    APIGW_REST-->>Client: Response 1 (TCP Connection Closed/Recycled)
    
    Client->>APIGW_REST: 2. HTTP POST /device/123 (Request 2)
    APIGW_REST->>Backend: Invoke Lambda (No memory or state from Request 1)
    Backend-->>APIGW_REST: 200 OK + Confirmation
    APIGW_REST-->>Client: Response 2 (TCP Connection Closed/Recycled)
```

### Key REST Attributes
- Neither API Gateway nor the backend retains connection state between consecutive requests.
- Each request must contain all context (authentication tokens, resource IDs) required to process it.
- **Server Push is impossible without client polling** (e.g., Long Polling / SSE).

---

## 3. Why WebSocket API is Stateful

WebSocket API establishes a persistent, long-lived TCP connection using a `wss://` handshake, enabling **full-duplex, bidirectional communication**.

```mermaid
sequenceDiagram
    autonumber
    actor Client
    participant APIGW_WS as API Gateway (WebSocket API)
    participant Backend as AWS Lambda / Backend Service

    Client->>APIGW_WS: 1. wss:// Connection Handshake ($connect)
    APIGW_WS-->>Client: 101 Switching Protocols (Connection Established: connectionId = abc123)
    
    Client->>APIGW_WS: 2. Send Frame: {"action": "sendData", "temp": 35}
    APIGW_WS->>Backend: Invoke Lambda with connectionId = abc123
    
    Note over Backend,APIGW_WS: Out-of-Band Server Push (No Client Request Needed)
    Backend->>APIGW_WS: 3. PostToConnection (connectionId = abc123, payload = "Cooling Mode")
    APIGW_WS-->>Client: 4. Server Push Frame: {"command": "setMode", "mode": "cooling"}
    
    Client->>APIGW_WS: 5. Disconnect ($disconnect)
```

### Key WebSocket Attributes
- **Persistent Connection**: The TCP socket remains open between client and API Gateway.
- **Connection Identifier**: API Gateway assigns a unique `connectionId` to every active connection.
- **Bi-Directional**: Both client and server can transmit data frames asynchronously at any time.

---

## 4. Crucial Exam Distinction: Stateful Communication vs. Stateless Compute

> [!IMPORTANT]
> **Stateful Communication ≠ Stateful Compute**
> - **Stateful Communication**: API Gateway maintains the persistent WebSocket TCP connection (`connectionId`).
> - **Stateless Compute**: Backend compute services (like AWS Lambda) remain **stateless and horizontally scalable**.
> - **Connection Management**: Connection metadata (`connectionId`, `userId`, `deviceId`) is typically persisted in an external database such as **Amazon DynamoDB**.

### Serverless WebSocket Architecture Pattern

```mermaid
flowchart TD
    subgraph Clients ["Client Layer"]
        Device1["IoT Device A<br/>(connectionId: conn-101)"]
        Device2["IoT Device B<br/>(connectionId: conn-102)"]
    end

    subgraph Gateway ["API Gateway WebSocket API"]
        WS_Route["WebSocket Router"]
        RouteConnect["$connect Route"]
        RouteDisconnect["$disconnect Route"]
        RouteDefault["Custom / $default Route"]

        WS_Route --> RouteConnect
        WS_Route --> RouteDisconnect
        WS_Route --> RouteDefault
    end

    subgraph Compute ["Stateless Compute Tier"]
        LambdaConnect["OnConnect Lambda"]
        LambdaDisconnect["OnDisconnect Lambda"]
        LambdaMessage["ProcessMessage Lambda"]
        LambdaPush["Server Push Worker Lambda"]
    end

    subgraph Storage ["State Management Tier"]
        DDB[("DynamoDB Connections Table<br/>• connectionId (PK)<br/>• userId / deviceId<br/>• connectedAt timestamp")]
    end

    Device1 <==>|Persistent WSS Connection| WS_Route
    Device2 <==>|Persistent WSS Connection| WS_Route

    RouteConnect --> LambdaConnect
    RouteDisconnect --> LambdaDisconnect
    RouteDefault --> LambdaMessage

    LambdaConnect -->|PutItem: Store connectionId| DDB
    LambdaDisconnect -->|DeleteItem: Remove connectionId| DDB
    LambdaMessage -->|Scan / Query State| DDB

    LambdaPush -->|1. Query active connectionIds| DDB
    LambdaPush ==>|2. ApiGatewayManagementApi.postToConnection| WS_Route

    style Gateway fill:#d4edda,stroke:#28a745,stroke-width:2px
    style DDB fill:#fff3cd,stroke:#ffc107,stroke-width:2px
    style Compute fill:#f8f9fa,stroke:#6c757d,stroke-width:1px
```

---

## 5. IoT Real-Time Use Case Breakdown

In IoT workloads, devices transmit high-frequency telemetry and require immediate server-initiated commands (e.g., emergency shutdowns, firmware update notifications, mode adjustments).

```mermaid
sequenceDiagram
    autonumber
    actor Device as IoT Temperature Sensor
    participant APIGW as API Gateway WebSocket
    participant Lambda as Process Event Lambda
    participant DDB as DynamoDB (Connections)
    participant AlertWorker as Background Alert Engine

    Device->>APIGW: 1. $connect handshake
    APIGW->>Lambda: 2. Invoke OnConnect
    Lambda->>DDB: 3. Store (connectionId = conn-99, deviceId = sensor-01)
    APIGW-->>Device: 4. Connection Accepted

    Device->>APIGW: 5. Send Telemetry Frame: {"temp": 42, "unit": "C"}
    APIGW->>Lambda: 6. Invoke ProcessData (connectionId = conn-99)
    Lambda->>AlertWorker: 7. Trigger Overheat Event (42°C > Threshold)

    Note over AlertWorker,APIGW: Server-Initiated Immediate Push
    AlertWorker->>DDB: 8. Lookup connectionId for sensor-01 -> conn-99
    AlertWorker->>APIGW: 9. PostToConnection (conn-99, {"action": "EMERGENCY_SHUTDOWN"})
    APIGW-->>Device: 10. Instant Push Frame: EMERGENCY_SHUTDOWN
```

---

## 6. Comprehensive Technology Matrix

| Feature / Dimension | REST API | HTTP API | WebSocket API |
| :--- | :--- | :--- | :--- |
| **Protocol** | HTTP / HTTPS (1.1, 2.0) | HTTP / HTTPS (1.1, 2.0) | WSS / WS (TCP) |
| **Communication Model** | Request / Response | Request / Response | Bidirectional / Full-Duplex |
| **Connection Type** | Ephemeral per request | Ephemeral per request | **Persistent long-lived connection** |
| **Statefulness** | **Stateless** | **Stateless** | **Stateful** |
| **Server-Initiated Push** | No (Requires Polling) | No (Requires Polling) | **Yes (`PostToConnection`)** |
| **Built-in Routes** | Custom HTTP Verbs/Paths | Custom HTTP Verbs/Paths | `$connect`, `$disconnect`, `$default` |
| **Billing Model** | Per million API calls | Per million API calls (cheaper) | Per million messages + Connection minutes |
| **Best For** | Traditional web APIs, CRUD | Cost-optimized web APIs | **Chat, IoT, Real-time dashboards** |

---

## 7. Common AWS Exam Traps & Distractor Analysis

### Exam Question Trap Matrix

```
Question Option Combinations:
------------------------------------------
Option A: REST = Stateless | WebSocket = Stateless   [INCORRECT]
Option B: REST = Stateful  | WebSocket = Stateless   [INCORRECT]
Option C: REST = Stateful  | WebSocket = Stateful    [INCORRECT]
Option D: REST = Stateless | WebSocket = Stateful    [CORRECT ✔]
```

> [!WARNING]
> **Trap 1: Assuming WebSocket Requires Stateful Compute**
> - *Mistake*: Thinking that because WebSocket is stateful, Lambda cannot be used as the backend.
> - *Correction*: Lambda is stateless; API Gateway maintains the connection state (`connectionId`) and passes it to Lambda. Lambda saves the state in DynamoDB.

> [!TIP]
> **Trap 2: Choosing REST API for Real-Time Server Push**
> - *Mistake*: Selecting REST API with HTTP Polling for real-time notifications.
> - *Correction*: Polling adds high overhead and latency. For real-time bidirectional push, select **WebSocket API**.

---

## 8. API Gateway Selection Decision Tree

```mermaid
flowchart TD
    Start(["API Gateway Selection Requirement"]) --> Q1{"What type of communication is required?"}

    Q1 -- "Request / Response (Client Initiated)" --> Q2{"Need advanced features?<br/>(API Keys, Usage Plans, WAF, Transformations)"}
    Q1 -- "Bidirectional / Full-Duplex / Real-time Push" --> Choice_WS["API Gateway WebSocket API<br/>• Stateful Connection<br/>• Full-Duplex Communication<br/>• Persistent WSS Protocol"]

    Q2 -- "Yes (Full REST Control)" --> Choice_REST["API Gateway REST API<br/>• Stateless<br/>• Usage Plans & API Keys<br/>• Request/Response Validation"]
    Q2 -- "No (Low Cost & Low Latency HTTP)" --> Choice_HTTP["API Gateway HTTP API<br/>• Stateless<br/>• 70% Cheaper / Faster<br/>• Standard OIDC/JWT Auth"]

    Choice_WS --> Rule_WS["Exam Takeaway:<br/>WebSocket = Stateful Communication<br/>(Connection preserved, compute remains stateless)"]
    Choice_REST --> Rule_REST["Exam Takeaway:<br/>REST API = Stateless Communication<br/>(Independent HTTP requests)"]

    style Choice_WS fill:#d4edda,stroke:#28a745,stroke-width:2px
    style Choice_REST fill:#fff3cd,stroke:#ffc107,stroke-width:1px
    style Choice_HTTP fill:#d1ecf1,stroke:#17a2b8,stroke-width:1px
```

---

## 9. Exam Memory Cheat Sheet

```
REST API                    ──> Stateless Communication (Request / Response)
WebSocket API               ──> Stateful Communication (Full-Duplex / Persistent WSS)
WebSocket Route Key Names   ──> $connect, $disconnect, $default
Server Push Mechanism       ──> ApiGatewayManagementApi.postToConnection
Connection State Persistence──> DynamoDB Table storing connectionId
Stateless Compute Tier      ──> AWS Lambda
```

---

## 10. Final Exam Takeaway

- **REST APIs** process independent requests where no connection state is preserved (**Stateless**).
- **WebSocket APIs** maintain long-lived TCP connections with assigned connection IDs (**Stateful**).
- **Stateless Lambda compute** can be paired with **Stateful WebSocket connections** by storing `connectionId` records in **DynamoDB**.