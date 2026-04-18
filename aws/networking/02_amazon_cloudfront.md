---
tags:
  - aws
  - networking
created_at: 2026-03-31T00:00:00
updated_at: 2026-04-18T12:30:09
recent_editor: CLAUDE
---

↑ [Overview](./00_networking_overview.md)

# Amazon CloudFront

## What It Is
**CloudFront** is AWS's CDN (Content Delivery Network). It caches your content at 600+ edge locations worldwide so users get responses from the nearest location instead of your origin server far away.

CloudFront is a **global** service (not regional).

## How It Works

You create a CloudFront distribution specifying an origin (S3, ALB, etc.) and cache behaviors. When a user makes a request, it is routed to the nearest edge location. If the edge has a cached copy that has not expired (within TTL), it is returned immediately. On a cache miss, the edge fetches the content from the origin, caches it, and returns it. Subsequent requests from the same region are served from cache without hitting the origin.

## Console Access
- AWS Console → CloudFront → Distributions
- Breadcrumb: CloudFront > Distributions


## How CloudFront Works

```
User in Seoul → CloudFront Edge (Seoul) → Origin (S3, ALB, EC2, etc.)
                 ↑ cached here              ↑ source of truth
                 fast (nearby)              only hit on cache miss
```

1. User requests content (e.g., image, HTML, API response)
2. Request goes to nearest CloudFront edge location
3. **Cache hit**: edge has it → return immediately (fast)
4. **Cache miss**: edge fetches from origin → caches it → returns to user
5. Next request from same region → served from cache


## Common Pattern: S3 Static Website + CloudFront

The standard way to host static websites (React, Vue, Next.js static export, plain HTML) on AWS:

```
Upload to S3 → CloudFront distribution → Users worldwide
(origin)        (CDN + HTTPS + caching)    (fast access)
```

### Why not just use S3 directly?

| | S3 alone | S3 + CloudFront |
|---|---------|----------------|
| **Speed** | Single region, far users = slow | 600+ edge locations = fast |
| **HTTPS** | S3 website endpoint = HTTP only | Free HTTPS with ACM certificate |
| **Custom domain** | Complicated | Easy (Route 53 + ACM) |
| **Caching** | None | Edge caching, reduces S3 requests + cost |
| **Security** | Must make bucket public | OAC — bucket stays private, only CloudFront can access |

### OAC (Origin Access Control)

```
Without OAC:  S3 bucket must be public     ← bad, anyone can access S3 directly
With OAC:     S3 bucket stays private      ← good
              Only CloudFront can read it
              Users can't bypass CloudFront to hit S3 directly
```

OAC is the recommended way to connect CloudFront to S3. It replaces the older OAI (Origin Access Identity).


## Origin Types

CloudFront can serve content from multiple origin types:

| Origin | Use case |
|--------|----------|
| **S3 bucket** | Static files, images, videos, website hosting |
| **ALB** | Dynamic web apps, APIs |
| **EC2** | Custom web server (must be public or via ALB) |
| **API Gateway** | REST/HTTP APIs |
| **MediaStore / MediaPackage** | Video streaming |
| **Custom origin (any HTTP server)** | On-premises server, external URL |


## Key Concepts

### Distribution
- The main CloudFront resource — a configuration that tells CloudFront where to get content and how to serve it
- Each distribution gets a domain: `d1234abcd.cloudfront.net`
- Can map to custom domain via Route 53 + ACM certificate

### TTL (Time To Live)
- How long CloudFront caches content at the edge before checking the origin again
- Default: 24 hours
- Short TTL (e.g., 60s) = fresher content, more origin requests
- Long TTL (e.g., 7 days) = faster, cheaper, but stale content risk
- Can invalidate cache manually (costs per invalidation path)

### Cache Behaviors
- Rules that define how CloudFront handles different URL patterns
- Example: `/api/*` → forward to ALB (no cache), `/images/*` → cache from S3 (long TTL)

### Edge Locations vs Regional Edge Caches
- **Edge locations** (600+) — closest to users, first cache layer
- **Regional edge caches** (13) — between edge and origin, second cache layer for less popular content


## CloudFront vs ElastiCache

| | CloudFront | ElastiCache |
|---|-----------|-------------|
| **What** | CDN — caches HTTP responses at edge | In-memory cache inside your VPC |
| **Where** | Between user and your server | Between your app and your DB |
| **Caches** | Static files, API responses, web pages | DB query results, sessions, computed data |
| **For** | End users (reduce latency) | Application (reduce DB load) |


## Pricing

**Source:** [CloudFront Pricing](https://aws.amazon.com/cloudfront/pricing/)

- **Data transfer out to internet**: $0.085/GB (first 10 TB/month, US/Europe)
- **HTTP requests**: $0.0075/10K requests
- **HTTPS requests**: $0.01/10K requests
- **Free tier**: 1 TB data transfer out + 10M requests/month (always free, not 12-month)

Additional costs:
- Cache invalidation: first 1,000 paths/month free, then $0.005/path
- Real-time logs: per log line
- CloudFront Functions / Lambda@Edge: per request + compute


## Precautions

### MAIN PRECAUTION: Cache Invalidation Takes Time and Costs Money
- If you update content at origin, CloudFront still serves old cached version until TTL expires
- Manual invalidation: `/*` invalidates everything but costs per path
- Better approach: use versioned file names (e.g., `app.v2.js`) so new URL = new cache

### 1. Use OAC for S3 Origins
- Never make S3 bucket public just for CloudFront
- OAC keeps bucket private, only CloudFront can access

### 2. Always Use HTTPS
- Free ACM certificate for custom domains
- Redirect HTTP → HTTPS in CloudFront settings

### 3. Don't Cache Everything
- Static assets (images, CSS, JS) → cache aggressively
- API responses → cache carefully or not at all (depends on data freshness needs)
- Authenticated content → usually don't cache

### 4. CloudFront is Global, WAF Scope Matters
- To attach WAF to CloudFront, the Web ACL must be created in **us-east-1** (Global scope)
- Regional Web ACLs (for ALB) won't work with CloudFront

## Example

A static website hosted in an S3 bucket uses a CloudFront distribution with an OAC so the bucket stays private.
Users worldwide hit the nearest edge location; cached content is served in single-digit milliseconds.
An ACM certificate on the distribution enables HTTPS with a custom domain.

## Why It Matters

CloudFront reduces latency for global users by caching content at 600+ edge locations.
It also offloads traffic from your origin, lowers data transfer costs, and adds a layer of DDoS protection via Shield Standard.

## Q&A

### Q: Can CloudFront cache dynamic content?

Yes. CloudFront handles both static and dynamic content.

- **Cacheable dynamic content**: Configure cache keys using query strings, cookies, and headers to cache dynamic responses
- **Non-cacheable dynamic content (API responses, etc.)**: Even without caching, CloudFront provides **network acceleration** through the AWS backbone network, reducing latency to the origin
- **TTL 0**: No caching, but connection optimization and security benefits ([Shield](17_aws_shield.md)/[WAF](18_aws_waf.md)) are retained

### Q: How does CloudFront reflect origin content changes?

By default, CloudFront fetches fresh content from the origin when the TTL expires.

**Methods to force refresh before TTL expiry:**

1. **Invalidation**: Force-delete cache for specific paths or wildcards (`/*`). First 1,000/month free, then $0.005 each. Propagation across edge locations takes several minutes — it is **not instant**.
2. **Versioning**: Include version in filename (e.g., `style.v2.css`). New URL = immediate effect. No invalidation cost.
3. **Cache-Control headers**: Control TTL from the origin using `max-age`, `s-maxage`.

CLI example for invalidation:
```
aws cloudfront create-invalidation --distribution-id EDFDVBD6EXAMPLE --paths "/*"
```

> **Tip:** Versioning is preferred for predictable deployments. Use invalidation for emergency content updates.

## CDK Setup for Static Frontend

### Full CDK distribution with SPA support

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

> **Tip:** After `cdk deploy`, CloudFront changes take up to 5 minutes to propagate. If the old version still shows, wait — don't redeploy.

## Official Documentation
- [Amazon CloudFront Documentation](https://docs.aws.amazon.com/cloudfront/)
- [CloudFront Pricing](https://aws.amazon.com/cloudfront/pricing/)

---
← Previous: [Elastic Load Balancing (ELB)](./01_elastic_load_balancing.md) | [Overview](./00_networking_overview.md) | Next: [Amazon API Gateway](./03_amazon_api_gateway.md) →
