# Entry and UI

<!-- planner:flow:start -->
## Flow Role

- Order: `05`
- Depends on: [04_questions.md](./04_questions.md)
- Enables / Affects: [06_data-and-retrieval.md](./06_data-and-retrieval.md)
- Purpose Fit: Fixes the product boundary and reviewer workflow before the retrieval and agent internals are defined.
<!-- planner:flow:end -->

## Objective

- Define how CS staff enter the POC and what the reviewer-facing experience must show.

## Decisions

- The POC entry is an internal web UI for CS staff only.
- The UI should accept either pasted customer inquiry text or selected ticket context from an internal workflow.
- The reviewer UI must show:
  - customer inquiry summary
  - generated draft
  - retrieved evidence/citations
  - safety or redaction flags
  - approve, edit, reject, and regenerate controls

## Plan

- Keep the browser thin: UI sends inquiry/ticket context to a backend API, not directly to Bedrock.
- Add an explicit reviewer step before any outbound action.
- Make evidence visibility first-class so CS staff can quickly verify why the draft was produced.
- Keep auth abstract in v1: the UI should have a single authenticated-staff boundary, but the exact provider can be deferred.

## Risks / Questions

- If the demo starts as an unauthenticated internal tool, the later auth retrofit must not change the core API contracts.
- If the reviewer UI hides evidence or redactions, staff trust in the system will be weak.
