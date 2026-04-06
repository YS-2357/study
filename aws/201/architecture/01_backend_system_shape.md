# Backend System Shape

## What It Is

The backend of a RAG + agent application organized by responsibility. Each module owns one job; a bug in any module has a predictable failure mode.

## How It Works

| Module | Responsibility | Failure if broken |
|--------|---------------|-------------------|
| `main.py` | API entrypoint, routing, Mangum adapter | Lambda can't route — 500 before agent runs |
| `agent.py` | Strands orchestration, Bedrock call | Agent loop never starts or returns empty |
| `pii.py` | PII detection before data leaves boundary | User data leaks to model, logs, OpenSearch |
| `retrieval.py` | Vector search against OpenSearch | Agent answers with no context — hallucination risk |
| `ingest.py` | Chunk + embed + write to OpenSearch | Retrieval returns nothing; RAG is blind at query time |

## Check order in the request lifecycle

```
Request
  → validate (main.py)       — reject malformed input at the boundary
  → PII check (pii.py)       — before anything reaches the model
  → retrieval (retrieval.py) — before the prompt is assembled
  → model call (agent.py)    — with context already attached
```

## Why It Matters

`ingest.py` runs at deploy/sync time, not at query time. A bug there produces no error at runtime — it just means the KB is empty or stale, so the model answers without context. RAG quality is set at ingestion, not at the moment of the query.

---
[Overview](../aws_services/00_overview.md) | Next: [Frontend, Contract, and E2E](02_frontend_contract_e2e.md) →
