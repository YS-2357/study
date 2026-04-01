# Agent Runtime

<!-- planner:flow:start -->
## Flow Role

- Order: `07`
- Depends on: [06_data-and-retrieval.md](./06_data-and-retrieval.md)
- Enables / Affects: [08_safety-and-security.md](./08_safety-and-security.md)
- Purpose Fit: Explain how this file advances the user goal without drifting outside scope.
<!-- planner:flow:end -->

## Objective

- Use Strands Agents SDK and Bedrock AgentCore to create grounded, reviewable draft responses without expanding into unnecessary runtime complexity.

## Decisions

- Strands Agents SDK is the orchestration layer for the POC agent.
- Bedrock AgentCore Runtime is the hosting/runtime target for a production-like deployment model.
- The agent is request-scoped and stateless for now.
- The agent’s job is to generate a draft reply and supporting rationale, not to send messages or mutate external systems.

## Plan

- Backend invokes the agent with:
  - sanitized inquiry text
  - retrieved support evidence
  - drafting instructions and tone constraints
- Agent produces:
  - draft response
  - evidence references
  - optional confidence or uncertainty markers for the reviewer
- Keep tool access narrow:
  - retrieval lookup is allowed
  - arbitrary external API calls are not needed for the first cut
- Use AgentCore Observability from the beginning so each inference and tool step is traceable.

## Risks / Questions

- If the prompt does not strongly enforce grounding, the draft may over-generalize beyond the retrieved evidence.
- If the agent gets direct access to too many tools too early, the POC surface area will grow without improving the core demo.
- Exact model and prompt design remain implementation details for the next stage.
