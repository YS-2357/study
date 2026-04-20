---
tags:
  - ai
  - claude
  - safety
created_at: 2026-04-20T13:59:45
updated_at: 2026-04-20T13:59:45
recent_editor: CLAUDE
source: anthropic.com
---

↑ [Overview](./00_claude_overview.md)

# Responsible Scaling Policy (RSP)

## What It Is

The Responsible Scaling Policy (RSP) is Anthropic's framework of technical and organizational safeguards that scale proportionally with model capability. Published September 2023. Core idea: the more dangerous a model could be, the stronger the protections required before it can be trained or deployed.

## Analogy

Think of biosafety levels (BSL-1 through BSL-4) for handling pathogens. A flu sample needs a basic lab (BSL-2); smallpox requires extreme containment (BSL-4). RSP applies the same logic to AI: more capable models require more stringent containment before deployment.

## AI Safety Levels (ASL)

| Level | Description | Current models |
|-------|-------------|---------------|
| ASL-1 | No meaningful catastrophic risk (chess AI, older models) | — |
| ASL-2 | Early dangerous capabilities, limited real-world uplift; standard LLMs | Claude Sonnet 4 |
| ASL-3 | Substantial misuse risk or early autonomous capability; strong security required | Claude Opus 4 |
| ASL-4+ | Not yet defined; expected to involve major autonomous capability jumps | Future models |

## ASL-3 Standards (Activated May 2025)

Two new requirements triggered when a model reaches ASL-3:

- **Security Standard** — Hardened internal security to prevent model weight theft
- **Deployment Standard** — Specific guardrails against CBRN (Chemical, Biological, Radiological, Nuclear) weapons uplift

## How It Works

1. Anthropic evaluates models for dangerous capability thresholds before training and deployment
2. If a model hits an ASL threshold, the corresponding standards must be in place before proceeding
3. If standards can't be met, training pauses — directly incentivizing solving safety as a condition for scaling

## Why It Matters

RSP creates an internal incentive structure: safety progress *unlocks* capability advancement. Anthropic designed it as a "race to the top" template — hoping competitors adopt similar frameworks, competing on safety rather than racing past it.

---
↑ [Overview](./00_claude_overview.md)

**Related:** [Constitutional AI](03_constitutional_ai.md), [Anthropic](01_anthropic.md), [Claude Models](02_claude_models.md)
**Tags:** #ai #claude #safety
