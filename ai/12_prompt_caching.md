---
tags:
  - ai
  - computing
created_at: 260401-000000
updated_at: 260417-141847
---

# Prompt Caching

## What It Is

Prompt caching is an LLM optimization where the provider saves the [KV cache](11_kv_cache.md) from previous requests and reuses it when the next request starts with the same token sequence. It reduces cost and latency for repeated prefixes (e.g., large system prompts, tool definitions).

## How It Works

```
Request 1:  [system prompt ... 5000 tokens] [user message A ... 50 tokens]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
             Computed and cached

Request 2:  [system prompt ... 5000 tokens] [user message B ... 60 tokens]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
             Cache HIT — reused, not recomputed
```

The critical rule: the cache only works on the prefix. The moment a token differs from the cached sequence, everything from that point forward must be recomputed.

| | Traditional cache | Prompt cache |
|---|---|---|
| Match type | Exact full match | Exact prefix match |
| One word different at the end | Miss | Hit (prefix reused) |
| One word different at the start | Miss | Miss (everything recomputed) |
| What is cached | The response | Internal KV cache vectors |

## Example

An agent with a 4000-token system prompt and 200-token tool definitions sends 50 requests. Without prompt caching, each request recomputes all 4200 prefix tokens. With prompt caching, only the first request pays the full cost — the other 49 reuse the cached prefix and only compute the new user message.

## Why It Matters

Most LLM API calls have a large, repeated portion (system prompt + tool definitions) and a small, changing portion (user message). Cached input tokens are significantly cheaper (often 90% discount). This matters when building agents with large system prompts or optimizing production costs.

---
← Previous: [KV Cache](11_kv_cache.md) | [Overview](00_overview.md) | Next: [Multi-Agent Orchestration](13_multi_agent_orchestration.md) →
