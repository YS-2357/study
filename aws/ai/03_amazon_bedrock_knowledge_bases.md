---
tags:
  - ai
  - aws
  - ml
  - storage
created_at: 2026-04-17T14:18:47
updated_at: 2026-04-18T12:30:09
recent_editor: CLAUDE
---

↑ [Overview](./00_ai_overview.md)

# Amazon Bedrock Knowledge Bases

## What It Is

Amazon Bedrock Knowledge Bases is a managed RAG (Retrieval-Augmented Generation) service that connects foundation models to your data sources so responses are grounded in your actual content instead of relying solely on the model's training data.

## Analogy

A librarian. The LLM is smart but only knows what it learned in school (training data). Knowledge Bases is the librarian that goes to the shelves (your documents), finds the relevant pages, and hands them to the LLM before it answers. Without the librarian, the LLM guesses. With the librarian, it cites your actual content.

## How It Works

### The RAG Pipeline

```
User query
    ↓
1. Embed the query (convert to vector)
    ↓
2. Search vector store for relevant chunks
    ↓
3. Retrieve top-k matching chunks
    ↓
4. Send query + retrieved chunks to the model
    ↓
5. Model generates a grounded response with citations
```

Knowledge Bases manages steps 1–4 automatically. You provide the data source and choose a vector store — Bedrock handles ingestion, chunking, embedding, indexing, and retrieval.

### Data Sources

Knowledge Bases can ingest from:

| Source | What it connects to |
|---|---|
| **[S3](../aws/19_amazon_s3.md)** | Documents in a bucket (PDF, TXT, HTML, CSV, MD, DOC, XLS) |
| **Web crawler** | Crawl and index web pages |
| **Confluence** | Atlassian Confluence pages |
| **SharePoint** | Microsoft SharePoint documents |
| **Salesforce** | Salesforce knowledge articles |
| **Custom** | Any source via Lambda connector |

### Chunking Strategies

When documents are ingested, they're split into chunks for embedding:

| Strategy | How it works | Best for |
|---|---|---|
| **Fixed-size** | Split every N tokens with optional overlap | Simple, predictable |
| **Default** | Bedrock decides chunk boundaries | Quick setup |
| **Hierarchical** | Parent-child chunks (large context + precise retrieval) | Long documents |
| **Semantic** | Split at natural topic boundaries | Mixed-topic documents |
| **No chunking** | Treat each file as one chunk | Short documents |

> **Tip:** Start with fixed-size (300 tokens, 20% overlap) for most use cases. Switch to semantic or hierarchical only if retrieval quality is poor.

### Vector Stores

Knowledge Bases needs a vector store to index embeddings:

| Store | Type | Notes |
|---|---|---|
| **Amazon OpenSearch Serverless** | Managed | Default option, no capacity planning |
| **Amazon Aurora PostgreSQL** | Managed | Use if you already run Aurora with pgvector |
| **Amazon Neptune Analytics** | Managed | Graph + vector for relationship-heavy data |
| **Pinecone** | Third-party | Popular dedicated vector DB |
| **MongoDB Atlas** | Third-party | Use if already on MongoDB |
| **Redis Enterprise Cloud** | Third-party | Use if already on Redis |

### Embedding Models

Knowledge Bases uses an embedding model to convert text to vectors. Available on Bedrock:

| Model | Dimensions | Max tokens | Notes |
|---|---|---|---|
| **Titan Embeddings V2** | 256 / 512 / 1024 | 8,192 | Default, cost-effective |
| **Cohere Embed** | 1024 | 512 | Multilingual strength |

### Retrieval and Response

Two ways to use a Knowledge Base:

1. **Retrieve** — get raw chunks back, handle prompting yourself
2. **RetrieveAndGenerate** — get a model-generated answer with citations

```python
import boto3

client = boto3.client("bedrock-agent-runtime", region_name="us-east-1")

# Option 1: Retrieve only (raw chunks)
chunks = client.retrieve(
    knowledgeBaseId="KB_ID",
    retrievalQuery={"text": "What is the refund policy?"}
)

# Option 2: Retrieve + Generate (grounded answer)
response = client.retrieve_and_generate(
    input={"text": "What is the refund policy?"},
    retrieveAndGenerateConfiguration={
        "type": "KNOWLEDGE_BASE",
        "knowledgeBaseConfiguration": {
            "knowledgeBaseId": "KB_ID",
            "modelArn": "arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-sonnet-4-20250514-v1:0"
        }
    }
)

print(response["output"]["text"])
# Includes citations pointing to source documents
```

### Keeping Data Fresh

- **Manual sync** — trigger re-ingestion when data changes
- **Automatic sync** — schedule periodic syncs (for supported sources)
- Incremental sync — only processes new/changed/deleted documents

## Example

Building a support KB from Zendesk article exports stored in S3:

1. Upload article CSV/HTML files to an S3 bucket
2. Create a Knowledge Base in the Bedrock console, point it to the bucket
3. Choose Titan Embeddings V2 and OpenSearch Serverless
4. Sync — Bedrock chunks, embeds, and indexes the articles
5. Query via `RetrieveAndGenerate` — model answers using article content with citations

## Why It Matters

Without RAG, models can only use their training data — they hallucinate when asked about your specific content. Knowledge Bases provides managed RAG so your [agents](36_amazon_bedrock_agents.md) and applications give answers grounded in your actual documents, with citations pointing back to the source.

## Precautions

### MAIN PRECAUTION: Retrieval Quality Depends on Chunking and Embedding Choices
- Bad chunking = irrelevant retrieval = bad answers, even with a great model
- Test retrieval quality with the `Retrieve` API before building the full pipeline
- Iterate on chunk size, overlap, and strategy

### 1. Vector Store Costs
- OpenSearch Serverless has a minimum cost even at zero traffic (collection base charge)
- For POCs, consider this fixed cost in your budget
- Aurora pgvector is cheaper if you already run Aurora

### 2. Document Format Matters
- Clean, well-structured documents retrieve better than messy HTML or scanned PDFs
- Pre-process documents (strip boilerplate, fix formatting) before ingestion
- HTML with clear headings chunks better than flat text walls

### 3. Sync Lag
- Data changes in S3 are not reflected until the next sync
- For real-time data, consider a custom retrieval pipeline instead
- Schedule syncs to match your data update frequency

### 4. Token Limits
- Retrieved chunks consume context window tokens
- More chunks = more grounding but less room for the model to reason
- Default top-k is 5 — tune based on your document density and model context window

---
← Previous: [Amazon Bedrock Guardrails](./02_amazon_bedrock_guardrails.md) | [Overview](./00_ai_overview.md) | Next: [Amazon Bedrock Agents](./04_amazon_bedrock_agents.md) →
