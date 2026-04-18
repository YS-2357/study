---
tags:
  - computing
created_at: 2026-04-10T00:00:00
updated_at: 2026-04-18T18:37:25
recent_editor: CODEX
---

↑ [Overview](./00_computing_overview.md)

# Decomposition

## What It Is

Decomposition is the practice of dividing a system into the smallest units where each unit has one reason to change. When a unit does two unrelated things, it becomes a candidate to split.

## How It Works

The working rule is: **one unit = one reason to change**.

In practice, that means a unit should do one coherent job, accept a clear input, produce a clear output, and change for one kind of reason only. If a unit contains presentation, validation, persistence, and permission logic together, it is carrying multiple change reasons and should be split.

The philosophy behind this is to separate policy from mechanism and decisions from side effects. Business rules, UI rendering, database access, and infrastructure concerns may participate in the same feature, but they should not live in the same unit just because they are part of the same request flow.

Every layer of a web application has its own natural unit boundary.

### Frontend

| Unit | Responsibility |
|------|---------------|
| Component | Renders one piece of the UI |
| Event handler | Responds to one user action |
| API client call | Sends one [HTTP request](../networking/05_http.md) |
| State update | Reflects one change in the UI |

### Backend

| Unit | Responsibility |
|------|---------------|
| Route | Maps one URL and method to a handler |
| Middleware | Applies one cross-cutting concern (auth, rate limit) |
| Handler | Validates one request and delegates to a service |
| Service function | Executes one piece of business logic |
| Repository function | Runs one database operation |

### Infrastructure

| Unit | Responsibility |
|------|---------------|
| Compute unit | Runs one function or service (Lambda, container) |
| IAM policy statement | Grants one permission on one resource |
| Security group rule | Allows one type of traffic on one port |
| [DNS record](../networking/04_dns.md) | Resolves one name to one address |
| Network path | Connects one source to one destination |

### Database

| Unit | Responsibility |
|------|---------------|
| Table / Collection | Stores one entity type |
| Column / Field | Holds one attribute of that entity |
| Index | Optimizes one query path |
| Query / Statement | Performs one read or write operation |
| Transaction | Groups operations that must succeed or fail together |
| Schema / Namespace | Owns one domain boundary |

### Realizing It In Code

To implement decomposition in code, define units around what changes together rather than around what seems related in one feature.

| Code unit | One reason to change |
|-----------|----------------------|
| UI component | Presentation or interaction changes |
| Validator | Input rules change |
| Auth / permission check | Access policy changes |
| Service / use-case function | Business decision changes |
| Repository / query function | Storage or query behavior changes |
| API client / gateway | External integration changes |
| Infrastructure resource | Platform or deployment behavior changes |

When writing code, a useful test is whether the unit can be described in one sentence without using "and". If the description becomes "validates input and saves data" or "renders results and checks permissions", the unit is still too large.

> **Tip:** Keep orchestration thin. A handler or controller may coordinate several units, but it should not absorb their responsibilities.

## Example

A user submits a text query. The request travels through one unit per concern:

```
UI Component          → renders search input
  onSubmit handler    → captures input, calls fetch
    POST /api/search  → one API client call
      Route           → maps POST /api/search to handler
        Auth middleware → checks token (one concern)
          Handler     → validates query, calls service
            Service fn → applies search logic
              Repo fn → runs one DB query
                Table → stores one entity type (search_logs)
```

Each step has one job. Changing the search logic touches only the service function. Changing auth touches only the middleware.

## Why It Matters

The split signal is: **one unit = one reason to change**. If fixing a search bug requires editing the same file as auth logic, the unit is too large. If a database tuning change forces edits to business rules, the boundary is weak. If a UI redesign changes persistence code, the decomposition is poor.

Well-decomposed units are easier to test, replace, and reason about because each one owns a narrow responsibility. This reduces the blast radius of change and makes the system easier to evolve without accidental coupling.

---
← Previous: [Endpoints](08_endpoints.md) | [Overview](./00_computing_overview.md)
