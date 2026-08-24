#ContinuousImprovementforExistingSolutions

Decoupled Event-Driven Architectures with Amazon SQS: AWS SAP-C02 & AIP-C01 Exam Guide

> [!NOTE]
> **Core Exam Concept**: Shared file systems (like **Amazon EFS**) are designed for shared POSIX file storage, **NOT for distributed work coordination**. Scanning an EFS directory from multiple compute workers causes **duplicate concurrent processing** and poor scaling. The optimal AWS pattern replaces directory polling with an event-driven queue pipeline: **S3 (Object Storage) $\rightarrow$ Lambda (Event Router) $\rightarrow$ SQS (Work Queue) $\rightarrow$ EC2 Auto Scaling Group (Decoupled Compute)**.

---

## 1. Problem Statement & Legacy Architecture Analysis

### Legacy Anti-Pattern Scenario
An enterprise video processing application uploads user video files to Amazon EFS. Multiple EC2 instances periodically scan the EFS directory to find and process unprocessed video files before writing output to Amazon S3.

```
Legacy Pipeline:
User Upload ──> EC2 Web Server ──> EFS Directory ──> EC2 Workers (Polling EFS) ──> Amazon S3
```

### Why Shared Storage Directory Polling Fails
```mermaid
flowchart TD
    subgraph Legacy ["Legacy Anti-Pattern: Shared Directory Polling"]
        User1["User Uploads"] --> EFS["Amazon EFS Directory"]
        EFS --> WorkerA["Worker A (Scans EFS)"]
        EFS --> WorkerB["Worker B (Scans EFS)"]
        EFS --> WorkerC["Worker C (Scans EFS)"]
        
        WorkerA -->|Duplicate Processing| Video1["video.mp4"]
        WorkerB -->|Duplicate Processing| Video1
        WorkerC -->|Duplicate Processing| Video1
        
        NoteLegacy["❌ No Work-Claim Mechanism<br/>❌ Multiple Workers Process Same File<br/>❌ Adding EC2 instances wastes money"]
    end

    style Legacy fill:#f8d7da,stroke:#dc3545,stroke-width:1px
```

- **No Work-Claim Mechanism**: When multiple worker instances scan EFS simultaneously, Worker A, Worker B, and Worker C all see `video-101.mp4` and initiate concurrent processing.
- **Duplicate Resource Consumption**: Multiple EC2 instances execute redundant encoding jobs on the exact same video file.
- **Ineffective Scaling**: Adding more EC2 instances to the Auto Scaling Group increases scanning contention and duplicate work rather than increasing system throughput.

---

## 2. Correct Architecture: Decoupled S3 + SQS Pipeline

```mermaid
flowchart TD
    subgraph Modern ["Modern Architecture: SQS Decoupled Event Pipeline"]
        User2["User Direct Upload"] ==>|Presigned S3 URL| S3Bucket["Amazon S3 Bucket"]
        S3Bucket -->|S3 Event Notification| Lambda["AWS Lambda<br/>(Create Job)"]
        Lambda -->|Send Message| SQS["Amazon SQS Queue<br/>(Buffer & Decouple)"]
        
        SQS -->|Message Lock| EC2_1["EC2 Worker 1"]
        SQS -->|Message Lock| EC2_2["EC2 Worker 2"]
        
        EC2_1 -->|Processed Output| S3Output["Amazon S3 Output"]
        EC2_2 -->|Processed Output| S3Output
        
        S3Output -->|Object Created| EB["Amazon EventBridge"]
        EB -->|Trigger Notification| SNS["Amazon SNS Topic"]
        SNS --> UserNotify["User Notification"]

        NoteModern["✅ Reliable Work Claiming<br/>✅ Visibility Timeout Locks Messages<br/>✅ EC2 ASG scales on Backlog per Instance"]
    end

    style Modern fill:#d4edda,stroke:#28a745,stroke-width:2px
    style SQS fill:#fff3cd,stroke:#ffc107,stroke-width:2px
```

---

## 3. SQS Message Lifecycle & Visibility Timeout Mechanics

The core mechanism preventing duplicate processing in Amazon SQS is the **Visibility Timeout**.

```mermaid
sequenceDiagram
    autonumber
    actor Client as S3 Event / Lambda
    participant SQS as Amazon SQS Queue
    participant Worker1 as EC2 Worker 1
    participant Worker2 as EC2 Worker 2

    Client->>SQS: 1. SendMessage (VideoJob-101)
    Note over SQS: Message is VISIBLE in Queue

    Worker1->>SQS: 2. ReceiveMessage (VideoJob-101)
    Note over SQS,Worker1: SQS starts Visibility Timeout (e.g. 5 minutes)<br/>Message becomes INVISIBLE to other consumers

    Worker2->>SQS: 3. ReceiveMessage (Polls Queue)
    SQS-->>Worker2: 4. Returns empty / Next Message (VideoJob-101 is locked)

    alt Success Case: Worker 1 Finishes Processing
        Worker1->>SQS: 5. DeleteMessage (VideoJob-101, ReceiptHandle)
        Note over SQS: Message permanently deleted from Queue
    else Failure Case: Worker 1 Crashes / Times Out
        Note over Worker1: Worker 1 crashes / fails during processing
        Note over SQS: Visibility Timeout Expires (5 mins elapsed)
        Note over SQS: Message becomes VISIBLE in Queue again
        Worker2->>SQS: 6. ReceiveMessage (VideoJob-101)
        Note over Worker2: Worker 2 retries processing (Zero Job Loss)
    end
```

### Key Visibility Timeout Properties
1. **Exclusive Lock**: When a worker receives a message, SQS temporarily hides it from other consumers for the configured `VisibilityTimeout` duration.
2. **Delete On Completion**: Upon successful job completion, the worker sends a `DeleteMessage` call using the message's `ReceiptHandle`.
3. **Automatic Crash Recovery**: If a worker crashes or fails to process the job before the visibility timeout expires, SQS automatically makes the message visible again for another worker to retry.

> [!IMPORTANT]
> **Visibility Timeout Rule**: Set the `VisibilityTimeout` to a value **greater than the maximum expected processing time** of a single job (e.g., if video processing takes up to 15 minutes, set Visibility Timeout to 20 minutes or use `ChangeMessageVisibility` dynamically).

---

## 4. Scaling Strategy: Backlog Per Instance Metric

Standard Auto Scaling based on CPU utilization or Memory usage fails for asynchronous queue workers. The correct metric for scaling SQS worker fleets is **Target Backlog Per Instance**.

```mermaid
flowchart TD
    subgraph SQS_Tier ["Message Queue Layer"]
        Queue["Amazon SQS Queue<br/>• ApproximateNumberOfMessagesVisible = 1,000"]
    end

    subgraph Metric ["Custom CloudWatch Metric Calculation"]
        Calc["Backlog Per Instance =<br/>MessagesVisible / RunningInstances<br/>(1,000 / 10 = 100 Messages / Instance)"]
    end

    subgraph ASG_Policy ["Auto Scaling Group Target Tracking"]
        Policy["Target Tracking Policy<br/>• Target Value: 20 Messages / Instance"]
        Policy -->|100 > 20 -> Scale Out| Action["Scale Out EC2 Instances<br/>(Add 40 Workers -> Total 50 Workers)"]
        Action --> Result["1,000 / 50 = 20 Messages / Instance<br/>(Optimal Processing Throughput)"]
    end

    Queue --> Calc
    Calc --> Policy

    style Queue fill:#fff3cd,stroke:#ffc107,stroke-width:2px
    style Action fill:#d4edda,stroke:#28a745,stroke-width:2px
```

### Metric Calculation Formula
$$\text{Backlog Per Instance} = \frac{\text{ApproximateNumberOfMessagesVisible}}{\text{Unhealthy/Healthy Running Instance Count}}$$

> [!TIP]
> **Target Tracking Scaling**: Auto Scaling Group uses a custom metric tracking policy based on `Backlog Per Instance`. If each worker can process 20 videos/hour, setting the target backlog per instance to 20 ensures instances scale up during traffic spikes and scale down to zero when the queue empties.

---

## 5. Amazon SQS Queue Types: Standard vs. FIFO

```
┌────────────────────────────────────────────────────────────────────────┐
│ Amazon SQS Standard vs. FIFO Queues                                    │
├───────────────────────────────────┬────────────────────────────────────┤
│ SQS Standard Queue                │ SQS FIFO Queue                     │
├───────────────────────────────────┼────────────────────────────────────┤
│ • Unlimited Throughput (RPS)      │ • Up to 3,000 msg/sec with batch   │
│ • At-Least-Once Delivery          │ • Exactly-Once Processing          │
│ • Best-Effort Ordering            │ • Strict First-In-First-Out Order  │
│ • Idempotent Workers Required     │ • Message Group ID & Deduplication │
└───────────────────────────────────┴────────────────────────────────────┘
```

| Dimension | SQS Standard Queue | SQS FIFO Queue |
| :--- | :--- | :--- |
| **Throughput Capacity** | **Nearly Unlimited** | High (300 msg/sec, 3,000 with batching) |
| **Ordering Guarantee** | Best-effort (out of order possible) | **Strict FIFO ordering** |
| **Delivery Guarantee** | **At-least-once** (duplicate possible) | **Exactly-once** (deduplication ID) |
| **Use Case Fit** | Independent tasks (Video encoding, logs) | Financial transactions, inventory updates |

> [!NOTE]
> **Idempotent Processing**: For video processing where files are independent objects, **SQS Standard Queue** is the correct exam choice due to unlimited throughput capacity. Applications should be designed to be **idempotent** (checking if output already exists in S3 before processing).

---

## 6. Distractor Analysis & Common Exam Traps

```mermaid
flowchart TD
    Start(["Workload Architecture Analysis"]) --> Q1{"File Payload Size?"}

    Q1 -- "Large Payload (> 10 MB up to GBs)" --> Q2{"Storage Choice?"}
    Q1 -- "Small Payload (< 256 KB)" --> SQS_Only["Direct SQS Message Payload"]

    Q2 -- "Object Storage + Event Driven" --> S3_Choice["Amazon S3<br/>• Direct upload via Presigned URL<br/>• Bypasses API Gateway 10MB limit"]
    Q2 -- "Shared POSIX Filesystem Required" --> EFS_Choice["Amazon EFS<br/>• File locking & concurrent directory access<br/>• NOT suitable as a work queue!"]

    S3_Choice --> Q3{"Processing Nature?"}

    Q3 -- "Lightweight & Short (< 15 mins)" --> Lambda_Proc["AWS Lambda Direct Execution"]
    Q3 -- "Heavy Compute / Long-Running" --> SQS_ASG["S3 Event Notification ➔ AWS Lambda<br/>➔ Amazon SQS ➔ EC2 Auto Scaling Group"]

    SQS_ASG --> Q4{"Ordering Requirement?"}

    Q4 -- "Strict Order Required (FIFO)" --> SQS_FIFO["SQS FIFO Queue<br/>• Exactly-once processing<br/>• Message Group ID"]
    Q4 -- "Independent Processing (High Scale)" --> SQS_Standard["SQS Standard Queue<br/>• At-least-once delivery<br/>• High throughput + Idempotent Workers"]

    style SQS_Standard fill:#d4edda,stroke:#28a745,stroke-width:2px
    style S3_Choice fill:#d1ecf1,stroke:#17a2b8,stroke-width:1px
    style EFS_Choice fill:#f8d7da,stroke:#dc3545,stroke-width:1px
```

### 1. Why Not API Gateway for Uploading 1 GB Videos?
> [!WARNING]
> API Gateway has a strict **10 MB payload size limit**. Uploading large binary files (like 1 GB videos) through API Gateway returns an HTTP 413 Payload Too Large error. Clients should upload directly to **Amazon S3 using a Presigned URL**.

### 2. Why Not AWS Lambda for Video Processing?
> [!CAUTION]
> AWS Lambda has a **15-minute maximum execution timeout** and limited disk/memory capacity. Heavy video processing or transcoding jobs taking longer than 15 minutes require compute environments like **Amazon EC2 Auto Scaling** or **AWS Batch**.

### 3. Why SQS Buffer is Essential (Shock Absorber)
> [!TIP]
> SQS acts as a **buffer (shock absorber)** between unpredictable upload bursts and processing capacity. If 1,000 users upload videos simultaneously, SQS holds the messages safely while the EC2 worker fleet scales out and processes jobs at its own controlled pace.

---

## 7. Comparative Technology Matrix

| Architecture Pattern | Scalability | Duplicate Work Risk | Failure Recovery | Cost Profile |
| :--- | :--- | :--- | :--- | :--- |
| **EFS Directory Polling (Legacy)** | Poor | **Extremely High** | Custom / Manual | High (Wasted EC2 compute) |
| **Direct Lambda Processing** | Limited (< 15 min limit) | Low | Retries (3 attempts) | High for heavy tasks |
| **S3 ➔ SQS ➔ EC2 ASG (Optimal)** | **Unlimited** | **Eliminated via SQS Lock** | **Visibility Timeout + DLQ** | **Lowest (Pay per usage & backlog)** |

---

## 8. Exam Memory Cheat Sheet & Keyword Matrix

```
Shared Storage Directory Polling       ──> ANTI-PATTERN (Replace with SQS Queue)
Multiple Workers Processing Same Job   ──> SQS Visibility Timeout
Unpredictable Traffic Burst Buffer     ──> Amazon SQS Queue (Shock Absorber)
Auto Scaling Queue Scaling Metric      ──> Custom Metric: Backlog Per Instance
Large Upload Payload (> 10 MB)         ──> Amazon S3 Presigned URL (Bypass API GW)
Long-Running Heavy Processing (>15 min)──> EC2 Auto Scaling Group / AWS Batch
Failed Message Isolation               ──> SQS Dead-Letter Queue (DLQ)
Event Fan-Out Notification             ──> Amazon EventBridge + Amazon SNS
```

---

## 9. Final Exam Mental Model

```
               [ User Upload via Presigned URL ]
                               │
                               ▼
                        [ Amazon S3 ]
                               │ (Object Created Event)
                               ▼
                        [ AWS Lambda ]
                               │ (Create Job)
                               ▼
                       [ Amazon SQS ] ◄── (Visibility Timeout Lock)
                               │
            ┌──────────────────┴──────────────────┐
            ▼                                     ▼
   [ EC2 Worker Instance 1 ]             [ EC2 Worker Instance 2 ]
   (Scales on Backlog/Instance)          (Scales on Backlog/Instance)
            │                                     │
            └──────────────────┬──────────────────┘
                               ▼
                    [ Amazon S3 Output ]
                               │
                               ▼
                    [ EventBridge ➔ SNS ]
```

- **S3 stores the objects.**
- **Lambda routes the events.**
- **SQS holds and locks the work items.**
- **EC2 Auto Scaling executes the heavy compute.**
- **EventBridge/SNS handles completion notifications.**