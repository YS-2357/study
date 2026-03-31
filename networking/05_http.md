# HTTP — Status Codes, Methods & REST API

## What It Is
HTTP (HyperText Transfer Protocol) is the protocol for communication between clients and servers on the web. Browsers, APIs, load balancers, CDNs — almost all web communication runs on HTTP.

Basic structure:
```
Client (browser, app) → HTTP Request → Server
Client ← HTTP Response ← Server
```

For protocol basics, see the HTTP/HTTPS section in [Protocols](01_protocols.md).
For the higher-level idea of an API as an interface, see [Interfaces](../computing/07_interfaces.md). This note is where the HTTP and REST API details live.

---

## HTTP Methods

The verb that tells the server what the client wants to do.

| Method | Meaning | Use Case | Example |
|--------|---------|----------|---------|
| **GET** | Read | Retrieve data | `GET /users/1` → get user 1 info |
| **POST** | Create | Create new data | `POST /users` → create new user |
| **PUT** | Full update | Replace entire resource | `PUT /users/1` → replace all of user 1 |
| **PATCH** | Partial update | Modify part of a resource | `PATCH /users/1` → change user 1's name only |
| **DELETE** | Delete | Remove data | `DELETE /users/1` → delete user 1 |
| **HEAD** | Headers only | Same as GET but no body | Check if a file exists |
| **OPTIONS** | Check allowed methods | List supported methods | CORS preflight request |

### Safe vs Unsafe
- **Safe** (no server state change): GET, HEAD, OPTIONS
- **Unsafe** (changes server state): POST, PUT, PATCH, DELETE

### Idempotent
Does sending the same request multiple times produce the same result?
- **Idempotent**: GET, PUT, DELETE, HEAD, OPTIONS
- **Not idempotent**: POST (creates a new resource each time), PATCH (depends on implementation)

---

## HTTP Status Codes

A 3-digit number the server returns to tell the client what happened.

### 1xx — Informational
Request received, still processing.

| Code | Name | Description |
|------|------|-------------|
| 100 | Continue | Headers received, send the body |
| 101 | Switching Protocols | Protocol change (e.g., HTTP → WebSocket) |

Rarely seen in practice.

### 2xx — Success
Request was processed successfully.

| Code | Name | Description | When |
|------|------|-------------|------|
| **200** | OK | Success | GET read, PUT/PATCH update |
| **201** | Created | Resource created | POST created new data |
| **202** | Accepted | Request accepted (not yet processed) | Async job started |
| **204** | No Content | Success but no response body | DELETE success |

### 3xx — Redirection
Go somewhere else.

| Code | Name | Description | When |
|------|------|-------------|------|
| **301** | Moved Permanently | Permanent move | URL permanently changed (affects SEO) |
| **302** | Found | Temporary move | Temporarily redirect to another URL |
| **304** | Not Modified | No change | Use cached version |
| **307** | Temporary Redirect | Temporary redirect | Like 302 but preserves HTTP method |
| **308** | Permanent Redirect | Permanent redirect | Like 301 but preserves HTTP method |

### 4xx — Client Error
The request is wrong — client's fault.

| Code | Name | Description | When |
|------|------|-------------|------|
| **400** | Bad Request | Malformed request | Invalid JSON, missing required parameter |
| **401** | Unauthorized | Not authenticated | Not logged in, token expired |
| **403** | Forbidden | No permission | Authenticated but not authorized |
| **404** | Not Found | Resource doesn't exist | Wrong URL or deleted resource |
| **405** | Method Not Allowed | Method not supported | DELETE on a GET-only endpoint |
| **408** | Request Timeout | Client too slow | Client took too long to send request |
| **409** | Conflict | Resource conflict | Trying to create something that already exists |
| **413** | Payload Too Large | Body too big | File upload exceeds size limit |
| **429** | Too Many Requests | Rate limited | API throttling, too many calls |

**401 vs 403:**
- 401 = "Who are you?" (authentication failure)
- 403 = "I know who you are, but you can't do this" (authorization failure)

### 5xx — Server Error
Server's fault — not the client's problem.

| Code | Name | Description | Cause |
|------|------|-------------|-------|
| **500** | Internal Server Error | Server crashed | App crash, unhandled exception, bug |
| **502** | Bad Gateway | Gateway error | LB can't reach backend, backend returned invalid response |
| **503** | Service Unavailable | Service down | Server overloaded, all instances down, ASG still scaling |
| **504** | Gateway Timeout | Backend too slow | Slow DB query, Lambda timeout |

**Common 5xx scenarios in AWS:**
- ALB → 502: No healthy instances in target group
- ALB → 503: All targets unhealthy
- ALB → 504: Backend response exceeds idle timeout (60s)
- API Gateway → 502: Lambda function error
- API Gateway → 504: Lambda exceeds 29s integration timeout
- CloudFront → 502: Can't connect to origin server

---

## REST API

### What It Is
REST (Representational State Transfer) is an architectural style for designing APIs on top of HTTP. It's not a protocol or standard — it's a set of design conventions.

A useful metaphor:
- **HTTP is the language and grammar**
- **REST is the writing style**

That means `GET`, `POST`, status codes, and headers come from HTTP itself. REST is the design approach that says how to use those HTTP pieces in a consistent, resource-oriented way.

### Core Principles
1. **Resource-oriented** — URLs represent resources (nouns): `/users`, `/orders/123`
2. **HTTP methods as actions** — GET (read), POST (create), PUT (update), DELETE (remove)
3. **Stateless** — Each request is independent, server doesn't store client state between requests
4. **Standard HTTP status codes** — Use the codes above to communicate results

### REST API Example

User management API:
```
GET    /users          → List all users          → 200 OK
GET    /users/1        → Get user 1              → 200 OK (or 404 Not Found)
POST   /users          → Create new user         → 201 Created
PUT    /users/1        → Replace user 1          → 200 OK
PATCH  /users/1        → Update user 1 partially → 200 OK
DELETE /users/1        → Delete user 1           → 204 No Content
```

### REST vs Other API Styles

| | REST | GraphQL | gRPC |
|---|------|---------|------|
| **Protocol** | HTTP | HTTP | HTTP/2 |
| **Data format** | JSON (mostly) | JSON | Protocol Buffers (binary) |
| **Endpoints** | Multiple (per resource) | Single endpoint | Methods per service |
| **Strengths** | Simple, standard, easy caching | Request only what you need | High performance, type-safe |
| **Weaknesses** | Over/under-fetching | Complex queries, hard to cache | Hard to call from browsers |
| **Use case** | Most web APIs | Frontend flexibility | Microservice-to-microservice |

### Same Goal, Different Style

Suppose the client wants to get user `1`.

**REST**
```text
GET /users/1
```
- The URL represents the resource
- The HTTP method tells the server what action the client wants

**GraphQL**
```graphql
query {
  user(id: 1) {
    id
    name
    email
  }
}
```
- The client asks for exactly the fields it wants
- This is usually sent to a single endpoint such as `/graphql`

**gRPC**
```text
UserService.GetUser(id=1)
```
- The client calls a remote method on a service
- This feels more like calling a function than accessing a URL resource

### AWS Services Related to REST APIs
- **API Gateway** — Create, manage, and deploy REST APIs (commonly paired with Lambda)
- **ALB** — HTTP routing (path-based, host header-based)
- **CloudFront** — Cache API responses at edge
- **Lambda** — Serverless API backend logic
