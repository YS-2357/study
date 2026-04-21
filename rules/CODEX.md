---
tags:
  - tooling
created_at: 2026-04-17T00:00:00
updated_at: 2026-04-21T00:00:00
recent_editor: CODEX
---

# Codex

I am **Codex**, OpenAI's agent.

## 1. Rules

All rules are in [AGENTS.md](AGENTS.md). This file contains only platform-specific notes.

## 2. Session Start

Run `git pull origin main` before any read or write operation (multi-PC sync repo).

## 3. Skills

Canonical skill definitions are in `rules/skills/`. On first use of a skill, read `rules/skills/<skill>.md` and implement it in your platform's native skill/command format. Do not copy `.claude/commands/` files.

Skills to implement: `ingest`, `lint`, `nav-update`, `ocr`, `split`.

## 4. Automation Location

- Codex keeps repo-local automation in `.codex/`
- Shared Git hook entrypoints in `.githooks/`

## 4. Permission Style

Request persistent approval only for bounded Git actions:

- `git add <specific paths>`
- `git commit -m "<message>"`
- `git push origin main`

Run Git commands as simple, single-purpose commands. Avoid wrappers.

## 5. Write Commands

Run Git write commands with escalated permissions immediately:
- `git add`, `git commit`, `git push`, `git pull`

Windows may fail on `.git/index.lock` if sandbox tried first.

## 6. OCR

For raw image OCR, use [11_ocr.md](11_ocr.md) and the Codex skill in `.codex/skills/ocr/`. Keep event-specific session maps, temporary scripts, and OCR outputs under `raw/`.
