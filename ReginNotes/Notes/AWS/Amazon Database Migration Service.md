**Use AWS Database Migration Service to replicate the data from the databases into Amazon Redshift**

AWS Database Migration Service helps you migrate databases to AWS quickly and securely. The source database remains fully operational during the migration, minimizing downtime to applications that rely on the database. With AWS Database Migration Service, you can continuously replicate your data with high availability and consolidate databases into a petabyte-scale data warehouse by streaming data to Amazon Redshift and Amazon S3.

Continuous Data Replication 

![](https://d1.awsstatic.com/product-marketing/DMS/product-page-diagram-AWS-DMS_continuous-data-replication.a0e3bd328d2a4bd9b40a83e767199dcc13cf678f.png)

 via - https://aws.amazon.com/dms/

You can migrate data to Amazon Redshift databases using AWS Database Migration Service. Amazon Redshift is a fully managed, petabyte-scale data warehouse service in the cloud. With an Amazon Redshift database as a target, you can migrate data from all of the other supported source databases.

The Amazon Redshift cluster must be in the same AWS account and the same AWS Region as the replication instance. During a database migration to Amazon Redshift, AWS DMS first moves data to an Amazon S3 bucket. When the files reside in an Amazon S3 bucket, AWS DMS then transfers them to the proper tables in the Amazon Redshift data warehouse. AWS DMS creates the S3 bucket in the same AWS Region as the Amazon Redshift database. The AWS DMS replication instance must be located in that same region.

Incorrect options:

**Use AWS Glue to replicate the data from the databases into Amazon Redshift** - AWS Glue is a fully managed extract, transform, and load (ETL) service that makes it easy for customers to prepare and load their data for analytics. AWS Glue job is meant to be used for batch ETL data processing.

Using AWS Glue involves significant development efforts to write custom migration scripts to copy the database data into Redshift.

**Use Amazon EMR to replicate the data from the databases into Amazon Redshift** - Amazon EMR is the industry-leading cloud big data platform for processing vast amounts of data using open source tools such as Apache Spark, Apache Hive, Apache HBase, Apache Flink and Presto. With EMR you can run Petabyte-scale analysis at less than half of the cost of traditional on-premises solutions and over 3x faster than standard Apache Spark. For short-running jobs, you can spin up and spin down clusters and pay per second for the instances used. For long-running workloads, you can create highly available clusters that automatically scale to meet demand. Amazon EMR uses Hadoop, an open-source framework, to distribute your data and processing across a resizable cluster of Amazon EC2 instances.

Using EMR involves significant infrastructure management efforts to set up and maintain the EMR cluster. Additionally, this option involves a major development effort to write custom migration jobs to copy the database data into Redshift.

**Use Amazon Kinesis Data Streams to replicate the data from the databases into Amazon Redshift** - Amazon Kinesis Data Streams (KDS) is a massively scalable and durable real-time data streaming service. KDS can continuously capture gigabytes of data per second from hundreds of thousands of sources such as website clickstreams, database event streams, financial transactions, social media feeds, IT logs, and location-tracking events.

However, the user is expected to manually provision an appropriate number of shards to process the expected volume of the incoming data stream. The throughput of an Amazon Kinesis data stream is designed to scale without limits via increasing the number of shards within a data stream. Therefore Kinesis Data Streams is not the right fit for this use-case.

References:

[https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redshift.html](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redshift.html)

[https://aws.amazon.com/dms/](https://aws.amazon.com/dms/)