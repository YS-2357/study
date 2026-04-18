---
tags:
  - aws
  - infrastructure
created_at: 2026-04-05T00:00:00
updated_at: 2026-04-18T11:46:13
recent_editor: CLAUDE
---

↑ [Overview](./00_aws_overview.md)

# Points of Presence (PoP)

## What It Is
A Point of Presence (PoP) is an edge location where AWS caches content and terminates connections closer to end users. PoPs are the physical infrastructure behind services like CloudFront, Route 53, and Global Accelerator.

**The problem it solves:**
- Your origin server is in `us-east-1`, but a user in Tokyo is 10,000+ km away
- Every request traveling that distance = high latency
- PoPs cache content and terminate connections at locations near users worldwide

**How it works:**
```
User in Tokyo → Nearest PoP (Tokyo edge) → Cache hit? → Serve immediately (fast)
                                          → Cache miss? → Fetch from origin → Cache → Serve
```

### PoP vs Region vs Availability Zone

| | Region | Availability Zone | Point of Presence |
|---|---|---|---|
| What it is | Geographic area with multiple data centers | One or more discrete data centers within a Region | Edge location for caching/acceleration |
| Purpose | Run full AWS services (EC2, RDS, etc.) | Fault isolation within a Region | Deliver content closer to users |
| Services | All AWS services | All AWS services | CloudFront, Route 53, Global Accelerator, WAF, Shield |
| Count | 30+ regions | 3–6 per region (typically) | 600+ globally |
| You manage | Choose which region to deploy in | Choose AZ placement for HA | Configured indirectly through CloudFront/Route 53 settings |

## How It Works

When a user makes a request, DNS resolution (via Route 53 or Anycast routing) directs the connection to the nearest PoP edge location. For CloudFront, the edge location checks its cache: a hit returns content immediately; a miss fetches from the origin, caches the response, then returns it. For Global Accelerator, the PoP receives TCP/UDP traffic and routes it over the AWS backbone network to the nearest healthy origin, bypassing the public internet for most of the journey.

## Console Access
- You don't create or manage PoPs directly
- They're used automatically when you configure:
  - **CloudFront** distributions (content caching)
  - **Route 53** (DNS resolution)
  - **Global Accelerator** (network acceleration)


## Key Concepts

### Edge Locations
- The actual PoP sites where content is cached and connections are terminated
- 600+ edge locations across 100+ cities worldwide
- Automatically selected based on user proximity

### Regional Edge Caches
- Larger cache layer between edge locations and your origin
- Holds content that's not popular enough for every edge location but still requested
- Reduces load on your origin server

```
User → Edge Location (PoP) → Regional Edge Cache → Origin (S3/EC2/etc.)
       (smallest cache)       (medium cache)        (source of truth)
```

### Which Services Use PoPs

| Service | How it uses PoPs |
|---|---|
| **CloudFront** | Caches static/dynamic content at edge locations |
| **Route 53** | Resolves DNS queries from the nearest edge location |
| **Global Accelerator** | Routes traffic through AWS backbone from nearest edge to your origin |
| **AWS WAF** | Runs at CloudFront edge locations to filter requests before they reach origin |
| **AWS Shield** | DDoS protection at the edge |


## Precautions

### MAIN PRECAUTION: PoPs Are Not Regions
- You cannot run EC2, RDS, Lambda, or other general compute at a PoP
- PoPs only serve edge functions: caching, DNS, acceleration, security filtering
- Your origin infrastructure still needs to be in a Region

### 1. Origin Design Still Matters
- PoPs improve delivery speed but don't fix a slow or unreliable origin
- Cache miss = full round trip to origin
- Design your origin for performance and availability

### 2. Caching Configuration
- PoP effectiveness depends entirely on your caching strategy
- Set appropriate TTLs — too short = frequent origin fetches, too long = stale content
- Use versioned file names for instant updates without invalidation

### 3. Cost Awareness
- No direct charge for PoPs themselves
- Cost comes from the services using them (CloudFront data transfer, Route 53 queries, etc.)
- CloudFront pricing varies by edge location geography — some regions cost more

### 4. Geographic Coverage
- Not all edge locations are equal — major cities have more capacity
- Check the [CloudFront edge location list](https://aws.amazon.com/cloudfront/features/#Amazon_CloudFront_Infrastructure) for coverage in your target markets

## Example

A user in São Paulo requests an image from a CloudFront distribution. The request hits the nearest PoP in São Paulo.
On a cache hit, the image is served in under 10 ms. On a cache miss, the PoP fetches it from the origin in `us-east-1`,
caches it locally, and serves future requests from São Paulo without crossing the ocean.

## Why It Matters

PoPs are the physical infrastructure that makes CloudFront, Route 53, and Global Accelerator fast.
Understanding PoPs explains why edge services reduce latency — content is served from locations physically close to users.

## Official Documentation
- [CloudFront Infrastructure](https://aws.amazon.com/cloudfront/features/#Amazon_CloudFront_Infrastructure)
- [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)

---
← Previous: [Subnet](03_subnet.md) | [Overview](./00_aws_overview.md) | Next: [Amazon VPC](04_amazon_vpc.md) →
