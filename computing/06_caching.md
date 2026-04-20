---
tags:
  - computing
created_at: 2026-03-23T00:00:00
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
---

↑ [Overview](./00_computing_overview.md)

# Caching

## What It Is

Caching is storing a copy of data in a faster or closer location so future requests are served quicker. The core trade-off: use more memory/space to save time.

## How It Works

### Key Concepts

- **Cache hit** — data found in cache → fast response
- **Cache miss** — data not in cache → fetch from origin, store for next time
- **Hit ratio** = hits / (hits + misses). Higher is better.
- **TTL (Time to Live)** — how long cached data stays valid. Short TTL = fresher data, more misses. Long TTL = faster, risk of stale data.

### Eviction Policies

When cache is full, something must be removed:
- **LRU (Least Recently Used)** — remove what hasn't been accessed longest
- **LFU (Least Frequently Used)** — remove what's accessed least often
- **TTL-based** — remove expired entries

### Cache Invalidation

Knowing when cached data is outdated — the hardest problem in caching.
- **Time-based** — expire after TTL
- **Event-based** — invalidate when source data changes
- **Manual** — explicitly clear cache

### Layers of Caching

| Layer | What's cached | Speed | Example |
|-------|--------------|-------|---------|
| CPU | Instructions, data | ~ns | L1/L2/L3 cache |
| Application | Computed results | ~μs | In-memory variables |
| In-memory store | Frequently queried data | ~ms | [ElastiCache](../cloud/aws/database/04_amazon_elasticache.md) (Redis, Memcached) |
| Database | Query results, buffer pool | ~ms | MySQL buffer pool |
| CDN | Static files, API responses | ~ms | [CloudFront](../cloud/aws/networking/02_amazon_cloudfront.md) edge locations |
| DNS | Domain → IP mappings | ~ms | Browser cache, resolver cache |
| Browser | Pages, images, scripts | ~ms | HTTP Cache-Control headers |

### Caching Patterns

**Cache-aside (Lazy Loading):**
1. App checks cache
2. Miss → app reads from DB, writes to cache
3. Next request → cache hit

**Write-through:**
1. App writes to cache and DB simultaneously
2. Cache always has latest data
3. Slower writes, but no stale reads

**Write-behind:**
1. App writes to cache only
2. Cache asynchronously writes to DB
3. Fastest writes, but risk of data loss

## Example

A web app queries a database for user profiles. Without caching, every page load hits the DB (~10ms). With [ElastiCache](../cloud/aws/database/04_amazon_elasticache.md) (Redis) in front, the first request is slow (cache miss), but subsequent requests return in ~1ms (cache hit). With a 90% hit ratio, 9 out of 10 requests skip the database entirely.

## Why It Matters

Caching appears at every level of AWS architecture: [CloudFront](../cloud/aws/networking/02_amazon_cloudfront.md) at the edge, [ElastiCache](../cloud/aws/database/04_amazon_elasticache.md) in front of databases, [DynamoDB DAX](../cloud/aws/database/03_amazon_dynamodb.md) for DynamoDB. Understanding cache patterns helps you choose the right strategy and avoid stale data bugs.

For LLM-specific caching, see [KV Cache](../ai/concepts/11_kv_cache.md) and [Prompt Caching](../ai/concepts/12_prompt_caching.md).

---
↑ [Overview](./00_computing_overview.md)

**Related:** [Workload Types](05_workload_types.md), [Interfaces](07_interfaces.md), [ElastiCache](../cloud/aws/database/04_amazon_elasticache.md), [CloudFront](../cloud/aws/networking/02_amazon_cloudfront.md), [DynamoDB DAX](../cloud/aws/database/03_amazon_dynamodb.md), [KV Cache](../ai/concepts/11_kv_cache.md), [Prompt Caching](../ai/concepts/12_prompt_caching.md)
**Tags:** #computing
