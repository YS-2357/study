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

This runs as a one-time Lambda job. The selected 1,000 are written to S3 as individual objects (one Q&A pair per file, no chunking) and ingested into Knowledge Bases. RDS stores only metadata (category, title, s3_key) for the selected records — not the content.

### Storage design

**RDS MySQL (t3.micro)** — metadata management layer; stores inquiry lifecycle and Q&A metadata (s3_key, category, title) — not Q&A content

**S3** — actual Q&A content (one object per Q&A pair, no chunking) + Knowledge Bases ingestion source

**Knowledge Bases** — retrieval layer (reads from S3; no chunking — each Q&A object is one retrieval unit)

**S3 `prompts/current.txt`** — active prompt guide (git repo holds versioned files; S3 holds only the active version Lambda reads)

### Network topology

```
Public subnet  → EC2 (receives inbound HTTP from users and CS staff)
Private subnet → Lambda, RDS (no public access)

VPC endpoints — Lambda reaches AWS services without internet:
  S3 Gateway endpoint          (free — Q&A content, prompt guide, finalized answers)
  bedrock-runtime              (Bedrock model invocation)
  bedrock-agent-runtime        (Knowledge Bases retrieval)

Security groups:
  EC2 SG    inbound 80/443 from 0.0.0.0/0
  Lambda SG outbound 3306 to RDS SG, 443 to VPC endpoint SG
  RDS SG    inbound 3306 from Lambda SG only
```

### Lambda functions

| Function | Trigger | What it does |
|----------|---------|--------------|
| `submit_inquiry` | API Gateway (POST /inquiry) | Save inquiry to RDS (status: pending), async invoke `generate_draft` |
| `generate_draft` | Async invoke from `submit_inquiry` | Regex PII masking → KB retrieval → Bedrock draft (with Guardrails) → save draft to RDS |
| `list_pending` | API Gateway (GET /inquiries) | Query RDS WHERE status = pending, return inquiries + drafts to CS admin page |
| `approve_inquiry` | API Gateway (POST /inquiries/{id}/approve) | Update draft content, set status pending → approved, invoke `sync_to_kb` |
| `sync_to_kb` | Invoke from `approve_inquiry` | Write approved Q&A to S3 finalized/, call Knowledge Bases StartIngestionJob |

### Three pipelines

```
1. Initial ingestion (one-time or on data update)

   Client-provided Q&A file (10,000 records, external import)
     → Selection Lambda (weighted sampling + k-NN → 1,000 records)
     → S3 selected-qa/ (one object per Q&A pair, no chunking)
       + RDS qa_records: metadata only (id, category, title, s3_key, created_at)
     → Knowledge Bases ingestion

   Product info, FAQ
     → S3 (product-info/, faq/)
     → Knowledge Bases ingestion

2. Real-time draft generation (per inquiry)

   Customer inquiry (category, title, content)
     → EC2 UI → API Gateway → submit_inquiry Lambda
         → RDS: save inquiry (status: pending)
         → async invoke generate_draft Lambda

   generate_draft Lambda (runs in background)
         → regex PII masking (inquiry → masked inquiry)
           [PHONE], [EMAIL], [ID_NUMBER], etc. — original stays in RDS
         → Knowledge Bases retrieval via bedrock-agent-runtime endpoint
           (masked inquiry as query, category filter + similarity)
         → Bedrock Claude Sonnet via bedrock-runtime endpoint
           (system prompt: S3 prompts/current.txt via PROMPT_BUCKET + PROMPT_KEY env vars)
           + Guardrails: PII filter as safety net for missed patterns
         → RDS: save draft (PII-free)

   CS staff opens admin page (EC2)
     → API Gateway → list_pending Lambda → query RDS → return inquiries + drafts

3. CS review and KB reinforcement (per approval)

   CS staff → admin page (EC2)
     → edit draft → confirm
     → API Gateway → approve_inquiry Lambda
         → RDS: update draft content, status: pending → approved
         → invoke sync_to_kb Lambda
             → S3: write to finalized/
             → Knowledge Bases: StartIngestionJob
```

### Infrastructure

| Component | Service | Spec | Why |
|-----------|---------|------|-----|
| UI (customer + CS admin) | [EC2](../../aws/101/aws_services/05_amazon_ec2.md) | t3.micro | Advisor recommendation — production experience |
| Central data store | [RDS MySQL](../../aws/101/aws_services/10_amazon_rds.md) | t3.micro | Advisor recommendation — relational schema needed |
| KB ingestion source | [S3](../../aws/101/aws_services/19_amazon_s3.md) | — | Knowledge Bases requires S3 as data source |
| RAG retrieval | [Knowledge Bases](aws_services/05_amazon_bedrock_knowledge_bases.md) | — | Managed chunking, embedding, and search |
| Draft generation | [Bedrock](aws_services/04_amazon_bedrock.md) + [Strands](aws_services/01_strands_agents_sdk.md) | — | Fixed prerequisite |
| Serverless compute | [Lambda](aws_services/09_aws_lambda.md) | — | 5 functions: submit_inquiry, generate_draft, list_pending, approve_inquiry, sync_to_kb |
| API routing | [API Gateway](aws_services/10_amazon_api_gateway.md) | — | EC2 UI to Lambda |
| Prompt guide | [S3](../../aws/101/aws_services/19_amazon_s3.md) `prompts/current.txt` | — | Active prompt; git repo stores versioned files, S3 holds only current |
| Network isolation | VPC (public + private subnets) | — | RDS in private subnet — no public endpoint |
| Bedrock access | VPC Interface Endpoints (bedrock-runtime, bedrock-agent-runtime) | — | Lambda in private subnet reaches Bedrock without internet |
| S3 access | VPC Gateway Endpoint | — | Free; Lambda reaches S3 without internet |
| PII masking | Regex (in Lambda) | — | Masks phone, email, ID numbers before any Bedrock call |
| PII safety net | [Bedrock Guardrails](aws_services/04_amazon_bedrock.md) | — | Catches context-based PII that regex misses; attached to InvokeModel |
| Monitoring | [CloudWatch](aws_services/08_amazon_cloudwatch.md) | — | Lambda logs, draft latency, RDS query time |

### RDS schema

```sql
-- Selected Q&A metadata (1,000 records; actual content lives in S3)
qa_records (id PK, category, title, s3_key, created_at)

-- Client-provided product data
products (id PK, name, price, size, color, description, updated_at)

-- Inquiry lifecycle
inquiries  (id PK, category, title, content, status ENUM(pending, approved), created_at)
drafts     (id PK, inquiry_id FK, content, created_at)
responses  (id PK, inquiry_id FK, staff_id FK, final_content, sent_at, s3_key)
staff      (id PK, name, email)
```

### Security

| Boundary | What to enforce |
|----------|----------------|
| Customer → UI | Auth, rate limiting, WAF |
| CS staff → admin | Role-based access |
| Network | EC2 in public subnet; Lambda and RDS in private subnet — RDS has no public endpoint |
| Lambda → Bedrock / KB | Via VPC endpoints only — no internet path |
| Lambda → RDS | Private subnet SG rule; credentials in SSM |
| Customer input | Input validation — guard against prompt injection |
| PII → LLM | Regex masks structural PII (phone, email, ID) in `generate_draft` before Retrieve and InvokeModel; original stored in RDS for CS staff only |
| PII safety net | Bedrock Guardrails attached to InvokeModel — catches context-based PII that regex misses |
| Prompt guide | Stored in SSM — not directly editable by end users |

## Example

```
Customer submits inquiry
  category: delivery | title: Late shipment | content: ordered 5 days ago...
  → EC2 UI → API Gateway → submit_inquiry Lambda
      → RDS: save inquiry (status: pending)
      → async invoke generate_draft Lambda (returns immediately)

generate_draft Lambda (background)
  → regex PII masking
      "ordered by Kim Minsu, 010-1234-5678" → "ordered by [NAME], [PHONE]"
  → Knowledge Bases retrieval (bedrock-agent-runtime endpoint)
      category: delivery filter + similarity, query: masked inquiry
      → relevant Q&A, product info, FAQ objects
  → Bedrock Claude Sonnet (bedrock-runtime endpoint)
      system prompt: S3 prompts/current.txt (PROMPT_BUCKET + PROMPT_KEY)
      + Guardrails: PII safety net
  → draft: "Thank you for reaching out. There is currently a logistics delay..."
  → RDS: save draft (PII-free)

CS staff opens admin page
  → API Gateway → list_pending Lambda
      → RDS: SELECT WHERE status = pending
      → returns inquiry + draft

CS staff edits draft → confirms
  → API Gateway → approve_inquiry Lambda
      → RDS: update draft, status: pending → approved
      → invoke sync_to_kb Lambda
          → S3: write to finalized/
          → Knowledge Bases: StartIngestionJob
```

## Why It Matters

CS staff are not slow — they write every answer from scratch. A RAG draft that is 80% correct changes the job from writing to reviewing. That alone cuts handle time significantly.

The feedback loop compounds the value. Every finalized answer feeds back into Knowledge Bases daily. The more inquiries the system handles, the better the drafts become.

> **Tip:** Store the prompt guide in SSM Parameter Store. CS managers need to adjust tone and format without a code deploy. SSM makes it a config change, not a release.

## Decomposition

**One unit = one reason to change.**

| Unit | One reason to change |
|------|----------------------|
| `submit_inquiry` Lambda | Inquiry intake or validation logic changes |
| `generate_draft` Lambda | Retrieval strategy or Bedrock model changes |
| `list_pending` Lambda | CS staff query or filter logic changes |
| `approve_inquiry` Lambda | Approval workflow or status logic changes |
| `sync_to_kb` Lambda | KB ingestion strategy or S3 path changes |
| Selection Lambda | Selection criteria change (weights, k-NN parameters) |
| RDS schema | Inquiry lifecycle structure changes |
| SSM prompt guide | Answer tone, format, or constraints change |
| VPC endpoints | AWS service connectivity changes |
| EC2 UI | Screen layout or UX changes |

## Design Decisions

### D1 — Use case reframing

**Started as:** FAQ document generator.

**Revised to:** Real-time CS inquiry draft assistant.

**Why:** The customer's pain is writing hundreds of similar answers per day, not authoring FAQ articles. The right unit of work is one incoming inquiry, not one FAQ entry.

---

### D2 — Q&A selection: 10,000 to 1,000, stored one-by-one in S3

**Why:** Putting all 10,000 records into the knowledge base adds noise. Balanced, representative records produce better retrieval.

**Strategy:** Client provides 10,000 records as an external file. Selection Lambda applies weighted sampling (underrepresented categories get higher weight) and k-NN to remove near-duplicates. Result: 1,000 high-quality records written to S3 as individual objects — one Q&A pair per file, no chunking.

**No chunking:** Each Q&A pair is already the smallest meaningful unit. Chunking risks splitting the question from its answer, degrading retrieval quality. One object = one retrieval unit.

---

### D3 — RDS as metadata layer, S3 as content layer

**Why:** RDS manages the inquiry lifecycle (draft, revision, final answer) and Q&A metadata (category, title, s3_key) with relational structure. It does not store Q&A content — that lives in S3.

**S3 role:** Stores the actual Q&A content (one object per pair, no chunking) and serves as the ingestion source for Knowledge Bases. Content is written directly to S3 by the Selection Lambda; RDS only holds the pointer (s3_key).

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

### D6 — Prompt guide as files: git for versions, S3 for active

**Why:** CS managers need to tune answer tone and format without a code deploy. Git tracks every version naturally — no extra tooling. S3 stores only `prompts/current.txt`, the file Lambda reads. Rollback = overwrite `current.txt` with an older local version. One small text file in S3: negligible cost.

**Trade-off vs SSM:** SSM has a 100-version limit and a per-parameter cost. Git has no version limit and is already in use. S3 prompt reads go through the existing S3 Gateway endpoint — no additional VPC endpoint needed.

---

### D7 — VPC for RDS isolation

**Why:** RDS holds customer inquiry data. Without a VPC, RDS is publicly accessible to anyone with the endpoint and credentials. VPC places RDS in a private subnet with no public route — only Lambda can reach it via security group rule. This is a data protection requirement, not an operational preference.

**Trade-off:** Lambda in a private subnet loses internet access. VPC endpoints (bedrock-runtime, bedrock-agent-runtime, S3 gateway) restore connectivity to required AWS services without routing traffic over the internet. Removing SSM in favor of S3 files eliminates the SSM interface endpoint and its hourly cost.

---

### D8 — Async draft generation

**Why:** `submit_inquiry` returns immediately after saving the inquiry. `generate_draft` runs in the background via async invoke. The customer does not need to see the draft — only CS staff does. Making the customer wait 3–5 seconds for Bedrock adds latency with no user benefit.

**Trade-off:** CS staff may open the admin page before the draft is ready if they check immediately after submission. Acceptable at this scale.

---

### D9 — Two-layer PII protection: regex + Guardrails

**Why:** CS staff need to see the original inquiry including PII (name, phone, address) to handle the case. The LLM must not. Two layers handle this at different cost points.

**Regex (Lambda, before any Bedrock call):** Masks structural patterns (phone numbers, email addresses, Korean resident registration numbers) with placeholders (`[PHONE]`, `[EMAIL]`, `[ID_NUMBER]`). Fast, deterministic, near-zero cost. The masked text is what Retrieve and InvokeModel receive. The original stays in RDS.

**Bedrock Guardrails (attached to InvokeModel):** Catches context-based PII that regex cannot structurally detect — names embedded in sentences, addresses in natural language. Managed service with audit trail.

**`Retrieve` over `RetrieveAndGenerate`:** `RetrieveAndGenerate` combines retrieval and generation in one API call but restricts prompt control. A custom S3 prompt guide requires full control over the system prompt, which means keeping `Retrieve` and `InvokeModel` as separate calls.

---

### D10 — No hardcoded values: all config via environment variables

**Why:** Hardcoded bucket names, IDs, keys, and endpoints make the code environment-specific and fragile. Every value that could change per environment or deployment must be an environment variable.

**Rule:** All Lambda functions read config from `os.environ`. Values are set in CDK/IaC — never in function code.

| Value | Environment variable |
|-------|---------------------|
| S3 bucket (Q&A, prompt, finalized) | `QA_BUCKET`, `PROMPT_BUCKET`, `FINALIZED_BUCKET` |
| Prompt S3 key | `PROMPT_KEY` |
| Knowledge Base ID | `KNOWLEDGE_BASE_ID` |
| Guardrail ID | `GUARDRAIL_ID` |
| Guardrail version | `GUARDRAIL_VERSION` |
| RDS endpoint | `DB_HOST` |
| RDS credentials | `DB_SECRET_ARN` (Secrets Manager) |

---
← [AWS 201](00_overview.md) | [Overview](00_overview.md) | Next: [Overview](00_overview.md) →
