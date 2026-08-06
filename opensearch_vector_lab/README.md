# Amazon OpenSearch Vector Search Optimization & Troubleshooting Lab

An interactive visual web laboratory and runnable Python benchmark tool demonstrating how to troubleshoot, scale, and optimize OpenSearch vector search for high-volume recommendation APIs (35M+ article vectors).

---

## 🎯 Exam & Real-World Scenario Overview

**Problem Statement:**
A large-scale content platform exposes a recommendation API using vector search in Amazon OpenSearch Service. At tens of millions of vectors:
1. **Rising Latencies** occur during traffic spikes.
2. **Hot Shards** receive disproportionately heavy query traffic.
3. **Irrelevant / Weakly Related Articles** are returned for semantically rich queries.

**The Two Correct Solutions:**
1. **Solution 1 (HNSW Tuning):** Tune `efSearch`, `efConstruction`, and `M` parameters. Validate improvements using OpenSearch Trace Analytics and query-level metrics.
2. **Solution 2 (Shard Rebalancing):** Resize and rebalance primary shards so vector data and query load are distributed evenly. Use OpenSearch Dashboards to monitor hot shards and reindex.

---

## 🚀 Quick Start

### 1. Interactive Visual Web Laboratory
Open `index.html` in your web browser (or serve locally via Python `python -m http.server 8080`).

```bash
# In directory: c:\Users\SHYBAS\OneDrive\AIP-C01-main\opensearch_vector_lab
python -m http.server 8080
```
Then navigate to `http://localhost:8080` in your web browser.

**Web Lab Features:**
- **Cluster Shard Load Heatmap:** Live node and primary shard temperature meters showing real-time CPU, QPS, and hot-shard hotspotting.
- **HNSW Graph Traversal Simulator:** Interactive HTML5 Canvas rendering multi-layer HNSW graph hopping, entry node evaluation, and `efSearch` candidate queue expansion.
- **Recommendation API Sandbox:** Real-time semantic query comparison testing Before vs. After results on article embeddings.
- **Trace Analytics Waterfall:** Microsecond span breakdowns for index search, hot-shard queueing, and HNSW graph traversal.

### 2. Python Reference Benchmark Script
Run the automated benchmark suite:

```bash
python opensearch_vector_optimization.py
```

Outputs:
- **TEST 1:** Unoptimized state (Hot Shards + Untuned HNSW default parameters).
- **TEST 2:** HNSW Parameter Tuning (`M=32`, `efSearch=128`).
- **TEST 3:** Shard Rebalancing (`_reindex` with uniform hash routing across 8 shards).
- **REST API Payload:** Complete OpenSearch k-NN JSON mapping payload.

---

## 📐 Deep Dive: HNSW Parameter Reference

| Parameter | Default Value | Recommended Scaled Value | Impact on Vector Search |
| :--- | :--- | :--- | :--- |
| `M` | `16` | `32` to `64` | Max bidirectional links per graph node. Higher `M` improves recall for high-dimensional vectors (e.g. 1536 dim) at the cost of higher graph memory. |
| `efConstruction` | `100` | `250` to `500` | Dynamic candidate size during index building. Higher value creates higher quality graph connections, increasing indexing time. |
| `efSearch` | `16` | `64` to `256` | Dynamic candidate list evaluated during query execution. Low `efSearch` causes missing nearest neighbors (irrelevant articles). Higher `efSearch` increases recall at slight query latency cost. |
| `number_of_shards` | Unbalanced (1-4) | Balanced across Nodes (e.g., 8-16) | Eliminates hot shard bottlenecks where a single node handles 70%+ of query traffic. |

---

## 🛠️ OpenSearch REST API Payload Reference

```json
{
  "settings": {
    "index": {
      "knn": true,
      "knn.algo_param.ef_search": 128,
      "number_of_shards": 8,
      "number_of_replicas": 1
    }
  },
  "mappings": {
    "properties": {
      "article_id": { "type": "keyword" },
      "article_title": { "type": "text" },
      "article_vector": {
        "type": "knn_vector",
        "dimension": 768,
        "method": {
          "name": "hnsw",
          "space_type": "cosinesimil",
          "engine": "lucene",
          "parameters": {
            "m": 32,
            "ef_construction": 250
          }
        }
      }
    }
  }
}
```
