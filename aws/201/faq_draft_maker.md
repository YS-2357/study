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

## Design Decisions

A log of decisions made, why, and what was rejected.

---

### D1 — Use case framing

**Started as:** FAQ draft maker — generating static FAQ content.

**Revised to:** CS inquiry draft assistant — generating draft answers for real incoming customer inquiries.

**Why:** The customer's pain is answering hundreds of similar inquiries per day, not authoring FAQ articles. The AI drafts a response to each incoming inquiry. CS staff revise and send. Approved answers accumulate and reinforce the knowledge base daily.

---

### D2 — Two retrieval stores, not one

**Started with:** Knowledge Bases for all RAG.

**Revised to:** KB for product info, OpenSearch for Q&A pairs.

**Why KB for product info:** Product documents are long. KB handles chunking and embedding automatically. Semantic retrieval is sufficient.

**Why OpenSearch for Q&A pairs:** Q&A pairs are atomic — no chunking needed. Hybrid search (BM25 + kNN) catches both exact keyword matches ("return policy") and semantic matches ("how do I send something back"). KB does not support hybrid search. OpenSearch also supports daily reinforcement — new finalized answers are indexed each day.

**Rejected:** Single KB for everything. Forcing Q&A pairs through KB's chunking layer breaks the unit boundary and loses hybrid search capability.

---

### D3 — No chunking for Q&A pairs

**Decision:** Each Q&A pair is one OpenSearch document. No chunking.

**Why:** A question and its answer are one retrieval unit. Chunking would split them or pad them. The retrieval quality degrades when a retrieved chunk contains half an answer.

---

### D4 — S3 is mandatory only for KB

**Started with:** S3 for all data.

**Revised to:** S3 only where required.

| Data | S3 mandatory? | Why |
|------|--------------|-----|
| Product info | Yes | KB requires S3 as its data source |
| Historical Q&A | No | Can come from existing DB or file export |
| Daily reinforcement source | No | Query session store directly — no S3 middleman needed |

**Rule:** store data where it is most naturally queried, not where convention points.

---

### D5 — Session store: DynamoDB vs RDS (open)

**The question:** where to store inquiry lifecycle state (pending → in_review → done)?

**DynamoDB:**
- Pros: serverless, no ops, fast key lookup by inquiry_id, GSI for status filter, TTL for auto-cleanup, cheaper
- Cons: no joins, hard to report across sessions (staff performance, avg handle time)
- Right when: access pattern is "get inquiry by ID" and "list pending inquiries"

**RDS:**
- Pros: joins across inquiry → staff → revision, SQL reporting, audit trail, strong consistency
- Cons: always-on cost, needs VPC + connection pooling for Lambda, more ops
- Right when: customer needs reporting across sessions

**Deciding question:** does the customer need cross-session reporting?
- No → DynamoDB
- Yes → RDS

**Current lean:** DynamoDB — the session is flat (one item per inquiry, status as a field), and reporting requirements have not been confirmed.

---

### D6 — Prompt instructions in SSM, not in code

**Decision:** store prompt instructions in [SSM Parameter Store](aws_services/14_aws_ssm_parameter_store.md).

**Why:** CS managers need to tune tone, format, or constraints without a code deploy. SSM makes it a configuration change, not a release. It is also versioned and auditable.

**Rejected:** hardcoded in Lambda env vars or in the codebase. Either forces a deploy for every prompt tweak.

---

### D7 — Preprocessing compute: Lambda vs Glue

**Decision:** depends on data volume and complexity.

| Condition | Choice |
|-----------|--------|
| Small volume, simple text normalization | Lambda |
| Large CRM export, complex transforms, schema discovery needed | Glue |

**Why not Glue always:** Glue has startup overhead and higher cost for small jobs. Lambda is simpler when the data fits.

---
← [AWS 201](00_overview.md) | [Overview](00_overview.md) | Next: [Overview](00_overview.md) →
