---
tags:
  - aws
  - tooling
created_at: 2026-04-17T14:18:47
updated_at: 2026-04-18T11:46:13
recent_editor: CLAUDE
---

↑ [Overview](./00_aws_overview.md)

# boto3

## What It Is

boto3 is the official [AWS](./00_aws_overview.md) SDK for Python. It lets Python code call any AWS service API — creating S3 buckets, reading DynamoDB items, invoking Bedrock models — without manually signing HTTP requests.

## Name

**boto** is the [Amazon river dolphin](https://en.wikipedia.org/wiki/Amazon_river_dolphin) (*Inia geoffrensis*), a pink freshwater dolphin native to the Amazon River — a nod to AWS's Amazon branding. The original Python SDK was named `boto`, followed by `boto2`, and then `boto3` as a complete rewrite released in 2015. The **3** means third generation, not Python 3.

## How It Works

boto3 exposes two interfaces:

| Interface | Call | Style | When to use |
|-----------|------|-------|-------------|
| `client` | `boto3.client("service")` | Low-level, mirrors AWS API 1:1 | Full control, all API params available |
| `resource` | `boto3.resource("service")` | High-level, object-oriented | Simpler CRUD on S3, DynamoDB, EC2 |

**Credential resolution order** (boto3 checks each in sequence):

1. Explicit `aws_access_key_id` / `aws_secret_access_key` arguments
2. Environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`)
3. `~/.aws/credentials` file
4. IAM role attached to the compute resource (Lambda, EC2, ECS task)

On AWS compute (Lambda, EC2), boto3 picks up the attached IAM role automatically — no credentials to manage in code.

**Service name strings** map to AWS service endpoints:

| String | Service |
|--------|---------|
| `"s3"` | Amazon S3 |
| `"dynamodb"` | Amazon DynamoDB |
| `"bedrock-runtime"` | [Amazon Bedrock](34_amazon_bedrock.md) inference |
| `"bedrock-agent-runtime"` | Bedrock Agents / Knowledge Bases / Flows |
| `"cloudwatch"` | [Amazon CloudWatch](08_amazon_cloudwatch.md) |
| `"ssm"` | [AWS SSM Parameter Store](14_aws_ssm_parameter_store.md) |

## Example

```python
import boto3

# List all S3 buckets in the account
s3 = boto3.client("s3", region_name="us-east-1")
response = s3.list_buckets()
for bucket in response["Buckets"]:
    print(bucket["Name"])
```

```python
import boto3

# DynamoDB resource interface — object-oriented
dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
table = dynamodb.Table("Users")
item = table.get_item(Key={"user_id": "abc123"})
print(item["Item"])
```

## Why It Matters

Every Python-based service in this repo that touches AWS uses boto3 — Bedrock inference, DynamoDB reads/writes, CloudWatch metrics, SSM config lookup. Understanding the `client` vs `resource` split and the credential resolution order prevents the two most common runtime errors: wrong service name string and missing IAM permissions.

| Perspective | Detail |
|-------------|--------|
| Feasibility | Covers all AWS services; some newer services only expose a `client`, not a `resource` |
| Pros & Cons | Zero boilerplate for auth on AWS compute; local dev requires credential setup via `~/.aws` or env vars |
| Differences | boto3 is Python-only; other languages use separate SDKs (`aws-sdk-js`, `aws-sdk-go`, etc.) — all wrap the same underlying REST APIs |

---
← Previous: [AWS Lambda](09_aws_lambda.md) | [Overview](./00_aws_overview.md) | Next: [Amazon API Gateway](10_amazon_api_gateway.md) →
