# Tools

<!-- planner:flow:start -->
## Flow Role

- Order: `03`
- Depends on: [02_premise.md](./02_premise.md)
- Enables / Affects: [04_questions.md](./04_questions.md)
- Purpose Fit: Maps the architecture to the minimum AWS and application components needed for the POC.
<!-- planner:flow:end -->

## Tool Matrix

| Tool Type | Required | Purpose |
| --- | --- | --- |
| Strands Agents SDK | Yes | Orchestrate retrieval-aware draft generation and tool usage flow. |
| Bedrock AgentCore Runtime | Yes | Host the agent in a production-like runtime with observability and future identity/memory hooks. |
| Bedrock Guardrails | Yes | Add input/output screening and PII/content filtering as one safety layer. |
| Retrieval / index layer | Yes | Search the cleaned Zendesk article corpus and return grounded evidence. |
| Internal web UI | Yes | Give CS staff a place to submit inquiries and review drafts. |
| Backend API service | Yes | Own retrieval, prompt construction, model calls, validation, and audit logging. |
| Cognito or SSO | Later | Optional staff authentication layer once the core flow is working. |
| Durable memory | Later | Optional follow-on for case continuity after the base POC succeeds. |

## Required Skills or Plugins

- [Strands Agents SDK notes](./aws_services/01_strands_agents_sdk.md)
- [Bedrock AgentCore notes](./aws_services/02_amazon_bedrock_agentcore.md)
- [Bedrock Guardrails notes](./aws_services/03_amazon_bedrock_guardrails.md)

## External Systems

- AWS Bedrock model access and AgentCore support in the target region.
- Source support content exported from Zendesk.
- The eventual outbound delivery channel used by CS after approval, likely an existing support tool rather than the AI service itself.
