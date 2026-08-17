#Aurora #mysql #highperformance
	#Redis #memcache
	

A company manages a stateful web application that persists data on a MySQL database. The application stack is hosted in the company's on-premises data center using a single server. The company is looking at increasing its market presence through promotions and campaigns. While the user experience has been good so far, the current application architecture will not support the growth that the company envisages. The company has hired you as an AWS Certified Solutions Architect Professional to migrate the current architecture to AWS which should continue to support SQL-based queries. The proposed solution should offer maximum reliability with better performance.

What would you recommend?

**Set up database migration to Amazon Aurora MySQL. Deploy the application in an Auto Scaling group for Amazon EC2 instances that are fronted by an Application Load Balancer. Store sessions in an Amazon ElastiCache for Redis with replication group**

<mark style="background:#fff88f">Amazon Aurora is designed for unparalleled high performance and availability at a global scale with full MySQL and PostgreSQL compatibility.</mark>

Amazon ElastiCache for Redis is a Redis-compatible in-memory service that delivers the ease of use and power of Redis along with the availability, reliability, and performance suitable for the most demanding applications. Both single-node and up to 15-shard clusters are available, enabling scalability to up to 3.55 TiB of in-memory data. Amazon ElastiCache for Redis is fully managed, scalable, and secure. This makes it an ideal candidate to power high-performance use cases such as web, mobile apps, gaming, ad tech, and IoT.

Redis and Memcached are popular, open-source, in-memory data stores. Although they are both easy to use and offer high performance, there are important differences to consider when choosing an engine. Memcached is designed for simplicity while Redis offers a rich set of features that make it effective for a wide range of use cases.

Redis lets you create multiple replicas of a Redis primary. This allows you to scale database reads and to have highly available clusters. The replication support makes Redis a more reliable solution than Memcached.

![](https://assets-pt.media.datacumulus.com/aws-sap-pt/assets/pt3-q4-i1.jpg)

 via - [https://aws.amazon.com/elasticache/redis-vs-memcached/](https://aws.amazon.com/elasticache/redis-vs-memcached/)

Incorrect options:

**Set up database migration to an Amazon RDS MySQL Multi-AZ DB instance. Deploy the application in an Auto Scaling group for Amazon EC2 instances that are fronted by an Application Load Balancer. Store sessions in Amazon ElastiCache for Memcached** - As explained above, the replication support makes <mark style="background:#fff88f">Redis a more reliable solution than Memcached</mark>. So this option is not the best fit.

**Set up database migration to an Amazon RDS MySQL DB instance using read replicas. Deploy the application in an Auto Scaling group for Amazon EC2 instances that are fronted by an Application Load Balancer. Store sessions using Amazon Neptune** - Amazon Neptune is a fast, fully managed database service powering graph use cases such as identity graphs, knowledge graphs, and fraud detection. You cannot use Neptune as a caching layer for storing user sessions.

**Set up database migration to an Amazon DocumentDB instance. Deploy the application in an Auto Scaling group for Amazon EC2 instances that are fronted by a Network Load Balancer. Store sessions in an Amazon ElastiCache for Redis with replication group** - Amazon DocumentDB is a scalable, highly durable, and fully managed database service for operating mission-critical MongoDB workloads. For the given use case, you cannot migrate the relational database (MySQL) into a document database (DocumentDB) as DocumentDB does not support SQL-based queries.

References:

[https://aws.amazon.com/elasticache/redis-vs-memcached/](https://aws.amazon.com/elasticache/redis-vs-memcached/)

[https://docs.aws.amazon.com/whitepapers/latest/aws-overview/database.html](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/database.html)

[https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Replication.Redis.Groups.html](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Replication.Redis.Groups.html)

Domain

Accelerate Workload Migration and Modernization