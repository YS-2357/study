# FAQ Draft Maker — Scenario Design

## What It Is

A FAQ draft maker takes a user's topic or question, retrieves relevant source documents, and generates a structured FAQ draft using a language model. The AI draft is not published directly — it goes through CS (Customer Service) staff approval before it becomes live content.

The core pattern is [RAG (Retrieval-Augmented Generation)](aws_services/05_amazon_bedrock_knowledge_bases.md): preprocess raw data → ingest into Knowledge Bases → retrieve on query → generate draft → human review.

Prerequisites fixed: [AWS CDK](aws_services/07_aws_cdk.md), [Amazon Bedrock AgentCore](aws_services/02_amazon_bedrock_agentcore.md), [Strands SDK](aws_services/01_strands_agents_sdk.md).

## How It Works

### Three pipelines — never conflate them

```
1. Preprocessing (raw data → clean data)
   Raw source (DB, CRM, files) → Lambda/Glue → cleaned docs → S3

2. Ingestion (S3 → searchable index)
   S3 (clean docs) → Knowledge Bases (chunk → embed → index)

3. Query + approval (per user request)
   user input → Strands agent → KB retrieve → Bedrock generate
     → draft saved to RDS (status: pending)
     → CS staff reviews → approves or rejects
     → RDS updated (status: approved / rejected)
```

Each pipeline has a different trigger, owner, and failure mode. Mixing any two is the most common design mistake.

### Why RDS — not DynamoDB

RDS is the right choice here, not DynamoDB. The reason is the approval workflow:

| Requirement | DynamoDB | RDS |
|-------------|----------|-----|
| Store draft content and status | Yes | Yes |
| Query all pending drafts for a CS team | Poor — no joins | Yes |
| Audit trail: who approved what, when | Possible but awkward | Natural |
| Relational constraints (draft → staff → action) | No | Yes |
| Data must persist indefinitely (no TTL) | Requires extra config | Default |
| Reporting: approval rate, avg review time | Very hard | Standard SQL |

DynamoDB TTL is appropriate when data is isolated, short-lived, and looked up by a single key. This workflow is none of those things.

### Service choices and rationale

| Layer | Service | Why |
|-------|---------|-----|
| Infrastructure as code | [CDK](aws_services/07_aws_cdk.md) | Fixed prerequisite. All resources are CDK-managed. |
| Agent runtime | [Bedrock AgentCore](aws_services/02_amazon_bedrock_agentcore.md) | Fixed prerequisite. Handles sessions, memory, tool execution. |
| Agent orchestration | [Strands SDK](aws_services/01_strands_agents_sdk.md) | Fixed prerequisite. Replaces custom agent loop code. |
| RAG retrieval | [Bedrock Knowledge Bases](aws_services/05_amazon_bedrock_knowledge_bases.md) | Managed chunking, embedding, and vector index. |
| LLM generation | [Amazon Bedrock](aws_services/04_amazon_bedrock.md) | Native to AgentCore. Model choice depends on quality vs cost. |
| Preprocessing compute | [AWS Lambda](aws_services/09_aws_lambda.md) or AWS Glue | Lambda for lightweight transforms. Glue for large-scale ETL. |
| Query compute | [AWS Lambda](aws_services/09_aws_lambda.md) | Stateless per request. |
| API entry point | [Amazon API Gateway](aws_services/10_amazon_api_gateway.md) | One route per operation. CDK L2 construct. |
| Document storage | [Amazon S3](../../aws/101/aws_services/19_amazon_s3.md) | Raw docs and clean docs in separate prefixes. Knowledge Bases reads clean docs. |
| Draft and approval store | [Amazon RDS](../../aws/101/aws_services/10_amazon_rds.md) | Relational workflow state, audit trail, cross-draft queries. |
| Monitoring | [Amazon CloudWatch](aws_services/08_amazon_cloudwatch.md) | Lambda logs, KB retrieval latency, RDS query time, approval SLA alarms. |

### RDS schema — what to store

```
drafts
  draft_id        PK
  question        text
  draft_content   text
  status          enum(pending, approved, rejected)
  created_at      timestamp
  updated_at      timestamp

approvals
  approval_id     PK
  draft_id        FK → drafts
  staff_id        FK → staff
  action          enum(approved, rejected)
  comment         text
  acted_at        timestamp

staff
  staff_id        PK
  name
  email
  role
```

This supports: "show all pending drafts", "who approved draft X", "how long did approval take", "rejection rate by staff member".

### Decisions left open — context-dependent

| Decision | Options | When to choose which |
|----------|---------|----------------------|
| Auth | IAM vs [Cognito](../../aws/101/aws_services/15_amazon_iam.md) | Internal CS tool → IAM. External users → Cognito. |
| Preprocessing compute | Lambda vs Glue | Small files and simple transforms → Lambda. Large volume or complex ETL → Glue. |
| Bedrock model | Claude Haiku / Sonnet / Opus | Haiku for speed and cost. Sonnet or Opus if draft quality is the priority. |
| Ingestion trigger | Manual vs S3 event → EventBridge | Manual to start. Event-driven when the doc set updates frequently. |
| CS UI | [S3 + CloudFront](aws_services/16_amazon_s3.md) vs [EC2](../../aws/101/aws_services/05_amazon_ec2.md) | Static review UI → S3 + CloudFront. Real-time collaboration or WebSocket → EC2. |
| RDS engine | PostgreSQL vs MySQL | PostgreSQL for richer JSON support and audit extensions. MySQL if existing team tooling requires it. |

### VPC — required in production

All private resources move inside a [VPC](../../aws/101/aws_services/04_amazon_vpc.md).

| Resource | Subnet | Reason |
|----------|--------|--------|
| Lambda (preprocessing, query) | Private | No direct internet exposure |
| RDS | Private | Never public-facing |
| NAT Gateway | Public | Lets private Lambda reach Bedrock, SSM, Knowledge Bases |
| API Gateway | Public | Entry point stays internet-accessible |

### Security — one concern per boundary

| Boundary | What to enforce |
|----------|----------------|
| User → API Gateway | Auth (IAM or Cognito), rate limiting, [WAF](../../aws/101/aws_services/18_aws_waf.md) |
| Lambda → Bedrock | IAM role, least privilege — no hardcoded API keys |
| Lambda → Knowledge Bases | IAM role scoped to one KB resource |
| Lambda → S3 | Preprocessing Lambda: write to clean prefix. Query Lambda: read-only. Separate roles. |
| Lambda → RDS | IAM authentication. Credentials in [SSM Parameter Store](aws_services/14_aws_ssm_parameter_store.md). |
| LLM input | Sanitize user query — guard against prompt injection |
| Draft output | CS staff is the approval gate — AI output never goes live without human review |

### What the prerequisites eliminate

| Custom work you do NOT need to build | Eliminated by |
|--------------------------------------|--------------|
| Embedding service | Knowledge Bases |
| Vector DB management | Knowledge Bases |
| Chunking logic | Knowledge Bases |
| Agent loop and tool orchestration | Strands SDK |
| Session and memory management | Bedrock AgentCore |
| Manual infra provisioning | CDK |

## Example

Production architecture:

```
Internet
  → WAF → CloudFront → S3 (CS staff review UI)
  → WAF → API Gateway → Lambda (Strands agent)
                           → Bedrock AgentCore (session, memory)
                               → Knowledge Bases (retrieve chunks)
                               → Bedrock Claude Sonnet (generate draft)
                           → RDS (save draft, status: pending)
  → Cognito (CS staff auth)

CS staff
  → review UI → API Gateway → Lambda (approval handler)
                                → RDS (update status: approved / rejected)

Raw data source (CRM, DB, files)
  → Preprocessing Lambda → S3 (clean docs, separate prefix)
  → Knowledge Bases ingestion (triggered on S3 upload)

NAT Gateway → Lambda reaches Bedrock, SSM, Knowledge Bases
SSM Parameter Store → KB ID, model ID, RDS connection string
CloudWatch → logs, approval SLA alarms, RDS slow query alerts
```

CDK provisions everything. No manual console changes.

## Why It Matters

The missing context in the initial design was the approval workflow. Without it, DynamoDB TTL seems reasonable — sessions expire, data is isolated. With it, RDS becomes mandatory: the workflow is relational, the audit trail must persist, and CS staff need cross-draft queries.

The preprocessing pipeline is the other addition that changes the shape: raw data from a CRM or internal DB is never clean enough to feed directly into Knowledge Bases. A preprocessing step normalizes, deduplicates, and filters before ingestion.

> **Tip:** When an AI system produces output that humans must approve before it takes effect, design the approval state as a first-class entity in a relational store — not a flag on a session record. The audit trail and cross-record queries will be needed.

---
← [AWS 201](00_overview.md) | [Overview](00_overview.md) | Next: [Overview](00_overview.md) →
