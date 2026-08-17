### 1. Foundation Models & GenAI (Amazon Bedrock)

- **[[Amazon BedRock]]:** The fully managed serverless service providing access to industry-leading foundation models (FMs) via unified APIs.

- **Amazon Bedrock AgentCore:** The advanced platform and SDK for building, securing, and operating autonomous agents with managed memory, policies, and tool integration.

- **Amazon Bedrock Knowledge Bases:** Fully managed infrastructure for Retrieval-Augmented Generation (RAG), connecting FMs securely to internal enterprise data sources.

- **Amazon Bedrock Prompt Management & Prompt Flows:** Tools designed to store, version, optimize, and orchestrate complex prompt workflows.

- **Amazon Titan:** AWS's native family of high-performing foundation models optimized for text, multimodal tasks, and embeddings.


### 2. The SageMaker Suite & MLOps

- **Amazon SageMaker AI:** The core managed platform for building, training, and deploying classical ML and deep learning models at scale.

- **Amazon SageMaker Unified Studio:** A unified environment combining analytics, EMR, Glue, Athena, Bedrock, and SageMaker tools into a single collaborative workspace.

- **Amazon SageMaker JumpStart:** A hub providing pre-trained open-source models, built-in algorithms, and solution templates for rapid prototyping.

- **Data & Prep:** **Amazon SageMaker Data Wrangler** (for data prep and feature engineering) and **Amazon SageMaker Ground Truth** (for managing data labeling workflows).

- **Governance & Operations:** **Amazon SageMaker Clarify** (for bias detection and model explainability), **Amazon SageMaker Model Monitor** (for tracking drift), **Amazon SageMaker Model Registry** (for model versioning), **Amazon SageMaker Processing** (for distributed data jobs), and **Amazon SageMaker Neo** (for compiling models to run efficiently on edge devices or hardware accelerators).


### 3. Specialized AI Capabilities

- **Amazon Comprehend:** Natural language processing service for sentiment analysis, entity extraction, and PII redaction.

- **Amazon Kendra:** Intelligent enterprise search service powered by machine learning for accurate document retrieval.
-
- **Amazon Lex:** Conversational AI service for building custom chatbots and voice interfaces using NLU.

- **Amazon Rekognition:** Computer vision service for image and video analysis, facial recognition, and moderation.

- **Amazon Textract:** Optical character recognition (OCR) that extracts text, tables, and structured data from scanned documents.

- **Amazon Transcribe:** Automatic speech recognition (ASR) to convert speech-to-text with high accuracy.

- **Amazon Augmented AI (A2I):** A service that makes it easy to build human review workflows for model predictions that require human validation.


### 4. Intelligent Assistants & Productivity (Amazon Q & Quick)

- **Amazon Q Business & Business Apps:** Generative AI assistant that allows employees to securely chat with enterprise data, search documents, and take actions across business applications.

- **Amazon Q Developer:** Generative AI-powered assistant for software development inside IDEs (like VS Code) to accelerate coding, testing, and debugging.

- **Amazon Quick (QuickSuite):** An AI-powered business intelligence and agentic analytics platform integrating visualization, workflow automation, and natural language insights.

### 1. Amazon Augmented AI (Amazon A2I)

- **Benefits:** Makes it easy to build human-in-the-loop (HITL) review workflows for machine learning predictions.

- **When to Use (AIP-C01 Triggers):** Look for _"human review,"_ _"low-confidence predictions,"_ or _"human-in-the-loop validation."_

- **Cost:** Pay per human review task routed through the service.

- **Usecase:** Automatically routing a scanned ID to a human reviewer if Amazon Rekognition's confidence score for matching the face falls below 85%.


### 2. Amazon Bedrock

- **Benefits:** A fully managed, serverless API service providing access to leading foundation models (FMs) from multiple providers without managing infrastructure.
 
- **When to Use (AIP-C01 Triggers):** Look for _"Generative AI,"_ _"Foundation Models,"_ _"serverless LLM,"_ or _"text/image generation without managing servers."_

- **Cost:** Pay-as-you-go based on the volume of input and output tokens processed.

- **Usecase:** Integrating Anthropic Claude into a customer service portal to instantly summarize long email threads.


### 3. Amazon Bedrock AgentCore

- **Benefits:** A structured runtime and SDK designed for building, securing, and operating autonomous generative AI agents that can take actions.
 
- **When to Use (AIP-C01 Triggers):** Look for _"autonomous AI agents,"_ _"multi-step AI workflows,"_ _"AI taking action on APIs,"_ or _"agentic logic."_
 
- **Cost:** Usage-based pricing on model inference tokens, orchestration tokens, and tool execution (like Lambda).

- **Usecase:** Deploying an autonomous financial advisor agent that can fetch current stock prices and execute trades via internal APIs on behalf of a user.


### 4. Amazon Bedrock Knowledge Bases

- **Benefits:** Fully managed infrastructure for Retrieval-Augmented Generation (RAG). It automatically connects FMs to your data and manages the vector embeddings.

- **When to Use (AIP-C01 Triggers):** Look for _"RAG,"_ _"grounding models in enterprise data,"_ _"vector database integration,"_ or _"reduce hallucinations with internal docs."_

- **Cost:** Pay for the vector database storage (e.g., OpenSearch) and the tokens used by the embedding model and the text generation model.

- **Usecase:** Pointing Bedrock to an S3 bucket of your company's HR policies so an AI chatbot can answer employee questions accurately based only on company rules.


### 5. Amazon Bedrock Prompt Management

- **Benefits:** A centralized tool to <font color="#00b050">create, test, version, and deploy prompts,</font> decoupling prompt engineering from application code.

- **When to Use (AIP-C01 Triggers):** Look for _"versioning prompts,"_ _"manage prompt lifecycle,"_ or _"decouple prompts from code base."_

- **Cost:** Included in standard Bedrock token pricing; you pay for the model inference during testing/usage.

- **Usecase:** Maintaining different versions of a clinical trial extraction prompt and safely rolling out a new, optimized prompt without redeploying the backend application.


### 6. Amazon Bedrock Prompt Flows

- **Benefits:** <font color="#00b050">A visual, drag-and-drop builder</font> interface to <font color="#00b050">chain together multiple</font> foundation models, prompts, and AWS services into complex generative AI workflows.

- **When to Use (AIP-C01 Triggers):** Look for _"visual AI builder,"_ _"chaining prompts,"_ _"no-code generative AI workflow,"_ or _"link multiple FMs."
- **Cost:** Pay for the underlying Bedrock model tokens and any invoked AWS services (like Lambda or S3) during the flow execution.

- **Usecase:** Visually designing a flow that first uses Amazon Textract to read a document, passes the text to Claude to classify it, and then saves the output to S3.


### 7. Amazon Comprehend - (classification)

- **Benefits:** Fully managed <font color="#00b050">Natural Language Processing (NLP) </font>to extract insights, sentiment, and entities from unstructured text.

- **When to Use (AIP-C01 Triggers):** Look for _"sentiment analysis,"_ _"extract key phrases,"_ _"PII redaction in text,"_or _"topic modeling

- **Cost:** Pay per 100 characters of text processed.

- **Usecase:** Analyzing thousands of product reviews to determine if the overall customer sentiment is positive, negative, or mixed.
   
### 8. Amazon Kendra

- **Benefits:** A highly accurate, ML-powered <font color="#00b050">enterprise search service </font>that understands natural language questions and searches across disparate internal data silos.

- **When to Use (AIP-C01 Triggers):** Look for _"enterprise search,"_ _"semantic search,"_ _"natural language query on documents,"_ or _"unify internal data silos."_

- **Cost:** Billed per hour for the Kendra index (provisioned capacity) and storage used.

- **Usecase:** Creating a unified search bar for a corporate intranet that can pull exact answers from a mix of SharePoint, S3 files, and Salesforce data.


### 9. Amazon Lex

- **Benefits:** Provides the advanced deep learning functionalities of <font color="#00b050">automatic speech recognition</font> (ASR) and natural language understanding (NLU) to build conversational interfaces (chatbots).

- **When to Use (AIP-C01 Triggers):** Look for _"build a chatbot,"_ _"conversational voice/text interface,"_ or _"intent recognition."_

- **Cost:** Pay per text or speech request processed by the bot.

- **Usecase:** Building an automated customer service chatbot on a website that can understand when a user wants to "book a flight" or "check account balance."


### 10. Amazon Q Business

- **Benefits:** A fully managed, <font color="#00b050">generative AI-powered assistant </font>designed specifically for enterprise employees to ask questions, generate content, and complete tasks based on company data.

- **When to Use (AIP-C01 Triggers):** Look for _"internal AI assistant,"_ _"chat with enterprise data,"_ _"employee productivity,"_ or _"secure generative AI for workforce."_

- **Cost:** Billed on a per-user, per-month subscription model.

- **Usecase:** An employee asks Amazon Q, "What is our standard protocol for processing refunds?" and Q searches internal documentation to provide a cited answer.


### 11. Amazon Q Business Apps (Q Apps)

- **Benefits:** Allows any employee to instantly transform a conversation with Amazon Q Business into a reusable, purpose-built generative AI application with a single click, without writing code.

- **When to Use (AIP-C01 Triggers):** Look for _"no-code AI app creation,"_ _"shareable AI tools for employees,"_ or _"turn conversations into apps."_

- **Cost:** Included as part of the Amazon Q Business Pro subscription tier.

- **Usecase:** An HR manager uses a chat to draft a specific onboarding plan, then clicks "Create Q App" to share this specialized generator tool with the rest of the HR team.


### 12. Amazon Q Developer

- **Benefits:** A generative AI assistant integrated directly into developer IDEs (like VS Code) and the AWS console to help write, debug, and explain code.

- **When to Use (AIP-C01 Triggers):** Look for _"AI coding assistant,"_ _"generate code in IDE,"_ _"explain legacy code,"_ or _"troubleshoot AWS errors."_

- **Cost:** Free tier available; Pro tier is billed per user, per month.

- **Usecase:** A developer highlights a block of complex Python code in Visual Studio Code and asks Q Developer to explain what it does and suggest performance optimizations.


### 13. Amazon QuickSight (Q / ML Features)

- **Benefits:** Serverless Business Intelligence (BI) with built-in ML capabilities (like forecasting, anomaly detection, and natural language querying via QuickSight Q).

- **When to Use (AIP-C01 Triggers):** Look for _"dashboards,"_ _"visualize data,"_ or _"ask questions about data in natural language."_

- **Cost:** Pay per user (Authors have a fixed monthly fee, Readers have pay-per-session pricing).

- **Usecase:** A sales executive types, "Show me revenue for Q3 in California" into a dashboard, and QuickSight Q automatically builds the graph.


### 14. Amazon Rekognition

- **Benefits:** Deep learning-based computer vision service to <font color="#00b050">analyze images and video without needing ML expertise.</font>

- **When to Use (AIP-C01 Triggers):** Look for _"image analysis,"_ _"facial recognition,"_ _"content moderation in images/video,"_ or _"detect PPE (Personal Protective Equipment)."_

- **Cost:** Pay per image processed or per minute of video analyzed.

- **Usecase:** Automatically scanning user-uploaded profile pictures to block explicit or inappropriate content before it goes live on an app.


### 15. Amazon SageMaker AI (Core)

- **Benefits:** The flagship, fully managed service for data scientists and developers to build, train, and deploy machine learning models at scale.

- **When to Use (AIP-C01 Triggers):** Look for _"build custom models,"_ _"train deep learning models,"_ _"managed ML infrastructure,"_ or _"deploy ML endpoints."_

- **Cost:** Billed by the second for the specific EC2 instance types used during training and hosting.

- **Usecase:** Training a highly customized fraud detection algorithm using PyTorch on proprietary historical banking data.


### 16. Amazon SageMaker Clarify

- **Benefits:** Provides tools to <font color="#00b050">detect bias in ML</font> models and understand <font color="#00b050">model predictions</font> (explainability).

- **When to Use (AIP-C01 Triggers):** Look for _"model explainability,"_ _"detect bias,"_ _"feature importance,"_ or _"fairness metrics."_

- **Cost:** Billed for the underlying SageMaker Processing instances used to run the Clarify jobs.

- **Usecase:** Running a report to ensure a loan approval model is not making biased decisions based on applicant age or gender.


### 17. Amazon SageMaker Data Wrangler

- **Benefits:** Simplifies the process of <font color="#00b050">data preparation and feature engineering </font>via a <font color="#00b050">visual interface, reducing the time it takes to clean data for ML.</font>

- **When to Use (AIP-C01 Triggers):** Look for _"visual data preparation,"_ _"feature engineering without code,"_ or _"clean ML data."_

- **Cost:** Billed for the EC2 instances used while running the visual interface and processing the data.

- **Usecase:** A data scientist visually identifies missing values and outliers in a CSV file and applies one-hot encoding transformations before training.

### 18. Amazon SageMaker Ground Truth

- **Benefits:** A fully managed <font color="#00b050">data labeling service </font>that makes it easy to build highly accurate training datasets using human labelers, vendors, or mechanical turk.
    
- **When to Use (AIP-C01 Triggers):** Look for _"data labeling,"_ _"create training datasets,"_ or _"annotate images/text."_
    
- **Cost:** Pay per object labeled (pricing varies based on whether you use internal teams or paid crowdsourcing).
    
- **Usecase:** Sending 10,000 images of traffic lights to a labeling workforce to draw bounding boxes around the lights to train an autonomous driving model.
    

### 19. Amazon SageMaker JumpStart

- **Benefits:** A <font color="#00b050">machine learning hub </font>providing pre-trained, open-source foundation models, built-in algorithms, and end-to-end solution templates.

- **When to Use (AIP-C01 Triggers):** Look for _"deploy open-source models,"_ _"pre-built ML solutions,"_ or _"one-click ML deployment."_

- **Cost:** You do not pay for JumpStart itself, but you pay for the SageMaker EC2 instances required to host or fine-tune the models you select.

- **Usecase:** Rapidly deploying an open-source Meta Llama model into a private VPC environment for a secure text generation proof-of-concept.


### 20. Amazon SageMaker Model Monitor

- **Benefits:** Continuously <font color="#00b050">monitors the quality of ML models in production,</font> <font color="#00b050">detecting data drift and alerting you when deviations occur.</font>

- **When to Use (AIP-C01 Triggers):** Look for _"data drift,"_ _"concept drift,"_ _"monitor production models,"_ or _"track model accuracy over time."_

- **Cost:** Billed for the SageMaker instances that run the scheduled monitoring jobs.

- **Usecase:** Setting up an alert that triggers if the statistical distribution of housing prices submitted to an ML model suddenly changes compared to the baseline data it was trained on.


### 21. Amazon SageMaker Model Registry

- **Benefits:** A <font color="#00b050">central repository</font> to catalog ML models, manage model versions, and track the approval status of models before they go into production.

- **When to Use (AIP-C01 Triggers):** Look for _"model versioning,"_ _"MLOps catalog,"_ _"track model lineage,"_ or _"approval workflows for models."_

- **Cost:** Free to use; you only pay for the associated S3 storage of the model artifacts.

- **Usecase:** A data science lead reviews the accuracy metrics of "Version 2.0" of a recommendation model in the registry and clicks "Approve," which triggers an automated deployment pipeline.


### 22. Amazon SageMaker Neo

- **Benefits:** A<font color="#00b050">utomatically compiles and optimizes ML models to run efficiently on specific edge devices and hardware accelerators.</font>

- **When to Use (AIP-C01 Triggers):** Look for _"optimize for edge devices,"_ _"compile models for specific hardware,"_ or _"reduce model footprint."_

- **Cost:** The compilation service is free; you pay for the instances used if you host the model in the cloud, or nothing if deployed to your own edge device.

 **Usecase:** Compiling an object detection deep learning model so that it runs fast and uses minimal memory on a small Raspberry Pi camera on a factory floor.


### 23. Amazon SageMaker Processing

- **Benefits:** A managed environment <font color="#00b050">to run massive, distributed data processing</font>, data evaluation, and feature engineering jobs.

- **When to Use (AIP-C01 Triggers):** Look for _"run data processing scripts,"_ _"evaluate models at scale,"_ or _"heavy feature engineering."_

- **Cost:** Billed by the second for the EC2 instances used during the duration of the processing job.

- **Usecase:** Spinning up a cluster of 10 temporary instances to run a heavy Apache Spark job that cleans 500GB of log data, and automatically shutting them down when finished.


### 24. Amazon SageMaker Unified Studio

- **Benefits:** <font color="#00b050">A single, collaborative development environment that integrates analytics, data engineering, and AI tools (EMR, Glue, Bedrock, SageMaker) into one unified workspace</font>.

- **When to Use (AIP-C01 Triggers):** Look for _"unified AI and data environment,"_ _"single workspace for data engineers and data scientists,"_ or _"discover and query cross-service data assets."_

- **Cost:** Standard pricing applies to the underlying AWS services (EMR, Bedrock, etc.) provisioned through the studio.

- **Usecase:** A team collaborates in one interface where a data engineer uses built-in SQL tools to prepare data, and a data scientist seamlessly uses that same data to train a model without switching platforms.


### 25. Amazon Textract

- **Benefits:** ML service that automatically extracts text, handwriting, and structured data (tables, forms) from scanned documents.

- **When to Use (AIP-C01 Triggers):** Look for _"extract text from PDFs/images,"_ _"read form data (key-value pairs),"_ or _"extract tables."_

- **Cost:** Pay per page processed (costs vary depending on whether you are extracting plain text, tables, or specialized IDs/invoices).

- **Usecase:** Scanning thousands of paper medical intake forms and automatically extracting patient names, dates, and check-box responses into a database.


### 26. Amazon Titan

- **Benefits:** A family of highly capable, pre-trained foundation models <font color="#00b050">built exclusively by AWS,</font> designed for text generation, embeddings, and multimodal tasks.

- **When to Use (AIP-C01 Triggers):** Look for _"AWS native foundation models,"_ _"Amazon's own LLM,"_ or _"text embeddings."_

- **Cost:** Pay-as-you-go based on input/output tokens via Amazon Bedrock.

- **Usecase:** Using the Amazon Titan Text Embeddings model to convert a massive catalog of PDF documents into mathematical vectors for a semantic search engine.


### 27. Amazon Transcribe

- **Benefits:** Fully managed automatic speech recognition (ASR) service that makes it easy to add <font color="#00b050">speech-to-text </font>capabilities to applications.

- **When to Use (AIP-C01 Triggers):** Look for _"speech-to-text,"_ _"transcribe audio files,"_ or _"generate subtitles for video."_

- **Cost:** Pay per second of audio transcribed (billed monthly).

- **Usecase:** Automatically generating text transcripts of recorded customer service phone calls so that they can be analyzed for sentiment by Amazon Comprehend.