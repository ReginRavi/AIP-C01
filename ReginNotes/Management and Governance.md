
These services form the **operational backbone**. They ensure your AI applications remain highly available, cost-effective, auditable, and easily monitored by your development team.

### 1. AWS Auto Scaling

- **Benefits:** Automatically adjusts compute capacity to maintain steady, predictable performance at the lowest possible cost based on defined policies.

- **When to Use (AIP-C01 Triggers):** Look for _"Dynamic scaling,"_ _"handle traffic spikes,"_ _"scale SageMaker endpoints,"_ or _"maintain application responsiveness."_

- **Cost Structure:** The service itself is free; you pay only for the AWS resources (e.g., EC2 instances or SageMaker endpoints) that are provisioned.

- **Use Case:** Scaling the EC2 instances hosting a tRPC backend to handle sudden surges in market-open traffic, ensuring the underlying quantitative fundamental and technical analysis engine remains highly responsive without requiring manual intervention.


### 2. AWS Chatbot

- **Benefits:** An interactive agent that makes it easy to monitor and interact with AWS resources directly within collaborative chat platforms like Slack or Microsoft Teams.

- **When to Use (AIP-C01 Triggers):** Look for _"Slack integration,"_ _"receive CloudWatch alerts in chat,"_ or _"run AWS CLI commands from Teams."_

- **Cost Structure:** Free; you only pay for the underlying services utilized (like Amazon SNS or CloudWatch alarms).

- **Use Case:** Sending immediate diagnostic alerts to a 7-person project team’s Slack channel (alerting the 5 developers, architect, and functional lead) if an automated Bedrock pipeline fails during a sprint.

### 3. AWS CloudTrail

- **Benefits:** Tracks user activity and API usage across your AWS infrastructure, providing a complete history of events for governance, compliance, and operational auditing.

- **When to Use (AIP-C01 Triggers):** Look for _"Audit API calls,"_ _"who did what,"_ _"track unauthorized access,"_ or _"compliance auditing."_

- **Cost Structure:** The first copy of management events is free; you pay for data events or additional trails.

- **Use Case:** Auditing exactly which IAM user or role invoked a sensitive Amazon Bedrock API to adjust the core parameters of a technical analysis scoring algorithm.


### 4. Amazon CloudWatch

- **Benefits:** The core observability service that collects operational data in the form of logs, metrics, and events, allowing you to set alarms and automatically react to changes.

- **When to Use (AIP-C01 Triggers):** Look for _"Monitor metrics,"_ _"set CPU/memory alarms,"_ _"track Bedrock invocation latency,"_ or _"trigger automated actions."_

- **Cost Structure:** Pay per custom metric, alarm configured, and dashboard created.

- **Use Case:** Setting an automated alarm on the EC2 memory usage of a mutual fund platform, triggering a notification if the intensive fundamental analysis algorithms consume too much RAM during processing.


### 5. Amazon CloudWatch Logs

- **Benefits:** A centralized logging service designed to store, monitor, and access highly detailed log files from various AWS services and custom applications.

- **When to Use (AIP-C01 Triggers):** Look for _"Store application logs,"_ _"troubleshoot Lambda errors,"_ _"retain Bedrock invocation logs,"_ or _"search application errors."_

- **Cost Structure:** Pay per GB of data ingested, archived, and analyzed via queries.

- **Use Case:** Storing the exact prompt inputs and the AI-generated mutual fund recommendations to deeply debug why the fundamental analysis engine produced a specific, unexpected portfolio output.


### 6. Amazon CloudWatch Synthetics

- **Benefits:** Allows you to create "canaries"—configurable scripts that run on a schedule to continually verify your endpoints and APIs from the outside in, mimicking a user's experience.

- **When to Use (AIP-C01 Triggers):** Look for _"Monitor API uptime,"_ _"simulate user workflows,"_ _"track endpoint latency,"_ or _"proactive testing."_

- **Cost Structure:** Pay per canary run.

- **Use Case:** Running a canary script every 5 minutes against a primary API endpoint to verify that the mutual fund platform is successfully returning mock data during the rapid prototyping and verification phase.


### 7. AWS Cost Anomaly Detection

- **Benefits:** Uses advanced machine learning to continuously monitor your cost and usage to detect unusual spend, minimizing the risk of billing surprises.

- **When to Use (AIP-C01 Triggers):** Look for _"Unexpected charges,"_ _"monitor AI spending spikes,"_ _"automated cost alerts,"_ or _"detect runaway processes."_

- **Cost Structure:** Free.

- **Use Case:** Automatically detecting if a logic error in a script causes thousands of unintended, expensive Bedrock inference calls for technical analysis, alerting the team before the monthly bill escalates.


### 8. AWS Cost Explorer

- **Benefits:** A visual interface that enables you to view, understand, forecast, and manage your AWS costs and usage over time.

- **When to Use (AIP-C01 Triggers):** Look for _"Forecast future spend,"_ _"break down AI costs by tag,"_ _"analyze historical usage,"_ or _"cost visualization."_

- **Cost Structure:** The user interface is free; there is a small fee per programmatic API request.

- **Use Case:** Forecasting the upcoming month's infrastructure costs for a mutual fund recommendation engine based on historical API usage and data processing volume.

### 9. Amazon Managed Grafana

- **Benefits:** A fully managed and secure data visualization service that allows you to instantly query, correlate, and visualize operational metrics, logs, and traces.

- **When to Use (AIP-C01 Triggers):** Look for _"Visualize operational data,"_ _"interactive monitoring dashboards,"__"open-source visualization,"_ or _"multi-source data querying."_

- **Cost Structure:** Pay per active user license per month.

- **Use Case:** Providing the project team with highly interactive, visual dashboards tracking the processing latency and performance metrics of the fundamental and technical analysis algorithms in real-time.


### 10. AWS Service Catalog

- **Benefits:** Allows organizations to create, manage, and distribute catalogs of IT services that are pre-approved for use on AWS, ensuring strict governance and compliance.

- **When to Use (AIP-C01 Triggers):** Look for _"Standardize deployments,"_ _"enforce compliance,"_ _"self-service portal,"_ or _"approved resource templates."_

- **Cost Structure:** Pay per portfolio created and per portfolio access.

- **Use Case:** Creating a pre-approved, compliant template for deploying a standard EC2 server—explicitly configured without containerization—that developers can launch safely to test the analysis engine within organizational guidelines.


### 11. AWS Systems Manager

- **Benefits:** An operations hub providing a unified user interface to view operational data from multiple AWS services and automate operational tasks across your resources (including Parameter Store for configuration management).

- **When to Use (AIP-C01 Triggers):** Look for _"Patch management,"_ _"run commands on multiple instances,"__"store configuration data (Parameter Store),"_ or _"unified operations."_

- **Cost Structure:** Core features (like Parameter Store standard parameters) are free; advanced features have pay-per-use pricing.

- **Use Case:** Storing the API keys for live market data services securely in Systems Manager Parameter Store, allowing developers to easily swap them out for fake historical mock data endpoints during early-stage development.

### 12. AWS Well-Architected Tool

- **Benefits:** Helps you review the state of your workloads and compares them to the latest AWS architectural best practices (covering operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability).

- **When to Use (AIP-C01 Triggers):** Look for _"Architecture review,"_ _"identify security risks,"_ _"optimize cost and performance,"_ or _"best practices assessment."_

- **Cost Structure:** Free.

- **Use Case:** Systematically reviewing a newly designed mutual fund platform architecture—ensuring the equity funds, technical scoring components, and backend APIs align with stringent best practices for reliability and security before production deployment.