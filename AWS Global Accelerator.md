# Global Blue-Green Deployments with AWS Global Accelerator

> [!NOTE]
> **Core Exam Concept**: When performing a **global multi-region blue-green deployment** for mobile or web applications where **client-side DNS caching** presents a risk, **Route 53 Weighted Routing is INSUFFICIENT**. The correct architectural solution is **AWS Global Accelerator**, which executes instant percentage-based traffic shifting at the **network layer** using **Static Anycast IPs**, bypassing DNS propagation delays entirely.

---

## 1. Problem Statement & Scenario Analysis

### Scenario Prerequisites & Requirements

| Requirement                  | Architectural Implication                                      | Key AWS Feature / Service                                           |
| :--------------------------- | :------------------------------------------------------------- | :------------------------------------------------------------------ |
| **Blue-Green Deployment**    | Two distinct production environments (Blue = v1, Green = v2)   | Traffic shifting between endpoint groups                            |
| **Global User Base**         | Multi-Region traffic management over AWS backbone              | AWS Global Accelerator                                              |
| **Mobile App Clients**       | Severe vulnerability to persistent client-side **DNS Caching** | Network-layer traffic steering via Static Anycast IPs               |
| **Tight Time Constraints**   | Only 2 days to test and execute cutover before major sale      | Rapid, zero-TTL traffic control                                     |
| **Controlled Risk Exposure** | Test on a small fraction of users before full cutover          | Gradual percentage-based traffic shifting (Traffic Dials & Weights) |
| **Instant Rollback**         | Must revert 100% of traffic to Blue instantly if Green fails   | Zero-delay network failover                                         |

### Key Exam Trigger Phrase
```
"Global application + Mobile users + DNS Caching concern + Fast blue-green traffic shift"
      │
      ├──> AWS Global Accelerator (Static Anycast IPs)
      ├──> Traffic Dials (Per-Region percentage)
      ├──> Endpoint Weights (Per-Environment percentage)
      └──> Bypass DNS TTL Propagation Delays
```

---

## 2. Anycast Network Layer vs. DNS Layer Traffic Shifting

### Why Route 53 Weighted Routing Fails with Mobile Clients
Mobile operating systems, ISPs, and recursive DNS resolvers frequently ignore DNS TTL (Time-To-Live) settings and cache IP addresses for hours or days. Changing Route 53 DNS weights does **NOT** guarantee that mobile clients will immediately receive the new IP address.

### Comparison Sequence

```mermaid
sequenceDiagram
    autonumber
    actor MobileUser as Mobile App Client
    participant Resolver as ISP / Mobile DNS Resolver
    participant R53 as Route 53 (DNS Layer)
    participant GA as AWS Global Accelerator (Network Layer)
    participant Blue as Blue Environment (v1)
    participant Green as Green Environment (v2)

    rect rgb(255, 240, 240)
    Note over MobileUser,R53: Scenario A: Route 53 Weighted DNS Traffic Shift
    MobileUser->>Resolver: 1. DNS Query for api.example.com
    Resolver->>R53: Query IP
    R53-->>Resolver: Returns Blue IP (TTL = 300s)
    Resolver-->>MobileUser: Cached Blue IP
    Note over R53: Admin changes Route 53 weight to 100% Green
    MobileUser->>Resolver: 2. Subsequent API Request
    Note over Resolver,MobileUser: Mobile OS ignores TTL and uses CACHED Blue IP!
    MobileUser->>Blue: Connects to OLD Blue Environment (Traffic shift delayed/failed)
    end

    rect rgb(240, 255, 240)
    Note over MobileUser,Green: Scenario B: AWS Global Accelerator Network Traffic Shift
    MobileUser->>GA: 1. Connects to Static Anycast IP (e.g. 1.2.3.4)
    GA->>Blue: 2. Routes 100% traffic over AWS Global Backbone to Blue
    Note over GA: Admin updates Endpoint Weights (100% Green) instantly
    MobileUser->>GA: 3. Subsequent API Request (Same Static Anycast IP)
    GA->>Green: 4. Instantly Routes 100% traffic to Green (Zero DNS Latency!)
    end
```

---

## 3. Global Blue-Green Multi-Region Architecture

```mermaid
flowchart TD
    subgraph Clients ["Global Mobile & Web Clients"]
        UserUS["Americas Users"]
        UserEU["Europe Users"]
        UserAP["Asia-Pacific Users"]
    end

    subgraph Edge ["AWS Anycast Edge Network"]
        GA["AWS Global Accelerator<br/>(2 Static Anycast IPs)"]
    end

    subgraph RegionUS ["Primary AWS Region (us-east-1)"]
        subgraph DialUS ["Traffic Dial: 100%"]
            ALB_US["Application Load Balancer"]
            
            subgraph TargetsUS ["Endpoint Weights"]
                Blue_US["Blue Endpoint (v1)<br/>Weight: 90"]
                Green_US["Green Endpoint (v2)<br/>Weight: 10"]
            end
            
            ALB_US --> Blue_US
            ALB_US --> Green_US
        end
    end

    subgraph RegionEU ["Secondary AWS Region (eu-west-1)"]
        subgraph DialEU ["Traffic Dial: 100%"]
            ALB_EU["Application Load Balancer"]
            
            subgraph TargetsEU ["Endpoint Weights"]
                Blue_EU["Blue Endpoint (v1)<br/>Weight: 90"]
                Green_EU["Green Endpoint (v2)<br/>Weight: 10"]
            end

            ALB_EU --> Blue_EU
            ALB_EU --> Green_EU
        end
    end

    UserUS -->|Anycast Routing| GA
    UserEU -->|Anycast Routing| GA
    UserAP -->|Anycast Routing| GA

    GA ==>|AWS Global Backbone| ALB_US
    GA ==>|AWS Global Backbone| ALB_EU

    style GA fill:#d4edda,stroke:#28a745,stroke-width:2px
    style Green_US fill:#fff3cd,stroke:#ffc107,stroke-width:2px
    style Green_EU fill:#fff3cd,stroke:#ffc107,stroke-width:2px
```

---

## 4. Traffic Dials vs. Endpoint Weights

AWS Global Accelerator provides two distinct levels of traffic control:

```
┌────────────────────────────────────────────────────────────────────────┐
│ Global Accelerator Traffic Steering Controls                           │
├───────────────────────────────────┬────────────────────────────────────┤
│ Traffic Dials (Regional Control)  │ Endpoint Weights (Resource Control)│
├───────────────────────────────────┼────────────────────────────────────┤
│ • Applied per Endpoint Group       │ • Applied per Endpoint within      │
│   (AWS Region).                   │   an Endpoint Group.               │
│ • Controls % of overall traffic    │ • Controls relative distribution   │
│   routed to a specific Region.    │   between Blue and Green ALBs.     │
│ • Range: 0% to 100%               │ • Range: 0 to 255                  │
└───────────────────────────────────┴────────────────────────────────────┘
```

### Example Blue-Green Configuration
To shift 10% of global traffic to the new Green environment in `us-east-1`:
- **Traffic Dial for `us-east-1`**: Set to `100%`.
- **Blue Endpoint Weight**: Set to `90`.
- **Green Endpoint Weight**: Set to `10`.

---

## 5. Gradual Canary Rollout & Instant Rollback Workflow

```mermaid
stateDiagram-v2
    [*] --> Phase1_Initial: Deploy Green Environment
    
    state Phase1_Initial {
        Blue_100: Blue (v1) = 100%
        Green_0: Green (v2) = 0%
    }
    
    Phase1_Initial --> Phase2_CanaryTest: Shift 5% Traffic
    
    state Phase2_CanaryTest {
        Blue_95: Blue (v1) = 95%
        Green_5: Green (v2) = 5%
    }
    
    Phase2_CanaryTest --> Phase3_RampUp: Validate Health & Metrics
    
    state Phase3_RampUp {
        Blue_50: Blue (v1) = 50%
        Green_50: Green (v2) = 50%
    }
    
    Phase3_RampUp --> Phase4_FullCutover: Final Cutover
    
    state Phase4_FullCutover {
        Blue_0: Blue (v1) = 0%
        Green_100: Green (v2) = 100%
    }

    Phase2_CanaryTest --> InstantRollback: High Error Rate / Defect Found
    Phase3_RampUp --> InstantRollback: Performance Degradation
    
    state InstantRollback {
        Rollback_Blue: Blue (v1) = 100% (Instantaneous)
        Rollback_Green: Green (v2) = 0%
    }

    InstantRollback --> [*]: Issue Resolved Offline
    Phase4_FullCutover --> [*]: Deployment Successful
```

### Step-by-Step Two-Day Execution Plan
1. **Day 1 (Initial Setup & Canary Shift)**:
   - Deploy Green environment (v2) alongside Blue (v1).
   - Configure Global Accelerator endpoint weights: Blue = 95, Green = 5.
   - Monitor CloudWatch metrics (HTTP 5xx errors, latency, conversion rate).
2. **Day 1 Evening (Ramp-Up)**:
   - Increase Green weight to 25, then 50 if healthy.
3. **Day 2 (Full Cutover)**:
   - Increase Green weight to 100 (Blue weight = 0). Decommission Blue after validation.
4. **Emergency Rollback**:
   - If Green returns errors at any phase, instantly set Green weight = 0, Blue weight = 100. Traffic reverts in **< 1 second**.

---

## 6. Distractor Analysis (Why Other Answers Are Incorrect)

```mermaid
flowchart TD
    Start(["Traffic Steering Requirement Analysis"]) --> Q1{"Scope of Deployment?"}
    
    Q1 -- "Single Region" --> Q2{"Constraint Type?"}
    Q1 -- "Multi-Region / Global" --> Q3{"Is Client DNS Caching a Concern?<br/>(e.g., Mobile Users)"}

    Q2 -- "Deployment Automation" --> Ans_CodeDeploy["AWS CodeDeploy<br/>• Automated Blue-Green / Canary"]
    Q2 -- "HTTP/HTTPS Traffic Splitting" --> Ans_ALB["ALB Weighted Target Groups<br/>• Single-region HTTP level splitting"]

    Q3 -- "Yes (Mobile DNS caching / Fast rollback mandatory)" --> Ans_GA["AWS Global Accelerator<br/>• Static Anycast IPs<br/>• Instant Network-Level Steering<br/>• Traffic Dials & Endpoint Weights"]

    Q3 -- "No (Standard DNS TTL propagation acceptable)" --> Ans_R53["Route 53 Weighted Routing<br/>• DNS-level percentage splitting<br/>• Subject to resolver TTL caching"]

    style Ans_GA fill:#d4edda,stroke:#28a745,stroke-width:2px
    style Ans_R53 fill:#fff3cd,stroke:#ffc107,stroke-width:1px
    style Ans_ALB fill:#d1ecf1,stroke:#17a2b8,stroke-width:1px
```

### 1. Why Not Route 53 Weighted Routing?
> [!WARNING]
> Route 53 Weighted Routing operates at the **DNS layer**. Because mobile devices and ISPs aggressively cache DNS responses, traffic changes take time to propagate. Route 53 cannot guarantee fast rollback or immediate user traffic shifting when DNS caching is present.

### 2. Why Not ALB Weighted Target Groups?
> [!NOTE]
> ALB Weighted Target Groups excel at blue-green traffic shifting **within a single AWS Region**. However, they cannot steer traffic across multiple AWS Regions or manage entry endpoints globally.

### 3. Why Not AWS CodeDeploy?
> [!CAUTION]
> AWS CodeDeploy automates the application deployment lifecycle (e.g., EC2/ECS/Lambda code updates). It does **NOT** provide a global, network-level entry point or multi-region traffic steering across independent application environments.

---

## 7. Comparative Technology Matrix

| AWS Feature / Option | Traffic Steering Layer | Cross-Region Scope | Immune to DNS Caching | Instant Rollback | Best Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **AWS Global Accelerator** | **Network Layer (IP)** | **Yes (Multi-Region)** | **Yes (Static Anycast)** | **Yes (< 1 sec)** | **Global Blue-Green with Mobile Clients** |
| **Route 53 Weighted** | Application Layer (DNS) | Yes (Multi-Region) | No (Subject to TTL) | No (DNS Lag) | Global Blue-Green without DNS caching risk |
| **ALB Weighted Target Groups**| HTTP Layer (Application) | No (Single Region) | Yes (HTTP Level) | Yes | In-Region Blue-Green deployment |
| **AWS CodeDeploy** | Deployment Orchestration | No (Regional agent) | N/A | Yes | Automated application deployment pipelines |

---

## 8. Exam Memory Cheat Sheet & Keyword Rules

```
Global Application + Mobile DNS Caching Risk  ──> AWS Global Accelerator
Regional Percentage Traffic Control          ──> Global Accelerator Traffic Dial
Endpoint Level Traffic Distribution          ──> Global Accelerator Endpoint Weights
Single-Region HTTP Target Shifting           ──> ALB Weighted Target Groups
DNS-Based Percentage Routing                 ──> Route 53 Weighted Routing
Deployment Lifecycle Automation              ──> AWS CodeDeploy
Static Ingress IP Requirement                ──> AWS Global Accelerator (2 Anycast IPs)
```

---

## 9. Final Exam Mental Model

```
                    [ Global Mobile & Web Clients ]
                                  │
                                  ▼
                [ 2 Static Anycast IPs (Global Accelerator) ]
                                  │
                  (Traffic Steering at Network Layer)
                                  │
        ┌─────────────────────────┴─────────────────────────┐
        ▼                                                   ▼
  [ Blue Environment (v1) ]                           [ Green Environment (v2) ]
  • ALB + EC2/ECS/Lambda                              • ALB + EC2/ECS/Lambda
  • Weight: 90                                        • Weight: 10
```

- **Route 53 changes DNS records.**
- **Global Accelerator changes network routing paths behind fixed Static Anycast IPs.**
- **When mobile DNS caching threatens a rapid blue-green cutover, choose Global Accelerator.**