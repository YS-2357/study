# CS Inquiry Draft Assistant — Scenario Design

## What It Is

A system that generates an AI draft answer for each incoming customer inquiry. CS staff review and revise the draft on an admin page before sending the final answer. The goal is not automation — CS staff make every final decision. The goal is to eliminate writing from scratch for hundreds of similar inquiries per day.

Prerequisites fixed: [AWS CDK](aws_services/07_aws_cdk.md), [Bedrock AgentCore](aws_services/02_amazon_bedrock_agentcore.md), [Strands SDK](aws_services/01_strands_agents_sdk.md).

## How It Works

### Data provided by the client

| Data | Detail | Role |
|------|--------|------|
| Q&A records | 10,000 records: category, title, content, answer | RAG retrieval source |
| Product info | Structured: price, size, color, etc. | RAG retrieval source |
| FAQ data | Curated FAQ documents | RAG retrieval source |
| Prompt guide | Answer tone, format, and constraints | Injected as system prompt — not RAG |

The inquiry UI is built in-house. It accepts three fields: category (9 predefined), title, content.

### Q&A selection: 10,000 to 1,000

All 10,000 records are not put into the knowledge base. 1,000 representative records are selected to reduce noise and balance categories.

```
Selection rule:
  - Categories with fewer records get higher weight (protect underrepresented categories)
  - Within the same category: k-NN similarity to select diverse, representative records
  - Result: 1,000 balanced, high-quality Q&A records
```

This runs as a one-time Lambda job. The selected 1,000 are exported to S3 and ingested into Knowledge Bases.

### Storage design

**RDS MySQL (t3.micro)** — central data management layer for all data

**S3** — Knowledge Bases ingestion source only

**Knowledge Bases** — retrieval layer (reads from S3)

**SSM Parameter Store** — prompt guide (editable without code deploy)

### Three pipelines

```
1. Initial ingestion (one-time or on data update)

   RDS qa_records (10,000)
     → Selection Lambda (weighted sampling + k-NN → 1,000 records)
     → S3 (selected-qa/)
     → Knowledge Bases ingestion

   Product info, FAQ
     → S3 (product-info/, faq/)
     → Knowledge Bases ingestion

2. Real-time draft generation (per inquiry)

   Customer inquiry (category, title, content)
     → EC2 UI → API Gateway → Lambda (Strands agent)
         → Knowledge Bases retrieval (same category filter + similarity)
         → Bedrock generation (system prompt: prompt guide from SSM)
         → Draft generated
     → RDS: save inquiry + draft (status: pending)
     → CS staff sees draft on admin page (EC2)

3. CS review and daily reinforcement

   CS staff → admin page (EC2)
     → Revise draft → submit final answer
     → API Gateway → Lambda
         → RDS: save response (status: done)
         → S3: write to finalized/

   EventBridge (daily 02:00)
     → Batch Lambda
         → Read S3 finalized/ → Knowledge Bases re-ingestion
```

### Infrastructure

| Component | Service | Spec | Why |
|-----------|---------|------|-----|
| UI (customer + CS admin) | [EC2](../../aws/101/aws_services/05_amazon_ec2.md) | t3.micro | Advisor recommendation — production experience |
| Central data store | [RDS MySQL](../../aws/101/aws_services/10_amazon_rds.md) | t3.micro | Advisor recommendation — relational schema needed |
| KB ingestion source | [S3](../../aws/101/aws_services/19_amazon_s3.md) | — | Knowledge Bases requires S3 as data source |
| RAG retrieval | [Knowledge Bases](aws_services/05_amazon_bedrock_knowledge_bases.md) | — | Managed chunking, embedding, and search |
| Draft generation | [Bedrock](aws_services/04_amazon_bedrock.md) + [Strands](aws_services/01_strands_agents_sdk.md) | — | Fixed prerequisite |
| Serverless compute | [Lambda](aws_services/09_aws_lambda.md) | — | Selection, ingestion, draft generation, batch |
| API routing | [API Gateway](aws_services/10_amazon_api_gateway.md) | — | EC2 UI to Lambda |
| Prompt guide | [SSM Parameter Store](aws_services/14_aws_ssm_parameter_store.md) | — | CS managers update without code deploy |
| Daily sync trigger | EventBridge | — | Knowledge Bases daily reinforcement |
| Monitoring | [CloudWatch](aws_services/08_amazon_cloudwatch.md) | — | Lambda logs, draft latency, RDS query time |

### RDS schema

```sql
-- Client-provided Q&A data
qa_records (id PK, category, title, content, answer, is_selected BOOL, created_at)

-- Client-provided product data
products (id PK, name, price, size, color, description, updated_at)

-- Inquiry lifecycle
inquiries  (id PK, category, title, content, status ENUM(pending, done), created_at)
drafts     (id PK, inquiry_id FK, content, created_at)
responses  (id PK, inquiry_id FK, staff_id FK, final_content, sent_at, s3_key)
staff      (id PK, name, email)
```

### Security

| Boundary | What to enforce |
|----------|----------------|
| Customer → UI | Auth, rate limiting, WAF |
| CS staff → admin | Role-based access |
| Lambda → Bedrock / KB | IAM role, least privilege |
| Lambda → RDS | IAM auth, credentials in SSM |
| Customer input | Input validation — guard against prompt injection |
| Prompt guide | Stored in SSM — not directly editable by end users |

## Example

```
Customer submits inquiry
  category: delivery | title: Late shipment | content: ordered 5 days ago...
  → EC2 UI → API Gateway → Lambda

Lambda (Strands agent)
  → Knowledge Bases retrieval (category: delivery filter + similarity)
      → returns relevant Q&A, product info, FAQ chunks
  → Bedrock Claude Sonnet
      system prompt: prompt guide from SSM
      context: retrieval results
  → draft: "Thank you for reaching out. There is currently a logistics delay..."
  → RDS: save inquiry + draft (status: pending)

CS staff (admin page on EC2)
  → reviews draft
  → revises: "We sincerely apologize. Due to a courier strike..."
  → submits final answer
  → RDS: save response (status: done)
  → S3: write to finalized/

EventBridge (daily 02:00)
  → Batch Lambda → read S3 finalized/ → Knowledge Bases re-ingestion
```

## Why It Matters

CS staff are not slow — they write every answer from scratch. A RAG draft that is 80% correct changes the job from writing to reviewing. That alone cuts handle time significantly.

The feedback loop compounds the value. Every finalized answer feeds back into Knowledge Bases daily. The more inquiries the system handles, the better the drafts become.

> **Tip:** Store the prompt guide in SSM Parameter Store. CS managers need to adjust tone and format without a code deploy. SSM makes it a config change, not a release.

## Decomposition

**One unit = one reason to change.**

| Unit | One reason to change |
|------|----------------------|
| Selection Lambda | Selection criteria change (weights, k-NN parameters) |
| KB ingestion | Embedding model or chunking strategy changes |
| Draft generation Lambda | Retrieval strategy or Bedrock model changes |
| RDS schema | Inquiry lifecycle structure changes |
| SSM prompt guide | Answer tone, format, or constraints change |
| EventBridge daily sync | Reinforcement schedule or batch logic changes |
| EC2 UI | Screen layout or UX changes |

## Design Decisions

### D1 — Use case reframing

**Started as:** FAQ document generator.

**Revised to:** Real-time CS inquiry draft assistant.

**Why:** The customer's pain is writing hundreds of similar answers per day, not authoring FAQ articles. The right unit of work is one incoming inquiry, not one FAQ entry.

---

### D2 — Q&A selection: 10,000 to 1,000

**Why:** Putting all 10,000 records into the knowledge base adds noise. Balanced, representative records produce better retrieval.

**Strategy:** Underrepresented categories get higher weight. Within each category, k-NN removes near-duplicate records. Result: 1,000 high-quality records.

---

### D3 — RDS as central data management layer

**Why:** All client-provided data (Q&A records, product info) and the inquiry lifecycle (draft, revision, final answer) need to be managed in one place with relational structure.

**S3 role:** Ingestion source for Knowledge Bases only. Selected data is exported from RDS to S3, then ingested into KB.

**Advisor recommendation:** RDS MySQL t3.micro — for production operations experience.

---

### D4 — EC2 t3.micro for UI

**Why:** Advisor recommendation for production experience. Running an actual server (vs. S3 static hosting or Lambda) builds operational skills: deploy, restart, monitor, debug on a real instance.

**Trade-off:** Always-on cost. Acceptable at t3.micro pricing for this scale.

---

### D5 — Knowledge Bases for retrieval

**Why:** Manages chunking, embedding, and search for selected Q&A, product info, and FAQ in one place. Category metadata enables pre-filtering before similarity search.

**Rejected:** OpenSearch — adds operational complexity. KB is sufficient given the retrieval requirements here.

---

### D6 — Prompt guide in SSM

**Why:** CS managers need to tune answer tone and format without a code deploy. SSM makes it a configuration change, not a release. It is also versioned and auditable.

---
← [AWS 201](00_overview.md) | [Overview](00_overview.md) | Next: [Overview](00_overview.md) →
