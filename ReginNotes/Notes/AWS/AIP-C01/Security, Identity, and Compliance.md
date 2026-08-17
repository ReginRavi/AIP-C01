These services form the **trust and security layer**. They ensure that sensitive data used for fine-tuning or RAG isn't leaked, that only authorized users or AI agents can access specific resources, and that your AI endpoints are protected from malicious attacks.

### 1. Amazon Cognito

- **Benefits:** A fully managed customer identity and access management (CIAM) service. It allows you to quickly add user sign-up, sign-in, and access control to your web and mobile apps, scaling to millions of users. It supports federated sign-in with social identity providers or enterprise SAML solutions.
    
- **When to Use (AIP-C01 Triggers):** Look for _"authenticate end users,"_ _"web/mobile app login,"_ _"social identity provider,"_ or _"exchange user tokens for temporary AWS credentials."_
    
- **Cost:** Pay based on the number of Monthly Active Users (MAUs).
    
- **Usecase:** Building a public-facing generative AI image creation web app and needing a secure way for users to register, log in, and securely invoke an Amazon API Gateway endpoint that triggers Amazon Bedrock.
    

### 2. AWS Encryption SDK

- **Benefits:** A client-side encryption library that helps developers easily encrypt and decrypt data _before_ it is sent to AWS or stored in a database.
    
- **When to Use (AIP-C01 Triggers):** Look for _"client-side encryption,"_ _"encrypt data before transit,"_ or _"encrypting data on the application server."_
    
- **Cost:** The SDK itself is free (open-source), but you pay for the underlying key provider requests (e.g., AWS KMS API calls) used to generate the data keys.
    
- **Usecase:** An on-premise application processing highly sensitive medical records must encrypt the text locally using the AWS Encryption SDK _before_ sending it over the internet to Amazon Bedrock for summarization.
    

### 3. IAM (AWS Identity and Access Management)

- **Benefits:** The fundamental AWS service for securely controlling access to AWS resources. It defines "who" can do "what" in your AWS environment.
    
- **When to Use (AIP-C01 Triggers):** Look for _"least privilege,"_ _"execution roles,"_ _"resource-based policies,"_ or _"control access to specific Bedrock foundation models."_
    
- **Cost:** Free.
    
- **Usecase:** Creating a strict IAM Execution Role for an Amazon Bedrock Agent so that it is explicitly authorized to read data from a specific internal S3 bucket, but denied access to delete files or modify model settings.
    

### 4. IAM Access Analyzer

- **Benefits:** An auditing tool that uses logic-based reasoning to analyze resource policies (like S3 bucket policies or KMS key policies) to determine which resources can be accessed publicly or by external accounts.
    
- **When to Use (AIP-C01 Triggers):** Look for _"audit permissions,"_ _"detect unintended public access,"_ _"cross-account access analysis,"_ or _"ensure training data is not public."_
    
- **Cost:** Free for resource access analysis; pay per IAM role/user analyzed for the "unused access" feature.
    
- **Usecase:** Automatically scanning the S3 bucket that holds your company's proprietary LLM fine-tuning data to mathematically verify that no resource policies have accidentally made the bucket accessible to the public internet.
    

### 5. IAM Identity Center (formerly AWS SSO)

- **Benefits:** The recommended service for centrally managing workforce access to multiple AWS accounts and business applications.
    
- **When to Use (AIP-C01 Triggers):** Look for _"workforce access,"_ _"internal corporate directory,"_ _"Single Sign-On (SSO),"_ or _"Active Directory integration."_
    
- **Cost:** Free.
    
- **Usecase:** Allowing your enterprise's internal data science team to log into Amazon SageMaker Unified Studio or Amazon Q Business using their existing corporate Microsoft Active Directory credentials without creating separate IAM users.
    

### 6. AWS KMS (Key Management Service)

- **Benefits:** A fully managed service to create, rotate, and control cryptographic keys used to encrypt data **at rest**(server-side encryption).
    
- **When to Use (AIP-C01 Triggers):** Look for _"data at rest encryption,"_ _"Customer Managed Keys (CMKs),"__"cryptographic control,"_ or _"encrypting S3 data/SageMaker models."_
    
- **Cost:** Fixed monthly fee per key, plus a per-request fee for cryptographic operations.
    
- **Usecase:** Enforcing compliance by using a Customer Managed Key in AWS KMS to encrypt the OpenSearch vector database containing sensitive embeddings for your RAG architecture.
    

### 7. Amazon Macie

- **Benefits:** A data security service that uses machine learning and pattern matching to discover and protect sensitive data (like Personally Identifiable Information - PII) stored in Amazon S3.
    
- **When to Use (AIP-C01 Triggers):** Look for _"discover PII in S3,"_ _"data loss prevention,"_ _"scan S3 for sensitive data,"_ or _"prepare clean data for ML."_
    
- **Cost:** Pay for the number of S3 buckets evaluated for inventory, and pay per GB of data explicitly scanned for sensitive data.
    
- **Usecase:** Scanning a massive S3 data lake of historical customer support transcripts to identify and remove social security numbers and credit cards _before_ that data is synced to an Amazon Bedrock Knowledge Base.
    

### 8. AWS Secrets Manager

- **Benefits:** A service to securely store, manage, retrieve, and automatically rotate database credentials, API keys, and other secrets. It eliminates the need to hardcode sensitive information in plain text within your application code.
    
- **When to Use (AIP-C01 Triggers):** Look for _"store third-party API keys,"_ _"rotate credentials automatically,"_ or _"securely retrieve database passwords at runtime."_
    
- **Cost:** Pay a fixed monthly fee per secret stored, plus a fee per 10,000 API calls to retrieve the secret.
    
- **Usecase:** Storing a specialized third-party API key (e.g., a real-time weather data provider) that an Amazon Bedrock Agent (AgentCore) needs to securely retrieve via AWS Lambda at runtime to execute an action.
    

### 9. AWS WAF (Web Application Firewall)

- **Benefits:** Protects web applications and APIs against common web exploits, bots, and excessive traffic that may affect availability, compromise security, or consume excessive resources. You can apply rate limits to specific action categories to control traffic and detect high-frequency automated attempts.
    
- **When to Use (AIP-C01 Triggers):** Look for _"block malicious IPs,"_ _"rate limiting,"_ _"protect API Gateway/AppSync endpoints,"_ or _"prevent excessive GenAI inference costs from bots."_
    
- **Cost:** Pay a monthly fee per web ACL, per security rule created, and per million requests inspected.
    
- **Usecase:** Placing AWS WAF in front of your Generative AI chatbot's API Gateway to implement rate-limiting. This prevents a malicious script from spamming your LLM endpoint, which would otherwise drive up your Amazon Bedrock token inference costs exponentially.