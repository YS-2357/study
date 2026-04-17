---
tags:
  - aws
  - container
---

# Amazon ECR (Elastic Container Registry)

## What It Is

Amazon ECR is a managed Docker container registry. When you package Lambda as a container image, that image lives in ECR. Lambda pulls from ECR when it needs to run your function.

## How It Works

### Role in the Lambda container pipeline

```
docker build (local or CI)
  → docker push → ECR repository
    → Lambda function points to ECR image URI
      → Lambda pulls image on cold start
```

ECR is the storage layer between your build and Lambda's runtime.

### Two registry types

| Type | What it is |
|------|-----------|
| **Private** | Your account's registry. Access controlled by IAM. |
| **Public** | Public Gallery (`public.ecr.aws`). AWS base images live here. |

Your Lambda images go to a private repository. AWS's base images (e.g. `public.ecr.aws/lambda/python:3.11`) come from the public registry.

### CDK — automatic ECR management

When you use `DockerImageCode.from_image_asset`, CDK handles the full pipeline:

```python
from aws_cdk import aws_lambda as lambda_

backend_fn = lambda_.DockerImageFunction(self, "BackendFn",
    code=lambda_.DockerImageCode.from_image_asset("./backend")
)
```

What CDK does automatically:
1. Creates an ECR repository in your account
2. Builds the Docker image from `./backend/Dockerfile`
3. Pushes the image to ECR
4. Configures Lambda to pull from that ECR URI
5. On `cdk destroy`: deletes the ECR repository and image

You never run `docker build` or `docker push` manually.

### Manual workflow (without CDK)

If managing ECR manually:

```bash
# Authenticate Docker to ECR
aws ecr get-login-password --region us-east-1 \
  | docker login --username AWS --password-stdin \
    123456789.dkr.ecr.us-east-1.amazonaws.com

# Create repository
aws ecr create-repository --repository-name my-lambda

# Build and push
docker build -t my-lambda ./backend
docker tag my-lambda:latest 123456789.dkr.ecr.us-east-1.amazonaws.com/my-lambda:latest
docker push 123456789.dkr.ecr.us-east-1.amazonaws.com/my-lambda:latest
```

With CDK, none of this is needed — `cdk deploy` does it.

### Image URI format

```
<account_id>.dkr.ecr.<region>.amazonaws.com/<repository>:<tag>
```

Example:
```
123456789.dkr.ecr.us-east-1.amazonaws.com/cs-ai-backend:latest
```

Lambda's function configuration points to this URI.

## Example

Full flow with CDK:

```
cdk deploy
  → CDK sees DockerImageCode.from_image_asset("./backend")
  → builds ./backend/Dockerfile
  → creates ECR repo: cs-ai-backendFn-<hash>
  → pushes image: 123456789.dkr.ecr.us-east-1.amazonaws.com/cs-ai-backendFn-<hash>:latest
  → creates Lambda pointing to that URI
  → on cdk destroy: Lambda deleted → ECR repo deleted → image deleted
```

## Why It Matters

ECR is why Lambda container images stay within your account and don't rely on external registries at runtime. Lambda has direct, low-latency access to ECR images in the same region. It's also why `cdk destroy` cleanly removes the image — ECR is CDK-managed, not a manually created orphan.

> **Tip:** ECR images are pulled on Lambda cold start. Large images (1–2 GB) increase cold start time. Keep your Docker layers ordered from least-changed (base image, system deps) to most-changed (your code) to maximize layer caching.

---
← Previous: [Amazon CloudFront](17_amazon_cloudfront.md) | [Overview](00_overview.md) | Next: [DynamoDB Workflow Status Tracking](19_amazon_dynamodb_workflow_status_tracking.md) →
