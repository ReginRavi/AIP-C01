
 
GitHub - Priyak2728/docs-for-adv-gen-ai-aws-course
 
https://github.com/Priyak2728/llm-as-judge.git
 
https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro
 
https://hadyelsahar.github.io/t-rex/
 
https://skillbuilder.aws/learn/HSEKTD11NX/official-practice-question-set-aws-certified--generative-ai-developer--professional-aipc01--english/ZDANP82P4V
 
What are Foundation Models? - Foundation Models in Generative AI Explained - AWS
 
https://aws.amazon.com/bedrock/faqs/
 

 
 
https://rumn.medium.com/setting-top-k-top-p-and-temperature-in-llms-3da3a8f74832
 
https://us-east-1.student.classrooms.aws.training/class/pR8WY6fWm5iJjGrjVY8zLY
https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html
https://docs.aws.amazon.com/lambda/latest/dg/concepts-basics.html
What is Step Functions? - AWS Step Functions
https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html
https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-data-insights.html
https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-getting-started.html
GitHub - Priyak2728/docs-for-adv-gen-ai-aws-course
https://github.com/Priyak2728/llm-as-judge.git
https://docs.aws.amazon.com/IAM/latest/UserGuide/when-to-use-iam.html
What is Amazon S3? - Amazon Simple Storage Service
https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro
https://hadyelsahar.github.io/t-rex/
https://skillbuilder.aws/learn/HSEKTD11NX/official-practice-question-set-aws-certified--generative-ai-developer--professional-aipc01--english/ZDANP82P4V
What are Foundation Models? - Foundation Models in Generative AI Explained - AWS
https://aws.amazon.com/bedrock/faqs/
Serverless Search - Amazon OpenSearch Serverless - AWS
GitHub - Priyak2728/chunking-strategies-on-AWS
Create a knowledge base by connecting to a data source in Amazon Bedrock Knowledge Bases - Amazon Be…
 
https://aws.amazon.com/bedrock/flows/
Prompt caching for faster model inference - Amazon Bedrock
Models at a glance - Amazon Bedrock
Understanding intelligent prompt routing in Amazon Bedrock - Amazon Bedrock
https://github.com/Priyak2728/bedrock-flows
docs-for-adv-gen-ai-aws-course/one stop doc for ur prep.pdf at main · Priyak2728/docs-for-adv-gen-ai…
 
 
 
 

 
 
 
AWS Certification / Interview Cheat Sheet
Requirement	Best Choice
General Enterprise RAG	OpenSearch
Hybrid Search (Keyword + Semantic)	OpenSearch
Lowest Cost	S3 Vectors
Already using PostgreSQL	Aurora PostgreSQL
SQL + Vector Search	Aurora PostgreSQL
Knowledge Graph	Neptune
GraphRAG	Neptune
Fraud Detection	Neptune
IAM Relationship Analysis	Neptune
Billions of vectors	OpenSearch
Archive/Long-term Storage	S3 Vectors
For Exam Questions
If the scenario says:
•	"Enterprise chatbot" → OpenSearch
•	"Cheapest vector storage" → S3 Vectors
•	"Relational database + vectors" → Aurora PostgreSQL
•	"Relationship analysis / GraphRAG / Fraud / IAM hierarchy" → Neptune Analytics
 
 
Prompt Router vs Model Router (Easy Memory Trick)
 
 
Plain Text
Prompt Router
↓
Chooses the best MODEL
 
RAG
↓
Chooses the best DOCUMENTS
 
Agent
↓
Chooses the best TOOL
Show more lines
AWS exam questions often mention "reduce inference cost while maintaining response quality across varying prompt complexity" → that is a strong indicator for Bedrock Intelligent Prompt Routing.
 
 
 
AWS Exam Shortcut
Requirement	Best Service
Large-scale ETL & transformation	✅ AWS Glue ETL
Data validation & quality rules	✅ Glue Data Quality
Small event-driven transformations	Lambda
No-code data preparation	DataBrew
Vector search & retrieval	OpenSearch
 
Exam Keyword Mapping
Keywords in Question	Answer
Cleaning + Validation	Glue ETL + Data Quality
High-throughput pipeline	Glue ETL
Document preprocessing	Glue ETL
Data quality checks	Glue Data Quality
Chunking/Embedding preparation	Glue ETL
Certification Tip
When an AWS GenAI question mentions:
"complex data cleaning", "data validation", "quality checks", "ETL pipeline", "before ingestion into a Bedrock Knowledge Base"
👉 Choose AWS Glue ETL with Glue Data Quality.
 
 
Certification Shortcut
Requirement	Best Choice
Strongest environment isolation	✅ Separate AWS Accounts
Network isolation only	VPCs
Access control within one account	IAM Roles
Storage-level restrictions	S3 Bucket Policies
Answer: ✅ Use separate AWS Accounts for Development, Testing, and Production environments.
 
 
Exam Tip
Metric	Primary Use Case
✅ BLEU	Translation
✅ ROUGE	Summarization
Perplexity	Language model quality/prediction
Accuracy	Classification
AWS Exam Keyword
If the question says:
"compare generated text to human-created reference translations"
👉 BLEU is the answer.
If it says:
"evaluate generated summaries against reference summaries"
👉 ROUGE is usually the answer.
 
 
Exam Tip
Technique	Purpose
✅ Chain-of-Thought (CoT)	Step-by-step reasoning
Few-Shot Prompting	Learn from examples
Zero-Shot Prompting	Perform task with instructions only
RAG	Retrieve external knowledge
AWS Certification Keyword
If the question mentions:
"intermediate reasoning steps", "step-by-step thinking", "complex multi-step tasks", or "improving reasoning accuracy"
👉 Chain-of-Thought (CoT) Prompting is the correct answer.
 
AWS GenAI Exam Tip
Requirement	Best Choice
Small model fine-tuning, minimal management	✅ Serverless Training
Lowest-cost large training jobs	Spot Instances
LLM training across multiple GPUs	Distributed Training
Production inference	Real-time Endpoint
Exam Keyword Trap
If you see:
"small model", "lightweight workload", "reduce operational overhead", "no infrastructure management", "pay only for what you use"
👉 Choose Amazon SageMaker Serverless Training.
AWS Exam Shortcut
Requirement	Best Service
Large-scale ETL & transformation	✅ AWS Glue ETL
Data validation & quality rules	✅ Glue Data Quality
Small event-driven transformations	Lambda
No-code data preparation	DataBrew
Vector search & retrieval	OpenSearch
 
Exam Keyword Mapping
Keywords in Question	Answer
Cleaning + Validation	Glue ETL + Data Quality
High-throughput pipeline	Glue ETL
Document preprocessing	Glue ETL
Data quality checks	Glue Data Quality
Chunking/Embedding preparation	Glue ETL
Certification Tip
When an AWS GenAI question mentions:
"complex data cleaning", "data validation", "quality checks", "ETL pipeline", "before ingestion into a Bedrock Knowledge Base"
👉 Choose AWS Glue ETL with Glue Data Quality.
 
Provide your feedback on BizChat
 
 
AWS Exam Tip
When you see phrases such as:
•	Environment isolation
•	Prevent accidental access to production
•	Security boundary
•	Development vs Production separation
•	Generative AI with sensitive data
👉 Choose Separate AWS Accounts.
Certification Shortcut
Requirement	Best Choice
Strongest environment isolation	✅ Separate AWS Accounts
Network isolation only	VPCs
Access control within one account	IAM Roles
Storage-level restrictions	S3 Bucket Policies
Answer: ✅ Use separate AWS Accounts for Development, Testing, and Production environments.
Exam Tip
Metric	Primary Use Case
✅ BLEU	Translation
✅ ROUGE	Summarization
Perplexity	Language model quality/prediction
Accuracy	Classification
 
AWS Exam Keyword
If the question says:
"compare generated text to human-created reference translations"
👉 BLEU is the answer.
If it says:
"evaluate generated summaries against reference summaries"
👉 ROUGE is usually the answer.
 
 
 
 
AWS Exam Tip
Requirement	Service
Build RAG quickly	✅ Bedrock Knowledge Bases
Add safety controls	Guardrails
Tool/API orchestration	Agents
ML feature management	SageMaker Feature Store
Certification Keyword Clues
If the question mentions:
•	RAG
•	Amazon S3 document corpus
•	Chunking
•	Embeddings
•	Vector database integration
•	Managed retrieval
👉 The answer is Amazon Bedrock Knowledge Bases.
 
 
Exam Tip
Technique	Purpose
✅ Chain-of-Thought (CoT)	Step-by-step reasoning
Few-Shot Prompting	Learn from examples
Zero-Shot Prompting	Perform task with instructions only
RAG	Retrieve external knowledge
AWS Certification Keyword
If the question mentions:
"intermediate reasoning steps", "step-by-step thinking", "complex multi-step tasks", or "improving reasoning accuracy"
👉 Chain-of-Thought (CoT) Prompting is the correct answer.
 
 
Evaluation:
 
Use Case	Metric
RAG Retrieval	✅ Recall@K
Vector Search	✅ Recall@K / mAP
Embedding Evaluation	✅ Recall@K / mAP
Summarization	✅ ROUGE
Translation	✅ BLEU
Fluency	✅ Perplexity
Image Generation	✅ FID
Classification	✅ Accuracy
Hallucination Detection	✅ Groundedness / Faithfulness
Model Comparison	✅ Bedrock Model Evaluation
 
 
Exam Tip
Metric	Primary Use
✅ BERTScore / Embedding Similarity	Semantic similarity
BLEU	Translation quality
ROUGE	Summarization quality
F1 Score	Classification / QA evaluation
Perplexity	Language model prediction quality
AWS Certification Keyword
If the question mentions:
•	Semantic similarity
•	Meaning rather than exact wording
•	Embeddings
•	Reference answer comparison
👉 BERTScore (or other e
 
 
Requirement	Best Answer
Reduce tokens sent to FM	✅ Context Pruning
Reuse previous answers	Semantic Caching
Route requests to cheaper models	Multi-tier Model Selection
Handle long-running inference jobs	Asynchronous Inference
Keyword Mapping
If you see:
•	Minimize prompt size
•	Reduce context window usage
•	Lower token costs
•	Shorten conversation history
•	Reduce inference latency
👉 Apply context pruning to the conversation history. ✅
 
 
Exam Tip
Guardrail Feature	Purpose
✅ Custom Denied Words and Phrases	Block specific words/phrases
Topic Denials	Block entire topics
Filtered PII Categories	Detect and redact PII
Input Filters	Filter user prompts
Keyword to Remember
If the question says:
"list of words or phrases explicitly prohibited from being generated"
👉 Custom Denied Words and Phrases is the correct answer. ✅
 
Exam Tip
Requirement	Service
Private access to AWS service from VPC	✅ Interface VPC Endpoint
Outbound internet access from private subnet	NAT Gateway
Internet connectivity for VPC	Internet Gateway
DNS aliasing	Route 53 CNAME
AWS Certification Keyword
If you see:
"Traffic must not leave the AWS network", "private access to Bedrock", "Lambda in a VPC", or "AWS PrivateLink"
👉 Choose: Amazon VPC Endpoint (Interface type). 
 
 
Exam Tip
Requirement	Service
Test and compare Foundation Models without code	✅ Amazon Bedrock Playground
Cloud IDE	AWS Cloud9
Workflow orchestration	Step Functions
ML/AI development platform	SageMaker Studio
Keyword Clues
If the question mentions:
•	No-code
•	Interactive testing
•	Prompt experimentation
•	Foundation Models from multiple providers
•	Model evaluation
👉 Amazon Bedrock Console Playground is the correct answer. ✅
 
 
Exam Tip
Requirement	Service
API traffic splitting / A-B testing	✅ Amazon API Gateway
Workflow orchestration	Step Functions
DNS-based routing	Route 53
Resource cataloging	Service Catalog
Keyword Clues
If you see:
•	A/B testing
•	Traffic routing
•	50/50 split
•	Incoming API requests
•	Multiple SageMaker endpoints
👉 Amazon API Gateway is the best answer. 
 
Exam Tip
Requirement	Best Choice
Custom model-routing logic	✅ AWS Lambda
Safety and content controls	Guardrails
Document retrieval	Vector Database
Multi-step workflow orchestration	Step Functions
Keyword Clues
If the question mentions:
•	"If prompt length < X, use Model A"
•	"Route requests based on custom logic"
•	"Select models dynamically"
•	"Pre-process incoming requests"
👉 A pre-processing AWS Lambda function is the correct answer.
 
 
Exam Tip
Requirement	Service
Cost analysis and usage reporting	✅ Cost Explorer
Performance monitoring	CloudWatch
Cost optimization recommendations	Trusted Advisor
Storage cost details	S3 reports
Keyword Clues
If the question mentions:
•	Cost monitoring
•	Usage tracking
•	Budgeting
•	Cost breakdowns
•	Optimization of FM invocations
👉 AWS Billing and Cost Management Console (Cost Explorer) is the best answer
 
 
AWS Exam Tip
Requirement	Condition Key
Restrict access to a specific FM	✅ bedrock:TargetModelId
Restrict S3 objects by tag	s3:ResourceTag/*
Check calling service	aws:CalledVia
Keyword clue: If the question mentions "allow only a specific Bedrock model" or "restrict model invocation by model ID", the answer is bedrock:TargetModelId.
 
 
AWS GenAI Exam Tip
Metric	Measures
✅ Groundedness / Faithfulness	Answer matches retrieved documents
Relevance	Retrieved documents match the query
BLEU	Translation quality
ROUGE	Summarization quality
Latency	Response speed
Keyword Clues
If the question mentions:
•	Hallucinations
•	Conflicts with retrieved documents
•	Answer consistency
•	RAG evaluation
•	Source-supported responses
👉 Groundedness (Faithfulness) is the correct answer.
 
 
Requirement	Best-Fit AWS Service
Multi-agent collaboration	AWS Strands Agents
Complex workflow orchestration	AWS Step Functions
Specialized AI capabilities	Amazon Bedrock Agents
Context persistence	DynamoDB
Human-in-the-loop approvals	Step Functions approval patterns
Error handling & retries	Step Functions
Audit logging	CloudWatch / CloudTrail integration
Secure EHR APIs	API Gateway + VPC Endpoints
 
AWS Exam Tip
When a scenario mentions:
•	Multiple AI agents
•	Agent coordination
•	Human-in-the-loop
•	Complex workflows
•	Regulated industries (Healthcare, Finance)
•	Context persistence
•	External system integration
Look for:
 
 
 
Plain Text
Bedrock Agents
+ Step Functions
+ DynamoDB
+ API Gateway
 
 
Exam Tip
Requirement	Best Service
A/B testing for API requests	✅ API Gateway
DNS-weighted routing	Route 53 Traffic Flow
Event-driven workflows	EventBridge
Custom business logic	Lambda
Keyword Clues
If you see:
•	A/B Testing
•	80/20 traffic split
•	Canary deployment
•	Route requests between models/endpoints
•	Production traffic management
👉 Choose Amazon API Gateway.
 
 
Correct Answer: Use Amazon Bedrock batch inference with request batching to process multiple transactions in a single API call, combined with prompt compression techniques to reduce token consumption.
Why?
The question emphasizes:
•	50,000 transactions/hour
•	High costs and latency
•	Optimize token usage
•	Maintain fraud detection accuracy
•	Using the same model (Claude 3.5 Sonnet)
The biggest cost driver in LLM inference is typically token consumption. The most effective optimization is:
•	Batch multiple transactions together instead of making one API call per transaction.
•	Compress prompts by removing redundant instructions and minimizing context.
 
 
 
Plain Text
Current:
50,000 transactions
→ 50,000 API calls
 
Optimized:
50,000 transactions
→ Fewer batched API calls
→ Lower overhead
→ Better throughput
→ Fewer tokens per transaction
Show more lines
This directly reduces:
•	API invocation overhead
•	Input token costs
•	End-to-end latency
while preserving the use of the same high-quality model.
 
AWS GenAI Exam Tip
Requirement	Best Choice
Reduce token costs	✅ Prompt Compression
Reduce API overhead	✅ Request Batching
Consistent model quality	✅ Keep same FM
Queue workloads	SQS
Lower-cost model routing	Cascading Models
Repeated prompt reuse	Caching
Keyword Clues
When you see:
•	High-volume inference
•	Token optimization
•	Cost reduction
•	Maintain same model accuracy
•	Many small requests
 
AWS Exam Tip
When you see:
Problem	Service
Scanned PDFs	✅ Textract
OCR extraction	✅ Textract
Handwritten forms	✅ Textract
Entity extraction	✅ Comprehend
Data cleaning/normalization	✅ Lambda
Better FM input quality	✅ Preprocessing pipeline
Keyword Clues
If the question mentions:
•	Poor OCR
•	Scanned documents
•	Handwritten annotations
•	Missing metadata
•	Improve foundation model response quality
👉 The answer is:
✅ Amazon Textract + Amazon Comprehend + AWS Lambda normalization and quality scoring before Amazon Bedrock.
 
Input Prompt:
 
My name is John Smith, my SSN is 123-45-6789, and my email is john@example.com.
Show more lines
 
After Amazon Comprehend PII Redaction:
 
My name is [NAME], my SSN is [SSN], and my email is [EMAIL].
 
Then send the sanitized prompt to Amazon Bedrock.
 
AWS Exam Tip
Requirement	Service
Detect & redact PII before FM	✅ Amazon Comprehend
Encrypt sensitive data	AWS KMS
Protect web applications	AWS WAF
Control FM inputs/outputs and safety	Bedrock Guardrails
Keyword Clues
If you see:
•	HIPAA
•	GDPR
•	PII detection
•	PII redaction
•	Pre-processing pipeline
•	Remove sensitive data before sending to FM
👉 Choose Amazon Comprehend
 
Exam Keyword Mapping
Keywords	Answer
Lowest cost	✅ Asynchronous Endpoint
Latency acceptable	✅ Asynchronous Endpoint
Long-running inference	✅ Asynchronous Endpoint
Low-latency API	Real-Time Endpoint
Multiple models on one endpoint	Multi-Model Endpoint
Sporadic traffic with instant responses	Serverless Endpoint
AWS Certification Tip
If the question says:
"Minimize cost" + "Low traffic" + "High latency is acceptable"
👉 Choose Amazon SageMaker Asynchronous Endpoint. ✅
 
 
Exam Tip
Evaluation Method	Best Use Case
✅ Automated evaluation on static test set	Classification, benchmarking
Human Evaluation	Subjective quality assessment
A/B Testing	Production comparison
Random Walk Search	Not an FM evaluation technique
Keyword Clues
If the question mentions:
•	Classification task
•	Known labels
•	Pre-defined test dataset
•	Objective comparison
•	Consistent scoring
👉 Automated Model Evaluation on a static test set is the correct answer. ✅
 
AWS Exam Shortcut
Requirement	Service
RAG / document retrieval	Knowledge Bases
Safety and content controls	Guardrails
Multi-step action execution with tools	✅ Bedrock Agents
Visual workflow orchestration	Bedrock Flows
Keyword Clues
If you see:
•	Agent
•	Action groups
•	Lambda integration
•	Tool use
•	Multi-step tasks
•	Planning and execution
👉 Amazon Bedrock Agents is the correct answer. 
 
 
Exam Tip
Parameter	Effect
✅ Increase Temperature	More creativity and diversity
Decrease Temperature	More deterministic output
Increase Top-P	More diverse token selection
Decrease Top-P	More focused and repetitive output
Max Tokens	Controls response length
Keyword Clues
If the question mentions:
•	Repetitive output
•	Need more variety
•	Increase creativity
•	Diverse text generation
👉 Increase the temperature. 
 
 
 
Exam Tip
Endpoint Type	Model Loading Behavior
Standard Endpoint	Model loaded when endpoint starts
✅ Multi-Model Endpoint	Load requested model on demand
Serverless Endpoint	Container starts on demand
Async Endpoint	Queues requests for processing
Keyword clue: If the question mentions "maximize instance utilization", "host multiple models", or "cost savings", remember:
MME = Models are loaded into memory only when invoked (on demand).
 
 
AWS Exam Shortcut
Symptom	Most Likely Cause
Variable time between streamed tokens	✅ Network congestion/routing
Slow first token	Long prompt context
Throttling/high load	Provisioned throughput issue
Repetitive or creative responses	Temperature setting
Keyword Clue
If you see:
"streaming inference", "token jitter", "inconsistent token arrival times"
👉 Think network latency, congestion, and routing variability.
Answer: ✅ Network congestion and variable internet routing.
 
 
AWS Exam Tip
For questions mentioning:
•	Massive vector databases
•	Embedding validation
•	Capacity planning
•	Automated optimization
•	Operational excellence
•	Cost optimization
Choose the architecture that includes:
 
CloudWatch
+ Lambda Automation
+ EMR Validation
+ Auto Scaling
+ Step Functions
+ EventBridge
+ QuickSight
+ S3 Intelligent Tiering
 
This represents a fully automated, enterprise-grade vector store operational management architecture.
 
Exam Tip
When a question mentions:
•	Creative quality
•	Repetitive content
•	Hallucinations
•	Narrative coherence
•	GenAI-specific failure modes
•	LLM evaluation
Look for evaluation approaches such as:
✅ Golden datasets
✅ Output diffing
✅ Reasoning path tracing
✅ Groundedness/Faithfulness testing
Answer: ✅ Golden datasets + output diffing + reasoning path tracing.
 
 
Exam Tip
Scenario	Best Solution
Sequential FM requests causing latency	✅ Concurrent Invocation
Many small inference requests	✅ Request Batching
Predictable heavy workload	Provisioned Throughput
Repeated user context lookups	ElastiCache
Streaming event ingestion	Kinesis
Keyword Clues
When you see:
•	Sequential processing
•	High throughput required
•	Peak load
•	Latency during spikes
•	Maintain model quality
👉 The best answer is:
✅ Concurrent model invocation + request batching.
 
Exam Tip
When the question mentions:
•	RAG
•	Large knowledge base
•	Millions of chunks
•	Complex queries
•	Need better relevance and retrieval efficiency
Look for:
✅ Hierarchical Chunking
✅ Query Preprocessing
✅ Domain-Specific Entity Extraction (Comprehend Medical)
Keyword Mapping
Requirement	Best Solution
Improve retrieval relevance	✅ Hierarchical Chunking
Medical document understanding	✅ Comprehend Medical
Reduce search space	✅ Hierarchical Retrieval
Repeated query optimization	ElastiCache
Database scaling	Aurora pgvector
Search engine optimization	OpenSearch
Answer: ✅ Configure Amazon Bedrock Knowledge Bases with hierarchical chunking and implement query preprocessing with medical entity extraction using Amazon Comprehend Medical.
 
What hierarchical chunking solves
Hierarchical chunking helps:
✅ Better relevance
✅ Fewer irrelevant chunks
✅ Better retrieval accuracy
✅ Reduced context size sent to the LLM
 
 
From a real-world performance engineering perspective:
✅ OpenSearch with optimized indexing/parallel retrieval is likely the stronger answer because the issue described is retrieval latency at scale.
From an AWS certification perspective:
✅ Hierarchical chunking + Comprehend Medical may be the expected answer because it improves retrieval efficiency and relevance within the Bedrock Knowledge Bases workflow.
So if this came from an actual exam bank, I'd scrutinize the wording:
•	If the question emphasizes latency and scale → I'd lean toward OpenSearch.
•	If it emphasizes Bedrock Knowledge Bases optimization and relevance → I'd lean toward hierarchical chunking + Comprehend Medical.
 
 
Let's map the requirements:
Requirement	Solution Component
Thousands of regulatory documents daily	Bedrock Knowledge Bases
Multiple document formats (PDF, Word, HTML)	S3 + Knowledge Bases ingestion
Semantic search across 10 years of data	OpenSearch Vector Store
Real-time regulatory updates	Step Functions orchestration
Audit trails	CloudTrail
Regulatory compliance	CloudTrail + Data Sovereignty Controls
Historical document management	S3 Lifecycle Policies
Enterprise integration	Step Functions + APIs
Large-scale RAG	Bedrock Knowledge Bases
 
Exam Keywords
If you see:
•	Regulatory compliance
•	Audit trail
•	Document analysis
•	10+ years of historical data
•	Semantic search
•	Bedrock RAG
Think:
Bedrock Knowledge Bases
+
OpenSearch
+
CloudTrail
+
S3 Lifecycle Policies
+
Step Functions
 
 
Exam Keyword Mapping
Requirement	Best Strategy
Sub-2-second responses	✅ Pre-computation
Real-time recommendations	✅ Latency-optimized model
Minimize perceived delay	✅ Response streaming
Handle ingestion spikes	Kinesis
Queue workloads	SQS
Cache repeated lookups	ElastiCache
 
AWS Exam Tip
When you see:
•	Strict latency SLA
•	Real-time decisions
•	Time-sensitive recommendations
•	Need consistent response times
•	GenAI inference bottleneck
Look for:
✅ Pre-computation
✅ Faster model selection
✅ Response streaming
 
AWS Exam Tip
When you see:
•	Optimize cost
•	Different query complexity
•	Use smaller model for simple tasks
•	Use larger model for complex reasoning
•	Model routing
 
Think:
Automated Model Selection
 
or
Prompt/Model Router
 
Memory Trick
Simple Question
↓
Claude Haiku
 
Complex Analysis
↓
Claude Sonnet
Show more lines
✅ Answer: Use Amazon Bedrock with automated query-complexity-based routing, sending simple requests to Claude 3 Haiku and complex requests to Claude 3.5 Sonnet.
 
 
AWS Exam Tip
If you see:
•	Vector database
•	Semantic search
•	Sub-100ms latency
•	Massive concurrency
•	Knowledge base search
•	RAG retrieval optimization
Think:
 
Amazon OpenSearch Service
Sharding
k-NN / ANN
Multi-Index Strategy
 
✅ Final Answer:
Deploy Amazon OpenSearch Service with sharding strategies, implement multi-index approaches for specialized domains, and use hierarchical indexing techniques for optimal performance.
 
Exam Tip
Evaluation Method	Best Use Case
✅ Automated evaluation on static test set	Classification, benchmarking
Human Evaluation	Subjective quality assessment
A/B Testing	Production comparison
Random Walk Search	Not an FM evaluation technique
Keyword Clues
If the question mentions:
•	Classification task
•	Known labels
•	Pre-defined test dataset
•	Objective comparison
•	Consistent scoring
👉 Automated Model Evaluation on a static test set is the correct answer. ✅
 
Exam Tip
Parameter	Effect
✅ Increase Temperature	More creativity and diversity
Decrease Temperature	More deterministic output
Increase Top-P	More diverse token selection
Decrease Top-P	More focused and repetitive output
Max Tokens	Controls response length
Keyword Clues
If the question mentions:
•	Repetitive output
•	Need more variety
•	Increase creativity
•	Diverse text generation
👉 Increase the temperature.
 
Why DynamoDB is Popular for Context Persistence
Fast
Single-digit millisecond reads/writes.
Serverless
No database servers to manage.
Scalable
Millions of users and sessions.
Durable
Stores workflow state even if systems restart.
Integrates Easily
Works well with:
•	Lambda
•	Bedrock Agents
•	Step Functions
•	API Gateway
 
Exam Tip
Scenario	Best Solution
Sequential FM requests causing latency	✅ Concurrent Invocation
Many small inference requests	✅ Request Batching
Predictable heavy workload	Provisioned Throughput
Repeated user context lookups	ElastiCache
Streaming event ingestion	Kinesis
Keyword Clues
When you see:
•	Sequential processing
•	High throughput required
•	Peak load
•	Latency during spikes
•	Maintain model quality
👉 The best answer is:
✅ Concurrent model invocation + request batching.
 
•	If the question emphasizes latency and scale → I'd lean toward OpenSearch.
•	If it emphasizes Bedrock Knowledge Bases optimization and relevance → I'd lean toward hierarchical chunking + Comprehend Medical.
 
Requirement-to-Service Mapping
Requirement	Best AWS Service
Completeness Validation	AWS Glue Data Quality
Accuracy Validation	AWS Glue Data Quality + Comprehend Medical
Consistency Validation	Glue Data Quality Rules
Anomaly Detection	Amazon EMR + Spark
100 TB/day Processing	EMR Distributed Processing
2-Hour SLA	EMR Parallel Processing
Workflow Orchestration	Step Functions
Audit Logs	S3
Validation Results	DynamoDB
Monitoring	CloudWatch
Schema Validation	Glue Data Catalog
Medical Ontology Matching	Comprehend Medical
 
Exam Trick to Remember
When you see:
Data Quality
+
100 TB scale
+
Healthcare
+
Compliance
 
Think:
Glue Data Quality
+
EMR
+
Comprehend Medical
+
Step Functions
+
CloudWatch
+
S3
 
Requirement Mapping
Requirement	Service
Tool call tracking	CloudWatch
Tool latency monitoring	CloudWatch
Tool reliability	X-Ray
Multi-agent coordination	DynamoDB
Real-time analytics	Kinesis Analytics
Automated optimization	EventBridge
Reporting & dashboards	QuickSight
Feedback analysis	Comprehend
 
 
AWS Glue is the only option that explicitly provides data lineage capabilities.
Exam Keyword Mapping
Requirement	Best AWS Service
Data Lineage	✅ AWS Glue
Decision Logging	✅ CloudWatch Logs
AI Governance	✅ SageMaker Model Cards
Automated Remediation	✅ Step Functions
Compliance Audits	✅ All of the above combined
 
 
Legal Documents
 │
 ▼
 AWS Glue Lineage Tracking
 │
 ▼
 GenAI Processing
 │
 ▼
 CloudWatch Decision Logs
 │
 ▼
 Policy Validation
 │
 ├─ Passed
 │ ▼
 │ Response
 │
 └─ Failed
 ▼
 Step Functions
 ▼
 Remediation Workflow
 ▼
 Compliance Report
 
Model Governance
 │
 ▼
SageMaker Model Cards
 
 
 
CloudTrail = WHO did it?
 
Who did it?
When did it happen?
What API was called?
Who changed a resource?
Compliance
Important for:
•	HIPAA
•	GDPR
•	SOC2
•	PCI-DSS
 
CloudWatch = HOW is it performing?
How is the system performing?
How much CPU is being used?
How many errors occurred?
What is the latency?
 
X-Ray = WHY is it slow/failing?
Why is my request slow?
Where did the error occur?
Which service is causing bottlenecks?
 
API Gateway = 50 ms
Lambda = 100 ms
OpenSearch = 4.5 sec
Bedrock = 350 ms
 
Comparison Table
Feature	CloudTrail	CloudWatch	X-Ray
Main Purpose	Audit	Monitoring	Tracing
Answers	Who did it?	How is it performing?	Why is it slow/failing?
Stores API Activity	✅	❌	❌
Metrics	❌	✅	Limited
Logs	Limited	✅	Trace Logs
Alarms	❌	✅	❌
Latency Analysis	Basic	✅	✅ Deep Analysis
Root Cause Analysis	❌	Partial	✅
Compliance Audits	✅	❌	❌
Multi-Service Request Flow	❌	❌	✅
 
 
CloudTrail
 = SECURITY & AUDIT
 
CloudWatch
 = MONITOR & ALERT
 
X-Ray
 = TRACE & DEBUG
 
Let's map the requirements:
Requirement	Needed Capability
12 languages	Multilingual embeddings
Images + Text	Multimodal embeddings
Product catalogs	Semantic search
Electronics, Fashion, Automotive terminology	Domain adaptation
Product categorization	Fine-tuning support
Cross-modal retrieval	Shared embedding space
The strongest clue is:
Multi-modal RAG system processing images, specifications, and reviews
This requires a single embedding model that can represent both text and images in the same semantic space.
 
 
Exam Keyword Analysis
Keywords pointing to Titan Multimodal:
 
•	Multi-modal RAG
 
•	Images
 
•	Technical specifications
 
•	Customer reviews
 
•	Cross-lingual
 
•	Product categorization
 
The moment you see:
 
Image + Text + Retrieval
 
AWS usually expects:
Titan Multimodal Embeddings
 
 
AWS Exam Shortcut
Scenario	Best Embedding Choice
Text-only RAG	Titan Text Embeddings v2
Multilingual Text Search	Cohere Embed Multilingual
Image + Text Search	✅ Titan Multimodal Embeddings
Product Catalog Search	✅ Titan Multimodal Embeddings
Cross-modal Retrieval	✅ Titan Multimodal Embeddings
 
 
Requirement	Best AWS Service
Technical documents	Amazon Textract
Maintenance logs	Amazon Comprehend
Sensor anomaly detection	AWS IoT Analytics
Technical terminology standardization	Amazon Comprehend (Custom Entity Recognition)
Event correlation	AWS IoT Analytics
Multilingual documentation	Amazon Translate (can be added to pipeline)
Data quality scoring	Combined processing pipeline
 
Requirement Mapping
Requirement	AWS Service
Compliance validation	AWS Config
Audit trails	AWS CloudTrail
Role-based access control	IAM
Sensitive data discovery	Amazon Macie
Data governance	Combined framework
Regulatory audits	CloudTrail + Config
Compliance monitoring	Config Rules
Data classification	Macie
Least-privilege access	IAM
 
 
Bedrock Prompt Caching + MemoryDB
Prompt caching helps only when prompts are nearly identical.
Problems:
•	Semantic variations may miss the cache.
•	MemoryDB is excellent for low-latency caching but less suitable for semantic similarity retrieval.
Exam Tip
When you see:
•	RAG
•	Repeated document analysis
•	Similar wording
•	Cost reduction
•	Legal clauses
•	Semantic reuse
Think:
Vector Embeddings
+
Semantic Cache
+
OpenSearch
 
because semantically similar content generates the highest cache-hit rates.
 
Requirement	AWS Service
Healthcare Equity (Bias Detection)	SageMaker Clarify
Explainability	SageMaker Clarify
Privacy Protection	Differential Privacy + Macie
PHI Detection	Amazon Macie
Healthcare Data Management	Amazon HealthLake
Continuous Learning	Federated Learning
Global Diagnostic System	SageMaker Models + HealthLake
 
Exam Keyword Mapping
Keyword	AWS Service
Bias/Fairness	SageMaker Clarify
Explainability	SageMaker Clarify
Privacy	Differential Privacy
PHI Detection	Amazon Macie
Healthcare Storage	HealthLake
FHIR	HealthLake
Continuous Learning	Federated Learning
 
Exam Tip
Whenever you see:
 
Responsible AI
Healthcare Equity
Explainability
Bias Detection
Privacy
Governance
 
AWS almost always expects:
SageMaker Clarify
+
HealthLake
+
Macie
+
Privacy Controls
 
The requirements are:
1. Accuracy
The system must generate factually correct content.
Multi-step prompt engineering + fact-checking constraints helps:
 
Step 1: Retrieve facts
Step 2: Validate facts
Step 3: Generate response
Step 4: Verify against constraints
 
This is more reliable than a simple prompt.
 
2. Localization
Requirement:
Multiple languages
Regional adaptation
 
Amazon Translate provides:
•	Real-time translation
•	Multi-language support
•	Locale-specific rendering
Example:
 
English Product Description
↓
Amazon Translate
↓
French / German / Japanese
 
 
3. Cultural Adaptation
The question mentions:
Localization
Style adaptation
Cultural context
 
This requires more than translation.
Using:
OpenSearch Vector Database
 
to retrieve regional examples and cultural content allows the model to adapt messaging appropriately.
Example:
US Marketing Style
vs
Japanese Marketing Style
 
Different retrieved contexts can guide the response.
 
4. Demographic Personalization
Amazon Personalize helps tailor content based on:
•	Region
•	Customer segment
•	Preferences
•	Demographics
Example:
Young professionals
↓
Technology-focused language
 
Retirees
↓
Safety-focused language
 
Exam Keyword Mapping
Requirement	Best Fit
Accuracy	✅ Multi-step prompting + fact checking
Localization	✅ Amazon Translate
Cultural adaptation	✅ OpenSearch vector retrieval
Demographic personalization	✅ Amazon Personalize
Multi-language GenAI	✅ Bedrock
Exam Tip
If a question asks for:
 
Accuracy
+ Localization
+ Cultural Context
+ Demographic Style Adaptation
 
Look for a solution that combines:
Bedrock
+ Fact-Checking Prompts
+ RAG/Vector Retrieval
+ Translate
+ Personalize
 
AWS Exam Tip
When you see:
•	Reduce LLM cost
•	Multiple model sizes
•	Simple vs complex requests
•	Maintain quality
•	Intelligent routing
Think:
Small Model First
↓
Confidence Check
↓
Escalate to Larger Model
 
Memory Trick
Cheap Model
↓
Confident? → Yes → Return
 
Confident? → No
↓
Expensive Model
 
 
AWS/GenAI Exam Tip
When a question mentions:
•	Code repositories
•	Multiple programming languages
•	Imports/exports
•	Function retrieval
•	Module relationships
•	Code understanding
Choose:
✅ AST-Based Chunking with Dependency Graph Maintenance
because it preserves both code structure and semantic relationships, providing the highest retrieval accuracy for code-centric RAG systems
 
The biggest clue is:
"balance latency-cost tradeoffs"
For recommendation systems, most recommendations are predictable and repetitive.
1. Pre-computation
Instead of generating recommendations in real-time:
 
User Request
↓
LLM
↓
Recommendation
 
generate them ahead of time:
 
Off-Peak Hours
↓
AWS Batch
↓
Generate Popular Recommendations
↓
Store Results
 
Then:
 
User Request
↓
Cached Recommendation
↓
<100 ms response
 
This dramatically reduces both:
•	Cost
•	Latency
 
Exam Shortcut
Requirement	Best Technique
Ultra-low latency	✅ Pre-computation
Cheapest real-time FM	✅ Claude 3 Haiku
Complex recommendation workflow	✅ Parallel Requests
Perceived latency only	Streaming
Consistent capacity	Provisioned Throughput
Batch/async workloads	SQS
 
 
Memory Trick
 
Need <500 ms?
 
1. Pre-compute whenever possible
2. Use smaller models (Haiku)
3. Run parallel requests
4. Avoid expensive reasoning models
 
Requirement	AWS Service
Real-time data ingestion	Amazon MSK
Predictive insights	Amazon Bedrock
Specialized AI tasks	Multiple FMs
Workflow orchestration	Step Functions
Global data consistency	Aurora Global Database
ERP integration	Workflow orchestration
Peak season scalability	MSK + Bedrock
Reporting	QuickSight
 
Requirement	AWS Service
HIPAA Compliance	S3 Encryption + CloudTrail + PrivateLink
Clinical Safety	Bedrock Guardrails
Medical Entity Recognition	Comprehend Medical
EHR Integration	AWS PrivateLink
Audit Logging	CloudTrail
Secure Data Storage	Amazon S3
Research + Operational Data	S3 Lifecycle Management
PHI Protection	Encryption + Controlled Access
 
Memory Trick
Healthcare AI
 
Medical Terms
→ Comprehend Medical
 
Safe Responses
→ Guardrails
 
EHR Connectivity
→ PrivateLink
 
Audit
→ CloudTrail
 
Patient Data
→ Encrypted S3
 
Requirement-to-Service Mapping
Requirement	Best Service
Defect Analysis	Amazon Bedrock
ERP Integration	AWS Lambda
Compliance Workflows	AWS Step Functions
Enterprise Knowledge Access	Amazon Q Business
Technician Manuals	Amazon Q Business
Troubleshooting Assistance	Amazon Q Business
Scalable Event Processing	Lambda + Step Functions
Memory Trick
 
Manufacturing AI Platform
 
Analyze Defects
→ Bedrock
 
Update ERP
→ Lambda
 
Process Compliance Docs
→ Step Functions
 
Help Technicians
→ Amazon Q Business
 
 
Simple Memory Trick
 
Glue = Discover, Catalog, Transform
 
Lake Formation = Govern, Secure, Control
 
Or:
 
Glue = Data Engineer
 
Lake Formation = Data Security Officer
 
Typical Exam Keywords
 
•	Schema discovery
•	Metadata management
•	ETL
•	Data catalog
•	Data lineage
 
Think:
✅ AWS Glue
 
 
Comparison Table
Feature	AWS Glue	Lake Formation
Discover Data	✅	❌
Data Catalog	✅	Uses Glue Catalog
ETL	✅	❌
Metadata Management	✅	❌
Schema Discovery	✅	❌
Access Control	❌	✅
Governance	❌	✅
Compliance	Limited	✅
Row-Level Security	❌	✅
Column-Level Security	❌	✅
Data Lake Security	❌	✅
 
Memory Trick
 
Stream Data
→ Kinesis
 
Analyze & Route
→ Lambda
 
Generate Text
→ Bedrock Streaming
 
Coordinate Events
→ EventBridge
 
Aurora pgvector provides:
•	Relational storage
•	Vector similarity search
•	Enterprise-grade scalability
 
 
Memory Trick
Medical RAG System
 
Find Knowledge
→ Hybrid Search + pgvector
 
Control Cost
→ Token Optimization
 
Improve Speed
→ Semantic Cache
 
Maintain Consistency
→ Provisioned Throughput
 
Protect Data
→ Compliance Checks
 
Why AWS Strands Agents?
Strands Agents are designed for:
•	Multi-system reasoning
•	Tool orchestration
•	Context sharing
•	Long-running workflows
Why ECS with GPU Instances?
Large media files
Visual assets
Global production
Show more lines
GPU-backed ECS workloads support:
•	Image generation
•	Video processing
•	Rendering pipelines
•	AI media workflows
and scale much better than Lambda for heavy media operations.
 
 
 
✅ AWS Batch + FSx for Lustre + ParallelCluster
✅ IoT Core + IoT Analytics + Timestream
✅ SageMaker GPU Training + Ground Truth + Neo
Memory Trick
Autonomous Vehicle Platform
 
Collect Data
→ IoT Core + Timestream
 
Train Models
→ SageMaker + Ground Truth
 
Run Simulations
→ Batch + ParallelCluster + FSx
 
Requirement Mapping
Requirement	Best Service
Multi-agent system	Amazon Bedrock Agents
Agent orchestration	AWS Step Functions
Conversation context	DynamoDB
Real-time customer events	Amazon Kinesis
Product catalog caching	ElastiCache
Tool integration	Bedrock Custom Tools
Inventory lookup	Agent Tools
CRM integration	Agent Tools
Promotional traffic spikes	ElastiCache + Kinesis
 
Memory Trick
 
User Feedback Loop
 
Collect
→ API Gateway
 
Process
→ Lambda
 
Store
→ DynamoDB
 
Exam Tip
When you see:
 
Bedrock
+
ThrottlingException
+
Need lower latency
+
Keep using Bedrock
 
Think:
✅ Provisioned Throughput
 
Memory Trick
 
On-Demand
= Shared Capacity
 
Provisioned Throughput
= Dedicated Capacity
 
Amazon MSK
The requirement explicitly mentions:
IoT sensor data streams
Manufacturing environments produce massive streams:
 
Temperature
Pressure
RPM
Vibration
Machine Status
Show more lines
MSK supports:
•	High-throughput ingestion
•	Real-time processing
•	Event-driven analytics
 
Amazon Comprehend
Supports:
•	English
•	German
•	French
•	Japanese
•	Spanish
 
Why AWS Amplify?
Amplify provides:
✅ Rapid UI development
✅ Declarative front-end components
✅ Easy Bedrock integration
✅ Low-code experience
This supports both:
•	Technical users
•	Business stakeholders
Why Bedrock Prompt Flows?
Prompt Flows are specifically designed for:
 
No-Code AI Workflows
Visual AI Configuration
Prompt Chaining
Evaluation Flows
 
Why API Gateway Usage Plans?
The scenario explicitly mentions:
Handle rate limiting from various providers
API Gateway usage plans help control:
Requests Per Second
Burst Limits
Quota Limits
 
Why Exponential Backoff?
Financial APIs may temporarily fail because of:
•	Traffic Spikes
•	Network Issues
•	Transient Errors
 
Instead of immediately retrying:
 
•	Retry
•	Retry
•	Retry
 
use:
 
•	1 sec
•	2 sec
•	4 sec
•	8 sec
 
This reduces pressure on provider APIs and increases successful retries.
 
Exam Shortcut
When you see:
 
External APIs
+
Rate Limits
+
Failover
+
Retries
+
Resilience
 
 
Think:
 
API Gateway
+
Step Functions
+
Exponential Backoff
+
CloudWatch
 
Memory Trick
 
Too Many Requests?
→ API Gateway Usage Plans
 
Temporary Failure?
→ Exponential Backoff
 
Provider Down?
→ Step Functions Fallback
 
Need Visibility?
→ CloudWatch
 
Amazon Bedrock Provisioned Throughput
Benefits:
•	Dedicated inference capacity
•	Predictable latency
•	Reduced throttling
•	Consistent performance during peak periods
Exam Tip
When you see:
 
•	Millions of records
•	Overnight processing
•	Latency not important
•	High throughput required
 
Think:
✅ Amazon Bedrock Batch Inference
 
Memory Trick
 
Real-Time Request
→ InvokeModel
 
Millions of Documents
→ Batch Inference
 
RAG Memory Trick
 
Wrong Facts?
→ Grounding Validation
 
Wrong JSON?
→ Schema Validation
 
Best Practice
→ RAG + Validation Layer
 
✅ Best Fit for "Several Hours Is Acceptable"
A major exam clue:
"The business is comfortable with several hours of latency"
Whenever latency is not critical and volume is massive:
 
Real-Time → InvokeModel
 
Massive Volume + Flexible SLA
→ Batch Inference
 
 
Exam Shortcut
When you see:
SAML
SSO
Department-based Access
Least Privilege
No Access Keys
 
Think:
✅ IAM Identity Center + Permission Sets
or
✅ Cognito Federation + IAM Roles
 
Memory Trick
 
Enterprise Workforce Access
→ IAM Identity Center
 
Application Users
→ Cognito
 
Least Privilege
→ Role Per Group
 
No Long-Term Keys
→ Temporary Credentials
 
 Model Training & Evaluation History
 
How was the model trained?
How was it evaluated?
Which version is in production?
What datasets were used?
Show more lines
SageMaker Model Registry + ML Lineage + Model Cards provide:
•	Model versioning
•	Training lineage
•	Evaluation tracking
•	Dataset traceability
•	Governance documentation
 
Exam Shortcut
When you see:
 
Auditors
Model Governance
Data Lineage
Model Versions
Compliance
Show more lines
Think:
✅ SageMaker Model Registry
✅ ML Lineage Tracking
✅ Model Cards
 
Memory Trick
Model Governance
→ SageMaker Registry + Lineage + Model Cards
 
Data Governance
→ Glue Data Catalog
 
Inference Audits
→ Structured CloudWatch Logs
 
Exam Memory Trick
 
Vector Search Slow?
 
Too Many Small Shards
↓
Use Fewer Larger Shards
 
Latency Problem
≠ More Replicas
 
Fan-Out Problem
≠ More Shards
 
AWS Exam Shortcut
When you see:
 
Bedrock Agent
+
REST API
+
OpenAPI Specification
+
Least Custom Code
 
Think:
OpenAPI
↓
Action Group
↓
Lambda
↓
Backend Service
 
Memory Trick
 
Already Have OpenAPI?
 
Don't Build Tools.
 
Import OpenAPI
↓
Bedrock Action Group
↓
Lambda
 
 
Exam Tip
When you see:
 
Mixed workloads
Simple + Complex requests
Need cost reduction
Need quality preservation
 
Think:
 
Multiple Models
+
Model Evaluations
+
Request Routing
 
Memory Trick
Cheap Tasks
→ Cheap Model
 
Complex Tasks
→ Powerful Model
 
Choose Models
→ Bedrock Model Evaluations
 
Route Requests
→ Intelligent Routing
 
A/B Test Different Foundation Models
Examples:
 
Environment A → Claude
Environment B → Titan
 
Experiment A → Claude Sonnet
Experiment B → Titan Premier
 
Using AWS AppConfig allows the team to:
•	Change models without code deployments
•	Configure per-environment behavior
•	Run experiments centrally
•	Roll back configurations safely
 
Exam Tip
When you see:
 
A/B Testing Models
No Code Changes
Show more lines
Think:
✅ AWS AppConfig
When you see:
 
Bedrock
+
Regional Failover
 
Think:
✅ Cross-Region Inference ✅ Inference Profiles
 
Memory Trick
Choose Model Dynamically
→ AppConfig
 
Survive Region Failure
→ Cross-Region Inference
 
Minimal Operations
→ Keep Bedrock Managed
 
Exam Tip
When you see:
Interactive chatbot
+
Bursty traffic
+
Low operational overhead
+
No model hosting
 
Think:
✅ API Gateway → Lambda → Amazon Bedrock (On-Demand Inference)
Memory Trick
 
Chatbot
→ InvokeModel
 
Batch Jobs
→ Batch Inference
 
Predictable Enterprise Load
→ Provisioned Throughput
 
Custom Model Hosting
→ SageMaker
 
Exam Tip
When you see:
 
MCP
+
Short-lived tools
+
Bursty traffic
+
No servers
 
Think:
 
API Gateway
+
Lambda
+
Stateless MCP Servers
 
Memory Trick
 
MCP + Serverless
 
Tool
↓
Lambda
 
Expose
↓
API Gateway
 
Consume
↓
MCP Clients
 
Lower-dimensional embeddings:
 
Smaller vectors
↓
Less storage in OpenSearch
↓
Lower indexing costs
↓
Faster vector queries
↓
Lower embedding costs
 
Exam Tip
When you see:
 
Too many embeddings
High vector storage cost
Large corpus
Small quality reduction acceptable
 
Think:
✅ Lower embedding dimensions
When you see:
Synchronous per-document processing
Can't keep up
Latency not critical
 
Think:
✅ Batch ingestion
 
Memory Trick
Reduce Cost
→ Smaller Embeddings
 
Reduce Ingestion Load
→ Batch Processing
 
Short Documents
→ Don't Chunk More
 
❌ Option 4: Semantic Chunking
Semantic chunking can improve retrieval quality for large documents, but these are:
Short news articles
Show more lines
Chunking would likely:
•	Increase the number of embeddings
•	Increase OpenSearch storage
•	Increase ingestion costs
The opposite of the stated goal.
 
Exam Tip
When you see:
 
Confluence
SharePoint
RAG
Minimal Custom Code
Amazon Bedrock
 
Think:
Bedrock Knowledge Base
+
Managed Connectors
+
OpenSearch Serverless
 
Memory Trick
Enterprise Documents
↓
Knowledge Base
 
Need RAG Fast?
↓
Don't Build Pipelines
 
Use Bedrock Knowledge Bases
 
When you see:
Large-scale processing
Results not needed immediately
High volume
Throttling issues
 
Think:
✅ Amazon Bedrock Batch Inference
 
Memory Trick
Real-time responses
→ InvokeModel
 
Millions/thousands of records
→ Batch Inference
 
Need throughput, not latency
→ Batch Inference
 
✅ Option 5: Aurora PostgreSQL + pgvector for Documents
This is ideal for:
 
Policy Documents
Regulatory Reports
Large PDFs
Structured Metadata
 
Architecture:
 
PDFs in S3
↓
Chunk Content
↓
Generate Embeddings
↓
Aurora PostgreSQL (pgvector)
 
Metadata:
- Product Line
- Region
- Effective Date
 
PDF Storage:
- Remains in S3
 
Benefits:
✅ Rich metadata filtering
✅ Vector similarity search
✅ No need to store full PDFs in the vector store
✅ Leverages existing Aurora investment
 
When you see:
 
Real-Time Data
+
DynamoDB
+
Semantic Search
 
Think:
✅ DynamoDB → OpenSearch Vector Search
 
Memory Trick
Long Documents
→ Aurora pgvector
 
Fast-Changing Notes
→ OpenSearch Vector Search
 
Original Files
→ Stay in S3
 
Exam Tip
When you see:
 
Large static prompt
Same instructions every request
High InputTokenCount
Need lower cost and latency
Show more lines
Think:
✅ Amazon Bedrock Prompt Caching
 
Memory Trick
 
Same Prompt Prefix
↓
Prompt Caching
 
Same Response Reuse
↓
Semantic Caching
 
Current Problem
With many small shards:
 
 
 
Plain Text
1
Query
2
↓
3
Shard 1
4
Shard 2
5
Shard 3
6
...
7
Shard 100+
Show more lines
Each vector search must:
•	Execute on many shards
•	Merge results from many shards
•	Coordinate across nodes
This creates:
✅ High CPU overhead
✅ Excessive shard coordination
✅ Increased p95/p99 latency
 
Why Fewer, Larger Shards Help
A better architecture:
 
 
 
Plain Text
1
Query
2
↓
3
Shard 1 (40 GB)
4
Shard 2 (40 GB)
5
Shard 3 (40 GB)
6
Shard 4 (40 GB)
Show more lines
Benefits:
•	Fewer shard searches
•	Lower coordination overhead
•	Better ANN (Approximate Nearest Neighbor) performance
•	Lower CPU consumption
•	Faster vector retrieval
For large OpenSearch vector workloads, a common best practice is to avoid excessive shard counts and use appropriately sized shards (often tens of GB per shard).
 
Exam Memory Trick
 
Vector Search Slow?
↓
Too Many Shards
 
Fix:
Fewer + Larger Shards
 
Latency Problem
≠ More Shards
 
CPU Problem
≠ More Fan-Out
 
Memory Trick
 
Chatbot
→ On-Demand Bedrock
 
Heavy Batch Processing
→ Provisioned Throughput
 
No Infrastructure Management
→ Stay on Bedrock
 
Exam Tip
When you see:
 
Fine-tuned model
+
Already using Bedrock
+
Want least operations
+
Reuse Bedrock APIs
 
Think:
✅ Amazon Bedrock Custom Model Import
Memory Trick
 
Custom Model
↓
Import to Bedrock
 
Need Real-Time
↓
Bedrock Runtime API
 
Need Least Ops
↓
Avoid SageMaker Endpoints
 
 
 
Why?
With InvokeModelWithResponseStream, the response is delivered incrementally over a long-lived connection. If a network interruption occurs after the request has already started streaming, the AWS SDK's standard retry mechanism generally cannot resume the partially completed stream.
A resilient design should:
•	Detect stream interruption.
•	Retry the request.
•	Resend the same prompt and conversation history (or maintain application state).
•	Handle potential duplicate or partial responses appropriately.
Example flow:
 
Client
↓
InvokeModelWithResponseStream
↓
Partial Response Received
↓
Network Failure
↓
Custom Retry Logic
↓
Resend Prompt + History
↓
Continue Processing
 
For AWS Bedrock streaming APIs:
 
Transient API failure before response
→ SDK retries
 
Interrupted streaming response
→ Application-level retry logic
 
Exam Memory Trick
 
Slow Vector Search?
 
First:
✅ HNSW / Vector Engine
 
Then:
✅ Proper Data Nodes
 
Not:
❌ More Replicas
❌ UltraWarm
❌ Lexical Search
 
Exam Memory Trick
Embeddings / Vector Search
→ Recall@K
→ mAP
 
Summarization
→ ROUGE
 
Translation
→ BLEU
 
Language Model Prediction
→ Perplexity
 
Here's a handy AWS GenAI Evaluation Metrics Cheat Sheet:
Metric	Used For	Best For	Measures	Suitable for Embeddings/RAG?
Recall@K	Information Retrieval	Vector Search, RAG	Whether relevant documents appear in the top K results	✅ Yes
Mean Average Precision (mAP)	Information Retrieval	Semantic Search, RAG	Ranking quality of retrieved documents	✅ Yes
ROUGE	Summarization	Text Summaries	Overlap between generated and reference summaries	❌ No
BLEU	Machine Translation	Translation Tasks	N-gram overlap with reference translation	❌ No
Perplexity (PPL)	Language Models	Model Evaluation	How well a model predicts next tokens	❌ No
Quick Examples
Use Case	Metric
RAG Retrieval Quality	✅ Recall@K, mAP
Vector Database Evaluation	✅ Recall@K, mAP
Semantic Search Performance	✅ Recall@K, mAP
Document Summarization	✅ ROUGE
Language Translation	✅ BLEU
Base LLM Performance	✅ Perplexity
Token Prediction	✅ Perplexity
 
Implement the "Idempotency Key pattern" within the tool's AWS Lambda function.
 
Why?
The scenario involves a high-impact, state-changing action:
 
 
 
Plain Text
Book Flight
Create Order
Submit Payment
Approve Loan
Show more lines
The biggest risk is:
 
 
 
Plain Text
Agent retries
Network issues
Duplicate requests
User resubmission
Show more lines
Without protection:
 
 
 
Plain Text
Book Flight
↓
Timeout occurs
↓
Agent retries
↓
Flight booked twice ❌
Show more lines
 
Idempotency Key Pattern
An idempotency key is a unique identifier attached to a request.
Example:
 
 
 
JSON
{
"bookingId": "ABC123",
"flight": "AI101",
"idempotencyKey": "txn-987654"
}
 
Workflow:
 
Request Received
↓
Check Idempotency Key
↓
Already Processed?
┌─────────┴─────────┐
│ │
Yes No
│ │
Return Existing Execute Action
Response Store Key
 
Exam Memory Trick
 
Read-Only Action
→ Normal Tool Call
 
State-Changing Action
→ Idempotency Key
 
Payment?
Booking?
Order Creation?
→ Idempotency
 
Exam Memory Trick
Requirement	Deployment Strategy
Zero Downtime	✅ Blue/Green
Gradual Validation	✅ Canary
Controlled Rollout	✅ Linear
Highest Risk	❌ All-at-Once
Instance-by-Instance Update	❌ Rolling
Quick Recall
SageMaker Endpoint Update
+
Zero Downtime
↓
Blue/Green Deployment
(Canary or Linear)
 
Exam Cheat Sheet
Requirement	Feature
Stop request after X seconds	✅ SDK Client Timeout
Limit output size	✅ max_tokens_to_sample
Stop on specific text	✅ stop_sequences
Repeatable output	✅ seed
Memory Trick
Time Limit?
→ Client Timeout
 
Token Limit?
→ max_tokens_to_sample
 
Text Trigger?
→ stop_sequences
 
Repeatability?
→ seed
 
Service	Captures Full Payload?	Purpose
AWS CloudTrail Data Events	❌ No	Records API activity metadata (who, when, what API)
Amazon CloudWatch Logs	✅ Yes	Stores application logs, including prompts and model responses if logging is enabled
AWS Config	❌ No	Resource configuration and compliance tracking
Amazon Macie	❌ No	Sensitive data discovery and classification
 
 
CloudTrail records:
 
InvokeModel called
User/Role
Timestamp
Region
Resource
 
 
But it does not record the complete prompt and model response payload by default.
 
Why CloudWatch Logs Is Correct
 
For Bedrock applications that need:
 
 
Full Prompt
Full Response
Audit Trail
Payload Inspection
 
 
the application (or Bedrock invocation logging features where applicable) writes the request/response data to CloudWatch Logs, making it the primary source for payload-level auditing.
 
Exam Memory Trick
 
Who called API?
→ CloudTrail
 
What resources changed?
→ AWS Config
 
Where is sensitive data?
→ Macie
 
Need request/response payloads?
→ CloudWatch Logs
 
Exam Memory Trick
Requirement	SageMaker Option
Real-time, always-on	Real-time Endpoint
Multiple models on shared infrastructure	Multi-Model Endpoint
Long-running background jobs	Asynchronous Endpoint
Scale to zero, lowest idle cost	✅ Serverless Inference
Quick Recall
 
Need Scale-to-Zero?
↓
SageMaker Serverless Inference
 
Observation	Problem
Training ↓, Validation ↑	✅ Overfitting
Training High, Validation High	✅ Underfitting
Production performance degrades over time	✅ Model Drift
Loss becomes NaN or extremely large	✅ Exploding Gradients
Memory Trick
 
Good on Training
Bad on Validation
↓
Overfitting
 
✅ Final Answer: Overfitting.
Exam Memory Trick
Requirement	Artifact Needed
Custom vLLM/TGI serving	✅ Docker Container
SageMaker custom inference runtime	✅ Docker Container
Container storage	✅ Amazon ECR
Model tuning parameters	❌ Hyperparameters
Orchestration	❌ Lambda
 
Exam Cheat Sheet
Requirement	Service
ML Workflow Automation	✅ SageMaker Pipelines
Model Approval Workflow	✅ SageMaker Pipelines
Conditional Registration	✅ SageMaker Pipelines
Model Registry Integration	✅ SageMaker Pipelines
Event Routing	EventBridge
General Workflow Orchestration	Step Functions
ML IDE	SageMaker Studio
 
Quick Cheat Sheet
Requirement	Parameter
Limit reasoning/tool calls	✅ max_iterations
Limit output length	✅ max_tokens_to_sample
Stop on specific text	✅ stop_sequences
Control randomness	✅ temperature
Memory Trick
 
Too Many Tool Calls?
↓
max_iterations
 
Too Many Tokens?
↓
max_tokens_to_sample
 
Amazon Aurora PostgreSQL with the pgvector extension
Why?
The requirement is:
•	Semantic search
•	RAG (Retrieval-Augmented Generation)
•	Billions of vector embeddings
•	Low latency
•	Scalable vector similarity search
Among the options provided, Aurora PostgreSQL with pgvector is the only purpose-built vector store solution.
Benefits:
✅ Native vector storage
✅ Approximate Nearest Neighbor (ANN) search support
✅ Metadata filtering
✅ SQL integration
✅ Suitable for enterprise RAG workload
 
Use Case	Service
Vector Search in PostgreSQL	✅ Aurora PostgreSQL + pgvector
Enterprise Semantic Search	✅ OpenSearch Vector Engine / pgvector
Document Storage	Amazon S3
Messaging	Amazon SQS
Key-Value Store	DynamoDB
Memory Trick
Need Vector Search?
↓
pgvector
 
Need Object Storage?
↓
S3
 
Need Queue?
↓
SQS
 
frequency_penalty or presence_penalty
 Why?
The symptom is:
Model repeating phrases
Model looping
Model generating the same words repeatedly
 
presence_penalty
Penalizes tokens that have already appeared at least once.
This encourages the model to introduce new topics or vocabulary rather than revisiting the same content.
 
Quick Cheat Sheet
Problem	Parameter
Repetitive phrases	✅ frequency_penalty
Repeating topics	✅ presence_penalty
Too deterministic	✅ temperature
Token selection diversity	✅ top_p
Response too long	✅ max_tokens_to_sample
Memory Trick
 
Model Keeps Repeating?
↓
frequency_penalty
presence_penalty
 
Too Predictable?
↓
temperature
 
Too Long?
↓
max_tokens_to_sample
 
Linear Deployment
Why?
The requirement is very specific:
Shift 10% of traffic every 30 minutes over a total period of 4 hours.
This is exactly what a Linear Deployment does in Amazon SageMaker.
Linear Deployment Pattern
 
 
 
Plain Text
Time 0 → 10% New Model, 90% Old Model
30 min → 20% New Model, 80% Old Model
60 min → 30% New Model, 70% Old Model
...
240 min → 100% New Model
Show more lines
Benefits:
•	✅ Gradual rollout
•	✅ Predictable traffic shifting
•	✅ Continuous monitoring during deployment
•	✅ Easy rollback if issues occur
 
SageMaker Deployment Cheat Sheet
Requirement	Deployment Type
Immediate switch	All-at-once
Small test then full rollout	Canary
Gradual percentage-based rollout	✅ Linear
Zero-downtime strategy (umbrella pattern)	Blue/Green
 
Requirement	Service
Track training runs	✅ SageMaker Experiments
Compare hyperparameters	✅ SageMaker Experiments
Track metrics (loss/accuracy)	✅ SageMaker Experiments
Register approved models	✅ SageMaker Model Registry
Store artifacts	Amazon S3
Capture logs	CloudWatch Logs
 
Memory Trick
 
Train → Compare → Analyze
↓
SageMaker Experiments
 
Approve → Deploy
↓
Model Registry
 
Temperature
Why?
The requirement is:
Use a smaller, cheaper model but maintain high fidelity to the prompt's intent.
The temperature parameter controls the randomness of token selection:
•	Low temperature (close to 0) → More deterministic, focused, and consistent outputs.
•	High temperature → More creative, diverse, and unpredictable outputs.
 
Memory Trick
 
Need Accurate, Predictable Output?
↓
Temperature → 0
 
 
Retrieval Methods Comparison
Retrieval Type	Component	Finds
Lexical Search	✅ BM25 / Lucene	Same or similar words
Semantic Search	✅ k-NN Vector Search	Similar meaning, different wording
Ranking Improvement	✅ Cross-Encoder Re-ranker	Reorders retrieved results
Custom Retrieval Logic	Lambda	Application-specific behavior
 
 
 
 
AWS RAG Exam Memory Trick
 
Same Words?
→ BM25 / Lucene
 
Same Meaning?
→ k-NN Vector Search
 
Better Ranking?
→ Re-ranker
 
Hybrid Search Best Practice
Many production RAG systems use:
BM25 (Lexical)
+
k-NN (Semantic)
 
Fine-Tuning Troubleshooting Cheat Sheet
Symptom	Most Likely Fix
Validation loss oscillates wildly	✅ Lower learning rate
Training loss low, validation loss high	✅ Overfitting
Loss becomes NaN or huge	✅ Lower learning rate / gradient clipping
Training and validation both poor	✅ Larger model, more epochs, better data
Responses too random	✅ Lower temperature
 
Memory Trick
Training Unstable?
↓
First Action:
Lower Learning Rate
 
1e-4
↓
1e-5
 
 Perplexity (PPL)
Why?
The question asks for a metric that measures:
Fluency, coherence, and grammatical correctness of generated text.
Perplexity (PPL) is the standard metric used to evaluate how well a language model predicts the next token in a sequence.
A lower perplexity generally indicates:
•	✅ More fluent text
•	✅ Better grammatical structure
•	✅ More coherent sentence generation
•	✅ Better language modeling capability
 
 
Quick SageMaker Auto Scaling Cheat Sheet
Setting	Purpose
Min Capacity	Lowest number of instances
Max Capacity	✅ Hard upper limit on instances
Target Tracking Policy	Scaling behavior/trigger
Cooldown Period	Delay between scaling actions
Memory Trick
 
Want a Cost Ceiling?
↓
Max Capacity
 
Want Always-On Capacity?
↓
Min Capacity
 
SageMaker Monitoring Cheat Sheet
Requirement	Service
Detect data drift	✅ SageMaker Model Monitor
Detect model/prediction drift	✅ SageMaker Model Monitor
Training debugging	✅ SageMaker Debugger
Experiment tracking	✅ SageMaker Experiments
API auditing	✅ CloudTrail
Memory Trick
Production Predictions Changing?
↓
Model Monitor
 
Training Issues?
↓
Debugger
 
Compare Training Runs?
↓
Experiments
 
AWS Audit Services Cheat Sheet
Requirement	Service
API activity auditing	✅ CloudTrail
Resource compliance tracking	AWS Config
Operational metrics and monitoring	CloudWatch
Event routing and automation	EventBridge
Memory Trick
Who called the API?
↓
CloudTrail
 
How many calls?
↓
CloudWatch
 
Resource compliance?
↓
AWS Config
 
Quick Bedrock Agent Cheat Sheet
Requirement	Configuration
Agent behavior & reasoning	✅ Instruction Prompt (System Prompt)
Tool definitions	✅ Action Groups
External knowledge	✅ Knowledge Base
Output length	✅ max_tokens_to_sample
Memory Trick
 
Want the Agent to think step-by-step?
↓
System Prompt
 
Want the Agent to use tools?
↓
Action Groups
 
Want the Agent to retrieve facts?
↓
Knowledge Base
 
Requirement	Service/Feature
Execute AI-generated code safely	✅ Bedrock Code Interpreter
Content safety	✅ Bedrock Guardrails
ML development environment	✅ SageMaker Notebooks
Serverless functions	✅ AWS Lambda
Memory Trick
 
Generate Code
+
Run Code
+
Sandbox
↓
Bedrock Code Interpreter
 
Requirement	Solution
Agent needs external API	✅ Action Group + Lambda
Agent needs SQL database access	✅ Action Group + Lambda
Document retrieval	✅ Knowledge Base
Workflow orchestration	✅ Bedrock Flows
 
Invisible digital watermarking
Why?
Amazon Titan Image Generator G1 includes invisible digital watermarking to help identify that an image was generated by AI.
Benefits:
•	✅ Embedded directly into the generated image
•	✅ Not visible to human viewers
•	✅ Helps detect AI-generated content
•	✅ Supports content authenticity and responsible AI practices
•	✅ Can be used later to verify the image origin
 
When using Amazon SageMaker to host a generative model, which feature provides a way to explain the importance of different input features to the model’s prediction? 
•	SageMaker Pipelines.
•	SageMaker Feature Store.
•	SageMaker Clarify.
•	SageMaker Model Monitor.
 
Copilot said:
✅ Correct Answer: 3. SageMaker Clarify
Why?
Amazon SageMaker Clarify is the AWS service designed for:
•	✅ Model explainability
•	✅ Feature importance analysis
•	✅ Bias detection
•	✅ Understanding model predictions
When hosting a model in SageMaker, Clarify can help answer questions such as:
Why did the model make this prediction?
Which input features had the biggest impact?
How important was each feature?
 
 
 
 
Quick SageMaker Cheat Sheet
Requirement	Service
Explain predictions / feature importance	✅ SageMaker Clarify
Detect bias	✅ SageMaker Clarify
Monitor drift in production	✅ SageMaker Model Monitor
Store ML features	✅ SageMaker Feature Store
Automate ML workflows	✅ SageMaker Pipelines
Memory Trick
 
Why did the model predict this?
↓
Clarify
 
Is the model drifting?
↓
Model Monitor
 
Where are features stored?
↓
Feature Store
 
Responsible AI Principles Cheat Sheet
Principle	Focus
✅ Fairness	Equitable treatment, reducing bias and discrimination
Transparency	Openness about AI systems and usage
Explainability	Understanding and interpreting decisions
Robustness	Reliability, safety, and resilience
Memory Trick
 
Bias?
Discrimination?
Equal Treatment?
↓
Fairness
 
Amazon Bedrock Model Evaluation
Why?
The question asks for a feature that enables comparison of:
•	✅ Time to First Token (TTFT)
•	✅ Throughput
•	✅ Multiple foundation models
•	✅ Using the same standardized prompt set
Amazon Bedrock Model Evaluation is designed to evaluate and compare foundation models using consistent datasets and prompts. This allows developers to make informed decisions about model selection based on both quality and performance characteristics.
 
Quick Exam Cheat Sheet
Requirement	AWS Service
Compare FM quality and performance	✅ Bedrock Model Evaluation
Dedicated model capacity	Bedrock Provisioned Throughput
Analyze logs	CloudWatch Logs Insights
AWS best-practice recommendations	Trusted Advisor
Memory Trick
 
Need to Compare Models?
↓
Bedrock Model Evaluation
 
Need Guaranteed Capacity?
↓
Provisioned Throughput
 
The Visual Builder (Canvas)
Why?
Amazon Bedrock Flows provides a Visual Builder (Canvas) that enables developers to design and orchestrate GenAI workflows using a drag-and-drop interface.
With the Visual Builder, you can visually connect:
•	✅ Multiple LLM/Foundation Model steps
•	✅ Prompt nodes
•	✅ Condition/decision branches
•	✅ Data transformation steps
•	✅ Knowledge Base lookups
•	✅ Inputs and outputs
 
Requirement	Feature
Visual GenAI workflow orchestration	✅ Bedrock Flows Visual Builder (Canvas)
Prompt management	Prompt Management Console
Agent reasoning & tool use	Bedrock Agents
General AWS workflow orchestration	Step Functions Studio
Memory Trick
 
Need Drag-and-Drop GenAI Workflow?
↓
Bedrock Flows Canvas
 
Need Tools & Reasoning?
↓
Bedrock Agent
 
 
Cosine Similarity
 
Why?
When vectors are normalized (scaled to unit length), Cosine Similarity is the standard metric used to measure how similar two vectors are based on the angle between them.
 
Use Case	Common Metric
Text Embeddings	✅ Cosine Similarity
Semantic Search	✅ Cosine Similarity
RAG Retrieval	✅ Cosine Similarity
Binary Vectors	Hamming Distance
Spatial Distance Problems	Euclidean (L2)
Memory Trick
 
Normalized Embeddings
↓
Cosine Similarity
 
Same Meaning
↓
Similar Angle
 
“Model Unit” (MU) commitment.
Why?
For Amazon Bedrock Provisioned Throughput, especially when using:
•	Custom Models
•	Fine-tuned Models
•	Imported Models
you must purchase and allocate Model Units (MUs).
A Model Unit (MU) represents dedicated inference capacity reserved for your model, providing:
•	✅ Predictable performance
•	✅ Guaranteed throughput
•	✅ Consistent latency
•	✅ Dedicated model capacity
 
Architecture
Custom Model
↓
Provisioned Throughput
↓
Model Units (MUs)
↓
Dedicated Inference Capacity
 
Exam Memory Trick
 
Bedrock On-Demand
↓
Pay Per Request
 
Bedrock Provisioned Throughput
↓
Model Units (MUs)
↓
Dedicated Capacity
 
Option	Why It's Incorrect
Learning Rate	A training hyperparameter, not an evaluation metric.
R-squared (R²)	Used for regression problems, not classification.
RMSE	Measures error in regression tasks, not classification accuracy.
Accuracy	✅ Measures the percentage of correctly classified images.
 
Quick ML Metric Cheat Sheet
Problem Type	Common Metric
Image Classification	✅ Accuracy
Binary Classification	Accuracy, Precision, Recall, F1
Regression	RMSE, MAE, R²
Summarization	ROUGE
Translation	BLEU
Retrieval/RAG	Recall@K, mAP
Memory Trick
"How many predictions are correct?"
↓
Accuracy
 
Option	Purpose
✅ Word Filters (Custom Word List)	Detect and block specific forbidden words or phrases
Sensitive Information Masking	Protect sensitive business information
PII Redaction	Remove personal information (emails, phone numbers, SSNs, etc.)
Toxic Content Filtering	Detect harmful, abusive, or unsafe content
 
Exam Memory Trick
 
Specific Forbidden Word?
↓
Word Filter
 
Email Address?
↓
PII Redaction
 
Sensitive Data?
↓
Information Masking
 
Offensive Content?
↓
Toxicity Filter
 
Amazon SageMaker Canvas
Why?
The key clue is:
"non-developer" and "no-code visual interface"
Why the Other Options Are Incorrect
Option	Why Not
Amazon SageMaker Canvas	✅ No-code ML for business users
Amazon SageMaker Autopilot	Automates model creation, but is primarily aimed at developers/data scientists and not a fully no-code business-user experience
Amazon SageMaker Studio	Integrated ML development environment requiring technical expertise
Amazon SageMaker JumpStart	Provides pretrained models and solutions, not a no-code model-building interface
 
Quick Cheat Sheet
Algorithm	Interpretable?	Classification?
✅ Decision Trees	High	Yes
Logistic Regression	Moderate	Yes
Neural Networks	Low	Yes
Linear Regression	Moderate	No (regression only)
Decision Trees are one of the most interpretable machine learning algorithms because you can directly trace how a prediction was made.
 
Requirement	Solution
Block specific business topics	✅ Guardrails Denied Topics
Block harmful content	✅ Guardrails Content Filters
Protect PII	✅ Sensitive Information Filters
Custom application logic	Lambda/Comprehend
 
Technique	Purpose
✅ Tensor Parallelism	Split tensor computations across GPUs
Pipeline Parallelism	Split layers across GPUs
Data Parallelism	Replicate model on multiple GPUs
Model Sharding	General term for splitting model weights
Memory Trick
 
LLM Too Large For One GPU
↓
Tensor Parallelism
 
8 GPUs
↓
tensor_parallel_degree = 8
 
Parameter	Purpose
Stop Sequences	Stops generation when a specified string appears.
Temperature	Controls randomness of token selection.
Top K	Limits selection to the K highest-probability tokens.
✅ Top P	Selects from the smallest set of tokens whose cumulative probability exceeds a threshold.
 
Parameter	Effect
Temperature	Randomness / creativity
Top P	Dynamic probability-based token selection
Top K	Fixed number of candidate tokens
Stop Sequences	Terminates generation
Max Tokens	Limits output length
 
Memory Trick
Cumulative Probability Threshold?
↓
Top P
 
Fixed Number of Tokens?
↓
Top K
 
Attach an identity-based policy to the ChatbotAppRole with a Condition block for bedrock:GuardrailIdentifier.
Why?
The requirement is:
The ChatbotAppRole must only be able to invoke a foundation model when a specific Amazon Bedrock Guardrail is applied.
 
 
 
IAM Guardrail Enforcement Cheat Sheet
Requirement	Best Solution
Require specific guardrail for one role	✅ IAM policy with bedrock:GuardrailIdentifier condition
Organization-wide restriction	SCP
UI convenience setting	Console configuration
Fine-grained least privilege	✅ Identity-based IAM policy
Memory Trick
 
Specific Role
+
Specific Guardrail
↓
IAM Condition
 
bedrock:GuardrailIdentifier
 
Option	Why Not
Increase Top K	Increases diversity of token selection; does not ensure short responses or a specific language.
Choose a different-sized LLM	Model size does not guarantee shorter outputs or a particular language.
Increase Temperature	Makes responses more creative and less deterministic; may reduce consistency.
Adjust the Prompt	✅ Directly controls language, length, format, and style.
 
 
Option	Purpose
✅ Explainability	Understanding why the AI made a prediction
Privacy	Protecting patient data and sensitive information
Sustainability	Reducing environmental impact and resource consumption
Fairness	Ensuring equitable treatment across different groups
 
Service	Purpose
Amazon Lex	Builds conversational chatbots and voice interfaces
Amazon Polly	✅ Converts text to natural-sounding speech
Amazon Transcribe	Converts speech to text
Amazon Translate	Translates text between languages
 
Memory Trick
 
Text → Speech
↓
Amazon Polly
 
Speech → Text
↓
Amazon Transcribe
 
Chatbot
↓
Amazon Lex
 
Language Translation
↓
Amazon Translate
 
Question Mentions	Answer
Semantic Search Quality	✅ Recall@K
Embedding Performance	✅ Recall@K / mAP
Vector Database Evaluation	✅ Recall@K / mAP
RAG Retrieval Evaluation	✅ Recall@K
Summarization Quality	✅ ROUGE
Translation Quality	✅ BLEU
Text Fluency	✅ Perplexity
Image Generation Quality	✅ FID
Image Classification	✅ Accuracy
 
Metric	Meaning
Recall@K	Are relevant documents in Top K?
Precision@K	How many retrieved docs are relevant?
mAP	Ranking quality
 
Metric	Use
Accuracy	Overall correctness
Precision	False positives matter
Recall	False negatives matter
F1 Score	Balance between Precision & Recall
 
Attribute	Example
Accuracy	Correct answers
Latency	Time to First Token (TTFT)
Cost	Price per request
Safety	Harmful output detection
Quality	Human evaluation
Hallucinations	Response faithfulness

