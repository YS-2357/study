# Caching

## What It Is
Caching is storing a copy of data in a faster or closer location so future requests are served quicker.

The core trade-off: **use more memory/space to save time**.

## Why Caching Exists
- Reading from disk is slow (~ms), reading from RAM is fast (~ns)
- Network requests are slow (10-100ms), local copies are instant
- Repeated computation is wasteful if the result doesn't change

Without caching, every request goes to the original source every time. With caching, the first request is slow (cache miss), but subsequent requests are fast (cache hit).

## Key Concepts

### Cache Hit vs Cache Miss
- **Cache hit** — requested data is found in cache → fast response
- **Cache miss** — data not in cache → fetch from origin, store in cache for next time

**Hit ratio** = hits / (hits + misses). Higher is better. A 90% hit ratio means 9 out of 10 requests are served from cache.

### TTL (Time to Live)
- How long cached data stays valid before it expires
- Short TTL = fresher data, more cache misses
- Long TTL = faster responses, risk of stale data
- Example: DNS TTL of 300 seconds means "cache this IP for 5 minutes"

### Eviction Policies
When cache is full, something must be removed. Common strategies:
- **LRU (Least Recently Used)** — remove what hasn't been accessed longest
- **LFU (Least Frequently Used)** — remove what's accessed least often
- **FIFO (First In First Out)** — remove oldest entry
- **TTL-based** — remove expired entries

### Cache Invalidation
The hardest problem in caching — knowing when cached data is outdated.
- **Time-based** — expire after TTL
- **Event-based** — invalidate when source data changes
- **Manual** — explicitly clear cache

> "There are only two hard things in Computer Science: cache invalidation and naming things." — Phil Karlton

## Layers of Caching

Caching happens at every level of a system:

| Layer | What's Cached | Example |
|-------|--------------|---------|
| **CPU** | Instructions and data | L1/L2/L3 cache (nanoseconds) |
| **Application** | Computed results, session data | In-memory variables, local maps |
| **Database** | Query results, buffer pool | MySQL buffer pool, PostgreSQL shared buffers |
| **In-memory store** | Frequently queried data | Redis, Memcached |
| **DNS** | Domain → IP mappings | Browser cache, resolver cache |
| **CDN** | Static files, API responses | CloudFront edge locations |
| **Browser** | Pages, images, scripts | Browser cache (HTTP Cache-Control headers) |

### CPU Cache
- Built into the processor, extremely fast (1-10ns)
- L1 (smallest, fastest) → L2 → L3 (largest, slowest)
- You don't control this directly — the CPU manages it
- See [Architecture](01_architecture.md) for more detail

### In-Memory Caching (Most Relevant for AWS)
- Store data in RAM instead of querying a database every time
- **Redis** — supports data structures (strings, lists, sets, sorted sets), persistence, replication
- **Memcached** — simpler, pure key-value, multi-threaded, no persistence
- Typical use: put a cache between your application and your database

**Without cache:**
```
App → Database (every request, 5-50ms each)
```

**With cache:**
```
App → Cache (hit: <1ms) or Cache miss → Database → Store in cache
```

### CDN Caching
- Cache content at edge locations geographically close to users
- Reduces latency for static content (images, CSS, JS, videos)
- Example: CloudFront caches S3 objects at 400+ edge locations worldwide

### DNS Caching
- See [DNS](../../networking/networking_kiro/04_dns.md) for full explanation
- Browser, OS, and DNS resolvers all cache DNS lookups
- TTL controls how long each level caches the result

## Common Caching Patterns

### Cache-Aside (Lazy Loading)
Most common pattern:
1. App checks cache
2. If hit → return cached data
3. If miss → query database → write result to cache → return

**Pros:** Only caches what's actually requested
**Cons:** First request is always slow (cache miss)

### Write-Through
1. App writes to cache AND database at the same time
2. Reads always come from cache

**Pros:** Cache is always up to date
**Cons:** Write latency increases, cache may hold data that's never read

### Write-Behind (Write-Back)
1. App writes to cache only
2. Cache asynchronously writes to database later

**Pros:** Very fast writes
**Cons:** Risk of data loss if cache fails before writing to database

## When NOT to Cache
- Data changes constantly and must always be fresh (e.g., stock prices)
- Data is accessed only once (caching wastes memory)
- Data is too large to fit in cache cost-effectively
- Security-sensitive data that shouldn't be stored in additional locations

## AWS Services Related to Caching
- **ElastiCache** — Managed Redis/Memcached (see [ElastiCache](../../aws101/aws_services_kiro/13_amazon_elasticache.md))
- **CloudFront** — CDN caching at edge locations
- **DAX** — DynamoDB Accelerator, in-memory cache specifically for DynamoDB
- **API Gateway** — Can cache API responses
