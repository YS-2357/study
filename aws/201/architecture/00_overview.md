# AWS 201 — Architecture Patterns

Application-level design patterns for RAG + agent systems. Not AWS service references — these cover how modules, contracts, and review systems fit together.

## Notes

1. [Backend System Shape](01_backend_system_shape.md) — Five modules, one responsibility each; check order in the request lifecycle.
2. [Frontend, Contract, and E2E](02_frontend_contract_e2e.md) — UI, typed client, API contract, and why E2E is stronger than UI testing.
3. [Review Pipeline](03_review_pipeline.md) — 15-criteria scoring, decision thresholds, and the actual cycles from the Codex build.
