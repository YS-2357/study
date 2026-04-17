---
tags:
  - ai
  - aws
  - ml
  - security
created_at: 260417-141847
updated_at: 260417-144255
---

# AgentCore Policy

## What It Is
AgentCore Policy is the Amazon Bedrock AgentCore capability for enforcing deterministic controls over what an agent can do. The [AgentCore developer guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) lists Policy as part of the AgentCore service set for governed agent operation.

## How It Works
Policy evaluates tool-use decisions against explicit rules before the action is allowed. This gives teams a control layer that is separate from the model's generated reasoning.

## Key Points

- Use Policy for actions where prompt-only instructions are too weak, such as writes, refunds, access changes, or external notifications.
- Keep policies close to [AgentCore Gateway](03_gateway.md) tool boundaries so each rule maps to a concrete action.
- Separate policy enforcement from evaluation: Policy blocks disallowed behavior, while [AgentCore Evaluations](08_evaluations.md) measures quality.
- Review policies when adding new tools because every new tool expands what the agent can attempt.

## Example
A finance agent may be allowed to read invoices but blocked from issuing refunds above a configured threshold unless a human approval path is used.

## Why It Matters
Prompt instructions are not enough for high-risk actions. Policy gives production agents deterministic boundaries that are easier to audit and reason about.

---
← Previous: [AgentCore Evaluations](08_evaluations.md) | [Overview](00_overview.md) | Next: [Amazon Bedrock AgentCore](../32_amazon_bedrock_agentcore.md) →
