# CS Inquiry Draft Assistant — Scenario Design

## What It Is

A CS inquiry draft assistant receives a real incoming customer inquiry and generates an AI draft answer for CS staff to review and revise on an admin page. The finalized answer is sent to the customer and saved back to S3, reinforcing the knowledge base on a daily sync cycle.

The goal is not to automate customer responses — CS staff remain in the loop. The goal is to eliminate the burden of answering hundreds of similar inquiries from scratch each day.

Prerequisites fixed: [AWS CDK](aws_services/07_aws_cdk.md), [Amazon Bedrock AgentCore](aws_services/02_amazon_bedrock_agentcore.md), [Strands SDK](aws_services/01_strands_agents_sdk.md).

## How It Works

### The data the customer provides

| Data | Format | Role |
|------|--------|------|
| Product information | Documents (PDF, Word, HTML) | RAG source — needs chunking |
| Historical Q&A pairs | Inquiry + answer records | RAG source — no chunking, each pair is atomic |
| Prompt instructions | Text | System prompt — not RAG, injected directly |

These three inputs shape the AI's draft. Product info and Q&A pairs go into retrieval. Prompt instructions tell the model how to write the answer (tone, format, constraints).

### Three pipelines — never conflate them

```
1. Initial ingestion (one-time or on update)

   Product info (long docs)
     → S3 → Knowledge Bases (chunk → embed → index)

   Historical Q&A pairs (atomic units)
     → Preprocessing Lambda → S3 (clean Q&A docs)
     → Embedding Lambda → OpenSearch (one doc per pair, hybrid index)

2. Real-time draft generation (per incoming inquiry)

   Customer inquiry (via UI)
     → Strands agent
         → embed inquiry
         → OpenSearch hybrid search (BM25 + kNN) on Q&A pairs
         → Knowledge Bases retrieval on product info
         → Bedrock generate draft (with prompt instructions as system prompt)
     → draft + inquiry saved to RDS (status: pending)
     → CS staff sees draft on admin page
     → CS staff revises → finalizes answer
     → RDS updated (status: done)
     → finalized answer → S3

3. Daily reinforcement (batch, scheduled)

   S3 (finalized answers accumulated today)
     → Embedding Lambda → OpenSearch index update
     → Knowledge Bases sync (if product info also updated)
```

### Why two retrieval stores

Product information and Q&A pairs have different shapes and different retrieval needs.

| Concern | Product info | Historical Q&A pairs |
|---------|-------------|----------------------|
| Document length | Long — needs chunking | Short — each pair is one unit |
| Chunking | Yes | No |
| Retrieval type | Semantic (vector) | Hybrid (BM25 + kNN) |
| Best store | [Knowledge Bases](aws_services/05_amazon_bedrock_knowledge_bases.md) | [OpenSearch](aws_services/13_amazon_opensearch.md) |
| Daily sync | Possible via S3 trigger | Yes — new finalized answers added daily |

Knowledge Bases manages chunking and embedding for product documents. OpenSearch handles hybrid search on Q&A pairs where exact keyword matches matter as much as semantic similarity.

### OpenSearch document schema (Q&A pairs)

```json
{
  "inquiry": "배송이 왜 이렇게 늦나요?",
  "answer": "현재 물류 지연이 발생하고 있으며...",
  "embedding": [0.012, -0.034, ...],
  "category": "delivery",
  "product_line": "electronics",
  "language": "ko",
  "source": "historical",
  "created_at": "2026-04-10"
}
```

New finalized answers added daily follow the same schema with `"source": "cs_finalized"`.

### Why RDS

The inquiry lifecycle is relational: one inquiry → one draft → one revision → one final answer → one CS staff member. This requires joins, status tracking, and audit trail across records.

```
inquiries
  inquiry_id      PK
  customer_id     FK
  content         text
  received_at     timestamp
  status          enum(pending, in_review, done)

drafts
  draft_id        PK
  inquiry_id      FK → inquiries
  draft_content   text
  created_at      timestamp

responses
  response_id     PK
  inquiry_id      FK → inquiries
  staff_id        FK → staff
  final_content   text
  sent_at         timestamp
  s3_key          text   ← where the finalized answer is stored

staff
  staff_id        PK
  name
  email
```

### Service choices and rationale

| Layer | Service | Why |
|-------|---------|-----|
| Infrastructure as code | [CDK](aws_services/07_aws_cdk.md) | Fixed prerequisite. All resources CDK-managed. |
| Agent runtime | [Bedrock AgentCore](aws_services/02_amazon_bedrock_agentcore.md) | Fixed prerequisite. Sessions, memory, tool execution. |
| Agent orchestration | [Strands SDK](aws_services/01_strands_agents_sdk.md) | Fixed prerequisite. Coordinates retrieval from two stores + generation. |
| Q&A retrieval | [Amazon OpenSearch](aws_services/13_amazon_opensearch.md) | Hybrid search on atomic Q&A pairs. Daily reinforcement via new finalized answers. |
| Product info retrieval | [Knowledge Bases](aws_services/05_amazon_bedrock_knowledge_bases.md) | Managed chunking and embedding for long product documents. |
| LLM generation | [Amazon Bedrock](aws_services/04_amazon_bedrock.md) | Generates draft from retrieved context + prompt instructions. |
| Prompt instructions | [SSM Parameter Store](aws_services/14_aws_ssm_parameter_store.md) | Injected as system prompt. Versioned and auditable. |
| Preprocessing compute | Lambda / Glue | Cleans historical Q&A before initial ingestion. |
| Document store | [Amazon S3](../../aws/101/aws_services/19_amazon_s3.md) | Stores finalized answers. Source for daily reinforcement. |
| Inquiry lifecycle store | [Amazon RDS](../../aws/101/aws_services/10_amazon_rds.md) | Inquiry → draft → revision → final answer. Relational, audit trail. |
| API entry point | [Amazon API Gateway](aws_services/10_amazon_api_gateway.md) | Separate routes: inquiry intake, draft fetch, revision submit. |
| Daily sync scheduler | Amazon EventBridge | Triggers daily S3 → OpenSearch reinforcement batch. |
| Monitoring | [Amazon CloudWatch](aws_services/08_amazon_cloudwatch.md) | Draft latency, CS revision time, daily sync status, approval SLA. |

### Decisions left open — context-dependent

| Decision | Options | When to choose which |
|----------|---------|----------------------|
| Auth | IAM vs [Cognito](../../aws/101/aws_services/15_amazon_iam.md) | Internal CS tool → IAM. Customer-facing inquiry UI → Cognito. |
| Bedrock model | Claude Haiku / Sonnet / Opus | Haiku for speed. Sonnet or Opus if draft quality is the priority. |
| OpenSearch | Serverless vs provisioned | Serverless for variable load. Provisioned for high, predictable throughput. |
| CS UI | [S3 + CloudFront](aws_services/17_amazon_cloudfront.md) vs [EC2](../../aws/101/aws_services/05_amazon_ec2.md) | Static admin page → S3 + CloudFront. Real-time collaboration or WebSocket → EC2. |
| RDS engine | PostgreSQL vs MySQL | PostgreSQL for richer JSON and audit extensions. |
| Reinforcement frequency | Daily vs real-time | Daily is simpler and sufficient for most inquiry volumes. Real-time if the FAQ set changes rapidly. |

### VPC — required in production

| Resource | Subnet | Reason |
|----------|--------|--------|
| Lambda (embedding, draft generation, batch) | Private | No direct internet exposure |
| OpenSearch | Private | Never public-facing |
| RDS | Private | Never public-facing |
| NAT Gateway | Public | Private Lambda reaches Bedrock, SSM, Knowledge Bases |
| API Gateway | Public | Entry point stays internet-accessible |

### Security — one concern per boundary

| Boundary | What to enforce |
|----------|----------------|
| Customer → inquiry UI | Auth, rate limiting, [WAF](../../aws/101/aws_services/18_aws_waf.md) |
| CS staff → admin page | Auth (IAM or Cognito), role-based access |
| Lambda → Bedrock | IAM role, no hardcoded keys |
| Lambda → OpenSearch | Fine-grained access control, index-level IAM |
| Lambda → Knowledge Bases | IAM role scoped to one KB resource |
| Lambda → RDS | IAM authentication, credentials in SSM |
| LLM input | Sanitize customer inquiry — guard against prompt injection |
| Prompt instructions | Stored in SSM, not in code — version-controlled, not user-editable |

## Example

```
Customer submits inquiry (UI)
  → API Gateway → Lambda
      → Strands agent
          → embed inquiry (Bedrock embedding model)
          → OpenSearch hybrid search → top-k similar Q&A pairs
          → Knowledge Bases retrieval → relevant product info chunks
          → Bedrock Claude Sonnet
              (system prompt: prompt instructions from SSM)
              (context: retrieved Q&A + product info)
          → draft answer generated
      → RDS: save inquiry + draft (status: pending)

CS staff (admin page)
  → sees customer inquiry + AI draft
  → revises draft → submits final answer
  → API Gateway → Lambda
      → RDS: update status to done, save final_content, s3_key
      → S3: write finalized answer

EventBridge (daily, e.g. 02:00)
  → Batch Lambda
      → S3: read new finalized answers since last sync
      → Embedding Lambda: generate vector per answer
      → OpenSearch: index new docs (source: cs_finalized)
      → Knowledge Bases sync (if product info updated)

VPC (private): Lambda, OpenSearch, RDS
NAT Gateway (public): Lambda → Bedrock, SSM, Knowledge Bases
SSM: model ID, OpenSearch endpoint, RDS connection string, prompt instructions
CloudWatch: draft latency, revision time, daily sync status
```

## Why It Matters

The architecture is justified by three concrete requirements:

1. **CS staff are the bottleneck** — not because they are slow, but because every answer starts from zero. RAG gives them a draft that is already 80% correct. Their job becomes editing, not writing.

2. **The knowledge base improves over time** — finalized answers feed back into OpenSearch daily. The more inquiries the system handles, the better the retrieval gets. This is the compounding value of the feedback loop.

3. **Two retrieval stores serve two document shapes** — product information is long and needs chunking (Knowledge Bases). Historical Q&A pairs are atomic and benefit from hybrid keyword + semantic search (OpenSearch). Forcing both into one store degrades retrieval quality for one of them.

> **Tip:** Store prompt instructions in SSM Parameter Store, not in code or environment variables. CS managers may need to tune tone or constraints without a code deploy. SSM makes that a configuration change, not a release.

---
← [AWS 201](00_overview.md) | [Overview](00_overview.md) | Next: [Overview](00_overview.md) →
