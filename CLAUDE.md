# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Sources

Always cite the official source when adding or correcting factual content. Link inline at the point where the claim is made, not in a separate references section.

## Language

Always respond in English unless the user explicitly asks otherwise. File content (notes, reports, etc.) may be in Korean, English, or both.

## What This Repo Is

A personal study notes repo. All content is Markdown. No build system, no tests, no dependencies.

## Note Structure

Every note file must follow this exact heading order:

```
# Title
## What It Is       ← 1-2 sentence definition (required)
## Analogy          ← only if it genuinely helps (optional)
## How It Works     ← mechanics, steps, diagrams (if applicable)
## Example          ← one concrete, small example (required)
## Why It Matters   ← practical relevance (required)
```

Every note ends with a navigation footer (preceded by `---`):

```
---
← Previous: [Title](link) | [Overview](00_overview.md) | Next: [Title](link) →
```

## Domain Layout

| Path | Content |
|------|---------|
| `ai/` | AI agents, LLM concepts (harness, tools, MCP, attention, KV cache) |
| `aws/101/aws_services/` | AWS 101 — 27 service notes (EC2 through PoP) |
| `aws/101/console_workthrough/` | Console walkthrough notes per service |
| `aws/201/aws_services/` | AWS 201 deep-dives (Bedrock, CDK, CloudWatch, Strands SDK) |
| `computing/` | CPU, virtualization, storage, GPU, caching, interfaces, endpoints |
| `git/` | Git tracking, staging, daily workflow |
| `networking/` | Protocols, addressing, OSI, DNS, HTTP |

Each domain has a `00_overview.md` as the study hub with navigation links.

## Content Rules

- Explain a concept once, in the note where it belongs — other notes link to it instead of re-explaining.
- Link inline where a concept is mentioned, not in a separate cross-references section.
- Use `> **Tip:**` for practical guidance. No other callout formats.
- No `---` horizontal rules except before the navigation footer.
- No history sections (inventor names, creation dates).
- Keep examples small and concrete, not abstract placeholders.

## README Rules

- READMEs list files/directories with one-line descriptions. No study content, no study order, no cross-references.
- Every domain README links to its `00_overview.md` for study order.
- When adding a new note, add it to both the domain README and the `00_overview.md`.
