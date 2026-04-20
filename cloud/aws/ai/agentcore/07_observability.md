---
tags:
  - ai
  - aws
  - ml
  - monitoring
created_at: 2026-04-17T14:18:47
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
---

↑ [Overview](./00_agentcore_overview.md)

# AgentCore Observability

## What It Is
AgentCore Observability is the Amazon Bedrock AgentCore capability for tracing, debugging, and monitoring agent execution. AWS positions Observability as part of operating AgentCore agents in production in the [AgentCore developer guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html).

## How It Works
Observability records what happened during an agent run, including model calls, tool calls, errors, latency, and session behavior. Those signals help teams debug failures and understand whether the agent is behaving as expected.

## Key Points

- Capture traces for model calls, tool calls, policy decisions, and runtime errors.
- Watch latency and failure rates separately from answer quality; both matter in production.
- Use traces to compare what the agent intended, which tool it called, and what the tool returned.
- Feed findings into [AgentCore Evaluations](08_evaluations.md) so repeated failures become measurable test cases.

## Example
When a multi-step agent returns a wrong answer, Observability can help inspect which tool was called, what the model saw, and where the workflow diverged.

## Why It Matters
Agent failures are often workflow failures, not just code exceptions. Observability gives teams the evidence needed to improve prompts, tools, policies, and runtime behavior.

---
↑ [Overview](./00_agentcore_overview.md)

**Related:** [AgentCore Browser](06_browser.md), [AgentCore Evaluations](08_evaluations.md)
**Tags:** #ai #aws #ml #monitoring
