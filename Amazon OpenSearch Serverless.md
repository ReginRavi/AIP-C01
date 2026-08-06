### 1. What is Amazon OpenSearch Serverless (AOSS)?

OpenSearch Serverless decouples compute from storage and automatically provisions and scales compute capacity measured in **OpenSearch Compute Units (OCUs)**.

#### Primary Use Cases

- **Default Backend for Amazon Bedrock Knowledge Bases:** When building a zero-code or low-code RAG pipeline in Bedrock, AOSS is the primary managed vector store created automatically by default.
    
- **Unpredictable / Volatile Search Workloads:** Ideal when indexing or query traffic spikes unpredictably (e.g., e-commerce search during sales) or drops to zero during non-business hours.
    
- **Vector Search / GenAI Applications:** Supports the **Vector Engine for OpenSearch Serverless**, optimized specifically for high-dimensional vector embeddings, hybrid search (keyword BM25 + $k$-NN vector), and metadata filtering.
    
- **Zero Operational Overhead:** Eliminates cluster sizing, shard management, node failure handling, and patch management.
    

### 2. OpenSearch Serverless (AOSS) vs. OpenSearch Managed Cluster

For the AIP-C01 exam, you must identify when _not_ to use Serverless and choose a Provisioned/Managed Cluster instead.

|**Decision Factor**|**OpenSearch Serverless (AOSS)**|**OpenSearch Managed Cluster**|
|---|---|---|
|**Traffic Profile**|Dynamic, unpredictable, intermittent|Steady-state, high-throughput, predictable|
|**Cost Strategy**|Pay-per-OCU (Compute) + Storage; no idle cluster management|Cheaper at scale using Reserved Instances (RIs) and Graviton (e.g., `r7g`)|
|**Control & Customization**|Fully managed; no shard or cluster-level tuning|Fine-grained control over shards, replicas, custom plugins, and $k$-NN algorithms (HNSW vs. IVF)|
|**Storage Tiering**|Automated unified storage|Support for UltraWarm and Cold storage tiers for massive log retention|
|**Exam Scenario Target**|_"Fast setup", "Serverless RAG with Bedrock", "No capacity planning"_|_"Cost optimization for 24/7 predictable traffic", "Custom plugin requirement"_|

### 3. Alternative AWS Services for Vector Search & RAG (AIP-C01 Context)

In exam scenarios, OpenSearch is not always the correct answer. You will be asked to select alternative services based on specific constraints:

#### A. Amazon Aurora / RDS PostgreSQL with `pgvector`

- **When to choose:** You already store operational/transactional data in PostgreSQL, or the application requires strict **ACID compliance** and complex **SQL metadata filtering** alongside vector similarity search.
    
- **Exam Keywords:** _Existing PostgreSQL database_, _SQL queries with vector similarity_, _ACID compliance_, _unified relational + vector store_.
    

#### B. Amazon Kendra

- **When to choose:** Turnkey enterprise document search across unstructured silos (S3, SharePoint, Salesforce, Confluence) without manually creating embeddings, chunking text, or tuning vector DBs.
    
- **Exam Keywords:** _Enterprise search_, _out-of-the-box connectors_, _native document permissions/ACLs_, _no custom ML pipeline_.
    

#### C. Amazon MemoryDB for Redis / ElastiCache for Redis

- **When to choose:** Real-time semantic caching for LLMs or ultra-low latency vector retrieval where sub-millisecond response times are mandatory.
    
- **Exam Keywords:** _Sub-millisecond latency_, _semantic response cache to lower LLM costs_, _in-memory vector store_.
    

#### D. Amazon Neptune Analytics

- **When to choose:** **GraphRAG** scenarios where the application needs to traverse complex relationships between entities (knowledge graphs) combined with vector similarity search.
    
- **Exam Keywords:** _Graph database_, _entity relationship traversal_, _Knowledge Graph + RAG_.
    

### 4. AIP-C01 Scenario Decision Matrix

```
                          [ What is the Primary Requirement? ]
                                           |
    +----------------------+---------------+----------------------+----------------------+
    |                      |                                      |                      |
[Enterprise Docs     [Managed GenAI            [Existing Relational     [Ultra-Low Latency /
 & Connectors]        RAG Pipeline]             Database / SQL]          Semantic Cache]
    |                      |                                      |                      |
    v                      v                                      v                      v
Amazon Kendra    Bedrock Knowledge Bases                  Aurora PostgreSQL      Amazon MemoryDB
                 + OpenSearch Serverless                    (pgvector)             for Redis
```

- **Scenario 1:** _"The team wants to quickly build a RAG application with Amazon Bedrock without managing underlying database capacity."_
    
    - **Answer:** Bedrock Knowledge Bases with **Amazon OpenSearch Serverless**.
        
- **Scenario 2:** _"A company wants to add semantic search to its e-commerce product catalog already hosted on Amazon Aurora PostgreSQL."_
    
    - **Answer:** Enable the **`pgvector` extension** on Amazon Aurora PostgreSQL.
        
- **Scenario 3:** _"An enterprise needs to search internal HR documents on SharePoint and Google Drive with strict access control lists (ACLs)."_
    
    - **Answer:** **Amazon Kendra**.
        
- **Scenario 4:** _"A team needs to reduce LLM API calls and costs by caching past responses based on semantic similarity with sub-millisecond response times."_
    
    - **Answer:** **Amazon MemoryDB for Redis** (used as a semantic cache).