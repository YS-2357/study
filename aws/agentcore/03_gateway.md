---
tags:
  - ai
  - aws
  - ml
created_at: 2026-04-17T14:18:47
updated_at: 2026-04-18T13:00:00
recent_editor: CLAUDE
---

↑ [Overview](./00_agentcore_overview.md)

# AgentCore Gateway

## What It Is
AgentCore Gateway is the Amazon Bedrock AgentCore service for turning existing systems into agent-accessible tools. AWS describes Gateway as a way to connect agents to tools through APIs, Lambda functions, and Model Context Protocol (MCP) servers in the [AgentCore developer guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html).

## How It Works
Gateway sits between the agent and the target system. It exposes selected capabilities as tools, then lets the agent discover and call those tools through the Gateway endpoint instead of directly wiring every backend into the agent.

## Key Points

- Use Gateway to make tool access explicit instead of hiding API clients inside the agent code.
- Expose narrow operations rather than broad administrative APIs.
- Combine Gateway with [AgentCore Policy](09_policy.md) so tool calls can be checked before execution.
- Combine Gateway with [AgentCore Identity](04_identity.md) so tools are called with managed credentials instead of hard-coded secrets.

## Example
A team can expose an internal ticket API and a Lambda refund function through Gateway, then let the agent call only those approved tools.

## Why It Matters
Gateway makes tool access explicit and central. That is easier to govern than giving an agent direct access to every API client and credential inside the application code.

---
← Previous: [AgentCore Memory](02_memory.md) | [Overview](./00_overview.md) | Next: [AgentCore Identity](04_identity.md) →
