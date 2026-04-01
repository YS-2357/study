# Premise

<!-- planner:flow:start -->
## Flow Role

- Order: `02`
- Depends on: [01_request.md](./01_request.md)
- Enables / Affects: [03_tools.md](./03_tools.md)
- Purpose Fit: Captures the assumptions and constraints that the tool and architecture choices must respect.
<!-- planner:flow:end -->

## Assumptions

- The first users are CS staff operating an internal support workflow.
- The provided Zendesk article export is sufficient to prove the retrieval and grounding path in the POC.
- Human approval remains mandatory even when the draft quality is high.
- Memory and full auth design are deferred until the core RAG review flow is proven.

## Known Context

- Premise source: [premise/260401.md](./premise/260401.md)
- Service notes available:
  - [Strands Agents SDK](./aws_services/01_strands_agents_sdk.md)
  - [Bedrock AgentCore](./aws_services/02_amazon_bedrock_agentcore.md)
  - [Bedrock Guardrails](./aws_services/03_amazon_bedrock_guardrails.md)
- Data currently visible in the repo:
  - [zendesk_articles.csv](./data/zendesk_articles.csv)
  - Columns include `title`, `html_url`, `updated_at`, and `body`.
  - Article bodies are HTML, so preprocessing and chunking are required before retrieval.

## Dependencies

- AWS Bedrock model access and an AgentCore-supported region.
- An internal web UI or lightweight reviewer console.
- A preprocessing step to clean HTML article bodies into retrieval-friendly text chunks.
- A backend service boundary that owns model access, retrieval, and safety checks.

## Risks

- If raw inquiry text with customer details reaches the model path unchanged, Guardrails alone are not enough.
- HTML-heavy support articles may degrade retrieval quality if not cleaned well.
- The POC can sprawl if auth, memory, and external system integration are all introduced at once.
- Missing evidence display in the reviewer UI would make it harder to trust or audit the draft.
