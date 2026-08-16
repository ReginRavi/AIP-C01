**Use AWS X-Ray to analyze the microservices applications through request tracing. Configure Amazon CloudWatch for monitoring containers, latency, web server requests, and incoming load-balancer requests and create CloudWatch alarms to send out notifications if system latency is increasing**

AWS X-Ray helps developers analyze and debug production, and distributed applications, such as those built using a microservices architecture.

Analyze and debug using X-Ray: 

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q6-i1.jpg)

 via - [https://aws.amazon.com/xray/](https://aws.amazon.com/xray/)

AWS X-Ray creates a map of services used by your application with trace data that you can use to drill into specific services or issues. This provides a view of connections between services in your application and aggregated data for each service, including average latency and failure rates.

X-Ray service map: 

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q6-i2.jpg)

 via - [https://aws.amazon.com/xray/features/](https://aws.amazon.com/xray/features/)

X-Ray Traces: 

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q6-i3.jpg)

 via - [https://aws.amazon.com/xray/features/](https://aws.amazon.com/xray/features/)

Amazon CloudWatch allows you to collect infrastructure metrics from more than 70 AWS services, such as Amazon Elastic Compute Cloud (Amazon EC2), Amazon DynamoDB, Amazon Simple Storage Service (Amazon S3), Amazon ECS, AWS Lambda, Amazon API Gateway, with no action on your part. For example, Amazon EC2 instances automatically publish CPU utilization, data transfer, and disk usage metrics to help you understand state changes. You can use built-in metrics for API Gateway to detect latency or use built-in metrics for AWS Lambda to detect errors or throttles. Likewise, Amazon CloudWatch also allows you to collect application metrics (such as user activity, error metrics or memory used) from your applications to monitor operational performance, troubleshoot issues, and spot trends.

Amazon CloudWatch for monitoring: 

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q6-i4.jpg)

 via - [https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_architecture.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_architecture.html)

Incorrect options:

**Use AWS X-Ray to analyze the microservices applications through request tracing. Configure Amazon EventBridge for monitoring containers, latency, web server requests, and incoming load-balancer requests and create alarms to send out notifications if system latency is increasing**

**Configure Amazon EventBridge for monitoring containers, latency, web server requests, and incoming load-balancer requests and create alarms to send out notifications if system latency is increasing. Use AWS Config to continually assesses, audit, and evaluate the configurations and relationships of your resources and trigger alarms when needed**

Amazon EventBridge is a serverless event bus service that uses the Amazon CloudWatch Events API, but also includes more functionality, like the ability to ingest events from SaaS apps. EventBridge is designed to extend the event model beyond AWS, bringing data from software-as-a-service (SaaS) providers into your AWS environment. This means you can consume events from popular providers such as Zendesk, PagerDuty, and Auth0. You can use these in your applications with the same ease as any AWS-generated event.

For the given use case, you can use Cloudwatch for monitoring containers, latency, web server requests, and incoming load-balancer requests and create CloudWatch alarms to send out notifications if system latency is increasing. Therefore, both these options are incorrect.

**Configure Amazon CloudWatch to monitor and analyze all microservices through request tracing. Enable CloudTrail to log all user activity** - X-Ray can be used to monitor and analyze AWS microservices through request tracing, so this option is incorrect.

References:

[https://aws.amazon.com/cloudwatch/features/](https://aws.amazon.com/cloudwatch/features/)

[https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html)

[https://aws.amazon.com/solutions/case-studies/connectwise/](https://aws.amazon.com/solutions/case-studies/connectwise/)

Domain

Design for New Solutions