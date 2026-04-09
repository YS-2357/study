# Amazon CloudFront — CDN for Static Frontend

## What It Is

Amazon CloudFront is a CDN (Content Delivery Network) that caches and serves your content from edge locations close to the user. In the frontend stack, it sits in front of S3 and is the only public entry point to your static files.

See also: [Amazon CloudFront (101)](../../101/aws_services/21_amazon_cloudfront.md)

## How It Works

### Role in the stack

```
Browser → CloudFront (edge location, nearest to user)
               ↓ cache miss
            S3 bucket (origin, single region)
               ↓
            returns file → CloudFront caches it → serves browser
```

On a cache hit, CloudFront serves from the edge without touching S3. On a miss, it fetches from S3 and caches for subsequent requests.

### Key concepts

| Term | Meaning |
|------|---------|
| Distribution | One CloudFront configuration (one URL) |
| Origin | Where CloudFront fetches content from (S3, API Gateway, ALB) |
| Behavior | Rules per path: which origin, cache policy, allowed methods |
| Edge location | AWS PoP that caches and serves content |
| OAC (Origin Access Control) | IAM-style grant allowing only this distribution to read from S3 |

### CDK setup

```python
from aws_cdk import aws_cloudfront as cf
from aws_cdk import aws_cloudfront_origins as origins

oac = cf.S3OriginAccessControl(self, "OAC")

distribution = cf.Distribution(self, "FrontendDist",
    default_behavior=cf.BehaviorOptions(
        origin=origins.S3BucketOrigin.with_origin_access_control(
            bucket,
            origin_access_control=oac
        ),
        viewer_protocol_policy=cf.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
        cache_policy=cf.CachePolicy.CACHING_OPTIMIZED
    ),
    default_root_object="index.html",
    error_responses=[
        cf.ErrorResponse(
            http_status=403,
            response_http_status=200,
            response_page_path="/index.html"  # SPA fallback
        )
    ]
)
```

| Parameter | Value | Why |
|-----------|-------|-----|
| `default_root_object` | `"index.html"` | Serves the app on root URL hit |
| `REDIRECT_TO_HTTPS` | viewer protocol policy | Forces HTTPS for all requests |
| `CACHING_OPTIMIZED` | cache policy | Caches static assets aggressively |
| `error_responses` 403 → 200 | SPA fallback | React Router routes (e.g. `/chat`) return 403 from S3; CloudFront rewrites to `index.html` so the SPA handles routing |

### SPA fallback — why it matters

A React app with client-side routing (e.g. `/chat`, `/history`) means those paths don't exist as S3 objects. When a user refreshes on `/chat`, S3 returns 403 (no such key). Without the error response rule, the user sees an error. With it, CloudFront returns `index.html` and React Router handles the path.

### Getting the distribution URL

```python
from aws_cdk import CfnOutput

CfnOutput(self, "FrontendUrl",
    value=f"https://{distribution.distribution_domain_name}"
)
```

Printed after `cdk deploy`. This is the URL the frontend is served from.

## Why It Matters

CloudFront makes the frontend globally fast and keeps S3 private. Without it, you'd either expose S3 as a public website (security risk) or serve files from a single region (latency for distant users). OAC replaces the older OAI pattern and is the current best practice for S3-backed distributions.

> **Tip:** After `cdk deploy`, CloudFront changes take up to 5 minutes to propagate. If the old version still shows, wait — don't redeploy.

---
← Previous: [Amazon S3](16_amazon_s3.md) | [Overview](00_overview.md) | Next: [Amazon ECR](18_amazon_ecr.md) →
