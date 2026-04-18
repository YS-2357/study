---
tags:
  - aws
created_at: 2026-03-31T00:00:00
updated_at: 2026-04-18T12:45:44
recent_editor: CLAUDE
---

# AWS Services Overview

AWS service notes grouped by category. Start with foundation, then pick whichever subdomain matches your current work.

## Subdomains

| Subdomain                                             | Focus                                                    |
| ----------------------------------------------------- | -------------------------------------------------------- |
| [Foundation](foundation/00_foundation_overview.md)    | Region, AZ, PoP, VPC, Subnet                             |
| [Compute](compute/00_compute_overview.md)             | EC2, Auto Scaling, Lambda, Fargate                       |
| [Storage](storage/00_storage_overview.md)             | S3, EBS, EFS, ECR                                        |
| [Database](database/00_database_overview.md)          | RDS, Aurora, DynamoDB, ElastiCache, Redshift, OpenSearch |
| [Networking](networking/00_networking_overview.md)    | ELB, CloudFront, API Gateway, Shield, WAF                |
| [Identity & Access](identity/00_identity_overview.md) | IAM, Security Groups                                     |
| [Analytics](analytics/00_analytics_overview.md)       | Kinesis, EMR, Data Pipeline, SageMaker                   |
| [AI](ai/00_ai_overview.md)                            | Bedrock family, AgentCore (nested)                       |
| [Operations](ops/00_ops_overview.md)                  | CloudWatch, SSM, Billing, Support                        |
| [Developer Tools](devtools/00_devtools_overview.md)   | CDK, boto3, Marketplace                                  |

## Top-Level Notes

- [Strands Agents SDK](31_strands_agents_sdk.md) — Multi-framework agent SDK; kept at top level because it's not strictly an AWS service (it's an open-source framework that deploys to AWS).

## Cross-references

- Networking fundamentals — [Networking](../networking/00_networking_overview.md)
- Computing concepts — [Computing](../computing/00_computing_overview.md)

---
↑ [Home](../home.md)
