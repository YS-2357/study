---
tags:
  - software
  - backend
created_at: 2026-04-23T15:20:41
updated_at: 2026-04-23T23:41:19
recent_editor: CODEX
---

↑ [Overview](./00_backend_overview.md)

# Middleware

## What It Is

Functions that sit in the request-response pipeline and run before (or after) your route handler. Each middleware receives the request, can modify it, and either passes it to the next function or terminates the chain.

## Analogy

Airport security lanes. Every passenger (request) passes through the same checkpoints — ID check (auth middleware), baggage scan (validation middleware), metal detector (logging middleware) — before reaching the gate (route handler). Any checkpoint can stop you.

## How It Works

```
Request → [logging] → [auth] → [validation] → route handler → Response
```

Each middleware has the same signature: `(request, response, next)`. Calling `next()` passes to the following middleware. Not calling it stops the chain.

```js
// Express.js example
app.use((req, res, next) => {
  console.log(`${req.method} ${req.path}`)  // logging
  next()  // pass to next middleware
})

app.use((req, res, next) => {
  const token = req.headers.authorization
  if (!token) return res.status(401).json({ error: 'Unauthorized' })
  req.user = verifyToken(token)  // attach user to request
  next()
})

app.get('/profile', (req, res) => {
  res.json(req.user)  // route handler — middleware already ran
})
```

**Common middleware types:**

| Type | What it does |
|------|-------------|
| Logging | Records every request (method, path, duration) |
| Auth | Verifies tokens, rejects unauthorized requests |
| Validation | Checks request body shape before hitting the handler |
| Rate limiting | Counts and limits requests per client |
| CORS | Adds headers allowing cross-origin browser requests |
| Error handling | Catches thrown errors, formats error responses |

## Example

Without auth middleware, every route handler must check auth itself. With middleware, auth runs once for all protected routes — the handler only sees valid, authenticated requests.

## Why It Matters

Middleware keeps cross-cutting concerns (auth, logging, rate limiting) out of business logic. It's the primary pattern for adding behavior to APIs without duplicating code.

---
↑ [Overview](./00_backend_overview.md)

**Related:** [REST API](./01_rest_api.md), [Authentication](./02_authentication.md), [Rate Limiting](./06_rate_limiting.md)
**Tags:** #software #backend
