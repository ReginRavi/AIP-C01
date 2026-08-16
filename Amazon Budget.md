
**AWS Budgets** and **AWS Cost Explorer** both query the same underlying billing dataset, but they serve two distinct financial governance roles:

- **AWS Budgets is PROACTIVE:** You set spending caps, usage limits, or coverage targets ahead of time, and it alerts you or triggers automated actions when thresholds are approached or breached.

- **AWS Cost Explorer is DIAGNOSTIC & ANALYTICAL:** It provides interactive dashboards to slice, filter, visualize historical spend, pinpoint root causes of cost spikes, and project future costs.
### Comparison Matrix

|**Feature / Dimension**|**AWS Budgets**|**AWS Cost Explorer**|
|---|---|---|
|**Primary Role**|Proactive planning, alerting & guardrails|Historical analysis, diagnostics & visualization|
|**Question It Answers**|_"Are we going over our agreed spend limit?"_|_"Why did our bill spike, and which service/tag caused it?"_|
|**Data Cadence**|Refreshed 1–3 times daily (approx. every 8–12 hrs)|Refreshed at least once daily (up to 24-hr delay)|
|**Alerting & Automation**|Native email, SNS, Slack, and **Budget Actions** (IAM/SCP/EC2/RDS shutdowns)|Integrated with **AWS Cost Anomaly Detection** (ML anomaly alerts)|
|**Supported Types**|Cost, Usage, RI/Savings Plans coverage & utilization|Unblended, Amortized, Blended, Net Unblended costs|
|**Time Horizon**|Current period & up to 12 months forecasted|Up to 12–14 months historical & up to 12 months forecast|
|**Pricing**|First 2 action-enabled budgets free; then $0.02/day per budget; Budget reports $0.01 each|Free standard console access ($0.01 per Paginated API request)|

### When to Use What (Use Cases)

#### Use AWS Budgets When You Need To:

- **Set Hard Financial Guardrails:** Prevent a Sandbox, QA, or Development account from exceeding a set limit (e.g., alert at 80%, 90%, and 100% of $1,000/month).
    
- **Automate Cost Enforcement (Budget Actions):**
    
    - Automatically apply a restrictive **Service Control Policy (SCP)** or IAM policy to block new resource provisioning when spend hits 100%.
        
    - Automatically stop tagged EC2 instances or RDS databases when monthly cost exceeds budget.
        
- **Track Capacity Commitment Efficiency:** Alert teams when **Savings Plans or Reserved Instance (RI) utilization** falls below 90%, or when coverage drops below a target threshold.
    
- **Monitor Resource Unit Consumption (Usage Budgets):** Track specific non-dollar metrics (e.g., S3 storage GBs, data transfer GBs, or running instance hours).
    

#### Use AWS Cost Explorer When You Need To:

- **Root-Cause Investigation:** Drill down into a sudden month-over-month bill increase using multi-dimensional filters (`Service`, `Linked Account`, `Region`, `Cost Allocation Tag`, `Usage Type`).
    
- **Analyze Amortized Costs:** Break down upfront RI/Savings Plans payments evenly across the commitment term rather than seeing a one-time charge on day 1.
    
- **Receive Right-Sizing & Savings Recommendations:** View AWS-generated recommendations for EC2 instance right-sizing, terminating idle resources, or purchasing Savings Plans.
    
- **Export Custom Financial Reports:** Build chargeback/showback reports grouped by `CostCenter` or `Project` tags for finance and department leads.
    

### Critical Watch-Outs & Pitfalls

- **Neither Tool Is Real-Time (Data Latency Gotcha):**
    
    - Both tools rely on AWS billing pipeline runs, which update **1 to 3 times per day (every 8–24 hours)**.

    - _Watch-out:_ If an engineer accidentally deploys an expensive rogue GPU cluster or an unthrottled Lambda loop, AWS Budgets **will not stop it instantly**. It will only alert after the next billing cycle ingestion. For sub-hour runaway cost mitigation, rely on CloudWatch Metric Alarms (e.g., Billing/EstimatedCharges, CPU, or Request Count) or AWS Lambda throttles.

- **Tag Activation Lag:**
    
    - User-defined cost tags (e.g., `Environment: Prod`) are not visible in Cost Explorer or Budgets until they are explicitly **activated** in the _Billing & Cost Management Console $\rightarrow$ Cost Allocation Tags_. Activation applies only to future billing data; it does not retroactively tag past spend.

- **Forecasted Alerts Need Historical Data:**
    
    - AWS Budgets forecasting requires approximately **5 weeks (35 days)** of historical usage data in the account before predictive breach alerts become statistically reliable.

- **Over-Restricting via Budget Actions:**
    
    - Applying an automated IAM policy or stopping instances via Budget Actions in a **Production** account can cause severe unintended outages. Restrict automated destructive actions to Sandbox and Non-Production environments.

- **Cost Explorer API Costs:**
    
    - Viewing Cost Explorer via the AWS Management Console is free, but calling the `ce:GetCostAndUsage` API programmatically costs **$0.01 per request**. Poorly optimized polling scripts can generate unexpected bills.


### Solutions Architect / Certification Keyword Clues

- If the scenario asks for: _"Set a spending limit"_, _"Automate instance shutdown on budget breach"_, or _"Alert when RI utilization drops below 80%"_ $\rightarrow$ **AWS Budgets**.

- If the scenario asks for: _"Interactive cost visualization"_, _"Find the root cause of an unexpected S3 charge"_, _"View amortized RI costs"_, or _"Identify unused EC2 instances"_ $\rightarrow$ **AWS Cost Explorer**.

- If the scenario asks for: _"ML-powered identification of unusual spending patterns without manual thresholds"_ $\rightarrow$ **AWS Cost Anomaly Detection**.

**Use AWS Organizations to set up a multi-account environment. Organize the accounts into the following Organizational Units (OUs): Security, Infrastructure, Workloads, Suspended and Exceptions** - AWS categorizes the Security OU and the Infrastructure OU as foundational. The foundational OUs contain accounts, workloads, and other AWS resources that provide common security and infrastructure capabilities to secure and support your overall AWS environment.

The Suspended OU is used as a temporary holding area for accounts that are required to have their use suspended either temporarily or permanently.

The Exceptions OU houses an account that requires an exception to the security policies that are applied to your Workloads OU.

AWS recommended OUs and accounts: 

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q3-i1.jpg)

 via - [https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/recommended-ous-and-accounts.html](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/recommended-ous-and-accounts.html)

**Configure an AWS Budget alert to move an AWS account to Exceptions OU if the account reaches a predefined budget threshold. Use Service Control Policies (SCPs) to limit/block resource usage in the Exceptions OU. Configure a Suspended OU to hold workload accounts with retired resources. Use Service Control Policies (SCPs) to limit/block resource usage in the Suspended OU** - AWS Budgets provides the capability to configure cost-saving controls, or actions, that run either automatically on your behalf or by using a workflow approval process. You can use actions to define an explicit response that you want to take when a budget exceeds its action threshold. You can trigger these alerts on actual or forecasted cost and usage budgets.

For the given scenario, the management account can move the member account to restrictive OU (Exceptions OU) after the budget threshold for the member account is met.

Using AWS Budgets actions to move an AWS account to an OU: 

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q3-i2.jpg)

 via - [https://aws.amazon.com/blogs/mt/manage-cost-overruns-part-1/](https://aws.amazon.com/blogs/mt/manage-cost-overruns-part-1/)

**Designate an account within the AWS Organizations organization to be the GuardDuty delegated administrator. Create an SNS topic in this account. Subscribe the security team to the topic so that the security team can receive alerts from GuardDuty via SNS**

When you use GuardDuty with an AWS Organizations organization, you can designate any account within the organization to be the GuardDuty delegated administrator. Only the organization management account can designate GuardDuty delegated administrators.

An account that is designated as a delegated administrator becomes a GuardDuty administrator account, has GuardDuty automatically enabled in the designated Region and is granted permission to enable and manage GuardDuty for all accounts in the organization within that Region. The other accounts in the organization can be viewed and added as GuardDuty member accounts associated with the delegated administrator account.

For the given use case, you can set up an SNS topic in this account and then subscribe the security team to the topic so that the security team can receive alerts from GuardDuty.

Incorrect options:

**Use AWS Organizations to set up a multi-account environment. Organize the accounts into the following Service Control Policies (SCPs): Security, Infrastructure, Workloads, Suspended, and Exceptions. Grant necessary permissions to the accounts by using the SCP guardrails** - Service control policies (SCPs) are a type of organization policy that you can use to manage permissions in your organization. SCPs offer central control over the maximum available permissions for all accounts in your organization. SCPs alone are not sufficient to grant permissions to the accounts in your organization. No permissions are granted by an SCP. <font color="#2DC26B">You cannot organize AWS accounts into Service Control Policies (SCPs). You organize AWS accounts into Organization Units by using AWS Organizations.</font>

**Configure an AWS Cost Explorer alert to move an AWS account to Exceptions OU if the account reaches a predefined budget threshold. Use Service Control Policies (SCPs) to limit/block resource usage in the Exceptions OU. Configure a Suspended OU to hold workload accounts with retired resources. Use Service Control Policies (SCPs) to limit/block resource usage in the Suspended OU** - AWS Cost Explorer lets you explore your AWS costs and usage at both a high level and at a detailed level of analysis, empowering you to dive deeper using several filtering dimensions (e.g., AWS Service, Region, Member Account, etc.). It is not possible to define actionable alerts in AWS Cost Explorer.

**Configure GuardDuty in all member accounts within the AWS Organizations organization. Create an SNS topic in each account. Subscribe the security team to the topic so that the security team can receive alerts from GuardDuty via SNS** - It is inefficient and cumbersome to configure GuardDuty in all member accounts within the AWS Organizations organization. It's better to centrally manage GuardDuty for all AWS accounts by using a GuardDuty delegated administrator account within the AWS Organizations organization.

References:

[https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/suspended-ou.html](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/suspended-ou.html)

[https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)

[https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/benefits-of-using-ous.html](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/benefits-of-using-ous.html)

[https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_organizations.html](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_organizations.html)