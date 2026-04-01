# Attention Mechanism (Q, K, V)

## What It Is
Attention is the core mechanism in transformer-based LLMs that lets each token figure out which other tokens are relevant to it. It uses three vectors per token: Query, Key, and Value.

## Why They Are Named Query, Key, Value

The names come from database/information retrieval, not from the math.

In a key-value store (like a dictionary):
- A **key** → **value** pair is stored (e.g., `"name" → "Alice"`)
- A **query** is sent to look up a matching key
- When the query matches a key, the value is returned

Attention is a "soft" version of this:

| Database lookup | Attention |
|---|---|
| Query matches one key exactly | Query matches all keys partially (similarity scores) |
| Returns one value | Returns a weighted blend of all values |

The names describe their roles, not the math. The original 2017 "Attention Is All You Need" paper used these names from this analogy.

## Where Q, K, V Come From

Every token starts as an embedding vector. That embedding is multiplied by three separate learned weight matrices to produce Q, K, and V:

```
Token embedding (e.g., 768-dim vector)
  × W_Q → Query vector
  × W_K → Key vector
  × W_V → Value vector
```

Every token gets all three. They are all the same shape.

## What Each One Does

Think of it like a search engine:

| Vector | Role | Analogy |
|---|---|---|
| **Query (Q)** | "What am I looking for?" | A search query |
| **Key (K)** | "What do I contain?" | A page title / tag that gets matched against the query |
| **Value (V)** | "Here is my actual content" | The page content returned when matched |

The Query asks, the Keys answer how relevant they are, and the Values provide the actual information.

## How Attention Works Step by Step

Computing attention for token 5 against all previous tokens:

```
Step 1: Compute similarity scores (Q dot-product K)
  Q₅ · K₁ = 0.8    (token 1 is somewhat relevant)
  Q₅ · K₂ = 0.1    (token 2 is not relevant)
  Q₅ · K₃ = 0.9    (token 3 is very relevant)
  Q₅ · K₄ = 0.2    (token 4 is not relevant)

Step 2: Softmax → attention weights (sum to 1)
  [0.30, 0.05, 0.60, 0.05]

Step 3: Weighted sum of Values → output
  0.30·V₁ + 0.05·V₂ + 0.60·V₃ + 0.05·V₄ = output₅
```

Token 5's output is mostly influenced by tokens 1 and 3 because their Keys matched token 5's Query.

## The Matrix Form

In practice, all tokens are computed at once using matrix multiplication:

```
Attention(Q, K, V) = softmax(Q × Kᵀ / √d) × V
```

Breaking it down:
- `Q × Kᵀ` → matrix of all similarity scores (every query against every key)
- `/ √d` → scale factor to prevent scores from getting too large (d = dimension of key vectors)
- `softmax` → normalize each row to attention weights
- `× V` → weighted combination of values

## Why Only K and V Are Cached

During token generation, when computing attention for a new token:
- A fresh **Q** is needed (from the new token — "what am I looking for?")
- **K and V from all previous tokens** are needed (to match against and retrieve from)

Previous tokens' K and V do not change. So they are cached. The new token's Q is computed fresh each time.

```
New token → compute Q (fresh)
             ↓
         Q × [cached K₁, K₂, ...Kₙ]ᵀ → scores
         scores × [cached V₁, V₂, ...Vₙ] → output
```

This is why it is called KV cache, not QKV cache. See [11_kv_cache.md](11_kv_cache.md) for details.

## Multi-Head Attention

In practice, the model runs multiple attention computations in parallel (called "heads"). Each head has its own W_Q, W_K, W_V matrices and learns to attend to different types of relationships:
- One head might focus on syntax (subject-verb agreement)
- Another might focus on semantic meaning
- Another might focus on positional proximity

The outputs of all heads are concatenated and projected back to the original dimension.

## When Beginners Should Care

Care about Q, K, V when:
- you want to understand what KV cache actually caches and why
- you see attention visualizations and want to interpret them
- you want to understand why longer contexts are more expensive (more K,V pairs to attend to)

Otherwise, it is enough to know that attention is how each token decides which other tokens matter to it.
