# Request

<!-- planner:flow:start -->
## Flow Role

- Order: `01`
- Depends on: [00_overview.md](./00_overview.md)
- Enables / Affects: [02_premise.md](./02_premise.md)
- Purpose Fit: Restates the assignment and fixes the success criteria that all later files must satisfy.
<!-- planner:flow:end -->

## Goal

- Build a CS AI Assistant POC for the AWS 201 assignment.
- Use Strands Agents SDK plus Bedrock AgentCore to create RAG-based reply drafts for customer inquiries.
- Keep CS staff in the loop so the AI never sends a final answer directly.

## Success Criteria

- The service can turn a staff-entered inquiry into a grounded draft reply.
- The draft is backed by retrievable support knowledge from the provided data.
- Customer PII is not exposed in the AI-visible or AI-generated output path.
- A CS reviewer can inspect, edit, approve, or reject the draft before sending.
- The architecture is simple enough for a POC but leaves clean extension points for auth and memory later.

## In Scope

- Internal staff UI and backend entry path.
- RAG retrieval from the Zendesk export and curated support content.
- Draft generation, grounding, safety filtering, and approval workflow.
- Service selection and component boundaries for AWS implementation.

## Out of Scope

- Customer self-service chat entry.
- Full CRM/Zendesk bi-directional integration design.
- Personalization or memory across multiple customer sessions.
- Production-grade IAM and identity rollout detail.

## Constraints

- The AI answer must not include customer personal information.
- The system is a drafting assistant, not an autonomous responder.
- The CS data currently available is a drive-uploaded dataset plus a local Zendesk article CSV export.
- Bedrock AgentCore availability may constrain region choice, so the plan should stay compatible with `us-east-1` or `us-west-2`.
