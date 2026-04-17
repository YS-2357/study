---
tags:
  - ai
  - aws
  - ml
  - computing
created_at: 260417-141847
updated_at: 260417-141847
---

# Amazon Bedrock Custom Models

## What It Is

Amazon Bedrock Custom Models lets you adapt a base foundation model to your domain by training it further on your data — either through fine-tuning on labeled examples or continued pre-training on unlabeled text.

## Analogy

A new hire who went through general training (the base model) now goes through your company's onboarding program (your data). After onboarding, they speak your jargon, follow your processes, and write in your tone — while still having all the general skills from before.

## How It Works

### Two customization methods

| Method | Input data | What it teaches | When to use |
|---|---|---|---|
| **Fine-tuning** | Labeled prompt-response pairs | How to respond to specific tasks | Task adaptation: classification, summarization in a specific style, following a format |
| **Continued pre-training** | Unlabeled text corpus | Domain knowledge and vocabulary | Knowledge injection: proprietary manuals, industry-specific language, internal documentation |

### Supported base models

Not all Bedrock models support customization. As of 2025, AWS Nova models (Micro, Lite, Pro) and Amazon Titan models support fine-tuning. Anthropic Claude models do not support Bedrock-managed fine-tuning — use Anthropic's own fine-tuning API for Claude.

### Training data format

Fine-tuning uses JSONL files stored in S3:

```jsonl
{"prompt": "Classify this review as positive or negative: 'Delivery was fast and product works great.'", "completion": "positive"}
{"prompt": "Classify this review as positive or negative: 'Stopped working after one week.'", "completion": "negative"}
```

Continued pre-training uses plain text files in S3:

```
Our platform uses a proprietary message format called PMF-3. Each PMF-3 message
contains a header block, a routing table, and a payload section...
```

### After training: Provisioned Throughput

Custom models cannot be called with On-Demand inference. You must purchase **Provisioned Throughput** — reserved model capacity billed by the hour — to serve requests against your custom model.

This is the main cost difference from base models:

| | Base model | Custom model |
|---|---|---|
| Inference billing | Per token | Hourly (Provisioned Throughput) |
| Minimum commitment | None | 1 month or 6 months |
| Cost | Low for variable traffic | Justified only at sustained high volume |

### Model import

Beyond fine-tuning, Bedrock also supports **Custom Model Import** — bring your own weights (Llama, Mistral, or other compatible open-weight models) and serve them through the Bedrock API without managing inference infrastructure.

## Example

A legal firm fine-tunes Nova Lite on 10,000 contract review examples. The custom model learns to output structured JSON with `{"clause_type": "...", "risk_level": "...", "summary": "..."}` for every clause. The base Nova Lite produces inconsistent formats; the fine-tuned version follows the schema on 97% of inputs.

## Why It Matters

Base models are generalists. Fine-tuning makes them specialists: consistent output formats, domain vocabulary, task-specific accuracy — without relying on long system prompts that consume tokens on every call. The tradeoff is cost and operational overhead from Provisioned Throughput.

| Perspective | Detail |
|---|---|
| Feasibility | Requires minimum training dataset size (typically 100+ examples for fine-tuning); model must support customization |
| Disruption | Training jobs are offline; swapping a custom model for a base model requires a code change to `modelId` |
| Pros & Cons | Higher accuracy and consistency for specific tasks; Provisioned Throughput is expensive at low volume |
| Differences | Fine-tuning changes model weights; [Prompt Management](46_amazon_bedrock_prompt_management.md) and few-shot prompting keep weights frozen — try prompting approaches before committing to fine-tuning |

---
← Previous: [Bedrock Data Automation](48_amazon_bedrock_data_automation.md) | [Overview](00_overview.md) | Next: [Overview](00_overview.md) →
