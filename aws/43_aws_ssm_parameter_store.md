---
tags:
  - aws
  - security
created_at: 2026-04-17T14:18:47
updated_at: 2026-04-17T14:18:47
recent_editor: CLAUDE
---

↑ [Overview](./00_overview.md)

# AWS SSM Parameter Store

## What It Is

AWS Systems Manager Parameter Store is a managed key-value store for configuration values and secrets. It holds config like API keys, resource IDs, and environment-specific settings that your Lambda (or other services) reads at runtime.

## How It Works

### Two tiers

| Tier | Limit | Cost |
|------|-------|------|
| Standard | 10,000 parameters, 4 KB each | Free |
| Advanced | Higher limits, larger values, policies | Paid |

Standard is sufficient for most application config.

### Two parameter types

| Type | What it stores | Encryption |
|------|---------------|-----------|
| `String` | Plaintext value | None |
| `SecureString` | Encrypted value | KMS key |

Use `SecureString` for anything sensitive (API keys, tokens). Use `String` for non-sensitive config (resource IDs, environment names).

### Reading a parameter at runtime (Lambda)

```python
import boto3

ssm = boto3.client("ssm")

def get_param(name: str) -> str:
    response = ssm.get_parameter(Name=name, WithDecryption=True)
    return response["Parameter"]["Value"]

kb_id = get_param("/cs-ai/kb-id")
```

`WithDecryption=True` is required for `SecureString` parameters. It's harmless for `String` parameters.

### Defining parameters in CDK (correct approach)

```python
from aws_cdk import aws_ssm as ssm

# Create the parameter as part of the stack
kb_param = ssm.StringParameter(self, "KbIdParam",
    parameter_name="/cs-ai/kb-id",
    string_value=kb.attr_knowledge_base_id
)

# Grant Lambda read access
kb_param.grant_read(lambda_fn)
```

The parameter is created by CDK on `cdk deploy` and deleted by CDK on `cdk destroy`.

## Example

### The SSM bug from today

The SSM parameter `/cs-ai/kb-id` was created manually in the AWS console during development. The Lambda read it correctly at runtime — no crash, no error.

The violation: it existed outside CDK. On `cdk destroy`:

```
cdk destroy → deletes Lambda, API Gateway, DynamoDB, OpenSearch...
           → SSM parameter: not in stack → not deleted
           → parameter remains, incurring no direct cost but:
               - holds a stale KB ID pointing to a deleted resource
               - IAM grants for it may persist
               - next deploy may conflict or silently reuse wrong value
```

Fix: move the parameter into the CDK stack. It now lives and dies with the stack.

### Why the reviewer caught it and testing didn't

At runtime the system worked. There was no behavioral failure. The bug was an **ownership violation** — a resource existed outside the IaC boundary. Only a rule-aware check asking "is every resource CDK-managed?" surfaced it.

This is the class of bug that `cdk destroy` exposes later, not immediately.

## Why It Matters

Config that changes per environment (KB IDs, table names, API endpoints) must not be hardcoded. SSM Parameter Store externalizes that config. But it only works correctly if the parameters are CDK-managed — otherwise they become orphans that outlive the stack.

> **Tip:** If a resource is not in the CDK stack, `cdk destroy` doesn't know it exists. IaC boundary = destroy boundary. No exceptions.

---
← Previous: [Amazon OpenSearch](42_amazon_opensearch.md) | [Overview](./00_overview.md) | Next: [DynamoDB TTL and Session Store](12_amazon_dynamodb.md) →
