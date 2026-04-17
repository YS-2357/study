---
tags:
  - aws
  - serverless
  - computing
created_at: 260417-141847
updated_at: 260417-141847
---

# AWS Lambda

## What It Is

AWS Lambda is a serverless compute service that runs code in response to events without you managing servers, and it scales automatically with pay-per-use pricing, as described in the [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html). In practice, a Lambda function is the small unit of code you deploy so AWS can run one job when an event arrives, as explained in [How Lambda works](https://docs.aws.amazon.com/lambda/latest/dg/concepts-basics.html).

## Analogy

A vending machine for backend code. You do not keep a cook standing in the kitchen all day. You put in a request, Lambda wakes up the right function, does the work, and stops when it is done.

## How It Works

You package code and dependencies as either a `.zip` archive or a container image, because Lambda supports those two deployment package types according to the [packaging documentation](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html). Each function has one handler entry point that receives an event object and returns a response, which is the core programming model described in [How Lambda works](https://docs.aws.amazon.com/lambda/latest/dg/concepts-basics.html).

Lambda can be invoked in three common ways:

| Invocation style | What happens | Common examples |
|---|---|---|
| Direct synchronous invoke | Caller waits for the result | API Gateway, function URL, SDK call |
| Direct asynchronous invoke | Lambda queues the event and processes it later | EventBridge, SNS |
| Event source mapping | Lambda polls a queue or stream and invokes your function with batches | SQS, Kinesis, DynamoDB Streams |

These invocation patterns are described in the [invocation methods guide](https://docs.aws.amazon.com/lambda/latest/dg/lambda-invocation.html) and the [event-driven architectures guide](https://docs.aws.amazon.com/lambda/latest/dg/concepts-event-driven-architectures.html).

For standard Lambda functions, one invocation can run for up to 15 minutes, memory can be configured up to 10,240 MB, and AWS automatically scales concurrency until you hit your account or function limits, as documented in [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html) and [Lambda concurrency](https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html).

```text
Event happens
  → Lambda receives or pulls the event
    → Lambda starts an execution environment
      → handler(event, context) runs
        → function returns response or error
          → Lambda stops or reuses the environment later
```

> **Tip:** Design Lambda handlers to be stateless and idempotent. Event source mappings can deliver records more than once, so duplicate processing is a normal possibility according to the [event source mapping guide](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html).

## Example

A frontend sends `POST /chat` to [Amazon API Gateway](10_amazon_api_gateway.md), which invokes a Lambda function. The function reads the request body, calls [Amazon Bedrock](04_amazon_bedrock.md), and returns a JSON response.

```python
import json

def handler(event, context):
    body = json.loads(event["body"])
    message = body["message"]

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"reply": f"Received: {message}"})
    }
```

If this function later grows large ML dependencies, the code can stay conceptually the same while the packaging moves to [Lambda Container Images](11_lambda_container_images.md).

## Why It Matters

AWS Lambda is the compute layer that makes the rest of this subtree fit together. [Amazon API Gateway](10_amazon_api_gateway.md) gives Lambda a public HTTP entry point, [Amazon CloudWatch](08_amazon_cloudwatch.md) captures its logs and metrics, and [Lambda Container Images](11_lambda_container_images.md) handle larger dependency sets. If you understand Lambda first, the surrounding AWS 201 notes read as supporting infrastructure around one event-driven execution model.

---
← Previous: [Amazon CloudWatch](08_amazon_cloudwatch.md) | [Overview](00_overview.md) | Next: [boto3](25_boto3.md) →
