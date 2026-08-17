A social media company has VPC Flow Logs enabled for its NAT gateway. The security team is seeing Action = ACCEPT for inbound traffic that comes from the public IP address 198.21.200.1 destined for a private EC2 instance. The team must determine whether the traffic represents unsolicited inbound connections from the internet. The first two octets of the VPC CIDR block are 205.1.

Which of the following options can address this requirement?

**Inspect the VPC Flow Logs using the CloudWatch console and select the log group that contains the NAT gateway's ENI and the EC2 instance's ENI. Leverage a query filter with the destination address set as `like 205.1` and the source address set as `like 198.21.200.1`. Execute the stats command to filter the sum of bytes transferred by the source address and the destination address**

NAT gateways managed by AWS don't accept traffic initiated from the internet. However, there are two reasons why the information in your VPC flow logs might appear to indicate that inbound traffic is being accepted from the internet.

1: Inbound internet traffic is permitted by your security group or network access control lists (ACL)

VPC flow logs show inbound internet traffic as accepted if the traffic is permitted by your security group or network ACLs. If network ACLs attached to a NAT gateway don’t explicitly deny traffic from the internet, then the traffic to the NAT gateway appears accepted. However, the traffic isn't actually accepted by the NAT gateway and is dropped. You can use just the first two octets in the search filter to analyze all network interfaces in the VPC, like so:

```
filter (dstAddr like 'xxx.xxx' and srcAddr like 'public IP')
| stats sum(bytes) as bytesTransferred by srcAddr, dstAddr
| limit 10
```

If the query results show traffic on the NAT gateway private IP from the public IP, but not traffic on other private IPs in the VPC. These results confirm that the incoming traffic was unsolicited.

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q14-i1.jpg)

 via - [https://aws.amazon.com/premiumsupport/knowledge-center/vpc-analyze-inbound-traffic-nat-gateway/](https://aws.amazon.com/premiumsupport/knowledge-center/vpc-analyze-inbound-traffic-nat-gateway/)

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q14-i2.jpg)

 via - [https://aws.amazon.com/premiumsupport/knowledge-center/vpc-analyze-inbound-traffic-nat-gateway/](https://aws.amazon.com/premiumsupport/knowledge-center/vpc-analyze-inbound-traffic-nat-gateway/)

Incorrect options:

**Inspect the VPC Flow Logs using the CloudTrail console and select the log group that contains the NAT gateway's ENI and the EC2 instance's ENI. Leverage a query filter with the destination address set as `like 205.1` and the source address set as `like 198.21.200.1`. Execute the stats command to filter the sum of bytes transferred by the source address and the destination address**

**Inspect the VPC Flow Logs using the CloudTrail console and select the log group that contains the NAT gateway's ENI and the EC2 instance's ENI. Leverage a query filter with the source address set as `like 205.1` and the destination address set as `like 198.21.200.1`. Execute the stats command to filter the sum of bytes transferred by the source address and the destination address**

You cannot use the CloudTrail console to analyze the VPC Flow Logs. You need to use the CloudWatch console for this analysis. Therefore both these options are incorrect.

**Inspect the VPC Flow Logs using the CloudWatch console and select the log group that contains the NAT gateway's ENI and the EC2 instance's ENI. Leverage a query filter with the source address set as `like 205.1` and the destination address set as `like 198.21.200.1`. Execute the stats command to filter the sum of bytes transferred by the source address and the destination address** - For the query filter, you need to use the destination address set as `like 205.1` with the source address set as `like 198.21.200.1` and NOT vice-versa.

References:

[https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)

[https://aws.amazon.com/premiumsupport/knowledge-center/vpc-analyze-inbound-traffic-nat-gateway/](https://aws.amazon.com/premiumsupport/knowledge-center/vpc-analyze-inbound-traffic-nat-gateway/)

Domain

Design Solutions for Organizational Complexity