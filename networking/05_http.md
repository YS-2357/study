---
tags:
  - networking
created_at: 2026-03-24T00:00:00
updated_at: 2026-04-17T14:18:47
recent_editor: CLAUDE
---

↑ [Overview](./00_overview.md)

# HTTP — Methods, Status Codes & REST API

## What It Is

HTTP (HyperText Transfer Protocol) is the protocol for communication between clients and servers on the web. Browsers, APIs, load balancers, CDNs — almost all web communication runs on HTTP.

```
Client (browser, app) → HTTP Request → Server
Client ← HTTP Response ← Server
```

For protocol basics (HTTP vs HTTPS, TLS), see [Protocols](01_protocols.md). For the concept of an API as an interface, see [Interfaces](../computing/07_interfaces.md).

## How It Works

### HTTP Methods

| Method | Meaning | Example | Idempotent |
|--------|---------|---------|------------|
| **GET** | Read | `GET /users/1` | Yes |
| **POST** | Create | `POST /users` | No |
| **PUT** | Full replace | `PUT /users/1` | Yes |
| **PATCH** | Partial update | `PATCH /users/1` | Depends |
| **DELETE** | Remove | `DELETE /users/1` | Yes |

- **Safe** (no state change): GET, HEAD, OPTIONS
- **Idempotent** (same result if repeated): GET, PUT, DELETE

### HTTP Status Codes

| Range | Meaning | Key Codes |
|-------|---------|-----------|
| 2xx | Success | 200 OK, 201 Created, 204 No Content |
| 3xx | Redirect | 301 Permanent, 302 Temporary, 304 Not Modified |
| 4xx | Client error | 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests |
| 5xx | Server error | 500 Internal, 502 Bad Gateway, 503 Unavailable, 504 Timeout |

**401 vs 403:** 401 = "Who are you?" (not authenticated). 403 = "I know who you are, but you can't do this" (not authorized).

**Common AWS 5xx scenarios:**
- ALB → 502: No healthy targets. 503: All targets unhealthy. 504: Backend exceeds idle timeout.
- API Gateway → 502: Lambda error. 504: Lambda exceeds 29s timeout.
- CloudFront → 502: Can't connect to origin.

### REST API

REST (Representational State Transfer) is a design style for APIs on top of HTTP. HTTP provides the language (methods, status codes); REST is the writing style (resource-oriented URLs, stateless requests).

```
GET    /users          → 200 OK           (list)
GET    /users/1        → 200 OK or 404    (read)
POST   /users          → 201 Created      (create)
PUT    /users/1        → 200 OK           (replace)
DELETE /users/1        → 204 No Content   (remove)
```

**Core principles:** resource-oriented URLs (nouns, not verbs), HTTP methods as actions, stateless requests, standard status codes.

### REST vs GraphQL vs gRPC

| | REST | GraphQL | gRPC |
|---|------|---------|------|
| Data format | JSON | JSON | Protocol Buffers (binary) |
| Endpoints | Multiple (per resource) | Single | Methods per service |
| Strength | Simple, cacheable | Request only what you need | High performance |
| Use case | Most web APIs | Frontend flexibility | Microservice-to-microservice |

## Example

A browser loading `https://example.com/users/1`:
1. Sends `GET /users/1` with headers (Accept, Authorization, etc.)
2. Server processes the request
3. Returns `200 OK` with JSON body: `{"id": 1, "name": "Alice"}`

## Why It Matters

HTTP is the foundation of [ALB](../aws/16_elastic_load_balancing.md) routing (path-based, host-based), [API Gateway](../aws/07_aws_lambda.md) design, and [CloudFront](../aws/21_amazon_cloudfront.md) caching. Understanding status codes is essential for debugging production issues.

---
← Previous: [DNS](04_dns.md) | [Overview](./00_overview.md) | Next: [Reverse Proxy](06_reverse_proxy.md) →
