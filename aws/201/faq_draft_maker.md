# FAQ Draft Maker — Scenario Design

## What It Is

A FAQ draft maker takes a user's topic or question, retrieves relevant source documents, and generates a structured FAQ draft using a language model. The core pattern is [RAG (Retrieval-Augmented Generation)](aws_services/05_amazon_bedrock_knowledge_bases.md): retrieve first, then generate.

Prerequisites fixed: [AWS CDK](aws_services/07_aws_cdk.md), [Amazon Bedrock AgentCore](aws_services/02_amazon_bedrock_agentcore.md), [Strands SDK](aws_services/01_strands_agents_sdk.md).

## How It Works

### Two pipelines — never conflate them

```
Ingestion (runs once or on schedule)
  S3 (source docs) → Knowledge Bases (chunk → embed → index)

Query (runs per user request)
  user input → Strands agent → KB retrieve → Bedrock generate → FAQ draft
```

These have different triggers, different compute, and different failure modes. Mixing them into one Lambda is the most common design mistake.

### Service choices and rationale

| Layer | Service | Why |
|-------|---------|-----|
| Infrastructure as code | [CDK](aws_services/07_aws_cdk.md) | Fixed prerequisite. All resources below are CDK-managed. |
| Agent runtime | [Bedrock AgentCore](aws_services/02_amazon_bedrock_agentcore.md) | Fixed prerequisite. Handles sessions, memory, tool execution. |
| Agent orchestration | [Strands SDK](aws_services/01_strands_agents_sdk.md) | Fixed prerequisite. Replaces custom agent loop code. |
| RAG retrieval | [Bedrock Knowledge Bases](aws_services/05_amazon_bedrock_knowledge_bases.md) | Managed chunking, embedding, and vector index. Eliminates custom ingestion pipeline. |
| LLM generation | [Amazon Bedrock](aws_services/04_amazon_bedrock.md) | Native to AgentCore. Model choice depends on quality vs cost requirement. |
| Compute | [AWS Lambda](aws_services/09_aws_lambda.md) | Stateless per request. No containers needed at this scale. |
| API entry point | [Amazon API Gateway](aws_services/10_amazon_api_gateway.md) | One route. CDK L2 construct. |
| Document storage | [Amazon S3](../../aws/101/aws_services/19_amazon_s3.md) | Knowledge Bases requires S3 as its data source. |
| Monitoring | [Amazon CloudWatch](aws_services/08_amazon_cloudwatch.md) | Lambda logs, KB retrieval latency, LLM call duration. |

### Decisions left open — context-dependent

| Decision | Options | When to choose which |
|----------|---------|----------------------|
| Auth | IAM vs [Cognito](../../aws/101/aws_services/15_amazon_iam.md) | Internal tool → IAM. Customer-facing → Cognito. |
| Draft history | None vs [DynamoDB TTL](aws_services/15_amazon_dynamodb_ttl.md) | Stateless is simpler. Add DynamoDB only if users need to revisit past drafts. |
| Bedrock model | Claude Haiku / Sonnet / Opus | Haiku for speed and cost. Sonnet or Opus if draft quality is the priority. |
| Ingestion trigger | Manual upload vs [S3 event → EventBridge](../../aws/101/aws_services/19_amazon_s3.md) | Manual is simpler to start. Add event-driven trigger when the doc set updates frequently. |
| Frontend | None vs [S3 + CloudFront](aws_services/16_amazon_s3.md) | API-only if the caller is another service. Add S3 + CloudFront only for a browser UI. |

### Security — one concern per boundary

| Boundary | What to enforce |
|----------|----------------|
| User → API Gateway | Auth (IAM or Cognito), rate limiting |
| Lambda → Bedrock | IAM role, least privilege — no hardcoded API keys |
| Lambda → Knowledge Bases | IAM role scoped to one KB resource |
| Lambda → S3 | Query Lambda: read-only. Ingestion Lambda: write. Separate roles. |
| LLM input | Validate and sanitize user query — guard against prompt injection |
| Secrets | Store model config and KB IDs in [SSM Parameter Store](aws_services/14_aws_ssm_parameter_store.md), not in env vars |

### What the prerequisites eliminate

| Custom work you do NOT need to build | Eliminated by |
|--------------------------------------|--------------|
| Embedding service | Knowledge Bases |
| Vector DB management and ops | Knowledge Bases |
| Chunking logic | Knowledge Bases |
| Agent loop and tool orchestration | Strands SDK |
| Session and memory management | Bedrock AgentCore |
| Manual infra provisioning | CDK |

### Production-level additions

The simple baseline works for an MVP or internal tool. A production deployment adds three layers: network isolation, a proper UI host, and a relational session store.

#### VPC — network isolation

All private resources (Lambda, RDS) move inside a [VPC](../../aws/101/aws_services/04_amazon_vpc.md). API Gateway and CloudFront remain public-facing.

```
Public subnet:   NAT Gateway (Lambda needs this to reach Bedrock)
Private subnet:  Lambda, RDS
```

Lambda in a VPC cannot reach the internet directly — NAT Gateway is required for Bedrock API calls. This adds cost and cold-start latency. Only add VPC when compliance or network policy requires it.

| Resource | Subnet | Reason |
|----------|--------|--------|
| Lambda | Private | No direct internet exposure |
| RDS | Private | Never public-facing |
| NAT Gateway | Public | Lets private Lambda reach Bedrock and SSM |
| API Gateway | VPC Link or public | Entry point stays internet-accessible |

#### UI — S3 + CloudFront vs EC2

| Option | When to use |
|--------|------------|
| [S3 + CloudFront](aws_services/17_amazon_cloudfront.md) | Static frontend (React, plain HTML). Serverless, cheap, CDN-cached. |
| [EC2](../../aws/101/aws_services/05_amazon_ec2.md) | Server-rendered UI, WebSocket, or persistent connection needs. More ops burden. |

S3 + CloudFront is the default. Use EC2 only when the UI requires server-side rendering or persistent connections that a static host cannot support.

#### Session state — DynamoDB TTL vs RDS

| Option | When to use |
|--------|------------|
| [DynamoDB TTL](aws_services/15_amazon_dynamodb_ttl.md) | Short-lived session data. Simple key lookup. High write throughput. |
| [Amazon RDS](../../aws/101/aws_services/10_amazon_rds.md) | Session data that needs relational queries, audit trails, or reporting across sessions. |

DynamoDB TTL is sufficient when sessions are isolated and expire. RDS is warranted when you need to query across users (e.g., "show all drafts from last week"), enforce relational constraints, or integrate with an existing database.

RDS in production: place in private subnet, use [IAM authentication](../../aws/101/aws_services/15_amazon_iam.md) instead of a hardcoded password, store credentials in [SSM Parameter Store](aws_services/14_aws_ssm_parameter_store.md).

#### Production security additions

| Addition | Why |
|----------|-----|
| [Security Groups](../../aws/101/aws_services/14_security_group.md) on Lambda and RDS | Restrict which resources can talk to which |
| [AWS WAF](../../aws/101/aws_services/18_aws_waf.md) on API Gateway or CloudFront | Block malformed requests, rate-limit abusers |
| [AWS Shield](../../aws/101/aws_services/17_aws_shield.md) | DDoS protection on CloudFront (Standard is free) |
| VPC Flow Logs → CloudWatch | Audit network traffic in the private subnet |

## Example

Minimal architecture for a customer-facing FAQ draft maker:

```
Browser
  → CloudFront → S3 (static frontend)
  → API Gateway → Lambda (Strands agent entry point)
      → Bedrock AgentCore (session, memory)
          → Knowledge Bases (retrieve top-k chunks from indexed docs)
          → Bedrock Claude Sonnet (generate FAQ draft)
  → Cognito (auth)

S3 (source docs)
  → Knowledge Bases ingestion (triggered on upload)

SSM Parameter Store
  → KB ID, model ID (read by Lambda at cold start)

CloudWatch
  → Lambda logs, latency alarms
```

CDK provisions everything. No manual console changes.

Production variant adds VPC, WAF, RDS, and moves Lambda into a private subnet:

```
Internet
  → WAF → CloudFront → S3 (static UI)
  → WAF → API Gateway → VPC Link → Lambda (private subnet)
                                     → Bedrock AgentCore
                                         → Knowledge Bases
                                         → Bedrock Claude Sonnet
                                     → RDS (private subnet, session state)
  → Cognito (auth)

NAT Gateway (public subnet)
  → Lambda reaches Bedrock, SSM, Knowledge Bases

S3 (source docs) → Knowledge Bases ingestion
SSM Parameter Store → KB ID, model ID, RDS connection string
CloudWatch → logs, alarms, VPC Flow Logs
```

## Why It Matters

The prerequisite stack (CDK + AgentCore + Strands + Knowledge Bases) is designed to eliminate the hard parts of RAG. The right question is not "how do I build a RAG pipeline" but "what decisions does Knowledge Bases not make for me" — and the answer is: auth, history persistence, model selection, and ingestion trigger timing.

Everything else is configuration, not architecture. Start with the minimal set, measure, then add only what a real usage pattern demands.

> **Tip:** Do not add DynamoDB, EventBridge, or a frontend until you have confirmed the use case requires them. Each addition is one more IAM policy, one more failure domain, and one more thing to monitor.

---
← [AWS 201](00_overview.md) | [Overview](00_overview.md) | Next: [Overview](00_overview.md) →
