---
tags:
  - tooling
created_at: 260417-141847
updated_at: 260417-141847
---
# Obsidian Tags

## What It Is

The tag system that labels every note in this repo for use in Obsidian's graph view, search, and tag pane. Each note carries one or more tags in its YAML frontmatter.

## How It Works

Tags are defined in a YAML frontmatter block at the very top of every note file, before the `# Title` heading:

```yaml
---
tags:
  - aws
  - serverless
---
```

Obsidian reads these tags and lets you filter notes by tag, view tag clusters in the graph view, and navigate between related notes across domains.

## Tag Taxonomy

| Tag | Covers | Example notes |
|-----|--------|---------------|
| `ai` | AI/ML, LLMs, agents, attention, KV cache | ai/ domain, Bedrock notes |
| `aws` | AWS services in general | All aws/ notes |
| `computing` | CPU, GPU, virtualization, caching, storage | computing/ domain |
| `container` | ECR, Docker, Lambda container images | Fargate, ECR, Lambda containers |
| `database` | RDS, DynamoDB, Aurora, ElastiCache | aws/101 DB notes |
| `git` | Git workflow, staging, tracking | git/ domain |
| `infrastructure` | VPC, regions, AZs, subnets, CDK | VPC, CDK, Region notes |
| `ml` | SageMaker, Bedrock, model training | Bedrock, SageMaker notes |
| `monitoring` | CloudWatch, observability | CloudWatch note |
| `networking` | Protocols, OSI, DNS, HTTP, proxies | networking/ domain |
| `security` | IAM, Shield, WAF, auth, secrets | IAM, WAF, Shield notes |
| `serverless` | Lambda, Fargate, API Gateway | Lambda, API GW, Mangum notes |
| `storage` | S3, EFS, EBS | Storage notes |
| `tooling` | Dev tools, editors, terminal setup | tooling/ domain, CDK, boto3 |

## Why It Matters

Tags are the primary way to navigate across domains in Obsidian. A note tagged `ai` and `aws` appears in both tag clusters in the graph view, showing the connection between LLM concepts and AWS services without duplicating content.

> **Tip:** When creating a new note, assign all applicable tags from the taxonomy above. Add a new tag to the taxonomy only if no existing tag fits — then update this file and CLAUDE.md.

---
↑ [Root](../00_overview.md)
