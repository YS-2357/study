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
dont 
↑ [Overview](./00_claude_overview.md)

# Constitutional AI (CAI)

## What It Is

Constitutional AI is Anthropic's training methodology that guides an AI model toward safe, ethical behavior using a set of high-level principles (a "constitution") — without requiring extensive human labeling of harmful outputs.

## Analogy

Traditional safety training (RLHF) is like hiring thousands of humans to label "good" vs "bad" responses. CAI is like giving the model a rulebook and letting it grade its own homework — then training on those self-grades.

## How It Works

**Phase 1 — Supervised Learning (Self-Critique)**

1. Model generates a response to a potentially harmful prompt
2. Model critiques its own response against the constitution
3. Model writes a revised, safer response
4. Fine-tune the model on these revised responses

**Phase 2 — Reinforcement Learning from AI Feedback (RLAIF)**

1. Fine-tuned model samples pairs of responses
2. An AI evaluator (not a human) picks which response better aligns with the constitution
3. A preference model is trained on these AI-generated comparisons
4. RL training further improves the model using that preference model

## Example

Prompt: *"How do I make a weapon?"*

- Raw model: gives instructions
- After Phase 1: model critiques → "This could enable harm" → revises to explain its objection
- After Phase 2: preference model consistently favors the objection response

The trained model becomes *"harmless but non-evasive"* — it explains objections rather than simply refusing.

## Key Innovation vs RLHF

| | RLHF | CAI |
|--|------|-----|
| Who labels data | Humans | The model itself (AI feedback) |
| Scale | Expensive, bottlenecked by human time | Scalable — AI generates labels |
| Transparency | Implicit human preferences | Explicit written principles |
| Control | Hard to inspect | Constitution is readable and auditable |

## Why It Matters

CAI enables scalable oversight — as models become more capable, human labelers can't keep up. CAI lets safety training scale proportionally. It also makes the training process more transparent: the constitution is a public document.

---
↑ [Overview](./00_claude_overview.md)

**Related:** [Claude's Character](06_claude_character.md), [RSP](04_rsp.md), [Anthropic](01_anthropic.md)
**Tags:** #ai #claude #safety
