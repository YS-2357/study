# Questions

<!-- planner:flow:start -->
## Flow Role

- Order: `04`
- Depends on: [03_tools.md](./03_tools.md)
- Enables / Affects: [05_entry-and-ui.md](./05_entry-and-ui.md)
- Purpose Fit: Records what is already decided for the POC cut and what remains open without blocking the first architecture.
<!-- planner:flow:end -->

## Open Questions

- Which existing support system should receive the final approved response: Zendesk, email, or a manual copy-paste workflow for the demo?
- Which retrieval implementation is best for the first pass: a lightweight custom vector index, Bedrock knowledge-base style integration, or another managed store?
- Which Bedrock model should be used for draft generation versus safety/validation checks?
- How aggressively should inquiry-side PII be masked before retrieval, especially when the ticket text itself may include order or account details?

## Decided

- Direct users of the POC are CS staff, not end customers.
- The agent only drafts; a human reviewer must approve before any final response is sent.
- Guardrails are necessary but not sufficient; application-level sanitization and validation stay in scope.
- Durable memory is deferred from the first architecture cut.
- Cognito is noted as a later identity option rather than a core dependency of the initial flow.

## Items That Change the Plan Flow

- If the product becomes customer-facing, `05_entry-and-ui.md` and `08_safety-and-security.md` both need major redesign.
- If cross-session case memory is added, `07_agent-runtime.md` and `10_observability-and-rollout.md` need to expand first.
- If the outbound delivery channel becomes fully integrated, `09_review-and-delivery.md` must absorb that boundary instead of staying tool-agnostic.
