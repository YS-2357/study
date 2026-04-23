---
tags:
  - software
  - backend
created_at: 2026-04-23T15:20:41
updated_at: 2026-04-23T15:20:41
recent_editor: CLAUDE
---

↑ [Backend Overview](./00_backend_overview.md)

# Rate Limiting

## What It Is

A control that limits how many requests a client can make in a given time window. Requests over the limit are rejected (HTTP 429 Too Many Requests) or delayed. Protects the server from abuse, DoS attacks, and runaway clients.

## Analogy

A turnstile at a subway station. It lets one person through at a time and blocks the next until the previous has cleared. No matter how fast you push, the gate controls the flow.

## How It Works

**Token Bucket** (most common):
- Each client has a bucket with a max capacity of N tokens
- Tokens refill at a fixed rate (e.g., 10/second)
- Each request consumes one token
- If bucket is empty → reject request
- Allows short bursts (full bucket) while enforcing a long-term average

**Sliding Window:**
- Tracks exact timestamps of recent requests
- Rejects if count in the last N seconds exceeds the limit
- More accurate than fixed windows but uses more memory

**Fixed Window:**
- Counts requests per time slot (e.g., per minute)
- Simple but has edge cases at window boundaries (2× burst at rollover)

**Implementation keys:**
- State is usually stored in Redis (fast, shared across server instances)
- Identify clients by IP, API key, or user ID
- Return `Retry-After` header so clients know when to retry

## Example

```
Client A: 100 requests/minute allowed
00:01 — 50 requests → OK
00:01 — 51st request → 429 Too Many Requests, Retry-After: 30
```

Real example: OpenAI API limits by tokens-per-minute and requests-per-minute per API key.

## Why It Matters

Without rate limiting, a single misbehaving client can exhaust server resources and degrade service for everyone. It's a required primitive for any public-facing API.

---
↑ [Backend Overview](./00_backend_overview.md)

**Related:** [REST API](./01_rest_api.md), [Middleware](./03_middleware.md)
**Tags:** #software #backend
