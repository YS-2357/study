---
tags:
  - ai
  - aws
  - ml
  - security
created_at: 2026-04-17T14:18:47
updated_at: 2026-04-18T13:00:00
recent_editor: CLAUDE
---

↑ [Overview](./00_agentcore_overview.md)

# AgentCore Identity

## What It Is
AgentCore Identity is the Amazon Bedrock AgentCore service for authenticating agents when they call AWS services and third-party tools. The [AgentCore Identity documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) describes it as identity and credential management for agent access.

## How It Works
Identity gives agents a managed way to obtain and use credentials instead of embedding secrets in code. It can integrate with identity providers and token flows so the agent can call approved tools under controlled identity rules.

## Key Points

- Use Identity when an agent must call AWS services, SaaS APIs, or internal tools on behalf of a workload or user.
- Keep credentials outside prompts, source code, and long-lived environment variables.
- Design identity scopes around the tool action, not around the agent's general purpose.
- Combine Identity with [AgentCore Gateway](03_gateway.md) so authentication and tool exposure are managed together.

## Example
An agent that reads customer records can use Identity-backed access instead of storing a long-lived API token in an environment variable.

## Why It Matters
Identity reduces secret sprawl. For production agents, credential handling is part of the architecture, not an implementation detail.

---
← Previous: [AgentCore Gateway](03_gateway.md) | [Overview](./00_agentcore_overview.md) | Next: [AgentCore Code Interpreter](05_code_interpreter.md) →
