A multi-national company operates hundreds of AWS accounts and the CTO wants to rationalize the operational costs. The CTO has mandated a centralized process for purchasing new Reserved Instances (RIs) or modifying existing RIs. Whereas earlier the business units (BUs) would directly purchase or modify RIs in their own AWS accounts independently, now all BUs must be denied independent purchase and the BUs must submit requests to a dedicated central team for purchasing RIs.

As an AWS Certified Solutions Architect Professional, which of the following solutions would you combine to enforce the new process most efficiently? (Select two)

Correct options:

**Make sure that all AWS accounts are assigned organizational units (OUs) within an AWS Organizations structure operating in all features mode**

AWS Organizations has two available feature sets:

All features – This feature set is the preferred way to work with AWS Organizations, and it includes Consolidating Billing features. When you create an organization, enabling all features is the default. With all features enabled, you can use the advanced account management features available in AWS Organizations such as integration with supported AWS services and organization management policies. Policies in AWS Organizations enable you to apply additional types of management to the AWS accounts in your organization. You can use policies when all features are enabled in your organization. Service control policies (SCPs) offer central control over the maximum available permissions for all of the accounts in your organization.

Consolidated Billing features – All organizations support this subset of features, which provides basic management tools that you can use to centrally manage the accounts in your organization. You cannot leverage SCPs in this feature mode.

**Set up a Service Control Policy (SCP) that contains a deny rule to the ec2:PurchaseReservedInstancesOffering and ec2:ModifyReservedInstances actions. Attach the SCP to each organizational unit (OU) of the AWS Organizations structure**

Service control policies (SCPs) are a type of organizational policy that you can use to manage permissions in your organization. SCPs offer central control over the maximum available permissions for all accounts in your organization. SCPs help you to ensure your accounts stay within your organization’s access control guidelines. SCPs alone are not sufficient to grant permissions to the accounts in your organization. No permissions are granted by an SCP. An SCP defines a guardrail or sets limits, on the actions that the account's administrator can delegate to the IAM users and roles in the affected accounts. The administrator must still attach identity-based or resource-based policies to IAM users or roles, or the resources in your accounts to actually grant permissions. SCPs don't affect users or roles in the management account. They affect only the member accounts in your organization.

For the given use case, you can set up an SCP that contains a deny rule to the ec2:PurchaseReservedInstancesOffering and ec2:ModifyReservedInstances actions.

Incorrect options:

**Make sure that all AWS accounts are assigned organizational units (OUs) within an AWS Organizations structure operating in the consolidated billing features mode** - You cannot leverage SCPs in this feature mode, so this option is incorrect.

**Leverage AWS Config to notify on the attachment of an IAM policy that allows access to the ec2:PurchaseReservedInstancesOffering and ec2:ModifyReservedInstances actions** - AWS Config cannot prevent the attachment of an IAM policy that allows access to the ec2:PurchaseReservedInstancesOffering and ec2:ModifyReservedInstances actions. So this option is incorrect for the given requirements.

**Set up an IAM policy in each AWS account with a deny rule to the ec2:PurchaseReservedInstancesOffering and ec2:ModifyReservedInstances actions** - This is a cumbersome and inefficient solution to prevent each of the member AWS accounts from purchasing the RIs. This is not the best fit solution.

References:

[https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html)

[https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html)

[https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)