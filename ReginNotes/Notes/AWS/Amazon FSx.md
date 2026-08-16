**Configure a new Amazon FSx for Windows file system with a deployment type of Multi-AZ. Transfer data to the newly created file system using the AWS DataSync service. Point all the file system users to the new location. You can test the failover of your Multi-AZ file system by modifying its throughput capacity**

In a Multi-AZ deployment, Amazon FSx automatically provisions and maintains a standby file server in a different Availability Zone. Any changes written to disk in your file system are synchronously replicated across Availability Zones to the standby. If there is planned file system maintenance or unplanned service disruption, Amazon FSx automatically fails over to the secondary file server, allowing you to continue accessing your data without manual intervention. Multi-AZ file systems are recommended for most production workloads that require high availability of shared Windows file data.

<mark style="background:#fff88f">To migrate your existing files to FSx for Windows File Server file systems, AWS recommends using AWS DataSync</mark>, an online data transfer service designed to simplify, automate, and accelerate copying large amounts of data to and from AWS storage services. <mark style="background:#fff88f">DataSync copies data over the internet or AWS Direct Connect.</mark>

<mark style="background:#fff88f">You can test the failover of your Multi-AZ file system by modifying its throughput capacity.</mark> When you modify your file system's throughput capacity, Amazon FSx switches out the file system's file server. Multi-AZ file systems automatically fail over to the secondary server while Amazon FSx replaces the preferred server file server first. Then the file system automatically fails back to the new primary server and Amazon FSx replaces the secondary file server.

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q5-i1.jpg)

 via - [https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html)

**You can monitor storage capacity and file system activity using Amazon CloudWatch, and monitor end-user actions with file access auditing using Amazon CloudWatch Logs and Amazon Kinesis Data Firehose**

You can monitor storage capacity and file system activity using Amazon CloudWatch. You can monitor end-user actions with file access auditing at any time (during or after the creation of a file system) via the AWS Management Console or the Amazon FSx CLI or API. You can also change the destination for publishing user access events by logging these events to CloudWatch Logs or streaming to Kinesis Data Firehose.

Incorrect options:

**Configure a new Amazon FSx for Windows file system with a deployment type of Single-AZ 1. Transfer data to the newly created file system using the AWS DataSync service. Point all the file system users to the new location** - With Single-AZ file systems, Amazon FSx automatically replicates your data within an Availability Zone (AZ) to protect it from component failure. It continuously monitors for hardware failures and automatically replaces infrastructure components in the event of a failure. Single-AZ 2 is the latest generation of Single-AZ file systems, and it supports both SSD and HDD storage. Single-AZ 1 file systems support SSD storage, Microsoft Distributed File System Replication (DFSR), and the use of custom DNS names. Single-AZ file systems will experience unavailability during file system maintenance, infrastructure component replacement, and when an Availability Zone is unavailable.

Multi-AZ file systems are recommended for most production workloads that require high availability of shared Windows file data. Single-AZ file systems offer a lower price point for workloads that don’t require the high availability of a Multi-AZ solution and that can recover from the most recent file system backup if data is lost.

**You can monitor the file system activity using AWS CloudTrail and monitor end-user actions with file access auditing using Amazon CloudWatch Logs** - This statement is incorrect. You can monitor storage capacity and file system activity using Amazon CloudWatch, monitor all Amazon FSx API calls using AWS CloudTrail, and<mark style="background:#fff88f"> monitor end-user actions with file access auditing using Amazon CloudWatch Logs and Amazon Kinesis Data Firehose.</mark>

**Configure a new Amazon FSx for Windows file system with a deployment type of Multi-AZ. Transfer data to the newly created file system using the AWS DataSync service. Point all the file system users to the new location. You can test the failover of your Multi-AZ file system by modifying the elastic network interfaces associated with your file system** - <mark style="background:#fff88f">You must not modify or delete the elastic network interfaces associated with your file system. Modifying or deleting the network interface can cause a permanent loss of connection between your VPC and your file system</mark>. Therefore this option is incorrect.

References:

[https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html)

[https://docs.aws.amazon.com/fsx/latest/WindowsGuide/migrate-files-fsx.html](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/migrate-files-fsx.html)

[https://aws.amazon.com/fsx/windows/faqs/](https://aws.amazon.com/fsx/windows/faqs/)

[https://docs.aws.amazon.com/fsx/latest/WindowsGuide/limit-access-security-groups.html](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/limit-access-security-groups.html)

[https://aws.amazon.com/blogs/aws/file-access-auditing-is-now-available-for-amazon-fsx-for-windows-file-server/](https://aws.amazon.com/blogs/aws/file-access-auditing-is-now-available-for-amazon-fsx-for-windows-file-server/)