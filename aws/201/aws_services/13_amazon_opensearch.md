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

### RAG pipeline position

```
ingest.py
  → chunk documents
    → call Bedrock embedding model (Titan Embed)
      → store {text, embedding, metadata} in OpenSearch index

retrieval.py
  → call Bedrock embedding model on user query
    → k-NN search against OpenSearch
      → return top-k chunks as context
        → assemble prompt → call Bedrock LLM
```

OpenSearch sits between ingestion and the model. The quality of retrieval — and therefore the quality of model answers — depends entirely on what was indexed and how.

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

### Index setup

The vector index must be created after the collection is deployed. It is not a CDK construct — it's an API call:

```python
# Run after cdk deploy, not during
import boto3, json, requests
from requests_aws4auth import AWS4Auth

auth = AWS4Auth(...)  # SigV4 signing for OpenSearch Serverless

index_body = {
    "mappings": {
        "properties": {
            "embedding": {"type": "knn_vector", "dimension": 1024},
            "text": {"type": "text"},
            "metadata": {"type": "object"}
        }
    },
    "settings": {"index": {"knn": True}}
}

requests.put(f"{collection_endpoint}/articles-index", auth=auth, json=index_body)
```

## Example

Retrieval query:

```python
# retrieval.py
def retrieve(query: str, top_k: int = 5) -> list[str]:
    query_embedding = embed(query)  # Bedrock Titan Embed call

    response = opensearch_client.search(
        index="articles-index",
        body={
            "query": {
                "knn": {
                    "embedding": {
                        "vector": query_embedding,
                        "k": top_k
                    }
                }
            }
        }
    )
    return [hit["_source"]["text"] for hit in response["hits"]["hits"]]
```

Returns the 5 most semantically similar document chunks to the query.

## Why It Matters

RAG quality is determined at two points: ingestion (what goes in) and retrieval (what comes back). OpenSearch controls retrieval. If the index has poor chunking, wrong field mappings, or stale data, the model answers from weak or missing context — regardless of how capable the model is.

> **Tip:** Index quality = answer quality. If RAG answers are wrong or vague, check `ingest.py` before debugging the model call.

---
← Previous: [Mangum](12_mangum.md) | [Overview](00_overview.md) | Next: [AWS SSM Parameter Store](14_aws_ssm_parameter_store.md) →
