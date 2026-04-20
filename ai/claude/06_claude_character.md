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

# Claude's Character

## What It Is

Claude's character is the set of values, personality traits, and behavioral priorities that Anthropic trains into Claude — not as rules to follow, but as internalized dispositions. The goal is a model that reasons from principles rather than pattern-matches to rules.

## The Constitution — Priority Order

When Claude's values conflict, it follows this hierarchy:

1. **Broadly Safe** — Don't undermine human oversight of AI during this critical period of development
2. **Broadly Ethical** — Be honest, avoid harmful actions, have good values
3. **Guideline-Compliant** — Follow Anthropic's operational guidance
4. **Genuinely Helpful** — Benefit users and operators substantively

Safety outranks ethics because Claude might be wrong about ethics; humans need the ability to correct it.

## Core Traits

| Trait | What It Means |
|-------|--------------|
| Intellectual humility | Sees multiple perspectives; admits uncertainty; not afraid to disagree with factually wrong views |
| Honesty | High truthfulness bar; no white lies; non-manipulative; calibrated confidence |
| Genuine curiosity | Interested in the user's perspective and values; engages substantively |
| Directness | Says what it thinks; doesn't pander or tell people what they want to hear |

## What Claude Is Not Trained To Do

- **Pander** — Adopt users' views uncritically
- **False neutrality** — Enforce a "middle" position while claiming objectivity
- **Evasive refusals** — Simply refuse without explanation; instead, explain objections

## "Brilliant Friend" Framing

Anthropic describes the target as *"a brilliant friend who happens to have the knowledge of a doctor, lawyer, financial advisor"* — one who gives frank, real information, respects your autonomy, and engages with your actual situation rather than giving overly cautious advice driven by liability.

## How Character Was Trained

1. Claude generates human messages relevant to character traits
2. Claude produces multiple response candidates aligned with those traits
3. Claude ranks responses by alignment quality
4. A preference model is trained on the synthetic rankings
5. RL training internalizes the preferences into the base model

## Why It Matters

Claude's character is why it behaves consistently across contexts — the same curiosity and honesty in a coding task as in a philosophical debate. Understanding this explains both its strengths (frank, substantive help) and its limits (won't help undermine human AI oversight, even if instructed).

---
↑ [Overview](./00_claude_overview.md)

**Related:** [Constitutional AI](03_constitutional_ai.md), [RSP](04_rsp.md), [Anthropic](01_anthropic.md)
**Tags:** #ai #claude #safety
