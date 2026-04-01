# Tools

<!-- planner:flow:start -->
## Flow Role

- Order: `03`
- Depends on: [02_premise.md](./02_premise.md)
- Enables / Affects: [04_questions.md](./04_questions.md)
- Purpose Fit: Locks the concrete commands, CLIs, AWS interfaces, and related references needed to execute the scoped POC without drifting into unrelated delivery or product work.
<!-- planner:flow:end -->

## Commands

- `python3 -m venv .venv` and `source .venv/bin/activate` for the local Python environment that will host ingestion, API, and agent code.
- `aws sts get-caller-identity` to verify the target AWS account before Bedrock or AgentCore work starts.
- `aws bedrock list-foundation-models --region us-east-1` or `aws bedrock list-foundation-models --region us-west-2` to confirm model access in an AgentCore-supported region.
- `python3 -m pytest` for preprocessing, retrieval, safety, and review-loop validation once the implementation code exists.

## MCP / Connectors

- No Codex MCP connector is required to implement the first cut inside this repo.
- If the runtime later needs agent-callable tools beyond retrieval, prefer MCP-compatible exposure through AgentCore Gateway or Strands MCP tools instead of direct browser/support-tool automation in v1.

## CLI Tools

- `aws` CLI for Bedrock access checks, region validation, and later CloudWatch/identity inspection.
- `npm install -g @aws/agentcore` to install the AgentCore CLI.
- `agentcore create --name <agent-name> --defaults` to scaffold the runtime project.
- `agentcore dev` to validate the agent locally before deployment.
- `agentcore deploy` to push the runtime into Bedrock AgentCore.
- `agentcore invoke --runtime <agent-name> "<prompt>"` to sanity-check the deployed runtime.

## Required Skills or Plugins

- [Strands Agents SDK notes](../aws_services/01_strands_agents_sdk.md)
- [Bedrock AgentCore notes](../aws_services/02_amazon_bedrock_agentcore.md)
- [Bedrock Guardrails notes](../aws_services/03_amazon_bedrock_guardrails.md)

## External Systems

- AWS account with Bedrock model access and AgentCore support in `us-east-1` or `us-west-2`.
- Source support content from [zendesk_articles.csv](../data/zendesk_articles.csv) and any curated CS knowledge added beside it.
- Internal web UI plus backend API boundary for CS reviewers; the browser should not call Bedrock directly.
- The eventual outbound delivery channel used by CS after approval, likely an existing support tool rather than the AI service itself.
