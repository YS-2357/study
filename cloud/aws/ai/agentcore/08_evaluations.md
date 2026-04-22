---
tags:
  - ai
  - aws
  - ml
  - monitoring
created_at: 2026-04-17T14:18:47
updated_at: 2026-04-22T09:57:48
recent_editor: CLAUDE
source:
  - aws-partner-summit-seoul-2026
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

## 3-Level Monitoring

| Level | What It Measures |
|-------|-----------------|
| Session | Goal success rate — did the agent complete the end-to-end user goal? |
| Trace | Response quality — 10 metrics per response (correctness, helpfulness, etc.) |
| Span | Tool selection & parameter accuracy — did the agent call the right tool with right args? |

### Silent Failure Pattern

Agents fail invisibly: dashboard metrics (latency, error rate) look fine while actual quality degrades. Example: a prompt edit accidentally removes a tool selection guide → tool accuracy drops 0.91 → 0.30 (67%), but no alert fires for weeks.

AgentCore Evaluations catches this via continuous trace monitoring.

## Evaluation Modes

| Mode | Trigger | Use Case |
|------|---------|----------|
| **Online** | 1–2% production traffic sampling | Real-time quality monitoring |
| **On-Demand** | CI/CD pipeline integration | Pre-deployment gate |

**Setup: 5 minutes.** Framework-agnostic — works with Bedrock Agent, Strands, LangChain, or custom agents.

## Judge Gate in CI/CD

```
Code Change → Build → [AgentCore Eval Gate] → Deploy
                              ↓ (quality drop)
                         Auto-rollback
```

Add AgentCore Evaluations as an on-demand step in your pipeline; block deploys when quality drops below threshold.

---
↑ [Overview](./00_agentcore_overview.md)

**Related:** [AgentCore Observability](07_observability.md), [AgentCore Policy](09_policy.md)
**Tags:** #ai #aws #ml #monitoring
