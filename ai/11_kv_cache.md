---
tags:
  - ai
  - computing
created_at: 2026-04-01T00:00:00
updated_at: 2026-04-17T14:18:47
recent_editor: CLAUDE
---

↑ [Overview](./00_ai_overview.md)

# KV Cache

## What It Is

KV cache stores the Key and Value vectors from the [attention mechanism](10_attention.md) so they do not need to be recomputed for every new token during generation.

## How It Works

Generating each new token requires attending to all previous tokens. The K and V vectors for previous tokens do not change, so recomputing them is wasteful.

```
Without KV cache:
  Token 3 → compute K,V for [1,2]     + token 3
  Token 4 → compute K,V for [1,2,3]   + token 4   ← recomputed 1,2
  Token 5 → compute K,V for [1,2,3,4] + token 5   ← recomputed 1,2,3

With KV cache:
  Token 3 → compute K,V for [1,2]     + token 3 → cache K,V for 1,2,3
  Token 4 → reuse cached [1,2,3]      + token 4 → cache adds 4
  Token 5 → reuse cached [1,2,3,4]    + token 5 → cache adds 5
```

Each step only computes K, V for the single new token, then looks up the rest from cache.

### Two Phases of Inference

| Phase | What happens | Speed |
|---|---|---|
| **Prefill** | Process entire input prompt at once, compute and cache all K, V | Fast (parallel) |
| **Decode** | Generate tokens one by one, reusing cached K, V | Slower (sequential) |

## Example

A model generating a 500-token response to a 1000-token prompt: during prefill, all 1000 input tokens are processed in parallel and their K, V cached. During decode, each new token only computes its own K, V and attends to the growing cache. Without KV cache, token 500 would recompute K, V for all 1499 previous tokens.

## Why It Matters

KV cache trades memory for speed. For long contexts, the cache can become very large (each layer stores K and V for every token). This is why context window limits exist and why longer contexts are more expensive. [Prompt caching](12_prompt_caching.md) extends this idea across API calls — saving the KV cache from prefill so the next request with the same prefix can skip it.

---
← Previous: [Attention](10_attention.md) | [Overview](./00_ai_overview.md) | Next: [Prompt Caching](12_prompt_caching.md) →
