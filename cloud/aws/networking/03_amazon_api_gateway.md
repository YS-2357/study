---
tags:
  - aws
  - serverless
  - networking
created_at: 2026-04-17T14:18:47
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
---

↑ [Overview](./00_networking_overview.md)

# Amazon API Gateway

## What It Is

Amazon API Gateway is a managed service that sits between the internet and your backend (Lambda, EC2, etc.), handling HTTP routing, throttling, CORS, and authentication. Lambda cannot receive public HTTP traffic directly — API Gateway is the entry point.

## How It Works

API Gateway receives an HTTP request, matches it to a route, and invokes the configured integration (e.g., Lambda). It then returns the integration's response to the caller.

```
Browser → API Gateway → Lambda → response → API Gateway → Browser
```

### Two main variants

| Type | When to use |
|------|-------------|
| **HTTP API** | Simple REST-style routing to Lambda or HTTP backends. Cheaper, lower latency. |
| **REST API** | Full feature set — request/response transformation, API keys, usage plans, WAF. |

HTTP API is sufficient for most Lambda backends. Use REST API only when you need request transformation or API key management.

### Route structure

Routes are defined as `METHOD /path` pairs:

```
POST /chat       → Lambda function
GET  /health     → Lambda function
```

API Gateway passes the full request (headers, body, query params, path) to Lambda as a JSON event. Lambda returns a JSON response with `statusCode`, `headers`, and `body`.

### CORS

API Gateway handles CORS headers for browser clients. Without it, browsers block cross-origin requests to your API.

```python
# CDK — HTTP API with CORS
from aws_cdk import aws_apigatewayv2 as apigw
from aws_cdk import aws_apigatewayv2_integrations as integrations

http_api = apigw.HttpApi(self, "ChatApi",
    cors_preflight=apigw.CorsPreflightOptions(
        allow_origins=["*"],
        allow_methods=[apigw.CorsHttpMethod.POST, apigw.CorsHttpMethod.GET],
        allow_headers=["Content-Type"]
    )
)

http_api.add_routes(
    path="/chat",
    methods=[apigw.HttpMethod.POST],
    integration=integrations.HttpLambdaIntegration("ChatIntegration", handler=lambda_fn)
)
```

### Throttling

API Gateway enforces rate limits before requests reach Lambda:

| Setting | Default |
|---------|---------|
| Burst limit | 5,000 req/s |
| Rate limit | 10,000 req/s |

Configure lower limits to protect against runaway costs or abuse.

## Example

Request flow for a chat message:

```
POST /chat {"message": "my order hasn't arrived"}
  → API Gateway matches POST /chat
  → Invokes Lambda with event:
      {
        "requestContext": {...},
        "body": "{\"message\": \"my order hasn't arrived\"}",
        "headers": {...}
      }
  → Lambda returns:
      {
        "statusCode": 200,
        "body": "{\"response\": \"Let me look that up for you.\"}"
      }
  → API Gateway returns 200 to browser
```

## Why It Matters

Lambda has no public URL by default. API Gateway gives it one. It also decouples the HTTP contract (routes, methods, auth) from the Lambda implementation — you can swap the backend without changing the client-facing API.

> **Tip:** The API Gateway URL is the only thing the frontend needs to know. All routing, auth, and throttling stays in the gateway layer, not in Lambda code.

---
↑ [Overview](./00_networking_overview.md)

**Related:** [Amazon CloudFront](./02_amazon_cloudfront.md), [AWS Shield](./04_aws_shield.md)
**Tags:** #aws #serverless #networking
