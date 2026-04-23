---
tags:
  - software
  - backend
created_at: 2026-04-23T15:20:41
updated_at: 2026-04-23T23:41:19
recent_editor: CODEX
---

↑ [Overview](./00_backend_overview.md)

# Microservices vs Monolith

## What It Is

Two approaches to structuring a backend. A **monolith** is one deployable unit containing all functionality. **Microservices** splits functionality into many small, independently deployable services that communicate over the network.

## Analogy

A Swiss Army knife (monolith) vs a toolbox (microservices). The knife is convenient and simple — everything in one place. The toolbox lets you replace or upgrade individual tools, but you have to carry more pieces and coordinate which tool you're using.

## How It Works

**Monolith:**
```
One codebase → one build → one deployed process
User Service + Order Service + Payment Service = one app
```
- Simple to develop, test, and deploy early on
- Scales as one unit — can't scale just the payment service

**Microservices:**
```
User Service  → deployed separately, owns its DB
Order Service → deployed separately, owns its DB
Payment Service → deployed separately, owns its DB
         ↕ communicate via REST, gRPC, or message queue
```
- Each service scales independently
- Each team owns one service
- Network calls between services add latency and failure points

**Trade-offs:**

| | Monolith | Microservices |
|--|---------|---------------|
| Complexity | Low | High |
| Deployment | Simple | Requires orchestration (Kubernetes) |
| Scaling | All-or-nothing | Per-service |
| Best for | Early stage, small teams | Large orgs, independent teams |
| Failure scope | One crash can kill everything | Failures are isolated |

## Example

Netflix started as a monolith and migrated to 700+ microservices as teams and scale grew. Most startups start with a monolith and extract services only when a specific bottleneck demands it.

## Why It Matters

The default advice is **start with a monolith, extract microservices when you have a clear reason**. Premature microservices add enormous operational complexity without benefit.

---
↑ [Overview](./00_backend_overview.md)

**Related:** [Message Queues](./05_message_queues.md), [REST API](./01_rest_api.md)
**Tags:** #software #backend
