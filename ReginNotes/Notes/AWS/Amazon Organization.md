AWS Organizations has two available feature sets:

All features – This feature set is the preferred way to work with AWS Organizations, and it includes Consolidating Billing features. When you create an organization, enabling all features is the default. With all features enabled, you can use the advanced account management features available in AWS Organizations such as integration with supported AWS services and organization management policies. Policies in AWS Organizations enable you to apply additional types of management to the AWS accounts in your organization. You can use policies when all features are enabled in your organization. Service control policies (SCPs) offer central control over the maximum available permissions for all of the accounts in your organization.

Consolidated Billing features – All organizations support this subset of features, which provides basic management tools that you can use to centrally manage the accounts in your organization. <mark style="background:#fff88f">You cannot leverage SCPs in this feature mode.</mark>

**AWS Organizations** is a <mark style="background:#fff88f">centralized account management and governance service</mark> that allows you to consolidate, organize, and manage multiple AWS accounts under a single hierarchy.

It provides a unified way to manage security boundaries, automate account provisioning, share resources, and consolidate billing across an entire organization.

### Core Structure & Components

```
                          [ Root ]
                             │
     ┌───────────────────────┴───────────────────────┐
     ▼                                               ▼
[ Core / Security OU ]                       [ Workloads OU ]
 ├── Log Archive Account                      ├── [ Dev OU ]
 └── Security Tooling Account                 │    ├── Dev App Account 1
                                              │    └── Dev App Account 2
                                              └── [ Prod OU ]
                                                   ├── Prod App Account 1
                                                   └── Prod App Account 2
```

- **Management Account (formerly Master Account):** The primary AWS account that creates the organization, pays the consolidated bill, and manages policies across member accounts.

- **Member Accounts:** All other standard AWS accounts that belong to the organization.

- **Organizational Units (OUs):** Logical containers used to group accounts in a tree-like hierarchy (e.g., `Security`, `Production`, `Development`). OUs can be nested inside other OUs.

- **Root:** The top-most parent container that houses all OUs and accounts.


### Key Capabilities & Features

#### 1. Service Control Policies (SCPs)

- **What they do:** Define maximum permission guardrails for IAM users, roles, and the root user in member accounts.

- **How they work:** SCPs do not grant permissions on their own; they act as a boundary. An explicit `Deny` in an SCP overrides all IAM allow statements.

- **Hierarchy:** Policies applied to an OU automatically inherit down to all nested OUs and member accounts within it.


#### 2. Consolidated Billing

- Combines billing across all member accounts into a **single invoice** paid by the Management Account.

- **Volume Pricing & Sharing:** Automatically aggregates usage across accounts to qualify for tier discounts and shares Reserved Instance (RI) and Savings Plans benefits across the organization.


#### 3. Centralized Governance & Integrated Services

- Integrates natively with other AWS services to enforce governance across accounts without manual setup:

    - **AWS CloudTrail:** Create an organization trail to log all API calls across all accounts into a central S3 bucket.

    - **AWS IAM Identity Center (SSO):** Centrally manage user access and multi-account permissions.

    - **AWS Resource Access Manager (RAM):** Share centralized resources (e.g., Transit Gateways, VPC subnets, Route 53 Resolver rules) across accounts.

    - **AWS Backup:** Enforce centralized backup policies across multiple accounts and regions.

    - **AWS Config:** Deploy organization-wide compliance rules and conformance packs.


### High-Yield Exam & Architecture Rules (SAP-C02)

|**Rule / Feature**|**Behavior**|
|---|---|
|**Management Account Immunity**|SCPs **never** apply to the Management (payer) Account or its root user.|
|**Default SCP Behavior**|Organizations starts with `FullAWSAccess` attached to all OUs/accounts by default (allow-list model).|
|**SCP vs. IAM Permissions**|An action is only permitted if allowed by **both** the IAM policy AND the SCP chain.|
|**Pricing**|AWS Organizations is offered at **no additional charge**. You pay only for the resources used within individual accounts.|