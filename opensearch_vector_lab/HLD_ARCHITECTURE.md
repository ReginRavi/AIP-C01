# High-Level Design (HLD): Scalable Vector Search Recommendation Architecture

This High-Level Design (HLD) document specifies the architecture, data flow, cluster topology, HNSW index parameter model, and monitoring feedback loop for a large-scale recommendation system (50M+ vectors) built on **Amazon OpenSearch Service**.

---

## 1. End-to-End System Architecture

The recommendation API ingests article text, generates vector embeddings, indexes them into OpenSearch with k-NN HNSW, and executes low-latency vector similarity queries.

```mermaid
flowchart TD
    subgraph Ingestion ["1. Content Ingestion and Embedding Pipeline"]
        CMS["Content Management System - New Articles"] --> BedrockEmbed["Amazon Bedrock - Titan Text Embeddings 768d"]
        BedrockEmbed --> OpenSearchIngest["OpenSearch Bulk Ingestion API"]
    end

    subgraph Traffic ["2. Client Traffic and API Layer"]
        User["User Application or Web Client"] --> ALB["AWS Application Load Balancer"]
        ALB --> RecAPI["Recommendation Microservice - ECS Container"]
    end

    subgraph Cluster ["3. Amazon OpenSearch Service Cluster"]
        RecAPI --> DataNodes["OpenSearch Data Nodes - c6g.4xlarge"]
        
        subgraph ShardTopology ["Balanced Shard Distribution - 8 Primary Shards"]
            Node1["Node 1 - Shard 0 and Shard 4"]
            Node2["Node 2 - Shard 1 and Shard 5"]
            Node3["Node 3 - Shard 2 and Shard 6"]
            Node4["Node 4 - Shard 3 and Shard 7"]
        end
        
        DataNodes --> ShardTopology
    end

    subgraph Execution ["4. Lucene HNSW Engine Execution"]
        ShardTopology --> HNSWGraph["HNSW Graph Search - M=32, efSearch=128"]
        HNSWGraph --> RecAPI
    end

    subgraph Monitoring ["5. Observability and Feedback Loop"]
        DataNodes --> TraceAnalytics["OpenSearch Trace Analytics and Dashboards"]
        TraceAnalytics --> CloudWatch["Amazon CloudWatch Alerts"]
    end
```

---

## 2. Shard Topology & Rebalancing Architecture (Solution 2)

To eliminate **Hot Shards** under heavy traffic surges, the index is rebalanced from an unbalanced 4-shard configuration to a uniformly hashed 8-shard configuration across multi-AZ data nodes.

```mermaid
flowchart LR
    subgraph BeforeState ["BEFORE: Unbalanced Shard Routing"]
        TrafficIn1["Query Surge 1,200 QPS"] --> HotShard["Primary Shard 0 - Node 1 CPU 99%"]
        TrafficIn1 --> S1["Primary Shard 1"]
        TrafficIn1 --> S2["Primary Shard 2"]
        TrafficIn1 --> S3["Primary Shard 3"]
    end

    subgraph RebalancePipeline ["Reindexing Workflow"]
        ReindexAPI["OpenSearch _reindex API"] --> NewIndex["New Rebalanced Index"]
    end

    subgraph AfterState ["AFTER: Uniformly Hashed Shard Routing"]
        TrafficIn2["Query Surge 1,200 QPS"] --> Gateway["OpenSearch Coordinator Node"]
        Gateway --> NS0["Node 1: Shard 0 and 4 - CPU 28%"]
        Gateway --> NS1["Node 2: Shard 1 and 5 - CPU 27%"]
        Gateway --> NS2["Node 3: Shard 2 and 6 - CPU 29%"]
        Gateway --> NS3["Node 4: Shard 3 and 7 - CPU 28%"]
    end

    BeforeState --> RebalancePipeline --> AfterState
```

---

## 3. HNSW Graph Structure & Parameter Tuning (Solution 1)

`HNSW` constructs a multi-layer graph where upper layers contain sparse skip-links and lower layers contain dense vector connections.

```mermaid
graph TD
    subgraph Layer2 ["HNSW Layer 2: Sparse Entry Layer"]
        L2_Entry["Entry Node - Article 102"] --> L2_N1["Node 890"]
    end

    subgraph Layer1 ["HNSW Layer 1: Medium Skip Layer"]
        L1_N1["Node 890"] --> L1_N2["Node 450"]
        L1_N2 --> L1_N3["Node 210"]
    end

    subgraph Layer0 ["HNSW Layer 0: Dense Base Vector Layer"]
        L0_Target["Target Query Vector - Financial LLMs"]
        L0_N1["Node 210"] --> L0_N2["Candidate Node 1"]
        L0_N2 --> L0_N3["Candidate Node 2"]
        L0_N3 --> L0_Target
    end

    L2_Entry -.-> L1_N1
    L1_N3 -.-> L0_N1
```

### Parameter Tuning Impact Matrix

| HNSW Parameter | Problem Identified | Optimized Setting | Technical Mechanism |
| :--- | :--- | :--- | :--- |
| `M` (Max Links per Node) | Low graph connectivity for 768-dim embeddings | `M = 32` | Increases max bidirectional connections per vector node from 16 to 32, allowing the graph traversal to escape local minima in high-dimensional space. |
| `efConstruction` | Poor graph edge quality built during indexing | `ef_construction = 250` | Expands candidate search size during graph construction, improving overall search graph quality. |
| `efSearch` | Weakly related or irrelevant articles returned | `ef_search = 128` | Expands dynamic candidate queue during query search. Higher `efSearch` ensures nearest neighbors are evaluated, boosting **Recall @ 10 to > 99%**. |

---

## 4. Query Execution Sequence Diagram

```mermaid
sequenceDiagram
    autonumber
    participant Client as Recommendation Microservice
    participant Coord as OpenSearch Coordinator Node
    participant DataNode as OpenSearch Data Nodes
    participant Engine as Lucene HNSW Engine

    Client->>Coord: POST /articles/_search with vector payload
    Coord->>Coord: Hash Routing and Select Target Shards
    Coord->>DataNode: Parallel Sub-Queries to Primary Shards 0-7
    DataNode->>Engine: Execute HNSW Search (efSearch = 128)
    Engine-->>DataNode: Return Top-K Vector Candidate IDs and Scores
    DataNode-->>Coord: Return Shard Level Results
    Coord->>Coord: Merge and Rank Global Top-10 Recommendations
    Coord-->>Client: HTTP 200 OK Response (28ms P99 Latency)
```

---

## 5. Summary of Architecture Recommendations

1. **Horizontal Scaling & Shard Balance:** Ensure primary shard count matches or is a multiple of data node count (8 primary shards across 4 nodes) to eliminate load concentration.
2. **Dynamic Index Settings Tuning:** Dynamically update `index.knn.algo_param.ef_search` via OpenSearch REST API during marketing events to maintain high recall without requiring index re-indexing.
3. **Query-Level Observability:** Monitor performance using **OpenSearch Trace Analytics** (query-level spans) rather than aggregate cluster-level CPU to identify single-shard latency bottlenecks early.
