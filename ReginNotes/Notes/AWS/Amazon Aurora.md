#Aurora #ApplicationLoadBalancer #NetworkLoadBalancer



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


**Enable Aurora Auto Scaling for Aurora Replicas. Deploy the application on Amazon EC2 instances configured behind an Auto Scaling Group** - To meet your connectivity and workload requirements, <mark style="background:#fff88f">Aurora Auto Scaling dynamically adjusts the number of Aurora Replicas provisioned for an Aurora DB cluster using single-master replication.</mark> Aurora Auto Scaling enables your Aurora DB cluster to handle sudden increases in connectivity or workload. <mark style="background:#fff88f">When the connectivity or workload decreases, Aurora Auto Scaling removes unnecessary Aurora Replicas so that you don't pay for unused provisioned DB instances.</mark>

You define and apply a <mark style="background:#fff88f">scaling policy to an Aurora DB cluster</mark>. The scaling policy defines the minimum and maximum number of Aurora Replicas that Aurora Auto Scaling can manage. Based on the policy, Aurora Auto Scaling adjusts the number of Aurora Replicas up or down in response to actual workloads, determined by using Amazon CloudWatch metrics and target values.

**Configure EC2 instances behind an Application Load Balancer with Round Robin routing algorithm and sticky sessions enabled** - Your load balancer serves as a <mark style="background:#fff88f">single point of contact for clients and distributes incoming traffic across its healthy registered targets</mark>. You can register each target with one or more target groups.

<mark style="background:#fff88f">By default, the round-robin routing algorithm is used to route requests at the target group level. Round robin is a good choice when the requests and targets are similar, or if you need to distribute requests equally among targets.</mark>

By default, an Application Load Balancer (ALB) routes each request independently to a registered target based on the chosen load-balancing algorithm. However, <mark style="background:#fff88f">you can use the sticky session feature (also known as session affinity) to enable the load balancer to bind a user's session to a specific target</mark>. This ensures that all requests from the user during the session are sent to the same target. This feature is useful for servers that maintain state information to provide a continuous experience to clients.<mark style="background:#fff88f"> To use sticky sessions, the client must support cookies.</mark>

Incorrect options:

**Enable Aurora Auto Scaling for Aurora Writes. Deploy the application on Amazon EC2 instances configured behind an Auto Scaling Group** - <mark style="background:#fff88f">Aurora Auto Scaling is possible for Aurora replicas and not for Aurora writer instances.</mark> Multi-master Aurora Cluster architecture is needed if multiple writers are needed for any use case.

**Configure EC2 instances behind an Application Load Balancer with flow hash routing algorithm and sticky sessions enabled** - The flow <mark style="background:#fff88f">hash routing algorithm can only be used with Network Load Balancers.</mark> So this option is incorrect.

**Configure EC2 instances behind a Network Load Balancer with Least Outstanding Requests routing algorithm and sticky sessions enabled** - This statement is incorrect. Network Load Balancer does not support Least Outstanding Requests routing algorithm. AWS suggests using the Least Outstanding Requests with an ALB when the requests for your application vary in complexity or your targets vary in processing capability.

For TCP traffic, the #NetworkLoadBalancer <mark style="background:#fff88f">selects a target using a flow hash algorithm based on the protocol, source IP address, source port, destination IP address, destination port, and TCP sequence number.</mark> The TCP connections from a client have different source ports and sequence numbers and can be routed to different targets. Each TCP connection is routed to a single target for the life of the connection.

For UDP traffic, the Network Load Balancer selects a target using a flow hash algorithm based on the protocol, source IP address, source port, destination IP address, and destination port. A UDP flow has the same source and destination, so it is consistently routed to a single target throughout its lifetime. Different UDP flows have different source IP addresses and ports, so they can be routed to different targets.

References:

[https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Integrating.AutoScaling.html](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Integrating.AutoScaling.html)

[https://docs.amazonaws.cn/en_us/elasticloadbalancing/latest/application/load-balancer-target-groups.html#modify-routing-algorithm](https://docs.amazonaws.cn/en_us/elasticloadbalancing/latest/application/load-balancer-target-groups.html#modify-routing-algorithm)

[https://docs.amazonaws.cn/en_us/elasticloadbalancing/latest/application/sticky-sessions.html](https://docs.amazonaws.cn/en_us/elasticloadbalancing/latest/application/sticky-sessions.html)

[https://aws.amazon.com/about-aws/whats-new/2019/11/application-load-balancer-now-supports-least-outstanding-requests-algorithm-for-load-balancing-requests/](https://aws.amazon.com/about-aws/whats-new/2019/11/application-load-balancer-now-supports-least-outstanding-requests-algorithm-for-load-balancing-requests/)

[https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)