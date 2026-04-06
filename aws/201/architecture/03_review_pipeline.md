# Review Pipeline

## What It Is

The project-specific review system used in the 201 Codex build: a 15-criteria scoring loop where every agent output passes through a reviewer and supervisor before being accepted.

For the general concept (role separation, adversarial gaps, behavioral vs structural bugs) see [Multi-Agent Orchestration](../../../ai/13_multi_agent_orchestration.md).

## How It Works

### Scoring

Every submission is scored against 15 criteria across these categories:

- CDK ownership (all resources in stack, no manual console)
- IAM correctness (least privilege, no wildcard)
- Security (PII handling, secrets in SSM not env vars)
- Contract compliance (API shape matches `shared/contracts/api.md`)
- Test coverage (E2E passes, edge cases covered)
- Cleanup (cdk destroy leaves zero orphans)
- Runtime behavior (no crashes, correct status codes)

### Decision thresholds

| Score | Decision |
|-------|----------|
| 15/15 | Approve |
| 10–14 | Conditional approve — fix named items, resubmit |
| < 10 | Reject — restart task |

### Actual cycles from today

| Task | Score | Decision | Outcome |
|------|-------|----------|---------|
| TASK-002a (infra) | Warning | Conditional | Fixed → TASK-002b passed |
| TEST-002 (SSM bug) | Fail item | Conditional | SSM moved into CDK → passed |

### What conditional approve means

Conditional approve is not "ship it and fix later." It means: fix the specific named items, resubmit, and the reviewer re-scores only those items. The loop doesn't restart from zero.

## Why It Matters

The review pipeline caught the SSM parameter bug — a structural violation that runtime testing never surfaces. Without it, `cdk destroy` would have orphaned the parameter silently.

> **Tip:** Define your 15 criteria before the first task runs. Criteria added mid-project introduce inconsistency — earlier tasks weren't scored against them.

---
← Previous: [Frontend, Contract, and E2E](02_frontend_contract_e2e.md) | [Overview](00_overview.md)
