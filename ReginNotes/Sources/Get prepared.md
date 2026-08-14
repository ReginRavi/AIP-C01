# AWS Certified Generative AI Developer – Professional (AIP-C01) Study Guide

---

## 1. Amazon Bedrock Core & Ecosystem

### Inference Types & Capacity
* **On-Demand:** Best for interactive chatbots, bursty traffic, and variable workloads. Pay-per-request pricing model.
* **Provisioned Throughput:** Dedicated model capacity required for predictable peak loads, custom/fine-tuned/imported models, and mitigating `ThrottlingException`. Measured in **Model Units (MUs)**.
* **Batch Inference:** Designed for large-scale, asynchronous processing of thousands to millions of records where latency is not critical (e.g., several hours SLA).
* **Cross-Region Inference (Inference Profiles):** Automatically distributes requests across multiple AWS regions to maintain availability during regional capacity constraints.
* **Custom Model Import:** Enables importing custom model weights into Bedrock to reuse standard Bedrock Runtime APIs with serverless management.

---

### Features & Capabilities

| Feature | Description |
| :--- | :--- |
| **Bedrock Playground** | No-code console experimentation |
| **Prompt Routing** | Routes simple/complex prompts |
| **Prompt Caching** | Caches static prompt prefixes |
| **Prompt Flows (Canvas)** | Drag-and-drop visual builder |
| **Bedrock Agents** | Autonomous tool orchestration |
| **Knowledge Bases** | Managed RAG, chunking & sync |
| **Bedrock Guardrails** | Content safety & PII filtering |
| **Code Interpreter** | Sandboxed dynamic code run |


* **Intelligent Prompt Routing:** Dynamically optimizes cost and quality by routing simple tasks to smaller models (e.g., Claude 3 Haiku) and complex reasoning to larger models (e.g., Claude 3.5 Sonnet).
* **Bedrock Agents:** Implements multi-step planning and tool execution. Connects to backend services via **Action Groups** integrated with AWS Lambda using OpenAPI schemas.
* **Bedrock Guardrails:** Enforces responsible AI using **Custom Denied Words/Phrases**, **Topic Denials**, and **Sensitive Information (PII) Redaction/Masking**. Enforced via IAM policies with the condition key `bedrock:GuardrailIdentifier`.
* **Bedrock Model Evaluation:** Compares Foundation Models against standardized datasets for metrics including accuracy, Groundedness, and **Time to First Token (TTFT)**.

---

## 2. RAG, Search & Vector Storage

### Vector Store Decision Matrix

| Requirement / Exam Trigger              | Best Choice                                | Key Advantage                                        |
| :-------------------------------------- | :----------------------------------------- | :--------------------------------------------------- |
| **Enterprise RAG / Hybrid Search**      | **Amazon OpenSearch Serverless / Service** | BM25 + k-NN lexical & semantic search                |
| **Relational Data + Vector Similarity** | **Amazon Aurora PostgreSQL (`pgvector`)**  | Rich SQL queries combined with vector embeddings     |
| **Knowledge Graphs / GraphRAG**         | **Amazon Neptune / Neptune Analytics**     | Multi-hop relationship and hierarchy traversals      |
| **Lowest Cost / Cold Vector Archive**   | **S3 Vectors / S3 Object Storage**         | High latency tolerance with minimal operational cost |
| **Fast-Changing Notes / DynamoDB Sync** | **DynamoDB + OpenSearch Vector Engine**    | Real-time synchronization via DynamoDB Streams       |

---

### Chunking & Retrieval Strategies
* **Hierarchical Chunking:** Splits documents into parent and child chunks. Child chunks are embedded for search precision, while parent chunks provide complete context to the LLM.
* **AST-Based Chunking:** Preserves Abstract Syntax Trees, module boundaries, and dependency relationships when indexing source code repositories.
* **OpenSearch Optimization:** Avoid excessive small shards. Use **fewer, larger shards** (tens of GBs) to reduce CPU coordination fan-out and lower p95/p99 query latencies.
* **Semantic Caching:** Uses vector similarity against past query embeddings (via OpenSearch) to serve cached LLM responses for semantically similar prompts.

---

## 3. Foundation Models, Prompting & Hyperparameters

### Inference Parameters

| Parameter                        | Function                                             | Adjust When                                                                                      |
| :------------------------------- | :--------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| **Temperature**                  | Controls randomness of token selection               | **↑** for creativity/variety; **↓ (near 0)** for deterministic/factual tasks |
| **Top-P (Nucleus)**              | Samples from tokens exceeding cumulative probability | **↑** for diverse outputs; **↓** for strict, focused candidate selection     |
| **Top-K**                        | Limits selection to the *K* most likely tokens       | Restricts sampling to a fixed token candidate pool                                               |
| **Frequency / Presence Penalty** | Penalizes repeated tokens or recurring topics        | **↑** when the model loops or repeats words/phrases                                     |
| **Stop Sequences**               | Halts generation at a specific token or string       | Structured output boundaries (e.g., `\n\nHuman:`)                                                |
| **Max Tokens**                   | Hard upper ceiling on generated output length        | Budgeting token usage and preventing runaway generation                                          |

---

### Prompt Engineering & Optimization Techniques
* **Chain-of-Thought (CoT):** Guides the model through intermediate reasoning steps for complex logic, math, or classification tasks.
* **Context Pruning:** Strips irrelevant conversation history and boilerplate instructions to reduce prompt size, context window usage, and inference cost.
* **Prompt Compression:** Removes redundant framing without losing semantic meaning before invoking expensive models.
* **Request Batching & Concurrency:** Packages multiple requests into a single payload or calls models concurrently to minimize API overhead and latency spikes.

---

## 4. Amazon SageMaker Ecosystem

| SageMaker Feature | Description |
| :--- | :--- |
| **SageMaker Canvas** | No-code visual ML for non-devs |
| **SageMaker Clarify** | Feature importance, explainability |
| **Model Monitor** | Data and prediction drift detection |
| **Model Registry** | Model versioning and approval gates |
| **SageMaker Pipelines** | Automated CI/CD ML workflows |
| **SageMaker Debugger** | Loss spikes, NaN values, gradients |


### SageMaker Deployment Strategies
* **Serverless Inference:** Scales down to zero; best for sporadic, intermittent traffic with acceptable cold starts.
* **Asynchronous Endpoints:** Queues incoming requests; best for long-running payloads (up to 1 hour) and non-real-time processing.
* **Multi-Model Endpoints (MME):** Dynamically loads multiple models into memory on demand to maximize GPU/CPU utilization across thousands of models.
* **Linear Deployments:** Shifts a fixed percentage of traffic at regular intervals (e.g., 10% every 30 minutes) for zero-downtime Blue/Green rollouts.

---

## 5. Applied AI, Preprocessing & Data Services

* **Amazon Comprehend:** Detects, classifies, and redacts PII before sending prompts to Foundation Models.
* **Amazon Comprehend Medical:** Extracts structured medical entities (ontologies, dosages, anatomy) for healthcare-specific RAG pipelines.
* **Amazon Textract:** Extracts text, tables, and forms from scanned PDFs and handwritten documents.
* **AWS Glue ETL & Glue Data Quality:** Large-scale document cleaning, schema validation, data lineage tracking, and pre-ingestion checks.
* **AWS Lake Formation:** Enforces centralized fine-grained governance (row/column-level security) over data lakes.
* **Amazon Polly vs. Transcribe:** Polly converts Text → Speech; Transcribe converts Speech → Text.
* **Titan Image Generator G1:** Includes invisible digital watermarking to support AI attribution and content authenticity.

---

## 6. Architecture, Security & Governance

### Observability & Auditing Matrix

| Service                    | Primary Role           | Exam Question Keyword                                             |
| :------------------------- | :--------------------- | :---------------------------------------------------------------- |
| **AWS CloudTrail**         | API Auditing           | **"Who"** invoked an API, user identity, timestamps, API metadata |
| **Amazon CloudWatch Logs** | Performance & Payloads | Full prompt/response invocation payloads, alarms, errors, CPU     |
| **AWS X-Ray**              | Distributed Tracing    | **"Why"** a multi-service pipeline is slow (latency bottlenecks)  |
| **AWS Config**             | Compliance Tracking    | Configuration drift, resource state rules                         |
| **Amazon Macie**           | Data Discovery         | Identifying unencrypted PII/PHI in S3 buckets                     |

---

### Architectural Design Patterns
* **Security Isolation:** Use **Separate AWS Accounts** for the strongest isolation boundary between Dev, Test, and Prod environments with sensitive data.
* **Private VPC Connectivity:** Route traffic to Bedrock and S3 without traversing the public internet using **Interface VPC Endpoints (AWS PrivateLink)**.
* **Idempotency Key Pattern:** Implement unique idempotency keys inside Lambda Action Groups for state-changing operations (e.g., payments, reservations) to prevent duplicate execution on retries.
* **Dynamic Configuration:** Use **AWS AppConfig** to adjust model endpoints or route traffic percentages for A/B testing without code deployments.

---

## 7. Metrics & Model Evaluation Reference

| Metric                               | Primary Use Case              | Focus Area                                        |
| :----------------------------------- | :---------------------------- | :------------------------------------------------ |
| **Recall@K**                         | Vector Search / RAG Retrieval | Relevant docs present in top-*K* results          |
| **Mean Average Precision (mAP)**     | Semantic Search / Embeddings  | Ranking quality and relevance order               |
| **Groundedness / Faithfulness**      | RAG Evaluation                | Output supported by context (Hallucination check) |
| **ROUGE**                            | Summarization                 | N-gram overlap with reference summary             |
| **BLEU**                             | Machine Translation           | N-gram precision against human translation        |
| **Perplexity (PPL)**                 | Base Language Models          | Fluency, coherence, next-token prediction         |
| **BERTScore**                        | Semantic Similarity           | Embedding-based contextual meaning comparison     |
| **FID (Fréchet Inception Distance)** | Image Generation              | Quality and diversity of generated images         |
| **Accuracy / Precision / Recall**    | Classification                | Correct category assignment                       |

---

## 8. Exam Memory Tricks (Quick Recall)

* **Model Routing:** Small Model First → Confidence Check → Escalate to Large Model.
* **Vector Search Latency:** Check for too many shards → Fix by consolidating into fewer, larger shards with HNSW indexing.
* **Bedrock Streaming Retries:** Transient failure before stream → SDK retry; Stream drops midway → Application-level state retry.
* **Overfitting Fix:** Lower learning rate, apply regularization, or augment dataset.
* **Healthcare RAG:** Encrypted S3 + Comprehend Medical + Guardrails + PrivateLink + CloudTrail.