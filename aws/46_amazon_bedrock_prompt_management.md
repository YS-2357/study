---
tags:
  - ai
  - aws
  - ml
  - tooling
created_at: 260417-141847
updated_at: 260417-141847
---

# Amazon Bedrock Prompt Management

## What It Is

Amazon Bedrock Prompt Management is a centralized store for creating, versioning, sharing, and deploying prompts across your Bedrock applications.

Instead of hardcoding prompts in application code, you manage them as versioned artifacts in Bedrock — separate from the code that calls them.

## Analogy

AWS SSM Parameter Store, but for prompts. Just as [SSM Parameter Store](14_aws_ssm_parameter_store.md) keeps configuration out of your code and lets you update it without a deploy, Prompt Management keeps prompt text out of your code and lets you iterate on wording, variables, and model settings independently.

## How It Works

### Prompt components

A prompt in Prompt Management consists of:

| Component | What it is |
|---|---|
| **Template text** | The prompt body with `{{variable}}` placeholders |
| **Input variables** | Named slots filled at runtime |
| **Model settings** | Which model, temperature, max tokens, stop sequences |
| **Variant** | A named version of the prompt (e.g., `concise`, `detailed`) |

You can store multiple variants of a prompt in one prompt resource and A/B test them.

### Versioning

- **Draft** — editable, used during development
- **Numbered versions** — immutable snapshots of the template + model settings
- Reference a specific version in code so a prompt change never silently breaks production

### Using a prompt in code

```python
import boto3

client = boto3.client("bedrock-agent-runtime", region_name="us-east-1")

response = client.invoke_flow(
    # -- or call the prompt directly via bedrock-agent --
)
```

Prompts can be referenced by [Flows](45_amazon_bedrock_flows.md) nodes and [Agents](36_amazon_bedrock_agents.md) instruction fields, or invoked directly via the `bedrock-agent` API:

```python
client = boto3.client("bedrock-agent", region_name="us-east-1")

response = client.get_prompt(
    promptIdentifier="PROMPT_ID",
    promptVersion="3"
)

template = response["variants"][0]["templateConfiguration"]["text"]["text"]
```

## Example

A content moderation team maintains a classification prompt. The prompt text evolves through testing — v1 was too strict, v2 reduced false positives, v3 added a new category. Each version is immutable. Production points to v2 while v3 is in staging. When v3 is validated, the alias is updated — no code change required.

## Why It Matters

Prompt quality directly affects application behavior. Without versioning, a prompt edit is invisible in git history and can silently degrade production. Prompt Management makes prompt changes explicit, auditable, and rollback-safe.

| Perspective | Detail |
|---|---|
| Feasibility | Supports multiple variants per prompt for A/B testing |
| Disruption | Version-based references mean production is not affected until an alias is updated |
| Pros & Cons | Decouples prompt iteration from code deploys; adds a dependency on Bedrock for prompt retrieval |
| Differences | Unlike a config file, prompts here are paired with model settings — the "what to say" and "how the model should respond" travel together |

---
← Previous: [Bedrock Flows](45_amazon_bedrock_flows.md) | [Overview](00_overview.md) | Next: [Bedrock Model Evaluation](47_amazon_bedrock_model_evaluation.md) →
