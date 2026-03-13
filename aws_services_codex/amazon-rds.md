# Amazon RDS

## 1. Definition
Amazon RDS is a managed relational database service that makes it easier to set up, operate, and scale relational databases in the cloud.

## 2. Category / Where It Fits
Which part of AWS it belongs to:
- Database

## 3. When To Use It
- When an application needs a relational database
- When you want managed backups, patching, and operations

## 4. What It Does
- Runs relational databases such as MySQL and PostgreSQL
- Provides managed database operations and maintenance features

## 5. What AWS Manages vs What You Manage
### AWS Manages
- Much of the database infrastructure, backups, patching, and failover features
### You Manage
- Schema design, queries, users, tuning choices, and application integration

## 6. Console Creation Considerations
- Choose the database engine and version carefully at creation time.
- Decide whether you need Multi-AZ, backups, and encryption from the start.
- Pick instance size and storage based on workload, not guesswork.
- Changing major engine decisions later can require downtime or migration.

## 7. Cost Shape
- Charged by instance size, storage, backups, and data transfer
- Multi-AZ, larger instances, and provisioned storage increase cost

## 8. Availability / Downtime Notes
- Multi-AZ can reduce downtime during failures
- Maintenance windows and major changes can still affect availability

## 9. Similar Services and Differences
- Commonly confused with Amazon DynamoDB
- RDS is relational and SQL-based; DynamoDB is NoSQL and key-value/document-based

## 10. Related Services
- Amazon VPC
- Security Group
- Amazon Aurora

## 11. Simple Example
- Run an ecommerce application's transactional database on PostgreSQL in RDS

## 12. Common Mistakes
- Choosing too small an instance
- Ignoring backups and maintenance planning

## 13. One-Line Summary
- Amazon RDS is a managed service for relational databases.

## 14. Official AWS Docs
- https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html
