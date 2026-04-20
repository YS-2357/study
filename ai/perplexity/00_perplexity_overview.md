---
tags:
  - ai
  - perplexity
created_at: 2026-04-20T13:50:42
updated_at: 2026-04-20T14:33:31
recent_editor: CODEX
source:
  - docs.perplexity.ai
  - docs.langchain.com
---

# Perplexity - Overview

Perplexity is an AI-powered answer and search platform. For developers, the important product is the Sonar API: an LLM API designed for web-grounded answers, citations, and research workflows.

## What It Is

Perplexity combines language-model generation with search-grounded context. Instead of only answering from model training data, Sonar can use current web information and return source-backed responses.

This makes it useful when code needs recent facts, public documentation lookup, source discovery, or a research step before another model writes or decides.

## Developer Interfaces

| Interface | What It Gives |
|-----------|---------------|
| Official SDKs | Perplexity provides Python and TypeScript SDKs for API calls. |
| OpenAI-compatible client | Existing OpenAI Chat Completions-style code can call Perplexity by changing the base URL and API key. |
| LangChain Python | `langchain-perplexity` provides `ChatPerplexity`, `PerplexitySearchRetriever`, and `PerplexitySearchResults`. |
| LangChain JS | LangChain JS also documents Perplexity chat-model usage. |

## LangChain Support

LangChain support matters because Perplexity can be used either as the model or as a web-search tool inside a larger agent workflow.

- `ChatPerplexity` - chat model wrapper around Perplexity models.
- `PerplexitySearchRetriever` - retrieves web-grounded search results for a query.
- `PerplexitySearchResults` - agent tool for search results.

Common pattern:

```text
agent needs current information
  -> call Perplexity search or Sonar
  -> get grounded answer and citations
  -> use those sources in the final response or note
```

## Why Use It In Code

Use Perplexity when the program needs external, current, or citation-backed knowledge:

- **Current documentation lookup** - SDK changes, product announcements, pricing, and release notes.
- **Research agents** - collect source-backed context before writing a report or note.
- **Web RAG** - retrieve public-web context without building a crawler/search index first.
- **Citation-heavy answers** - show where claims came from.
- **Tool-using agents** - let a coding or research agent call Perplexity as a search capability.
- **OpenAI-style migration** - reuse existing Chat Completions-shaped code with a different endpoint.

Do not use Perplexity as the default for every generation task. If the task does not need web grounding, citations, or current information, a normal chat model may be simpler and cheaper.

## Official Sources

- [Perplexity SDK overview](https://docs.perplexity.ai/docs/sdk/overview)
- [Sonar API quickstart](https://docs.perplexity.ai/docs/sonar/quickstart)
- [OpenAI Chat Completions SDK compatibility](https://docs.perplexity.ai/guides/chat-completions-sdk)
- [Perplexity LangChain integration](https://docs.perplexity.ai/docs/getting-started/integrations/langchain)
- [LangChain Perplexity provider](https://docs.langchain.com/oss/python/integrations/providers/perplexity)

---
[AI Overview](../00_ai_overview.md)
