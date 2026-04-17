---
tags:
  - aws
  - container
  - serverless
created_at: 260417-141847
updated_at: 260417-141847
---

# Lambda Container Images

## What It Is

Lambda container images are a packaging format for Lambda functions that replaces the standard zip file. Instead of uploading a zip, you build a Docker image, push it to ECR, and point Lambda at it. The limit jumps from 250 MB (zip, uncompressed) to 10 GB (container image).

## How It Works

### Standard zip vs container image

| | Zip | Container image |
|--|-----|----------------|
| Max size (uncompressed) | 250 MB | 10 GB |
| Package format | `.zip` | Docker image in ECR |
| Build step | `pip install` → zip | `docker build` → `docker push` |
| Cold start | Faster | Slightly slower |
| When to use | Small functions, simple deps | Large ML libs, complex runtimes |

### Build and deploy flow

```
Write Dockerfile
  → docker build (locally or in CI)
    → docker push to ECR
      → Lambda function points to ECR image URI
        → cdk deploy wires it together
```

### Dockerfile structure for Lambda + FastAPI

```dockerfile
FROM public.ecr.aws/lambda/python:3.11

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Lambda handler entry point
CMD ["main.handler"]
```

`main.handler` = the `handler` object in `main.py` (the Mangum-wrapped FastAPI app).

### CDK — Lambda from container image

```python
from aws_cdk import aws_lambda as lambda_
from aws_cdk import aws_ecr_assets as ecr_assets

backend_fn = lambda_.DockerImageFunction(self, "BackendFn",
    code=lambda_.DockerImageCode.from_image_asset("./backend"),
    memory_size=1024,
    timeout=Duration.seconds(30),
    environment={
        "KB_ID": kb.attr_knowledge_base_id,
        "TABLE_NAME": table.table_name
    }
)
```

`from_image_asset` tells CDK to build the Docker image from `./backend`, push it to ECR, and use it as the function code. No manual `docker build` or `docker push` needed.

## Example

Without container images, installing large dependencies (e.g. `boto3`, `strands-agents`, `langchain`, `sentence-transformers`) easily exceeds 250 MB. The solution is not to trim dependencies — it's to use the right packaging format.

```
requirements.txt adds up to ~400 MB unpacked
  → zip packaging fails: exceeds Lambda limit
  → container image: 400 MB is well under 10 GB limit
  → no code changes, only packaging changes
```

## Why It Matters

The packaging decision is a runtime constraint, not a preference. When your dependencies exceed 250 MB, the architecture must use container images regardless of other considerations. Knowing this upfront prevents a late-stage refactor.

> **Tip:** Use `DockerImageFunction` in CDK from the start if your stack includes ML or agent frameworks. Switching from zip to container image mid-project means rewriting the Lambda construct.

---
← Previous: [Amazon API Gateway](39_amazon_api_gateway.md) | [Overview](00_overview.md) | Next: [Mangum](41_mangum.md) →
