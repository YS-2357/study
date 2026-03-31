# Amazon Aurora

## 1. Definition
Amazon Aurora is a fully managed relational database engine compatible with MySQL and PostgreSQL.

## 2. Category / Where It Fits
Which part of AWS it belongs to:
- Database

## 3. When To Use It
- When you want a managed relational database with strong performance and high availability
- When MySQL or PostgreSQL compatibility is useful

## 4. What It Does
- Provides a managed relational database with AWS-designed storage architecture
- Supports high availability and read scaling options

## 5. What AWS Manages vs What You Manage
### AWS Manages
- Much of the infrastructure, replication, backups, and failover capability
### You Manage
- Database schema, queries, users, and workload tuning

## 6. Console Creation Considerations
- Choose the Aurora-compatible engine and version carefully.
- Decide whether you need replicas, Multi-AZ behavior, or serverless options.
- Set VPC, subnet group, and security groups correctly before launch.
- Aurora can cost more than standard RDS if the workload does not need its strengths.

## 7. Cost Shape
- Charged by instance usage, storage, I/O-related factors, and backups
- High-performance workloads and multiple replicas increase cost

## 8. Availability / Downtime Notes
- Built for higher availability than many standard single-instance database setups
- Upgrades and poor architecture choices can still cause interruption

## 9. Similar Services and Differences
- Commonly confused with standard Amazon RDS engines
- Aurora is part of RDS but uses AWS-designed storage for performance and availability benefits

## 10. Related Services
- Amazon RDS
- Amazon VPC
- Security Group

## 11. Simple Example
- Run a high-traffic application database that needs fast reads and managed failover

## 12. Common Mistakes
- Choosing Aurora without checking whether standard RDS is enough
- Ignoring cost differences for replicas and storage activity

## 13. One-Line Summary
- Amazon Aurora is a high-performance managed relational database in RDS.

## 14. Official AWS Docs
- https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html
