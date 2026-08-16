**Set up an interface VPC endpoint for Kinesis Data Streams in the VPC. Ensure that the VPC endpoint policy allows traffic from the applications**

You can use an interface VPC endpoint to keep traffic between your Amazon VPC and Kinesis Data Streams from leaving the Amazon network. <font color="#2DC26B">Interface VPC endpoints don't require an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection</font>. <mark style="background:#fff88f">Interface VPC endpoints are powered by AWS PrivateLink</mark>, an AWS technology that enables private communication between AWS services using an elastic network interface with private IPs in your Amazon VPC. You do not need to change the settings for your streams, producers, or consumers. Simply create an interface VPC endpoint for your Kinesis Data Streams traffic from and to your Amazon VPC-based applications to start flowing through the interface VPC endpoint.

VPC endpoint policies enable you to control access by either attaching a policy to a VPC endpoint or by using additional fields in a policy that is attached to an IAM user, group, or role to restrict access to only occur via the specified VPC endpoint. These policies can be used to restrict access to specific streams to a specified VPC endpoint when used in conjunction with the IAM policies to only grant access to Kinesis data stream actions via the specified VPC endpoint.

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q2-i1.jpg)

 via - [https://docs.aws.amazon.com/streams/latest/dev/vpc.html](https://docs.aws.amazon.com/streams/latest/dev/vpc.html)

Incorrect options:

**Set up an interface VPC endpoint for Kinesis Data Streams in the VPC. Ensure that the applications have the required IAM permissions to use the interface VPC endpoint** - Although you can use an IAM policy to restrict access to specific streams to a specified VPC endpoint by only granting access to Kinesis data stream actions via the specified VPC endpoint. However, you need to make changes in the code for the different applications to assume the relevant IAM role and then make changes in the permissions policy attached to the IAM role to grant access to Kinesis Data Streams via the VPC endpoint. This is not an elegant solution when compared to just using the VPC endpoint policy.

**Set up a gateway VPC endpoint for Kinesis Data Streams in the VPC. Ensure that the VPC endpoint policy allows traffic from the applications**

**Set up a gateway VPC endpoint for Kinesis Data Streams in the VPC. Ensure that the applications have the required IAM permissions to use the gateway VPC endpoint**

There are three types of VPC endpoints. You must create the type of VPC endpoint that's required by the endpoint service.

Interface - Create an interface endpoint to send traffic to endpoint services that use a Network Load Balancer to distribute traffic. Traffic destined for the endpoint service is resolved using DNS.

GatewayLoadBalancer - Create a Gateway Load Balancer endpoint to send traffic to a fleet of virtual appliances using private IP addresses. You route traffic from your VPC to the Gateway Load Balancer endpoint using route tables. The Gateway Load Balancer distributes traffic to the virtual appliances and can scale with demand.

Gateway - Create a gateway endpoint to send traffic to Amazon S3 or DynamoDB using private IP addresses. You route traffic from your VPC to the gateway endpoint using route tables. Gateway endpoints do not enable AWS PrivateLink.

<mark style="background:#fff88f">You cannot set up a gateway VPC endpoint for Kinesis Data Streams. Gateway VPC endpoint is only supported for S3 and DynamoDB.</mark> Therefore, both these options are incorrect.

References:

[https://docs.aws.amazon.com/streams/latest/dev/vpc.html](https://docs.aws.amazon.com/streams/latest/dev/vpc.html)

[https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html)