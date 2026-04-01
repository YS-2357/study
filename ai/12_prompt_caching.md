# Prompt Caching

## What It Is
Prompt caching is an LLM optimization where the provider saves internal computations (KV cache) from previous requests and reuses them when the next request starts with the same token sequence.

It reduces cost and latency for repeated prefixes (e.g., large system prompts, tool definitions).

## How It Works

An LLM processes tokens left to right, computing internal vector states (key-value pairs from the attention mechanism) at each step. These computations are expensive.

Prompt caching saves these intermediate states for a prefix of tokens:

```
Request 1:  [system prompt ... 5000 tokens] [user message A ... 50 tokens]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
             Computed and cached

Request 2:  [system prompt ... 5000 tokens] [user message B ... 60 tokens]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
             Cache HIT — reused, not recomputed
                                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                              Only this part is computed
```

The critical rule: the cache only works on the prefix (the beginning). The moment a token differs from the cached sequence, everything from that point forward must be recomputed.

```
✅ Difference at the end → cache hit on the prefix
✗ Difference at the start or middle → cache miss from that point onward
```

## How It Differs from Traditional Caching

| | Traditional cache | Prompt cache |
|---|---|---|
| Match type | Exact full match | Exact prefix match |
| One word different at the end | Miss | Hit (prefix reused) |
| One word different at the start | Miss | Miss (everything recomputed) |
| What is cached | The response | Internal vector computations (KV cache) |

Traditional caching treats the entire input as a key — one character difference means a completely different key and a cache miss.

Prompt caching matches on the prefix — as long as the beginning is identical, the cached computation is reused regardless of what comes after.

## Why It Matters

Most LLM API calls have a large, repeated portion (system prompt + tool definitions, often thousands of tokens) and a small, changing portion (user message). Prompt caching means you only pay to compute the new part.

Providers like Anthropic and OpenAI offer this. Cached input tokens are significantly cheaper (often 90% discount on input token cost).

## When Beginners Should Care

Care about prompt caching when:
- you are building an agent with a large system prompt or many tools
- you want to understand why providers charge differently for cached vs uncached tokens
- you are optimizing cost or latency for production agents

Otherwise, it is enough to know that providers automatically cache repeated prefixes to save cost.
