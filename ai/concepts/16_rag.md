---
tags:
  - ai
  - rag
created_at: 2026-04-21T00:00:00
updated_at: 2026-04-24T14:00:29
recent_editor: CODEX
---

# RAG (Retrieval-Augmented Generation)

## What It Is

RAG is a pattern that grounds an LLM's response in external documents fetched at query time instead of relying only on knowledge baked into the model's weights. `RAG` is still the umbrella term, but production teams now often describe the system in more specific retrieval-stack terms such as hybrid search, filtering, query rewriting, and reranking.

## Analogy

An open-book exam. The model looks up the relevant pages before answering instead of writing from memory alone.

## How It Works

### Classic Baseline

Two phases:

**Ingestion (offline):** documents are split into chunks, each chunk is converted into a vector by an [embedding model](./17_embedding_models.md), and stored in a vector database.

**Runtime:** the user's query is embedded the same way, the system retrieves relevant chunks, those chunks are injected into the prompt, and the LLM answers using them as context.

```text
Query -> Embed -> Retrieve -> Top-K chunks -> LLM -> Response
```

### Current Production Vocabulary

Modern RAG systems usually add more retrieval control around that baseline:

- **Keyword / sparse search** matches exact terms and identifiers.
- **Semantic / dense search** matches by meaning using embeddings.
- **Hybrid search** combines both. OpenAI's retrieval docs expose semantic search and also support tuning hybrid search weights between embedding matches and sparse keyword matches. [OpenAI Retrieval](https://developers.openai.com/api/docs/guides/retrieval)
- **Metadata filtering** narrows the candidate set by attributes such as date, product, tenant, or document type. [OpenAI Retrieval](https://developers.openai.com/api/docs/guides/retrieval)
- **Query rewriting** rewrites a user question into a retrieval-friendly form before search. [OpenAI Retrieval](https://developers.openai.com/api/docs/guides/retrieval)
- **Reranking** takes a larger candidate set from first-pass retrieval and reorders it with a stronger ranking model. Pinecone describes this as a standard two-stage quality improvement for RAG pipelines. [Pinecone Rerank Results](https://docs.pinecone.io/guides/search/rerank-results)
- **Context assembly** selects the few chunks that actually go into the model context.
- **Grounded answer / citations** means the model answers from retrieved evidence and points back to it when possible.
- **Retrieval eval vs. answer eval** separates "Did we fetch the right evidence?" from "Did the model answer correctly from that evidence?"

### Advanced and Research Terms

Some names are real and useful, but they are not the default language for every RAG system:

- **Contextual retrieval** is Anthropic's approach of adding chunk-specific context before embedding and BM25 indexing to improve retrieval quality. [Anthropic - Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval)
- **Context engineering** is the broader agent-era framing: not just retrieval, but managing the full set of tokens given to the model, including tools, memory, message history, and external data. [Anthropic - Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- **GraphRAG** uses graph-derived structures and query modes such as global search and local search instead of only chunk similarity. This is useful when relationships and entities matter, not as the default for ordinary document QA. [Microsoft GraphRAG](https://microsoft.github.io/graphrag/)
- **Self-RAG** is a research approach where the model learns to retrieve, generate, and critique through self-reflection. [Self-RAG](https://arxiv.org/abs/2310.11511)
- **CRAG** (Corrective RAG) is a research approach where the system evaluates retrieval quality and triggers corrective retrieval actions when the initial evidence looks weak. [Corrective Retrieval Augmented Generation](https://arxiv.org/abs/2401.15884)

## Default Production Process

For a normal enterprise document-grounded system, the usual process is:

1. Ingest and clean documents.
2. Chunk documents and attach useful metadata.
3. Build dense retrieval, and often sparse retrieval too.
4. Retrieve with hybrid search by default.
5. Apply metadata filters and optionally rewrite the query.
6. Rerank the candidate chunks.
7. Assemble a small cited context window.
8. Generate an answer that stays inside the evidence, or refuse when evidence is weak.
9. Evaluate retrieval quality separately from answer quality.

## Example

A support bot over internal docs. User asks: *"What's the refund policy for enterprise plans?"* A production system would usually run hybrid retrieval, restrict by product or policy metadata if available, rerank the candidates, pass the strongest few chunks to the LLM, and answer from those chunks rather than from the model's memory alone.

## Why It Matters

RAG solves two core LLM weaknesses: stale knowledge and hallucination. But saying only "we use RAG" is now often too vague. In practice, answer quality depends heavily on the retrieval stack around it: chunking, filtering, hybrid search, reranking, and context assembly. That is why modern teams still use the term `RAG`, but increasingly talk in retrieval-system terms when designing or debugging it.

---
↑ [Overview](./00_concepts_overview.md)

**Related:** [Embedding Models](./17_embedding_models.md), [Agent](./01_agent.md), [Tools](./04_tools.md), [Multi-Agent Orchestration](./13_multi_agent_orchestration.md)
**Tags:** #ai #rag
