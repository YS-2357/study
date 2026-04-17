---
tags:
  - ai
  - aws
  - ml
---

# Amazon Bedrock Model Evaluation

## What It Is

Amazon Bedrock Model Evaluation is a managed service for benchmarking and comparing foundation models on your own tasks — using automatic metrics, a built-in judge model, or human reviewers.

Instead of running ad-hoc tests locally, you submit an evaluation job in Bedrock and get structured scores back.

## Analogy

A standardized exam for models. You write the test questions (your task dataset), all candidate models sit the same exam, and Bedrock scores the answers. You pick the model that scores highest on the criteria you care about.

## How It Works

### Evaluation types

| Type | How scoring works | When to use |
|---|---|---|
| **Automatic** | Built-in metrics computed against a reference dataset | Speed, reproducibility, no human cost |
| **Model-as-judge** | A separate LLM scores each response against criteria | Nuanced quality; no reference answers needed |
| **Human** | Human reviewers score responses in a managed UI | High-stakes decisions, subjective quality |

### Automatic metrics

Bedrock provides task-specific metrics depending on the use case:

| Task | Metrics |
|---|---|
| Text summarization | ROUGE-1, ROUGE-2, ROUGE-L, BERTScore |
| Question answering | Exact match, F1 |
| Text generation | Perplexity, BERTScore |
| Classification | Accuracy |
| RAG / grounded QA | Correctness, faithfulness, answer relevance |

### Job input

You provide:
1. A dataset of prompt-response pairs in S3 (JSONL format)
2. One or more model IDs to evaluate
3. The task type and metrics to compute

Bedrock runs all models against the dataset in parallel and returns aggregated scores.

## Example

Choosing between Claude Haiku 3.5 and Nova Lite for a Korean support chatbot:

1. Collect 200 real support questions with ideal answers → upload to S3 as JSONL
2. Create an evaluation job: both models, task = question answering, metrics = F1 + BERTScore
3. Bedrock runs both models against all 200 questions
4. Results show Nova Lite scores 0.71 F1 vs Haiku 0.79 F1 → choose Haiku despite higher cost

```json
// dataset entry (JSONL)
{"prompt": "반품 정책이 어떻게 되나요?", "referenceResponse": "구매 후 30일 이내에 반품 가능합니다."}
```

## Why It Matters

Picking the wrong model for a task wastes money (too expensive) or degrades quality (too weak). Model Evaluation replaces guesswork with measured scores on your actual workload before you commit to a model in production.

| Perspective | Detail |
|---|---|
| Feasibility | Supports cross-model comparison in a single job; human evaluation requires setting up an AWS Managed workforce or private team |
| Disruption | Evaluation jobs are offline — no impact on production workloads |
| Pros & Cons | Saves manual testing time; automatic metrics only measure what your reference dataset covers |
| Differences | Differs from [Guardrails](03_amazon_bedrock_guardrails.md) contextual grounding check — that is runtime filtering; this is offline benchmarking |

---
← Previous: [Bedrock Prompt Management](21_amazon_bedrock_prompt_management.md) | [Overview](00_overview.md) | Next: [Bedrock Data Automation](23_amazon_bedrock_data_automation.md) →
