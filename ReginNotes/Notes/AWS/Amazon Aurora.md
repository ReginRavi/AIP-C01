**Configure the Aurora MySQL DB cluster to publish slow query and error logs to Amazon CloudWatch Logs**

You can configure your Aurora MySQL DB cluster to publish general, slow, audit, and error log data to a log group in Amazon CloudWatch Logs. With CloudWatch Logs, you can perform real-time analysis of the log data, and use CloudWatch to create alarms and view metrics. You can use CloudWatch Logs to store your log records in highly durable storage.

To publish logs to CloudWatch Logs, the respective logs must be enabled. <font color="#2DC26B">Error logs are enabled by default, but you must enable the other types of logs explicitly. </font><mark style="background:#fff88f">The slow query logs and error logs can be used to identify the root cause behind the given issue.</mark>

**Install and configure an Amazon CloudWatch Logs agent on the EC2 instances to send the application logs to CloudWatch Logs**

You can collect metrics and logs from Amazon EC2 instances and on-premises servers with the CloudWatch agent. The unified CloudWatch agent enables you to collect internal system-level metrics from Amazon EC2 instances across operating systems. The metrics can include in-guest metrics, in addition to the metrics for EC2 instances. You can collect logs from Amazon EC2 instances and on-premises servers, running either Linux or Windows Server. The application logs (via the CloudWatch logs) can be used to identify the root cause behind the given issue.

**Set up the AWS X-Ray SDK to trace incoming HTTP requests on the EC2 instances as well as set up tracing of SQL queries with the X-Ray SDK for Java**

You can use the X-Ray SDK to trace incoming HTTP requests that your application serves on an EC2 instance. Use a Filter to instrument incoming HTTP requests. When you add the X-Ray servlet filter to your application, the X-Ray SDK for Java creates a segment for each sampled request. This segment includes timing, method, and disposition of the HTTP request. You can also instrument your SQL database queries by adding the X-Ray SDK for Java JDBC interceptor to your data source configuration. X-Ray tracing for the HTTP requests as well as the SQL queries can help in identifying the root cause behind the given issue.

Incorrect options:

**Use CloudTrail and configure a trail to deliver Amazon Aurora query activity to an Amazon S3 bucket. Process and analyze these real-time log streams using Amazon Kinesis Data Streams** - You can use CloudTrail to view, search, download, archive, analyze, and respond to account activity across your AWS infrastructure. You can identify who or what took which action, what resources were acted upon, when the event occurred, and other details to help you analyze and respond to activity in your AWS account. CloudTrail provides a record of actions taken by a user, role, or AWS service in Amazon Aurora. <mark style="background:#fff88f">However, CloudTrail does not capture any query activity in Aurora, so this option is incorrect.</mark>

**Enable `detailed monitoring` for Amazon EC2 instances to send data points to CloudWatch every minute. Track the metric 'CPUUtilization' to know when the auto-scaling process can kick in** - Tracking the 'CPUUtilization' parameter is irrelevant to the given use case as it would not point to the root cause behind the given issue.

**Enable `Aurora lab mode` which will then publish all logs and activity on Aurora DB to CloudWatch logs** - Aurora lab mode is used to enable Aurora features that are available in the current Aurora database version but are not enabled by default. These features are tested in development/test environments. `Aurora lab mode` is not relevant for capturing the log activity of Aurora DB. This option has been added as a distractor.

References:

[https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)

[https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.CloudWatch.html](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.CloudWatch.html)

[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html)

[https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-java-filters.html](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-java-filters.html)

[https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-java-sqlclients.html](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-java-sqlclients.html)