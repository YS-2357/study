# Safety and Security

<!-- planner:flow:start -->
## Flow Role

- Order: `08`
- Depends on: [07_agent-runtime.md](./07_agent-runtime.md)
- Enables / Affects: [09_review-and-delivery.md](./09_review-and-delivery.md)
- Purpose Fit: Adds the safety controls that make the draft flow acceptable for customer-support use.
<!-- planner:flow:end -->

## Objective

- Prevent customer PII leakage and constrain the agent/runtime so the POC remains safe and auditable.

## Decisions

- Application-level sanitization is mandatory before and after model invocation.
- Bedrock Guardrails are used as a second-layer safety control, not the only protection.
- The model and retrieval path remain behind a backend API; the browser never talks directly to Bedrock.
- Auth and role design are deferred, but the service boundary must assume internal-only access in v1.

## Plan

- Before retrieval/model use:
  - normalize ticket text
  - strip or mask obvious customer identifiers where feasible
  - block disallowed raw fields from entering prompts
- During model invocation:
  - apply Guardrails for PII and unsafe content checks
  - keep the agent in a constrained runtime with approved tools only
- After model invocation:
  - validate the draft for residual PII or unsupported claims
  - surface any redaction/safety flags in the reviewer UI
- Add audit logging for who requested a draft, what evidence was used, and whether the reviewer approved or edited it.

## Risks / Questions

- Guardrails still mean AWS receives the request text, so regulatory requirements need separate consideration if the workload becomes more sensitive.
- False positives from redaction or filtering may remove information that the CS reviewer actually needs.
- The eventual choice of Cognito versus another identity provider belongs to a later hardening pass, but API boundaries should already assume authenticated staff access.
