
### 1. K-NN (K-Nearest Neighbors) — Exact Search

- **How it works:** Computes the exact distance (e.g., Euclidean, Cosine, or Manhattan) between a query vector and _every single vector_ in the dataset. It then sorts the distances to find the true top-$K$ nearest neighbors.

- **Accuracy:** 100% exact (no loss of precision; it always finds the absolute closest points).
   
- **Performance/Scalability:** Highly compute-intensive with $O(N)$ time complexity per query, where $N$ is the size of the dataset. As datasets grow into millions or billions of items, latency becomes unacceptably high.


#### AWS Exam Use Cases for K-NN:

- **Small to Medium Datasets:** When the dataset size is small enough that exact search can finish within acceptable latency thresholds.

- **Strict Legal/Financial Precision Requirements:** Scenarios where missing the absolute closest data point is not an option (e.g., highly sensitive compliance or regulatory matching).

- **Amazon SageMaker Built-in K-NN Algorithm:** Used for classification and regression tasks where tabular datasets are relatively small and exact boundary mapping is desired.

### 2. ANN (Approximate Nearest Neighbors) — Scalable Vector Search

- **How it works:** Instead of scanning every vector, ANN algorithms (such as HNSW—Hierarchical Navigable Small World, or IVF—Inverted File Index) build an index upfront. They trade a tiny amount of accuracy for massive speedups by exploring only a subset of the most promising clusters or graph nodes.

- **Accuracy:** High (typically 95%–99%+ recall), but "approximate"—it may occasionally miss the absolute closest neighbor in exchange for blindingly fast results.

- **Performance/Scalability:** Extremely fast ($O(\log N)$ or sub-linear search time). Scales effortlessly to billions of high-dimensional vectors with sub-millisecond latencies.


#### AWS Exam Use Cases for ANN:

- **Generative AI & RAG (Retrieval-Augmented Generation):** Finding relevant context chunks from millions of documents stored in a vector database to pass to an LLM in Amazon Bedrock.

- **Large-Scale Recommendation Engines:** Real-time product, movie, or song recommendations based on user embeddings.

- **Semantic Search & Image/Visual Recognition:** Querying massive catalogs of text or image embeddings instantaneously.

- **AWS Services to Know:** * **Amazon OpenSearch Service** (using the k-NN plugin powered by HNSW/FAISS).
    
    - **Amazon Aurora PostgreSQL / Amazon RDS for PostgreSQL** (using the `pgvector` extension for ANN vector search).
    
    - **Amazon MemoryDB for Redis / ElastiCache** (as a high-throughput vector store).
     

### Summary Table for the Exam

| **Metric / Feature**     | **K-NN (Exact Search)**                                             | **ANN (Approximate Search)**                            |
| ------------------------ | ------------------------------------------------------------------- | ------------------------------------------------------- |
| **Search Speed**         | Slow ($O(N)$ — linear scan)                                         | Ultra-fast ($O(\log N)$ — sub-linear)                   |
| **Accuracy / Recall**    | 100% Exact                                                          | High (~95%–99%), but approximate                        |
| **Dataset Scale**        | Small datasets                                                      | Large to massive datasets (Millions/Billions)           |
| **Primary AWS Use Case** | Small tabular classification/regression or strict exact-match needs | RAG, Semantic Search, Recommendations, Large Vector DBs |
