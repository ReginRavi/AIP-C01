Yes. For SAP-C02, I would build your study sheet around one question:

Service → Why AWS created it → Problem solved → Exam keywords

Below is the compact recognition sheet. I have grouped closely related services so you learn the architectural decision rather than memorize isolated definitions.

ANALYTICS

Amazon Athena
Why exists: Query data directly in S3 without running a database.
Keywords: serverless SQL, S3 data, ad hoc queries, no infrastructure, pay per query.

AWS Data Exchange
Why exists: Find, subscribe to, and consume third-party datasets.
Keywords: third-party data, data subscription, external datasets, data marketplace.

Amazon Data Firehose
Why exists: Deliver streaming data into destinations with minimal operational work.
Keywords: near-real-time delivery, streaming ingestion, S3, Redshift, OpenSearch, managed delivery, buffering.

Amazon EMR
Why exists: Run big-data frameworks such as Spark and Hadoop at scale.
Keywords: Spark, Hadoop, big data, distributed processing, cluster, batch analytics.

AWS Glue
Why exists: Serverless data integration and ETL.
Keywords: ETL, serverless, data catalog, crawlers, schema discovery, data lake, transformation.

Amazon Kinesis Data Streams
Why exists: Ingest and process real-time streaming data.
Keywords: real-time, streaming, shards, producers, consumers, replay, high-throughput streams.

AWS Lake Formation
Why exists: Centrally govern and secure data lakes.
Keywords: data lake, centralized permissions, fine-grained access, S3, Glue Catalog, governance.

Amazon Managed Service for Apache Flink
Why exists: Process streaming data using Apache Flink without managing clusters.
Keywords: stream processing, Apache Flink, real-time analytics, stateful processing.

Amazon MSK
Why exists: Managed Apache Kafka.
Keywords: Kafka, Kafka-compatible, streaming, producers/consumers, partitions, brokers, managed Kafka.

Amazon OpenSearch Service
Why exists: Search, log analytics, and near-real-time analytics.
Keywords: full-text search, logs, dashboards, indexing, search engine, log analytics.

Amazon QuickSight
Why exists: Business intelligence and dashboards.
Keywords: BI, dashboards, visualization, reports, business analytics.

APPLICATION INTEGRATION

Amazon AppFlow
Why exists: Transfer data between SaaS applications and AWS services.
Keywords: SaaS integration, Salesforce, data transfer, no-code/low-code, ETL.

AWS AppSync
Why exists: Managed GraphQL API service.
Keywords: GraphQL, API, real-time data, subscriptions, mobile/web applications.

Amazon EventBridge
Why exists: Route events between producers and targets.
Keywords: event-driven, event bus, event pattern, content filtering, AWS events, SaaS events, custom events.

Amazon MQ
Why exists: Managed traditional message brokers for applications that need broker compatibility.
Keywords: ActiveMQ, RabbitMQ, JMS, AMQP, MQTT, STOMP, migration from existing brokers.

Amazon SNS
Why exists: One-to-many pub/sub messaging.
Keywords: fan-out, topic, notification, pub/sub, multiple subscribers.

Amazon SQS
Why exists: Decouple components and buffer asynchronous work.
Keywords: queue, asynchronous, buffer, worker, decoupling, DLQ, FIFO, retry.

AWS Step Functions
Why exists: Orchestrate multi-step workflows.
Keywords: state machine, workflow, retry, catch, choice, parallel, map, wait, human approval.

BLOCKCHAIN

Amazon Managed Blockchain
Why exists: Build and operate blockchain networks without managing blockchain infrastructure.
Keywords: blockchain, distributed ledger, Ethereum, Hyperledger, decentralized network.

BUSINESS APPLICATIONS

Amazon SES
Why exists: Send transactional and bulk email.
Keywords: email, transactional email, marketing email, SMTP, bounce, complaint, DKIM.

CLOUD FINANCIAL MANAGEMENT

AWS Budgets
Why exists: Set cost/usage thresholds and receive alerts.
Keywords: budget, threshold, alert, cost control, forecast.

AWS Cost and Usage Report
Why exists: Detailed billing and usage data for analysis.
Keywords: CUR, detailed billing, granular cost data, S3, cost allocation.

AWS Cost Explorer
Why exists: Analyze AWS spending interactively.
Keywords: cost analysis, usage analysis, trends, filtering, forecasting.

Savings Plans
Why exists: Reduce compute costs in exchange for a usage commitment.
Keywords: commitment, discounted compute, 1 or 3 years, flexible compute usage.

COMPUTE

AWS App Runner
Why exists: Deploy web applications and APIs without managing infrastructure.
Keywords: source code/container, web application, fully managed, automatic scaling.

AWS Auto Scaling
Why exists: Automatically scale supported AWS resources based on demand.
Keywords: automatic scaling, resource scaling, target utilization.

AWS Batch
Why exists: Run large-scale batch computing jobs.
Keywords: batch jobs, queues, compute-intensive, job scheduling.

Elastic Beanstalk
Why exists: Deploy applications while AWS manages underlying infrastructure.
Keywords: PaaS, application deployment, managed platform, EC2, ALB, Auto Scaling.

Amazon EC2
Why exists: Give you virtual server control.
Keywords: virtual machine, OS control, custom software, persistent server, instance types.

Amazon EC2 Auto Scaling
Why exists: Automatically add/remove EC2 instances.
Keywords: ASG, desired capacity, scaling policy, health checks, replacement.

AWS Fargate
Why exists: Run containers without managing EC2 worker nodes.
Keywords: serverless containers, no EC2 management, ECS, EKS, task/pod.

AWS Lambda
Why exists: Execute code without managing servers.
Keywords: serverless, event-driven, invocation, automatic scaling, pay per request, stateless.

Amazon Lightsail
Why exists: Simplify small application deployments with predictable bundled pricing.
Keywords: simple VPS, predictable pricing, small workloads, beginner, bundled resources.

AWS Outposts
Why exists: Run AWS infrastructure in your own data center.
Keywords: on-premises AWS, hybrid, low latency, data residency, local processing.

AWS Wavelength
Why exists: Put AWS compute/storage close to 5G networks.
Keywords: 5G, ultra-low latency, telecom, edge.

CONTAINERS

Amazon ECR
Why exists: Store and manage container images.
Keywords: container registry, Docker image, private registry, image scanning, lifecycle policy.

Amazon ECS
Why exists: AWS-native container orchestration.
Keywords: containers, task, service, cluster, AWS-native, simpler than Kubernetes.

ECS Anywhere
Why exists: Run ECS-managed containers outside AWS.
Keywords: on-premises, external instances, ECS control plane, hybrid.

Amazon EKS
Why exists: Managed Kubernetes.
Keywords: Kubernetes, pods, nodes, Helm, operators, Kubernetes API.

EKS Anywhere
Why exists: Run Kubernetes clusters in your own environments using EKS tooling.
Keywords: on-premises Kubernetes, hybrid, EKS tooling.

EKS Distro
Why exists: AWS-supported Kubernetes distribution.
Keywords: Kubernetes distribution, upstream Kubernetes, self-managed environments.

DATABASE

Amazon Aurora
Why exists: High-performance managed relational database compatible with MySQL/PostgreSQL.
Keywords: relational, SQL, MySQL-compatible, PostgreSQL-compatible, high availability, read replicas.

Aurora Serverless
Why exists: Aurora for workloads with variable database capacity requirements.
Keywords: variable demand, intermittent workload, automatic capacity, serverless relational.

Amazon DocumentDB
Why exists: Managed document database compatible with MongoDB workloads.
Keywords: document database, JSON-like documents, MongoDB compatibility.

DynamoDB
Why exists: Highly scalable managed NoSQL database.
Keywords: key-value, document, serverless, massive scale, low latency, access patterns, Global Tables.

ElastiCache
Why exists: Provide fast in-memory caching.
Keywords: Redis, Memcached, cache, hot data, low latency, reduce database load.

Amazon Keyspaces
Why exists: Managed Apache Cassandra-compatible database.
Keywords: Cassandra, wide-column, serverless, high scale, NoSQL.

Amazon Neptune
Why exists: Managed graph database.
Keywords: graph, relationships, nodes, edges, knowledge graph, recommendation.

Amazon RDS
Why exists: Managed relational databases without managing database servers.
Keywords: SQL, relational, managed database, Multi-AZ, read replica, automated backups.

Amazon Redshift
Why exists: Data warehouse for large-scale analytical queries.
Keywords: data warehouse, OLAP, analytics, columnar, SQL, reporting.

Amazon Timestream
Why exists: Purpose-built time-series database.
Keywords: time series, IoT, metrics, telemetry, timestamps.

DEVELOPER TOOLS

AWS CodeArtifact
Why exists: Private package repository.
Keywords: Maven, npm, Python packages, dependencies, private repository.

AWS CodeBuild
Why exists: Managed build service.
Keywords: compile, test, build, CI, buildspec.

AWS CodeDeploy
Why exists: Automate application deployments.
Keywords: deployment, blue/green, in-place, rollback, EC2, Lambda.

Amazon CodeGuru
Why exists: Identify application performance and code quality issues.
Keywords: code review, performance profiling, recommendations, Java, Python.

AWS CodePipeline
Why exists: Automate CI/CD workflow stages.
Keywords: pipeline, source, build, test, deploy, CI/CD.

AWS X-Ray
Why exists: Trace requests across distributed applications.
Keywords: distributed tracing, segments, traces, latency, microservices, Lambda, API Gateway.

END USER COMPUTING

Amazon AppStream 2.0
Why exists: Stream desktop applications to users without installing them locally.
Keywords: application streaming, browser, desktop applications, remote access.

Amazon WorkSpaces
Why exists: Managed virtual desktops.
Keywords: VDI, virtual desktop, remote desktop, workforce, managed desktop.

FRONTEND WEB AND MOBILE

AWS Amplify
Why exists: Simplify development and deployment of web/mobile applications.
Keywords: frontend, mobile, hosting, authentication, APIs, full-stack.

Amazon API Gateway
Why exists: Managed API front door.
Keywords: REST, HTTP, WebSocket, throttling, authentication, Lambda integration, API management.

AWS Device Farm
Why exists: Test applications on real mobile devices and browsers.
Keywords: mobile testing, real devices, automated testing, compatibility.

Amazon Pinpoint
Why exists: Customer engagement and messaging.
Keywords: campaigns, analytics, push notifications, email, SMS, customer engagement.

IoT

AWS IoT Core
Why exists: Connect devices securely to AWS.
Keywords: MQTT, device gateway, telemetry, device shadows, certificates.

AWS IoT Device Defender
Why exists: Audit and monitor IoT security.
Keywords: IoT security, audit, detect anomalies, device behavior.

AWS IoT Device Management
Why exists: Manage fleets of IoT devices.
Keywords: fleet management, provisioning, groups, jobs, device registry.

AWS IoT Events
Why exists: Detect and respond to IoT events.
Keywords: event detection, IoT state, alarms, conditions.

AWS IoT Greengrass
Why exists: Extend AWS capabilities to edge devices.
Keywords: edge, local processing, offline operation, IoT devices.

AWS IoT SiteWise
Why exists: Collect and analyze industrial equipment data.
Keywords: industrial IoT, factory, equipment, telemetry, operational data.

AWS IoT Things Graph
Why exists: Connect devices and services using visual workflows.
Keywords: IoT workflows, device interactions, orchestration.

AWS IoT 1-Click
Why exists: Trigger AWS Lambda functions from simple IoT devices.
Keywords: simple devices, one-click action, Lambda.

MACHINE LEARNING

Amazon Comprehend
Why exists: Analyze natural language text.
Keywords: NLP, sentiment, entities, key phrases, PII, classification.

Amazon Fraud Detector
Why exists: Detect fraudulent activity.
Keywords: fraud detection, transactions, risk, machine learning.

Amazon Kendra
Why exists: Enterprise intelligent search.
Keywords: enterprise search, natural language search, documents, knowledge base.

Amazon Lex
Why exists: Build conversational bots.
Keywords: chatbot, conversational AI, voice, text, intent.

Amazon Personalize
Why exists: Build personalized recommendations.
Keywords: recommendations, personalization, user behavior, product recommendations.

Amazon Polly
Why exists: Convert text to speech.
Keywords: text-to-speech, TTS, voice.

Amazon Rekognition
Why exists: Analyze images and videos.
Keywords: image recognition, video analysis, faces, objects, labels, moderation.

Amazon SageMaker AI
Why exists: Build, train, deploy, and operate machine-learning models.
Keywords: ML lifecycle, training, inference, model deployment, notebooks, endpoints.

Amazon Textract
Why exists: Extract text and structured data from documents.
Keywords: OCR, forms, tables, scanned documents.

Amazon Transcribe
Why exists: Convert speech to text.
Keywords: speech-to-text, transcription, audio.

Amazon Translate
Why exists: Machine translation.
Keywords: translation, multilingual.

MEDIA

Amazon Elastic Transcoder
Why exists: Convert media files between formats.
Keywords: transcoding, video conversion, media formats.

Amazon Kinesis Video Streams
Why exists: Ingest and process video streams.
Keywords: video streaming, cameras, real-time video, IoT.

MANAGEMENT AND GOVERNANCE

AWS CloudFormation
Why exists: Infrastructure as code.
Keywords: IaC, templates, stacks, repeatable infrastructure.

AWS CloudTrail
Why exists: Record AWS API activity.
Keywords: audit, API calls, governance, who did what, when, where.

Amazon CloudWatch
Why exists: Monitor AWS resources and applications.
Keywords: metrics, alarms, logs, dashboards, monitoring.

CloudWatch Logs
Why exists: Centralize and analyze application/system logs.
Keywords: log groups, log streams, retention, metric filters.

AWS CLI
Why exists: Automate AWS management from command line.
Keywords: automation, scripting, CLI.

AWS Compute Optimizer
Why exists: Recommend right-sized AWS resources.
Keywords: rightsizing, optimization, recommendations, utilization.

AWS Config
Why exists: Track resource configuration and compliance.
Keywords: configuration history, compliance rules, configuration changes.

AWS Control Tower
Why exists: Establish governed multi-account AWS environments.
Keywords: landing zone, multi-account, governance, guardrails.

AWS Health Dashboard
Why exists: Show AWS service/account-specific health events.
Keywords: AWS outages, account-specific events, maintenance.

AWS License Manager
Why exists: Manage software licenses.
Keywords: license compliance, BYOL, software licenses.

Amazon Managed Grafana
Why exists: Managed Grafana dashboards and visualization.
Keywords: Grafana, dashboards, metrics, logs, managed.

Amazon Managed Service for Prometheus
Why exists: Managed Prometheus-compatible monitoring.
Keywords: Prometheus, metrics, PromQL, monitoring, managed.

AWS Management Console
Why exists: Graphical interface for AWS resource management.
Keywords: GUI, AWS management.

AWS Organizations
Why exists: Centrally manage multiple AWS accounts.
Keywords: multi-account, SCP, consolidated billing, organizational units.

AWS Proton
Why exists: Platform engineering for container/serverless deployments.
Keywords: templates, platform engineering, ECS, Fargate, standardized environments.

AWS Service Catalog
Why exists: Control and standardize approved AWS products.
Keywords: approved products, governance, self-service, portfolios.

Service Quotas
Why exists: View/manage AWS service limits.
Keywords: quotas, limits, increase request.

AWS Systems Manager
Why exists: Centrally manage EC2 and hybrid infrastructure.
Keywords: patching, Parameter Store, Session Manager, Run Command, inventory.

AWS Trusted Advisor
Why exists: Recommend improvements across AWS accounts.
Keywords: cost, security, performance, fault tolerance, service limits.

AWS Well-Architected Tool
Why exists: Evaluate workloads against AWS Well-Architected Framework.
Keywords: six pillars, workload review, architecture assessment.

MIGRATION AND TRANSFER

AWS Application Discovery Service
Why exists: Discover on-premises application dependencies and inventory.
Keywords: discovery, dependency mapping, inventory, migration planning.

AWS Application Migration Service
Why exists: Lift-and-shift servers into AWS.
Keywords: rehost, lift-and-shift, continuous replication, migration.

AWS DMS
Why exists: Migrate/replicate databases.
Keywords: database migration, replication, CDC, heterogeneous migration.

AWS DataSync
Why exists: High-speed managed data transfer.
Keywords: file transfer, NFS, SMB, S3, EFS, FSx, on-premises.

AWS Migration Hub
Why exists: Track migrations centrally.
Keywords: migration tracking, application portfolio, centralized migration view.

AWS SCT
Why exists: Convert database schemas between database engines.
Keywords: schema conversion, heterogeneous migration, Oracle to PostgreSQL.

AWS Snow Family
Why exists: Move/process large amounts of data when network transfer is impractical.
Keywords: offline transfer, physical appliance, massive data, edge processing.

AWS Transfer Family
Why exists: Managed SFTP/FTPS/FTP access to AWS storage.
Keywords: SFTP, FTPS, FTP, legacy file transfer, S3, EFS.

NETWORKING AND CONTENT DELIVERY

Amazon CloudFront
Why exists: Global content delivery through edge locations.
Keywords: CDN, caching, edge, global content delivery, origin.

AWS Direct Connect
Why exists: Dedicated private network connection from on-premises to AWS.
Keywords: dedicated connection, private connectivity, predictable network, hybrid.

Elastic Load Balancing
Why exists: Distribute traffic across targets.
Keywords: load balancing, health checks, ALB, NLB, GWLB.

AWS Global Accelerator
Why exists: Improve global application availability/performance using AWS global network.
Keywords: static anycast IP, global traffic, TCP/UDP, fast failover.

AWS PrivateLink
Why exists: Private access to services without traversing the public internet.
Keywords: private endpoint, interface endpoint, service provider, SaaS, endpoint service.

Amazon Route 53
Why exists: DNS and global traffic management.
Keywords: DNS, hosted zones, routing policies, health checks, failover, latency, weighted.

AWS Transit Gateway
Why exists: Central hub for connecting many VPCs and networks.
Keywords: hub-and-spoke, VPC peering alternative, centralized routing, multi-account.

Amazon VPC
Why exists: Isolated virtual networking in AWS.
Keywords: subnet, route table, security group, NACL, IGW, NAT, VPC endpoints.

AWS VPN
Why exists: Encrypted network connectivity over the internet.
Keywords: Site-to-Site VPN, Client VPN, IPsec, encrypted tunnel, hybrid.

SECURITY, IDENTITY AND COMPLIANCE

AWS Artifact
Why exists: Access AWS compliance reports and agreements.
Keywords: compliance reports, SOC, PCI, ISO, agreements.

AWS Audit Manager
Why exists: Collect evidence for audits.
Keywords: audit evidence, compliance, automated evidence collection.

AWS Certificate Manager
Why exists: Manage TLS/SSL certificates.
Keywords: HTTPS, TLS, certificates, ACM, public/private certificates.

AWS CloudHSM
Why exists: Dedicated hardware security modules under customer control.
Keywords: HSM, hardware, cryptographic keys, FIPS, customer control.

Amazon Cognito
Why exists: Application user authentication and authorization.
Keywords: user pools, identity pools, web/mobile authentication, federation.

Amazon Detective
Why exists: Investigate security findings and relationships.
Keywords: investigation, security findings, behavior analysis, root cause.

AWS Directory Service
Why exists: Managed directory services.
Keywords: Active Directory, Microsoft AD, domain join, LDAP.

AWS Firewall Manager
Why exists: Centrally manage firewall/security policies across accounts.
Keywords: centralized security, multi-account, WAF, Shield, Network Firewall.

Amazon GuardDuty
Why exists: Threat detection.
Keywords: threat detection, malicious activity, anomaly, findings.

AWS IAM Identity Center
Why exists: Central workforce access across AWS accounts and applications.
Keywords: SSO, workforce, multi-account access, permission sets.

IAM
Why exists: Control access to AWS resources.
Keywords: users, roles, policies, permissions, least privilege.

Amazon Inspector
Why exists: Automated vulnerability management.
Keywords: vulnerabilities, EC2, ECR, Lambda, CVE, software packages.

AWS KMS
Why exists: Managed encryption key management.
Keywords: encryption, keys, CMK/KMS key, envelope encryption, data at rest.

Amazon Macie
Why exists: Discover and protect sensitive data in S3.
Keywords: sensitive data, PII, S3, data discovery.

AWS Network Firewall
Why exists: Managed stateful network firewall.
Keywords: VPC firewall, stateful, IDS/IPS-style controls, centralized inspection.

AWS RAM
Why exists: Share supported AWS resources across accounts.
Keywords: resource sharing, multi-account, Organizations, shared resources.

AWS Secrets Manager
Why exists: Securely store and rotate secrets.
Keywords: passwords, API keys, rotation, database credentials.

AWS Security Hub
Why exists: Centralize and prioritize security findings.
Keywords: centralized findings, security posture, standards, aggregation.

AWS STS
Why exists: Issue temporary AWS credentials.
Keywords: temporary credentials, AssumeRole, federation, cross-account.

AWS Shield
Why exists: DDoS protection.
Keywords: DDoS, Layer 3/4, Shield Standard, Shield Advanced.

AWS WAF
Why exists: Filter malicious web requests.
Keywords: Layer 7, HTTP/HTTPS, SQL injection, XSS, web ACL, rate-based rules.

STORAGE

AWS Backup
Why exists: Centrally manage backups across AWS services.
Keywords: centralized backup, backup policies, vault, retention, cross-account.

Amazon EBS
Why exists: Persistent block storage for EC2.
Keywords: block storage, EC2, boot volume, low latency, snapshots.

AWS Elastic Disaster Recovery
Why exists: Recover workloads into AWS after disaster.
Keywords: DR, continuous replication, RPO, RTO, recovery.

Amazon EFS
Why exists: Managed shared file system for Linux workloads.
Keywords: NFS, shared filesystem, multiple EC2, Linux, elastic storage.

Amazon FSx
Why exists: Managed specialized file systems.

FSx for Windows File Server:
Keywords: SMB, Windows, Active Directory.

FSx for Lustre:
Keywords: HPC, high performance, machine learning, S3 integration.

FSx for NetApp ONTAP:
Keywords: enterprise NAS, NFS, SMB, multiprotocol, NetApp.

FSx for OpenZFS:
Keywords: ZFS, NFS, high-performance file system.

Amazon S3
Why exists: Durable scalable object storage.
Keywords: object storage, 11 9s durability, lifecycle, versioning, replication, static assets, data lake.

Amazon S3 Glacier
Why exists: Low-cost archival storage.
Keywords: archive, long-term retention, infrequent access, compliance, retrieval time.

AWS Storage Gateway
Why exists: Connect on-premises environments to AWS cloud storage.

File Gateway:
Keywords: NFS/SMB, S3-backed file storage.

Volume Gateway:
Keywords: iSCSI, block storage, hybrid, cached/stored volumes.

Tape Gateway:
Keywords: virtual tapes, backup, VTL, replacement for physical tape.

THE MOST IMPORTANT SAP-C02 SERVICE RECOGNITION MAP

When you see:

"Queue"
→ SQS

"Fan-out"
→ SNS

"Event routing"
→ EventBridge

"Workflow"
→ Step Functions

"Serverless function"
→ Lambda

"Serverless container"
→ Fargate

"AWS-native containers"
→ ECS

"Kubernetes"
→ EKS

"Virtual machine control"
→ EC2

"Simple PaaS"
→ Elastic Beanstalk

"Simple VPS"
→ Lightsail

"Key-value/document"
→ DynamoDB

"Relational SQL"
→ RDS/Aurora

"Variable relational capacity"
→ Aurora Serverless

"Cache/hot data"
→ ElastiCache

"Graph relationships"
→ Neptune

"MongoDB-compatible document"
→ DocumentDB

"Cassandra-compatible"
→ Keyspaces

"Data warehouse"
→ Redshift

"Time-series"
→ Timestream

"Search/log analytics"
→ OpenSearch

"Object storage"
→ S3

"Block storage"
→ EBS

"Shared Linux filesystem"
→ EFS

"Windows SMB"
→ FSx for Windows

"HPC filesystem"
→ FSx for Lustre

"Dedicated private connection"
→ Direct Connect

"Encrypted internet connection"
→ VPN

"Connect many VPCs"
→ Transit Gateway

"Private service access"
→ PrivateLink

"Global CDN"
→ CloudFront

"Global static IP / fast failover"
→ Global Accelerator

"DNS"
→ Route 53

"Who did what in AWS"
→ CloudTrail

"Resource configuration history"
→ Config

"Threat detection"
→ GuardDuty

"Security investigation"
→ Detective

"Centralized security findings"
→ Security Hub

"Vulnerability scanning"
→ Inspector

"S3 sensitive data"
→ Macie

"Web attack filtering"
→ WAF

"DDoS"
→ Shield

"Encryption keys"
→ KMS

"Secrets/password rotation"
→ Secrets Manager

"Temporary credentials"
→ STS

"Multi-account governance"
→ Organizations / Control Tower

"Central workforce SSO"
→ IAM Identity Center

"On-premises discovery"
→ Application Discovery Service

"Server lift-and-shift"
→ Application Migration Service

"Database migration"
→ DMS

"Schema conversion"
→ SCT

"Large offline data transfer"
→ Snow Family

"High-speed file transfer"
→ DataSync

"SFTP into S3/EFS"
→ Transfer Family

THE SAP-C02 DECISION PATTERN

For almost every service question, run this sequence:

1. What problem exists?

2. Is the workload synchronous or asynchronous?

3. Does it need persistent storage?

4. What is the data access pattern?

5. Does it need SQL?

6. Does it need Kubernetes?

7. Does it need server-level control?

8. Is traffic predictable or unpredictable?

9. Is the workload global?

10. What is the availability/RTO/RPO requirement?

11. What is the operational overhead?

12. What is the cheapest architecture that satisfies all requirements?

The exam rarely rewards "I know what this service does" by itself.

It rewards:

Requirement → constraint → architecture → AWS service → trade-off → cost.

That is the level of thinking you should use for SAP-C02.
