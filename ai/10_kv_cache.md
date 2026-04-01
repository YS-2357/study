# KV Cache

## What It Is
KV cache (Key-Value cache) is a fundamental optimization in transformer-based LLMs that avoids redundant computation during token generation.

It stores the Key and Value vectors from the attention mechanism so they do not need to be recomputed for every new token.

## Why It Exists

In a transformer, generating each new token requires attending to all previous tokens. The attention mechanism computes three vectors for each token:
- **Query (Q)** — "what am I looking for?"
- **Key (K)** — "what do I contain?"
- **Value (V)** — "what information do I carry?"

To generate token N, the model needs the K and V vectors of all tokens 1 through N-1.

Without caching, the model would recompute K and V for every previous token at every generation step. This is redundant — the K and V for token 1 do not change when generating token 5 vs token 6.

## How It Works

```
Without KV cache (wasteful):
  Generate token 3 → compute K,V for [1,2]     + new token 3
  Generate token 4 → compute K,V for [1,2,3]   + new token 4   ← recomputed 1,2
  Generate token 5 → compute K,V for [1,2,3,4] + new token 5   ← recomputed 1,2,3

With KV cache (efficient):
  Generate token 3 → compute K,V for [1,2]     + new token 3 → cache K,V for 1,2,3
  Generate token 4 → reuse cached [1,2,3]      + new token 4 → cache adds 4
  Generate token 5 → reuse cached [1,2,3,4]    + new token 5 → cache adds 5
```

Each step only computes K,V for the single new token, then looks up the rest from cache.

## Two Phases of Inference

| Phase | What happens | Speed |
|---|---|---|
| **Prefill** | Process the entire input prompt at once, compute and cache all K,V vectors | Fast (parallel) |
| **Decode** | Generate tokens one by one, reusing cached K,V, appending each new one | Slower (sequential) |

The prefill phase is parallelizable because all input tokens are known. The decode phase is sequential because each token depends on the previous one.

## KV Cache vs Prompt Caching

| | KV cache | Prompt caching |
|---|---|---|
| Scope | Within a single request | Across multiple requests |
| What it avoids | Recomputing K,V for previous tokens during generation | Recomputing the prefill phase for a repeated prefix |
| Managed by | The model runtime automatically | The API provider (Anthropic, OpenAI, etc.) |
| User control | None — always on | Sometimes opt-in, sometimes automatic |

KV cache is the foundation. Prompt caching extends the same idea across API calls — saving the KV cache from the prefill phase so the next request with the same prefix can skip it.

## Trade-off: Memory vs Compute

KV cache trades memory for speed. For long contexts, the cache can become very large:
- Each layer of the model stores K and V vectors for every token
- A model with 80 layers and a 100K token context = a lot of GPU memory

This is why context window limits exist and why techniques like sliding window attention or grouped-query attention (GQA) were developed — to reduce KV cache memory usage.

## When Beginners Should Care

Care about KV cache when:
- you want to understand why LLM inference gets slower and more expensive with longer contexts
- you see terms like "prefill" and "decode" in performance benchmarks
- you want to understand what prompt caching is built on top of

Otherwise, it is enough to know that KV cache is an automatic optimization that makes token generation efficient.
