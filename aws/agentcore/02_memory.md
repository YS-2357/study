---
tags:
  - ai
  - aws
  - ml
created_at: 2026-04-17T14:18:47
updated_at: 2026-04-18T11:46:13
recent_editor: CLAUDE
---

↑ [Overview](./00_agentcore_overview.md)

# AgentCore Memory

## What It Is
AgentCore Memory is the Amazon Bedrock AgentCore capability for storing agent context across interactions. The [AgentCore developer guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) lists Memory as a service that helps agents maintain useful context beyond a single request.

## How It Works
An agent writes useful information from a session into Memory and retrieves relevant context in later sessions. This keeps the agent code from needing to build a custom database, retrieval layer, and retention strategy before it can remember user preferences or prior work.

## Key Points

- Store only information that should influence future sessions, not every transient token from every interaction.
- Separate user-specific memory from shared team or application memory when privacy and personalization matter.
- Treat Memory as agent context, not as the source of truth for business records.
- Pair Memory with [AgentCore Evaluations](08_evaluations.md) to catch regressions where remembered context makes answers worse instead of better.

## Example
A support agent can remember that a user prefers concise answers and usually asks about billing incidents, then retrieve that preference during later sessions.

## Why It Matters
Agents are often stateless by default. Memory gives a production agent continuity without forcing every team to design its own persistence model.

---
← Previous: [AgentCore Runtime](01_runtime.md) | [Overview](./00_agentcore_overview.md) | Next: [AgentCore Gateway](03_gateway.md) →
