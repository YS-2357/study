---
tags:
  - aws
  - serverless
  - tooling
created_at: 2026-04-17T14:18:47
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
---

↑ [Overview](./00_compute_overview.md)

# Mangum

## What It Is

Mangum is an ASGI adapter that lets FastAPI (and other ASGI frameworks) run inside [AWS Lambda](./03_aws_lambda.md). Lambda speaks its own event format; FastAPI speaks ASGI. Mangum translates between them.

## How It Works

When API Gateway invokes a Lambda function, it passes a JSON event — not an HTTP request. FastAPI expects an ASGI-compatible HTTP request. Without an adapter, they can't communicate.

```
API Gateway event (JSON)
  → Mangum translates → ASGI scope (HTTP request)
    → FastAPI handles it → ASGI response
      → Mangum translates → Lambda response (JSON)
        → API Gateway returns to browser
```

Mangum wraps the entire FastAPI app in one line:

```python
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.post("/chat")
async def chat(request: ChatRequest):
    ...

# This is the Lambda handler
handler = Mangum(app)
```

`handler` is what Lambda calls. Everything else is standard FastAPI.

### What Mangum translates

| Lambda event field | ASGI equivalent |
|-------------------|----------------|
| `httpMethod` | HTTP method (GET, POST, etc.) |
| `path` | URL path |
| `headers` | Request headers |
| `body` | Request body |
| `queryStringParameters` | Query string |

On the way back: FastAPI's response (status code, headers, body) becomes the Lambda response JSON that API Gateway returns to the browser.

## Example

`main.py` in the Lambda container:

```python
from fastapi import FastAPI
from mangum import Mangum
from agent import run_agent

app = FastAPI()

@app.post("/chat")
async def chat(body: dict):
    response = await run_agent(body["message"])
    return {"response": response}

@app.get("/health")
async def health():
    return {"status": "ok"}

# Lambda entry point — must match CMD in Dockerfile
handler = Mangum(app)
```

`Dockerfile`:
```dockerfile
CMD ["main.handler"]
```

## Why It Matters

Without Mangum, you would rewrite your entire FastAPI app as raw Lambda handlers — one function per route, manual request parsing, no middleware. Mangum lets you write standard FastAPI and deploy it to Lambda unchanged.

> **Tip:** The `handler` name in `main.py` must match the CMD in the Dockerfile exactly. `CMD ["main.handler"]` means: file `main.py`, object `handler`.

---
↑ [Overview](./00_compute_overview.md)

**Related:** [Lambda Container Images](05_lambda_container_images.md), [AWS Lambda](./03_aws_lambda.md)
**Tags:** #aws #serverless #tooling
