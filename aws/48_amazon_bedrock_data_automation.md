---
tags:
  - aws
  - ml
  - storage
created_at: 260417-141847
updated_at: 260417-141847
---

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

| Mode                | What it does                                                                       |
| ------------------- | ---------------------------------------------------------------------------------- |
| **Standard output** | Predefined extractions: text, tables, key-value pairs, bounding boxes, transcripts |
| **Custom output**   | You define a JSON schema; BDA extracts exactly those fields using a blueprint      |

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

BDA processes asynchronously: `InvokeDataAutomationAsync` reads input from an Amazon Simple Storage Service ([Amazon S3](../aws/19_amazon_s3.md)) URI and stores output in the S3 bucket or prefix that you specify in `outputConfiguration` ([AWS API Reference](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation-runtime_InvokeDataAutomationAsync.html)). You then call `GetDataAutomationStatus`; when the status is `Success`, the response points to the S3 location where the output can be retrieved ([AWS API Reference](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation-runtime_GetDataAutomationStatus.html)).

### How S3 connects

S3 is the handoff layer between your files and BDA:

| S3 role                     | What goes there                                                        | Why it matters                                                                                                                                                                                                                                       |
| --------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Input bucket or prefix**  | Source PDFs, images, audio, or video                                   | BDA does not need the file bytes embedded in the async request; the request points to `s3://bucket/prefix-or-object`                                                                                                                                 |
| **Output bucket or prefix** | JSON output, extracted fields, metadata, and modality-specific results | Downstream jobs can read the structured output from S3 without calling BDA again                                                                                                                                                                     |
| **IAM permissions**         | Read access to input objects and write access to the output prefix     | Amazon Bedrock S3 access commonly requires `s3:GetObject`, `s3:ListBucket`, and `s3:PutObject`, plus AWS KMS permissions if the bucket uses a KMS key ([AWS User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/s3-bucket-access.html)) |

The common pattern is: upload raw files to an input prefix, invoke BDA with that input S3 URI and an output S3 URI, wait for the invocation to finish, then let [AWS Lambda](09_aws_lambda.md), Glue, Athena, or an application read the JSON results from S3.

## Example

Extracting invoice fields from a batch of PDFs:

1. Upload PDFs to `s3://my-bucket/invoices/raw/`
2. Create a blueprint with the schema: `{ "vendor_name", "invoice_number", "total_amount", "due_date" }`
3. Create a BDA project and attach the blueprint
4. Submit an async job with `inputConfiguration.s3Uri` set to the raw input prefix and `outputConfiguration.s3Uri` set to `s3://my-bucket/invoices/extracted/`
5. Poll `GetDataAutomationStatus` with the returned invocation ARN
6. Read the extracted JSON output from the S3 output prefix

```python
import boto3

client = boto3.client("bedrock-data-automation-runtime", region_name="us-east-1")

response = client.invoke_data_automation_async(
    inputConfiguration={"s3Uri": "s3://my-bucket/invoices/raw/"},
    outputConfiguration={"s3Uri": "s3://my-bucket/invoices/extracted/"},
    dataAutomationConfiguration={"dataAutomationProjectArn": "arn:aws:..."},
    dataAutomationProfileArn="arn:aws:..."
)

invocation_arn = response["invocationArn"]
status = client.get_data_automation_status(invocationArn=invocation_arn)
```

## Why It Matters

Processing documents at scale with custom extraction code is fragile — every new document layout breaks the parser. BDA uses foundation models to understand layout and context, so it handles format variations without per-layout code. It replaces brittle regex or OCR pipelines for Intelligent Document Processing (IDP) workloads.

| Perspective | Detail |
|---|---|
| Feasibility | Handles multi-page PDFs, tables, handwriting, and mixed layouts; video/audio add transcription and scene extraction |
| Disruption | Async-only — not suitable for real-time extraction needs |
| Pros & Cons | No ML training required; accuracy depends on blueprint quality and document consistency |
| Differences | Unlike [Knowledge Bases](35_amazon_bedrock_knowledge_bases.md) which chunks and indexes for retrieval, BDA extracts specific structured fields from each document |

---
← Previous: [Bedrock Model Evaluation](47_amazon_bedrock_model_evaluation.md) | [Overview](00_overview.md) | Next: [Bedrock Custom Models](49_amazon_bedrock_custom_models.md) →
