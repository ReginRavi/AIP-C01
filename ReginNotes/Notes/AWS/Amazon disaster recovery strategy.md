A multinational financial services organization operates a mission critical trading platform that processes real time transactions and market data in the us-west-1 Region. The platform consists of stateless application tiers running on Amazon EC2 behind an Application Load Balancer, a relational database that stores transactional records, and an event driven ingestion layer that must preserve strict ordering of incoming data.

Due to new regulatory requirements, the company must implement a cross Region disaster recovery strategy that ensures near instantaneous failover with no data loss. Business stakeholders have defined a Recovery Time Objective (RTO) of less than 10 minutes and a Recovery Point Objective (RPO) of zero. The solution must automatically maintain synchronized data across Regions, minimize operational overhead, and provide a deterministic failover mechanism that avoids manual intervention during an outage.

What do you recommend?

**Implement an active-active architecture with real-time data replication across both Regions and configure Route 53 with health checks and weighted routing**

An active-active architecture runs production workloads simultaneously in multiple Regions. Real-time replication ensures that both Regions process live traffic and maintain synchronized data. Because both Regions are active, failover can occur almost immediately, satisfying an RTO of less than 10 minutes. With synchronous or real-time replication, no committed transactions are lost, achieving a zero RPO.

Using Route 53 health checks with weighted routing enables automatic traffic shifting to the healthy Region if one Region fails. This architecture provides the highest level of availability and meets both strict RTO and RPO requirements.

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q13-i1.jpg)

 via - [https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q13-i2.jpg)

 via - [https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)

Incorrect options:

**Implement a pilot light architecture with continuous data replication in the secondary Region and configure Route 53 health checks with automated DNS failover** - A pilot light architecture maintains core infrastructure and data replication in the secondary Region but does not run the full production workload. Additional resources must be launched during failover. Although pilot light can achieve low RPO with continuous replication, the time required to scale infrastructure can exceed the required RTO of less than 10 minutes. This architecture does not guarantee near-instantaneous failover.

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q13-i3.jpg)

 via - [https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)

**Implement a warm standby architecture with scheduled data replication to the secondary Region and configure Route 53 health checks with automated DNS failover** - A warm standby architecture maintains scaled-down but functional infrastructure in the secondary Region. However, the option specifies regular data replication rather than real-time replication. Regular replication introduces potential replication lag, which prevents achieving a zero RPO. Any lag results in possible data loss during failover. Therefore, this solution does not meet the strict zero RPO requirement.

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q13-i4.jpg)

 via - [https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)

**Enable cross-Region read replicas for the database and manually promote the replica in the secondary Region if a failure occurs** - Cross-Region read replicas use asynchronous replication. Because replication is not synchronous, there is always a possibility of replication lag, which prevents achieving a zero RPO. Additionally, manual promotion introduces operational delay and increases recovery time. Even if promotion is quick, this solution cannot guarantee both zero RPO and sub-10-minute RTO.

Reference:

[https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)