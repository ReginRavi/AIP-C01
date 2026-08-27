# AWS SAP-C02 Complete Services Reference & Incompatibility Guide

> **Target Exam**: AWS Certified Solutions Architect – Professional (SAP-C02)  
> **Purpose**: Definitive master lookup table listing all AWS services, core purpose, origin rationale, associated service integrations, and **critical incompatible service combinations / exam traps**.

---

## 1. Compute & Hybrid Infrastructure Services

| Service Name | What it is for? | Why it is there in the first place? | Related / Associated Services | Non-Related / Incompatible Services & Key Exam Traps |
| :--- | :--- | :--- | :--- | :--- |
| **Amazon EC2** | Scalable virtual servers in the cloud (IaaS). | Eliminates physical server hardware procurement and data center management. | EBS, VPC, Auto Scaling, ELB, IAM, CloudWatch. | ❌ Cannot automatically failover across Regions without multi-region deployment or Route 53 DNS. |
| **AWS Fargate** | Serverless compute engine for containers (ECS & EKS). | Removes the operational burden of provisioning, scaling, patching, and managing EC2 host instances. | Amazon ECS, Amazon EKS, AWS ECR, CloudWatch, ALB. | ❌ **NOT supported on AWS Outposts** (ECS/EKS on Outposts requires EC2 capacity). ❌ No direct SSH/OS access. |
| **Amazon ECS** | AWS-native container orchestration service. | Simple, zero-cost control plane for managing containerized applications on AWS. | AWS Fargate, EC2, ECR, ALB, Route 53, CloudWatch. | ❌ Does NOT support Kubernetes manifests/Helm natively without conversion. |
| **Amazon EKS** | Managed Kubernetes container orchestration service. | Allows running standard Kubernetes workloads on AWS with native CNCF tool compatibility. | AWS Fargate, EC2, ECR, Karpenter, Helm, ArgoCD. | ❌ Control plane is NOT free ($0.10/hr / $73/mo per cluster). |
| **AWS Lambda** | Event-driven serverless compute service. | Executes code in response to events without provisioning or managing servers. | API Gateway, EventBridge, SQS, SNS, S3, DynamoDB. | ❌ **15-minute max execution timeout** (cannot run long batch jobs). ❌ Cannot run custom OS kernels. |
| **AWS Outposts** | AWS physical hardware racks installed in customer data centers. | Delivers ultra-low latency (<10ms) local processing and on-premises data residency compliance. | EC2, EBS, S3 on Outposts, Direct Connect, VPC. | ❌ **AWS Fargate is NOT supported**. ❌ EKS Anywhere does NOT run on Outposts hardware. |
| **AWS Batch** | Managed batch processing for parallel/grid computing jobs. | Dynamically provisions compute resources (EC2/Fargate) based on volume and job queues. | AWS Fargate, EC2 Spot, SQS, S3, ECR. | ❌ Not designed for real-time web application request/response APIs. |
| **AWS App Runner** | Managed container application deployment service. | Fully managed deployment of web apps and APIs directly from source code or container image. | ECR, AWS Copilot, IAM, Route 53. | ❌ Does not allow low-level host tuning, custom networking plugins, or Kubernetes CRDs. |
| **AWS Wavelength** | Edge compute embedded in 5G telecommunication provider data centers. | Delivers single-digit millisecond latency to 5G mobile devices and end-users. | EC2, EBS, VPC Carrier Gateways, 5G Telco Networks. | ❌ Not for standard corporate office site-to-site VPNs or general public web hosting. |
| **AWS Local Zones** | Infrastructure deployment placed close to major population/industry centers. | Serves sub-10ms latency applications to local users without building regional data centers. | EC2, EBS, ALB, VPC. | ❌ Does not contain all AWS regional services (e.g. specialized ML hardware may be missing). |

---

## 2. Storage & Archival Services

| Service Name | What it is for? | Why it is there in the first place? | Related / Associated Services | Non-Related / Incompatible Services & Key Exam Traps |
| :--- | :--- | :--- | :--- | :--- |
| **Amazon S3** | High-durability (11 9s) object storage for files, media, and backups. | Provides unlimited, low-cost internet-accessible object storage via HTTP REST APIs. | CloudFront, IAM, KMS, Lambda, S3 Lifecycle, Athena. | ❌ **NOT block storage** (cannot mount directly as OS boot volume). ❌ Not POSIX compliant. |
| **Amazon EBS** | High-performance block storage volumes attached to single EC2 instances. | Serves persistent disk storage for databases and operating systems that survive instance reboot. | EC2, EBS Snapshots, Data Lifecycle Manager (DLM), KMS. | ❌ **Cannot be attached across multiple AZs** (Multi-Attach is single-AZ only). ❌ Not global storage. |
| **Amazon EFS** | Scalable, elastic NFS file system shared across multiple EC2 instances/Fargate. | Provides shared POSIX-compliant file storage accessible concurrently from Linux servers. | EC2, AWS Fargate, AWS Lambda, AWS DataSync, IAM. | ❌ **Linux ONLY** (Does NOT support Windows native SMB protocol). |
| **Amazon FSx for Windows** | Fully managed native Microsoft Windows file system (SMB protocol). | Provides Windows-compatible shared file storage backed by native Active Directory. | Windows EC2, AWS Directory Service, AWS DataSync. | ❌ Linux workloads requiring POSIX permissions should use EFS, not FSx for Windows. |
| **Amazon FSx for Lustre** | High-performance parallel file system for HPC, ML, and big data workloads. | Delivers sub-millisecond latency and hundreds of GB/s throughput for intensive compute tasks. | EC2, AWS Batch, S3, SageMaker. | ❌ High cost; NOT designed for long-term general-purpose cold file archiving. |
| **AWS Storage Gateway** | Hybrid cloud storage bridge (File, Volume, Tape Gateways). | Gives on-premises applications seamless access to AWS cloud storage with local caching. | Amazon S3, S3 Glacier, KMS, Direct Connect. | ❌ **File Gateway is NOT for bulk one-off data migrations** (Use AWS DataSync for migrations). |
| **AWS Snowball Edge** | Physical ruggedized appliance for offline bulk data migration (up to 80-100 TB). | Transports petabyte-scale data physically when network bandwidth is too slow/expensive. | Amazon S3, AWS SCT Extraction Agent, KMS. | ❌ **Not for continuous real-time CDC replication** (Use AWS DMS over network). |
| **AWS DataSync** | Automated network data transfer service for NFS, SMB, and S3 storage. | Accelerates bulk data migration and scheduled backups over network links. | Amazon S3, EFS, FSx, Storage Gateway. | ❌ **NOT for relational database transaction log replication** (Use AWS DMS for DBs). |

---

## 3. Databases & In-Memory Caching Services

| Service Name | What it is for? | Why it is there in the first place? | Related / Associated Services | Non-Related / Incompatible Services & Key Exam Traps |
| :--- | :--- | :--- | :--- | :--- |
| **Amazon RDS** | Managed relational database (MySQL, Postgres, MariaDB, Oracle, SQL Server). | Automates OS patching, DB backups, multi-AZ failover, and hardware management. | EC2, Secrets Manager, KMS, CloudWatch, Direct Connect. | ❌ **Multi-AZ Standby is PASSIVE** (Cannot be queried for read scaling; use Read Replicas). |
| **Amazon Aurora** | Cloud-native relational database (MySQL & PostgreSQL compatible). | Delivers up to 5x MySQL performance with storage auto-scaling up to 128 TiB. | Aurora Global Database, Aurora Serverless v2, Secrets Manager. | ❌ **Not multi-master across regions** (Aurora Global DB has 1 Primary Writer + Regional Readers). |
| **Amazon DynamoDB** | Fully managed serverless key-value NoSQL database. | Guarantees single-digit millisecond latency at any scale without server management. | DynamoDB Global Tables, DAX, DynamoDB Streams, Lambda. | ❌ **NOT for complex multi-table SQL joins or ACID OLAP analytics** (Use Redshift/RDS). |
| **Amazon ElastiCache** | In-memory key-value cache engine (Redis / Memcached). | Offloads read pressure from databases and reduces application response latency to sub-ms. | RDS, Aurora, DynamoDB, EC2, AWS Lambda. | ❌ **Memcached does NOT support multi-AZ failover or persistence** (Use Redis for HA/Persistence). |
| **Amazon Redshift** | Fully managed petabyte-scale columnar Data Warehouse (OLAP). | Executes complex analytical queries and aggregations across massive datasets. | S3, AWS Glue, QuickSight, DMS, EMR. | ❌ **NOT for high-frequency OLTP transactional writes** (Frequent small writes degrade performance). |
| **Amazon Neptune** | Fully managed graph database (Property Graph / RDF). | Queries complex networks of highly connected data (social graphs, fraud networks). | Lambda, EC2, S3, IAM. | ❌ Not for traditional tabular relational data or standard SQL queries. |
| **Amazon Timestream** | Serverless time-series database for IoT and operational metrics. | Efficiently stores and analyzes timestamped data streams with automated lifecycle tiering. | IoT Core, Kinesis, Grafana, Lambda. | ❌ Not for general-purpose key-value lookups or relational tables. |

---

## 4. Networking & Content Delivery Services

| Service Name | What it is for? | Why it is there in the first place? | Related / Associated Services | Non-Related / Incompatible Services & Key Exam Traps |
| :--- | :--- | :--- | :--- | :--- |
| **Amazon VPC** | Isolated virtual network environment in the AWS Cloud. | Gives complete logical isolation and control over virtual networking, IP subnets, and routing. | EC2, Subnets, Route Tables, Internet Gateways, NAT Gateways. | ❌ VPC subnets **CANNOT span multiple Availability Zones** (A subnet resides in 1 AZ). |
| **AWS Transit Gateway** | Centralized hub connecting multiple VPCs and on-premises networks. | Simplifies network topology by replacing thousands of complex VPC peering connections. | VPC Peering, Direct Connect Gateway, AWS Site-to-Site VPN. | ❌ **Does NOT support overlapping CIDR blocks** between attached VPCs. |
| **Amazon Route 53** | Highly available and scalable DNS and domain registration service. | Resolves domain names to IP addresses and routes global user traffic using intelligent routing. | Route 53 Resolver, S3, CloudFront, ALB, Direct Connect. | ❌ **Route 53 updates propagate in < 60 seconds** (Do NOT fall for 12-hour propagation traps). |
| **AWS Direct Connect** | Dedicated private physical network connection from on-premises to AWS. | Provides predictable network performance, lower latency, and reduced data egress costs. | Direct Connect Gateway, Private VIF, Public VIF, Transit Gateway. | ❌ **Public VIF CANNOT connect to Virtual Private Gateways (VGWs) or Direct Connect Gateways** (Requires Private VIF). |
| **Amazon CloudFront** | Global Content Delivery Network (CDN) edge distribution service. | Caches static/dynamic web content at global edge locations to minimize user latency. | S3, ALB, API Gateway, AWS WAF, Route 53, Shield. | ❌ CloudFront caches content globally; **it does NOT replace database replication**. |
| **AWS Global Accelerator** | Network service that routes traffic over AWS global backbone using static Anycast IPs. | Improves availability and performance for global users by bypassing public internet congestion. | ALB, NLB, EC2, Route 53. | ❌ **Does NOT cache HTTP content at edge** (CloudFront caches content; Global Accelerator routes TCP/UDP). |
| **AWS PrivateLink** | Private, secure connection from VPC to AWS services or 3rd-party SaaS without Internet. | Eliminates exposure of internal VPC traffic to the public internet using VPC Interface Endpoints. | Network Load Balancer (NLB), VPC, IAM. | ❌ Interface Endpoints require an NLB on the service provider side, **NOT an ALB**. |

---

## 5. Security, Identity & Governance Services

| Service Name | What it is for? | Why it is there in the first place? | Related / Associated Services | Non-Related / Incompatible Services & Key Exam Traps |
| :--- | :--- | :--- | :--- | :--- |
| **AWS IAM** | Identity and Access Management for AWS resources and permissions. | Controls WHO can access WHICH AWS resources under WHAT conditions (least-privilege). | IAM Roles, Policies, STS, IAM Identity Center. | ❌ **Do NOT use IAM User long-lived access keys** for EC2/Lambda (Use IAM Roles). |
| **AWS IAM Identity Center**| Centralized workforce Single Sign-On (SSO) and multi-account identity management. | Connects enterprise IdPs (Okta, Azure AD) via SAML/SCIM to manage access across AWS accounts. | AWS Organizations, SAML 2.0 IdPs, SCIM. | ❌ **Does NOT support OpenID Connect (OIDC)** for web apps (SAML 2.0 only). |
| **AWS KMS** | Managed service for creating and controlling cryptographic encryption keys. | Protects sensitive data at rest across AWS services using envelope encryption. | S3, EBS, RDS, Secrets Manager, CloudTrail. | ❌ **KMS Custom Key Stores (HSM) incur high hourly costs**; default KMS keys are managed free. |
| **AWS Secrets Manager** | Rotates, manages, and retrieves secrets (database credentials, API keys). | Eliminates hardcoded credentials in application code through automated KMS-encrypted rotation. | RDS, Lambda, KMS, EC2, ECS. | ❌ **Parameter Store is cheaper for static strings**; Secrets Manager is for automated rotation. |
| **Amazon GuardDuty** | Intelligent threat detection and continuous security monitoring service. | Analyzes VPC Flow Logs, CloudTrail, and DNS logs using ML to detect compromised resources. | Security Hub, EventBridge, CloudTrail, VPC Flow Logs. | ❌ **GuardDuty DOES NOT block threats automatically** (It alerts via EventBridge for remediation). |
| **AWS WAF** | Web Application Firewall protecting web applications from Layer 7 exploits. | Filters malicious HTTP/HTTPS payloads (SQL injection, XSS, rate limiting) at edge or ALB. | CloudFront, Application Load Balancer, API Gateway. | ❌ **WAF operates at Layer 7 (HTTP/S) ONLY**; does not block Layer 3/4 SYN floods (Use Shield). |
| **AWS Shield Advanced** | Managed DDoS protection service against large-scale volumetric attacks. | Provides 24/7 access to DDoS Response Team (DRT) and cost protection against DDoS scaling bills. | CloudFront, Route 53, ALB, AWS WAF. | ❌ **Shield Standard is FREE on all AWS services**; Shield Advanced requires a $3,000/mo commit. |
| **AWS Organizations** | Policy-based management service for consolidating multiple AWS accounts. | Centralizes billing, account creation, control policies (SCPs), and resource sharing across accounts. | SCPs, AWS RAM, AWS Control Tower, IAM Identity Center. | ❌ **SCPs do NOT grant permissions** (SCPs act as boundary guardrails; IAM role still needed). |
| **AWS Config** | Continuous resource configuration tracking and compliance evaluation service. | Audits infrastructure changes over time against security baselines and internal governance rules. | Config Rules, CloudTrail, Systems Manager. | ❌ **AWS Config tracks WHAT resource state changed**; CloudTrail logs WHO called the API. |

---

## 6. Analytics, Data Integration & Messaging Services

| Service Name | What it is for? | Why it is there in the first place? | Related / Associated Services | Non-Related / Incompatible Services & Key Exam Traps |
| :--- | :--- | :--- | :--- | :--- |
| **Amazon Kinesis Streams** | Real-time streaming data ingestion engine for large-scale data points. | Ingests and processes hundreds of thousands of data records per second with sub-second latency. | Kinesis Firehose, Lambda, Analytics, S3. | ❌ **Not for HTTP REST message queuing** (Use SQS for application decoupling). |
| **Amazon MSK** | Managed Streaming for Apache Kafka clusters. | Runs open-source Apache Kafka workloads natively on AWS without managing Kafka brokers. | EC2, Lambda, Glue Schema Registry. | ❌ **MSK is NOT optimized for low-latency key-value single-item lookups** (Use DynamoDB). |
| **AWS Glue** | Serverless data integration and ETL (Extract, Transform, Load) service. | Automatically discovers, catalogs, cleans, and transforms structured/unstructured data for analytics. | S3, Athena, Redshift, Glue Data Catalog. | ❌ **AWS Glue is NOT for converting database engine schemas/PL-SQL** (Use AWS SCT for DB schemas). |
| **Amazon Athena** | Serverless interactive query service that analyzes data in S3 using standard SQL. | Queries S3 data lakes directly without loading data into a database or data warehouse. | Amazon S3, AWS Glue Data Catalog, QuickSight. | ❌ **NOT an OLTP database engine**; Athena queries binary or text files in S3. |
| **Amazon SQS** | Fully managed message queuing service for decoupling application components. | Eliminates message loss and handles asynchronous communication between distributed services. | AWS Lambda, EC2 Auto Scaling, SNS, EventBridge. | ❌ **SQS FIFO queues cap throughput at 3,000 msgs/sec with batching** (Standard queues are unlimited). |
| **Amazon SNS** | Managed pub/sub notification service for system-to-system and system-to-user messaging. | Fans out messages instantly to multiple subscribers (SQS, Lambda, HTTP, Email, SMS). | Amazon SQS, AWS Lambda, EventBridge, CloudWatch. | ❌ **SNS does NOT persist messages** (If no subscriber receives the payload, it is lost unless DLQ configured). |
| **Amazon EventBridge** | Serverless event bus that routes events between AWS services and SaaS applications. | Simplifies event-driven architectures by decoupling producers and consumers using rules. | Lambda, Step Functions, SQS, CloudWatch. | ❌ **Not designed for streaming high-frequency IoT video feeds** (Use Kinesis Video Streams). |
| **AWS Step Functions** | Serverless visual workflow orchestrator for complex multi-step application state machines. | Manages state, retries, and error handling for multi-step Lambda microservices. | AWS Lambda, Fargate, SQS, SNS, DynamoDB. | ❌ **Standard Workflows have execution limits**; Express Workflows are for high-volume short tasks. |

---

## 7. Migration, Modernization & Management Services

| Service Name | What it is for? | Why it is there in the first place? | Related / Associated Services | Non-Related / Incompatible Services & Key Exam Traps |
| :--- | :--- | :--- | :--- | :--- |
| **AWS MGN** | Automated block-level server rehosting (lift-and-shift) migration service. | Replicates physical, virtual, or cloud servers directly into EC2 instances with minimal downtime. | EC2, EBS, AWS Migration Hub. | ❌ **Cannot migrate databases into managed Amazon RDS/Aurora engines** (Use AWS DMS). |
| **AWS DMS** | Relational and NoSQL database migration service with continuous CDC replication. | Migrates database records with minimal cutover downtime between homogeneous/heterogeneous databases. | AWS SCT, RDS, Aurora, Redshift, S3. | ❌ **DMS does NOT rewrite database DDL schemas or stored procedures** (Use AWS SCT first). |
| **AWS SCT** | Converts database DDL schemas, PL/SQL code, and views between different engines. | Translates proprietary database code (Oracle/SQL Server) into open-source target dialects (Postgres/MySQL). | AWS DMS, AWS Snowball Edge, Redshift. | ❌ **SCT does NOT migrate data records**; SCT converts database structure/code only. |
| **AWS Transfer Family** | Managed SFTP, FTPS, FTP, and AS2 endpoints for file transfers directly into S3/EFS. | Enables business partner B2B file transfer compatibility without running SFTP EC2 instances. | Amazon S3, Amazon EFS, AWS KMS, IAM. | ❌ **NOT for automated storage migration** (Use AWS DataSync for storage sync). |
| **AWS Systems Manager** | Centralized operational management hub for fleet configuration and automation. | Automates OS patching, remote shell access (Session Manager), and runbook execution without SSH. | EC2, CloudWatch, AWS Config, IAM. | ❌ **SSM Agent does NOT stream OS memory/disk metrics to CloudWatch** (Use CloudWatch Agent). |
| **AWS CloudFormation** | Infrastructure as Code (IaC) service for modeling and provisioning AWS resources via YAML/JSON. | Automates repeatable, auditable infrastructure provisioning across accounts and regions. | CloudFormation Stacks, StackSets, Change Sets. | ❌ **`DeletionPolicy: Snapshot` is NOT supported on Amazon S3 buckets** (`Retain` only). |

---

## 8. Machine Learning & Specialized AI Services

| Service Name | What it is for? | Why it is there in the first place? | Related / Associated Services | Non-Related / Incompatible Services & Key Exam Traps |
| :--- | :--- | :--- | :--- | :--- |
| **Amazon Rekognition** | Image and video analysis service using deep learning (facial recognition, object detection). | Automates image tagging, celebrity recognition, and content moderation in media workflows. | S3, AWS Lambda, Kinesis Video Streams. | ❌ **CANNOT query objects stored in Amazon S3 Glacier directly** in real time! |
| **Amazon Textract** | ML document processing service that extracts text, forms, and tables from scanned documents. | Automates extraction of structured data from PDFs, images, and newsprint beyond basic OCR. | S3, OpenSearch, Lambda, Step Functions. | ❌ **Amazon Rekognition is NOT for document OCR** (Use Textract for scanned text/forms). |
| **Amazon Lex** | Conversational AI service for building voice and text chatbots (ASR + NLU). | Provides Automatic Speech Recognition (ASR) and Natural Language Understanding (NLU) for IVR/bots. | Amazon Connect, AWS Lambda, Polly. | ❌ **Amazon Polly does NOT recognize incoming user speech** (Polly is Text-to-Speech only). |
| **Amazon Polly** | Text-to-Speech (TTS) service that turns written text into lifelike spoken audio. | Synthesizes written text into multi-lingual audio output for mobile applications and screen readers. | Amazon Lex, Amazon Connect, S3. | ❌ Cannot convert spoken audio input to text or recognize user intents. |
| **Amazon Comprehend** | Natural Language Processing (NLP) text analytics service for extracting sentiment and entities. | Analyzes customer feedback, emails, and documents to identify key phrases, sentiment, and PII. | S3, Glue, Lambda, OpenSearch. | ❌ Does not process live telephone speech directly without an ASR engine like Lex/Transcribe. |

---

## 9. Final SAP-C02 Incompatibility & Trap Rule Summary

1. **AWS Fargate** $\longrightarrow$ ❌ **NOT supported on AWS Outposts** (ECS/EKS on Outposts requires EC2 capacity).
2. **Public VIF (Direct Connect)** $\longrightarrow$ ❌ **CANNOT attach to Virtual Private Gateways (VGWs) or Direct Connect Gateways** (Requires Private VIF).
3. **Amazon Rekognition** $\longrightarrow$ ❌ **CANNOT query objects in S3 Glacier/Glacier Deep Archive directly** (Requires restoring to S3 Standard first).
4. **CloudFormation `DeletionPolicy: Snapshot`** $\longrightarrow$ ❌ **NOT supported on S3 Buckets** (Only `Retain` or `Delete` allowed for `AWS::S3::Bucket`).
5. **SSM Agent** $\longrightarrow$ ❌ **DOES NOT stream OS memory or disk utilization metrics** (Requires installing the **Unified CloudWatch Agent**).
6. **AWS DataSync** $\longrightarrow$ ❌ **NOT for continuous relational database replication** (Use **AWS DMS** for relational DBs).
7. **AWS SCT** $\longrightarrow$ ❌ **NOT for migrating database data records** (SCT converts DDL schema/code; **AWS DMS** migrates data).
