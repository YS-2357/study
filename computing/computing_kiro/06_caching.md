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
- **ElastiCache** — Managed Redis/Memcached/Valkey (see [ElastiCache](../../aws/101/aws_services_kiro/13_amazon_elasticache.md))
- **CloudFront** — CDN caching at edge locations
- **DAX** — DynamoDB Accelerator, in-memory cache specifically for DynamoDB
- **API Gateway** — Can cache API responses

---

## Valkey vs Redis vs Memcached

These are all in-memory data stores used for caching. They run in RAM, so they're extremely fast (sub-millisecond).

### What Each One Is

**Memcached** (2003~)
- The original in-memory caching system
- Pure key-value store — you store a string key and a string/binary value, that's it
- Multi-threaded — can use multiple CPU cores natively
- No persistence — if it restarts, all data is gone
- No replication — single node only (you can shard across multiple nodes, but each node is independent)
- Simplest to understand and operate

**Redis** (2009~)
- Started as "Memcached but with more features"
- Supports rich data structures: strings, lists, sets, sorted sets, hashes, streams, bitmaps
- Persistence — can save data to disk (RDB snapshots, AOF log)
- Replication — primary/replica for high availability
- Pub/Sub — can act as a message broker
- Lua scripting, transactions, TTL per key
- Single-threaded for commands (uses one CPU core for processing, I/O threads added in v6)
- Was open source (BSD license) until 2024

**Valkey** (2024~)
- A fork of Redis, created when Redis changed its license from open source (BSD) to a more restrictive dual license (RSALv2 + SSPLv1) in March 2024
- Linux Foundation project — backed by AWS, Google, Oracle, Ericsson, Snap
- Functionally identical to Redis 7.2 at fork time — same commands, same data structures, same protocol
- Goal: remain truly open source (BSD license) and community-driven
- AWS ElastiCache now offers Valkey as an engine option alongside Redis and Memcached

### Why Valkey Exists (the License Drama)

```
2009-2024: Redis = open source (BSD license), anyone can use/modify/sell
March 2024: Redis Labs changes license to RSALv2 + SSPLv1
             → Cloud providers (AWS, GCP, etc.) can no longer offer Redis as a managed service freely
             → Community forks Redis 7.2.4 → creates "Valkey" under Linux Foundation
             → Valkey stays BSD licensed (truly open source)
```

AWS switched ElastiCache's default from "Redis" to "Valkey" because of this.

### Comparison Table

| Feature | Memcached | Redis | Valkey |
|---------|-----------|-------|--------|
| **Type** | Key-value only | Key-value + data structures | Key-value + data structures |
| **Data structures** | Strings only | Strings, Lists, Sets, Sorted Sets, Hashes, Streams, etc. | Same as Redis |
| **Persistence** | ✗ (memory only) | ✔ (RDB, AOF) | ✔ (RDB, AOF) |
| **Replication** | ✗ | ✔ (primary-replica) | ✔ (primary-replica) |
| **Clustering** | Client-side sharding | Redis Cluster (server-side) | Same as Redis |
| **Threading** | Multi-threaded | Mostly single-threaded | Multi-threaded I/O (improving) |
| **Pub/Sub** | ✗ | ✔ | ✔ |
| **Lua scripting** | ✗ | ✔ | ✔ |
| **License** | BSD | RSALv2 + SSPLv1 (2024~) | BSD (open source) |
| **AWS 서비스** | ElastiCache | ElastiCache | ElastiCache |

### When to Use What

- **Memcached** — 단순 캐싱만 필요할 때. 세션 스토어, HTML fragment 캐싱 등. 데이터 구조 불필요, 멀티스레드 성능이 중요할 때.
- **Redis/Valkey** — 데이터 구조가 필요할 때 (sorted set으로 리더보드, list로 큐, pub/sub으로 실시간 알림 등). 영속성이나 복제가 필요할 때.
- **Valkey vs Redis** — 기능적으로 거의 동일. AWS에서는 Valkey가 기본 권장. 라이선스 차이가 핵심 (Valkey = open source, Redis = 제한적 라이선스).

### AWS ElastiCache Engine 선택

ElastiCache 생성 시 엔진을 선택:
- **Valkey** — AWS 기본 권장 (2024~), Redis 호환, 오픈소스
- **Redis** — 기존 Redis 워크로드 호환
- **Memcached** — 단순 캐싱, 멀티스레드

> 대부분의 신규 프로젝트에서는 Valkey를 선택하면 된다. Redis에서 Valkey로의 마이그레이션은 프로토콜이 동일하므로 거의 무중단으로 가능.
