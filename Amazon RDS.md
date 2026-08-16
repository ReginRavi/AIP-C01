Disaster recovery 

**Use cross-Region Read Replicas**

In addition to using Read Replicas to reduce the load on your source DB instance, you can also use <mark style="background:#fff88f">Read Replicas to implement a DR solution</mark> for your production DB environment. If the source DB instance fails, you can promote your Read Replica to a standalone source server. Read Replicas can also be created in a different Region than the source database. Using a cross-Region Read Replica can help ensure that you get back up and running if you experience a regional availability issue.

**Enable the automated backup feature of Amazon RDS in a multi-AZ deployment that creates backups in a single or multiple AWS Region(s)**

Amazon RDS provides high availability and failover support for DB instances using Multi-AZ deployments. Amazon RDS uses several different technologies to provide failover support. Multi-AZ deployments for MariaDB, MySQL, Oracle, and PostgreSQL DB instances use Amazon's failover technology.

The automated backup feature of Amazon RDS enables point-in-time recovery for your database instance. Amazon RDS will backup your database and transaction logs and store both for a user-specified retention period. If it’s a Multi-AZ configuration, backups occur on the standby to reduce I/O impact on the primary. Amazon RDS supports single Region or cross-Region automated backups.

Incorrect options:

**Use RAID 1 configuration for the RDS DB cluster** - This option has been added as a distractor. RAID configuration options can only be used for EC2 instance–hosted databases. By using EBS storage volumes with EC2 instances, you can configure volumes with any RAID levels. For example, for greater I/O performance, you can opt for RAID 0, which can stripe multiple volumes together. RAID 1 can be used for data redundancy because it mirrors two volumes together.

**Use RDS Provisioned IOPS (SSD) Storage in place of General Purpose (SSD) Storage** - Amazon RDS Provisioned IOPS Storage is an SSD-backed storage option designed to deliver fast, predictable, and consistent I/O performance. <mark style="background:#fff88f">This storage type enhances the performance of the RDS database, but this isn't a disaster recovery option.</mark>

**Use database cloning feature of the RDS DB cluster** - This option has been added as a distractor. <mark style="background:#fff88f">Database cloning is only available for Aurora and not for RDS.</mark>

References:

[https://aws.amazon.com/rds/features/](https://aws.amazon.com/rds/features/)

[https://aws.amazon.com/blogs/database/implementing-a-disaster-recovery-strategy-with-amazon-rds/](https://aws.amazon.com/blogs/database/implementing-a-disaster-recovery-strategy-with-amazon-rds/)

[https://aws.amazon.com/about-aws/whats-new/2021/07/amazon-rds-cross-region-automated-backups-regional-expansion/](https://aws.amazon.com/about-aws/whats-new/2021/07/amazon-rds-cross-region-automated-backups-regional-expansion/)

[https://aws.amazon.com/blogs/database/best-storage-practices-for-running-production-workloads-on-hosted-databases-with-amazon-rds-or-amazon-ec2/](https://aws.amazon.com/blogs/database/best-storage-practices-for-running-production-workloads-on-hosted-databases-with-amazon-rds-or-amazon-ec2/)