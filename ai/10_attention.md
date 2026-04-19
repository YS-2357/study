---
tags:
  - ai
created_at: 2026-04-01T00:00:00
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
---

↑ [Overview](./00_ai_overview.md)

# Attention Mechanism (Q, K, V)

## What It Is

Attention is the core mechanism in transformer-based LLMs that lets each token figure out which other tokens are relevant to it. It uses three vectors per token: Query, Key, and Value.

## Analogy

The names come from database/information retrieval. In a key-value store, a query is sent to look up a matching key, and the matching value is returned. Attention is a "soft" version: the query matches all keys partially (similarity scores) and returns a weighted blend of all values.

## How It Works

Every token starts as an embedding vector. That embedding is multiplied by three learned weight matrices to produce Q, K, and V:

```
Token embedding × W_Q → Query vector   ("what am I looking for?")
Token embedding × W_K → Key vector     ("what do I contain?")
Token embedding × W_V → Value vector   ("what information do I carry?")
```

Computing attention for token 5 against all previous tokens:

```
Step 1: Similarity scores (Q · K)
  Q₅ · K₁ = 0.8, Q₅ · K₂ = 0.1, Q₅ · K₃ = 0.9, Q₅ · K₄ = 0.2

Step 2: Softmax → attention weights (sum to 1)
  [0.30, 0.05, 0.60, 0.05]

Step 3: Weighted sum of Values → output
  0.30·V₁ + 0.05·V₂ + 0.60·V₃ + 0.05·V₄ = output₅
```

The matrix form: `Attention(Q, K, V) = softmax(Q × Kᵀ / √d) × V`

- `Q × Kᵀ` → all similarity scores
- `/ √d` → scale factor to prevent scores from getting too large
- `softmax` → normalize to attention weights
- `× V` → weighted combination of values

## Example

In the sentence "The cat sat on the mat," when processing "sat," the attention mechanism might assign high weight to "cat" (the subject) and low weight to "the" (less relevant). The Query of "sat" matches strongly with the Key of "cat."

## Why It Matters

Understanding Q, K, V helps you understand:
- What [KV cache](11_kv_cache.md) actually caches and why (only K and V, not Q — because Q is always fresh for the new token)
- Why longer contexts are more expensive (more K, V pairs to attend to)
- Why multi-head attention exists (different heads learn different relationship types: syntax, semantics, proximity)

---
↑ [Overview](./00_ai_overview.md)

**Related:** [Profiles](09_profiles.md), [KV Cache](11_kv_cache.md)
**Tags:** #ai
