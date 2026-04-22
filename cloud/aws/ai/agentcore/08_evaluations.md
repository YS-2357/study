---
tags:
  - ai
  - aws
  - ml
  - monitoring
created_at: 2026-04-17T14:18:47
updated_at: 2026-04-22T00:00:00
recent_editor: CLAUDE
---

↑ [Overview](./00_agentcore_overview.md)

# AgentCore Evaluations

## What It Is
AgentCore Evaluations is the Amazon Bedrock AgentCore capability for measuring agent quality. The [AgentCore developer guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) includes Evaluations as a service for assessing production agent behavior.

## How It Works
Evaluations scores sessions, traces, or spans against quality criteria. A team can use those scores to compare agent versions, detect regressions, and decide whether a change is safe to deploy.

## Key Points

- Evaluate task completion, tool-use accuracy, safety behavior, and answer quality separately.
- Run evaluations before deployment and continue sampling production sessions after deployment.
- Use real traces from [AgentCore Observability](07_observability.md) when possible so tests reflect actual workflows.
- Treat evaluation results as release evidence, not as a substitute for deterministic controls such as [AgentCore Policy](09_policy.md).

## Example
A release candidate agent can be evaluated on task success, answer helpfulness, and tool-use accuracy before it is promoted to production.

## Why It Matters
Production agents need measurement, not just manual spot checks. Evaluations turn quality into something teams can track over time.

---
↑ [Overview](./00_agentcore_overview.md)

**Related:** [AgentCore Observability](07_observability.md), [AgentCore Policy](09_policy.md)
**Tags:** #ai #aws #ml #monitoring
