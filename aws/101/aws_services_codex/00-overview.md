# AWS Services Codex Overview

This folder contains AWS 101 study notes written in a consistent Codex format.

Each service file follows roughly the same structure:
- definition
- where it fits
- when to use it
- what AWS manages vs what you manage
- console creation considerations
- cost shape
- availability notes
- similar services and differences
- one-line summary
- official AWS docs link

The goal is not to turn these files into full documentation. The goal is to make it easy to:
- compare similar AWS services quickly
- answer AWS 101 questions in plain language
- jump from one service to the next without losing context

## Current Coverage

- `25` service and concept files are currently included
- all service/concept files include an `Official AWS Docs` section
- all service/concept files include a `Console Creation Considerations` section
- the notes are intentionally AWS 101 level, but aligned to official AWS framing

## Recommended Study Paths

### 1. Core beginner path

Read in this order if you want the fastest overall understanding:

1. [`23-region.md`](23-region.md)
2. [`16-availability-zone.md`](16-availability-zone.md)
3. [`14-amazon-vpc.md`](14-amazon-vpc.md)
4. [`25-subnet.md`](25-subnet.md)
5. [`24-security-group.md`](24-security-group.md)
6. [`05-amazon-ec2.md`](05-amazon-ec2.md)
7. [`15-auto-scaling.md`](15-auto-scaling.md)
8. [`19-aws-lambda.md`](19-aws-lambda.md)
9. [`18-aws-fargate.md`](18-aws-fargate.md)
10. [`12-amazon-s3.md`](12-amazon-s3.md)
11. [`10-amazon-rds.md`](10-amazon-rds.md)
12. [`03-amazon-dynamodb.md`](03-amazon-dynamodb.md)
13. [`08-amazon-iam.md`](08-amazon-iam.md)
14. [`20-aws-shield.md`](20-aws-shield.md)
15. [`21-aws-waf.md`](21-aws-waf.md)

### 2. Compute comparison path

Use this when practicing questions like `EC2 vs Lambda vs Fargate` or `Auto Scaling vs Load Balancer`.

1. [`05-amazon-ec2.md`](05-amazon-ec2.md)
2. [`19-aws-lambda.md`](19-aws-lambda.md)
3. [`18-aws-fargate.md`](18-aws-fargate.md)
4. [`15-auto-scaling.md`](15-auto-scaling.md)

Key interaction:
- `EC2` gives server control
- `Lambda` runs event-driven code without server management
- `Fargate` runs containers without managing servers
- `Auto Scaling` changes EC2 capacity, but does not replace load balancing

### 3. Database comparison path

Use this when practicing questions like `RDS vs Aurora`, `RDS vs DynamoDB`, or `when is ElastiCache needed`.

1. [`10-amazon-rds.md`](10-amazon-rds.md)
2. [`01-amazon-aurora.md`](01-amazon-aurora.md)
3. [`03-amazon-dynamodb.md`](03-amazon-dynamodb.md)
4. [`06-amazon-elasticcache.md`](06-amazon-elasticcache.md)

Key interaction:
- `RDS` = managed relational database service
- `Aurora` = AWS-designed relational engine inside the RDS family
- `DynamoDB` = NoSQL for access-pattern-driven, low-latency scale
- `ElastiCache` = cache layer, not system of record

### 4. Storage and delivery path

Use this when practicing questions like `S3 vs EBS`, `why CloudFront`, or `what is a PoP`.

1. [`12-amazon-s3.md`](12-amazon-s3.md)
2. [`04-amazon-ebs.md`](04-amazon-ebs.md)
3. [`02-amazon-cloudfront.md`](02-amazon-cloudfront.md)
4. [`22-pop.md`](22-pop.md)

Key interaction:
- `S3` = object storage
- `EBS` = EC2-attached block storage
- `CloudFront` = CDN in front of origins
- `PoP` = edge location used by services such as CloudFront

### 5. Analytics and streaming path

Use this when comparing batch analytics, data warehousing, and streaming.

1. [`11-amazon-redshift.md`](11-amazon-redshift.md)
2. [`07-amazon-emr.md`](07-amazon-emr.md)
3. [`09-amazon-kinesis.md`](09-amazon-kinesis.md)
4. [`17-aws-data-pipeline.md`](17-aws-data-pipeline.md)
5. [`13-amazon-sagemaker.md`](13-amazon-sagemaker.md)

Key interaction:
- `Redshift` = data warehouse
- `EMR` = big data frameworks like Spark/Hadoop
- `Kinesis` = real-time streaming
- `Data Pipeline` = older scheduled data movement/orchestration service
- `SageMaker AI` = machine learning platform

## Topic Map

### Global infrastructure and networking

- [`23-region.md`](23-region.md)
- [`16-availability-zone.md`](16-availability-zone.md)
- [`14-amazon-vpc.md`](14-amazon-vpc.md)
- [`25-subnet.md`](25-subnet.md)
- [`24-security-group.md`](24-security-group.md)
- [`22-pop.md`](22-pop.md)

Use these together when answering:
- `Region vs Availability Zone`
- `VPC vs Subnet`
- `Security Group vs network-level concepts`
- `PoP vs Region`

### Compute

- [`05-amazon-ec2.md`](05-amazon-ec2.md)
- [`15-auto-scaling.md`](15-auto-scaling.md)
- [`19-aws-lambda.md`](19-aws-lambda.md)
- [`18-aws-fargate.md`](18-aws-fargate.md)

Use these together when answering:
- `Which compute model fits this workload?`
- `Do I need to manage servers?`
- `How does Auto Scaling actually work?`

### Storage and content delivery

- [`12-amazon-s3.md`](12-amazon-s3.md)
- [`04-amazon-ebs.md`](04-amazon-ebs.md)
- [`02-amazon-cloudfront.md`](02-amazon-cloudfront.md)

Use these together when answering:
- `object vs block storage`
- `origin vs edge delivery`
- `storage choice by access pattern`

### Databases

- [`10-amazon-rds.md`](10-amazon-rds.md)
- [`01-amazon-aurora.md`](01-amazon-aurora.md)
- [`03-amazon-dynamodb.md`](03-amazon-dynamodb.md)
- [`06-amazon-elasticcache.md`](06-amazon-elasticcache.md)

Use these together when answering:
- `relational vs NoSQL`
- `managed DB vs cache`
- `standard RDS vs Aurora`

### Analytics and AI

- [`11-amazon-redshift.md`](11-amazon-redshift.md)
- [`07-amazon-emr.md`](07-amazon-emr.md)
- [`09-amazon-kinesis.md`](09-amazon-kinesis.md)
- [`17-aws-data-pipeline.md`](17-aws-data-pipeline.md)
- [`13-amazon-sagemaker.md`](13-amazon-sagemaker.md)

Use these together when answering:
- `warehouse vs big data processing vs streaming`
- `older orchestration service vs newer patterns`
- `analytics vs ML platform`

### Security

- [`08-amazon-iam.md`](08-amazon-iam.md)
- [`20-aws-shield.md`](20-aws-shield.md)
- [`21-aws-waf.md`](21-aws-waf.md)
- [`24-security-group.md`](24-security-group.md)

Use these together when answering:
- `identity vs network security`
- `DDoS protection vs web request filtering`
- `who can do what vs who can connect`

## High-Value Cross-File Links

These are the combinations that come up most often in real AWS 101 questions.

### EC2 + Auto Scaling + networking

- Read [`05-amazon-ec2.md`](05-amazon-ec2.md)
- Then [`15-auto-scaling.md`](15-auto-scaling.md)
- Then [`14-amazon-vpc.md`](14-amazon-vpc.md), [`25-subnet.md`](25-subnet.md), and [`24-security-group.md`](24-security-group.md)

This helps with questions like:
- how EC2 is launched
- how scaling creates new instances
- how those instances are placed and protected in the network

### Lambda + IAM + VPC

- Read [`19-aws-lambda.md`](19-aws-lambda.md)
- Then [`08-amazon-iam.md`](08-amazon-iam.md)
- Then [`14-amazon-vpc.md`](14-amazon-vpc.md) and [`25-subnet.md`](25-subnet.md)

This helps with questions like:
- how Lambda runs
- what permissions it needs
- how it can connect to private resources

### CloudFront + WAF + Shield + PoP

- Read [`02-amazon-cloudfront.md`](02-amazon-cloudfront.md)
- Then [`21-aws-waf.md`](21-aws-waf.md)
- Then [`20-aws-shield.md`](20-aws-shield.md)
- Then [`22-pop.md`](22-pop.md)

This helps with questions like:
- why CloudFront improves speed
- how AWS protects public web apps
- what edge locations actually mean

### RDS + Aurora + ElastiCache

- Read [`10-amazon-rds.md`](10-amazon-rds.md)
- Then [`01-amazon-aurora.md`](01-amazon-aurora.md)
- Then [`06-amazon-elasticcache.md`](06-amazon-elasticcache.md)

This helps with questions like:
- when to choose a managed relational DB
- what Aurora changes
- when a cache is added in front of the database

## How To Use These Notes In Practice

- Start with the `One-Line Summary` if you need a fast answer
- Read `Similar Services and Differences` if the question is comparative
- Read `Console Creation Considerations` if the question is operational
- Read `What AWS Manages vs What You Manage` if the question is about responsibility boundaries
- Open the `Official AWS Docs` link if you need exact AWS wording

## Validation Notes

- The folder was previously reviewed against official AWS documentation
- each service file now includes a direct official documentation link
- the notes remain concise on purpose and do not replace the official docs

## Related Folder

If you want deeper networking intuition behind VPC, subnets, load balancers, ports, and routing, also read:
- [`../../../networking/networking_codex/00_overview.md`](../../../networking/networking_codex/00_overview.md)

That folder is especially useful before or alongside:
- [`14-amazon-vpc.md`](14-amazon-vpc.md)
- [`25-subnet.md`](25-subnet.md)
- [`24-security-group.md`](24-security-group.md)
- any load-balancer-related AWS 101 practice
