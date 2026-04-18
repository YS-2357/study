---
tags:
  - ai
  - aws
  - ml
  - serverless
created_at: 2026-04-17T14:18:47
updated_at: 2026-04-18T12:30:09
recent_editor: CLAUDE
---

↑ [Overview](./00_agentcore_overview.md)

# AgentCore Runtime

## What It Is
AgentCore Runtime is the Amazon Bedrock AgentCore service for hosting and invoking agent code as production infrastructure. AWS describes AgentCore Runtime as a way to securely deploy and scale dynamic AI agents and tools using supported frameworks and protocols in the [AgentCore Runtime guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html).

## How It Works
You package the agent, deploy it to Runtime, and invoke it through the generated runtime endpoint. Runtime handles the agent execution environment while the agent code still owns the reasoning loop, model calls, and tool decisions.

## Key Points

- Use Runtime when the agent needs managed production hosting instead of a local process or generic script runner.
- Keep framework code separate from Runtime concerns: the framework decides how the agent reasons, while Runtime hosts and invokes the agent.
- Add [AgentCore Observability](07_observability.md) early so runtime failures, tool calls, and latency can be traced after deployment.
- Use [AgentCore Identity](04_identity.md), [AgentCore Gateway](03_gateway.md), and [AgentCore Policy](09_policy.md) when the runtime needs governed access to external systems.

## Example
An agent built with [Strands Agents SDK](../11_strands_agents_sdk.md) can run locally during development, then be deployed to Runtime so application code calls a managed endpoint instead of a local process.

## Why It Matters
Runtime is the compute anchor for AgentCore. Without it, Memory, Gateway, Identity, Observability, Evaluations, Code Interpreter, Browser, and Policy are supporting capabilities around agent execution rather than a complete production agent platform.

---
← Previous: [AgentCore Services Overview](./00_agentcore_overview.md) | [Overview](./00_agentcore_overview.md) | Next: [AgentCore Memory](02_memory.md) →
