# Review and Delivery

<!-- planner:flow:start -->
## Flow Role

- Order: `09`
- Depends on: [08_safety-and-security.md](./08_safety-and-security.md)
- Enables / Affects: [10_observability-and-rollout.md](./10_observability-and-rollout.md)
- Purpose Fit: Ensures the service remains a human-reviewed drafting assistant rather than an autonomous responder.
<!-- planner:flow:end -->

## Objective

- Define the human approval loop and the boundary between AI draft generation and final customer communication.

## Decisions

- Every draft must be reviewed by a CS 담당자 before outbound delivery.
- The reviewer can:
  - approve as-is
  - edit and then approve
  - reject and request a new draft
- The system should preserve the evidence used for the draft so the reviewer can justify or correct the final answer.

## Plan

- Show the reviewer:
  - input inquiry
  - generated draft
  - cited support content
  - safety flags and redaction notes
- Record outcome states such as `drafted`, `edited`, `approved`, and `rejected`.
- Keep the outbound delivery integration simple for the POC:
  - manual send or lightweight handoff is acceptable
  - full bidirectional support-tool integration can wait until the review experience is validated

## Risks / Questions

- If the review step is too slow or too opaque, the POC will not feel useful even if the draft quality is good.
- If approvals are not logged, it will be hard to explain how the final customer response was produced.
