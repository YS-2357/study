# Amazon CloudFront - AWS Console Guide

## Official Documentation
- [Amazon CloudFront Documentation](https://docs.aws.amazon.com/cloudfront/)
- [CloudFront Pricing](https://aws.amazon.com/cloudfront/pricing/)

## What It Is
**CloudFront** is AWS's CDN (Content Delivery Network). It caches your content at 600+ edge locations worldwide so users get responses from the nearest location instead of your origin server far away.

CloudFront is a **global** service (not regional).

## Console Access
- AWS Console → CloudFront → Distributions
- Breadcrumb: CloudFront > Distributions

---

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

---

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
| **HTTPS** | S3 website endpoint = HTTP only | ✅ Free HTTPS with ACM certificate |
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

---

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

---

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

---

## CloudFront vs ElastiCache

| | CloudFront | ElastiCache |
|---|-----------|-------------|
| **What** | CDN — caches HTTP responses at edge | In-memory cache inside your VPC |
| **Where** | Between user and your server | Between your app and your DB |
| **Caches** | Static files, API responses, web pages | DB query results, sessions, computed data |
| **For** | End users (reduce latency) | Application (reduce DB load) |

---

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

---

## Precautions

### ⚠️ MAIN PRECAUTION: Cache Invalidation Takes Time and Costs Money
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
