**Amazon GuardDuty** is an intelligent, fully managed continuous threat detection service. It monitors AWS accounts, workloads, container clusters, and data to identify unauthorized behavior, account compromises, and malicious activity using machine learning, anomaly detection, and integrated threat intelligence.

### 1. Key Characteristics & Architecture

- **Zero Workload Impact (Agentless by default):** Analyzes log streams directly from the AWS backend infrastructure without consuming CPU/memory or degrading application performance.
    
- **Independent Data Ingestion:** Reads foundational log streams directly—even if VPC Flow Logs or S3 Data Events are not explicitly turned on in your account.
    
- **Integrated Threat Intelligence:** Uses proprietary AWS security feeds, CrowdStrike, Proofpoint, and community feeds (known malicious IPs, Tor exit nodes, malware hashes, crypto-mining pools).
    
- **Finding Severity Scoring:** Categorizes findings into Low (`0.1–3.9`), Medium (`4.0–6.9`), and High (`7.0–8.9`) in standard AWS Security Finding Format (ASFF).
    
- **Multi-Account Governance:** Integrates with **AWS Organizations** to designate a _Delegated Security Administrator Account_ and automatically enable GuardDuty on all existing and newly created member accounts.
    

```
┌─────────────────────────────────────────────────────────────┐
│                    GUARDDUTY DATA SOURCES                   │
├───────────────────────────────┬─────────────────────────────┤
│ Foundational (Always-On)      │ Optional Protection Plans   │
├───────────────────────────────┼─────────────────────────────┤
│ • AWS CloudTrail Mgmt Events  │ • S3 Protection             │
│ • VPC Flow Logs (Direct feed) │ • EKS Audit Log Monitoring  │
│ • Route 53 DNS Query Logs     │ • Runtime Monitoring (EKS,  │
│                               │   ECS/Fargate, EC2)         │
│                               │ • RDS Login Protection      │
│                               │ • Lambda Network Monitoring │
│                               │ • Malware Protection (EBS,  │
│                               │   S3, AWS Backup)           │
└───────────────────────────────┴─────────────────────────────┘
                               │
                               ▼ (ML, Anomaly Detection, Threat Feeds)
┌─────────────────────────────────────────────────────────────┐
│                     GUARDDUTY FINDINGS                      │
└──────────────────────────────┬──────────────────────────────┘
                               │
            ┌──────────────────┴──────────────────┐
            ▼                                     ▼
 [ Amazon EventBridge ]                  [ AWS Security Hub ]
  ├──► Automated Remediation (Lambda)     └──► Centralized SIEM /
  └──► Alerting (SNS, PagerDuty, Slack)        Governance Dashboard
```

### 2. Is it Serverless? Who Manages the Infrastructure?

|**Dimension**|**GuardDuty Specification**|
|---|---|
|**Serverless?**|**100% Serverless.** No servers to provision, configure, or patch.|
|**Infrastructure Owner**|**AWS fully manages** the underlying infrastructure, ML models, log ingestion pipelines, and threat intelligence updates.|
|**Agent Requirement**|**Agentless** for foundational data sources, S3, RDS, and Malware scans. _(Requires a lightweight security agent only if you enable OS-level EKS/ECS/EC2 Runtime Monitoring)._|

### 3. Operational Overhead: High or Least?

GuardDuty provides the **LEAST operational overhead** of any threat detection mechanism on AWS:

- **One-Click Enablement:** Turn it on globally or across an organization in seconds.
    
- **Zero Rule Maintenance:** Unlike Web Application Firewalls (WAF) or traditional SIEM tools, you do not write, update, or tune signature detection rules manually.
    
- **Automated Actionability:** Streams findings directly to **Amazon EventBridge**, enabling automated serverless remediations (e.g., triggering a Lambda function to isolate a compromised EC2 instance or revoke an IAM role).
    

### 4. Cost Model & Pricing

GuardDuty charges are based on the **volume of data and events analyzed**, not per finding or per EC2 instance count:

|**Protection Plan / Source**|**Pricing Metric**|
|---|---|
|**CloudTrail Management Events**|Billed per million events ($4.00/million events).|
|**VPC Flow Logs & DNS Query Logs**|Tiered pricing per GB analyzed (e.g., $1.00/GB for the first 500 GB).|
|**S3 Data Events**|Billed per million S3 events ($0.80/million events).|
|**EKS Audit Logs**|Billed per million audit events ($1.60/million events).|
|**RDS Protection**|Billed per provisioned database vCPU per month ($1.00/vCPU).|
|**Runtime Monitoring**|Billed per vCPU per month for managed workloads.|
|**Malware Protection**|Billed per GB of EBS snapshot/S3 object scanned when triggered.|
|**Free Tier / Trial**|**30-day free trial** for every account to estimate monthly run rate before billing starts.|

### 5. When to Use & Common Real-World Scenarios

#### Scenario A: Compromised IAM Credentials

- **Trigger:** An IAM secret key is leaked on GitHub or used from an unusual country / Tor exit node to make unusual API calls (`Recon:IAM/TorIP`, `UnauthorizedAccess:IAMUser/InstanceCredentialExfiltration`).
    
- **GuardDuty Response:** Flags credential exfiltration and alerts security teams to immediately deactivate the compromised access key.
    

#### Scenario B: Compromised EC2 / Container Cryptomining

- **Trigger:** An EC2 instance or EKS pod starts communicating with known Bitcoin/Monero mining pools or command-and-control (C2) servers (`CryptoCurrency:EC2/BitcoinTool.B!DNS`).
    
- **GuardDuty Response:** EventBridge triggers a Lambda function that modifies the instance's Security Group to isolate it from the VPC and takes an EBS snapshot for forensic analysis.
    

#### Scenario C: S3 Ransomware & Data Exfiltration

- **Trigger:** A principal suddenly disables S3 bucket encryption, begins mass-deleting objects, or reads an unusual volume of data from an unfamiliar IP (`Exfiltration:S3/AnomalousBehavior`, `Impact:S3/MaliciousIPCaller`).
    
- **GuardDuty Response:** Alerts on anomalous S3 access patterns before complete data exfiltration occurs.
    

#### Scenario D: Database Credential Stuffing & Brute-Force

- **Trigger:** Repeated failed login attempts against an Amazon Aurora or RDS PostgreSQL/MySQL database from external anomalous IPs (`Discovery:RDS/MaliciousIPCaller`).
    
- **GuardDuty Response:** Highlights brute-force attempts on private database endpoints.
    

### 6. Quick Decision Matrix: GuardDuty vs. Other AWS Security Services

|**Service**|**Primary Purpose**|**Scope / Layer**|
|---|---|---|
|**Amazon GuardDuty**|**Intelligent Threat Detection & Anomaly Monitoring** (Who is attacking or behaving suspiciously?)|CloudTrail, VPC Flow, DNS, EKS, RDS, S3, Runtime|
|**Amazon Inspector**|**Vulnerability & CVE Management** (What unpatched software packages or open ports exist?)|EC2 OS packages, Container images (ECR), Lambda code|
|**Amazon Macie**|**Sensitive Data Discovery** (Where is unencrypted PII, credit card data, or PHI?)|S3 Buckets / Object Content|
|**AWS Security Hub**|**Central Security Dashboard & Compliance Posture** (Aggregates GuardDuty, Inspector, Macie + CIS benchmarks)|Centralized posture management (CSPM)|
|**AWS WAF / Shield**|**Edge Traffic Inspection & DDoS Prevention** (Blocks SQLi, XSS, and layer 7 web attacks)|CloudFront, ALB, API Gateway|

**Use AWS Web Application Firewall (WAF) as the first line of defense to protect the API Gateway APIs against malicious exploits and DDoS attacks. Install Amazon Inspector on the EC2 instance to check for vulnerabilities. Configure Amazon GuardDuty to monitor any malicious attempts to access the APIs illegally**

AWS WAF is a web application firewall that helps protect web applications and APIs from attacks. It enables you to configure a set of rules (called a web access control list (web ACL)) that allow, block, or count web requests based on customizable web security rules and conditions that you define. You can protect the following resource types:

1. Amazon CloudFront distribution
2. Amazon API Gateway REST API
3. Application Load Balancer
4. AWS AppSync GraphQL API
5. Amazon Cognito user pool

You can use AWS WAF to protect your API Gateway API from common web exploits, such as SQL injection and cross-site scripting (XSS) attacks. These could affect API availability and performance, compromise security, or consume excessive resources. For example, you can create rules to allow or block requests from specified IP address ranges, requests from CIDR blocks, requests that originate from a specific country or region, requests that contain malicious SQL code, or requests that contain malicious scripts.

DDoS attacks are attempts by an attacker to disrupt the availability of targeted systems. For infrastructure layer attacks, you can use AWS services such as Amazon CloudFront and Elastic Load Balancing (ELB) to provide automatic DDoS protection. For application layer attacks, you can use AWS WAF as the primary mitigation. AWS WAF web access control lists (web ACLs) minimize the effects of a DDoS attack at the application layer.

How WAF works: 

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q9-i1.jpg)

 via - [https://aws.amazon.com/waf/](https://aws.amazon.com/waf/)

GuardDuty is an intelligent threat detection service that continuously <mark style="background:#fff88f">monitors</mark> your AWS accounts, Amazon Elastic Compute Cloud (EC2) instances, Amazon Elastic Kubernetes Service (EKS) clusters, and data stored in Amazon Simple Storage Service (S3) for malicious activity without the use of security software or agents. If potential malicious activity, such as anomalous behavior, credential exfiltration, or command and control infrastructure (C2) communication is detected, GuardDuty generates detailed security findings that can be used for security visibility and assisting in remediation. GuardDuty can monitor reconnaissance activities by an attacker such as unusual API activity, intra-VPC port scanning, unusual patterns of failed login requests, or unblocked port probing from a known bad IP.

How GuardDuty works: 

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q9-i2.jpg)

 via - [https://aws.amazon.com/guardduty/](https://aws.amazon.com/guardduty/)

Amazon Inspector is an automated vulnerability management service that continually scans Amazon Elastic Compute Cloud (EC2) and container workloads for software vulnerabilities and unintended network exposure.

How Amazon Inspector works: 

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q9-i3.jpg)

 via - [https://aws.amazon.com/inspector](https://aws.amazon.com/inspector)

Incorrect options:

**Configure Amazon CloudFront in front of the APIs to protect against malicious exploits and DDoS attacks. Install Amazon GuardDuty on the EC2 instances to assess any vulnerabilities** - This statement is incorrect. GuardDuty cannot assess vulnerabilities in the EC2 instances. Amazon Inspector is the automated vulnerability management service that continually scans Amazon Elastic Compute Cloud (EC2) and container workloads for software vulnerabilities and unintended network exposure.

**Enable AWS Network Firewall on API Gateway as well as the Amazon EC2 instances to check for vulnerabilities and protect against DDoS attacks as well as malicious exploits** - AWS Network Firewall is a managed service that makes it easy to deploy essential network protections for all of your Amazon Virtual Private Clouds (VPCs). AWS Network Firewall works with AWS Firewall Manager to centrally manage security policies and automatically enforce mandatory security policies across existing and newly created accounts and VPCs. This service works at the VPC level and not at the API Gateway or the EC2 instance level.

How AWS Network Firewall works: 

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q9-i4.jpg)

 via - [https://aws.amazon.com/network-firewall/](https://aws.amazon.com/network-firewall/)

**Use AWS Web Application Firewall (WAF) as the first line of defense to protect the API Gateway APIs against malicious exploits and DDoS attacks. Install Amazon Inspector on the EC2 instance to check for vulnerabilities. Configure Amazon GuardDuty to block any malicious attempts to access the APIs illegally** - <mark style="background:#fff88f">GuardDuty cannot block any malicious attempts to access the APIs illegally. Rather, it can only monitor/detect such attempts.</mark>

References:

[https://aws.amazon.com/guardduty/faqs/](https://aws.amazon.com/guardduty/faqs/)

[https://aws.amazon.com/premiumsupport/knowledge-center/waf-mitigate-ddos-attacks/](https://aws.amazon.com/premiumsupport/knowledge-center/waf-mitigate-ddos-attacks/)

Domain

Design for New Solutions