AWS Config allows you to manage AWS Config rules <mark style="background:#fff88f">across all AWS accounts within an organization.</mark> You can:

Centrally create, update, and delete AWS Config rules across all accounts in your organization.

Deploy a common set of AWS Config rules across all accounts and specify accounts where AWS Config rules should not be created.

Use the APIs from the management account in AWS Organizations to enforce governance by ensuring that the underlying AWS Config rules are not modifiable by your organization’s member accounts.

If a new account joins an organization, the rule or conformance pack is deployed to that account. When an account leaves an organization, the rule or conformance pack is removed.

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q16-i1.jpg)

 via - [https://docs.aws.amazon.com/config/latest/developerguide/config-rule-multi-account-deployment.html](https://docs.aws.amazon.com/config/latest/developerguide/config-rule-multi-account-deployment.html)

AWS Config allows you to remediate noncompliant resources that are evaluated by AWS Config Rules. AWS Config applies remediation using AWS Systems Manager Automation documents. These documents define the actions to be performed on noncompliant AWS resources evaluated by AWS Config Rules. You can associate SSM documents by using AWS Management Console or by using APIs. To apply remediation on non-compliant resources, you can either choose the remediation action you want to associate from a prepopulated list or create your own custom remediation actions using SSM documents. AWS Config provides a recommended list of remediation actions in the AWS Management Console.

AWS CloudFormation StackSets extends the capability of CloudFormation stacks by enabling you to create, update, or delete stacks across multiple accounts and AWS Regions with a single operation. Using an administrator account, you define and manage an AWS CloudFormation template, and use the template as the basis for provisioning stacks into selected target accounts across specified AWS Regions.

**Use AWS Firewall Manager to manage AWS WAF rules across accounts in the organization. Leverage AWS Systems Manager Parameter Store to store account numbers and OUs. Update AWS Systems Manager Parameter Store as needed to add or remove accounts or OUs. Create cross-account IAM roles in member accounts with permissions to create and update AWS WAF rules. Create a Lambda function to assume IAM roles in the management account to create and update AWS WAF rules in the member accounts** - This option involves significant manual work every time an account is added/removed from the organization. You need to update the items in Systems Manager Parameter Store and further update the Lambda to assume the role for the new account. Hence this option is incorrect.

**Use AWS Control Tower to manage AWS WAF rules across accounts in the organization. Leverage AWS Secrets Manager to store account numbers and OUs. Update AWS Secrets Manager as needed to add or remove accounts or OUs. Create cross-account IAM roles in member accounts with permissions to create and update AWS WAF rules. Create a Lambda function to assume IAM roles in the management account to create and update AWS WAF rules in the member accounts** - This option involves significant manual work every time an account is added/removed from the organization. You need to update the items in Secrets Manager and further update the Lambda to assume the role for the new account. Hence this option is incorrect.

**Use AWS Security Hub to manage AWS WAF rules across accounts in the organization. Leverage AWS KMS to store account numbers and OUs. Update AWS KMS as needed to add or remove accounts or OUs. Create IAM users in member accounts. Allow AWS Firewall Manager in the management account to use the access key and secret access key to create and update AWS WAF rules in the member accounts** - This option has been added as a distractor. <mark style="background:#fff88f">You cannot use AWS Security Hub to manage AWS WAF rules across accounts in the organization</mark>, rather you need to use AWS Firewall Manager to accomplish this. AWS KMS is a managed service that helps you more easily create and control the keys used for cryptographic operations. The service provides a highly available key generation, storage, management, and auditing solution for you to encrypt or digitally sign data within your own applications or control the encryption of data across AWS services. You cannot use AWS KMS to store account numbers and OUs.

References:

[https://docs.aws.amazon.com/config/latest/developerguide/config-rule-multi-account-deployment.html](https://docs.aws.amazon.com/config/latest/developerguide/config-rule-multi-account-deployment.html)

[https://aws.amazon.com/about-aws/whats-new/2019/12/aws-security-hub-integrates-with-aws-firewall-manager/](https://aws.amazon.com/about-aws/whats-new/2019/12/aws-security-hub-integrates-with-aws-firewall-manager/)

[https://docs.aws.amazon.com/config/latest/developerguide/remediation.html](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html)

[https://aws.amazon.com/premiumsupport/knowledge-center/lambda-function-assume-iam-role/](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-function-assume-iam-role/)

Domain

Design Solutions for Organizational Complexity