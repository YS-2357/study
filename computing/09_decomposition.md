# Decomposition

## What It Is

Decomposition is the practice of dividing a system into the smallest units where each unit has one reason to change. When a unit does two unrelated things, it becomes a candidate to split.

## How It Works

Every layer of a web application has its own natural unit boundary.

### Frontend

| Unit | Responsibility |
|------|---------------|
| Component | Renders one piece of the UI |
| Event handler | Responds to one user action |
| API client call | Sends one HTTP request |
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
| DNS record | Resolves one name to one address |
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

The split signal is: **one unit = one reason to change**. If fixing a search bug requires editing the same file as auth logic, the unit is too large. Decomposed units let teams change, test, and deploy each piece independently, which reduces the blast radius of any single change.

---
← Previous: [Endpoints](08_endpoints.md) | [Overview](00_overview.md) | Next: [Computing Basics — Overview](00_overview.md) →
