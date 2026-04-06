# AWS 201 Services — Overview

Deeper AWS service topics beyond 101 fundamentals, focused on AI agents and production infrastructure.

## Study Order

### AI Agents
1. [Strands Agents SDK](01_strands_agents_sdk.md) — Open-source agent framework.
2. [Amazon Bedrock AgentCore](02_amazon_bedrock_agentcore.md) — Production infrastructure for AI agents.
3. [Amazon Bedrock Guardrails](03_amazon_bedrock_guardrails.md) — Input/output filtering and PII protection.

### Amazon Bedrock
4. [Amazon Bedrock](04_amazon_bedrock.md) — Foundation model access and inference.
5. [Amazon Bedrock Knowledge Bases](05_amazon_bedrock_knowledge_bases.md) — Managed RAG over your data.
6. [Amazon Bedrock Agents](06_amazon_bedrock_agents.md) — Managed low-code agent builder.

### Tooling
7. [AWS CDK](07_aws_cdk.md) — Infrastructure as code for deploying AWS resources.
8. [Amazon CloudWatch](08_amazon_cloudwatch.md) — Monitoring, logs, and alarms.

### Runtime Infrastructure
9. [Amazon API Gateway](09_amazon_api_gateway.md) — HTTP routing layer between the internet and Lambda.
10. [Lambda Container Images](10_lambda_container_images.md) — Package Lambda as Docker when dependencies exceed 250 MB.
11. [Mangum](11_mangum.md) — ASGI adapter that lets FastAPI run inside Lambda.
12. [Amazon OpenSearch](12_amazon_opensearch.md) — Vector store for RAG retrieval.
13. [AWS SSM Parameter Store](13_aws_ssm_parameter_store.md) — Managed config store; must be CDK-managed or it orphans on destroy.
14. [DynamoDB TTL and Session Store](14_amazon_dynamodb_ttl.md) — TTL mechanics, Unix timestamp pitfalls, and the single-source config rule.
15. [Amazon S3 — Static Frontend Hosting](15_amazon_s3.md) — S3 as a private static host behind CloudFront.
16. [Amazon CloudFront](16_amazon_cloudfront.md) — CDN in front of S3; OAC, SPA fallback, HTTPS redirect.
17. [Amazon ECR](17_amazon_ecr.md) — Container registry for Lambda images; CDK manages it automatically.

## Cross-references

- Agent concepts → [AI](../../../ai/00_overview.md)
- AWS 101 foundations → [AWS 101 Services](../../101/aws_services/00_overview.md)
