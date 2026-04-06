# Frontend, Contract, and E2E

## What It Is

The three-layer verification chain that connects user action to backend response: UI (`App.tsx`) → typed client (`api.ts`) → API contract (`shared/contracts/api.md`) → Lambda.

## How It Works

| Layer | File | Owns |
|-------|------|------|
| UI | `App.tsx` | Renders chat, captures input, displays response |
| Typed client | `api.ts` | HTTP calls, typed request/response shapes |
| Contract | `shared/contracts/api.md` | Agreed endpoint, method, payload, error codes |
| Backend | `main.py` + modules | Implements the contract |

The contract is written first. Both sides build to it independently.

## Example

One full user flow:

```
User types "my order hasn't arrived" → clicks Send
  → App.tsx calls api.ts: sendMessage(message, session_id)
    → POST /chat { message, session_id }
      → API Gateway → Lambda → main.py
        → pii.py: no PII
        → retrieval.py: top-3 KB chunks
        → agent.py: Bedrock call with context
        → returns { response: "...", session_id }
      → 200
    → App.tsx renders response
```

## Why "works in UI" is weaker than contract + E2E

"Works in UI" confirms UX. It doesn't verify payload shape, status codes, session handling, or error paths.

A UI test can pass while the backend silently returns the wrong field name. An E2E test against the contract catches that — because the contract defines exactly what shape to assert.

## Why It Matters

The contract forces frontend and backend to agree before connecting. E2E passing means the full path was exercised end-to-end, not just per layer. Without a contract, integration bugs are found late, in production, by users.

---
← Previous: [Backend System Shape](01_backend_system_shape.md) | [Overview](00_overview.md) | Next: [Review Pipeline](03_review_pipeline.md) →
