---
tags:
  - ai
  - rag
created_at: 2026-04-21T00:00:00
updated_at: 2026-04-23T23:41:19
recent_editor: CODEX
---

# RAG (Retrieval-Augmented Generation)

## What It Is

A pattern that grounds an LLM's response in external documents fetched at query time — instead of relying on knowledge baked into the model's weights.

## Analogy

An open-book exam. The model looks up the relevant pages before answering instead of writing from memory alone.

## How It Works

Two phases:

**Ingestion (offline):** documents are split into chunks, each chunk is converted into a vector by an embedding model, and stored in a vector database.

**Runtime:** the user's query is embedded the same way, the vector DB finds the most semantically similar chunks, those chunks are injected into the prompt, and the LLM answers using them as context.

```
Query → Embed → Similarity Search → Top-K chunks → LLM → Response
```

## Example

A support bot over internal docs. User asks: *"What's the refund policy for enterprise plans?"* The system retrieves the 3 most relevant policy chunks and passes them to the LLM. The answer comes from the actual docs — not from the model guessing.

## Why It Matters

RAG solves two core LLM weaknesses: stale knowledge (training cutoff) and hallucination (making things up when uncertain). It's the foundation of almost every production agent — document Q&A, code search, customer support, internal knowledge bases.

---
↑ [Overview](./00_concepts_overview.md)

**Related:** [Embedding Models](./17_embedding_models.md), [Agent](./01_agent.md), [Tools](./04_tools.md), [Multi-Agent Orchestration](./13_multi_agent_orchestration.md)
**Tags:** #ai #rag
