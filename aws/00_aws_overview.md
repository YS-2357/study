---
tags:
  - aws
created_at: 2026-03-31T00:00:00
updated_at: 2026-04-18T13:00:00
recent_editor: CLAUDE
---

# AWS Services Overview

AWS service notes organized by category. Foundational concepts (01-30) and advanced topics (31-50).

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
9. [AWS Shield](17_aws_shield.md) - DDoS protection.
10. [AWS WAF](18_aws_waf.md) - Web application firewall.

### Compute

11. [Amazon EC2](05_amazon_ec2.md) - Virtual servers.
12. [Auto Scaling](06_auto_scaling.md) - Automatically adjust EC2 capacity.
13. [AWS Lambda](07_aws_lambda.md) - Serverless functions.
14. [AWS Fargate](26_aws_fargate.md) - Serverless containers.
15. [Lambda Container Images](40_lambda_container_images.md) - Deploy Lambda from Docker images.

### Storage

16. [Amazon S3](19_amazon_s3.md) - Object storage.
17. [Amazon EBS](20_amazon_ebs.md) - Block storage for EC2.
18. [Amazon EFS](22_amazon_efs.md) - Shared file storage.
19. [Amazon ECR](44_amazon_ecr.md) - Container image registry.

### Database & Caching

20. [Amazon RDS](10_amazon_rds.md) - Managed relational databases.
21. [Amazon Aurora](11_amazon_aurora.md) - High-performance relational database.
22. [Amazon DynamoDB](12_amazon_dynamodb.md) - Serverless NoSQL database.
23. [Amazon ElastiCache](13_amazon_elasticache.md) - In-memory caching.
24. [Amazon OpenSearch](42_amazon_opensearch.md) - Search and analytics engine.

### Analytics & Data

25. [Amazon EMR](08_amazon_emr.md) - Managed big data processing.
26. [Amazon Kinesis](09_amazon_kinesis.md) - Real-time data streaming.
27. [Amazon Redshift](23_amazon_redshift.md) - Data warehouse.
28. [AWS Data Pipeline](25_aws_data_pipeline.md) - Legacy ETL orchestration.

### AI & Machine Learning

29. [Amazon SageMaker](24_amazon_sagemaker.md) - ML platform.
30. [Amazon Bedrock](34_amazon_bedrock.md) - Foundation model service.
31. [Bedrock Guardrails](33_amazon_bedrock_guardrails.md) - Safety filters for AI.
32. [Bedrock Knowledge Bases](35_amazon_bedrock_knowledge_bases.md) - RAG for foundation models.
33. [Bedrock Agents](36_amazon_bedrock_agents.md) - AI agents with tool use.
34. [Bedrock Flows](45_amazon_bedrock_flows.md) - Visual workflow builder for AI.
35. [Bedrock Prompt Management](46_amazon_bedrock_prompt_management.md) - Version and manage prompts.
36. [Bedrock Model Evaluation](47_amazon_bedrock_model_evaluation.md) - Benchmark and compare models.
37. [Bedrock Data Automation](48_amazon_bedrock_data_automation.md) - Extract structured data from documents.
38. [Bedrock Custom Models](49_amazon_bedrock_custom_models.md) - Fine-tune foundation models.
39. [Amazon Bedrock AgentCore](32_amazon_bedrock_agentcore.md) - Managed agent runtime.
40. [Strands Agents SDK](31_strands_agents_sdk.md) - Build multi-agent systems.

### Identity & Access

41. [Amazon IAM](15_amazon_iam.md) - Identity and access management.

### Monitoring & Operations

42. [Amazon CloudWatch](38_amazon_cloudwatch.md) - Monitoring and observability.
43. [AWS SSM Parameter Store](43_aws_ssm_parameter_store.md) - Secure configuration storage.

### API & Integration

44. [Amazon API Gateway](39_amazon_api_gateway.md) - REST and HTTP APIs.
45. [Mangum](41_mangum.md) - ASGI adapter for Lambda.

### Developer Tools

46. [AWS CDK](37_aws_cdk.md) - Infrastructure as code in Python/TypeScript.
47. [boto3](50_boto3.md) - AWS SDK for Python.

### General

48. [Cloud Computing Billing](28_cloud_computing_billing.md) - Billing behavior when services are off.
49. [AWS Marketplace](29_aws_marketplace.md) - Buying and selling software on AWS.
50. [AWS Support Plans](30_aws_support_plans.md) - Support tiers and response times.

## Subtrees

- [AgentCore](agentcore/00_overview.md) - Deep-dive into Bedrock AgentCore components.

## Cross-references

- Networking concepts - [Networking](../networking/00_networking_overview.md)
- Computing concepts - [Computing](../computing/00_computing_overview.md)

---
↑ [Root](../00_overview.md)
