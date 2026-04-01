# AWS 201 - CS AI Assistant POC

## Purpose

Design an internal CS AI Assistant POC that generates grounded reply drafts with Strands Agents SDK and Bedrock AgentCore, enforces PII-safe handling, and requires CS review before final delivery.

## Scope Boundary

- In scope:
  - Internal CS staff workflow for turning a customer inquiry into an AI-generated draft reply.
  - Retrieval over the provided Zendesk article export and related curated support knowledge.
  - PII-safe request handling, grounded draft generation, reviewer approval, and auditability.
  - A clear upgrade path for later additions such as Cognito, long-lived memory, and broader data sources.
- Out of scope:
  - Direct customer-facing chatbot entry in v1.
  - Autonomous final response delivery without human review.
  - Durable cross-session user memory.
  - Final identity implementation details such as Cognito configuration or full RBAC.

## Current Ordered Workspace

<!-- planner:file-map:start -->
- [`00_overview.md`](./00_overview.md): Overview
- [`01_request.md`](./01_request.md): Request
- [`02_premise.md`](./02_premise.md): Premise
- [`03_tools.md`](./03_tools.md): Tools
- [`04_questions.md`](./04_questions.md): Questions
- [`05_entry-and-ui.md`](./05_entry-and-ui.md): Entry and UI
- [`06_data-and-retrieval.md`](./06_data-and-retrieval.md): Data and Retrieval
- [`07_agent-runtime.md`](./07_agent-runtime.md): Agent Runtime
- [`08_safety-and-security.md`](./08_safety-and-security.md): Safety and Security
- [`09_review-and-delivery.md`](./09_review-and-delivery.md): Review and Delivery
- [`10_observability-and-rollout.md`](./10_observability-and-rollout.md): Observability and Rollout
<!-- planner:file-map:end -->

## Flow Checks

- `05_entry-and-ui.md` locks the core product boundary: CS staff are the direct users of the POC.
- `06_data-and-retrieval.md` shapes what context the agent can see and cite, based on the Zendesk export.
- `07_agent-runtime.md` only drafts responses; it never bypasses human review.
- `08_safety-and-security.md` adds app-level PII controls before and after the model, with Guardrails as a second layer.
- `09_review-and-delivery.md` is the final control point for approval, editing, and outbound send.
- `10_observability-and-rollout.md` keeps the first cut intentionally small and identifies later additions such as Cognito and memory.

## Recommended Architecture

1. Internal CS web UI receives a customer inquiry or ticket context.
2. Backend normalizes the input and strips or masks obvious customer PII before LLM-facing processing.
3. Retrieval pipeline searches cleaned Zendesk article content and returns grounded evidence.
4. Strands Agents SDK orchestrates the RAG draft flow, running on Bedrock AgentCore Runtime.
5. Guardrails plus application validation inspect input and output for unsafe or disallowed content.
6. CS reviewer sees the draft, evidence, and safety flags, then edits or approves.
7. Final approved response is sent through the existing customer-support channel.

## Deferred Decisions

- Whether staff authentication is handled by Cognito, existing corporate SSO, or a simpler pilot-only gate.
- Whether the POC later adds case-level memory or remains request-scoped.
- Which managed retrieval/index layer is used in the first implementation pass.

## Recent Planning Memory

<!-- planner:recent-memory:start -->
- Initial AWS 201 architecture workspace created from premise 260401.
- Retrieval source confirmed as Zendesk article CSV with HTML bodies.
<!-- planner:recent-memory:end -->
