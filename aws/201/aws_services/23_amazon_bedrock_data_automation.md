# Amazon Bedrock Data Automation

## What It Is

Amazon Bedrock Data Automation (BDA) is a managed service that extracts structured information from unstructured content — documents, images, video, and audio — using foundation models, without writing custom extraction pipelines.

## Analogy

A smart document scanner that reads and understands, not just copies. You hand it a stack of PDFs, invoices, or medical forms, and it returns structured JSON with the fields you asked for — not a raw text dump.

## How It Works

### Input types

| Content type | What BDA can process |
|---|---|
| **Documents** | PDF, Word, HTML, CSV, Excel, TXT |
| **Images** | PNG, JPEG, TIFF, WEBP |
| **Video** | MP4, MOV, MKV, and others |
| **Audio** | MP3, WAV, FLAC, and others |

### Two modes

| Mode | What it does |
|---|---|
| **Standard output** | Predefined extractions: text, tables, key-value pairs, bounding boxes, transcripts |
| **Custom output** | You define a JSON schema; BDA extracts exactly those fields using a blueprint |

**Blueprint** — a reusable extraction template for a document type. You create one blueprint per form type (e.g., invoice, insurance claim, lab report) and apply it to all documents of that type.

### Processing flow

```
Documents / images / video / audio in S3
        ↓
BDA project (+ optional blueprint)
        ↓
Async processing job
        ↓
Structured JSON output in S3
```

BDA processes asynchronously. You submit a job, poll for completion (or use EventBridge), and fetch results from S3.

## Example

Extracting invoice fields from a batch of PDFs:

1. Create a blueprint with the schema: `{ "vendor_name", "invoice_number", "total_amount", "due_date" }`
2. Create a BDA project and attach the blueprint
3. Submit an async job pointing at an S3 prefix of PDFs
4. Fetch results — each PDF produces one JSON file with the extracted fields

```python
import boto3

client = boto3.client("bedrock-data-automation-runtime", region_name="us-east-1")

response = client.invoke_data_automation_async(
    inputConfiguration={"s3Uri": "s3://my-bucket/invoices/"},
    outputConfiguration={"s3Uri": "s3://my-bucket/output/"},
    dataAutomationConfiguration={"dataAutomationProjectArn": "arn:aws:..."}
)

invocation_arn = response["invocationArn"]
```

## Why It Matters

Processing documents at scale with custom extraction code is fragile — every new document layout breaks the parser. BDA uses foundation models to understand layout and context, so it handles format variations without per-layout code. It replaces brittle regex or OCR pipelines for Intelligent Document Processing (IDP) workloads.

| Perspective | Detail |
|---|---|
| Feasibility | Handles multi-page PDFs, tables, handwriting, and mixed layouts; video/audio add transcription and scene extraction |
| Disruption | Async-only — not suitable for real-time extraction needs |
| Pros & Cons | No ML training required; accuracy depends on blueprint quality and document consistency |
| Differences | Unlike [Knowledge Bases](05_amazon_bedrock_knowledge_bases.md) which chunks and indexes for retrieval, BDA extracts specific structured fields from each document |

---
← Previous: [Bedrock Model Evaluation](22_amazon_bedrock_model_evaluation.md) | [Overview](00_overview.md) | Next: [Bedrock Custom Models](24_amazon_bedrock_custom_models.md) →
