**Use SageMaker AI real time inference with UltraServers style multi instance configurations and enable model parallelism libraries such as DeepSpeed or FasterTransformer to shard the model across multiple GPUs. Configure the endpoint to load coordinated model partitions across instances and use high performance networking to support cross device communication during inference**

![](https://assets-pt.media.datacumulus.com/aws-aip-pt/assets/pt1-q40-i1.jpg)

 via - [https://aws.amazon.com/blogs/machine-learning/deploy-large-models-at-high-performance-using-fastertransformer-on-amazon-sagemaker/](https://aws.amazon.com/blogs/machine-learning/deploy-large-models-at-high-performance-using-fastertransformer-on-amazon-sagemaker/)

![](https://assets-pt.media.datacumulus.com/aws-aip-pt/assets/pt1-q40-i2.jpg)

 via - [https://aws.amazon.com/blogs/machine-learning/deploy-large-models-at-high-performance-using-fastertransformer-on-amazon-sagemaker/](https://aws.amazon.com/blogs/machine-learning/deploy-large-models-at-high-performance-using-fastertransformer-on-amazon-sagemaker/)

Model parallelism is the primary technique for running extremely large models that cannot fit into the memory of a single device. Libraries such as DeepSpeed or FasterTransformer enable sharding the model across multiple GPUs and coordinate execution by distributing layers or tensor blocks across nodes. UltraServers style multi instance configurations provide the high bandwidth networking that allows these components to communicate efficiently during inference. This approach allows the model to operate at full size without modification and supports reliable serving of inference requests. Distributed partitioning ensures that each component of the model resides on the correct hardware while maintaining low latency cross device communication.

![](https://assets-pt.media.datacumulus.com/aws-aip-pt/assets/pt1-q40-i3.jpg)

 via - [https://aws.amazon.com/blogs/machine-learning/deploy-large-models-at-high-performance-using-fastertransformer-on-amazon-sagemaker/](https://aws.amazon.com/blogs/machine-learning/deploy-large-models-at-high-performance-using-fastertransformer-on-amazon-sagemaker/)



**Expose the business unit vector indexes through cross account IAM permissions supported by OpenSearch Serverless or Aurora pgvector and connect the AI platform account using AWS PrivateLink for secure, private retrieval. Then allow the Bedrock based assistant to issue vector similarity queries on demand while the data remains in the owner accounts**

This approach uses AWS PrivateLink and cross account IAM permissions to let the AI platform query remote vector indexes without duplicating data or violating account level separation. OpenSearch Serverless supports cross account access using the assume role option, and Aurora pgvector supports cross account retrieval through secure VPC connectivity and IAM authentication when combined with controlled API exposure.

This design aligns with the requirements for secure multi account retrieval, optimal vector search performance, and minimal data movement. It preserves data ownership within each business unit while enabling efficient vector similarity search for retrieval augmented generation in the Bedrock environment.
______________________

A SaaS support assistant is producing outdated recommendations even though the documentation repository has already incorporated the latest troubleshooting procedures and removed obsolete content. A review of the pipeline shows that only a portion of the corpus has been re-embedded using the new embedding model and preprocessing logic, while many older vectors remain unchanged.

How should you identify and correct embedding drift so that search results consistently reflect the most up to date knowledge?

Perform a partial refresh by re-embedding only the segments related to newly added troubleshooting steps while leaving legacy embeddings in place. Validate retrieval quality using targeted tests rather than performing a full corpus re-embedding

Correct answer

Rebuild the entire vector store using Amazon Bedrock Knowledge Bases with a single Titan Embeddings model and uniform preprocessing rules to eliminate version mismatches. Run retrieval relevance checks and drift evaluation tests to confirm that all vectors are aligned with the updated corpus

Re-embed only the documents that changed in the recent update cycle and preserve all older vectors generated with the previous embedding model. Modify OpenSearch ANN search settings to reduce stale recommendations without altering the embedding workflow

Your answer is incorrect

Use Amazon Bedrock Knowledge Bases but retain the mixed set of legacy and new embeddings while applying metadata filters that boost recently updated articles. Depend on Bedrock model based re-ranking to adjust for inconsistencies between the different embedding generations

Overall explanation

Correct option:

**Rebuild the entire vector store using Amazon Bedrock Knowledge Bases with a single Titan Embeddings model and uniform preprocessing rules to eliminate version mismatches. Run retrieval relevance checks and drift evaluation tests to confirm that all vectors are aligned with the updated corpus**

Re-embedding the entire corpus with a single Amazon Titan Embeddings model and a consistent preprocessing pipeline eliminates the root cause of drift, which is the mixing of vectors from different models and tokenization strategies. When all embeddings live in the same semantic space, similarity search behaves predictably and the knowledge assistant is much more likely to prioritize the updated troubleshooting content over stale material. Bedrock Knowledge Bases provides a managed RAG workflow that takes care of chunking, embedding, and storage in a vector store, while letting you choose a consistent embedding model such as Amazon Titan Text Embeddings.

After re-embedding, you can run evaluation workflows that analyze retrieval relevance and measure how often updated documents appear in the top results. AWS guidance on RAG evaluation and embedding quality encourages systematic testing of retrieval results whenever you change embedding models or pipelines, so a full refresh combined with evaluation is a best practice rather than a one off fix.

Here is a deep-dive into vector data stores using Amazon Bedrock Knowledge Bases: 

![](https://assets-pt.media.datacumulus.com/aws-aip-pt/assets/pt1-q73-i1.jpg)

 via - [https://aws.amazon.com/blogs/machine-learning/dive-deep-into-vector-data-stores-using-amazon-bedrock-knowledge-bases/](https://aws.amazon.com/blogs/machine-learning/dive-deep-into-vector-data-stores-using-amazon-bedrock-knowledge-bases/)

![](https://assets-pt.media.datacumulus.com/aws-aip-pt/assets/pt1-q73-i2.jpg)

 via - [https://aws.amazon.com/blogs/machine-learning/dive-deep-into-vector-data-stores-using-amazon-bedrock-knowledge-bases/](https://aws.amazon.com/blogs/machine-learning/dive-deep-into-vector-data-stores-using-amazon-bedrock-knowledge-bases/)

Incorrect options:

**Use Amazon Bedrock Knowledge Bases but retain the mixed set of legacy and new embeddings while applying metadata filters that boost recently updated articles. Depend on Bedrock model based re-ranking to adjust for inconsistencies between the different embedding generations** - Keeping a mixed population of embeddings produced by different models and preprocessors leaves the semantic space fragmented, so nearest neighbor search can still prefer stale vectors even if you apply metadata filters or re ranking. Re-ranking and filtering are useful for tuning relevance within a consistent embedding space, but they do not repair fundamental incompatibilities between vector representations generated with different models or tokenization strategies. AWS guidance on Bedrock Knowledge Bases and vector stores emphasizes consistent embedding strategy and refresh workflows as key factors for accurate retrieval in RAG applications.

**Re-embed only the documents that changed in the recent update cycle and preserve all older vectors generated with the previous embedding model. Modify OpenSearch ANN search settings to reduce stale recommendations without altering the embedding workflow** - Refreshing only a subset of documents while leaving the majority of vectors on an older embedding model keeps two incompatible vector distributions in the same index, which maintains the drift problem instead of resolving it. Tuning ANN algorithms, distance metrics, or index parameters in Amazon OpenSearch Service improves performance and scalability, but does not fix semantic mismatches between embeddings generated by different models.

**Perform a partial refresh by re-embedding only the segments related to newly added troubleshooting steps while leaving legacy embeddings in place. Validate retrieval quality using targeted tests rather than performing a full corpus re-embedding** - A partial refresh that only re-embeds segments tied to new troubleshooting steps still leaves many related documents and older content represented by legacy embeddings, which can cause the similarity search to pull outdated material that appears closer in the old semantic space. Targeted tests might show apparent improvements on a narrow subset of queries, but they can easily miss broader drift effects that occur when users phrase questions differently or search across adjacent topics. AWS prescriptive guidance on RAG and embeddings stresses that when you change the embedding model or preprocessing pipeline, a comprehensive re embedding of the corpus combined with systematic evaluation is the reliable way to eliminate stale or inconsistent retrieval behavior.

References:

[https://aws.amazon.com/blogs/machine-learning/dive-deep-into-vector-data-stores-using-amazon-bedrock-knowledge-bases/](https://aws.amazon.com/blogs/machine-learning/dive-deep-into-vector-data-stores-using-amazon-bedrock-knowledge-bases/)

[https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)

Domain

Testing, Validation, and Troubleshooting

-------------
A scientific research organization is building an advanced GenAI workspace that allows researchers to perform two very different categories of computations. Some tasks involve quick, stateless operations such as running small mathematical calculations or looking up reference values, while other tasks require submitting long running simulation jobs that need high performance compute resources and containerized environments. The organization wants a unified framework that allows its foundation models to access both types of tools in a consistent way, while ensuring that lightweight tasks run with minimal latency and heavy simulation workloads run in scalable, dedicated compute environments.

Which options can be combined to provide an efficient and extensible tool framework for both lightweight and heavy computational workloads? (Select two)

Use a single Amazon ECS cluster to run Model Context Protocol (MCP) servers for both quick calculations and GPU intensive simulations. Configure all requests to be processed through the same set of containerized tools regardless of workload size

Your selection is correct

Provision Amazon ECS based Model Context Protocol (MCP) servers to host containerized simulation tools that require GPU acceleration or long running compute. Configure the foundation model to invoke these ECS based MCP servers through the same MCP interface used for lightweight tools to maintain consistency

Deploy Lambda functions to execute both lightweight tools and simulation workloads and increase memory and timeout limits for simulation tasks. Configure the foundation model to invoke Lambda directly for all operations without differentiating workload types

Correct selection

Deploy Lambda based Model Context Protocol (MCP) servers to host stateless tool functions such as lightweight calculations and quick data lookups. Expose these Lambda based tools through MCP compliant interfaces

Your selection is incorrect

Deploy Lambda based Model Context Protocol (MCP) servers for lightweight tools and use API Gateway endpoints to trigger simulations running on Amazon ECS. Configure the foundation model to use MCP only for quick utilities while calling API Gateway separately for simulation workloads

Overall explanation

Correct option:

**Deploy Lambda based Model Context Protocol (MCP) servers to host stateless tool functions such as lightweight calculations and quick data lookups. Expose these Lambda based tools through MCP compliant interfaces**

Using Lambda based MCP servers for lightweight tools provides the lowest latency and operationally simplest environment for fast calculations, lookup operations, and other stateless functions. Lambda is designed for rapid, event driven execution without the need for container orchestration or compute provisioning. This makes it ideal for tools that must respond instantly to model requests and perform tasks that finish within short execution windows. Exposing these Lambda functions as MCP compliant servers creates a standardized interface the foundation model can use without needing to know how or where each tool is hosted.

This design enables a clean separation of tool responsibilities since Lambda automatically scales with request volume, handles concurrency for small workloads, and keeps cost proportional to actual usage. By integrating Lambda based MCP servers into the model extension framework, the system supports efficient invocations, minimal overhead, and rapid response times for all lightweight tasks. This ensures the GenAI workspace remains responsive and cost effective for functions that do not require heavy compute.

AWS Serverless MCP Server: 

![](https://assets-pt.media.datacumulus.com/aws-aip-pt/assets/pt1-q34-i1.jpg)

 via - [https://aws.amazon.com/blogs/compute/introducing-aws-serverless-mcp-server-ai-powered-development-for-modern-applications/](https://aws.amazon.com/blogs/compute/introducing-aws-serverless-mcp-server-ai-powered-development-for-modern-applications/)

**Provision Amazon ECS based Model Context Protocol (MCP) servers to host containerized simulation tools that require GPU acceleration or long running compute. Configure the foundation model to invoke these ECS based MCP servers through the same MCP interface used for lightweight tools to maintain consistency**

ECS based MCP servers provide an ideal environment for resource intensive simulation workflows that require GPU acceleration, long processing times, custom libraries, or specialized containerized dependencies. By using Amazon ECS, you can run tools inside tailored container images that include the simulations, frameworks, and scientific libraries needed by researchers. ECS tasks can be configured to run on GPU instances, scale horizontally for distributed workloads, and execute for extended durations that would exceed Lambda service limits. Exposing these simulation tools as MCP compliant endpoints ensures that they appear identical to the foundation model, even though they run in a much heavier compute environment.

This unified MCP interface eliminates the need for the model to manage separate invocation patterns and encourages the development of additional tools without modifying the application logic. The foundation model can issue complex requests through the same protocol while ECS handles compute intensive processing behind the scenes. This approach delivers a scalable, extensible, and operationally robust simulation framework aligned with the demands of scientific research environments.

Incorrect options:

**Use a single Amazon ECS cluster to run Model Context Protocol (MCP) servers for both quick calculations and GPU intensive simulations. Configure all requests to be processed through the same set of containerized tools regardless of workload size** - Running all MCP servers on a single ECS cluster forces lightweight tasks to incur container startup times, higher latency, and unnecessary cost. It also loses the elasticity and rapid response that Lambda provides for stateless operations and wastes GPU or CPU capacity on tasks that do not need it.

**Deploy Lambda functions to execute both lightweight tools and simulation workloads and increase memory and timeout limits for simulation tasks. Configure the foundation model to invoke Lambda directly for all operations without differentiating workload types** - Simulations cannot run efficiently on Lambda because of time limits, lack of GPU support, and container constraints. Increasing memory or timeout values does not resolve the need for specialized hardware and long running workloads.

**Deploy Lambda based Model Context Protocol (MCP) servers for lightweight tools and use API Gateway endpoints to trigger simulations running on Amazon ECS. Configure the foundation model to use MCP only for quick utilities while calling API Gateway separately for simulation workloads** - Splitting interfaces by using MCP for lightweight tools and API Gateway for simulations creates an inconsistent access model for the foundation model. This breaks the unified tool invocation requirement and forces the model to treat simulation tasks differently, increasing complexity.

References:

[https://aws.amazon.com/blogs/machine-learning/unlocking-the-power-of-model-context-protocol-mcp-on-aws/](https://aws.amazon.com/blogs/machine-learning/unlocking-the-power-of-model-context-protocol-mcp-on-aws/)

[https://aws.amazon.com/blogs/compute/introducing-aws-serverless-mcp-server-ai-powered-development-for-modern-applications/](https://aws.amazon.com/blogs/compute/introducing-aws-serverless-mcp-server-ai-powered-development-for-modern-applications/)

Domain

Implementation and Integration
___________________

A startup is building a multi tenant software as a service knowledge assistant that uses retrieval augmented generation on Amazon Bedrock to provide customer specific answers. Each customer uploads proprietary documents that the system stores as embeddings inside a vector database for semantic search. The platform must scale to thousands of tenants while ensuring strict data isolation, encryption, secure cross tenant access control, and predictable performance for each customer.

What is the most effective way to architect the multi tenant vector storage and isolation model?

Store all tenants' embeddings in a single shared OpenSearch Serverless vector collection and tag each vector with a tenant ID for filtering. Then rely on client side application logic to filter out results that do not match the active tenant

Deploy a separate Aurora PostgreSQL cluster with pgvector for each tenant so embeddings remain fully isolated at the database level. Then integrate each cluster with a shared retrieval service that connects to the correct cluster based on the tenant identifier

Your answer is incorrect

Export all tenant documents to Amazon S3 and use a centralized Amazon Bedrock Knowledge Base to generate embeddings for every tenant in one unified vector store. Then apply metadata based filtering inside the Knowledge Base to ensure that queries return only tenant relevant results

Correct answer

Create dedicated vector collections or namespaces per tenant using Amazon OpenSearch Serverless and enforce tenant isolation with resource policies, encryption by default, and fine grained IAM controls. Then route all customer queries through a multi tenant aware retrieval layer that selects the correct collection based on the authenticated tenant identity

Overall explanation

Correct option:

**Create dedicated vector collections or namespaces per tenant using Amazon OpenSearch Serverless and enforce tenant isolation with resource policies, encryption by default, and fine grained IAM controls. Then route all customer queries through a multi tenant aware retrieval layer that selects the correct collection based on the authenticated tenant identity**

This solution uses Amazon OpenSearch Serverless multi tenant capabilities where each tenant receives its own isolated vector collection, providing strict separation of data and search operations. Resource policies and encryption by default ensure that only the intended tenant can access its collection, while IAM based access control prevents cross tenant leakage. A multi tenant retrieval layer uses authenticated tenant context to route queries to the correct vector collection. This design aligns with the requirements for secure vector storage, scalable semantic search, and predictable performance across thousands of customers.

Build a multi-tenant serverless architecture in Amazon OpenSearch Service: 

![](https://assets-pt.media.datacumulus.com/aws-aip-pt/assets/pt1-q24-i1.jpg)

 via - [https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-a-multi-tenant-serverless-architecture-in-amazon-opensearch-service.html](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-a-multi-tenant-serverless-architecture-in-amazon-opensearch-service.html)

Incorrect options:

**Store all tenants' embeddings in a single shared OpenSearch Serverless vector collection and tag each vector with a tenant ID for filtering. Then rely on client side application logic to filter out results that do not match the active tenant** - Storing all embeddings in a single shared vector collection and filtering by tenant ID creates a high risk of accidental data leakage because isolation depends entirely on application logic. This design does not take advantage of native data isolation patterns provided by OpenSearch Serverless and violates multi tenant security best practices.

**Export all tenant documents to Amazon S3 and use a centralized Amazon Bedrock Knowledge Base to generate embeddings for every tenant in one unified vector store. Then apply metadata based filtering inside the Knowledge Base to ensure that queries return only tenant relevant results** - Placing all tenant data into a single Amazon Bedrock Knowledge Base centralizes embeddings and increases the risk of cross tenant exposure through misconfigured metadata filters. It also prevents independent scaling or performance tuning per tenant.

**Deploy a separate Aurora PostgreSQL cluster with pgvector for each tenant so embeddings remain fully isolated at the database level. Then integrate each cluster with a shared retrieval service that connects to the correct cluster based on the tenant identifier** - Provisioning a separate Aurora pgvector cluster per tenant guarantees strong isolation but does not scale to thousands of customers and increases operational overhead significantly. This architecture contradicts the goal of centralizing infrastructure while keeping costs and management tasks low.

References:

[https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-a-multi-tenant-serverless-architecture-in-amazon-opensearch-service.html](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-a-multi-tenant-serverless-architecture-in-amazon-opensearch-service.html)

[https://aws.amazon.com/blogs/database/load-vector-embeddings-up-to-67x-faster-with-pgvector-and-amazon-aurora/](https://aws.amazon.com/blogs/database/load-vector-embeddings-up-to-67x-faster-with-pgvector-and-amazon-aurora/)

Domain

Foundation Model Integration, Data Management and Compliance

_____________
A media platform uses generative models to produce large volumes of content recommendations and short summaries. Manual review for fairness and stereotyping has become impractical, but the trust and safety team still needs a consistent evaluation approach that identifies biased or unfair patterns across demographic groups with periodic human spot checks.

As the responsible AI specialist, how would you design an automated judging system that evaluates fairness, reduces judge model bias, and remains aligned with human reviewers?

Your answer is incorrect

Create an LLM as a judge workflow by defining fairness scoring rubrics and evaluating each output through Amazon Bedrock Prompt Flows that run a single high performing foundation model. Periodically compare judge results with historical fairness thresholds and adjust scoring prompts instead of performing calibration with human labeled data

Use Amazon Bedrock Guardrails to block outputs that contain demographic references or potentially sensitive phrases. Enable CloudWatch alarms so reviewers can examine filtered responses and treat filter triggers as evidence of fairness compliance

Correct answer

Design an LLM as a judge workflow by defining structured fairness rubrics and evaluating each generated output through Amazon Bedrock Prompt Flows that orchestrate fairness scoring. Use ensemble judging across multiple Bedrock models and regularly calibrate judge scores against a human labeled dataset to reduce bias and maintain reviewer alignment

Implement a fairness judging pipeline by defining scoring prompts and routing generated outputs through a single model in Amazon Bedrock Prompt Flows. Leverage CloudWatch metrics to validate judge consistency over time instead of performing calibration with human labeled samples

Overall explanation

Correct option:

**Design an LLM as a judge workflow by defining structured fairness rubrics and evaluating each generated output through Amazon Bedrock Prompt Flows that orchestrate fairness scoring. Use ensemble judging across multiple Bedrock models and regularly calibrate judge scores against a human labeled dataset to reduce bias and maintain reviewer alignment**

A structured fairness rubric evaluated through Amazon Bedrock Prompt Flows provides a consistent and repeatable method for fairness scoring across diverse outputs. Using multiple Bedrock models as an ensemble strengthens the integrity of the evaluation by reducing single model bias and producing more stable judgments. Human calibration is required to maintain alignment with real reviewer expectations as model behavior evolves. Comparing automated judge outputs to human labeled samples ensures the fairness evaluation pipeline remains reliable and effective at identifying subtle stereotyping patterns.

Here is a deep-dive on using LLM-as-a-judge for Amazon Bedrock Model Evaluation:

![](https://assets-pt.media.datacumulus.com/aws-aip-pt/assets/pt1-q67-i1.jpg)

 via - [https://aws.amazon.com/blogs/machine-learning/llm-as-a-judge-on-amazon-bedrock-model-evaluation/](https://aws.amazon.com/blogs/machine-learning/llm-as-a-judge-on-amazon-bedrock-model-evaluation/)

![](https://assets-pt.media.datacumulus.com/aws-aip-pt/assets/pt1-q67-i2.jpg)

 via - [https://aws.amazon.com/blogs/machine-learning/llm-as-a-judge-on-amazon-bedrock-model-evaluation/](https://aws.amazon.com/blogs/machine-learning/llm-as-a-judge-on-amazon-bedrock-model-evaluation/)

Incorrect options:

**Implement a fairness judging pipeline by defining scoring prompts and routing generated outputs through a single model in Amazon Bedrock Prompt Flows. Leverage CloudWatch metrics to validate judge consistency over time instead of performing calibration with human labeled samples** - Routing outputs through a single Bedrock model and relying on CloudWatch metrics does not provide sufficient protection against systematic bias. Lack of human calibration prevents verification that automated judgments remain aligned with fairness expectations.

**Create an LLM as a judge workflow by defining fairness scoring rubrics and evaluating each output through Amazon Bedrock Prompt Flows that run a single high performing foundation model. Periodically compare judge results with historical fairness thresholds and adjust scoring prompts instead of performing calibration with human labeled data** - Adjusting scoring prompts based on historical thresholds cannot replace human calibration, which is required to validate fairness judgments against real reviewer standards. Running only a single model inside Prompt Flows also increases exposure to judge model bias because ensemble diversity is not used.

**Use Amazon Bedrock Guardrails to block outputs that contain demographic references or potentially sensitive phrases. Enable CloudWatch alarms so reviewers can examine filtered responses and treat filter triggers as evidence of fairness compliance** - Guardrails help filter unsafe content but do not generate fairness scores or identify demographic bias in generated text. Treating guardrail triggers as fairness evidence overlooks subtle stereotyping patterns that require structured evaluation through judge models.

References:

[https://aws.amazon.com/blogs/machine-learning/llm-as-a-judge-on-amazon-bedrock-model-evaluation/](https://aws.amazon.com/blogs/machine-learning/llm-as-a-judge-on-amazon-bedrock-model-evaluation/)

[https://aws.amazon.com/blogs/aws/new-rag-evaluation-and-llm-as-a-judge-capabilities-in-amazon-bedrock/](https://aws.amazon.com/blogs/aws/new-rag-evaluation-and-llm-as-a-judge-capabilities-in-amazon-bedrock/)

---------------
**Integrate the graph database with a vector capable analytics engine that supports top K similarity search on embedded text stored as node or edge properties. Then run vector similarity queries inside the graph engine so the retrieval respects graph relationships before passing results to the foundation model**

This solution uses a graph analytics engine that natively supports vector based top K queries on embedded text. This approach allows the system to perform semantic similarity search while still honoring graph relationships such as supplier to route or supplier to warehouse connectivity, which preserves the intent of the graph aware retrieval design. Running vector queries within the graph layer avoids the inconsistency that occurs when vector stores and graph stores operate independently. It ensures context retrieval uses both semantic signals and graph topology before the FM call.

![](https://assets-pt.media.datacumulus.com/aws-aip-pt/assets/pt1-q22-i1.jpg)

 via - [https://aws.amazon.com/blogs/database/find-and-link-similar-entities-in-a-knowledge-graph-using-amazon-neptune-part-2-vector-similarity-search/](https://aws.amazon.com/blogs/database/find-and-link-similar-entities-in-a-knowledge-graph-using-amazon-neptune-part-2-vector-similarity-search/)

Incorrect options:

**Store the graph in a separate database and export all node and edge data into a vector store so the system can run a global vector search across all content. Then attach graph metadata to the top K vector results to approximate graph awareness during post processing** - Exporting graph data into a stand alone vector store loses graph connectivity and forces the system to approximate relationships using metadata. This reduces precision for risk analysis because the retrieval process no longer uses native graph traversal or topology.

**Convert the entire graph to flattened documents and generate embeddings for each combined record so the assistant can perform a single vector similarity search. Then rely on the foundation model to infer supply chain relationships directly from the flattened text** - Flattening graph structures into plain text breaks natural graph relationships and weakens retrieval accuracy for topological questions like supplier risk propagation. The FM cannot reliably reconstruct multi hop graph relationships from flattened embeddings.

**Run vector similarity searches in a stand alone vector database and then filter the top results by querying the graph database separately. Then merge both results client side before sending them to the foundation model to provide contextual answers** - Running vector search and graph queries in separate systems and merging results client side produces inconsistent retrieval sets and adds coordination overhead. The retrieval layer loses the ability to rank results using combined semantic and graph features.

References:

[https://aws.amazon.com/blogs/database/find-and-link-similar-entities-in-a-knowledge-graph-using-amazon-neptune-part-2-vector-similarity-search/](https://aws.amazon.com/blogs/database/find-and-link-similar-entities-in-a-knowledge-graph-using-amazon-neptune-part-2-vector-similarity-search/)

[https://docs.aws.amazon.com/neptune-analytics/latest/userguide/vector-index.html](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/vector-index.html)

Domain

Foundation Model Integration, Data Management and Compliance


--------------
A legal tech startup uses an FM on Amazon Bedrock to extract risk tagged summaries from long contract documents. They are preparing a new version of their Bedrock prompt template to improve clarity but are concerned that the update may miss certain sensitive clauses that the previous version consistently detected. The team wants a repeatable regression testing framework where both the old and new prompt templates run against a large set of historical contract documents, produce structured outputs, and generate comparison metrics that highlight improvements or regressions before a prompt version is promoted.

As the GenAI lead, how should you design this regression testing workflow using AWS services?

Use Amazon Bedrock Prompt Management to automatically run both prompt versions on the entire corpus and update template versions based on output comparisons. Store the regression test results in DynamoDB and visualize them directly through Guardrails analytics

Correct answer

Use Step Functions to orchestrate a test workflow that runs both prompt versions on the same contract corpus, store all outputs in S3, and use a Lambda function to compare results and generate regression metrics. Publish the comparison data to CloudWatch Metrics to track improvements or degradations over time

Use Amazon Comprehend to evaluate the semantic similarity between old and new prompt outputs and store the similarity scores in S3. Run the regression workflow through Lambda without orchestrating multi step comparisons

Your answer is incorrect

Use Step Functions to coordinate a pipeline that runs both prompt versions on the contract corpus and store all outputs in DynamoDB for comparison. Use a Lambda function to trigger new prompt version updates automatically whenever regression metrics indicate improvements

Overall explanation

Correct option:

**Use Step Functions to orchestrate a test workflow that runs both prompt versions on the same contract corpus, store all outputs in S3, and use a Lambda function to compare results and generate regression metrics. Publish the comparison data to CloudWatch Metrics to track improvements or degradations over time**

This approach uses Step Functions to coordinate a controlled regression test workflow where both old and new prompts run on the same dataset, ensuring consistent and repeatable evaluation. Storing the outputs in S3 and comparing them with a Lambda function allows the team to compute structured regression metrics that quantify differences across clauses and summaries. Publishing the metrics to CloudWatch allows the team to monitor trend changes in prompt quality and identify regressions before releasing new versions. This design aligns with best practices for automated prompt evaluation and supports scalable and maintainable regression testing workflows.

Incorrect options:

**Use Amazon Comprehend to evaluate the semantic similarity between old and new prompt outputs and store the similarity scores in S3. Run the regression workflow through Lambda without orchestrating multi step comparisons** - Amazon Comprehend cannot replace structured regression logic because semantic similarity scoring alone does not verify whether risk clauses are missing or misclassified. Running everything through Lambda without orchestration limits the ability to perform controlled multi stage testing across a large corpus.

**Use Amazon Bedrock Prompt Management to automatically run both prompt versions on the entire corpus and update template versions based on output comparisons. Store the regression test results in DynamoDB and visualize them directly through Guardrails analytics** - Amazon Bedrock Prompt Management does not run regression testing automatically and cannot evaluate template performance without external workflows. Guardrails analytics cannot visualize prompt regression metrics, and prompt updates must follow approvals rather than automatic version promotion.

**Use Step Functions to coordinate a pipeline that runs both prompt versions on the contract corpus and store all outputs in DynamoDB for comparison. Use a Lambda function to trigger new prompt version updates automatically whenever regression metrics indicate improvements** - This option is incorrect because DynamoDB is not designed to store large contract summaries or structured comparison datasets at scale. Automatically updating prompt versions based on regression metrics removes the required manual approval and governance steps that are critical for legal and compliance driven workloads.

References:

[https://aws.amazon.com/blogs/machine-learning/observing-and-evaluating-ai-agentic-workflows-with-strands-agents-sdk-and-arize-ax/](https://aws.amazon.com/blogs/machine-learning/observing-and-evaluating-ai-agentic-workflows-with-strands-agents-sdk-and-arize-ax/)

[https://aws.amazon.com/bedrock/evaluations/](https://aws.amazon.com/bedrock/evaluations/)

Domain

Foundation Model Integration, Data Management and Compliance