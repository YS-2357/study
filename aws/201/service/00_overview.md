---
tags:
  - aws
created_at: 260417-141847
updated_at: 260417-141847
---

# AWS 201 Service Overview

Deeper AWS service topics beyond 101 fundamentals, focused on AI agents and production infrastructure.

## Study Order

### AI Agents
1. [Strands Agents SDK](01_strands_agents_sdk.md) — Open-source agent framework.
2. [Amazon Bedrock AgentCore](02_amazon_bedrock_agentcore.md) — Production infrastructure for AI agents.
  - [AgentCore services and capabilities](agentcore/00_overview.md) — Runtime, Memory, Gateway, Identity, Code Interpreter, Browser, Observability, Evaluations, and Policy.
3. [Amazon Bedrock Guardrails](03_amazon_bedrock_guardrails.md) — Input/output filtering and PII protection.

### Amazon Bedrock
4. [Amazon Bedrock](04_amazon_bedrock.md) — Foundation model access and inference.
5. [Amazon Bedrock Knowledge Bases](05_amazon_bedrock_knowledge_bases.md) — Managed RAG over your data.
6. [Amazon Bedrock Agents](06_amazon_bedrock_agents.md) — Managed low-code agent builder.
20. [Amazon Bedrock Flows](20_amazon_bedrock_flows.md) — Visual pipeline builder for deterministic multi-step prompt workflows.
21. [Amazon Bedrock Prompt Management](21_amazon_bedrock_prompt_management.md) — Centralized versioned store for prompts, separate from code.
22. [Amazon Bedrock Model Evaluation](22_amazon_bedrock_model_evaluation.md) — Benchmark and compare models on your own dataset before committing.
23. [Amazon Bedrock Data Automation](23_amazon_bedrock_data_automation.md) — Extract structured fields from documents, images, video, and audio.
24. [Amazon Bedrock Custom Models](24_amazon_bedrock_custom_models.md) — Fine-tune base models on your data; requires Provisioned Throughput to serve.

### Tooling
7. [AWS CDK](07_aws_cdk.md) — Infrastructure as code for deploying AWS resources.
8. [Amazon CloudWatch](08_amazon_cloudwatch.md) — Monitoring, logs, and alarms.
9. [AWS Lambda](09_aws_lambda.md) — Serverless compute that runs code in response to events.
25. [boto3](25_boto3.md) — Official AWS SDK for Python; client and resource interfaces for every AWS service.

### Runtime Infrastructure
10. [Amazon API Gateway](10_amazon_api_gateway.md) — HTTP routing layer between the internet and Lambda.
11. [Lambda Container Images](11_lambda_container_images.md) — Package Lambda as Docker when dependencies exceed 250 MB.
12. [Mangum](12_mangum.md) — ASGI adapter that lets FastAPI run inside Lambda.
13. [Amazon OpenSearch](13_amazon_opensearch.md) — Vector store for RAG retrieval.
14. [AWS SSM Parameter Store](14_aws_ssm_parameter_store.md) — Managed config store; must be CDK-managed or it orphans on destroy.
15. [DynamoDB TTL and Session Store](15_amazon_dynamodb_ttl.md) — TTL mechanics, Unix timestamp pitfalls, and the single-source config rule.
16. [Amazon S3 — Static Frontend Hosting](16_amazon_s3.md) — S3 as a private static host behind CloudFront.
17. [Amazon CloudFront](17_amazon_cloudfront.md) — CDN in front of S3; OAC, SPA fallback, HTTPS redirect.
18. [Amazon ECR](18_amazon_ecr.md) — Container registry for Lambda images; CDK manages it automatically.
19. [DynamoDB Workflow Status Tracking](19_amazon_dynamodb_workflow_status_tracking.md) — Why teams store `pending` / `processing` / `done` state in DynamoDB.

## Cross-references

- Agent concepts → [AI](../../../ai/00_overview.md)
- AWS 101 foundations → [AWS 101 Services](../../101/service/00_overview.md)

---
↑ [AWS 201](../00_overview.md)
