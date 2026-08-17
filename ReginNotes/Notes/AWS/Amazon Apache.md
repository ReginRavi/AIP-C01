**Store the data in Apache ORC, partitioned by date and sorted by device type of the device** - Apache Parquet and ORC are columnar storage formats that are optimized for fast retrieval of data and used in AWS analytical applications.

By partitioning your data, you can restrict the amount of data scanned by each query, thus improving performance and reducing cost. You can partition your data by any key. A common practice is to partition the data based on time, often leading to a multi-level partitioning scheme. For example, a customer who has data coming in every hour might decide to partition by year, month, date, and hour. Another customer, who has data coming from many different sources but that is loaded only once per day, might partition by a data source identifier and date.

For the given use case, as the company does daily analysis, so it only needs to look at the data generated for a given date. Hence partitioning by date offers significant performance and cost advantages. Since the company also wants to analyze product improvements for each device type, it is better to keep the data sorted by device type, so it allows for faster query execution.

Incorrect options:

**Store the data in Apache Parquet, partitioned by device type and sorted by date** - Apache Parquet is a columnar storage format that is optimized for fast retrieval of data and used in AWS analytical applications. However, partitioning by device type is incorrect for this use case, and partitioning by date is optimal.

**Store the data in compressed .csv, partitioned by date and sorted by the status of the device**

**Store the data in compressed .csv, partitioned by date and sorted by device type**

Both the above options are not columnar storage formats, they are row-based formats that are not optimal for big data retrievals for complex analytical queries.
#AWS
#Apache


Reference:

[https://docs.aws.amazon.com/athena/latest/ug/partitions.html](https://docs.aws.amazon.com/athena/latest/ug/partitions.html)