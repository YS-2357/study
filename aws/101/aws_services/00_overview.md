---
tags:
  - aws
created_at: 2026-03-31
updated_at: 2026-04-17
---
# AWS 101 Services Overview

AWS service notes organized by category. Each note covers what the service is, how it works, and key console considerations.

## Study Order

### Global Infrastructure

1. [Region](01_region.md) - Geographic areas where AWS runs infrastructure.
2. [Availability Zone](02_availability_zone.md) - Isolated data centers within a Region.
3. [Subnet](03_subnet.md) - IP address ranges within a VPC.
4. [Points of Presence](27_pop.md) - Edge locations for caching and acceleration.

### Networking & Security

5. [Amazon VPC](04_amazon_vpc.md) - Virtual private network in AWS.
6. [Security Group](14_security_group.md) - Instance-level firewall rules.
7. [Elastic Load Balancing](16_elastic_load_balancing.md) - Distribute traffic across targets.
8. [Amazon CloudFront](21_amazon_cloudfront.md) - CDN for content delivery at the edge.

### Compute

9. [Amazon EC2](05_amazon_ec2.md) - Virtual servers.
10. [Auto Scaling](06_auto_scaling.md) - Automatically adjust EC2 capacity.
11. [AWS Lambda](07_aws_lambda.md) - Serverless functions.
12. [AWS Fargate](26_aws_fargate.md) - Serverless containers.

### Storage

13. [Amazon S3](19_amazon_s3.md) - Object storage.
14. [Amazon EBS](20_amazon_ebs.md) - Block storage for EC2.
15. [Amazon EFS](22_amazon_efs.md) - Shared file storage.

### Database & Caching

16. [Amazon RDS](10_amazon_rds.md) - Managed relational databases.
17. [Amazon Aurora](11_amazon_aurora.md) - High-performance relational database.
18. [Amazon DynamoDB](12_amazon_dynamodb.md) - Serverless NoSQL database.
19. [Amazon ElastiCache](13_amazon_elasticache.md) - In-memory caching.

### Analytics

20. [Amazon EMR](08_amazon_emr.md) - Managed big data processing.
21. [Amazon Kinesis](09_amazon_kinesis.md) - Real-time data streaming.
22. [Amazon Redshift](23_amazon_redshift.md) - Data warehouse.
23. [Amazon SageMaker](24_amazon_sagemaker.md) - ML platform.
24. [AWS Data Pipeline](25_aws_data_pipeline.md) - Legacy ETL orchestration.

### Security & Compliance

25. [Amazon IAM](15_amazon_iam.md) - Identity and access management.
26. [AWS Shield](17_aws_shield.md) - DDoS protection.
27. [AWS WAF](18_aws_waf.md) - Web application firewall.

### General

28. [Cloud Computing Billing](28_cloud_computing_billing.md) - Billing behavior when services are off.
29. [AWS Marketplace](29_aws_marketplace.md) - Buying and selling software on AWS.
30. [AWS Support Plans](30_aws_support_plans.md) - Support tiers and response times.

## Cross-references

- Networking concepts - [Networking](../../../networking/00_overview.md)
- Computing concepts - [Computing](../../../computing/00_overview.md)

---
↑ [Root](../../../00_overview.md)
