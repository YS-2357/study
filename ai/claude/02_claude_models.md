---
tags:
  - ai
  - claude
  - models
created_at: 2026-04-20T13:59:45
updated_at: 2026-04-23T23:41:19
recent_editor: CODEX
source: anthropic.com
---

↑ [Overview](./00_claude_overview.md)

# Claude Models

## What It Is

Claude is Anthropic's AI assistant model family. Models are organized in three tiers — Opus (most capable), Sonnet (balanced), Haiku (fastest) — and versioned with a major.minor number (e.g., 4.7).

## Naming Convention

`claude-[tier]-[major]-[minor]` — e.g., `claude-sonnet-4-6`, `claude-haiku-4-5-20251001`.

Models with the same snapshot date are identical across all platforms.

### Tier Name Etymology

Anthropic chose literary and musical art forms — introduced with the Claude 3 family (March 2024, [announcement](https://www.anthropic.com/news/claude-3-family)):

| Name | Origin | Why it fits |
|------|--------|-------------|
| **Haiku** | Japanese poem — 17 syllables (5-7-5), the briefest structured form | Smallest, fastest, lowest cost |
| **Sonnet** | 14-line poem (Petrarch, Shakespeare) — structured and complete | Balanced speed and intelligence |
| **Opus** | Latin for "work"; classical music's term for a major composition (e.g., Beethoven Op. 125) | Most capable, most substantial |

The progression Haiku → Sonnet → Opus mirrors poetic complexity — from the most compressed form to the most ambitious work.

## Current Models (as of Apr 2026)

| Model | Tier | Context | Max Output | Knowledge Cutoff | Input / Output (per 1M tokens) |
|-------|------|---------|------------|-----------------|-------------------------------|
| Claude Opus 4.7 | Most capable | 1M | 128k | Jan 2026 | $5 / $25 |
| Claude Sonnet 4.6 | Balanced | 1M | 64k | Aug 2025 | $3 / $15 |
| Claude Haiku 4.5 | Fastest | 200k | 64k | Feb 2025 | $1 / $5 |

## Capabilities

All current models support:
- Text and image input (vision)
- Multilingual output
- Extended thinking (Sonnet 4.6, Haiku 4.5)
- Adaptive thinking (Opus 4.7 only)
- Tool use / function calling
- Prompt caching

## Platform Availability

All models available on: Claude API, [Amazon Bedrock](../../cloud/aws/ai/01_amazon_bedrock.md), Google Cloud Vertex AI, Microsoft Foundry.

## Tier Roles

- **Opus** — complex, long-running agentic tasks; highest reasoning; rigorous and consistent
- **Sonnet** — best speed-intelligence tradeoff; coding, long-context, agent planning, design
- **Haiku** — near-frontier intelligence at lowest cost; high-volume, latency-sensitive tasks

## Why It Matters

Choosing the right tier affects cost and latency by 5–25×. Haiku handles ~80% of tasks at a fraction of Opus cost; Opus is reserved for tasks requiring deep reasoning or sustained multi-step execution.

---
↑ [Overview](./00_claude_overview.md)

**Related:** [Anthropic](01_anthropic.md), [Constitutional AI](03_constitutional_ai.md), [Amazon Bedrock](../../cloud/aws/ai/01_amazon_bedrock.md), [Prompt Caching](../concepts/12_prompt_caching.md)
**Tags:** #ai #claude #models
