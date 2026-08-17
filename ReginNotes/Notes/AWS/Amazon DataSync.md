**AWS DataSync** is an online, high-speed data transfer and synchronization service that automates and accelerates moving active datasets between on-premises storage, other cloud providers (Azure, GCP), and AWS storage services (Amazon S3, Amazon EFS, and Amazon FSx).

### Core Characteristics & Capabilities

- **High-Speed Network Protocol:** Uses a purpose-built, multi-threaded transfer protocol with inline compression and sparse-file detection, making it up to **10x faster** than open-source tools like `rsync` or custom scripts.

- **Full Data Integrity Verification:** Automatically calculates checksums during transfer and verifies them at the destination to prevent silent data corruption.

- **Incremental Synchronization:** After the initial baseline copy, it transfers only changed/new files (delta sync).

- **Metadata & Permission Preservation:** Retains POSIX permissions, ownership (UID/GID), timestamps, and Windows ACLs (Access Control Lists).

- **End-to-End Encryption:** Encrypts data in transit via TLS 1.2/1.3 and supports AWS KMS encryption at rest.

- **Bandwidth Throttling & Scheduling:** Enables task scheduling (cron-based) and bandwidth limits so business network traffic is not saturated.

### Is it Serverless? Who Manages the Infrastructure?

|**Dimension**|**AWS-to-AWS & Cross-Cloud (S3/Azure/GCP)**|**On-Premises to AWS**|
|---|---|---|
|**Architecture**|**100% Serverless & Agentless**|**Hybrid Managed Model**|
|**Agent / VM Required?**|**No agent required**. AWS manages compute and network endpoints entirely in the cloud.|**Yes**. You deploy a lightweight **DataSync Agent** (VM on VMware ESXi, Hyper-V, KVM, or EC2).|
|**Infrastructure Management**|**AWS fully manages** the scaling, compute, patching, and transfer pipelines.|**Shared:** You provide the on-prem VM hypervisor resources; AWS manages the agent software updates, encryption, and sync tasks.|

### Operational Overhead: High or Least?

AWS DataSync represents the **LEAST operational overhead** choice for large-scale, automated network file transfers compared to manual alternatives.

- **Why it has minimal overhead:**

    - Replaces complex custom Python/Bash scripts, retry logic, error alerting, and cron jobs.

    - Native integration with **AWS CloudWatch** (metrics, task logging, and alarms) and **AWS EventBridge** (event-driven triggers).

    - No servers, storage clusters, or tuning parameters to maintain on AWS.


### Pricing & Cost Model

- **Pay-per-GB Transferred:** Billed at a flat rate of **$0.0125 per GB** transferred (~$12.50 per TB).

- **Enhanced Mode (Optional):** Small per-task execution fee (~$0.60 per run) for parallel scanning across massive datasets (billions of objects).

- **No Minimum Charges & No Upfront Costs:** You only pay for what you synchronize.

- **Standard AWS Storage Costs Apply:** Regular S3 API requests (`PUT`/`GET`), EFS throughput, and cross-region egress charges apply as normal.


### Supported Sources and Destinations

```
┌────────────────────────────────────────────────────────┐
│                        SOURCES                         │
├────────────────────────────────────────────────────────┤
│ • On-Premises: NFS, SMB, HDFS, Object Storage          │
│ • Other Clouds: Azure Blob/Files, Google Cloud Storage │
│ • AWS Storage: S3, EFS, FSx (Windows/Lustre/ONTAP/ZFS) │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼ (AWS DataSync via TLS)
┌────────────────────────────────────────────────────────┐
│                      DESTINATIONS                      │
├────────────────────────────────────────────────────────┤
│ • Amazon S3 (All storage classes, including Glacier)   │
│ • Amazon EFS (Elastic File System)                     │
│ • Amazon FSx (Windows File Server, Lustre, ONTAP, ZFS) │
└────────────────────────────────────────────────────────┘
```

### When to Use: High-Yield Scenarios (SAP-C02 Exam Triggers)

|**Scenario / Use Case**|**Why DataSync is the Best Choice**|
|---|---|
|**Active On-Premises NAS Migration to S3 / EFS / FSx**|Moves active data over Direct Connect or Internet while preserving POSIX permissions and Windows ACLs with minimal cutover downtime.|
|**Periodic Data Replication & Offsite Backups**|Scheduled synchronization of local file systems directly into cold storage like S3 Glacier Flexible / Deep Archive.|
|**Cross-Cloud Ingestion (Azure Blob / GCP $\rightarrow$ S3)**|Fully agentless migration from third-party object stores into AWS data lakes without building custom ETL pipelines.|
|**Inter-Region / Inter-Account AWS Storage Sync**|Synchronizing EFS-to-EFS or FSx-to-FSx across AWS regions for Disaster Recovery (DR) and cross-account data sharing.|
|**Hybrid In-Cloud Processing**|Regularly pushing on-prem sensor/genomics/financial datasets into S3 or FSx for Lustre for fast EC2/EMR batch processing, then syncing results back.|

### AWS DataSync vs. Other AWS Migration & Storage Services

| **Requirement / Exam Trigger** | **AWS DataSync**                                                                                     | **AWS Snowball / Snowcone**                                             | **AWS Storage Gateway**                                               | **AWS Transfer Family**                                       |
| ------------------------------ | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------- |
| **Transfer Mechanism**         | **Online network sync** (Direct Connect / Internet)                                                  | **Offline physical appliance** (shipped via courier)                    | **Hybrid local cache** with continuous live background sync           | **Managed protocols** (SFTP, FTPS, FTP, AS2) for B2B partners |
| **Best Scenario**              | Bandwidth is available ($\ge 100\text{ Mbps}$ to $10\text{ Gbps}$), recurring or one-time batch sync | Bandwidth is limited / slow ($>10\text{ TB}$ to PBs over poor networks) | On-prem apps need low-latency local disk access to cloud S3/EBS files | External clients upload files via SFTP directly into S3/EFS   |
| **Real-Time Client Access**    | No (task-based batch sync)                                                                           | No (offline snapshot)                                                   | **Yes** (active local NFS/SMB/iSCSI mount)                            |                                                               |
**Leverage AWS DataSync to transfer the biological data to Amazon S3. Use S3 events to trigger an AWS Lambda function that starts an AWS Step Functions workflow for orchestrating an AWS Batch job that processes the biological data**

AWS DataSync is an online data movement and discovery service that simplifies and accelerates data migrations to AWS as well as moving data between on-premises storage, edge locations, other clouds, and AWS Storage. You can use DataSync to migrate active data to AWS, archive data to free up on-premises storage capacity, replicate data to AWS for business continuity, or transfer data to the cloud for analysis and processing.

For data transfer between on-premises and AWS Storage services, a single DataSync task is capable of fully utilizing a 10 Gbps network link. Since each workflow job consumes around 100GB of data and the company sees approximately 20 runs every day, DataSync can easily handle such active data transfer workloads. For the given use case, you can then configure an S3 event to trigger an AWS Lambda function that starts an AWS Step Functions workflow for orchestrating an AWS Batch job that processes the biological data.

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q19-i1.jpg)

 via - [https://aws.amazon.com/datasync/faqs/](https://aws.amazon.com/datasync/faqs/)

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q19-i2.jpg)

 via - [https://aws.amazon.com/datasync/faqs/](https://aws.amazon.com/datasync/faqs/)

Incorrect options:

**Leverage AWS Data Pipeline to transfer the biological data to Amazon S3. Use S3 events to trigger an AWS Step Functions workflow for orchestrating an AWS Batch job that processes the biological data** - You cannot trigger an AWS Step Function directly from an S3 event, so this option is incorrect.

**Leverage AWS Data Pipeline to transfer the biological data to Amazon S3. Use S3 events to trigger an Amazon EC2 Auto Scaling group to launch custom-AMI EC2 instances to process the biological data** - You cannot trigger an Amazon EC2 Auto Scaling group directly from an S3 event, so this option is incorrect.

**Leverage AWS Storage Gateway file gateway to transfer the biological data to Amazon S3. Use S3 events to trigger an AWS Lambda function that starts an AWS Step Functions workflow for orchestrating an AWS Batch job that processes the biological data** - You should use AWS DataSync to migrate existing or active data to Amazon S3 and use the File Gateway configuration of AWS Storage Gateway to retain access to the migrated data and for ongoing updates from your on-premises file-based applications. Since the data processing workflow/application is being migrated from on-premises to AWS Cloud, you no longer have any on-premises applications that need to access the processed data from AWS Cloud. So this option is incorrect.

References:

[https://aws.amazon.com/datasync/](https://aws.amazon.com/datasync/)

[https://aws.amazon.com/datasync/faqs/](https://aws.amazon.com/datasync/faqs/)

_____
A company manages a healthcare diagnostics application that writes thousands of lab images to a mounted NFS file system each night from 10 PM - 5 AM. The company wants to migrate this application from its on-premises data center to AWS Cloud over a private network. The company has already established an AWS Direct Connect connection to AWS to facilitate this migration. This application is slated to be moved to Amazon EC2 instances with the Elastic File System (Amazon EFS) file system as the storage service.

Which of the following represents the MOST optimal way of replicating all images to the cloud before the application is fully migrated to the cloud?

 **Deploy an AWS DataSync agent to an on-premises server that has access to the NFS file system. Send data over the Direct Connect connection to an AWS PrivateLink interface VPC endpoint for Amazon EFS by using a private VIF. Configure a DataSync scheduled task to send the images to the EFS file system every night**

You can use VPC endpoints to ensure data transferred between your AWS DataSync agent, either deployed on-premises or in-cloud, doesn't traverse the public internet or need public IP addresses. Using VPC endpoints increases the security of your data by keeping network traffic within your Amazon Virtual Private Cloud (Amazon VPC). VPC endpoints for DataSync are powered by AWS PrivateLink, a highly available, scalable technology that enables you to privately connect your VPC to supported AWS services.

The DataSync agent transfers data between your storage and AWS. In most situations, you deploy the agent as a virtual machine in the same local network as your source storage. This approach minimizes network overhead associated with transferring data by using network protocols such as Network File System (NFS) and Server Message Block (SMB) or when accessing your object storage that's compatible with the Amazon S3 API. This setup is common regardless of the endpoint type you use to connect your agent to AWS.

When you use a VPC endpoint, your DataSync agent communicates directly with AWS without crossing the public internet. Data is transferred using AWS Direct Connect or a virtual private network (VPN). The private IP addresses that DataSync creates for the transfer are accessible only from inside your VPC.

Reference architecture of using DataSync with VPC endpoints: 

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q8-i1.jpg)

 via - [https://docs.aws.amazon.com/datasync/latest/userguide/datasync-in-vpc.html](https://docs.aws.amazon.com/datasync/latest/userguide/datasync-in-vpc.html)

Incorrect options:

**Create an NFS file share using the AWS Storage Gateway file gateway. Mount your NFS file share on a drive on your client and map it to your Amazon S3 bucket. Configure an AWS Lambda function to process event notifications from Amazon S3 and copy the images from Amazon S3 to the EFS file system** - <mark style="background:#fff88f">AWS Storage Gateway provides seamless access to data in hybrid architectures. When the entire application is being moved to AWS Cloud, AWS Storage Gateway is not the best fit for the given use case</mark>. In addition, the data is initially copied to S3 and then replicated into EFS, thereby making the process inefficient.

**Define a cron job on the on-premises system to run the AWS s3 sync command from the on-premises file system to Amazon S3. Use the Amazon S3 Event Notifications to call a Lambda function that will copy the images from the S3 bucket to the EFS file system** - The data is initially copied to S3 and then replicated into EFS, thereby making the process inefficient.

**Deploy an AWS DataSync agent to an on-premises server that has access to the NFS file system. Connect to AWS VPC endpoint for EFS over a public VIF of the Direct Connect connection. Configure a DataSync scheduled task to send the images to the EFS file system every night** - A VPC endpoint allows you to privately connect your VPC to supported AWS services without requiring an internet gateway or a NAT device, VPN connection, or AWS Direct Connect connection. A public virtual interface (VIF) can access all AWS public services using public IP addresses. You cannot leverage public VIF to access the VPC endpoint for EFS. Therefore this option is incorrect.

References:

[https://docs.aws.amazon.com/datasync/latest/userguide/datasync-in-vpc.html](https://docs.aws.amazon.com/datasync/latest/userguide/datasync-in-vpc.html)

[https://aws.amazon.com/blogs/storage/transferring-files-from-on-premises-to-aws-and-back-without-leaving-your-vpc-using-aws-datasync/](https://aws.amazon.com/blogs/storage/transferring-files-from-on-premises-to-aws-and-back-without-leaving-your-vpc-using-aws-datasync/)

**Use AWS DataSync to automate and accelerate online data transfers to the given AWS storage services**

AWS DataSync is an online data transfer service that simplifies, automates, and accelerates copying large amounts of data to and from AWS storage services over the internet or AWS Direct Connect.

AWS DataSync fully automates and accelerates moving large active datasets to AWS, up to 10 times faster than command-line tools. It is natively integrated with Amazon S3, Amazon EFS, Amazon FSx for Windows File Server, Amazon CloudWatch, and AWS CloudTrail, which provides seamless and secure access to your storage services, as well as detailed monitoring of the transfer.

DataSync uses a purpose-built network protocol and scale-out architecture to transfer data. A single DataSync agent is capable of saturating a 10 Gbps network link. DataSync fully automates the data transfer. It comes with retry and network resiliency mechanisms, network optimizations, built-in task scheduling, monitoring via the DataSync API and Console, and CloudWatch metrics, events, and logs that provide granular visibility into the transfer process. DataSync performs data integrity verification both during the transfer and at the end of the transfer.

How DataSync Works 

![](https://d1.awsstatic.com/cloud-storage/Storage/aws-datasync-how-it-works-diagram-s3-efs-fsx.c26c66393dc4e433369ee9947f39e9c54cd338bb.png)

 via - [https://aws.amazon.com/datasync/](https://aws.amazon.com/datasync/)

Incorrect options:

**Use AWS Snowball Edge Storage Optimized device to automate and accelerate online data transfers to the given AWS storage services** - Snowball Edge Storage Optimized is the optimal choice if you need to securely and quickly transfer dozens of terabytes to petabytes of data to AWS. It provides up to 80 TB of usable HDD storage, 40 vCPUs, 1 TB of SATA SSD storage, and up to 40 Gb network connectivity to address large scale data transfer and pre-processing use cases. As each Snowball Edge Storage Optimized device can handle 80TB of data, you can order 10 such devices to take care of the data transfer for all applications. The original Snowball devices were transitioned out of service and Snowball Edge Storage Optimized are now the primary devices used for data transfer. You may see the Snowball device on the exam, just remember that the original Snowball device had 80TB of storage space.

AWS Snowball Edge is suitable for offline data transfers, for customers who are bandwidth constrained or transferring data from remote, disconnected, or austere environments. Therefore, it cannot support automated and accelerated online data transfers.

**Use AWS Transfer Family to automate and accelerate online data transfers to the given AWS storage services** - <mark style="background:#fff88f">The AWS Transfer Family provides fully managed support for file transfers directly into and out of Amazon S3.</mark> Therefore, it cannot support migration into the other AWS storage services mentioned in the given use-case (such as EFS and Amazon FSx for Windows File Server).

**Use File Gateway to automate and accelerate online data transfers to the given AWS storage services** - AWS Storage Gateway's file interface, or file gateway, offers you a seamless way to connect to the cloud to store application data files and backup images as durable objects on Amazon S3 cloud storage.<mark style="background:#fff88f"> File gateway offers SMB or NFS</mark>-based access to data in Amazon S3 with local caching.<mark style="background:#fff88f"> It can be used for on-premises applications, and for Amazon EC2-based applications that need file protocol access to S3 object storage. Therefore, it cannot support migration into the other AWS storage services mentioned in the given use-case (such as EFS and Amazon FSx for Windows File Server).</mark>

References:

[https://aws.amazon.com/datasync/faqs/](https://aws.amazon.com/datasync/faqs/)

[https://aws.amazon.com/storagegateway/file/](https://aws.amazon.com/storagegateway/file/)

[https://aws.amazon.com/aws-transfer-family/](https://aws.amazon.com/aws-transfer-family/)