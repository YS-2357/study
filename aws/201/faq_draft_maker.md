# FAQ Draft Maker — Scenario Design

## What It Is

A FAQ draft maker takes a user's topic or question, retrieves relevant FAQ documents, and generates a structured draft using a language model. The AI draft requires CS (Customer Service) staff approval before it becomes live content.

The retrieval layer is [Amazon OpenSearch](aws_services/13_amazon_opensearch.md) with hybrid search (BM25 keyword + kNN vector). FAQs are discrete Q&A units — no chunking strategy is needed. Metadata (category, product, language, source) drives filtered retrieval.

Prerequisites fixed: [AWS CDK](aws_services/07_aws_cdk.md), [Amazon Bedrock AgentCore](aws_services/02_amazon_bedrock_agentcore.md), [Strands SDK](aws_services/01_strands_agents_sdk.md).

## How It Works

### Three pipelines — never conflate them

```
1. Preprocessing (raw data → clean FAQ docs)
   Raw source (CRM, DB, files) → Lambda / Glue → cleaned Q&A docs → S3

2. Ingestion (S3 → searchable index)
   S3 (clean FAQ docs)
     → Embedding Lambda (Bedrock embedding model → vector per FAQ)
     → OpenSearch (one doc per FAQ: vector + metadata fields)

3. Query + approval (per user request)
   user input → Strands agent
     → embed query → OpenSearch hybrid search (BM25 + kNN + metadata filter)
     → top-k FAQ docs → Bedrock generate draft
     → draft saved to RDS (status: pending)
     → CS staff reviews → approves or rejects
     → RDS updated (status: approved / rejected)
```

### Why OpenSearch directly — not Knowledge Bases

[Knowledge Bases](aws_services/05_amazon_bedrock_knowledge_bases.md) is designed for long documents that need chunking. FAQs are already atomic — each Q&A pair is one unit. KB's chunking layer adds complexity without benefit, and you lose direct control over the index schema and hybrid search tuning.

| Concern | Knowledge Bases | OpenSearch directly |
|---------|----------------|---------------------|
| Chunking | Forced — wrong for FAQs | Skipped — one doc per FAQ |
| Metadata filtering | Limited | Native — filter before scoring |
| Hybrid search (BM25 + kNN) | Not supported | Built-in |
| Index schema control | Abstracted away | Full control |
| Re-index from S3 | Managed but opaque | Explicit, auditable |

**Hybrid search is especially valuable for FAQs:**

| Search type | Catches |
|-------------|---------|
| BM25 (keyword) | Exact matches — "return policy" → "return policy" |
| kNN (vector) | Semantic matches — "send item back" → "return policy" |
| Combined | Both — which is what real user queries require |

### OpenSearch document schema

Each FAQ is one OpenSearch document:

```json
{
  "question": "How do I return an item?",
  "answer": "You can return any item within 30 days...",
  "embedding": [0.012, -0.034, ...],
  "category": "returns",
  "product_line": "electronics",
  "language": "en",
  "source": "crm_ticket",
  "updated_at": "2026-04-10"
}
```

Metadata filtering narrows the search space before scoring — faster and more precise than post-retrieval filtering.

### Why S3 as the durable store

OpenSearch is the search index, not the source of truth. S3 holds the processed FAQ documents durably.

| Role | Service |
|------|---------|
| Source of truth for processed FAQs | S3 |
| Search and retrieval | OpenSearch |
| Re-index trigger | S3 event → Embedding Lambda → OpenSearch |

If the OpenSearch index is corrupted or needs a schema change, S3 is what you re-index from.

### Why RDS — not DynamoDB

The approval workflow is relational. DynamoDB cannot serve it well.

| Requirement | DynamoDB | RDS |
|-------------|----------|-----|
| Query all pending drafts for a CS team | Poor — no joins | Yes |
| Audit trail: who approved what, when | Awkward | Natural |
| Relational constraints (draft → staff → action) | No | Yes |
| Data must persist indefinitely | Requires extra config | Default |
| Reporting: approval rate, avg review time | Very hard | Standard SQL |

### RDS schema

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

### Service choices and rationale

| Layer | Service | Why |
|-------|---------|-----|
| Infrastructure as code | [CDK](aws_services/07_aws_cdk.md) | Fixed prerequisite. All resources are CDK-managed. |
| Agent runtime | [Bedrock AgentCore](aws_services/02_amazon_bedrock_agentcore.md) | Fixed prerequisite. Handles sessions, memory, tool execution. |
| Agent orchestration | [Strands SDK](aws_services/01_strands_agents_sdk.md) | Fixed prerequisite. Orchestrates embed → retrieve → generate. |
| Retrieval | [Amazon OpenSearch](aws_services/13_amazon_opensearch.md) | Hybrid search (BM25 + kNN) + metadata filtering. Full schema control. |
| Embedding | Lambda + [Bedrock embedding model](aws_services/04_amazon_bedrock.md) | One vector per FAQ at ingestion. One vector per query at runtime. |
| LLM generation | [Amazon Bedrock](aws_services/04_amazon_bedrock.md) | Generates FAQ draft from retrieved docs. |
| Preprocessing compute | Lambda / Glue | Lambda for small transforms. Glue for large-scale ETL from CRM. |
| Document store | [Amazon S3](../../aws/101/aws_services/19_amazon_s3.md) | Source of truth for processed FAQs. OpenSearch re-indexes from here. |
| Draft and approval store | [Amazon RDS](../../aws/101/aws_services/10_amazon_rds.md) | Relational workflow state, audit trail, cross-draft queries. |
| API entry point | [Amazon API Gateway](aws_services/10_amazon_api_gateway.md) | Separate routes for query API and CS approval API. |
| Monitoring | [Amazon CloudWatch](aws_services/08_amazon_cloudwatch.md) | Lambda logs, OpenSearch latency, RDS query time, approval SLA alarms. |

### Decisions left open — context-dependent

| Decision | Options | When to choose which |
|----------|---------|----------------------|
| Auth | IAM vs [Cognito](../../aws/101/aws_services/15_amazon_iam.md) | Internal CS tool → IAM. External users → Cognito. |
| Preprocessing compute | Lambda vs Glue | Small volume, simple transforms → Lambda. Large CRM export, complex ETL → Glue. |
| Bedrock model | Claude Haiku / Sonnet / Opus | Haiku for speed and cost. Sonnet or Opus if draft quality is the priority. |
| Ingestion trigger | Manual vs S3 event | Manual to start. Event-driven when FAQ set updates frequently. |
| CS UI | [S3 + CloudFront](aws_services/17_amazon_cloudfront.md) vs [EC2](../../aws/101/aws_services/05_amazon_ec2.md) | Static review UI → S3 + CloudFront. Real-time collaboration → EC2. |
| RDS engine | PostgreSQL vs MySQL | PostgreSQL for richer JSON and audit extensions. MySQL if existing tooling requires it. |
| OpenSearch | Serverless vs provisioned | Serverless for variable load. Provisioned for predictable high throughput. |

### VPC — required in production

| Resource | Subnet | Reason |
|----------|--------|--------|
| Lambda (embedding, query, preprocessing) | Private | No direct internet exposure |
| OpenSearch | Private | Never public-facing |
| RDS | Private | Never public-facing |
| NAT Gateway | Public | Lets private Lambda reach Bedrock and SSM |
| API Gateway | Public | Entry point stays internet-accessible |

### Security — one concern per boundary

| Boundary | What to enforce |
|----------|----------------|
| User → API Gateway | Auth, rate limiting, [WAF](../../aws/101/aws_services/18_aws_waf.md) |
| Lambda → Bedrock | IAM role, no hardcoded API keys |
| Lambda → OpenSearch | Fine-grained access control, index-level IAM |
| Lambda → S3 | Embedding Lambda: read. Preprocessing Lambda: write. Separate roles. |
| Lambda → RDS | IAM authentication. Credentials in [SSM Parameter Store](aws_services/14_aws_ssm_parameter_store.md). |
| LLM input | Sanitize user query — guard against prompt injection |
| Draft output | CS staff approval gate — AI output never goes live without human review |

## Example

Production architecture:

```
Internet
  → WAF → CloudFront → S3 (CS staff review UI)
  → WAF → API Gateway
      → Lambda (Strands agent: query handler)
            → embed query (Bedrock embedding model)
            → OpenSearch hybrid search (BM25 + kNN + metadata filter)
            → Bedrock Claude Sonnet (generate draft from top-k FAQs)
            → RDS (save draft, status: pending)
      → Lambda (approval handler)
            → RDS (update status: approved / rejected)
  → Cognito (CS staff auth)

Raw data (CRM, DB, files)
  → Preprocessing Lambda / Glue → S3 (clean FAQ docs)
  → S3 event → Embedding Lambda
      → Bedrock embedding model (vector per FAQ)
      → OpenSearch (index doc: vector + metadata)

VPC (private subnet): Lambda, OpenSearch, RDS
NAT Gateway (public subnet): Lambda → Bedrock, SSM
SSM Parameter Store: model ID, OpenSearch endpoint, RDS connection string
CloudWatch: logs, OpenSearch latency, RDS slow queries, approval SLA alarms
```

## Why It Matters

Three design decisions determine the shape of this system:

1. **No chunking** — FAQs are already atomic. Forcing a chunking layer (KB) adds complexity and breaks the unit boundary.
2. **Hybrid search** — keyword alone misses semantic matches; vector alone misses exact matches. Both are needed for real user queries.
3. **RDS over DynamoDB** — the approval workflow is relational. Audit trail, cross-draft queries, and staff reporting cannot be served by a key-value store.

> **Tip:** When AI output requires human approval, model the approval state as a first-class relational entity — not a flag on a session record. The audit trail and cross-record queries will be needed in production.

---
← [AWS 201](00_overview.md) | [Overview](00_overview.md) | Next: [Overview](00_overview.md) →
