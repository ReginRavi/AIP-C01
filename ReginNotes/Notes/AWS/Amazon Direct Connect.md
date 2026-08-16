**Use AWS Direct Connect along with a site-to-site VPN to establish a connection between the data center and AWS Cloud**

AWS Direct Connect is a cloud service solution that makes it easy to establish a dedicated network connection from your premises to AWS. AWS Direct Connect lets you establish a dedicated network connection between your network and one of the AWS Direct Connect locations.

With AWS Direct Connect plus VPN, you can combine one or more AWS Direct Connect dedicated network connections with the Amazon VPC VPN. This combination provides an IPsec-encrypted private connection that also reduces network costs, increases bandwidth throughput, and provides a more consistent network experience than internet-based VPN connections. This solution combines the AWS managed benefits of the VPN solution with low latency, increased bandwidth, more consistent benefits of the AWS Direct Connect solution, and an end-to-end, secure IPsec connection. Therefore, AWS Direct Connect plus VPN is the correct solution for this use-case.

AWS Direct Connect Plus VPN: 

![](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/images/image10.png)

 via - [https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-vpn.html](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-vpn.html)

Incorrect options: **Use site-to-site VPN to establish a connection between the data center and AWS Cloud** - AWS Site-to-Site VPN enables you to securely connect your on-premises network or branch office site to your Amazon Virtual Private Cloud (Amazon VPC). A VPC VPN Connection utilizes IPSec to establish encrypted network connectivity between your intranet and Amazon VPC over the Internet. VPN Connections are a good solution if you have an immediate need, have low to modest bandwidth requirements, and can tolerate the inherent variability in Internet-based connectivity.

However,<mark style="background:#fff88f"> Site-to-site VPN cannot provide low latency and high throughput connection,</mark> therefore this option is ruled out.

**Use VPC transit gateway to establish a connection between the data center and AWS Cloud** - A transit gateway is a network transit hub that you can use to interconnect your virtual private clouds (VPC) and on-premises networks. <mark style="background:#fff88f">A transit gateway by itself cannot establish a low latency and high throughput connection </mark>between a data center and AWS Cloud. Hence this option is incorrect.

**Use AWS Direct Connect to establish a connection between the data center and AWS Cloud** - <mark style="background:#fff88f">AWS Direct Connect by itself cannot provide an encrypted connection</mark> between a data center and AWS Cloud, so this option is ruled out.

References: [https://aws.amazon.com/directconnect/](https://aws.amazon.com/directconnect/)

[https://docs.aws.amazon.com/directconnect/latest/UserGuide/encryption-in-transit.html](https://docs.aws.amazon.com/directconnect/latest/UserGuide/encryption-in-transit.html)

[https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-vpn.html](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-vpn.html)