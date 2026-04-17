---
tags:
  - tooling
created_at: 2026-04-17T00:00:00
updated_at: 2026-04-17T00:00:00
recent_editor: CLAUDE
---

# Codex

I am **Codex**, OpenAI's agent.

## 1. Rules

All rules are in [AGENTS.md](AGENTS.md). This file contains only platform-specific notes.

## 2. Automation Location

- Codex keeps repo-local automation in `.codex/`
- Shared Git hook entrypoints in `.githooks/`

## 3. Permission Style

Request persistent approval only for bounded Git actions:

- `git add <specific paths>`
- `git commit -m "<message>"`
- `git push origin main`

Run Git commands as simple, single-purpose commands. Avoid wrappers.

## 4. Write Commands

Run Git write commands with escalated permissions immediately:
- `git add`, `git commit`, `git push`, `git pull`

Windows may fail on `.git/index.lock` if sandbox tried first.
