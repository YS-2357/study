---
tags:
  - tooling
created_at: 2026-04-17T00:00:00
updated_at: 2026-04-21T00:00:00
recent_editor: CODEX
---

# Kiro

I am **Kiro**, AWS's agent.

## 1. Rules

All rules are in [AGENTS.md](AGENTS.md). This file contains only platform-specific notes.

## 2. Session Start

Run `git pull origin main` before any read or write operation (multi-PC sync repo).

## 3. Skills

Canonical skill definitions are in `rules/skills/`. On first use of a skill that doesn't exist in `.kiro/skills/`, read `rules/skills/<skill>.md` and create a Kiro-native implementation in `.kiro/skills/<skill>.md`. Do not copy `.claude/commands/` files.

Skills to implement: `ingest`, `lint`, `nav-update`, `ocr`, `split`.

## 4. Status

Kiro-specific automation will be added when integration is configured.

## 5. Automation Location

When configured:
- Entrypoints in `.githooks/`
- Kiro-specific logic in `.kiro/hooks/`

## 6. OCR

For raw image text extraction, use [11_ocr.md](11_ocr.md) and implement the shared [ocr](skills/ocr.md) procedure in `.kiro/skills/ocr.md` if needed. Prefer direct visual reading in small batches, and keep extraction outputs under `raw/`.
