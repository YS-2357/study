---
tags:
  - ai
  - aws
  - ml
created_at: 2026-04-17T14:18:47
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
---

↑ [Overview](./00_ai_overview.md)

# Amazon Bedrock

## What It Is

Amazon Bedrock is a fully managed service that provides API access to foundation models (FMs) from multiple providers — no infrastructure to manage, no model weights to host. You send a prompt via API, get a response, pay per token.

## Analogy

A food court with multiple restaurant stalls. Anthropic, Meta, Amazon, Mistral each have a stall. You walk up to whichever one you want, order (API call), pay per dish (per token), and leave. You never enter the kitchen.

## How It Works

### Two Clients

Bedrock has two separate boto3 clients — like how RDS has a management client to *create* databases and a database driver to *query* them.

| Client | What it does | When you use it |
|---|---|---|
| `bedrock` | Management — list models, manage guardrails, check access | Setup, admin |
| `bedrock-runtime` | Inference — send prompts, get responses | Your app code (99% of the time) |

AWS splits them for least privilege: your app can *call* models without permission to *delete guardrails* or *change model access*.

### Two API Styles

On the runtime side, there are two ways to call a model:

| API | What it does | Use |
|---|---|---|
| `InvokeModel` | Raw call — format JSON differently per provider (Claude ≠ Nova) | Legacy, provider-specific features |
| `Converse` | Unified format — same code for any model, just swap `modelId` | Almost always use this |

### Model Access

Bedrock offers models from multiple providers through a single API:

| Provider | Models | Strengths |
|---|---|---|
| **Anthropic** | Claude (Haiku, Sonnet, Opus) | Reasoning, coding, long context |
| **Amazon** | Nova (Micro, Lite, Pro, Premier) | Cost-effective, multimodal |
| **Meta** | Llama | Open-weight, fine-tunable |
| **Mistral** | Mistral, Mixtral | Fast inference, multilingual |
| **Cohere** | Command, Embed | Enterprise search, embeddings |
| **AI21 Labs** | Jamba | Long context, multilingual |
| **Stability AI** | Stable Diffusion | Image generation |

> **Tip:** Enable model access in the Bedrock console before making API calls. Models are not available by default — you request access per model per region.

### Inference Modes

| Mode | How it works | Use case |
|---|---|---|
| **On-Demand** | Pay per token, no commitment | Development, variable traffic |
| **Cross-Region** | Routes to available capacity across regions | Higher throughput, resilience |
| **Provisioned Throughput** | Reserved model units | Predictable high-volume workloads |
| **Batch** | Submit jobs, results delivered asynchronously | Large-scale offline processing |

### Key Capabilities

**Converse API** — unified API for multi-turn conversations across all text models. Handles message formatting differences between providers so your code stays the same when switching models.

**Custom models** — fine-tune or continue pre-training a base model on your data:
- **Fine-tuning** — adapt a model to your domain with labeled examples
- **Continued pre-training** — teach a model new knowledge from unlabeled data
- Custom models run on dedicated throughput (Provisioned Throughput required)

**Model evaluation** — compare models on your tasks using automatic metrics or human reviewers directly in the console.

### The Bedrock Ecosystem

Bedrock is both a model access layer and a platform. Other Bedrock services build on top of it:

| Service | What it adds |
|---|---|
| [Knowledge Bases](./03_amazon_bedrock_knowledge_bases.md) | RAG — connect models to your data |
| [Agents](./04_amazon_bedrock_agents.md) | Managed agent builder with action groups |
| [AgentCore](./10_amazon_bedrock_agentcore.md) | Production infrastructure for any agent framework |
| [Guardrails](./02_amazon_bedrock_guardrails.md) | Input/output filtering and PII protection |

## Example

Calling Claude via the Converse API:

```python
import boto3

client = boto3.client("bedrock-runtime", region_name="us-east-1")

response = client.converse(
    modelId="anthropic.claude-sonnet-4-20250514-v1:0",
    messages=[
        {"role": "user", "content": [{"text": "Explain VPCs in one sentence."}]}
    ]
)

print(response["output"]["message"]["content"][0]["text"])
```

Switching to Nova — same code, different model ID:

```python
response = client.converse(
    modelId="amazon.nova-pro-v1:0",
    messages=[
        {"role": "user", "content": [{"text": "Explain VPCs in one sentence."}]}
    ]
)
```

## Why It Matters

Bedrock is the foundation layer for all AWS generative AI services. Every other Bedrock service — [Knowledge Bases](./03_amazon_bedrock_knowledge_bases.md), [Agents](./04_amazon_bedrock_agents.md), [AgentCore](./10_amazon_bedrock_agentcore.md), [Guardrails](./02_amazon_bedrock_guardrails.md) — depends on Bedrock for model access. Understanding Bedrock's model landscape and inference modes is prerequisite to using any of them effectively.

## Pricing

Tokens ≈ billing units. ~1 token ≈ 0.75 English words, ~1 token ≈ 0.5 Korean characters.

| Model | Input (per 1M tokens) | Output (per 1M tokens) | Good for |
|---|---|---|---|
| Nova Micro | $0.035 | $0.14 | Simple routing, classification |
| Nova Lite | $0.06 | $0.24 | Multimodal, budget tasks |
| Claude Haiku 3.5 | $0.80 | $4.00 | Fast, best quality/cost ratio |
| Nova Pro | $0.80 | $3.20 | Balanced, multimodal |
| Claude Sonnet 4 | $3.00 | $15.00 | Complex reasoning, best quality |

> **Tip:** For cost-sensitive projects needing good Korean output, Claude Haiku 3.5 or Nova Pro hits the sweet spot. Sonnet is overkill unless you need top-tier reasoning.

## Precautions

### MAIN PRECAUTION: Model Access Is Per-Region and Per-Model
- You must explicitly enable each model in each region via the console
- Not all models are available in all regions
- Start in `us-east-1` or `us-west-2` for broadest availability

### 1. Pricing Varies Dramatically
- Input/output token prices differ by 10–100x across models
- Haiku/Nova Micro for simple tasks, Sonnet/Opus for complex reasoning
- Use batch inference for non-real-time workloads to reduce cost

### 2. Data Privacy
- AWS does not use your Bedrock inputs/outputs to train models
- Data encrypted in transit (TLS) and at rest (KMS)
- Use VPC endpoints to keep traffic off the public internet
- Data stays in your selected region

### 3. Rate Limits
- On-Demand has per-account token-per-minute limits
- Request quota increases early if you expect high traffic
- Cross-Region inference helps with throughput but adds complexity

---
↑ [Overview](./00_ai_overview.md)

**Related:** [Amazon Bedrock Guardrails](./02_amazon_bedrock_guardrails.md), [Knowledge Bases](./03_amazon_bedrock_knowledge_bases.md), [Agents](./04_amazon_bedrock_agents.md), [AgentCore](./10_amazon_bedrock_agentcore.md)
**Tags:** #ai #aws #ml
