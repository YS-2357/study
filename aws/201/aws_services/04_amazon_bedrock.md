# Amazon Bedrock

## What It Is

Amazon Bedrock is a fully managed service that provides API access to foundation models (FMs) from multiple providers — no infrastructure to manage, no model weights to host.

## How It Works

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
| [Knowledge Bases](05_amazon_bedrock_knowledge_bases.md) | RAG — connect models to your data |
| [Agents](06_amazon_bedrock_agents.md) | Managed agent builder with action groups |
| [AgentCore](02_amazon_bedrock_agentcore.md) | Production infrastructure for any agent framework |
| [Guardrails](03_amazon_bedrock_guardrails.md) | Input/output filtering and PII protection |

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

Bedrock is the foundation layer for all AWS generative AI services. Every other Bedrock service — [Knowledge Bases](05_amazon_bedrock_knowledge_bases.md), [Agents](06_amazon_bedrock_agents.md), [AgentCore](02_amazon_bedrock_agentcore.md), [Guardrails](03_amazon_bedrock_guardrails.md) — depends on Bedrock for model access. Understanding Bedrock's model landscape and inference modes is prerequisite to using any of them effectively.

## Precautions

### ⚠️ MAIN PRECAUTION: Model Access Is Per-Region and Per-Model
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
← Previous: [Amazon Bedrock Guardrails](03_amazon_bedrock_guardrails.md) | [Overview](00_overview.md) | Next: [Amazon Bedrock Knowledge Bases](05_amazon_bedrock_knowledge_bases.md) →
