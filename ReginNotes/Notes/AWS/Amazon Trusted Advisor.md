#TrustedAdvisor #AccessAnalyzer

The easiest way to remember it:

> **Trusted Advisor = “Is my AWS environment healthy and optimized?”**  
> **Access Analyzer = “Who can access my AWS resources, and is that access too broad?”**

|Feature|**AWS Trusted Advisor**|**IAM Access Analyzer**|
|---|---|---|
|Main purpose|AWS environment recommendations|IAM/access security analysis|
|Focus|**Cost, security, performance, fault tolerance, service limits**|**Permissions and resource access**|
|Finds|Unused resources, security configuration issues, quotas, cost-saving opportunities, etc.|Public/cross-account access, internal access, unused permissions|
|IAM policy analysis|Limited / specific checks|**Yes, core capability**|
|Cross-account access|Can flag certain security issues|**Specifically analyzes it**|
|Public S3/resource access|Can have security-related checks|**Specifically analyzes resource policies**|
|Policy validation|Not its main purpose|**Yes**|
|Least privilege|Indirectly|**Strong focus**|
|Scope|Broad AWS account health|IAM and supported resource permissions|

AWS describes <mark style="background:#fff88f">Trusted Advisor as a service that provides recommendations</mark> across areas such as security, cost optimization, performance, fault tolerance, and service quotas.

<mark style="background:#fff88f">IAM Access Analyzer, on the other hand, specifically analyzes access and IAM policies</mark>. It can identify **external access, internal access, unused access**, validate policies, and even generate policies based on CloudTrail activity.

### Example

Suppose you have an S3 bucket:

S3 bucket: company-data

Bucket policy:

"Principal": "*"

"Action": "s3:GetObject"

**Access Analyzer** asks:

> “Does this policy allow public or external access?”

It can generate a finding showing that the bucket is accessible outside your defined zone of trust.

**Trusted Advisor** is broader. It asks things like:

> “Are there security issues, unused resources, cost opportunities, performance problems, or service-quota concerns in this AWS environment?”

### Another example: IAM role

Suppose:

Role: DeveloperRole

  

Permissions:

s3:*

ec2:*

iam:*

Access Analyzer can help determine whether permissions are **unused or overly broad**, and its policy-validation capabilities can flag policy issues and security warnings.

### For AWS certification exams

Think:

**Trusted Advisor → AWS account best-practice advisor**

**Access Analyzer → IAM permissions/access advisor**

A common exam clue:

- **“Cost optimization / service limits / fault tolerance / performance” → Trusted Advisor**
- **“Public access / cross-account access / unintended access / least privilege / IAM policy” → Access Analyzer**