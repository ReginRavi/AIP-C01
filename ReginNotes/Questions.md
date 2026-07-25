A retail company has a generative AI (GenAI) product recommendation application that uses Amazon Bedrock. The application suggests products to customers based on browsing history and demographics. The company needs to implement <font color="#00b050">fairness evaluation</font> across multiple demographic groups to detect and measure bias in recommendations between two prompt approaches. The company <font color="#00b050">wants to collect and monitor fairness metrics in real time</font>. The company must receive an alert if the fairness metrics show a discrepancy of more than 15% between demographic groups. The company must receive weekly reports that compare the performance of the two prompt approaches. 

Which solution will meet these requirements with the LEAST custom development effort? 

A. Configure an Amazon CloudWatch dashboard to display default metrics from Amazon Bedrock API calls. Create custom metrics based on model outputs. Set up Amazon EventBridge rules to invoke AWS lambda functions that perform post-processing analysis on model responses and publish custom fairness metrics. 

B. Create the two prompt variants in Amazon Bedrock Prompt Management. Use Amazon Bedrock Flows to deploy the prompt variants with defined traffic allocation. Configure Amazon Bedrock guardrails that have content filters to monitor demographic fairness. Set up Amazon CloudWatch alarms on the GuardrailContentSource dimension that use InvocationsIntervened metrics to detect recommendation discrepancy threshold violations. 

C. Set up Amazon SageMaker Clarify to analyze model outputs. Publish fairness metrics to Amazon CloudWatch. Create CloudWatch composite alarms that combine SageMaker Clarify bias metrics with Amazon Bedrock latency metrics to provide a comprehensive fairness evaluation dashboard. 

D. Create an Amazon Bedrock model evaluation job to compare fairness between the two prompt variants. Enable model invocation logging in Amazon CloudWatch. Set up CloudWatch alarms for InvocationsIntervened metrics with a dimension for each demographic group. 

Based on the requirements and AWS best practices for the AWS Certified Generative AI Developer (AIP-C01) exam, the correct answer is **B**.

Here is the breakdown of why this solution requires the LEAST custom development effort:

- **Real-Time A/B Testing (Two Prompt Approaches):** **Amazon Bedrock Prompt Management** and **Amazon Bedrock Flows** provide native, fully managed mechanisms to create multiple prompt variants and allocate traffic between them. This eliminates the need to build a custom A/B testing or routing framework within your application code.

- **Real-Time Fairness Monitoring & Alerting:** **Amazon Bedrock Guardrails** actively monitor model inputs and outputs for policy violations (such as bias or toxic content) in real-time. When a guardrail blocks or modifies a response, it automatically publishes the `InvocationsIntervened` metric to **Amazon CloudWatch**.

- **Least Custom Development:** By routing traffic through Bedrock Flows and applying Guardrails, you can use native CloudWatch metric math to set an alarm that triggers if the discrepancy between demographic dimensions exceeds 15%. This is a purely configuration-based approach.


**Why the other options are incorrect:**

- **A:** Relies heavily on custom AWS Lambda functions to parse outputs and manually publish metrics to CloudWatch. This violates the "least custom development effort" requirement.
    
- **C:** Amazon SageMaker Clarify is an excellent tool for bias detection, but combining Clarify bias metrics specifically with _Bedrock latency metrics_ to create a fairness dashboard makes no logical sense. Furthermore, integrating Clarify for real-time inference on Bedrock requires more custom pipeline plumbing than native Bedrock Guardrails.
    
- **D:** <font color="#548dd4">Amazon Bedrock model evaluation jobs are batch/offline processes designed to evaluate models against specific static datasets. They cannot be used for real-time traffic monitoring and alerting in a live production application</font>.

A finance company is developing an AI assistant to help clients plan investments and manage their portfolios. The company identifies several high-risk conversation patterns such as requests for specific stock recommendations or guaranteed returns. High-risk conversation patterns could lead to regulatory violations if the company cannot implement appropriate controls. 

The company must ensure that the AI assistant does not provide inappropriate financial advice, generate content about competitors, or make claims that are not factually grounded in the company's approved financial guidance. The company wants to use Amazon Bedrock Guardrails to implement a solution. 

Which combination of steps will meet these requirements? (Choose three.) 

A. Add the high-risk conversation patterns to a denied topics guardrail. 

B. Configure a content filter guardrail to filter prompts that contain the high-risk conversation patterns. 

C. Configure a content filter guardrail to filter prompts that contain competitor names. 

D. Add the names of competitors as custom word filters. Set the input and output actions to block. 

E. Set a low grounding score threshold. 

F. Set a high grounding score threshold. 

Based on the requirements and AWS best practices for Amazon Bedrock Guardrails, the correct combination of steps is **A, D, and F**.

Here is a breakdown of why these options are correct and map perfectly to the specific requirements:

- **A. Add the high-risk conversation patterns to a denied topics guardrail:** Denied topics allow you to use natural language to define specific subjects the AI must avoid (e.g., "giving specific stock recommendations or guaranteeing returns"). This is the correct mechanism for blocking complex, domain-specific conversational patterns. Content filters (Option B) are used for generic harmful categories like hate speech, toxicity, or violence, not custom business logic.

- **D. Add the names of competitors as custom word filters. Set the input and output actions to block:** Custom word filters allow you to explicitly define a list of specific words or phrases (like competitor brand names) to block. Setting it to block on both input and output ensures the user cannot prompt the model about a competitor, and the model cannot generate a response containing the competitor's name. (Option C is incorrect because content filters do not handle custom terminology).

- **F. Set a high grounding score threshold:** Amazon Bedrock Guardrails includes contextual grounding checks to prevent hallucinations. By setting a _high_ grounding score threshold, you strictly enforce that the AI's responses must be heavily supported by and grounded in the company's approved financial reference documents. Setting a low threshold (Option E) would increase the risk of the model making unfounded claims.


A company has deployed an AI assistant as a React application that uses AWS Amplify, an AWS AppSync GraphQL API, and Amazon Bedrock Knowledge Bases. The application uses the GraphQL API to call the Amazon Bedrock RetrieveAndGenerate API for knowledge base interactions. The company configures an AWS Lambda resolver to use the RequestResponse invocation type. 

Application users report frequent timeouts and slow response times. Users report these problems more frequently for complex questions that require longer processing. 

The company needs a solution to fix these performance issues and enhance the user experience. 

Which solution will meet these requirements? 

A. Use AWS Amplify AI Kit to implement streaming responses from the GraphQL API and to optimize client-side rendering. 

B. Increase the timeout value of the Lambda resolver. Implement retry logic with exponential backoff. 

C. Update the application to send an API request to an Amazon SQS queue. Update the AWS AppSync resolver to poll and process the queue. 

D. Change the RetrieveAndGenerate API to the InvokeModelWithResponseStream API. Update the application to use an Amazon API Gateway WebSocket API to support the streaming response. 

Based on AWS best practices for generative AI application architecture, the correct solution is **A**.

Here is a breakdown of why this is the best approach and why the alternatives fall short:

### The Problem

The current architecture uses a standard, synchronous `RequestResponse` invocation. The React application sends a query to AppSync, AppSync triggers a Lambda function, and Lambda waits for Amazon Bedrock to generate the _entire_ response before sending it all back. For complex Generative AI tasks, this takes a significant amount of time, leading to poor perceived performance (the user just stares at a loading spinner) and frequent HTTP/Lambda timeouts.

### Why Option A is Correct

- **AWS Amplify AI Kit:** This toolkit is specifically designed to solve this exact problem for full-stack developers using Amplify and AppSync. It provides native React components (like `useAIConversation`) and backend configurations to seamlessly stream LLM responses token-by-token.
    
- **Streaming over AppSync:** By implementing streaming, the application no longer waits for the entire text block to generate. It renders words on the screen as soon as Bedrock outputs them. This instantly solves the timeout issue (the connection is kept alive via continuous data flow) and drastically improves the user experience by reducing perceived latency.
    

### Why the Other Options are Incorrect

- **B (Increase Lambda timeout & retry):** While you can increase Lambda timeouts (up to 15 minutes) and AppSync timeouts (up to 30 seconds), this does not fix the core UX issue. The user is still forced to wait a long time with no feedback. Furthermore, if generation takes longer than 30 seconds, AppSync will still sever the connection.
    
- **C (Amazon SQS & Polling):** This introduces an asynchronous, event-driven architecture suitable for background processing (like rendering a large video), but it is a terrible pattern for real-time conversational AI assistants. Polling introduces unnecessary latency and massive architectural complexity.
    
- **D (API Gateway WebSocket):** While building a custom API Gateway WebSocket API and using the `InvokeModelWithResponseStream` API _does_ achieve streaming, it requires you to completely abandon your existing AWS AppSync GraphQL architecture and rewrite the backend and frontend connection logic from scratch. Amplify AI Kit (Option A) provides this capability natively without the heavy lifting.
    

[Building a React App with AWS Amplify AI Kit](https://www.youtube.com/watch?v=Q7WMOhRILxo) This tutorial demonstrates how to practically implement the AWS Amplify AI Kit within a React application to handle streaming conversational chat and interactions with Amazon Bedrock Knowledge Bases.

[

![](https://www.gstatic.com/images/branding/productlogos/youtube/v9/192px.svg)

Building a Storytelling App with AWS Amplify AI Kit

AWS Developers · 2.1K views



](https://www.youtube.com/watch?v=Q7WMOhRILxo)

![](https://i.ytimg.com/vi/Q7WMOhRILxo/maxresdefault.jpg)

![](https://www.gstatic.com/images/branding/productlogos/youtube/v9/192px.svg)

An ecommerce company operates a global product recommendation system that needs to switch between multiple foundation models (FM) in Amazon Bedrock based on regulations, cost optimization, and performance requirements. The company must apply custom controls based on proprietary business logic, including dynamic cost thresholds, AWS Region-specific compliance rules, and real-time A/B testing across multiple FMs. The system must be able to switch between FMs without deploying new code. The system must route user requests based on complex rules including user tier, transaction value, regulatory zone, and real-time cost metrics that change hourly and require immediate propagation across thousands of concurrent requests. 

Which solution will meet these requirements? 

A. Deploy an AWS Lambda function that uses environment variables to store routing rules and Amazon Bedrock FM IDs. Use the Lambda console to update the environment variables when business requirements change. Configure an Amazon API Gateway REST API to read request parameters to make routing decisions. 

B. Deploy Amazon API Gateway REST API request transformation templates to implement routing logic based on request attributes. Store Amazon Bedrock FM endpoints as REST API stage variables. Update the variables when the system switches between models. 

C. Configure an AWS Lambda function to fetch routing configurations from the AWS AppConfig Agent for each user request. Run business logic in the Lambda function to select the appropriate FM for each request. Expose the FM through a single Amazon API Gateway REST API endpoint. 

D. Use AWS Lambda authorizers for an Amazon API Gateway REST API to evaluate routing rules that are stored in AWS AppConfig. Return authorization contexts based on business logic. Route requests to model-specific Lambda functions for each Amazon Bedrock FM. 

Based on AWS architectural best practices and the specific requirements for the AWS Certified Generative AI Developer (AIP-C01) exam, the correct answer is **C**.

Here is the breakdown of why this solution is the most appropriate and why the alternatives fail:

### Why Option C is Correct

- **Dynamic Configuration without Code Deployments:** **AWS AppConfig** is explicitly designed to manage and deploy dynamic configurations (like feature flags, routing rules, and cost thresholds) independent of code deployments. You can change your active FMs or update hourly cost thresholds in AppConfig, and it propagates to your application immediately.

- **High Performance at Scale:** The **AWS AppConfig Agent** (implemented as a Lambda extension) caches configuration data locally and polls for updates in the background. This ensures the Lambda function has single-digit millisecond access to the latest routing rules for thousands of concurrent requests without introducing network latency.

- **Handling Complex Logic:** Using an AWS Lambda function allows you to execute the complex proprietary business logic (user tier calculations, A/B testing, and regulatory zone checks) against the cached AppConfig data to dynamically select the correct Amazon Bedrock FM ID at runtime.


### Why the Other Options are Incorrect

- **A (Lambda Environment Variables):** Updating environment variables requires a Lambda function configuration update, which triggers a cold start for new execution environments. Furthermore, relying on manual updates via the AWS Console for hourly changes across a global system is highly prone to human error and does not scale.

- **B (API Gateway Transformation Templates):** API Gateway uses Velocity Template Language (VTL) for request transformations. VTL is meant for simple payload formatting, not for executing complex, proprietary business logic, dynamic cost calculations, or real-time A/B testing.

- **D (Lambda Authorizers for Routing):** <font color="#548dd4">Lambda Authorizers are meant strictly for **authentication and authorization** (evaluating identity and permissions), not for application routing logic.</font> Using an authorizer to route traffic based on A/B testing or cost metrics is a severe architectural anti-pattern. Additionally, maintaining separate "model-specific" Lambda functions adds unnecessary operational overhead.


__________________________
A financial services company is building a customer support application that retrieves relevant financial regulation documents from a database based on semantic similarity to user queries. The application must integrate with Amazon Bedrock to generate responses. The application must search documents in English, Spanish, and Portuguese. The application must filter documents by metadata such as publication date, regulatory agency, and document type.  
  
The database stores approximately 10 million document embeddings. To minimize operational overhead, the company wants a solution that minimizes management and maintenance effort while providing low-latency responses for real-time customer interactions.  
  
Which solution will meet these requirements?

- Use Amazon OpenSearch Serverless to provide vector search capabilities and metadata filtering. Integrate with Amazon Bedrock Knowledge Bases to enable Retrieval Augmented Generation (RAG) using an Anthropic Claude foundation model.correct
- Deploy an Amazon Aurora PostgreSQL database with the pgvector extension. Store embeddings and metadata in tables. Use SQL queries for similarity search and send results to Amazon Bedrock for response generation.
- Use Amazon S3 Vectors to configure a vector index and non-filterable metadata fields. Integrate S3 Vectors with Amazon Bedrock for RA
- Set up an Amazon Neptune Analytics database with a vector index. Use graph-based retrieval and Amazon Bedrock for response generation.

Explanation:

Option A is the optimal solution because it provides scalable semantic search, rich metadata filtering, and tight integration with Amazon Bedrock while minimizing operational overhead. Amazon OpenSearch Serverless is designed for high-volume, low-latency search workloads and removes the need to manage clusters, capacity planning, or scaling policies.

With support for vector search and structured metadata filtering, OpenSearch Serverless enables efficient similarity search across 10 million embeddings while applying constraints such as language, publication date, regulatory agency, and document type. This is critical for financial services use cases where relevance and compliance depend on precise filtering.

Integrating OpenSearch Serverless with Amazon Bedrock Knowledge Bases enables a fully managed RAG workflow. The knowledge base handles embedding generation, retrieval, and context assembly,

while Amazon Bedrock generates responses using a foundation model. This significantly reduces custom glue code and operational complexity.

Multilingual support is handled at the embedding and retrieval layer, allowing documents in English, Spanish, and Portuguese to be searched semantically without language-specific query logic. OpenSearch’s distributed architecture ensures consistent low-latency responses for real-time customer interactions.

Option B increases operational overhead by requiring database tuning and scaling for vector workloads.

Option C does not support advanced metadata filtering, which is a key requirement.

Option D introduces unnecessary complexity and is not optimized for large-scale semantic document retrieval.

Therefore, Option A best meets the requirements for performance, scalability, multilingual support, and minimal management effort in an Amazon BedrockCbased RAG application

2. A company deploys multiple Amazon BedrockCbased generative AI (GenAI) applications across multiple business units for customer service, content generation, and document analysis. Some applications show unpredictable token consumption patterns. The company requires a comprehensive observability solution that provides real-time visibility into token usage patterns across multiple models. The observability solution must support custom dashboards for multiple stakeholder groups and provide alerting capabilities for token consumption across all the foundation models that the company’s applications use.  
  
Which combination of solutions will meet these requirements with the LEAST operational overhead? (Select TWO.)

- Use Amazon CloudWatch metrics as data sources to create custom Amazon QuickSight dashboards that show token usage trends and usage patterns across FMs.correct
- Use CloudWatch Logs Insights to analyze Amazon Bedrock invocation logs for token consumption patterns and usage attribution by application. Create custom queries to identify high-usage scenarios. Add log widgets to dashboards to enable continuous monitoring.
- Create custom Amazon CloudWatch dashboards that combine native Amazon Bedrock token and invocation CloudWatch metrics. Set up CloudWatch alarms to monitor token usage thresholds.correct
- Create dashboards that show token usage trends and patterns across the company’s FMs by using an Amazon Bedrock zero-ETL integration with Amazon Managed Grafana.correct
- Implement Amazon EventBridge rules to capture Amazon Bedrock model invocation events. Route token usage data to Amazon OpenSearch Serverless by using Amazon Data Firehose. Use OpenSearch dashboards to analyze usage patterns.wrong

Explanation:

The combination of Options C and D delivers comprehensive, real-time observability for Amazon Bedrock workloads with the least operational overhead by relying on native integrations and managed services.

Amazon Bedrock publishes built-in CloudWatch metrics for model invocations and token usage.

Option C leverages these native metrics directly, allowing teams to build centralized CloudWatch dashboards without additional data pipelines or custom processing. CloudWatch alarms provide threshold-based alerting for token consumption, enabling proactive cost and usage control across all foundation models. This approach aligns with AWS guidance to use native service metrics whenever possible to reduce operational complexity.

Option D complements CloudWatch by enabling advanced, stakeholder-specific visualizations through Amazon Managed Grafana. The zero-ETL integration allows Bedrock and CloudWatch metrics to be visualized directly in Grafana without building ingestion pipelines or managing storage layers. Grafana dashboards are particularly well suited for serving different audiences, such as engineering, finance, and product teams, each with customized views of token usage and trends.

Option A introduces unnecessary complexity by adding a business intelligence layer that is better suited for historical analytics than real-time operational monitoring.

Option B is useful for deep log analysis but requires query maintenance and does not provide efficient real-time dashboards at scale.

Option E involves multiple services and custom data flows, significantly increasing operational overhead compared to native metric-based observability.

By combining CloudWatch dashboards and alarms with Managed Grafana’s zero-ETL visualization capabilities, the company achieves real-time visibility, flexible dashboards, and automated alerting across all Amazon Bedrock foundation models with minimal operational effort.

3. A hotel company wants to enhance a legacy Java-based property management system (PMS) by adding AI capabilities. The company wants to use Amazon Bedrock Knowledge Bases to provide staff with room availability information and hotel-specific details. The solution must maintain separate access controls for each hotel that the company manages. The solution must provide room availability information in near real time and must maintain consistent performance during peak usage periods.  
  
Which solution will meet these requirements?

- Deploy a single Amazon Bedrock knowledge base that contains combined data for all hotels. Configure AWS Lambda functions to synchronize data from each hotel’s PMS database through direct  
    API connections. Implement AWS CloudTrail logging with hotel-specific filters to audit access logs for each hotel’s data.
- Create an Amazon EventBridge rule for each hotel that is invoked by changes to the PMS database. Configure the rule to send updates to a centralized Amazon Bedrock knowledge base in a management AWS account. Configure resource-based policies to enforce hotel-specific access controls.wrong
- Implement one Amazon Bedrock knowledge base for each hotel in a multi-account structure. Use direct data ingestion to provide near real-time room availability information. Schedule regular synchronization for less critical information.correct
- Build a centralized Amazon Bedrock Agents solution that uses multiple knowledge bases. Implement AWS IAM Identity Center with hotel-specific permission sets to control staff access.

Explanation:

Option C best meets the requirements by aligning with AWS best practices for data isolation, access control, and scalable GenAI retrieval. Implementing a separate Amazon Bedrock knowledge base for each hotel ensures strict separation of data and permissions. This approach naturally enforces hotel-level access control without requiring complex policy logic or post-query filtering.

A multi-account structure further strengthens security and governance by isolating each hotel’s data plane. AWS recommends account-level isolation for workloads with strong tenancy or compliance boundaries. Hotel staff can be granted access only to their hotel’s account and corresponding knowledge base, eliminating the risk of cross-hotel data exposure.

Direct data ingestion into each knowledge base enables near real-time updates for critical data such as room availability. For information that does not change frequently, scheduled synchronization reduces ingestion cost while maintaining accuracy. This hybrid ingestion model balances freshness and operational efficiency.

Because Amazon Bedrock Knowledge Bases are fully managed, performance remains consistent during peak usage periods without the company managing indexing, scaling, or retrieval infrastructure. Each knowledge base scales independently, preventing noisy-neighbor issues that could arise in a centralized design.

Option A and B rely on a centralized knowledge base, which increases policy complexity and introduces risk of misconfigured access controls.

Option D adds unnecessary orchestration complexity and does not inherently solve real-time data freshness requirements.

Therefore, Option C provides the most secure, scalable, and operationally efficient solution for enhancing the PMS with Amazon Bedrock Knowledge Bases.

4. A financial services company is creating a Retrieval Augmented Generation (RAG) application that uses Amazon Bedrock to generate summaries of market activities. The application relies on a vector database that stores a small proprietary dataset with a low index count. The application must perform similarity searches. The Amazon Bedrock model’s responses must maximize accuracy and maintain high performance.  
  
The company needs to configure the vector database and integrate it with the application.  
  
Which solution will meet these requirements?

- Launch an Amazon MemoryDB cluster and configure the index by using the Flat algorithm.  
    Configure a horizontal scaling policy based on performance metrics.
- Launch an Amazon MemoryDB cluster and configure the index by using the Hierarchical Navigable Small World (HNSW) algorithm. Configure a vertical scaling policy based on performance metrics.correct
- Launch an Amazon Aurora PostgreSQL cluster and configure the index by using the Inverted File with Flat Compression (IVFFlat) algorithm. Configure the instance class to scale to a larger size when the load increases.
- Launch an Amazon DocumentDB cluster that has an IVFFlat index and a high probe value.  
    Configure connections to the cluster as a replica set. Distribute reads to replica instances.

Explanation:

Option B is the optimal solution because it maximizes similarity search accuracy and performance for a small, proprietary dataset while maintaining low operational complexity. Amazon MemoryDB is a fully managed, in-memory database that provides microsecond-level latency, making it ideal for real-time RAG workloads that require fast vector similarity searches.

For small datasets with low index counts, the Hierarchical Navigable Small World (HNSW) algorithm

is recommended by AWS for its high recall and accuracy. Unlike approximate methods optimized for

massive datasets, HNSW excels at returning the most semantically relevant vectors with minimal loss

of precision, which directly improves the quality of responses generated by the Amazon Bedrock foundation model.

Vertical scaling in MemoryDB is sufficient for this use case because the dataset size is limited. Scaling up instance size provides increased memory and compute capacity without the complexity of managing distributed indexes or sharding strategies. This simplifies operations while maintaining predictable performance.

Option A’s Flat algorithm is computationally expensive and inefficient at scale, even for moderate query volumes.

Option C introduces higher latency and operational overhead by using a relational database not optimized for in-memory vector search.

Option D is unsuitable because Amazon DocumentDB is not designed for high-performance vector similarity workloads and introduces unnecessary replica management complexity.

Therefore, Option B best meets the requirements for accuracy, performance, and efficient integration with an Amazon BedrockCbased RAG application.

5. A financial services company needs to build a document analysis system that uses Amazon Bedrock to process quarterly reports. The system must analyze financial data, perform sentiment analysis, and validate compliance across batches of reports. Each batch contains 5 reports. Each report requires multiple foundation model (FM) calls. The solution must finish the analysis within 10 seconds for each batch. Current sequential processing takes 45 seconds for each batch.  
  
Which solution will meet these requirements?

- Use AWS Lambda functions with provisioned concurrency to process each analysis type sequentially. Configure the Lambda function timeouts to 10 seconds. Configure automatic retries with exponential backoff.
- Use AWS Step Functions with a Parallel state to invoke separate AWS Lambda functions for each analysis type simultaneously. Configure Amazon Bedrock client timeouts. Use Amazon CloudWatch metrics to track execution time and model inference latency.correct
- Create an Amazon SQS queue to buffer analysis requests. Deploy multiple AWS Lambda functions with reserved concurrency. Configure each Lambda function to process different aspects of each report sequentially and then combine the results.
- Deploy an Amazon ECS cluster that runs containers that process each report sequentially. Use a load balancer to distribute batch workloads. Configure an auto-scaling policy based on CPU utilization.

Explanation:

Option B is the correct solution because it parallelizes independent foundation model inference tasks while maintaining orchestration, observability, and time-bound execution. AWS Generative AI best practices emphasize reducing end-to-end latency by parallelizing independent inference calls rather than scaling individual calls vertically.

In this scenario, each report requires multiple independent analyses such as financial extraction, sentiment analysis, and compliance validation. These tasks do not depend on each other’s output, making them ideal candidates for parallel execution. AWS Step Functions provides a Parallel state that can invoke multiple AWS Lambda functions simultaneously, drastically reducing total processing time compared to sequential execution.

By invoking Amazon Bedrock from separate Lambda functions in parallel, the system can reduce batch execution time from 45 seconds to well under the 10-second requirement, assuming each inference call remains within acceptable latency bounds. Step Functions also provide built-in error handling, retries, and state tracking, which improves reliability without increasing complexity.

CloudWatch metrics allow teams to monitor both workflow execution time and individual model inference latency, enabling performance tuning and operational visibility. Configuring client-side timeouts ensures that slow or failed model invocations do not block the entire batch.

Option A still processes tasks sequentially and therefore cannot meet the strict latency requirement.

Option C introduces queuing delays and sequential processing within each report, which increases total execution time.

Option D relies on container-based sequential processing and adds unnecessary operational overhead for a workload that is event-driven and latency-sensitive.

Therefore, Option B best meets the performance, scalability, and operational efficiency requirements for high-speed batch document analysis using Amazon Bedrock.

6. An elevator service company has developed an AI assistant application by using Amazon Bedrock. The application generates elevator maintenance recommendations to support the company’s elevator technicians. The company uses Amazon Kinesis Data Streams to collect the elevator sensor data.  
  
New regulatory rules require that a human technician must review all AI-generated recommendations. The company needs to establish human oversight workflows to review and approve AI recommendations. The company must store all human technician review decisions for audit purposes.  
  
Which solution will meet these requirements?

- Create a custom approval workflow by using AWS Lambda functions and Amazon SQS queues for human review of AI recommendations. Store all review decisions in Amazon DynamoDB for audit purposes.
- Create an AWS Step Functions workflow that has a human approval step that uses the waitForTaskToken API to pause execution. After a human technician completes a review, use an AWS Lambda function to call the SendTaskSuccess API with the approval decision. Store all review decisions in Amazon DynamoDcorrect
- Create an AWS Glue workflow that has a human approval step. After the human technician review, integrate the application with an AWS Lambda function that calls the SendTaskSuccess AP
- Store all human technician review decisions in Amazon DynamoD
- Configure Amazon EventBridge rules with custom event patterns to route AI recommendations to human technicians for review. Create AWS Glue jobs to process human technician approval queues. Use Amazon ElastiCache to cache all human technician review decisions.

Explanation:

AWS Step Functions provides native support for human-in-the-loop workflows, making it the best fit for regulatory oversight requirements. The waitForTaskToken integration pattern is explicitly designed to pause a workflow until an external actor―such as a human reviewer―completes a task.

In this architecture, AI-generated recommendations are sent to a human technician for review. The workflow pauses execution using a task token. Once the technician approves or rejects the recommendation, an AWS Lambda function calls SendTaskSuccess or SendTaskFailure, allowing the workflow to continue deterministically.

This approach ensures full auditability, as Step Functions records every state transition, timestamp, and execution path. Storing review outcomes in Amazon DynamoDB provides durable, queryable audit records required for regulatory compliance.

Option A requires custom orchestration and lacks native workflow state management.

Option C incorrectly uses AWS Glue, which is not designed for approval workflows.

Option D uses caching instead of durable audit storage and introduces unnecessary complexity.

Therefore, Option B is the AWS-recommended, lowest-risk, and most auditable solution for

mandatory human review of AI outputs.

7. A company uses an AI assistant application to summarize the company’s website content and provide information to customers. The company plans to use Amazon Bedrock to give the application access to a foundation model (FM).  
  
The company needs to deploy the AI assistant application to a development environment and a production environment. The solution must integrate the environments with the FM. The company wants to test the effectiveness of various FMs in each environment. The solution must provide product owners with the ability to easily switch between FMs for testing purposes in each environment.  
  
Which solution will meet these requirements?

- Create one AWS CDK application. Create multiple pipelines in AWS CodePipeline. Configure each pipeline to have its own settings for each F
- Configure the application to invoke the Amazon Bedrock FMs by using the aws_bedrock.ProvisionedModel.fromProvisionedModelArn() method.
- Create a separate AWS CDK application for each environment. Configure the applications to invoke the Amazon Bedrock FMs by using the aws_bedrock.FoundationModel.fromFoundationModelId() method. Create a separate pipeline in AWS CodePipeline for each environment.correct
- Create one AWS CDK application. Configure the application to invoke the Amazon Bedrock FMs by using the aws_bedrock.FoundationModel.fromFoundationModelId() method. Create a pipeline in AWS CodePipeline that has a deployment stage for each environment that uses AWS CodeBuild deploy actions.wrong
- Create one AWS CDK application for the production environment. Configure the application to invoke the Amazon Bedrock FMs by using the aws_bedrock.ProvisionedModel.fromProvisionedModelArn() method. Create a pipeline in AWS CodePipeline. Configure the pipeline to deploy to the production environment by using an AWS CodeBuild deploy action. For the development environment, manually recreate the resources by referring to the production application code.

Explanation:

Option C best satisfies the requirement for flexible FM testing across environments while minimizing

operational complexity and aligning with AWS-recommended deployment practices. Amazon Bedrock supports invoking on-demand foundation models through the FoundationModel abstraction, which allows applications to dynamically reference different models without requiring dedicated provisioned capacity. This is ideal for experimentation and A/B testing in both development and production environments.

Using a single AWS CDK application ensures infrastructure consistency and reduces duplication. Environment-specific configuration, such as selecting different foundation model IDs, can be externalized through parameters, context variables, or environment-specific configuration files. This allows product owners to easily switch between FMs in each environment without modifying application logic.

A single AWS CodePipeline with distinct deployment stages for development and production is an AWS best practice for multi-environment deployments. It enforces consistent build and deployment steps while still allowing environment-level customization. AWS CodeBuild deploy actions enable automated, repeatable deployments, reducing manual errors and improving governance.

Option A increases complexity by introducing multiple pipelines and relies on provisioned models, which are not necessary for FM evaluation and experimentation. Provisioned throughput is better suited for predictable, high-volume production workloads rather than frequent model switching.

Option B creates unnecessary operational overhead by duplicating CDK applications and pipelines, making long-term maintenance more difficult.

Option D directly conflicts with infrastructure-as-code best practices by manually recreating development resources, which increases configuration drift and reduces reliability.

Therefore, Option C provides the most flexible, scalable, and AWS-aligned solution for testing and switching foundation models across development and production environments.

8. A company is developing a generative AI (GenAI) application that uses Amazon Bedrock foundation models. The application has several custom tool integrations. The application has experienced unexpected token consumption surges despite consistent user traffic.  
  
The company needs a solution that uses Amazon Bedrock model invocation logging to monitor InputTokenCount and OutputTokenCount metrics. The solution must detect unusual patterns in tool usage and identify which specific tool integrations cause abnormal token consumption. The solution must also automatically adjust thresholds as traffic patterns change.  
  
Which solution will meet these requirements?

- Use Amazon CloudWatch Logs to capture model invocation logs. Create CloudWatch dashboards for token metrics. Configure static CloudWatch alarms with fixed thresholds for each tool integration.
- Store model invocation logs in Amazon S3. Use AWS Glue and Amazon Athena to analyze token usage trends.
- Use Amazon CloudWatch Logs to capture model invocation logs. Create CloudWatch metric filters to extract tool-specific invocation patterns. Apply CloudWatch anomaly detection alarms that automatically adjust baselines for each tool’s token metrics.correct
- Store model invocation logs in an Amazon S3 bucket. Use AWS Lambda to process logs in real time. Manually update CloudWatch alarm thresholds based on trends identified by the Lambda function.

Explanation:

Option C best meets the requirements by combining native Amazon Bedrock logging with adaptive monitoring and minimal operational overhead. Amazon Bedrock model invocation logging can be sent directly to CloudWatch Logs, where detailed fields such as InputTokenCount, OutputTokenCount, and tool invocation metadata are captured for each request.

CloudWatch metric filters allow extraction of structured metrics from logs, including tool-specific token consumption patterns. By defining filters per tool integration, the company can isolate which tools are responsible for increased token usage without building custom log-processing pipelines.

CloudWatch anomaly detection provides automatic baseline modeling and dynamic thresholds based on historical traffic patterns. Unlike static alarms, anomaly detection adapts as usage evolves, making it ideal for applications with changing workloads or seasonal usage patterns. This directly satisfies the requirement to automatically adjust thresholds as traffic patterns change.

When abnormal token consumption occurs, anomaly detection alarms trigger immediately, enabling rapid investigation and remediation. Because this solution uses fully managed AWS services without custom analytics jobs or manual threshold tuning, it significantly reduces operational effort.

Option A fails to adapt to changing patterns.

Option B introduces batch analysis and delayed insights.

Option D requires manual intervention and custom code, increasing maintenance burden.

Therefore, Option C provides the most scalable, adaptive, and low-maintenance solution for monitoring and controlling token consumption in Amazon BedrockCbased applications.

9. A company uses AWS Lambda functions to build an AI agent solution. A GenAI developer must set up a Model Context Protocol (MCP) server that accesses user information. The GenAI developer must also configure the AI agent to use the new MCP server. The GenAI developer must ensure that only authorized users can access the MCP server.  
  
Which solution will meet these requirements?

- Use a Lambda function to host the MCP server. Grant the AI agent Lambda functions permission to invoke the Lambda function that hosts the MCP server. Configure the AI agent’s MCP client to invoke  
    the MCP server asynchronously.wrong
- Use a Lambda function to host the MCP server. Grant the AI agent Lambda functions permission to invoke the Lambda function that hosts the MCP server. Configure the AI agent to use the STDIO transport with the MCP server.
- Use a Lambda function to host the MCP server. Create an Amazon API Gateway HTTP API that proxies requests to the Lambda function. Configure the AI agent solution to use the Streamable HTTP transport to make requests through the HTTP APcorrect
- Use Amazon Cognito to enforce OAuth 2.1.
- Use a Lambda layer to host the MCP server. Add the Lambda layer to the AI agent Lambda functions. Configure the agentic AI solution to use the STDIO transport to send requests to the MCP server. In the AI agent’s MCP configuration, specify the Lambda layer ARN as the command. Specify the user credentials as environment variables.

Explanation:

Option C is the correct solution because it provides a secure, scalable, and standards-compliant way to expose an MCP server to an AI agent while enforcing strong user authorization. The Model Context Protocol supports HTTP-based transports for remote MCP servers, making Streamable HTTP the appropriate choice when the server is hosted as a managed service rather than a local process.

Hosting the MCP server in AWS Lambda enables automatic scaling and cost-efficient execution. By placing Amazon API Gateway in front of the Lambda function, the company creates a secure, managed HTTP endpoint that the AI agent can invoke reliably. This architecture cleanly separates transport, authentication, and business logic, which aligns with AWS serverless best practices.

Using Amazon Cognito to enforce OAuth 2.1 ensures that only authenticated and authorized users can access the MCP server. This satisfies security and compliance requirements when the MCP server handles sensitive user information. Cognito integrates natively with API Gateway, removing the need for custom authentication logic and reducing operational overhead.

Option A lacks user-level authorization controls.

Option B and Option D rely on STDIO transport, which is intended for local or tightly coupled processes and is not suitable for distributed, serverless architectures.

Option D also introduces security risks by handling credentials through environment variables.

Therefore, Option C best meets the requirements for secure access control, scalability, and correct MCP integration in an AWS-based AI agent architecture.

10. A company is using Amazon Bedrock and Anthropic Claude 3 Haiku to develop an AI assistant. The AI assistant normally processes 10,000 requests each hour but experiences surges of up to 30,000 requests each hour during peak usage periods. The AI assistant must respond within 2 seconds while operating across multiple AWS Regions.  
  
The company observes that during peak usage periods, the AI assistant experiences throughput bottlenecks that cause increased latency and occasional request timeouts. The company must  
  
resolve the performance issues.  
  
Which solution will meet this requirement?

- Purchase provisioned throughput and sufficient model units (MUs) in a single Region. Configure the application to retry failed requests with exponential backoff.
- Implement token batching to reduce API overhead. Use cross-Region inference profiles to automatically distribute traffic across available Regions.correct
- Set up auto scaling AWS Lambda functions in each Region. Implement client-side round-robin request distribution. Purchase one model unit (MU) of provisioned throughput as a backup.wrong
- Implement batch inference for all requests by using Amazon S3 buckets across multiple Regions. Use Amazon SQS to set up an asynchronous retrieval process.

Explanation:

Option B is the correct solution because it directly addresses both throughput bottlenecks and latency requirements using native Amazon Bedrock performance optimization features that are designed for real-time, high-volume generative AI workloads.

Amazon Bedrock supports cross-Region inference profiles, which allow applications to transparently route inference requests across multiple AWS Regions. During peak usage periods, traffic is automatically distributed to Regions with available capacity, reducing throttling, request queuing, and timeout risks. This approach aligns with AWS guidance for building highly available, low-latency GenAI applications that must scale elastically across geographic boundaries.

Token batching further improves efficiency by combining multiple inference requests into a single model invocation where applicable. AWS Generative AI documentation highlights batching as a key optimization technique to reduce per-request overhead, improve throughput, and better utilize model capacity. This is especially effective for lightweight, low-latency models such as Claude 3 Haiku, which are designed for fast responses and high request volumes.

Option A does not meet the requirement because purchasing provisioned throughput in a single Region creates a regional bottleneck and does not address multi-Region availability or traffic spikes beyond reserved capacity. Retries increase load and latency rather than resolving the root cause.

Option C improves application-layer scaling but does not solve model-side throughput limits. Client-side round-robin routing lacks awareness of real-time model capacity and can still send traffic to saturated Regions.

Option D is unsuitable because batch inference with asynchronous retrieval is designed for offline or non-interactive workloads. It cannot meet a strict 2-second response time requirement for an

interactive AI assistant.

Therefore, Option B provides the most effective and AWS-aligned solution to achieve low latency, global scalability, and high throughput during peak usage periods.

11. A company uses AWS Lake Formation to set up a data lake that contains databases and tables for multiple business units across multiple AWS Regions. The company wants to use a foundation model (FM) through Amazon Bedrock to perform fraud detection. The FM must ingest sensitive financial data from the data lake. The data includes some customer personally identifiable information (PII).  
  
The company must design an access control solution that prevents PII from appearing in a production environment. The FM must access only authorized data subsets that have PII redacted from specific data columns. The company must capture audit trails for all data access.  
  
Which solution will meet these requirements?

- Create a separate dataset in a separate Amazon S3 bucket for each business unit and Region combination. Configure S3 bucket policies to control access based on IAM roles that are assigned to FM training instances. Use S3 access logs to track data access.
- Configure the FM to authenticate by using AWS Identity and Access Management roles and Lake Formation permissions based on LF-Tag expressions. Define business units and Regions as LF-Tags that are assigned to databases and tables. Use AWS CloudTrail to collect comprehensive audit trails of data access.correct
- Use direct IAM principal grants on specific databases and tables in Lake Formation. Create a custom application layer that logs access requests and further filters sensitive columns before sending data to the F
- Configure the FM to request temporary credentials from AWS Security Token Service. Access the data by using presigned S3 URLs that are generated by an API that applies business unit and Regional filters. Use AWS CloudTrail to collect comprehensive audit trails of data access.

Explanation:

Option B is the correct solution because it uses native AWS governance, access control, and auditing capabilities to protect PII while enabling controlled FM access to authorized data subsets. AWS Lake Formation is designed specifically to manage fine-grained permissions for data lakes, including column-level access control, which is critical when handling sensitive financial and PII data.

LF-Tags allow data administrators to define scalable, attribute-based access control policies. By tagging databases, tables, and columns with business unit and Region metadata, the company can enforce policies that ensure the foundation model only accesses approved datasets with PII-redacted columns. This eliminates the risk of sensitive data leaking into production inference workflows.

IAM role-based authentication ensures that the FM accesses data using least-privilege credentials. This integrates cleanly with Amazon Bedrock, which supports IAM-based authorization for service-to-service access. AWS CloudTrail provides immutable audit logs for all access attempts, satisfying compliance and regulatory requirements.

Option A introduces unnecessary data duplication and weak governance controls.

Option C relies on custom application logic, increasing operational risk and complexity.

Option D bypasses Lake Formation’s fine-grained controls and relies on presigned URLs, which reduces governance visibility and control.

Therefore, Option B best meets the requirements for security, compliance, scalability, and auditability when integrating Amazon Bedrock with a Lake FormationCgoverned data lake.

12. A medical company is building a generative AI (GenAI) application that uses Retrieval Augmented Generation (RAG) to provide evidence-based medical information. The application uses Amazon OpenSearch Service to retrieve vector embeddings. Users report that searches frequently miss results that contain exact medical terms and acronyms and return too many semantically similar but irrelevant documents. The company needs to improve retrieval quality and maintain low end-user latency, even as the document collection grows to millions of documents.  
  
Which solution will meet these requirements with the LEAST operational overhead?

- Configure hybrid search by combining vector similarity with keyword matching to improve semantic understanding and exact term and acronym matching.correct
- Increase the dimensions of the vector embeddings from 384 to 1536. Use a post-processing AWS Lambda function to filter out irrelevant results after retrieval.
- Replace OpenSearch Service with Amazon Kendra. Use query expansion to handle medical acronyms and terminology variants during pre-processing.wrong
- Implement a two-stage retrieval architecture in which initial vector search results are re-ranked by an ML model hosted on Amazon SageMaker.

Explanation:

Option A is the correct solution because hybrid search directly addresses the core retrieval failure modes while maintaining low latency and minimal operational overhead. In medical and scientific domains, exact terminology, abbreviations, and acronyms (for example, drug names, procedures, or conditions) are critical. Pure vector similarity search often underweights these exact matches, leading to missed results and excessive semantically related but irrelevant documents.

Amazon OpenSearch Service natively supports hybrid search, which combines keyword-based retrieval (such as BM25) with vector similarity search. Keyword search ensures precise matching for exact terms and acronyms, while vector search captures semantic meaning and contextual similarity. By blending these approaches, the retrieval system improves both precision and recall without introducing additional infrastructure.

Hybrid search operates within the same OpenSearch index and query path, which preserves low end-user latency even at large scale. This is especially important as the document collection grows to millions of documents. Because OpenSearch handles scoring and ranking internally, no additional orchestration layers or post-processing steps are required.

Option B increases computational cost and latency while failing to address exact-term recall.

Option C introduces a new service and ingestion pipeline, increasing operational overhead and latency.

Option D adds model hosting, re-ranking infrastructure, and complexity that is unnecessary when OpenSearch provides native hybrid retrieval.

Therefore, Option A delivers the best balance of retrieval quality, scalability, latency, and operational simplicity for medical RAG workloads.

13. A company is developing a generative AI (GenAI) application that analyzes customer service calls in real time and generates suggested responses for human customer service agents. The application must process 500,000 concurrent calls during peak hours with less than 200 ms end-to-end latency for each suggestion. The company uses existing architecture to transcribe customer call audio streams. The application must not exceed a predefined monthly compute budget and must maintain auto scaling capabilities.  
  
Which solution will meet these requirements?

- Deploy a large, complex reasoning model on Amazon Bedrock. Purchase provisioned throughput and optimize for batch processing.
- Deploy a low-latency, real-time optimized model on Amazon Bedrock. Purchase provisioned throughput and set up automatic scaling policies.correct
- Deploy a large language model (LLM) on an Amazon SageMaker real-time endpoint that uses  
    dedicated GPU instances.
- Deploy a mid-sized language model on an Amazon SageMaker serverless endpoint that is optimized for batch processing.

Explanation:

Option B is the correct solution because it aligns with AWS guidance for building high-throughput, ultra-low-latency GenAI applications while maintaining predictable costs and automatic scaling. Amazon Bedrock provides access to foundation models that are specifically optimized for real-time inference use cases, including conversational and recommendation-style workloads that require responses within milliseconds.

Low-latency models in Amazon Bedrock are designed to handle very high request rates with minimal per-request overhead. Purchasing provisioned throughput ensures that sufficient model capacity is reserved to handle peak loads, eliminating cold starts and reducing request queuing during traffic surges. This is critical when supporting up to 500,000 concurrent calls with strict latency requirements.

Automatic scaling policies allow the application to dynamically adjust capacity based on demand, ensuring cost efficiency during off-peak hours while maintaining performance during peak usage. This directly supports the requirement to stay within a predefined monthly compute budget.

Option A fails because batch processing and complex reasoning models introduce higher latency and are not suitable for real-time suggestions.

Option C introduces significantly higher operational and cost overhead due to dedicated GPU instances and manual scaling responsibilities.

Option D is optimized for batch workloads and cannot meet the sub-200 ms latency requirement.

Therefore, Option B provides the best balance of performance, scalability, cost control, and operational simplicity using AWS-native GenAI services.

14. A media company must use Amazon Bedrock to implement a robust governance process for AI-generated content. The company needs to manage hundreds of prompt templates. Multiple teams use the templates across multiple AWS Regions to generate content. The solution must provide version control with approval workflows that include notifications for pending reviews. The solution must also provide detailed audit trails that document prompt activities and consistent prompt parameterization to enforce quality standards.  
  
Which solution will meet these requirements?

- Configure Amazon Bedrock Studio prompt templates. Use Amazon CloudWatch dashboards to display prompt usage metrics. Store approval status in Amazon DynamoDwrong
- Use AWS Lambda functions to enforce approvals.correct
- Use Amazon Bedrock Prompt Management to implement version control. Configure AWS CloudTrail for audit logging. Use AWS Identity and Access Management policies to control approval permissions. Create parameterized prompt templates by specifying variables.
- Use AWS Step Functions to create an approval workflow. Store prompts in Amazon S3. Use tags to implement version control. Use Amazon EventBridge to send notifications.
- Deploy Amazon SageMaker Canvas with prompt templates stored in Amazon S3. Use AWS CloudFormation for version control. Use AWS Config to enforce approval policies.

Explanation:

Option B is the correct solution because Amazon Bedrock Prompt Management is purpose-built to manage, govern, and standardize prompt usage at scale across teams and Regions. It provides native version control, allowing teams to track prompt changes over time and ensure that only approved versions are used in production workflows.

Prompt Management supports approval workflows that align with enterprise governance requirements. Approval permissions can be enforced through IAM policies, ensuring that only authorized reviewers can approve or publish prompt versions. This removes the need for custom workflow engines or external storage systems, significantly reducing operational overhead.

Parameterized prompt templates enable consistent prompt structure while allowing controlled variation through defined variables. This ensures consistent quality standards and reduces prompt drift, which is critical when hundreds of prompts are reused across multiple applications and teams.

AWS CloudTrail integrates natively with Amazon Bedrock to provide immutable audit logs for prompt creation, updates, approvals, and usage. These detailed audit trails satisfy compliance requirements and allow security and governance teams to trace prompt activity across Regions and users.

Option A requires significant custom development to coordinate approvals and maintain state.

Option C relies on general-purpose workflow services and manual versioning mechanisms that are error-prone and difficult to scale.

Option D uses services not designed for large-scale GenAI prompt governance and introduces unnecessary complexity.

Therefore, Option B best meets the requirements for scalable, auditable, and low-overhead governance of AI-generated content using Amazon Bedrock.

15. An enterprise application uses an Amazon Bedrock foundation model (FM) to process and analyze 50 to 200 pages of technical documents. Users are experiencing inconsistent responses and receiving truncated outputs when processing documents that exceed the FM's context window limits.  
  
Which solution will resolve this problem?

- Configure fixed-size chunking at 4,000 tokens for each chunk with 20% overlap. Use application-level logic to link multiple chunks sequentially until the FM's maximum context window of 200,000 tokens is reached before making inference calls.wrong
- Use hierarchical chunking with parent chunks of 8,000 tokens and child chunks of 2,000 tokens. Use Amazon Bedrock Knowledge Bases built-in retrieval to automatically select relevant parent chunks based on query context. Configure overlap tokens to maintain semantic continuity.
- Use semantic chunking with a breakpoint percentile threshold of 95% and a buffer size of 3 sentences. Use the RetrieveAndGenerate API to dynamically select the most relevant chunks based on embedding similarity scores.correct
- Create a pre-processing AWS Lambda function that analyzes document token count by using the FM's tokenizer. Configure the Lambda function to split documents into equal segments that fit within 80% of the context window. Configure the Lambda function to process each segment independently before aggregating the results.

Explanation:

Option C directly addresses the root cause of truncated and inconsistent responses by using AWS-recommended semantic chunking and dynamic retrieval rather than static or sequential chunk processing. Amazon Bedrock documentation emphasizes that foundation models have fixed context windows and that sending oversized or poorly structured input can lead to truncation, loss of context, and degraded output quality.

Semantic chunking breaks documents based on meaning instead of fixed token counts. By using a breakpoint percentile threshold and sentence buffers, the content remains coherent and semantically complete. This approach reduces the likelihood that important concepts are split across chunks, which is a common cause of inconsistent summarization results.

The RetrieveAndGenerate API is designed specifically to handle large documents that exceed a model’s context window. Instead of forcing all content into a single inference call, the API generates embeddings for chunks and dynamically selects only the most relevant chunks based on similarity to the user query. This ensures that the FM receives only high-value context while staying within its context window limits.

Option A is ineffective because chaining chunks sequentially does not align with how FMs process context and risks exceeding context limits or introducing irrelevant information.

Option B improves structure but still relies on larger parent chunks, which can lead to inefficiencies when processing very large documents.

Option D processes segments independently, which often causes loss of global context and inconsistent summaries.

Therefore, Option C is the most robust, AWS-aligned solution for resolving truncation and consistency issues when processing large technical documents with Amazon Bedrock.

16. An ecommerce company is using Amazon Bedrock to build a generative AI (GenAI) application. The application uses AWS Step Functions to orchestrate a multi-agent workflow to produce detailed product descriptions. The workflow consists of three sequential states: a description generator, a technical specifications validator, and a brand voice consistency checker. Each state produces intermediate reasoning traces and outputs that are passed to the next state. The application uses an Amazon S3 bucket for process storage and to store outputs.  
  
During testing, the company discovers that outputs between Step Functions states frequently exceed the 256 KB quota and cause workflow failures. A GenAI Developer needs to revise the application architecture to efficiently handle the Step Functions 256 KB quota and maintain workflow observability. The revised architecture must preserve the existing multi-agent reasoning and acting (ReAct) pattern.  
  
Which solution will meet these requirements with the LEAST operational overhead?

- Store intermediate outputs in Amazon DynamoD
- Pass only references between states. Create a Map state that retrieves the complete data from DynamoDB when required for each agent's processing step.correct
- Configure an Amazon Bedrock integration to use the S3 bucket URI in the input parameters for large outputs. Use the ResultPath and ResultSelector fields to route S3 references between the agent steps while maintaining the sequential validation workflow.wrong
- Use AWS Lambda functions to compress outputs to less than 256 KB before each agent state. Configure each agent task to decompress outputs before processing and to compress results before passing them to the next state.
- Configure a separate Step Functions state machine to handle each agent’s processing. Use Amazon EventBridge to coordinate the execution flow between state machines. Use S3 references for the outputs as event data.

Explanation:

Option B is the best solution because it directly addresses the Step Functions 256 KB state payload quota by externalizing large intermediate artifacts to Amazon S3 and passing only lightweight references (URIs/keys) between states. This is a standard AWS pattern for workflows that produce large intermediate results, and it avoids introducing additional databases, compression logic, or cross-state-machine coordination that increases operational overhead.

In a multi-agent ReAct workflow, intermediate reasoning traces can be verbose and grow quickly as each agent produces chain-of-thought style artifacts, structured outputs, and supporting evidence. Step Functions is designed to orchestrate state transitions and pass JSON payloads, but large payloads should be stored outside the state machine and referenced by pointer values. Using Amazon S3 for intermediate outputs is operationally efficient because the application already uses S3 for storage, and S3 provides durable, low-cost storage with simple access patterns.

ResultPath and ResultSelector allow each state to store or reshape results so that only the required reference fields (such as s3Uri, object key, metadata, trace IDs) are forwarded to subsequent states. This preserves observability because the workflow can still log trace references, correlate steps with S3 objects, and store structured metadata for debugging. It also preserves the sequential validation design, keeping the existing ReAct pattern intact while preventing failures due to oversized payloads.

Option A adds additional services and read/write patterns that increase operational complexity.

Option C introduces custom compression/decompression logic that is fragile, adds latency, and complicates troubleshooting.

Option D increases orchestration overhead by splitting workflows and coordinating with events, which makes debugging harder and increases failure modes.

Therefore, Option B meets the payload limit requirement while keeping the architecture simple and observable.

17. A company is using Amazon Bedrock to build a customer-facing AI assistant that handles sensitive customer inquiries. The company must use defense-in-depth safety controls to block sophisticated prompt injection attacks. The company must keep audit logs of all safety interventions. The AI assistant must have cross-Region failover capabilities.  
  
Which solution will meet these requirements?

- Configure Amazon Bedrock guardrails with content filters set to high to protect against prompt injection attacks. Use a guardrail profile to implement cross-Region guardrail inference. Use Amazon CloudWatch Logs with custom metrics to capture detailed guardrail intervention events.correct
- Configure Amazon Bedrock guardrails with content filters set to high. Use AWS WAF to block suspicious inputs. Use AWS CloudTrail to log API calls.
- Deploy Amazon Comprehend custom classifiers to detect prompt injection attacks. Use Amazon API Gateway request validation. Use CloudWatch Logs to capture intervention events.
- Configure Amazon Bedrock guardrails with custom content filters and word filters set to high. Configure cross-Region guardrail replication for failover. Store logs in AWS CloudTrail for compliance auditing.wrong

Explanation:

Option A provides the most complete, AWS-native defense-in-depth solution for protecting against prompt injection attacks while meeting audit and resiliency requirements. Amazon Bedrock guardrails are designed specifically to enforce safety policies on both user inputs and model outputs, including protections against prompt injection and jailbreak attempts.

Setting content filters to high increases sensitivity to malicious or manipulative inputs. Guardrail profiles allow the same guardrail configuration to be applied consistently across multiple Regions, enabling cross-Region inference and failover without configuration drift. This directly satisfies the requirement for regional resilience.

Amazon CloudWatch Logs captures detailed guardrail intervention events, including when content is blocked, modified, or flagged. Custom metrics derived from these logs enable fine-grained auditing, alerting, and reporting on safety enforcement actions. This provides a more detailed audit trail of safety interventions than API-level logs alone.

Option B adds WAF protection but lacks detailed guardrail intervention logging.

Option C introduces additional services and custom logic that increase complexity and may miss model-specific injection patterns.

Option D references replication concepts that are not aligned with Bedrock guardrail operational models and relies on word filters, which are insufficient against sophisticated prompt injection techniques.

Therefore, Option A best meets the requirements for layered protection, auditability, and cross-Region resilience using managed Amazon Bedrock safety controls.

18. A retail company has a generative AI (GenAI) product recommendation application that uses Amazon Bedrock. The application suggests products to customers based on browsing history and demographics. The company needs to implement fairness evaluation across multiple demographic groups to detect and measure bias in recommendations between two prompt approaches. The company wants to collect and monitor fairness metrics in real time. The company must receive an alert if the fairness metrics show a discrepancy of more than 15% between demographic groups. The company must receive weekly reports that compare the performance of the two prompt approaches.  
  
Which solution will meet these requirements with the LEAST custom development effort?

- Configure an Amazon CloudWatch dashboard to display default metrics from Amazon Bedrock API calls. Create custom metrics based on model outputs. Set up Amazon EventBridge rules to invoke AWS Lambda functions that perform post-processing analysis on model responses and publish custom fairness metrics.
- Create the two prompt variants in Amazon Bedrock Prompt Management. Use Amazon Bedrock Flows to deploy the prompt variants with defined traffic allocation. Configure Amazon Bedrock guardrails to monitor demographic fairness. Set up Amazon CloudWatch alarms on the Guardrail Content Source dimension by using Invocations Intervened metrics to detect recommendation discrepancy threshold violations.correct
- Set up Amazon SageMaker Clarify to analyze model outputs. Publish fairness metrics to Amazon CloudWatch. Create CloudWatch composite alarms that combine SageMaker Clarify bias metrics with Amazon Bedrock latency metrics.
- Create an Amazon Bedrock model evaluation job to compare fairness between the two prompt variants. Enable model invocation logging in Amazon CloudWatch. Set up CloudWatch alarms for Invocations Intervened metrics with a dimension for each demographic group.

Explanation:

Option B best satisfies the requirements with the least custom development effort by using native Amazon Bedrock capabilities for prompt experimentation, traffic management, fairness monitoring, and alerting. Amazon Bedrock Prompt Management allows teams to define and manage multiple prompt variants without code changes, making it ideal for comparing recommendation strategies across demographic groups.

Amazon Bedrock Flows enables controlled traffic allocation between prompt variants, which supports real-time A/B testing. This allows the company to collect live fairness metrics under production conditions instead of relying on offline analysis. Because Flows are fully managed, they eliminate the need for custom routing or experimentation frameworks.

Amazon Bedrock guardrails provide built-in monitoring and intervention mechanisms. When configured for fairness-related checks, guardrails can detect policy violations and surface metrics such as Invocations Intervened, which indicate when outputs are modified or blocked due to rule enforcement. These metrics integrate directly with Amazon CloudWatch, enabling real-time dashboards and threshold-based alarms. Setting an alarm at a 15% discrepancy threshold satisfies the alerting requirement with minimal configuration.

Weekly reporting can be generated from CloudWatch metrics using scheduled exports or dashboards without building custom analytics pipelines.

Option A requires significant custom post-processing logic.

Option C introduces an additional service with higher operational overhead and is not optimized for real-time monitoring.

Option D focuses on offline evaluation jobs and does not provide continuous real-time fairness monitoring.

Therefore, Option B provides the most AWS-native, scalable, and low-effort solution for fairness evaluation and monitoring.

19. A company is developing a customer support application that uses Amazon Bedrock foundation models (FMs) to provide real-time AI assistance to the company’s employees. The application must display AI-generated responses character by character as the responses are generated. The application needs to support thousands of concurrent users with minimal latency. The responses typically take 15 to 45 seconds to finish.  
  
Which solution will meet these requirements?

- Configure an Amazon API Gateway WebSocket API with an AWS Lambda integration. Configure the WebSocket API to invoke the Amazon Bedrock InvokeModelWithResponseStream API and stream partial responses through WebSocket connections.correct
- Configure an Amazon API Gateway REST API with an AWS Lambda integration. Configure the REST API to invoke the Amazon Bedrock standard InvokeModel API and implement frontend client-side polling every 100 ms for complete response chunks.
- Implement direct frontend client connections to Amazon Bedrock by using IAM user credentials and the InvokeModelWithResponseStream API without any intermediate gateway or proxy layer.
- Configure an Amazon API Gateway HTTP API with an AWS Lambda integration. Configure the HTTP API to cache complete responses in an Amazon DynamoDB table and serve the responses through multiple paginated GET requests to frontend clients.

Explanation:

This requirement explicitly calls for character-by-character streaming, long-running responses, low latency, and massive concurrency, which aligns directly with Amazon Bedrock streaming inference patterns.

Amazon Bedrock provides the InvokeModelWithResponseStream API specifically for streaming partial model outputs as tokens are generated. This enables near-instant feedback to users instead of waiting for the full response to complete, which is essential when responses last up to 45 seconds.

Amazon API Gateway WebSocket APIs are purpose-built for bidirectional, low-latency, server-initiated communication, allowing the backend to push characters or tokens to clients in real time. This eliminates inefficient polling and supports thousands of concurrent open connections.

AWS Lambda integrates natively with WebSocket APIs and scales automatically with connection volume, enabling a fully managed, serverless architecture. This approach maintains security, centralized authentication, throttling, and observability while avoiding direct client access to Bedrock APIs.

Option B introduces polling latency and unnecessary API overhead and does not provide true streaming.

Option C violates AWS security best practices by exposing Bedrock directly to clients and does not scale securely.

Option D only serves completed responses and cannot meet the real-time streaming requirement.

Therefore, Option A is the only solution that fully satisfies streaming behavior, concurrency, latency, and managed-service constraints.

20. A company is developing a generative AI (GenAI) application by using Amazon Bedrock. The application will analyze patterns and relationships in the company’s data. The application will process millions of new data points daily across AWS Regions in Europe, North America, and Asia before storing the data in Amazon S3.  
  
The application must comply with local data protection and storage regulations. Data residency and processing must occur within the same continent. The application must also maintain audit trails of the application’s decision-making processes and provide data classification capabilities.  
  
Which solution will meet these requirements?

- Deploy the application in each Region with local IAM policies. Use Amazon Bedrock cross-Region inference to distribute the workload. Use Amazon CloudWatch to log AI decision-making processes. Manually track compliance certifications across Regions.
- Use SCPs with AWS Organizations to manage location-specific permissions. Use AWS CloudTrail immutable logs to audit decision-making processes. Import a custom model into Amazon Bedrock and deploy the model to each Region.
- Use Amazon S3 Object Lock with Region-specific S3 bucket policies. Pre-process the data points within the Region based on geographic origin before sending the data points to Amazon Bedrock. Use Amazon Macie to classify the data. Use AWS CloudTrail immutable logs to audit the decision-making processes.correct
- Create separate AWS accounts for each Region with individual compliance frameworks. Use Amazon SageMaker AI with custom monitoring. Create manual compliance reports for each regulatory jurisdiction.

Explanation:

This scenario requires strict data residency, regional processing, classification, and auditable decision trails, which Option C addresses using AWS-native governance services.

Region-specific Amazon S3 buckets enforce geographic data boundaries. Amazon S3 Object Lock ensures immutability of stored data and logs, supporting regulatory retention and non-repudiation requirements. Pre-processing data within the same Region before invoking Amazon Bedrock ensures that inference and data handling do not cross continental boundaries.

Amazon Macie provides managed, automated data classification for sensitive data types such as PII and financial records, fulfilling the classification requirement without custom tooling.

AWS CloudTrail immutable logs provide comprehensive audit trails of all API calls, model invocations, and data access events, ensuring traceability of AI decision-making processes.

Option A violates residency rules through cross-Region inference.

Option B does not provide data classification.

Option D introduces high operational overhead and relies on manual compliance reporting.

Therefore, Option C is the most compliant, scalable, and operationally efficient solution for regionally governed GenAI workloads.

21. A specialty coffee company has a mobile app that generates personalized coffee roast profiles by using Amazon Bedrock with a three-stage prompt chain. The prompt chain converts user inputs into structured metadata, retrieves relevant logs for coffee roasts, and generates a personalized roast recommendation for each customer.  
  
Users in multiple AWS Regions report inconsistent roast recommendations for identical inputs, slow inference during the retrieval step, and unsafe recommendations such as brewing at excessively high  
  
temperatures. The company must improve the stability of outputs for repeated inputs. The company must also improve app performance and the safety of the app’s outputs. The updated solution must ensure 99.5% output consistency for identical inputs and achieve inference latency of less than 1 second. The solution must also block unsafe or hallucinated recommendations by using validated safety controls.  
  
Which solution will meet these requirements?

- Deploy Amazon Bedrock with provisioned throughput to stabilize inference latency. Apply Amazon Bedrock guardrails with semantic denial rules to block unsafe outputs. Use Amazon Bedrock Prompt Management to manage prompts by using approval workflows.correct
- Use Amazon Bedrock Agents to manage chaining. Log model inputs and outputs to Amazon CloudWatch Logs. Use logs from CloudWatch to perform A/B testing for prompt versions.
- Cache prompt results in Amazon ElastiCache. Use AWS Lambda functions to pre-process metadata and to trace end-to-end latency. Use AWS X-Ray to identify and remediate performance bottlenecks.
- Use Amazon Kendra to improve roast log retrieval accuracy. Store normalized prompt metadata within Amazon DynamoDwrong
- Use AWS Step Functions to orchestrate multi-step prompts.

Explanation:

Option A is the only choice that simultaneously addresses all three requirements: (1) higher output consistency for identical inputs, (2) sub-1-second performance, and (3) validated safety controls that block unsafe or hallucinated recommendations.

Provisioned throughput in Amazon Bedrock reserves capacity for the chosen model, which helps stabilize latency and reduces the chance of throttling or variable response times across Regions. This is important for a mobile app with strict latency goals and users distributed across multiple Regions. While provisioned throughput primarily improves performance predictability, it also reduces variability caused by contention during peak demand.

Amazon Bedrock guardrails provide validated safety controls to filter or block unsafe content. Semantic denial rules are appropriate for preventing dangerous brewing guidance (for example, excessively high temperatures) and for reducing hallucinated instructions that violate safety policies. Guardrails can be enforced consistently regardless of prompt-chain complexity, providing a uniform safety layer around the model outputs.

Amazon Bedrock Prompt Management supports controlled prompt versioning and approval workflows. By standardizing prompts, controlling changes, and ensuring the same prompt version is used for identical inputs, the company improves output stability and reduces drift caused by unmanaged prompt edits. Combined with strict configuration control (including fixed inference

parameters such as temperature where appropriate), this improves repeatability and increases the likelihood of achieving the 99.5% consistency target.

Option B improves observability and experimentation but does not provide strong safety enforcement or latency stabilization.

Option C improves performance through caching and tracing but does not provide validated safety controls and does not directly address cross-Region output consistency.

Option D may improve retrieval but does not enforce safety controls or ensure repeatable outputs.

Therefore, Option A best meets the stability, performance, and safety requirements using AWS-native controls.

22. A company uses Amazon Bedrock to implement a Retrieval Augmented Generation (RAG)-based system to serve medical information to users. The company needs to compare multiple chunking strategies, evaluate the generation quality of two foundation models (FMs), and enforce quality thresholds for deployment.  
  
Which Amazon Bedrock evaluation configuration will meet these requirements?

- Create a retrieve-only evaluation job that uses a supported version of Anthropic Claude Sonnet as the evaluator model. Configure metrics for context relevance and context coverage. Define deployment thresholds in a separate CI/CD pipeline.
- Create a retrieve-and-generate evaluation job that uses custom precision-at-k metrics and an LLM-as-a-judge metric with a scale of 1C5. Include each chunking strategy in the evaluation dataset. Use a supported version of Anthropic Claude Sonnet to evaluate responses from both FMs.correct
- Create a separate evaluation job for each chunking strategy and FM combination. Use Amazon Bedrock built-in metrics for correctness and completeness. Manually review scores before deployment approval.
- Set up a pipeline that uses multiple retrieve-only evaluation jobs to assess retrieval quality. Create separate evaluation jobs for both FMs that use Amazon Nova Pro as the LLM-as-a-judge model. Evaluate based on faithfulness and citation precision metrics.

Explanation:

Option B is the correct evaluation configuration because it enables end-to-end assessment of both retrieval and generation quality while supporting direct comparison of chunking strategies and foundation models. Amazon Bedrock evaluation jobs are designed to support RAG workflows by evaluating how well retrieved context supports accurate and high-quality model outputs.

A retrieve-and-generate evaluation job evaluates the complete RAG pipeline, not just retrieval. This is essential for medical information use cases, where both the relevance of retrieved content and the correctness of generated responses directly impact user safety and trust. Including multiple chunking strategies in the evaluation dataset allows side-by-side comparison under identical prompts and conditions.

Custom precision-at-k metrics measure how effectively the retrieval component surfaces relevant chunks, while an LLM-as-a-judge metric provides qualitative scoring of generated responses. Using a numeric scale enables consistent, repeatable evaluation and supports automated quality gates. Amazon Bedrock supports LLM-based evaluators to score dimensions such as accuracy, completeness, and relevance.

Using the same evaluator model to assess outputs from both FMs ensures consistent scoring and eliminates evaluator bias. This configuration allows the company to define quantitative thresholds that must be met before deployment, enabling automated promotion through CI/CD pipelines.

Option A evaluates retrieval only and cannot assess generation quality.

Option C introduces manual review, which does not scale and delays deployment.

Option D separates retrieval and generation evaluation, making it harder to correlate chunking strategies with final output quality.

Therefore, Option B best meets the requirements for systematic evaluation, comparison, and quality enforcement in an Amazon BedrockCbased RAG system.

23. A financial services company is developing a real-time generative AI (GenAI) assistant to support human call center agents. The GenAI assistant must transcribe live customer speech, analyze context, and provide incremental suggestions to call center agents while a customer is still speaking. To preserve responsiveness, the GenAI assistant must maintain end-to-end latency under 1 second from speech to initial response display. The architecture must use only managed AWS services and must support bidirectional streaming to ensure that call center agents receive updates in real time.  
  
Which solution will meet these requirements?

- Use Amazon Transcribe streaming to transcribe calls. Pass the text to Amazon Comprehend for sentiment analysis. Feed the results to Anthropic Claude on Amazon Bedrock by using the Invoke Model AP
- Store results in Amazon DynamoDcorrect
- Use a WebSocket API to display the results.
- Use Amazon Transcribe streaming with partial results enabled to deliver fragments of transcribed text before customers finish speaking. Forward text fragments to Amazon Bedrock by using the InvokeModelWithResponseStream AP
- Stream responses to call center agents through an Amazon API Gateway WebSocket AP
- Use Amazon Transcribe batch processing to convert calls to text. Pass complete transcripts to Anthropic Claude on Amazon Bedrock by using the Converse Stream AP
- Return responses through an Amazon Lex chatbot interface.
- Use the Amazon Transcribe streaming API with an AWS Lambda function to transcribe each audio segment. Call the Amazon Titan Embeddings model on Amazon Bedrock by using the InvokeModel APwrong
- Publish results to Amazon SN

Explanation:

Option B is the only solution that satisfies all strict real-time, streaming, and latency requirements. Amazon Transcribe streaming with partial results allows transcription fragments to be delivered before the speaker finishes a sentence. This significantly reduces perceived latency and enables downstream processing to begin immediately, which is essential for maintaining sub-1-second end-to-end response times.

Using Amazon Bedrock’s InvokeModelWithResponseStream API enables token-level or chunk-level streaming responses from the foundation model. This allows the GenAI assistant to begin delivering suggestions to call center agents incrementally instead of waiting for a full model response. This streaming inference capability is critical for interactive, real-time agent assistance use cases.

Amazon API Gateway WebSocket APIs provide fully managed, bidirectional communication between backend services and agent dashboards. This ensures that updates flow continuously to agents as new transcription fragments and model outputs become available, preserving real-time responsiveness without requiring custom socket infrastructure.

Option A introduces additional synchronous processing layers and storage writes that increase latency.

Option C uses batch transcription and post-call processing, which cannot meet real-time requirements.

Option D uses embeddings and asynchronous messaging, which are not suitable for live incremental suggestions and bidirectional streaming.

Therefore, Option B best aligns with AWS real-time GenAI architecture patterns by combining streaming transcription, streaming model inference, and managed bidirectional communication while maintaining low latency and operational simplicity.

24. A company is building a serverless application that uses AWS Lambda functions to help students around the world summarize notes. The application uses Anthropic Claude through Amazon Bedrock. The company observes that most of the traffic occurs during evenings in each time zone. Users report experiencing throttling errors during peak usage times in their time zones.  
  
The company needs to resolve the throttling issues by ensuring continuous operation of the application. The solution must maintain application performance quality and must not require a fixed hourly cost during low traffic periods.  
  
Which solution will meet these requirements?

- Create custom Amazon CloudWatch metrics to monitor model errors. Set provisioned throughput to a value that is safely higher than the peak traffic observed.
- Create custom Amazon CloudWatch metrics to monitor model errors. Set up a failover mechanism to redirect invocations to a backup AWS Region when the errors exceed a specified threshold.
- Enable invocation logging in Amazon Bedrock. Monitor key metrics such as Invocations, InputTokenCount, OutputTokenCount, and InvocationThrottles. Distribute traffic across cross-Region inference endpoints.correct
- Enable invocation logging in Amazon Bedrock. Monitor InvocationLatency, InvocationClientErrors, and InvocationServerErrors metrics. Distribute traffic across multiple versions of the same model.

Explanation:

Option C is the correct solution because it resolves throttling while preserving performance and avoiding fixed costs during low-traffic periods. Amazon Bedrock supports on-demand inference with usage-based pricing, making it well suited for applications with time-zoneCdependent traffic spikes.

Throttling during peak hours typically occurs when inference requests exceed available regional capacity. Cross-Region inference allows Amazon Bedrock to automatically distribute requests across multiple AWS Regions, reducing contention and preventing throttling without requiring reserved or provisioned capacity. This approach ensures continuous operation while maintaining low latency for users in different geographic locations.

Invocation logging and native metrics such as InvocationThrottles, InputTokenCount, and OutputTokenCount provide visibility into usage patterns and capacity constraints. Monitoring these metrics enables teams to validate that traffic distribution is working as intended and that performance remains consistent during peak periods.

Option A introduces fixed hourly costs by relying on provisioned throughput, which directly violates the requirement to avoid unnecessary spend during low-traffic periods.

Option B introduces regional failover complexity and reactive behavior instead of proactive load distribution.

Option D does not address the root cause of throttling, as distributing traffic across model versions within the same Region does not increase available capacity.

Therefore, Option C best aligns with AWS Generative AI best practices for scalable, cost-efficient, global serverless applications.

25. A financial services company needs to pre-process unstructured data such as customer transcripts, financial reports, and documentation. The company stores the unstructured data in Amazon S3 to support an Amazon Bedrock application.  
  
The company must validate data quality, create auditable metadata, monitor data metrics, and  
  
customize text chunking to optimize foundation model (FM) performance.  
  
Which solution will meet these requirements with the LEAST development effort?

- Use Amazon SageMaker Data Wrangler to create a data flow. Configure Amazon CloudWatch metrics and alarms to monitor data quality. Use a custom AWS Lambda function to pre-process the data. Load processed data into Amazon Bedrock.
- Set up an AWS Glue crawler to catalog data sources. Create AWS Glue ETL jobs to run custom transformation scripts. Use AWS Glue Data Quality to validate and monitor data quality. Load processed data into Amazon Bedrock.correct
- Use Amazon Comprehend to extract entities. Create an AWS Lambda function to chunk text. Run Amazon Athena to query and validate data quality. Load processed data into Amazon Bedrock.
- Create an AWS Step Functions workflow to orchestrate data pre-processing tasks. Run custom code on Amazon EC2 instances. Use Amazon SageMaker Model Monitor to monitor data quality. Load processed data into Amazon Bedrock.

Explanation:

Option B is the most appropriate solution because it uses AWS-native, purpose-built data engineering and governance services to address data quality validation, metadata creation, monitoring, and transformation with minimal custom development. AWS Glue is designed specifically for large-scale data preparation and integrates seamlessly with Amazon S3, making it ideal for preprocessing unstructured datasets for downstream GenAI applications.

AWS Glue crawlers automatically infer schemas and populate the AWS Glue Data Catalog, creating auditable, queryable metadata for all datasets. This satisfies the requirement for traceability and governance, which is especially critical in financial services environments. Glue ETL jobs allow teams to implement customizable transformation logic, including text normalization and chunking strategies optimized for foundation model context windows.

AWS Glue Data Quality provides built-in rulesets for validating completeness, accuracy, and consistency. It also publishes quality metrics that can be monitored over time, meeting the requirement for ongoing data quality monitoring without building custom validation frameworks.

Because AWS Glue is fully managed, it eliminates the need to manage infrastructure, scaling, or orchestration. This significantly reduces development and operational effort compared to custom Lambda pipelines or EC2-based processing. The processed and validated data can then be safely ingested into Amazon Bedrock workflows or knowledge bases.

Option A and C require custom logic for validation, monitoring, and chunking, increasing development complexity.

Option D introduces unnecessary infrastructure management and services not optimized for data preprocessing.

Therefore, Option B best meets the requirements while minimizing development effort and aligning with AWS Generative AI data preparation best practices.

26. 1.A company provides a service that helps users from around the world discover new restaurants. The service has 50 million monthly active users. The company wants to implement a semantic search solution across a database that contains 20 million restaurants and 200 million reviews. The company currently stores the data in PostgreSQL.  
  
The solution must support complex natural language queries and return results for at least 95% of queries within 500 ms. The solution must maintain data freshness for restaurant details that update hourly. The solution must also scale cost-effectively during peak usage periods.  
  
Which solution will meet these requirements with the LEAST development effort?

- Migrate the restaurant data to Amazon OpenSearch Service. Implement keyword-based search rules that use custom analyzers and relevance tuning to find restaurants based on attributes such as cuisine type, features, and location. Create Amazon API Gateway HTTP API endpoints to transform user queries into structured search parameters.wrong
- Migrate the restaurant data to Amazon OpenSearch Service. Use a foundation model (FM) in Amazon Bedrock to generate vector embeddings from restaurant descriptions, reviews, and menu items. When users submit natural language queries, convert the queries to embeddings by using the same Fcorrect
- Perform k-nearest neighbors (k-NN) searches to find semantically similar results.
- Keep the restaurant data in PostgreSQL and implement a pgvector extension. Use a foundation model (FM) in Amazon Bedrock to generate vector embeddings from restaurant data. Store the vector embeddings directly in PostgreSQ
- Create an AWS Lambda function to convert natural language queries to vector representations by using the same F
- Configure the Lambda function to perform similarity searches within the database.
- Migrate restaurant data to an Amazon Bedrock knowledge base by using a custom ingestion pipeline. Configure the knowledge base to automatically generate embeddings from restaurant information. Use the Amazon Bedrock Retrieve API with built-in vector search capabilities to query the knowledge base directly by using natural language input.

Explanation:

Option B best satisfies the requirements while minimizing development effort by combining managed semantic search capabilities with fully managed foundation models. AWS Generative AI guidance describes semantic search as a vector-based retrieval pattern where both documents and user queries are embedded into a shared vector space. Similarity search (such as k-nearest neighbors) then retrieves results based on meaning rather than exact keywords.

Amazon OpenSearch Service natively supports vector indexing and k-NN search at scale. This makes it well suited for large datasets such as 20 million restaurants and 200 million reviews while still achieving sub-second latency for the majority of queries. Because OpenSearch is a distributed, managed service, it automatically scales during peak traffic periods and provides cost-effective performance compared with building and tuning custom vector search pipelines on relational databases.

Using Amazon Bedrock to generate embeddings significantly reduces development complexity. AWS manages the foundation models, eliminates the need for custom model hosting, and ensures consistency by using the same FM for both document embeddings and query embeddings. This aligns directly with AWS-recommended semantic search architectures and removes the need for model lifecycle management.

Hourly updates to restaurant data can be handled efficiently through incremental re-indexing in OpenSearch without disrupting query performance. This approach cleanly separates transactional data storage from search workloads, which is a best practice in AWS architectures.

Option A does not meet the semantic search requirement because keyword-based search cannot reliably interpret complex natural language intent.

Option C introduces scalability and performance risks by running large-scale vector similarity searches inside PostgreSQL, which increases operational complexity.

Option D adds unnecessary ingestion and abstraction layers intended for retrieval-augmented generation, not high-throughput semantic search.

Therefore, Option B provides the optimal balance of performance, scalability, data freshness, and minimal development effort using AWS Generative AI services.

27. An ecommerce company is developing a generative AI (GenAI) solution that uses Amazon Bedrock with Anthropic Claude to recommend products to customers. Customers report that some recommended products are not available for sale or are not relevant. Customers also report long response times for some recommendations.  
  
The company confirms that most customer interactions are unique and that the solution recommends products not present in the product catalog.  
  
Which solution will meet this requirement?

- Increase grounding within Amazon Bedrock Guardrails. Enable automated reasoning checks. Set up provisioned throughput.wrong
- Use prompt engineering to restrict model responses to relevant products. Use streaming inference to reduce perceived latency.
- Create an Amazon Bedrock Knowledge Bases and implement Retrieval Augmented Generation (RAG). Set the PerformanceConfigLatency parameter to optimized.correct
- Store product catalog data in Amazon OpenSearch Service. Validate model recommendations against the catalog. Use Amazon DynamoDB for response caching.

Explanation:

Option C is the correct solution because it directly addresses both correctness and performance issues by grounding the model’s responses in authoritative product data using Retrieval Augmented Generation. Amazon Bedrock Knowledge Bases are designed to connect foundation models to trusted enterprise data sources, ensuring that generated responses are constrained to known, validated content.

By ingesting the product catalog into a knowledge base, the GenAI application retrieves only products that actually exist in the catalog. This prevents hallucinated or unavailable recommendations, which is a common issue when models rely solely on prompt instructions without retrieval grounding. RAG ensures that the model’s output is based on retrieved facts rather than learned generalizations.

Setting the PerformanceConfigLatency parameter to optimized enables Bedrock to prioritize lower-latency retrieval and inference paths, improving responsiveness for real-time recommendation scenarios. This directly addresses the reported performance issues without requiring provisioned throughput or caching strategies that are ineffective for mostly unique interactions.

Option A improves safety and latency predictability but does not ensure recommendations are limited to valid products.

Option B relies on prompt constraints, which are not sufficient to prevent hallucinations.

Option D introduces additional validation and caching layers but increases complexity and does not improve generation relevance.

Therefore, Option C best resolves both relevance and latency challenges using AWS-native, low-maintenance GenAI integration patterns.

28. A financial services company is developing a Retrieval Augmented Generation (RAG) application to help investment analysts query complex financial relationships across multiple investment vehicles, market sectors, and regulatory environments. The dataset contains highly interconnected entities that have multi-hop relationships. Analysts must examine relationships holistically to provide accurate investment guidance. The application must deliver comprehensive answers that capture indirect relationships between financial entities and must respond in less than 3 seconds.  
  
Which solution will meet these requirements with the LEAST operational overhead?

- Use Amazon Bedrock Knowledge Bases with GraphRAG and Amazon Neptune Analytics to store financial data. Analyze multi-hop relationships between entities and automatically identify related information across documents.correct
- Use Amazon Bedrock Knowledge Bases and an Amazon OpenSearch Service vector store to implement custom relationship identification logic that uses AWS Lambda to query multiple vector embeddings in sequence.wrong
- Use Amazon OpenSearch Serverless vector search with k-nearest neighbor (k-NN). Implement manual relationship mapping in an application layer that runs on Amazon EC2 Auto Scaling.
- Use Amazon DynamoDB to store financial data in a custom indexing system. Use AWS Lambda to query relevant records. Use Amazon SageMaker to generate responses.

Explanation:

Option A best satisfies the requirement to capture multi-hop, highly interconnected relationships with minimal operational overhead. Traditional vector similarity search excels at finding semantically similar text but is not optimized for reasoning over explicit entity-to-entity relationships, especially when analysts need indirect, multi-hop connections (for example, fund → holding → issuer → sector → regulation). Graph-based retrieval is designed specifically for these kinds of relationship traversals.

GraphRAG combines retrieval-augmented generation with graph-aware context selection. By representing entities and their relationships in a graph store, the system can traverse multiple hops to assemble a holistic set of relevant facts. This improves completeness and reduces the chance that the model misses indirect relationships that are essential for accurate investment guidance.

Amazon Neptune Analytics provides a managed graph analytics environment capable of efficiently traversing and analyzing complex relationship networks. When integrated with Amazon Bedrock Knowledge Bases, it reduces custom engineering by providing managed ingestion, retrieval, and orchestration patterns suitable for GenAI applications. This lowers operational overhead compared to building and maintaining custom multi-stage retrieval logic.

Meeting the sub-3-second requirement is also more feasible with a graph-optimized engine because multi-hop traversals can be executed efficiently compared to chaining multiple vector searches and joining results in an application layer. The managed nature of Knowledge Bases and Neptune Analytics reduces maintenance, scaling, and operational burden while enabling strong performance.

Option B and C require extensive custom logic and orchestration, increasing complexity and latency.

Option D is not designed for graph-style multi-hop exploration and would require significant custom indexing and retrieval logic.

Therefore, Option A is the most AWS-aligned and operationally efficient approach for multi-hop relationship-aware RAG with strong performance.

29. A company has a customer service application that uses Amazon Bedrock to generate personalized responses to customer inquiries. The company needs to establish a quality assurance process to evaluate prompt effectiveness and model configurations across updates. The process must automatically compare outputs from multiple prompt templates, detect response quality issues, provide quantitative metrics, and allow human reviewers to give feedback on responses. The process must prevent configurations that do not meet a predefined quality threshold from being deployed.  
  
Which solution will meet these requirements?

- Create an AWS Lambda function that sends sample customer inquiries to multiple Amazon Bedrock model configurations and stores responses in Amazon S3. Use Amazon QuickSight to visualize response patterns. Manually review outputs daily. Use AWS CodePipeline to deploy configurations that meet the quality threshold.
- Use Amazon Bedrock evaluation jobs to compare model outputs by using custom prompt datasets. Configure AWS CodePipeline to run the evaluation jobs when prompt templates change. Configure CodePipeline to deploy only configurations that exceed the predefined quality threshold.correct
- Set up Amazon CloudWatch alarms to monitor response latency and error rates from Amazon Bedrock. Use Amazon EventBridge rules to notify teams when thresholds are exceeded. Configure a manual approval workflow in AWS Systems Manager.
- Use AWS Lambda functions to create an automated testing framework that samples production traffic and routes duplicate requests to the updated model version. Use Amazon Comprehend sentiment analysis to compare results. Block deployment if sentiment scores decrease.

Explanation:

Option B is the correct solution because Amazon Bedrock evaluation jobs are purpose-built to assess prompt effectiveness, model behavior, and response quality in a repeatable and automated manner. Evaluation jobs support both quantitative metrics and LLM-based judgment, making them suitable for detecting subtle response quality regressions that simple sentiment or latency metrics cannot capture.

By using custom prompt datasets, the company can consistently test multiple prompt templates and model configurations against the same inputs. This enables accurate comparison across updates and eliminates variability introduced by live traffic sampling. Amazon Bedrock evaluation jobs also support structured scoring outputs, which can be used to enforce objective quality thresholds.

Integrating evaluation jobs directly into AWS CodePipeline ensures that quality checks are automatically triggered whenever prompt templates or configurations change. This creates a gated deployment workflow in which only configurations that meet or exceed the predefined quality threshold are promoted. This directly satisfies the requirement to prevent low-quality configurations from being deployed.

Human reviewers can be incorporated by reviewing evaluation results and scores produced by the jobs, enabling informed feedback without manual data collection.

Option A and D rely on custom frameworks and indirect quality signals, increasing complexity and reducing reliability.

Option C focuses on operational health rather than response quality.

Therefore, Option B provides the most robust, scalable, and AWS-aligned quality assurance process for Amazon BedrockCbased applications.

30. A company upgraded its Amazon BedrockCpowered foundation model (FM) that supports a multilingual customer service assistant. After the upgrade, the assistant exhibited inconsistent behavior across languages. The assistant began generating different responses in some languages when presented with identical questions.  
  
The company needs a solution to detect and address similar problems for future updates. The evaluation must be completed within 45 minutes for all supported languages. The evaluation must process at least 15,000 test conversations in parallel. The evaluation process must be fully automated  
  
and integrated into the CI/CD pipeline. The solution must block deployment if quality thresholds are not met.  
  
Which solution will meet these requirements?

- Create a distributed traffic simulation framework that sends translation-heavy workloads to the assistant in multiple languages simultaneously. Use Amazon CloudWatch metrics to monitor latency, concurrency, and throughput. Run simulations before production releases to identify infrastructure bottlenecks.
- Deploy the assistant in multiple AWS Regions with Amazon Route 53 latency-based routing and AWS Global Accelerator to improve global performance. Store multilingual conversation logs in Amazon S3. Perform weekly post-deployment audits to review consistency.
- Create a pre-processing pipeline that normalizes all incoming messages into a consistent format before sending the messages to the assistant. Apply rule-based checks to flag potential hallucinations in the outputs. Focus evaluation on normalized text to simplify testing across languages.
- Set up standardized multilingual test conversations with identical meaning. Run the test conversations in parallel by using Amazon Bedrock model evaluation jobs. Apply similarity and hallucination thresholds. Integrate the process into the CI/CD pipeline to block releases that fail.correct

Explanation:

Option D is the correct solution because it directly evaluates multilingual output consistency and quality in an automated, scalable, and deployment-gating workflow. Amazon Bedrock model evaluation jobs are designed to run large-scale, repeatable evaluations against defined datasets and to produce quantitative metrics that can be used as objective release criteria.

The core issue is semantic inconsistency across languages for equivalent inputs. The most reliable way to detect this is to create standardized test conversations where each language version expresses the same intent and constraints. Running those tests through the updated model and comparing results with similarity metrics (for example, semantic similarity between expected and actual answers, or between language variants) surfaces regressions that infrastructure testing cannot detect.

Bedrock evaluation jobs support running evaluations at scale and are well suited for processing large datasets quickly. By parallelizing evaluation runs across languages and conversations, the company can meet the 45-minute requirement while executing at least 15,000 conversations. Because the process is standardized, it also allows consistent baseline comparisons across releases.

Applying hallucination thresholds ensures that answers remain grounded and do not introduce fabricated details, which is particularly important when language-specific behavior shifts after a model upgrade. Integrating evaluation jobs into the CI/CD pipeline enables fully automated execution on every model or configuration update. The pipeline can enforce a hard quality gate that blocks deployment if thresholds are not met, preventing regressions from reaching production.

Option A focuses on performance and infrastructure bottlenecks, not multilingual response quality.

Option B is post-deployment and too slow to prevent regressions.

Option C normalizes inputs but does not measure multilingual output equivalence or provide robust, quantitative gating.

Therefore, Option D best meets the automation, scale, timing, and deployment-blocking requirements.
_________________________
Feedback for a legal drafting tool indicates that while arguments cite valid case law, they often fail to address the specific question asked. Which evaluation metric is appropriate for identifying this issue? 

The most appropriate evaluation metric for this specific issue is **Answer Relevance** (sometimes referred to as Prompt Relevance or Question Relevance).

Here is the breakdown of why this is the correct metric and how it fits into the broader generative AI evaluation landscape:

### Why Answer Relevance?

- **The Core Metric:** Answer Relevance specifically measures how well the foundation model's generated output aligns with and directly answers the user's original prompt.

- **The Diagnosis:** If a response scores high on factuality but low on Answer Relevance, it means the model is generating true statements (valid case law) but has lost track of the user's actual intent (the specific legal question).


### Why Other Common Metrics Are Incorrect Here

- **Faithfulness / Grounding:** This measures whether the response is factually supported by the retrieved context. Because the feedback states the tool _is_ citing valid case law, the tool is already succeeding at being faithful/grounded.

- **Context Relevance:** This measures whether the retrieval system (like a vector database in a RAG architecture) is pulling the right documents. While poor context _can_ lead to poor answers, the ultimate metric for measuring if the _final output_ addresses the prompt is Answer Relevance.

- **Toxicity / Harmfulness:** Unrelated to this issue, as this measures unsafe content.


### AWS AIP-C01 Context

In the context of Amazon Bedrock Model Evaluation jobs, when you want to ensure the model isn't just hallucinating legally sound but irrelevant arguments, you would configure an **LLM-as-a-judge** evaluation focusing on **Relevance** to automatically score how well the drafted arguments answer the specific prompts provided in your test dataset.

A company is building a solution to generate images for protective eyewear. The solution must have high accuracy and must minimize the risk of incorrect annotations. Which solution will meet these requirements? 

Data augmentation by using an Amazon Bedrock knowledge base 

Image recognition by using Amazon Rekognition 

Data summarization by using Amazon QuickSight Q 

Human-in-the-loop validation by using Amazon SageMaker Ground Truth Plus 

The correct solution is **Human-in-the-loop validation by using Amazon SageMaker Ground Truth Plus**.

### Why This Is the Correct Solution

- **SageMaker Ground Truth Plus** is a fully managed service that uses expert human labelers along with machine learning-assisted workflows to create, review, and validate high-quality labeled datasets.

- When training ML or Generative AI models where **annotation accuracy is critical** (e.g., verifying bounding boxes or masks for specific items like protective eyewear), automated models alone can produce bad labels. Ground Truth Plus incorporates expert human-in-the-loop validation and built-in quality assurance to minimize annotation errors and maximize dataset precision.


### Why Other Options Are Incorrect

- **Data augmentation by using an Amazon Bedrock knowledge base:** Bedrock Knowledge Bases are used for Retrieval-Augmented Generation (RAG) with text embeddings, not for generating or annotating high-accuracy computer vision training data.

- **Image recognition by using Amazon Rekognition:** While Rekognition can detect Personal Protective Equipment (PPE) in images, it does not provide custom human-in-the-loop annotation validation workflows to build high-accuracy training/generation datasets.

- **Data summarization by using Amazon QuickSight Q:** QuickSight Q is a Business Intelligence (BI) tool for natural language querying of business metrics, completely unrelated to image data processing or annotation.


### AIP-C01 Keyword Trigger

> **"Minimize risk of incorrect annotations"** / **"High-accuracy labeling"** / **"Expert human review of dataset labels"** ➔ **Amazon SageMaker Ground Truth Plus**

An application is showing a ‘ThrottlingException‘. What is the first architectural change to make? 

Request a higher credit limit for your AWS account‘s credit card. 

Increase the memory of the Lambda function to 10GB. 

Immediately move the application to a different AWS Region. 

**None of the options provided are correct.**

A `ThrottlingException` (HTTP 429) occurs when your application makes too many API requests too quickly, exceeding the allowed rate limit for a specific AWS service. It is a capacity and traffic management issue, not a billing or compute resource issue.

Here is why the listed options will fail to resolve the problem:

- **Request a higher credit limit:** Throttling is governed by AWS **Service Quotas** (e.g., Requests Per Second or Tokens Per Minute), not your credit card limit or account billing status.

- **Increase the memory of the Lambda function:** Increasing memory speeds up compute time and resolves out-of-memory errors, but it will not stop a downstream AWS API from blocking your requests for going over the rate limit. In fact, a faster Lambda function might hit the rate limit _faster_.

- **Immediately move to a different AWS Region:** While different regions have separate quota pools, completely migrating an application is a massive, complex operational shift. It is never the _first_ step you should take.


### The Correct Architectural Changes

To properly handle a `ThrottlingException`, you should implement the following standard AWS architectural patterns:

1. **Implement Exponential Backoff and Jitter (Code Level)** Before changing infrastructure, update your application's retry logic. Instead of retrying a failed request immediately, the application should wait progressively longer between retries (e.g., 1s, 2s, 4s) while adding a random delay (jitter) so multiple retries don't hit the API at the exact same time.

2. **Request a Service Quota Increase (Account Level)** If your application legitimately needs higher throughput to function, go to the AWS Service Quotas console and request a limit increase for the specific service that is throttling you.

3. **Decouple with a Queue (Architectural Level)** If you are processing batch jobs or background tasks, place an **Amazon SQS** queue between your application and the API. This acts as a shock absorber, allowing your workers to pull and process messages at a controlled, steady rate that stays safely under the API limit.

4. **Implement Caching** If your application frequently requests the same data, add a caching layer (like Amazon ElastiCache or API Gateway caching). This prevents redundant requests from eating into your API quota.

5. **Enable Cross-Region Routing** If you are using services like Amazon Bedrock, you can configure **Cross-Region Inference profiles**. This automatically distributes your API requests to available capacity pools in other regions without requiring you to move your actual application infrastructure.
_____________

A news agency wants to generate images in a specific ‘brand style‘ using Stable Diffusion XL on Bedrock. What is the most efficient method? 

- Use Style Presets or an Image-to-Image reference within the model parameters. 

- Use Amazon Rekognition to crop the generated images after they are created. 

- Manually edit every generated image in Photoshop before publication. 

- Fine-tune the Stable Diffusion model using 10,000 branded images. 

The correct solution is **Use Style Presets or an Image-to-Image reference within the model parameters**.

### Why This Is the Correct Solution

When using Stable Diffusion XL (SDXL) on Amazon Bedrock, efficiency means achieving the desired output without incurring heavy compute costs, manual labor, or infrastructure overhead.

- **Style Presets:** SDXL natively supports a `style_preset` parameter (e.g., `photographic`, `cinematic`, `digital-art`, `analog-film`) that instantly forces the model to generate the image in a highly specific aesthetic.

- **Image-to-Image (img2img):** If a brand has a specific visual aesthetic that standard text prompts struggle to capture, you can pass a reference image (a brand asset) alongside the text prompt via the Image-to-Image API. By adjusting the `image_strength` (or prompt strength), you force the model to closely mimic the reference image's color palette, composition, and style without requiring any model training.


### Why Other Options Are Incorrect

- **Fine-tune the Stable Diffusion model using 10,000 branded images:** While fine-tuning (or training a LoRA adapter) _does_ teach a model a brand style, using 10,000 images is incredibly expensive, time-consuming, and resource-heavy. It violates the requirement for the "most efficient" method when parameter tuning can accomplish the goal dynamically.

- **Manually edit every generated image in Photoshop before publication:** This is a manual, unscalable process that defeats the purpose of using generative AI for automated workflows.

- **Use Amazon Rekognition to crop the generated images:** Amazon Rekognition is a computer vision service used for analyzing images (e.g., face detection, content moderation). It does not apply visual styles or perform creative image editing.

________________
A company wants to avoid creating new models from the beginning. The company instead wants to adapt pre-trained models to create models for new, related tasks. Which ML strategy meets these requirements? 

- Use transfer learning. 

- Increase the number of epochs. 

- Use unsupervised learning. 

- Decrease the number of epochs. 

**Use transfer learning.**

**Transfer learning** is a machine learning technique where a model that has already been trained on a large dataset for a specific task is reused and adapted (fine-tuned) as the starting point for a new, related task. This strategy allows you to avoid the time, computational resources, and massive datasets required to train a new model entirely from scratch.

Here is why the other options do not fit this requirement:

- **Increase/Decrease the number of epochs:** An epoch is one complete pass of the <font color="#548dd4">training dataset through the algorithm</font>. Adjusting the number of epochs is a hyperparameter tuning step used during the training of any model, but it does not represent a strategy for adapting a pre-trained model to a new task.
    
- **Use unsupervised learning:** This is a training method used to <font color="#548dd4">find hidden <font color="#548dd4">patterns or groupings in unlabeled data</font></font>. It is a fundamental category of machine learning, not a method for adapting pre-existing models to new tasks.
________________
A model is providing ‘Hallucinated‘ facts about a specific product. What is the first step in a Responsible AI workflow? 

1. Change the model‘s temperature to 1.0 to see if it eventually gets the fact right. 

2. Delete the model and wait for the next version to be released by the provider. 

3. Fine-tune the model on the product‘s entire website. 

4. Use Bedrock Model Evaluation to quantify the error rate, then implement RAG to ground the model. 

The correct solution is **Use Bedrock Model Evaluation to quantify the error rate, then implement RAG to ground the model.**

### Why This Is the Correct Solution

In a **Responsible AI workflow**, you must always **measure before you mitigate**:

1. **Quantify the Issue (Evaluation):** Using **Amazon Bedrock Model Evaluation** allows you to test the model against a benchmark dataset using metrics like _Faithfulness_, _Factuality_, or _Correctness_. This gives you an objective baseline error rate to measure improvements against.

2. **Mitigate via Grounding (RAG):** Hallucinations regarding specific, factual product details occur because foundation models rely on static training data. Implementing **Retrieval-Augmented Generation (RAG)** supplies the model with authoritative, real-time product documentation as context during inference, preventing it from inventing details.


### Why Other Options Are Incorrect

- **Change temperature to 1.0:** Increasing temperature increases randomness and variability in model outputs, which actually **increases** the likelihood of hallucinations rather than fixing factual errors.

- **Delete the model and wait:** This is passive, lacks governance, and doesn't solve the core problem, as general-purpose FMs will always run the risk of hallucinating specific enterprise data unless grounded.

- **Fine-tune the model on the entire website:** Fine-tuning is costly, complex to maintain, and inefficient for factual knowledge updates. Furthermore, fine-tuning alone does not eliminate hallucinations as effectively as RAG grounding.
----------------------------
A company makes forecasts each quarter to decide how to optimize operations to meet expected demand. An AI practitioner is writing a report about the trained ML models to provide transparency and explainability to stakeholders. What should be included in the report? 

1. Partial dependence plots (PDPs) 

2. Model convergence tables 

3. Code for model training 

4. Sample data for training 

 Correct 

Partial dependence plots (PDPs) are a standard technique in XAI (Explainable AI) to visualize the relationship between input features and the predicted output. 

The correct inclusion for the report is **Partial dependence plots (PDPs)**.

## Why Partial Dependence Plots (PDPs)?

In operations and forecasting, stakeholders need to trust the model's predictions before they allocate budgets or shift supply chains. Partial Dependence Plots are a core Explainable AI (XAI) technique that visualizes the marginal effect of one or two features on the model's predicted outcome.

For example, if a model forecasts product demand, a PDP can visually demonstrate exactly how a change in a specific feature—such as a price increase, a seasonal shift, or marketing spend—drives the expected demand up or down. This translates complex, "black-box" machine learning math into intuitive, visual business logic that non-technical operations teams can understand and act upon.

## Why the Alternatives Fall Short

When the explicit goal is transparency and explainability for stakeholders, the other options do not provide the necessary insights:

- **Model convergence tables:** These show how a model's error rate decreases over time during the training phase. They are diagnostic tools used by data scientists to verify that the algorithm is learning properly, but they reveal nothing about _how_ or _why_ the model makes specific business predictions.

- **Code for model training:** Source code provides technical transparency for engineering audits, but it is completely unreadable to business stakeholders and does not explain the actual relationships the model learned from the data.

- **Sample data for training:** While auditing training data is important for checking data quality and bias, a raw dataset alone does not explain the patterns the machine learning model actually extracted or how it weights different variables to generate a final forecast.


[What is Partial Dependence Plot (PDP)?](https://www.youtube.com/watch?v=iebOaQs4zHM) This video visually breaks down how PDPs work in Explainable AI to reveal the influence of individual features inside complex black-box models.

(https://www.youtube.com/watch?v=iebOaQs4zHM)


______________________
You are training a custom model in Amazon Bedrock using a large dataset in an S3 bucket. The training job fails with a ‘ResourceNotFound‘ error for the training data. What is the most likely cause? 

1. The training data is in .txt format instead of .csv. 

2. The S3 bucket is in a different AWS Region than the Bedrock training job. 

3. The model being fine-tuned has reached its ‘End of Life‘ date. 

4. The correct answer is **The S3 bucket is in a different AWS Region than the Bedrock training job.**

### Why This Is the Correct Cause

When customizing (fine-tuning) a foundation model in Amazon Bedrock, AWS strictly requires that the Amazon S3 bucket containing your training and validation data resides in the **same AWS Region** where the model customization job is running.

If your S3 bucket is located in a different region, the Bedrock service cannot locate or access the resources through its regional endpoints. This cross-region boundary limitation typically manifests as a `ResourceNotFound`, `AccessDenied`, or `GetObject` permission error directed at the training data.

### Why the Other Options Are Incorrect

- **The training data is in .txt format instead of .csv:** Neither of these formats is correct for Bedrock. Amazon Bedrock fine-tuning requires data to be in **JSON Lines (.jsonl)** format. However, submitting the wrong file format triggers a data validation or parsing error, not a `ResourceNotFound` error.
    
- **The model being fine-tuned has reached its ‘End of Life‘ date:** If you attempt to fine-tune a model that is deprecated, retired, or unavailable in your region, Bedrock will throw an error stating that the _model identifier is invalid_ or unsupported, rather than claiming it cannot find the training data.

__________________________
QuestionA marketing agency wants to generate high-quality images for a social media campaign using a text description (e.g., ‘A futuristic city with green parks‘). Which model family on Amazon Bedrock is specifically designed for image generation? 

2. Stable Diffusion (by Stability AI) 

3. Claude 3 (by Anthropic) 

4. Amazon Titan Text 

5. Amazon Titan Embeddings 

Stable Diffusion is the primary model on Amazon Bedrock used for generating and editing images from natural language descriptions. 

The correct answer is indeed **Stable Diffusion (by Stability AI)**.

Here is a detailed breakdown of why this model is the correct choice and why the other foundation models (FMs) fail to meet the requirements of this specific scenario.

### Why Stable Diffusion Is Correct

- **Stable Diffusion** (such as SDXL) is a specialized **text-to-image** foundation model available on Amazon Bedrock. It is explicitly designed to take natural language prompts (like "A futuristic city with green parks") and generate high-fidelity, creative visual assets. This perfectly aligns with the marketing agency's need to generate images for a social media campaign.

- _(Note: AWS also offers the **Amazon Titan Image Generator** model for this exact use case, but it is not listed among the options)._


### Why the Other Options Are Incorrect

- **Claude 3 (by Anthropic):** The Claude 3 family (Haiku, Sonnet, Opus) are highly advanced Large Language Models (LLMs). While they are _multimodal_—meaning they can "see" and analyze images you upload to them—they **cannot generate images**. They only output text.

- **Amazon Titan Text:** This model family (which includes Titan Text Premier, Express, and Lite) is designed purely for text-based tasks such as summarization, copywriting, question answering, and brainstorming. It has no image generation capabilities.

- **Amazon Titan Embeddings:** This model is designed for a mathematical process. It takes text (and in some versions, images) and converts it into numerical vectors (embeddings). This is used for semantic search and Retrieval-Augmented Generation (RAG) within vector databases, not for creating visual artwork.

### AIP-C01 Keyword Triggers

When you see questions on the exam asking you to select the correct foundation model, look for these specific mapping triggers:

- _"Generate images from text" / "Creative visual assets" / "Inpainting/Outpainting"_ ➔ **Stable Diffusion** or **Amazon Titan Image Generator**

- _"Complex reasoning" / "Highly accurate coding" / "Multimodal image analysis"_ ➔ **Anthropic Claude 3**

- _"Vector search" / "RAG database integration" / "Semantic similarity"_ ➔ **Amazon Titan Embeddings** or **Cohere Embed**

________________________
A startup wants to use a Large Language Model for a task that involves processing sensitive PII (Personally Identifiable Information). They want the model to automatically detect and ‘mask‘ things like Social Security Numbers and Credit Card numbers in the model‘s output. Which feature should they enable? 

1. Amazon Macie 

2. Sensitive Information Filtering in Bedrock Guardrails 

3. Amazon Bedrock Model Evaluation 

4. AWS Lambda 

5. The correct feature to enable is **Sensitive Information Filtering in Bedrock Guardrails**.

### Why This Is the Correct Solution

Amazon Bedrock Guardrails provides a built-in feature specifically designed to handle Personally Identifiable Information (PII) and Protected Health Information (PHI).

When you configure **Sensitive Information Filters**, you can select specific types of PII (like Social Security Numbers, Credit Card numbers, email addresses, or phone numbers). You are then given two action choices for how the guardrail should handle them:

1. **Block:** The prompt or response is entirely blocked if it contains the sensitive data.
    
2. **Mask:** The guardrail automatically replaces the sensitive data with a masking character (e.g., replacing an SSN with `***-**-****`) before the response is returned to the user or application. This perfectly aligns with the startup's requirement.
    

### Why the Other Options Are Incorrect

- **Amazon Macie:** Macie is an excellent AWS machine learning service for discovering and protecting PII, but it is strictly designed to scan static files stored in **Amazon S3 buckets**. It cannot intercept, scan, or mask real-time conversational inputs/outputs from an LLM.
    
- **Amazon Bedrock Model Evaluation:** This feature is used offline (or in staging) to test a model's accuracy, toxicity, or factual grounding against a test dataset. It does not manipulate or mask real-time production traffic.
    
- **AWS Lambda:** While you _could_ write custom Python code and regular expressions inside a Lambda function to intercept outputs and scrub PII, doing so requires significant custom development and maintenance. On an AWS exam, you should always choose the native, fully managed feature (Guardrails) over building custom code to reinvent the wheel.

_________________________
A retail company observes that 70% of user queries for their chatbot are simple transactional questions. Their monthly bill for a large foundation model has exceeded the budget. Which strategy should the developer implement to reduce costs while maintaining quality for complex issues? 

1. Implement a semantic routing layer to direct simple queries to a cost-optimized FM and complex queries to the large-parameter FM. 

2. Configure Provisioned Throughput for the large-parameter FM to reduce the per-token cost. 

3. Replace the large FM with a smaller FM for all queries and use few-shot prompting. 

4. Enable Amazon Bedrock Guardrails to block queries that are deemed too complex. 

The correct strategy is to **Implement a semantic routing layer to direct simple queries to a cost-optimized FM and complex queries to the large-parameter FM.**

### Why This Is the Correct Strategy

This architectural pattern is known as **Model Routing** (or Semantic Routing). In generative AI, you pay for the intelligence you use. Using a massive, highly capable model (like Anthropic Claude 3 Opus) to answer a simple transactional question (e.g., "What are your store hours?") is massive overkill and highly cost-inefficient.

By placing a semantic router (often a much smaller, faster classifier model or embedding-based vector search) in front of your foundation models, you can accurately triage the traffic:

- **The 70% (Simple Queries):** Routed to a highly cost-optimized, fast model (like Claude 3 Haiku or Amazon Titan Text Express). This slashes the monthly bill.

- **The 30% (Complex Queries):** Routed to the large-parameter foundation model. This ensures that when deep reasoning or complex logic is actually required, the application maintains high quality.


### Why the Other Options Are Incorrect

- **Configure Provisioned Throughput for the large-parameter FM:** Provisioned Throughput is designed for massive, consistent, steady-state workloads and requires a heavy upfront financial commitment (usually a 1 to 6-month term). It does not fix the fundamental architectural flaw of using an expensive model for simple tasks.

- **Replace the large FM with a smaller FM for all queries:** While this would successfully reduce costs, it violates the requirement to _"maintain quality for complex issues."_ A smaller model, even with few-shot prompting, will likely fail or hallucinate on the 30% of queries that require advanced reasoning.

- **Enable Amazon Bedrock Guardrails to block queries that are deemed too complex:** Bedrock Guardrails are designed for security, safety, and compliance (blocking PII, hate speech, or competitor names). They are not designed to block legitimate customer questions just because they are difficult, which would severely degrade the user experience.

__________________
A RAG system retrieves the right documents, but the model says ‘I don‘t know‘. What is the likely prompt issue? 

1. The S3 bucket is in ‘Glacier‘ storage class. 

2. The developer forgot to include the ‘Domain‘ column in the CSV. 

3. The model‘s temperature is set to 0.0. 

**None of the options provided are correct.** It appears the correct answer was left off your list.

correct answer: The prompt has a ‘strictness‘ instruction that is too aggressive.

In a Retrieval-Augmented Generation (RAG) architecture, there are two distinct phases: the **retrieval phase** (finding the data) and the **generation phase** (the foundation model reading the data to write an answer). Since the scenario explicitly states the system _retrieves the right documents_, the retrieval mechanism is working perfectly.

Here is why the provided options are incorrect:

- **The S3 bucket is in 'Glacier' storage class:** Amazon S3 Glacier is for long-term cold storage. If your data was in Glacier, synchronous retrieval would fail entirely (it takes minutes to hours to restore data). You would never "retrieve the right documents" in real-time.

- **The developer forgot to include the 'Domain' column in the CSV:** This is a metadata or data-formatting issue. While missing metadata might make it harder to filter searches, the scenario explicitly states the retrieval phase succeeded.

- **The model's temperature is set to 0.0:** Temperature is an inference hyperparameter, not a prompt issue. Furthermore, setting the temperature to `0.0` is actually a **best practice** for RAG. It makes the model deterministic and forces it to rely strictly on the provided facts rather than hallucinating. It would not cause the model to ignore valid context.


### What is the _actual_ prompt issue?

If a foundation model receives the correct documents but still defaults to an "I don't know" fallback response, the problem lies in the **prompt template** passed to the generation model. On an AWS exam, the correct answer to this scenario will typically be one of the following:

1. **The retrieved context was not successfully passed into the prompt:** The developer wrote the prompt template (e.g., _"Answer the user's question based on the following context:"_) but a coding error resulted in the `{context}` variable being blank when sent to the LLM API.

2. **Overly strict negative constraints:** The system prompt instructs the model to be _too_ cautious (e.g., _"If the exact answer is not explicitly stated word-for-word in the context, you must say 'I don't know'"_). If the context contains the answer but phrases it slightly differently than the user's question, the model will overly index on the negative constraint and refuse to answer.

3. **Context Truncation (Token limits):** The prompt includes the documents, but the combined length exceeds the foundation model's maximum context window. The system truncates the end of the prompt—which happens to be where the actual answer is located—leaving the model with incomplete information.

_____________________________________________
A developer is using ‘Chain of Thought‘ prompting to help a model solve complex logic puzzles. However, the ‘thoughts‘ are taking up too many output tokens, making the response expensive. What is a more cost-effective architectural solution? 

1. Use a ‘Few-Shot‘ prompt with 100 examples to skip the need for reasoning. 

2. Increase the temperature to 1.0 to make the reasoning faster. 

3. Enable ‘Provisioned Throughput‘ to reduce the cost per token. 

4. Switch to a smaller, cheaper model for the ‘reasoning‘ step and pass only the final answer to a larger model. 

**None of the options provided are correct.**

This scenario describes a classic Generative AI trade-off: **Chain of Thought (CoT)** drastically improves a foundation model's ability to solve complex logic by forcing it to "show its work" step-by-step, but output tokens are the most expensive part of LLM inference.

Here is why the provided options are incorrect and will fail in production:

- **Switch to a smaller, cheaper model for the 'reasoning' step:** This is architecturally backward. Smaller models generally lack the parameter depth to solve _complex logic puzzles_. If you route the hard reasoning step to a small model, it will fail the puzzle, making whatever it passes to the large model useless.

- **Use a 'Few-Shot' prompt with 100 examples:** For complex logic, skipping the CoT reasoning step usually causes the model to guess and fail. Furthermore, pushing 100 long examples into the prompt drastically increases your **input token** consumption, which can easily erase any cost savings you gained by reducing output tokens.

- **Increase the temperature to 1.0 to make the reasoning faster:** Temperature controls randomness, not latency or token count. Setting temperature to 1.0 on a logic puzzle is catastrophic, as it encourages the model to hallucinate or drift from strict logical constraints. (Logic puzzles usually require a temperature of 0.0).

- **Enable 'Provisioned Throughput':** While this _technically_ changes how you are billed, Provisioned Throughput requires a massive, fixed hourly financial commitment (typically thousands of dollars a month). It is for high-volume, steady-state workloads, not for optimizing the token efficiency of a single prompt pattern.

### The Correct Architectural Solutions

To solve the cost issue of Chain of Thought prompting, you should implement one of the following standard AI architectures:

1. **Model Distillation (Fine-Tuning)** Use the large, expensive model to generate thousands of successful CoT logic puzzle answers. Use those answers as a training dataset to **fine-tune a smaller, cheaper model**. Once fine-tuned, the smaller model internalizes the logic patterns and can often output the correct final answer directly, bypassing the need to generate expensive reasoning tokens every time.

2. **LLM Cascading (Confidence Routing)** Implement a router that first sends the puzzle to a fast, cheap model using CoT. If the small model's output indicates high confidence (or passes a programmatic verification check), you use it. Only if the small model fails do you trigger the large, expensive model.

3. **Use `<thinking>` Tags with Target Extraction** If you must use the large model, instruct it to place its reasoning inside XML tags (e.g., `<thinking>...</thinking>`) and place the final answer in `<answer>...</answer>`. While you still pay for the generation, your application code can seamlessly strip out the thinking tags before presenting it to the user, improving the user experience while maintaining the logical accuracy.


____________________________________

A company has fine-tuned an Amazon Titan model. Which deployment configuration must the company use to utilize this custom model in production?

- Invoke the model using the On-Demand Throughput standard endpoint.
- Purchase and configure Provisioned Throughput for the custom model.
- Deploy the custom model to a SageMaker Serverless Inference endpoint.
- Use the Amazon Bedrock Batch Inference API with the custom model ARN.

 Incorrect  

### Correct

**Option B. Purchase and configure Provisioned Throughput for the custom model**

- **Correct because:** Fine-tuned **Amazon Titan models** require **Provisioned Throughput** in Amazon Bedrock to be deployed in production.
- Provisioned Throughput guarantees dedicated capacity for the custom model, ensuring predictable performance and availability.
- On-demand endpoints cannot be used for fine-tuned Titan models; only provisioned throughput supports custom deployments.

### Incorrect

**Option A. Invoke the model using the On-Demand Throughput standard endpoint**

- Incorrect because On-Demand Throughput is only available for **base foundation models**, not fine-tuned custom models.
- Custom Titan models cannot be invoked this way in production.

**Option C. Deploy the custom model to a SageMaker Serverless Inference endpoint**

- Incorrect because Titan models are hosted and deployed through **Amazon Bedrock**, not SageMaker.
- SageMaker is used for custom ML models, but Titan fine-tunes are restricted to Bedrock’s deployment mechanisms.

**Option D. Use the Amazon Bedrock Batch Inference API with the custom model ARN**

- Incorrect because Batch Inference is designed for **large-scale offline predictions**, not real-time production deployment.
- It does not provide the continuous, scalable serving required for production workloads.
__________________________________________
A fintech company is building a financial advisor bot that uses RAG to pull data from thousands of quarterly reports. They are seeing very high latency during the retrieval phase. Which optimization strategy should the developer implement to speed up the retrieval without losing semantic meaning? 

1. Implement a ‘reranker‘ model to filter the top 100 results down to the top 5. 

2. Convert all quarterly reports to plain text and remove all punctuation to reduce token count. 

3. Use ‘Parent Document Retrieval‘ where small chunks are searched, but the full parent context is sent to the LLM. 

4. Switch to a ‘Small‘ embedding model and use metadata filtering to narrow the search space. 

The correct strategy is to **Switch to a ‘Small‘ embedding model and use metadata filtering to narrow the search space.**

### Why This Is the Correct Strategy

This approach tackles retrieval latency from two highly effective architectural angles:

1. **Metadata Filtering (Pre-filtering):** Searching across millions of vectors (thousands of quarterly reports) takes time. By attaching metadata to your embeddings (e.g., `Year=2023`, `Company=Amazon`, `Quarter=Q4`), you can filter the database _before_ running the vector search. The engine only performs the heavy semantic math on the exact subset of documents that matter, drastically reducing latency.

2. **Small Embedding Models:** High-dimensional embedding models capture immense nuance but create massive vectors that take longer to query. Switching to an embedding model with fewer dimensions (or using a model like Amazon Titan Text Embeddings v2 that allows you to customize the output dimension) significantly speeds up the K-Nearest Neighbors (KNN) math required during the retrieval phase, while maintaining sufficient semantic meaning for corporate documents.

### Why the Other Options Are Incorrect

- **Implement a 'reranker' model to filter the top 100 results down to the top 5:** Rerankers are used to improve the _accuracy and relevance_ of retrieved documents, but they actually **increase latency**. A cross-encoder reranker requires a computationally heavy second pass over the retrieved documents.

- **Use 'Parent Document Retrieval':** This is an advanced RAG technique used to improve the _generation quality_ (by finding the answer in a small chunk, but giving the LLM the larger surrounding document for context). It does not speed up the vector retrieval latency.

- **Convert reports to plain text and remove all punctuation:** This violates the core constraint of the question. Removing punctuation destroys the semantic meaning and syntactic structure of financial documents, severely degrading the embedding quality and the foundation model's ability to read it.

____________________
Developing a legal application requires validating if a specialized model offers value over a standard RAG implementation. Which step represents the most logical and cost-effective first step for a Proof of Concept (PoC)? 

1. Perform a Continued Pre-training job on the base model using the unlabeled legal corpus. 

2. Deploy a large cluster of GPU instances on Amazon EC2 to train a model from scratch. 

3. Immediately purchase Provisioned Throughput for a model and begin fine-tuning. 

4. Establish a performance baseline by evaluating a general-purpose Large Language Model (LLM) using relevant RAG techniques and prompt engineering. 

The correct first step is to **Establish a performance baseline by evaluating a general-purpose Large Language Model (LLM) using relevant RAG techniques and prompt engineering.**

### Why This Is the Correct Strategy

In the AWS Generative AI adoption lifecycle, you must always start with the most cost-effective, least complex solution before escalating to advanced customization.

Before you can determine if a specialized, fine-tuned legal model offers any real value, you must first know how well a standard, off-the-shelf model performs. By building a quick Proof of Concept (PoC) using zero-shot/few-shot prompting and a standard RAG architecture, you establish a **performance baseline**. If RAG achieves 90% accuracy, you can then make a data-driven business decision about whether spending thousands of dollars on fine-tuning is worth fighting for that final 10%.

### Why the Other Options Are Incorrect

- **Perform a Continued Pre-training job on the base model:** Continued pre-training is a highly complex, expensive process used to teach a model an entirely new vocabulary (e.g., dense medical or legal jargon it has never seen). It is an advanced optimization step, never a first step for a PoC.

- **Deploy a large cluster of GPU instances on Amazon EC2 to train from scratch:** Training a foundation model from scratch takes months, massive amounts of data, and millions of dollars. It is an extreme anti-pattern for a standard enterprise application PoC.

- **Immediately purchase Provisioned Throughput and begin fine-tuning:** Provisioned Throughput requires a massive, fixed-term financial commitment. Committing to this infrastructure before proving that prompt engineering and RAG are insufficient violates the AWS Well-Architected Framework's cost optimization pillar.


### The AWS GenAI Customization Hierarchy

When answering exam questions about model customization, always apply this progression from cheapest/easiest to most expensive/complex:

1. **Prompt Engineering** (Start here)

2. **RAG** (Add context)

3. **Fine-Tuning / Instruction Tuning** (Alter model behavior/tone)

4. **Continued Pre-training** (Teach new domain vocabulary)

5. **Train from Scratch** (Almost never the right answer for enterprises)

________________________
A company is training a model to detect fraud in bank transactions. Since fraud is rare, only 0.1% of their 1 million transactions are labeled as ‘Fraud‘. The model currently achieves 99.9% accuracy by simply predicting ‘Not Fraud‘ for every single case. Which metric should the AI practitioner use to better understand the model‘s performance on the rare ‘Fraud‘ class? 

1. Mean Absolute Error (MAE) 

2. R-squared 

3. F1 Score or Precision/Recall 

4. Overall Accuracy 

The correct metric to use is **F1 Score or Precision/Recall**.

### Why This Is the Correct Solution

This scenario describes the **Accuracy Paradox**, a common pitfall in machine learning when dealing with highly imbalanced datasets. Because legitimate transactions vastly outnumber fraudulent ones, a model can achieve near-perfect accuracy by doing no actual learning and simply guessing the majority class every time.

To evaluate how well the model actually detects the rare event, you must look at metrics that focus on the minority class:

- **Recall (Sensitivity):** Out of all the _actual_ fraud cases, how many did the model successfully find? (Crucial for minimizing False Negatives).

- **Precision:** Out of all the cases the model _claimed_ were fraud, how many were actually fraud? (Crucial for minimizing False Positives and avoiding customer friction).

- **F1 Score:** The harmonic mean of Precision and Recall. It provides a single, balanced metric that completely ignores the massive number of True Negatives (the 99.9% normal transactions) that skew standard accuracy.

### Why the Other Options Are Incorrect

- **Overall Accuracy:** The prompt explicitly demonstrates why this fails. Measuring total correct predictions over total total cases masks the model's complete inability to detect the minority class.
    
- **Mean Absolute Error (MAE):** This is a metric used for **regression** models (predicting continuous numerical values, like housing prices or temperature). Fraud detection is a **classification** problem (categorizing data into distinct buckets like Fraud/Not Fraud).
    
- **R-squared:** Like MAE, R-squared is a regression metric that measures how well the independent variables explain the variance in the dependent variable. It is not used for classification tasks.

______________________
A company wants to build a generative AI application that summarizes confidential company emails. They are concerned about costs and want to only pay for the exact number of characters processed by the model. Which pricing model for Amazon Bedrock is most appropriate? 

1. On-Demand pricing 

2. Flat monthly subscription 

3. Reserved Instance pricing 

4. Provisioned Throughput 

5. The correct pricing model is **On-Demand pricing**.

### Why This Is the Correct Solution

With **On-Demand pricing** in Amazon Bedrock, you operate on a strict pay-as-you-go model. You are billed based on the exact volume of input tokens (the text you send, such as the confidential emails) and output tokens (the text the model generates, such as the summaries). Because a token directly correlates to a specific number of characters or words, this is the only pricing model that ensures the company pays exclusively for exactly what it processes, with no upfront commitments.

### Why the Other Options Are Incorrect

- **Provisioned Throughput:** This model requires you to purchase guaranteed, steady-state compute capacity (Model Units) for a 1-month or 6-month term. You pay a fixed hourly rate for that capacity regardless of how many characters you actually process, which violates the requirement to pay only for exact usage.

- **Reserved Instance pricing:** This is a billing concept used for infrastructure services like Amazon EC2 or Amazon RDS (where you reserve a specific virtual server). It does not exist in Amazon Bedrock.

- **Flat monthly subscription:** Amazon Bedrock does not offer a generic flat-rate subscription; billing is either usage-based (On-Demand) or capacity-based (Provisioned Throughput).

______________________________
An application requires low latency for the first few words of a response. Which API feature must be enabled in the code? 

1. Use Provisioned Throughput to increase the speed of the underlying hardware. 

2. Set the ‘Max Tokens‘ parameter to 10 to ensure the response is short. 

3. Store the model‘s weights on an Amazon EBS Provisioned IOPS volume. 

4. Enable Response Streaming using the InvokeModelWithResponseStream API. 

The correct feature to enable is **Enable Response Streaming using the InvokeModelWithResponseStream API.**

### Why This Is the Correct Solution

In generative AI, foundation models generate text one piece (token) at a time. If you use a standard synchronous API call (`InvokeModel`), your application must wait until the model finishes generating the _entire_ response before it receives any data.

By using **`InvokeModelWithResponseStream`**, the API sends the output back to your application in chunks as it is being generated. This drastically reduces the **Time to First Token (TTFT)**, allowing your application to display the first few words to the user almost instantly while the rest of the response continues loading in the background.

### Why the Other Options Are Incorrect

- **Use Provisioned Throughput to increase the speed of the underlying hardware:** Provisioned Throughput guarantees consistent compute capacity and helps with high concurrency, but it still processes requests synchronously unless streaming is explicitly enabled in the code.

- **Set the 'Max Tokens' parameter to 10 to ensure the response is short:** While this forces the model to stop generating quickly, it severely limits the utility of the application (capping answers to roughly 7-8 words) and does not actually change how the API delivers the data.

- **Store the model's weights on an Amazon EBS Provisioned IOPS volume:** Amazon Bedrock is a fully managed serverless service. You do not manage the underlying infrastructure, Amazon EC2 instances, or EBS storage volumes that host the foundation models.
___________________

A retail company wants to use a chatbot to handle customer returns. The chatbot needs to be able to look up a customer‘s order history in a database and then trigger an email to the shipping department. Which Amazon Bedrock feature allows the model to interact with external systems and APIs? 

1. Amazon Bedrock Agents 

2. Amazon Bedrock Model Customization 

3. Amazon Bedrock Knowledge Bases 

4. Amazon Bedrock Guardrails 

The correct feature is **Amazon Bedrock Agents**.

### Why This Is the Correct Solution

**Amazon Bedrock Agents** (specifically through the use of **Action Groups**) empower foundation models to execute multi-step business tasks by connecting them to your company's APIs and infrastructure.

When a customer asks for a return, the Agent uses its internal reasoning to determine which systems it needs to interact with. It can then securely execute AWS Lambda functions or external APIs to look up the order in your database, evaluate the return policy, and push a command to your shipping system to trigger an email.

### Why the Other Options Are Incorrect

- **Amazon Bedrock Knowledge Bases:** This feature connects models to vector databases for Retrieval-Augmented Generation (RAG). It allows the model to _read_ existing text (like a return policy document), but it cannot _take actions_ or write data to external systems (like sending an email).

- **Amazon Bedrock Guardrails:** This is a security and compliance feature used to filter toxic content, redact Personally Identifiable Information (PII), and enforce topic boundaries. It does not provide API integration capabilities.

- **Amazon Bedrock Model Customization:** This refers to the offline process of fine-tuning or continued pre-training a model's weights using a static training dataset. It alters how the model generates text, but it does not grant the model the ability to dynamically execute code or interact with live databases in real-time.
_______________
You are building a real-time customer support bot. To reduce the ‘Perceived Latency‘, you decide to use streaming. Which client-side technology is most commonly used to handle the streaming response from the Amazon Bedrock API? 

1. REST API with 60-second timeouts 

2. GraphQL Subscriptions 

3. Long Polling with HTTP 1.1 

4. Server-Sent Events (SSE) or WebSockets 

The correct answer is **Server-Sent Events (SSE) or WebSockets**.

### Why This Is the Correct Solution

When streaming foundation model responses from Amazon Bedrock (`InvokeModelWithResponseStream`) to a client-side interface (like a web or mobile browser):

- **Server-Sent Events (SSE):** SSE provides a lightweight, standard HTTP mechanism for unidirectional streaming. The server holds an HTTP connection open and pushes text tokens to the client as soon as they are generated by Bedrock. This allows the UI to render words incrementally (typing effect) with minimal overhead.
    
- **WebSockets:** WebSockets provide a full-duplex, persistent TCP connection, making them ideal when real-time bidirectional communication is needed (e.g., streaming user audio/text in and receiving model tokens back simultaneously via AWS API Gateway WebSocket APIs).

### Why the Other Options Are Incorrect

- **REST API with 60-second timeouts:** Standard synchronous REST calls buffer the entire payload before returning the final response to the client. The user sits waiting until generation finishes, completely failing to reduce perceived latency.

- **Long Polling with HTTP 1.1:** Long polling repeatedly opens and closes HTTP connections to check for new data. This creates significant network overhead and latency lag, making it unsuitable for smooth, token-by-token streaming.

- **GraphQL Subscriptions:** While GraphQL subscriptions can handle streaming under the hood (typically using WebSockets), SSE or WebSockets are the underlying transport technologies actually used to deliver the stream

___________________
A developer is trying to use a newly released model, but it‘s not showing up in their account. What is the most common reason? 

1. The developer has not yet uploaded a ‘PracticeTest‘ CSV file. 

2. Model Access has not been granted in the Bedrock Console for that region. 

3. The developer is not using a high-end GPU on their local laptop. 

4. The model is only available for users with a ‘Prime‘ membership. 

 add Keywords from the exam point of view as well  

The correct reason is **Model Access has not been granted in the Bedrock Console for that region.**

### Why This Is the Correct Reason

By default, Amazon Bedrock does not automatically grant you access to use its foundation models, even if they are newly released and generally available in your AWS Region.

Because Bedrock hosts models from various third-party providers (like Anthropic, Meta, Mistral, and Cohere), AWS requires customers to explicitly review and accept the specific End User License Agreement (EULA) and Acceptable Use Policy for each individual model. You must navigate to the **Model Access** page in the Bedrock Console and request access before the model becomes usable in your account. Furthermore, model access is strictly **region-specific**; granting access in `us-east-1` does not automatically grant access in `us-west-2`.

### Why the Other Options Are Incorrect

- **The developer is not using a high-end GPU on their local laptop:** Amazon Bedrock is a fully managed, serverless cloud service. The inference (running the model) happens on AWS data centers, meaning your local laptop hardware is completely irrelevant to model availability or performance.

- **The model is only available for users with a 'Prime' membership:** Amazon Prime is a retail consumer subscription. AWS operates entirely separately and uses standard cloud billing (On-Demand or Provisioned Throughput).

- **The developer has not yet uploaded a 'PracticeTest' CSV file:** Model access is governed by IAM permissions and console opt-ins, not by uploading specific data files.


### 🔑 AIP-C01 Exam Keywords to Remember

When you see questions regarding missing models, access denied errors, or setting up Bedrock for the first time, look for these specific exam triggers:

- **Model Access / Opt-in:** The required first step in Bedrock. If a model is missing or throws an `AccessDeniedException` on your first API call, checking the "Model Access" page is almost always the answer.

- **EULA / End User License Agreement:** The primary reason _why_ AWS forces you to request access manually.

- **Regional Availability:** Not all models are available in all AWS Regions. If a newly released model isn't on the Model Access page at all, you are likely in a region where it hasn't launched yet.

- **IAM Permissions:** Even if Model Access is granted in the console, the developer's IAM User/Role must still have the `bedrock:InvokeModel` permission attached to their IAM policy to actually generate a response.
_____________
You are using Amazon Bedrock Model Evaluation to compare two models. You choose the ‘Automatic‘ evaluation type. Which metric is NOT typically available in an automatic evaluation? 

1. BLEU (Bilingual Evaluation Understudy) 

2. Subjective Helpfulness as perceived by an expert 

3. ROUGE (Recall-Oriented Understudy for Gisting Evaluation) 

4. Exact Match 

The correct answer is **Subjective Helpfulness as perceived by an expert**.

### Why This Is the Correct Solution

Amazon Bedrock Model Evaluation is divided into two primary paradigms: **Automatic Evaluation** and **Human Evaluation**.

- **Automatic Evaluation:** Relies on programmatic algorithms, mathematical formulas, or an LLM-as-a-judge to rapidly and deterministically compute objective scores at scale. It evaluates factual accuracy, toxicity, structural similarity, or exact text matching without requiring human intervention.

- **Human Evaluation:** Is explicitly designed to capture nuanced, qualitative, and subjective metrics. If you need to evaluate attributes like "subjective helpfulness," "brand voice alignment," or "professional tone," you must configure a Human Evaluation job, which routes the model's outputs to either your internal team or an AWS-managed workforce of expert reviewers.


Because it requires actual human perception, subjective helpfulness cannot be generated by a purely programmatic automatic evaluation.

### Why the Other Options Are Incorrect

- **BLEU (Bilingual Evaluation Understudy):** This is a classic, programmatic automatic metric (often used in translation) that calculates the overlap of n-grams between the model's output and a reference string.

- **ROUGE (Recall-Oriented Understudy for Gisting Evaluation):** This is a standard automatic metric used heavily for text summarization tasks. It mathematically calculates the structural recall of overlapping words or phrases against a reference summary.

- **Exact Match:** This is a deterministic, automated algorithm that strictly checks if the model's output perfectly matches a predefined reference answer string (commonly used for strict Question & Answer workflows).


### 🔑 AIP-C01 Exam Keywords to Remember

When you see questions regarding model evaluation in Amazon Bedrock, use these trigger mappings:

- _"Scale," "Speed," "Objective scoring," "BERTScore," "F1 Score," "Toxicity"_ ➔ **Automatic Evaluation**

- _"Subjective," "Nuance," "Brand Voice," "Style," "Helpfulness"_ ➔ **Human Evaluation (BYO Workforce or AWS Managed)**

- _"Custom prompts/datasets without a human workforce"_ ➔ **LLM-as-a-Judge (under Automatic Evaluation)**
________________________
You are using a ‘Multi-Modal‘ model to analyze security camera footage. The model needs to describe what is happening in a 1-minute clip. How should the video data be provided to a Bedrock model like Claude 3 Vision? 

1. Upload the raw .mp4 file directly to the InvokeModel API. 

2. Streaming the video live via Kinesis Video Streams into the Bedrock API. 

3. Extract key frames from the video and provide them as a sequence of Base64 encoded images in the prompt. 

4. Use Amazon Transcribe to turn the video audio into text and send only the text. 

The correct approach is to **Extract key frames from the video and provide them as a sequence of Base64 encoded images in the prompt.**

### Why This Is the Correct Solution

While models like Anthropic's Claude 3 are highly capable "multimodal" foundation models, their vision capabilities on Amazon Bedrock are specifically engineered to process static images, not raw video file formats.

To perform video analysis, you must implement a standard architectural pattern known as **Frame Extraction**. By programmatically pulling key frames from the video (e.g., one frame per second) and encoding them as Base64 image payloads, you can pass them to the model in sequential order. Claude 3 can analyze up to 20 images in a single prompt, allowing it to understand the temporal sequence and describe the unfolding events in the clip just as if it had watched a video.

### Why the Other Options Are Incorrect

- **Upload the raw .mp4 file directly to the InvokeModel API:** The `InvokeModel` API for Claude 3 does not accept `.mp4`, `.mov`, or other video MIME types. Sending a video file will result in an immediate validation error.

- **Streaming the video live via Kinesis Video Streams into the Bedrock API:** Amazon Kinesis Video Streams (KVS) is an excellent AWS service for ingesting live video, but it cannot stream directly into a Bedrock foundation model. You would still need an intermediary compute layer (like AWS Lambda or Amazon EC2) to consume the KVS stream, extract the frames, and convert them to Base64 before sending them to Bedrock.

- **Use Amazon Transcribe to turn the video audio into text and send only the text:** Security camera footage heavily relies on visual actions, and often lacks audio entirely. Even with audio, translating speech to text completely ignores the requirement to analyze the visual scene.


### 🔑 AIP-C01 Exam Keywords to Remember

When faced with questions about multimodal inputs or video analysis on the exam, look for these specific triggers:

- _"Analyze video" / "Process security footage" / "Understand motion"_ ➔ **Frame extraction as Base64 images**

- _"Max images per prompt"_ ➔ **Claude 3 supports multiple images per request** (allowing for temporal sequence analysis).

- _"Video ingestion pipeline"_ ➔ **Amazon Kinesis Video Streams + AWS Lambda (for frame extraction) + Amazon Bedrock**

___________________
A company wants to use language models for inference on edge devices with the lowest latency possible. Which solution will meet these requirements? 

1. Incorporate a centralized SLM API for asynchronous communication. 

2. Incorporate a centralized LLM API for asynchronous communication. 

3. Deploy optimized small language models (SLMs) on edge devices. 

4. Deploy optimized large language models (LLMs) on edge devices. 

The correct solution is to **Deploy optimized small language models (SLMs) on edge devices.**

### Why This Is the Correct Solution

When the absolute priority is the **lowest latency possible**, you must eliminate network round-trip times (the time it takes data to travel from the device to a cloud server and back). By deploying models locally on the edge device itself (on-device inference), the application processes data instantly.

Because edge devices (like smartphones, IoT sensors, or industrial computers) have limited memory, battery, and compute power, standard Large Language Models (LLMs) are far too massive to run natively. **Small Language Models (SLMs)**—which are highly optimized, quantized, and have far fewer parameters—are specifically engineered to run efficiently on edge hardware while maintaining acceptable performance for focused tasks.

### Why the Other Options Are Incorrect

- **Deploy optimized large language models (LLMs) on edge devices:** LLMs require massive amounts of VRAM (often multiple high-end GPUs) to run. You physically cannot deploy a standard large language model on constrained edge devices without causing catastrophic hardware failure or out-of-memory errors.

- **Incorporate a centralized SLM/LLM API for asynchronous communication:** Any centralized API requires an internet connection to send data to the cloud. This introduces network latency, jitter, and potential packet loss, completely violating the requirement for the "lowest latency possible." Furthermore, asynchronous communication specifically implies that the system does not wait for an immediate response, which contradicts real-time, low-latency requirements.

### 🔑 AIP-C01 Exam Keywords to Remember

When you see questions on the exam regarding edge computing, latency, or device constraints, look for these specific mappings:

- _"Edge devices" / "No internet connection" / "Local inference"_ ➔ **Deploy optimized Small Language Models (SLMs)**

- _"Reduce model size for edge" / "Run on mobile"_ ➔ **Model Quantization / SLMs**

- _"Zero network latency" / "Real-time edge processing"_ ➔ **On-device inference (Avoid centralized APIs)**
______________
An AI practitioner is building a deep learning model to predict house prices. They notice the model performs perfectly on the training data but fails miserably on new, unseen data from the next month. What is the technical term for this problem? 

1. Underfitting 

2. Overfitting 

3. Data Leakage 

4. Bias-Variance Tradeoff 

The correct technical term for this problem is **Overfitting**.

### Why This Is the Correct Answer

**Overfitting** occurs when a machine learning model learns the training data _too_ well. Instead of just learning the underlying, generalized patterns (like the relationship between square footage and price), the model effectively memorizes the exact training dataset, including all of its random noise, anomalies, and outliers.

Because the model is highly customized to the exact quirks of the training data, it is completely unable to generalize when it is exposed to new, unseen data, resulting in poor real-world performance.

### Why the Other Options Are Incorrect

- **Underfitting:** This is the exact opposite of overfitting. Underfitting happens when a model is too simple to capture the underlying patterns in the data at all. An underfit model performs poorly on **both** the training data and the unseen data.

- **Data Leakage:** This occurs when information from outside the training dataset (usually the test/validation data) accidentally "leaks" into the training process. While this also causes a model to look great in testing and fail in production, the specific scenario of memorizing training data while failing on purely unseen data is the textbook definition of overfitting.

- **Bias-Variance Tradeoff:** This is a fundamental theory in machine learning that describes the balance between a model being too simple (high bias/underfitting) and too complex (high variance/overfitting). It is the overarching concept, not the specific name of the failure mode described in the scenario.


### 🔑 AIP-C01 Exam Keywords to Remember

When you see questions regarding model performance or training metrics on the exam, use these mappings:

- _"Perfect on training, fails on test" / "Fails to generalize"_ ➔ **Overfitting (High Variance)**

- _"Poor performance on both training and test"_ ➔ **Underfitting (High Bias)**

- _"Model used future data during training" / "Target variable included in features"_ ➔ **Data Leakage**

- _"Methods to fix overfitting"_ ➔ **More data, early stopping, dropout, L1/L2 regularization**

________________________
A developer is in us-east-1, but data residency requirements state inference must happen in the EU. How should they handle this? 

1. Deploy the application and Bedrock endpoints in an EU region like eu-central-1. 

2. Send the data to us-east-1 but tag it with ‘Location: EU‘. 

3. Use a VPN to ‘spoof‘ the developer‘s location to London. 

4. Enable the ‘Data Residency‘ checkbox in the us-east-1 Bedrock settings. 

The correct approach is to **Deploy the application and Bedrock endpoints in an EU region like eu-central-1.**

### Why This Is the Correct Solution

In AWS, **data residency** is strictly tied to the AWS Region you select. AWS operates under the principle of regional isolation: data stored and processed in a specific region stays in that region unless the customer explicitly configures it to move elsewhere.

If compliance or legal requirements dictate that data cannot leave the European Union for processing, the developer must instantiate their Amazon Bedrock API calls and application infrastructure within an EU-based AWS Region (such as `eu-central-1` in Frankfurt or `eu-west-1` in Ireland). It does not matter where the developer themselves is physically sitting; what matters is the API endpoint they target in their code.

### Why the Other Options Are Incorrect

- **Enable the ‘Data Residency’ checkbox in the us-east-1 Bedrock settings:** This is a fabricated feature. There is no "data residency checkbox" that magically processes `us-east-1` data in Europe. You must deploy to the actual region.

- **Send the data to us-east-1 but tag it with 'Location: EU':** Resource tagging is used for cost allocation, organizing resources, and IAM access control. Tags have absolutely no impact on the physical location of data processing or compliance laws.

- **Use a VPN to 'spoof' the developer's location to London:** Using a VPN changes the developer's IP address, but if their code still calls the `us-east-1` Bedrock API endpoint, the sensitive data is still being transmitted to and processed in the United States, completely violating the data residency requirement.


### 🔑 AIP-C01 Exam Keywords to Remember

When you see questions regarding compliance, geography, or data sovereignty on the exam, use these mappings:

- _"Data residency" / "Sovereignty" / "Must not leave the country"_ ➔ **Deploy in the specific AWS Region**

- _"Where is Bedrock data stored/processed?"_ ➔ **It remains in the region where the API call was made.** AWS does not use customer prompts or responses to train base models, and data does not cross regional boundaries.

- _"Cross-region inference"_ ➔ **An opt-in Bedrock feature** that allows AWS to route inference traffic across multiple regions to improve throughput, which _should not_ be used if strict single-region data residency is required.
_______
