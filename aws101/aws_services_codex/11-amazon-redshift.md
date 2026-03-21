# Amazon Redshift

## 1. Definition
Amazon Redshift is a fully managed data warehouse service for large-scale analytics.

## 2. Category / Where It Fits
Which part of AWS it belongs to:
- Analytics

## 3. When To Use It
- When analyzing large amounts of structured data
- When business reporting and dashboards need fast query performance

## 4. What It Does
- Stores and queries large analytical datasets
- Supports SQL-based reporting and aggregation
- Offers provisioned and serverless options for analytics workloads

## 5. What AWS Manages vs What You Manage
### AWS Manages
- Much of the infrastructure, storage options, and core platform operations
### You Manage
- Schema design, query tuning, data loading, and access control

## 6. Console Creation Considerations
- Choose provisioned or serverless based on usage pattern.
- Place the cluster in the right VPC and subnet group.
- Set node size, storage, and access controls carefully.
- Redshift is for analytics, so avoid sizing it like a normal OLTP database.

## 7. Cost Shape
- Charged by cluster or serverless usage, storage, and data transfer
- Large datasets and continuous analytical workloads increase cost

## 8. Availability / Downtime Notes
- Built for analytics rather than high-transaction apps
- Maintenance or resize events can affect performance or access

## 9. Similar Services and Differences
- Commonly confused with Amazon RDS
- Redshift is for analytics at scale; RDS is for transactional application databases

## 10. Related Services
- Amazon S3
- AWS Glue
- Amazon QuickSight

## 11. Simple Example
- Analyze years of sales data for monthly management reports

## 12. Common Mistakes
- Using Redshift for regular OLTP application workloads
- Ignoring distribution and sort key design

## 13. One-Line Summary
- Amazon Redshift is a data warehouse for large-scale analytics.

## 14. Official AWS Docs
- https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html
