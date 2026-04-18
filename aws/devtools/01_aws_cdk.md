---
tags:
  - aws
  - infrastructure
  - tooling
created_at: 2026-04-17T14:18:47
updated_at: 2026-04-18T11:46:13
recent_editor: CLAUDE
---

↑ [Overview](./00_aws_overview.md)

# AWS CDK (Cloud Development Kit)

## What It Is

AWS CDK is an infrastructure-as-code framework that lets you define AWS resources in a programming language (Python, TypeScript, etc.) instead of clicking through the console. One command deploys everything, one command deletes everything.

## Analogy

The console is like building furniture by hand — click, configure, click. CDK is like having a blueprint. You write the blueprint once in Python, and `cdk deploy` builds all the furniture. `cdk destroy` disassembles it all. Same result, but repeatable and version-controlled.

## How It Works

### The Flow

```
You write Python code (stacks with resource definitions)
        ↓
cdk synth   →  generates CloudFormation template
        ↓
cdk deploy  →  CloudFormation creates actual AWS resources
        ↓
cdk destroy →  CloudFormation deletes everything
```

CDK is a wrapper around CloudFormation. You write Python, CDK converts it to CloudFormation, CloudFormation talks to AWS.

### Installation

CDK has two parts: the CLI (Node.js) and your infrastructure code (Python). Both are needed.

```bash
# 1. CDK CLI — runs on Node.js
node --version                # check if Node.js is installed
npm install -g aws-cdk        # install CDK CLI
cdk --version                 # verify

# 2. Your CDK code — written in Python
python3 --version             # check if Python is installed
pip install aws-cdk-lib       # install CDK Python library
```

> **Tip:** Node.js is only for the CLI tool. All your infrastructure code is Python.

### Project Setup

```bash
mkdir my-project && cd my-project
cdk init app --language python
```

Generated structure:

```
my-project/
├── app.py                      ← entry point
├── my_project/
│   └── my_project_stack.py     ← infrastructure code goes here
├── requirements.txt
└── cdk.json                    ← CDK config
```

### Three Commands

| Command | What it does |
|---|---|
| `cdk synth` | Preview — generates CloudFormation template, no changes to AWS |
| `cdk deploy` | Create or update all resources |
| `cdk destroy` | Delete everything in the stack |

First time in a new account/region:

```bash
cdk bootstrap   # one-time setup, creates a staging bucket for CDK
```

### Key Concepts

- **App** — top-level container, holds one or more stacks
- **Stack** — a deployable unit (maps to one CloudFormation stack)
- **Construct** — a resource or group of resources (S3 bucket, Lambda, etc.)

### Construct Levels

| Level | What it is | When to use |
|---|---|---|
| **L1** | Raw CloudFormation (1:1 mapping, verbose) | Rarely — only when L2 doesn't exist |
| **L2** | Opinionated defaults, simpler API | 90% of the time |
| **L3** | Patterns combining multiple resources | Common architectures (e.g., `LambdaRestApi`) |

## Example

### S3 Bucket

```python
from aws_cdk import Stack, RemovalPolicy, aws_s3 as s3
from constructs import Construct

class CsAiStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        bucket = s3.Bucket(self, "ArticlesBucket",
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )
```

| Parameter | Value | Why |
|---|---|---|
| `removal_policy` | `DESTROY` | `cdk destroy` actually deletes the bucket. Default `RETAIN` keeps it. |
| `auto_delete_objects` | `True` | Empties bucket before deleting. Without this, destroy fails if bucket has files. |
| `bucket_name` | (omitted) | CDK auto-generates a unique name. Avoids global uniqueness headache. |
| `versioned` | (omitted, default `False`) | No need for version history in POC. Enable if you want rollback on articles. |
| `encryption` | (omitted, default `S3_MANAGED`) | SSE-S3 encryption, free, sufficient for POC. |

### IAM Roles and Grants

CDK auto-generates IAM policies via `grant` methods — you don't write policy JSON yourself:

```python
from aws_cdk import aws_iam as iam

# Create a role that Bedrock can assume
kb_role = iam.Role(self, "KbRole",
    assumed_by=iam.ServicePrincipal("bedrock.amazonaws.com")
)

# Grant read access — CDK generates the s3:GetObject policy automatically
bucket.grant_read(kb_role)
```

| Parameter | Value | Why |
|---|---|---|
| `assumed_by` | `ServicePrincipal("bedrock.amazonaws.com")` | Which service can assume this role. Use `"ecs-tasks.amazonaws.com"` for Fargate. |
| `grant_read` | `bucket.grant_read(role)` | Auto-generates `s3:GetObject` + `s3:ListBucket`. No manual policy JSON. |
| `grant_read_write` | `bucket.grant_read_write(role)` | Adds `s3:PutObject`, `s3:DeleteObject` on top of read. |

### OpenSearch Serverless

Vector database for RAG retrieval. Needs three resources: encryption policy, network policy, then the collection.

```python
from aws_cdk import aws_opensearchserverless as oss

# 1. Encryption policy (required)
enc_policy = oss.CfnSecurityPolicy(self, "EncPolicy",
    name="cs-ai-enc",
    type="encryption",
    policy='{"Rules":[{"ResourceType":"collection","Resource":["collection/cs-ai-articles"]}],"AWSOwnedKey":true}'
)

# 2. Network policy (public access for POC)
net_policy = oss.CfnSecurityPolicy(self, "NetPolicy",
    name="cs-ai-net",
    type="network",
    policy='[{"Rules":[{"ResourceType":"collection","Resource":["collection/cs-ai-articles"]},{"ResourceType":"dashboard","Resource":["collection/cs-ai-articles"]}],"AllowFromPublic":true}]'
)

# 3. Collection
collection = oss.CfnCollection(self, "ArticlesCollection",
    name="cs-ai-articles",
    type="VECTORSEARCH"
)
collection.add_dependency(enc_policy)
collection.add_dependency(net_policy)
```

| Parameter | Value | Why |
|---|---|---|
| `name` | `"cs-ai-articles"` | Collection name. Must match the name in encryption/network policies. |
| `type` | `"VECTORSEARCH"` | Makes it a vector DB. Other options: `SEARCH` (text), `TIMESERIES`. |
| `AWSOwnedKey` | `true` | Free AWS-managed encryption key. Use `false` + custom KMS for more control. |
| `AllowFromPublic` | `true` | Public access for POC simplicity. Use VPC endpoint for production. |
| `add_dependency` | enc/net policies | Policies must exist before collection. CDK doesn't auto-detect this for L1. |

### Bedrock Knowledge Base

Connects S3 (articles) → embedding model (Titan) → OpenSearch (vector store). The RAG pipeline.

```python
from aws_cdk import aws_bedrock as bedrock

kb = bedrock.CfnKnowledgeBase(self, "SupportKB",
    name="cs-support-kb",
    role_arn=kb_role.role_arn,
    knowledge_base_configuration={
        "type": "VECTOR",
        "vectorKnowledgeBaseConfiguration": {
            "embeddingModelArn": f"arn:aws:bedrock:us-east-1::foundation-model/amazon.titan-embed-text-v2:0"
        }
    },
    storage_configuration={
        "type": "OPENSEARCH_SERVERLESS",
        "opensearchServerlessConfiguration": {
            "collectionArn": collection.attr_arn,
            "vectorIndexName": "articles-index",
            "fieldMapping": {
                "vectorField": "embedding",
                "textField": "text",
                "metadataField": "metadata"
            }
        }
    }
)
```

| Parameter | Value | Why |
|---|---|---|
| `role_arn` | `kb_role.role_arn` | IAM role KB uses to access S3 and OpenSearch. |
| `type` | `"VECTOR"` | Vector-based knowledge base for RAG. |
| `embeddingModelArn` | Titan Embed V2 | Cheapest embedding model. Cohere Embed is alternative for multilingual. |
| `vectorIndexName` | `"articles-index"` | Index name inside OpenSearch. You create this index separately. |
| `vectorField` | `"embedding"` | OpenSearch field that stores the vector. |
| `textField` | `"text"` | OpenSearch field that stores the original text chunk. |
| `metadataField` | `"metadata"` | OpenSearch field for title, URL, date — used for citations. |

Then connect the S3 data source:

```python
bedrock.CfnDataSource(self, "ArticlesSource",
    knowledge_base_id=kb.attr_knowledge_base_id,
    name="zendesk-articles",
    data_source_configuration={
        "type": "S3",
        "s3Configuration": {
            "bucketArn": bucket.bucket_arn
        }
    }
)
```

| Parameter | Value | Why |
|---|---|---|
| `type` | `"S3"` | Data source type. Also supports web crawler, Confluence, SharePoint. |
| `bucketArn` | `bucket.bucket_arn` | Points to your articles bucket. CDK resolves the ARN automatically. |

- After deploy, trigger a sync to ingest articles
- L1 constructs (`Cfn` prefix) — Bedrock CDK is still L1 level

### Guardrails

PII filtering layer. Checks input and output around model calls.

```python
guardrail = bedrock.CfnGuardrail(self, "PiiGuardrail",
    name="cs-pii-guardrail",
    blocked_input_messaging="입력에 개인정보가 포함되어 처리할 수 없습니다.",
    blocked_outputs_messaging="응답에 개인정보가 포함되어 제거되었습니다.",
    sensitive_information_policy_config={
        "piiEntitiesConfig": [
            {"type": "EMAIL", "action": "ANONYMIZE"},
            {"type": "PHONE", "action": "ANONYMIZE"},
            {"type": "NAME", "action": "ANONYMIZE"},
            {"type": "CREDIT_DEBIT_CARD_NUMBER", "action": "BLOCK"},
        ]
    }
)
```

| Parameter | Value | Why |
|---|---|---|
| `blocked_input_messaging` | Korean message | Shown to user when input is blocked. |
| `blocked_outputs_messaging` | Korean message | Shown to user when output is blocked. |
| `type` | `"EMAIL"`, `"PHONE"`, etc. | PII entity type to detect. Full list: NAME, ADDRESS, SSN, CREDIT_DEBIT_CARD_NUMBER, etc. |
| `action` | `"ANONYMIZE"` | Replaces PII with placeholders (`[EMAIL]`). Alternative: `"BLOCK"` rejects entire request. |

### Fargate (FastAPI Backend)

Serverless container hosting for your API server.

```python
from aws_cdk import (
    aws_ecs as ecs,
    aws_ecs_patterns as patterns,
)

cluster = ecs.Cluster(self, "ApiCluster", vpc=vpc)

api_service = patterns.ApplicationLoadBalancedFargateService(self, "ApiService",
    cluster=cluster,
    task_image_options=patterns.ApplicationLoadBalancedTaskImageOptions(
        image=ecs.ContainerImage.from_asset("./backend"),
        container_port=8000,
        environment={"KB_ID": kb.attr_knowledge_base_id}
    ),
    cpu=256,
    memory_limit_mib=512,
    desired_count=1
)
```

| Parameter | Value | Why |
|---|---|---|
| `image` | `from_asset("./backend")` | Builds Docker image from your backend folder. Also supports ECR images. |
| `container_port` | `8000` | FastAPI default port. Must match your Uvicorn config. |
| `environment` | `{"KB_ID": ...}` | Env vars passed to container. Use for config, not secrets. |
| `cpu` | `256` | 0.25 vCPU — smallest Fargate size. See [Fargate CPU/memory combos](../aws/26_aws_fargate.md). |
| `memory_limit_mib` | `512` | 512 MB — minimum for 256 CPU. Cheapest option. |
| `desired_count` | `1` | One task for POC. Increase for HA. |

### Full Resource Map

What CDK creates for your project:

| Resource | CDK construct level | Cost concern |
|---|---|---|
| S3 bucket | L2 | Negligible |
| OpenSearch Serverless | L1 | Highest — destroy when not testing |
| Knowledge Base | L1 | Per query |
| Guardrails | L1 | Per assessment |
| Fargate + ALB | L3 | Per hour while running |
| IAM roles | L2 | Free |
| Tags | Built-in | Free |

## Why It Matters

CDK makes infrastructure reproducible and deletable. For cost-sensitive projects, `cdk destroy` guarantees you're not paying for forgotten resources. For your 201 project, the assignment requires CDK for all resource creation and deletion.

## Precautions

### MAIN PRECAUTION: cdk destroy May Not Delete Everything
- Some resources have deletion protection by default (S3 buckets with objects, RDS)
- Set `removal_policy=RemovalPolicy.DESTROY` and `auto_delete_objects=True` for S3 buckets you want fully cleaned up
- Always verify with `aws` CLI after destroy

### 1. Bootstrap Once Per Account/Region
- `cdk bootstrap` is required before the first deploy
- Creates a staging S3 bucket and IAM roles
- Forgetting this gives a confusing error on first deploy

### 2. Tags
- Add tags to your stack so all resources inherit them
- Your assignment requires tags on all resources

```python
from aws_cdk import Tags
Tags.of(self).add("Project", "cs-ai-assistant")
Tags.of(self).add("Environment", "dev")
```

### 3. Cost Control
- Always `cdk destroy` when done testing
- Use `cdk diff` before deploy to see what will change
- OpenSearch Serverless has a minimum cost even at 1 OCU — destroy when not in use

---
← Previous: [Amazon Bedrock Agents](36_amazon_bedrock_agents.md) | [Overview](./00_aws_overview.md) | Next: [Amazon CloudWatch](38_amazon_cloudwatch.md) →
