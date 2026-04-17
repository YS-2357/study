---
tags:
  - aws
  - database
created_at: 260417-141847
updated_at: 260417-141847
---

# Amazon DynamoDB — TTL and Session Store

## What It Is

A focused 201-level look at DynamoDB as a session store with TTL (Time to Live). The 101 note covers DynamoDB fundamentals — this note covers how TTL works and what breaks when it's misconfigured.

See also: [Amazon DynamoDB (101)](../../101/service/12_amazon_dynamodb.md)

## How It Works

### TTL

TTL is a DynamoDB feature that auto-deletes items after a specified time. You store a Unix timestamp in a designated TTL attribute. DynamoDB checks that attribute and deletes the item within 48 hours of expiry (usually within minutes).

```
item created → TTL attribute set to (now + session_duration)
                         ↓
             DynamoDB polls TTL attribute
                         ↓
             expires_at < now → item deleted automatically
```

No Lambda, no cron job, no manual cleanup. DynamoDB handles it.

### Setting up TTL (CDK)

```python
from aws_cdk import aws_dynamodb as dynamodb, Duration, RemovalPolicy

table = dynamodb.Table(self, "SessionTable",
    partition_key=dynamodb.Attribute(
        name="session_id",
        type=dynamodb.AttributeType.STRING
    ),
    time_to_live_attribute="expires_at",   # TTL attribute name
    removal_policy=RemovalPolicy.DESTROY,
    billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST
)
```

`time_to_live_attribute` tells DynamoDB which field holds the expiry timestamp. The field must store a **Unix timestamp in seconds** (not milliseconds).

### Writing an item with TTL

```python
import boto3, time

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("SessionTable")

SESSION_TTL_SECONDS = 8 * 60 * 60  # 8 hours

table.put_item(Item={
    "session_id": session_id,
    "history": [],
    "expires_at": int(time.time()) + SESSION_TTL_SECONDS
})
```

`expires_at` is set at write time. DynamoDB reads it to decide when to delete the item.

## Example

### The TTL mismatch bug from today

Two places in the codebase set TTL values:

```python
# CDK stack
SESSION_TTL = 900  # 15 minutes (seconds)

# Lambda session handler
SESSION_TTL_SECONDS = 8 * 60 * 60  # 8 hours (seconds)
```

Both are valid Unix timestamp offsets, but they disagree by a factor of 32. The CDK value (900s) was the intended session window. The Lambda value (8h) was a leftover from an earlier draft.

Result: items persisted for 8 hours instead of 15 minutes. No crash, no error — just silent over-retention.

**Fix:** single-source the TTL value. Define it once in CDK and pass it to Lambda as an environment variable:

```python
# CDK
SESSION_TTL_SECONDS = 900

table = dynamodb.Table(self, "SessionTable",
    time_to_live_attribute="expires_at",
    ...
)

lambda_fn = lambda_.DockerImageFunction(self, "BackendFn",
    environment={
        "SESSION_TTL_SECONDS": str(SESSION_TTL_SECONDS),
        ...
    }
)
```

```python
# Lambda
import os, time

TTL = int(os.environ["SESSION_TTL_SECONDS"])
expires_at = int(time.time()) + TTL
```

One source, one value, no mismatch.

## Why It Matters

TTL is how session stores stay clean without a cleanup job. But TTL values defined in multiple places drift apart. The mismatch won't crash anything — it silently changes session lifetime, retention cost, and cleanup behavior.

> **Tip:** TTL must be a Unix timestamp in **seconds**. A common mistake is writing milliseconds (`time.time() * 1000`) — DynamoDB won't recognize it as expired for decades.

---
← Previous: [AWS SSM Parameter Store](14_aws_ssm_parameter_store.md) | [Overview](00_overview.md) | Next: [Amazon S3](16_amazon_s3.md) →
