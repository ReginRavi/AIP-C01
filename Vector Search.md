A large scale content platform exposes a recommendation API that identifies “related articles” using a vector search workflow backed by Amazon OpenSearch Service. As the article corpus has grown into tens of millions of vectors, the platform has started experiencing rising latencies, especially during marketing events and seasonal surges. Internal debugging shows that certain shards receive disproportionately heavy query traffic, and engineers occasionally observe irrelevant or weakly related articles being returned for semantically rich queries.

As a GenAI engineer, how should you troubleshoot and optimize the vector search configuration so that retrieval performance and relevance remain consistent as the system scales? (Select two)

This scenario tests two fundamental pillars of scale-out vector search in Amazon OpenSearch Service for the **AIP-C01** exam: **Cluster Infrastructure (Shard Sizing)** and **Vector Index Algorithm Tuning (HNSW Parameters)**.

### The Two Core Problems in the Scenario

```
                              [ THE DUAL BOTTLENECK ]
                                         |
         +-------------------------------+-------------------------------+
         |                                                               |
  PROBLEM 1: "HOT SHARDS"                                 PROBLEM 2: "WEAK RELEVANCE"
  Certain shards get overwhelmed during surges.           Default ANN vector search settings return 
  --> Solved by Shard Resizing & Rebalancing              weakly related articles at large scale.
                                                          --> Solved by Tuning HNSW Parameters
```

### 1. Fix #1: Resizing & Rebalancing Shards (Fixing "Hot Shards")

#### What is a "Hot Shard"?

An OpenSearch index is divided into logical partitions called **shards**, which are distributed across physical nodes in the cluster. If data is partitioned poorly or query volume spikes for specific vectors, **one or two shards end up handling 80% of the work** while other nodes sit idle.

#### The Solution:

- **Rebalance & Reindex:** To distribute the tens of millions of vectors and search traffic evenly across all nodes, you must change the primary shard count (via reindexing) and ensure OpenSearch balances shard placement evenly.
    
- **OpenSearch Dashboards:** Used to visually detect which specific nodes/shards are overloaded ("hot") during peak periods.
    

### 2. Fix #2: HNSW Parameter Tuning (Fixing Retrieval Accuracy & Speed)

Vector search in OpenSearch uses the **Hierarchical Navigable Small World (HNSW)** algorithm to perform Approximate Nearest Neighbor (ANN) search. HNSW organizes high-dimensional vectors into a multi-layer graph (like a multi-level highway system).

When scaling to **tens of millions of vectors**, default settings fail. You must manually tune the three core HNSW parameters:

|**Parameter**|**What it Does (Analogy)**|**Impact of Increasing Value**|
|---|---|---|
|**`M`**|Maximum number of bidirectional links (connections) connected to each vector node in the graph. _(Highway On-Ramps)_|⬆️ Improves **recall & relevance**<br><br>  <br><br>⬆️ Increases **RAM memory usage**|
|**`efConstruction`**|Number of nearest neighbors evaluated when inserting a new vector into the graph during indexing. _(Map Construction Detail)_|⬆️ Builds a **higher-quality graph**<br><br>  <br><br>⬆️ Increases **index build time**|
|**`efSearch`**|Size of the dynamic candidate list evaluated **at query time**. _(Number of alternate routes checked while driving)_|⬆️ Improves **accuracy/recall** (fixes weakly related results)<br><br>  <br><br>⬆️ Increases **query latency**|

#### Why Trace Analytics Matter:

Query behavior changes under real-world traffic surges. Using **OpenSearch Trace Analytics** allows engineers to measure latency down to the specific query layer to dial in the exact `efSearch` balance between speed and precision.

### 💡 Why the Other Options are Exam Traps

1. **Trap: "Consolidate into a single high-memory node"**
    
    - _Why it fails:_ Vector search requires horizontal scaling across multiple distributed nodes. A single node creates an absolute bottleneck and completely eliminates fault tolerance and scale-out capacity.
        
2. **Trap: "Increase Top-K and pass to Bedrock for re-ranking"**
    
    - _Why it fails:_ Re-ranking with a Foundation Model via Bedrock adds massive network and token latency. It does _not_ fix the underlying vector index or the hot shards—it only makes peak-traffic latency worse and drastically increases API costs.
        
3. **Trap: "Switch to HNSW but keep defaults and use cluster-level CloudWatch metrics"**
    
    - _Why it fails:_ Switching to HNSW without tuning `efSearch`/`M` leaves the algorithm running on default parameters unsuited for tens of millions of vectors. Furthermore, cluster-level metrics mask the query-level performance of individual hot shards.