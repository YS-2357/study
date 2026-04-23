---
tags:
  - ai
  - embeddings
created_at: 2026-04-23T14:11:56
updated_at: 2026-04-23T23:41:19
recent_editor: CODEX
---

↑ [Overview](./00_concepts_overview.md)

# Embedding Models

## What It Is

An embedding model maps any input (text, image, code) to a fixed-size dense vector — a point in high-dimensional space — such that semantically similar inputs land close together and dissimilar inputs land far apart. The vector is what retrieval systems actually compare.

## Analogy

A coordinate system for meaning. Just as GPS coordinates place every location on Earth in the same numeric space so you can measure distance between any two points, an embedding model places every piece of text in the same vector space so you can measure semantic distance between any two texts — "cat" and "kitten" land close, "cat" and "database" land far.

## How It Works

### Contrastive Training

The dominant training paradigm. The model learns by seeing triplets:

```
(anchor, positive, hard negative)
e.g. (query, relevant document, similar-but-wrong document)
```

**Loss — InfoNCE:** for each anchor, maximize similarity to its positive while minimizing similarity to all negatives in the batch. Models trained this way consistently top the [MTEB benchmark](https://huggingface.co/spaces/mteb/leaderboard) (56 retrieval/classification tasks).

**Hard negatives are critical.** Random negatives (unrelated text) are too easy — the model learns nothing useful from them. Hard negatives are documents that look relevant but aren't. They force the model to learn fine-grained distinctions. Recent work uses dynamic hard negative mining (DHNM) — re-mining negatives as training progresses rather than fixing them at the start.

### Where Positives Come From

| Source | Example |
|--------|---------|
| NLI datasets | entailment pairs (premise → hypothesis) |
| MS MARCO | (search query, clicked document) |
| StackExchange, Reddit | (question, accepted answer) |
| LLM-generated synthetic pairs | GPT-4 writes (question, passage) from a document |

Synthetic data generation via LLM is now the dominant scaling strategy — it lets teams build domain-specific pairs cheaply and at scale.

### Architecture: Fine-tune from Pre-trained LLM

Embedding models are almost never trained from scratch. The standard pipeline:

```
Pre-trained LLM (BERT, Mistral, Qwen, …)
  → contrastive fine-tuning on (query, positive, hard-negative) pairs
  → embedding model
```

The backbone already understands language; fine-tuning teaches it to compress meaning into one vector.

### LLM-as-Embedder (current trend)

Encoder-only models (BERT-style) dominated early work. Decoder-only LLMs (GPT-style) are now used directly as embedding models — taking the last token's hidden state as the vector. Examples: **NV-Embed** (NVIDIA, [arxiv 2405.17428](https://arxiv.org/abs/2405.17428)), **E5-Mistral**, **GTE-Qwen**.

These outperform encoder-only models on MTEB because the larger pre-trained backbone carries more world knowledge. One key tweak: the causal [attention](./10_attention.md) mask is removed during fine-tuning so each token can attend to all others (bidirectional), not just left context.

## Example

Sentence pair cosine similarities (approximate):

| Pair | Similarity |
|------|-----------|
| "cat" / "kitten" | ~0.92 |
| "How do I reset my password?" / "steps to change account password" | ~0.88 |
| "cat" / "database index" | ~0.10 |

At query time in a [RAG](./16_rag.md) pipeline: embed the user query → cosine-search the vector DB → retrieve top-K chunks → pass to LLM.

## Why It Matters

Embedding models are the retrieval layer underneath RAG, semantic search, recommendation systems, and duplicate detection. Model quality directly determines what context the LLM sees — a weak embedding model surfaces the wrong chunks, and no amount of prompt engineering fixes that.

---
↑ [Overview](./00_concepts_overview.md)

**Related:** [RAG](./16_rag.md), [Attention](./10_attention.md), [KV Cache](./11_kv_cache.md)
**Tags:** #ai #embeddings
