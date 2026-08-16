A SaaS company delivers a multi-tenant platform for healthcare record management using shared Amazon DynamoDB tables and AWS Lambda functions. Each healthcare provider (tenant) sends a unique provider_id as part of every request. The company wants to implement a tiered pricing model that bills each tenant based on their actual consumption of DynamoDB resources, including both read and write activity. The team already collects AWS Cost and Usage Reports (CUR) in a centralized billing account and wants to use this data to drive tenant-level chargebacks. They are looking for the most accurate, cost-effective, and low-maintenance approach for tracking and allocating DynamoDB usage costs per tenant.

Which solution best meets the company's requirements with the least operational effort?

**Update Lambda function logic to log provider_id, estimated RCUs and WCUs per request, and metadata in structured JSON format to Amazon CloudWatch Logs. Schedule a separate Lambda function to process these logs, aggregate usage per tenant, and retrieve the total monthly DynamoDB spend via the AWS Cost Explorer API. Use the proportion of per-tenant usage to allocate DynamoDB costs accurately**

This is the only option that offers both granularity and minimal operational effort. Here, the Lambda functions are instrumented to log structured JSON entries for each request, including the provider_id, RCUs, WCUs, and any relevant metadata. These logs are stored in Amazon CloudWatch Logs. A scheduled Lambda function is then used to parse the logs, aggregate the read/write usage for each tenant, and retrieve the total monthly DynamoDB charges via the AWS Cost Explorer API. The proportional usage per tenant is applied to the overall cost to calculate precise tenant-wise expenses. This method ensures high accuracy, supports long-term traceability through structured logs, leverages the CUR for total spend, and avoids the need for complex data pipelines or tagging hacks. It’s cost-effective, scalable, and aligns perfectly with the company’s goals.

Optimizing Cost Per Tenant Visibility in SaaS Solutions: 

![](https://d2908q01vomqb2.cloudfront.net/77de68daecd823babbb58edb1c8e14d7106e83bb/2023/02/24/Figure-2_Capturing-Tentant-Data.png)

 via - [https://aws.amazon.com/blogs/apn/optimizing-cost-per-tenant-visibility-in-saas-solutions/](https://aws.amazon.com/blogs/apn/optimizing-cost-per-tenant-visibility-in-saas-solutions/)

Incorrect options:

**Enhance the Lambda functions to emit custom metrics to Amazon CloudWatch using the PutMetricData API. Track provider_id, estimated RCUs and WCUs per request, and create metric filters for each tenant. Use CloudWatch metric math and dashboards to aggregate usage. Combine this with DynamoDB pricing to estimate tenant-level cost** - This approach suggests using the PutMetricData API in AWS Lambda to emit custom CloudWatch metrics for each tenant, with dimensions like provider_id, read capacity units (RCUs), and write capacity units (WCUs) consumed. CloudWatch dashboards and metric math can be configured to visualize tenant-specific usage patterns. While this method provides near real-time observability and minimal architectural changes, it is not ideal for long-term cost allocation and billing purposes. CloudWatch metrics are not integrated with AWS Cost and Usage Reports (CUR), making it difficult to validate historical billing data or maintain auditability. Additionally, there is added cost and complexity associated with storing and querying high-cardinality metrics over long retention periods. Hence, this solution lacks the robustness and long-term traceability needed for accurate chargeback.

**Add cost allocation tags with provider_id to each DynamoDB table and activate the tag in the Billing and Cost Management console. Modify the Lambda functions to log the provider_id in CloudWatch Logs. Use the Cost and Usage Reports (CUR) to filter by tags and analyze tenant-level consumption and cost** - This solution proposes assigning cost allocation tags with the key provider_id to DynamoDB tables and activating those tags in the AWS Billing and Cost Management console. The idea is to then use these tags within the CUR to analyze tenant-specific DynamoDB usage. However, this approach is flawed because <mark style="background:#fff88f">all tenants share the same DynamoDB table, and AWS tagging is applied at the resource level, not at the per-request or per-tenant level</mark>. As a result, tagging the table does not distinguish between different tenants’ usage patterns. Logging provider_id in CloudWatch Logs does not influence cost allocation in CUR either. Therefore, while the approach sounds simple, it fundamentally fails to provide the tenant-level granularity that the billing system requires.

**Enable DynamoDB Streams and configure a separate Lambda function to consume the stream, extracting the provider_id and size of each write. Aggregate write-based activity per tenant and map it against total DynamoDB spend** - This option involves enabling DynamoDB Streams to capture write operations and using a separate Lambda function to extract the provider_id and relevant write metadata from each stream record. The data is then aggregated to estimate tenant-wise write activity, which is mapped to the total DynamoDB bill. While this method provides insight into write-heavy workloads, it has a critical flaw: it does not account for read activity, which is also a major component of DynamoDB billing. Consequently, tenants with significant read activity could be underbilled or overlooked entirely. Moreover, <mark style="background:#fff88f">integrating Streams adds complexity and overhead,</mark> and the analysis is limited to write operations only. As such, this solution provides an incomplete and potentially inaccurate view of tenant costs, making it unsuitable for a fair and comprehensive billing model.

References:

[https://aws.amazon.com/blogs/apn/optimizing-cost-per-tenant-visibility-in-saas-solutions/](https://aws.amazon.com/blogs/apn/optimizing-cost-per-tenant-visibility-in-saas-solutions/)

[https://aws.amazon.com/aws-cost-management/aws-cost-explorer/](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)

[https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html)

[https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html)

[https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html)

[https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html)

Domain

Design for New Solutions