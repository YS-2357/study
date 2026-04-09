# Amazon S3 — Static Frontend Hosting

## What It Is

A focused 201-level look at S3 as a static frontend host. The 101 note covers S3 fundamentals (buckets, objects, storage classes). This note covers using S3 to serve a React/Vite build as a website, paired with CloudFront.

See also: [Amazon S3 (101)](../../101/aws_services/19_amazon_s3.md)

## How It Works

### S3 as a static host

A React/Vite build produces static files: `index.html`, JS bundles, CSS, assets. S3 stores them as objects. CloudFront serves them to browsers. S3 itself never handles HTTP traffic directly — CloudFront is the entry point.

```
cdk deploy
  → CDK builds frontend (or you build manually)
    → uploads dist/ to S3 bucket
      → CloudFront points at S3 as origin
        → browser hits CloudFront URL → gets index.html
```

### CDK setup

```python
from aws_cdk import (
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    RemovalPolicy
)

bucket = s3.Bucket(self, "FrontendBucket",
    removal_policy=RemovalPolicy.DESTROY,
    auto_delete_objects=True,
    block_public_access=s3.BlockPublicAccess.BLOCK_ALL  # CloudFront accesses it, not public
)

# Deploy built frontend files to S3
s3deploy.BucketDeployment(self, "DeployFrontend",
    sources=[s3deploy.Source.asset("./frontend/dist")],
    destination_bucket=bucket
)
```

| Parameter | Value | Why |
|-----------|-------|-----|
| `block_public_access` | `BLOCK_ALL` | S3 is not public — CloudFront accesses it via OAC |
| `removal_policy` | `DESTROY` | `cdk destroy` deletes the bucket |
| `auto_delete_objects` | `True` | Empties bucket before deleting; destroy fails if bucket has files |
| `Source.asset("./frontend/dist")` | Built output folder | Upload the Vite/React build output |

### Access pattern

S3 bucket is private. CloudFront gets access via **Origin Access Control (OAC)** — an IAM-style grant that lets only your CloudFront distribution read from the bucket.

```python
from aws_cdk import aws_cloudfront as cf
from aws_cdk import aws_cloudfront_origins as origins

oac = cf.S3OriginAccessControl(self, "OAC")

distribution = cf.Distribution(self, "FrontendDist",
    default_behavior=cf.BehaviorOptions(
        origin=origins.S3BucketOrigin.with_origin_access_control(bucket, origin_access_control=oac)
    ),
    default_root_object="index.html"
)

# Grant CloudFront read access to the bucket
bucket.grant_read(
    iam.ServicePrincipal("cloudfront.amazonaws.com",
        conditions={"StringEquals": {"AWS:SourceArn": distribution.distribution_arn}}
    )
)
```

## Example

Frontend build and deploy flow:

```bash
# Build React/Vite app
cd frontend && npm run build   # outputs to frontend/dist/

# CDK picks up dist/ via Source.asset("./frontend/dist")
cdk deploy                     # uploads dist/ to S3, wires CloudFront
```

After deploy, CloudFront URL serves `index.html`. Browser loads JS, makes API calls to API Gateway.

## Why It Matters

S3 + CloudFront is the standard pattern for serving a static frontend at scale — no running server, no compute cost at idle, global CDN delivery. The bucket stays private; CloudFront is the only allowed reader.

> **Tip:** Always set `default_root_object="index.html"` on the CloudFront distribution. Without it, hitting the root URL returns an S3 access error, not your app.

---
← Previous: [DynamoDB TTL and Session Store](15_amazon_dynamodb_ttl.md) | [Overview](00_overview.md) | Next: [Amazon CloudFront](17_amazon_cloudfront.md) →
