---
tags:
  - aws
  - database
created_at: 2026-04-17T14:18:47
updated_at: 2026-04-17T14:18:47
recent_editor: CLAUDE
---

↑ [Overview](./00_aws_overview.md)

# Amazon OpenSearch

## What It Is

Amazon OpenSearch is a managed search and analytics engine. In an AI/RAG stack, it serves as the vector store: it holds document embeddings from the ingestion pipeline and responds to similarity queries from the retrieval layer.

## How It Works

### Two deployment variants

| Variant | What it is | When to use |
|---------|-----------|-------------|
| **OpenSearch Service** | EC2-based cluster, always running | Predictable high-volume workloads |
| **OpenSearch Serverless** | Capacity-based, scales to zero concept | Variable load, POC, dev workloads |

For a demo or POC, use Serverless. Cost warning: even Serverless has a minimum OCU (OpenSearch Compute Unit) charge — destroy when not in use.

### Key concepts

| Term | Meaning |
|------|---------|
| Index | A collection of documents (like a table) |
| Document | One record in an index (like a row) |
| Field | A property of a document (like a column) |
| Vector field | A field that stores an embedding (float array) |
| k-NN search | "Find the k documents most similar to this query vector" |
| BM25 | Keyword ranking algorithm — scores documents by term frequency |

### Two search modes

| Mode | How it works | Catches |
|------|-------------|---------|
| **Semantic (k-NN)** | Embed query → find nearest vectors | Meaning-similar docs even with different words |
| **Keyword (BM25)** | Match exact or stemmed terms | Exact names, product codes, IDs |
| **Hybrid** | Run both → merge + re-rank results | Both semantic matches and exact matches |

Pure vector search misses exact matches (e.g. order numbers, product SKUs). Pure keyword search misses paraphrases. Hybrid covers both — use it by default for production RAG.

### RAG pipeline position

```
ingest.py
  → chunk documents
    → call Bedrock embedding model (Titan Embed)
      → store {text, embedding, metadata} in OpenSearch index

retrieval.py
  → call Bedrock embedding model on user query
    → hybrid search (k-NN + BM25) against OpenSearch
      → re-rank merged results
        → return top-k chunks as context
          → assemble prompt → call Bedrock LLM
```

### OpenSearch vs Bedrock Knowledge Bases

| | OpenSearch (direct) | Bedrock Knowledge Bases |
|---|---|---|
| Retrieval control | Full — custom hybrid search, filters, re-ranking | Limited — managed search, some filter options |
| Setup | You write ingest + retrieval code | Managed — point at S3, KB handles the rest |
| Chunking | Your code controls it | KB strategy options (fixed, semantic, hierarchical) |
| Operational burden | Higher — you own the pipeline | Lower — AWS manages it |
| Use when | Custom pipeline, hybrid search, metadata filters | Standard RAG, minimal code, quick setup |

### Applying to a support-ticket RAG pipeline

If a support-ticket draft assistant used OpenSearch directly instead of [Knowledge Bases](35_amazon_bedrock_knowledge_bases.md), the `generate_draft` Lambda would look like this:

```
generate_draft Lambda
  → regex PII masking (inquiry → masked inquiry)
  → embed masked inquiry via Bedrock Titan Embed
  → hybrid search in OpenSearch
      k-NN on embedding field
    + BM25 on text field
    + category metadata filter (pre-filter before search)
  → top-k Q&A chunks as context
  → Bedrock Claude Sonnet (system: cached prompt, user: context + masked inquiry)
  → save draft to RDS
```

Category metadata filter runs before similarity search — it narrows the search space to only the relevant category first, then ranks by similarity within that set.

### Index design for Q&A pairs

```python
index_body = {
    "mappings": {
        "properties": {
            "embedding":  {"type": "knn_vector", "dimension": 1024},
            "text":       {"type": "text"},        # BM25 target
            "category":   {"type": "keyword"},     # pre-filter field
            "title":      {"type": "text"},
            "s3_key":     {"type": "keyword"}      # pointer back to S3 object
        }
    },
    "settings": {"index": {"knn": True}}
}
```

`category` is `keyword` (exact match for pre-filtering), `text` is `text` (analyzed, BM25-ranked).

### Serverless setup (CDK)

Three resources must be created in order: encryption policy → network policy → collection.

```python
from aws_cdk import aws_opensearchserverless as oss

enc_policy = oss.CfnSecurityPolicy(self, "EncPolicy",
    name="cs-enc",
    type="encryption",
    policy='{"Rules":[{"ResourceType":"collection","Resource":["collection/cs-articles"]}],"AWSOwnedKey":true}'
)

net_policy = oss.CfnSecurityPolicy(self, "NetPolicy",
    name="cs-net",
    type="network",
    policy='[{"Rules":[{"ResourceType":"collection","Resource":["collection/cs-articles"]}],"AllowFromPublic":true}]'
)

collection = oss.CfnCollection(self, "ArticlesCollection",
    name="cs-articles",
    type="VECTORSEARCH"
)
collection.add_dependency(enc_policy)
collection.add_dependency(net_policy)
```

`add_dependency` is required — CDK doesn't auto-detect ordering for L1 constructs.

## Example

Hybrid retrieval query with category pre-filter:

```python
def retrieve(query: str, category: str, top_k: int = 5) -> list[str]:
    query_embedding = embed(query)  # Bedrock Titan Embed call

    response = opensearch_client.search(
        index="articles-index",
        body={
            "query": {
                "bool": {
                    "filter": [
                        {"term": {"category": category}}   # pre-filter by category
                    ],
                    "should": [
                        {
                            "knn": {
                                "embedding": {"vector": query_embedding, "k": top_k}
                            }
                        },
                        {
                            "match": {"text": query}        # BM25 keyword match
                        }
                    ]
                }
            }
        }
    )
    return [hit["_source"]["text"] for hit in response["hits"]["hits"]]
```

Returns the top-k most relevant Q&A chunks for the given category — combining semantic similarity and exact keyword matches.

## Why It Matters

RAG quality is determined at two points: ingestion (what goes in) and retrieval (what comes back). OpenSearch controls retrieval. Hybrid search catches both paraphrased matches (vector) and exact-term matches (BM25) — neither alone is sufficient for a production CS system where inquiries mix natural language with specific order numbers or product codes.

[Knowledge Bases](35_amazon_bedrock_knowledge_bases.md) is the managed alternative: lower control, lower operational burden. Choose OpenSearch when you need custom hybrid search, metadata pre-filtering, or full pipeline control.

> **Tip:** Index quality = answer quality. If RAG answers are wrong or vague, check the ingest pipeline — chunking strategy and field mappings — before debugging the model call.

---
← Previous: [Mangum](12_mangum.md) | [Overview](./00_aws_overview.md) | Next: [AWS SSM Parameter Store](43_aws_ssm_parameter_store.md) →
