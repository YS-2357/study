# Study Agent Guide

This file provides shared guidance to coding agents working in this repository.

## Scope

These instructions apply to the entire `study/` repository unless a deeper `AGENTS.md` or `CLAUDE.md` overrides them for a subtree.

## Source Of Truth

- Follow the detailed note-format and README standards in [README.md](README.md).
- Use this file as the compact operating guide for agents working in this repo.

## Sources

- Always cite the official source when adding or correcting factual content.
- Link inline at the point where the claim is made, not in a separate references section.

## Language

- Always respond in English unless the user explicitly asks otherwise.
- File content such as notes and reports may be in Korean, English, or both.

## What This Repo Is

- A personal study notes repo.
- All content is Markdown.
- No build system, no tests, no dependencies.

## Core Rules

- `README.md` files must stay folder indexes only. Do not add study content, study order, or concept explanations to a README.
- The nearest relevant `00_overview.md` is the study hub for its subtree. Update that overview when notes in that subtree are added, removed, renamed, or reordered.
- Explain a concept once in the note where it belongs. In other notes, link to the existing explanation instead of duplicating it.
- On first use in a note, write the full name before the abbreviation in parentheses, then use the short form afterward. Example: `Cloud Development Kit (CDK)`.
- Link inline where a concept is mentioned, not in a separate cross-references section.
- Use `> **Tip:**` for practical guidance. No other callout formats.
- No `---` horizontal rules except before the navigation footer.
- No history sections such as inventor names or creation dates.
- Keep examples small and concrete, not abstract placeholders.
- Prefer editing existing Markdown notes, links, and navigation over adding tooling, scripts, or structural churn.
- Preserve the repository's existing organization unless the task explicitly requires a reorganization.

## Note Structure

Every note file must follow this heading order:

```md
# Title
## What It Is
## Analogy
## How It Works
## Example
## Why It Matters
```

Rules:
- `What It Is` is required and should be a 1-2 sentence definition.
- `Analogy` is optional and should appear only if it genuinely helps.
- `Example` is required and should be concrete and small.
- `Why It Matters` is required.

Every note ends with a navigation footer preceded by `---`:

```md
---
← Previous: [Title](link) | [Overview](00_overview.md) | Next: [Title](link) →
```

## Domain Layout

| Path | Content |
|------|---------|
| `ai/` | AI agents, LLM concepts such as harness, tools, MCP, attention, and KV cache |
| `aws/101/aws_services/` | AWS 101 service notes |
| `aws/101/console_workthrough/` | Console walkthrough notes per service |
| `aws/201/aws_services/` | AWS 201 deep-dives |
| `computing/` | CPU, virtualization, storage, GPU, caching, interfaces, endpoints |
| `git/` | Git tracking, staging, daily workflow |
| `networking/` | Protocols, addressing, OSI, DNS, HTTP |

Each domain has a `00_overview.md` as the study hub with navigation links.

## Primary Artifacts

- `README.md`: folder index and directory description only
- `00_overview.md`: study hub and ordered navigation for a subtree
- concept notes: the main study content
- walkthrough notes: step-by-step operational or console guides
- image references: screenshots and image assets used by notes

## Editing Checklist

- If you edit a note, preserve the required structure defined in [README.md](README.md).
- If you edit a note, preserve or repair the navigation footer.
- If you add or rename a note, update the nearest relevant `00_overview.md`.
- If a folder's contents change materially, update that folder's `README.md`.
- If a concept is already documented elsewhere, link to the existing note instead of re-explaining it.
- Do not put study content into `README.md`.

## README Rules

- READMEs list files and directories with one-line descriptions.
- READMEs do not contain study content, study order, or cross-references.
- Every domain README links to its `00_overview.md` for study order.
- When adding a new note, add it to both the domain README and the relevant `00_overview.md`.

## Subtree Policy

- Add a nested `AGENTS.md` or `CLAUDE.md` only when a subtree needs materially different instructions from the repo root.
- Keep subtree files narrow. They should extend or override root behavior only for that subtree.

## Agent Delivery Hooks

- Working rule: `"실패는 요란하게, 성공은 조용하게"` ("fail loudly, succeed quietly").
- When an agent creates, fixes, renames, moves, or deletes a file, it must finish the delivery loop in the same turn when feasible: update the relevant docs, verify repo and folder rules, check security, commit, and push.
- Relevant docs usually include the nearest `00_overview.md`, the folder `README.md`, navigation footers, and any note links affected by the change.
- Before pushing, the agent must confirm that changed files follow this repo's Markdown structure, README rules, and navigation rules.
- Before pushing study-content Markdown, the agent must review the changed study files and explicitly acknowledge that it knows their contents. Repo plumbing such as `.claude/`, `.codex/`, `.githooks/`, `.kiro/`, `.env`, `AGENTS.md`, and `CLAUDE.md` is excluded from this acknowledgment check.
- Before pushing, the agent must check for security problems such as secrets, tokens, credentials, private keys, or unsafe command snippets that accidentally embed real sensitive values. If a security issue is found, stop and fix it before pushing.
- Git hook entrypoints live in `.githooks/`, while agent-specific hook logic lives in `.codex/hooks/` and `.claude/hooks/`. Keep automation separated this way so Codex and Claude can evolve independently.
- Keep agent-specific skills, helper files, and automation separated too: Codex-owned assets belong under `.codex/`, and Claude-owned assets belong under `.claude/`.
- The hook enforces the mechanical checks, but the agent is still responsible for deciding which related docs need updates.

## Git Push

Token is in `.env` as `GITHUB_TOKEN`. Use this command to push:

```bash
set -a && source .env && set +a && git -c credential.helper= -c "http.https://github.com/.extraheader=AUTHORIZATION: basic $(printf 'YS-2357:%s' "$GITHUB_TOKEN" | base64 -w0)" push origin main
```
