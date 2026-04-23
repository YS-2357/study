---
tags:
  - software
  - backend
created_at: 2026-04-23T15:20:41
updated_at: 2026-04-23T23:41:19
recent_editor: CODEX
---

↑ [Overview](./00_backend_overview.md)

# REST API

## What It Is

A design style for HTTP APIs where resources (users, orders, posts) are represented as URLs, and standard HTTP methods (GET, POST, PUT, DELETE) express what to do with them. REST stands for Representational State Transfer.

## Analogy

A waiter at a restaurant. The menu is the API (what's available). You use standard verbs — "give me" (GET), "add this" (POST), "replace this" (PUT), "remove this" (DELETE). The waiter (server) handles your request and brings back a response.

## How It Works

**URL = resource, HTTP method = action:**

| Method | URL | Meaning |
|--------|-----|---------|
| `GET` | `/users` | List all users |
| `GET` | `/users/42` | Get user 42 |
| `POST` | `/users` | Create a new user |
| `PUT` | `/users/42` | Replace user 42 |
| `PATCH` | `/users/42` | Partially update user 42 |
| `DELETE` | `/users/42` | Delete user 42 |

**HTTP status codes:**

| Code | Meaning |
|------|---------|
| `200` | OK |
| `201` | Created |
| `400` | Bad Request (client error) |
| `401` | Unauthorized |
| `404` | Not Found |
| `500` | Internal Server Error |

**REST is stateless** — each request carries all the information needed. The server stores no session between requests.

## Example

```
GET /users/42
Authorization: Bearer <token>

Response 200:
{ "id": 42, "name": "Alice", "email": "alice@example.com" }
```

```
POST /users
Body: { "name": "Bob", "email": "bob@example.com" }

Response 201:
{ "id": 43, "name": "Bob", "email": "bob@example.com" }
```

## Why It Matters

REST is the default API style for web services. Understanding it lets you consume any third-party API and design backend services that frontend and mobile clients can use predictably.

---
↑ [Overview](./00_backend_overview.md)

**Related:** [Authentication](./02_authentication.md), [Middleware](./03_middleware.md), [Rate Limiting](./06_rate_limiting.md)
**Tags:** #software #backend
