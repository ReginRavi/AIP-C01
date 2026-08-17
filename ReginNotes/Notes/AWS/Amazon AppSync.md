#AppSync


**Configure Amazon S3 for hosting the web application while using AWS AppSync for database access services. Use Amazon Simple Queue Service (Amazon SQS) for queuing orders and AWS Lambda for business logic. Use Amazon SQS dead-letter queue for tracking and re-processing failed orders**

Amazon S3 can be configured to host a web application.

AWS AppSync creates serverless GraphQL and Pub/Sub APIs that simplify application development through a single endpoint to securely query, update, or publish data. AWS AppSync creates serverless GraphQL and Pub/Sub APIs that simplify application development through a single endpoint to securely query, update, or publish data.

How AWS AppSync works: 

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q7-i1.jpg)

 via - [https://aws.amazon.com/appsync/](https://aws.amazon.com/appsync/)

Amazon SQS supports dead-letter queues (DLQ), which other queues (source queues) can target for messages that can't be processed (consumed) successfully. Dead-letter queues are useful for debugging your application or messaging system because they let you isolate unconsumed messages to determine why their processing doesn't succeed.

SQS dead-letter queues: 

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q7-i2.jpg)

 via - [https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)

Incorrect options:

**Configure Amazon CloudFront for hosting the website and Amazon API Gateway for database API services. Use Amazon Simple Queue Service (Amazon SQS) for order queuing and AWS Lambda for business logic. Use Amazon SQS long polling for retaining failed orders** - <mark style="background:#fff88f">You cannot use Amazon CloudFront for hosting a website</mark> as the website is hosted on the Cloudfront distribution's underlying origin (such as S3 or an EC2 instance). You cannot use<mark style="background:#fff88f"> Amazon SQS long polling for retaining failed orders.</mark> When the wait time for the `ReceiveMessage` API action is greater than 0, long polling is in effect. Long polling helps reduce the cost of using Amazon SQS by eliminating the number of empty responses and false empty responses. Long polling is a configurable parameter of SQS queues and not a temporary storage space to hold failed orders.

**Use Amazon Lightsail for web hosting with AWS AppSync for database API services. Use Simple Queue Service (Amazon SQS) for order queuing. Use Amazon Elastic Container Service (Amazon ECS) for business logic and use the `visibility timeout` parameter of Amazon SQS to retain the failed orders** - <mark style="background:#fff88f">You cannot use the `visibility timeout` parameter of Amazon SQS to retain the failed orders</mark>. Immediately after a message is received in an SQS queue, it remains in the queue. To prevent other consumers from processing the message again, Amazon SQS sets a `visibility timeout`, a period during which Amazon SQS prevents other consumers from receiving and processing the message. `Visibility timeout` is a configurable parameter of SQS queues and not a temporary storage space to hold failed orders.

**Use AWS Elastic Beanstalk for hosting the web application and Amazon API Gateway for database API services. Use Kinesis Data Streams for queuing orders and AWS Lambda to build business logic. Configure an Amazon S3 bucket for retaining failed orders on an hourly basis** - Amazon Kinesis Streams allows real-time processing of streaming big data and the ability to read and replay records to multiple Amazon Kinesis Applications. Amazon SQS offers a reliable, highly-scalable hosted queue for storing messages as they travel between applications or microservices. It moves data between distributed application components and helps you decouple these components.

You should not use S3 to retain failed orders on an hourly basis. This would result in too many small objects (1 object for each failed order) on S3 which need to be written and read multiple times. In addition, it would be cumbersome to keep track of the failed orders and do the root cause analysis. You could run SQL queries via Athena on this underlying data in S3. However, it would turn out to be costly and inefficient while querying small objects via Athena. Therefore, this use case is an anti-pattern for S3.

References:

[https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html)

[https://aws.amazon.com/appsync/](https://aws.amazon.com/appsync/)

[https://aws.amazon.com/sqs/faqs/](https://aws.amazon.com/sqs/faqs/)

[https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/)

[https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance-design-patterns.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance-design-patterns.html)