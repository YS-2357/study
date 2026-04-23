---
tags:
  - software
  - backend
created_at: 2026-04-23T15:20:41
updated_at: 2026-04-23T15:20:41
recent_editor: CLAUDE
---

↑ [Backend Overview](./00_backend_overview.md)

# Authentication

## What It Is

**Authentication** = proving who you are. **Authorization** = what you're allowed to do. The two are often confused but always distinct. Three main approaches: sessions, JWT, and OAuth 2.0.

## Analogy

A hotel. Authentication is showing your ID at check-in. The key card you get is the session/token — you don't re-show your ID at every door. Authorization is which doors your key card opens (guest room vs staff areas).

## How It Works

### Sessions
Server stores session data; client holds only a session ID in a cookie.
```
Login → server creates session → stores in DB → sends session ID cookie
Request → browser sends cookie → server looks up session → authorized
```
**Stateful** — server must remember every session.

### JWT (JSON Web Token) — [RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519)
Self-contained signed token. Server stores nothing.
```
Login → server signs token with secret → sends JWT to client
Request → client sends JWT in header → server verifies signature → authorized
```
Structure: `header.payload.signature` (base64-encoded, dot-separated)

**Stateless** — server just verifies the signature. Scales easily.

**Risk:** JWTs can't be invalidated before expiry. Use short expiry + refresh tokens.

### OAuth 2.0 — [RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749)
Delegated authorization — "Sign in with Google/GitHub."
```
User → your app → redirected to Google → user approves → Google sends code
→ your app exchanges code for access token → your app calls Google APIs
```
OAuth is **authorization**, not authentication. OpenID Connect (OIDC) adds authentication on top of OAuth.

## Example

JWT header sent with every request:
```
Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjQyfQ.abc123
```

Decoded payload:
```json
{ "userId": 42, "exp": 1745000000 }
```

## Why It Matters

Every web app needs auth. JWT is the default for stateless APIs and mobile apps. OAuth is required whenever you integrate third-party identity providers.

---
↑ [Backend Overview](./00_backend_overview.md)

**Related:** [REST API](./01_rest_api.md), [Middleware](./03_middleware.md)
**Tags:** #software #backend
