---
tags:
  - ai
  - aws
  - ml
created_at: 260417-141847
updated_at: 260417-141847
---

# AgentCore Browser

## What It Is
AgentCore Browser is the Amazon Bedrock AgentCore capability for giving agents managed browser automation. The [AgentCore developer guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) lists Browser as a service for web interaction by agents.

## How It Works
The agent sends browser actions to the managed browser environment instead of launching a browser on the application host. The browser session can navigate pages, read page content, and interact with web interfaces according to the agent workflow.

## Key Points

- Use Browser when the target system does not expose a clean API or when the workflow depends on page state.
- Prefer APIs through [AgentCore Gateway](03_gateway.md) when a stable API exists.
- Keep browser tasks narrow and observable because web pages change more often than APIs.
- Use [AgentCore Observability](07_observability.md) to trace which pages and actions were involved when a browser task fails.

## Example
A research agent can open a vendor status page, inspect the current incident banner, and summarize the result for an operator.

## Why It Matters
Many useful tasks still require web interfaces. Browser gives agents that reach without coupling production code to local browser processes.

---
← Previous: [AgentCore Code Interpreter](05_code_interpreter.md) | [Overview](00_overview.md) | Next: [AgentCore Observability](07_observability.md) →
