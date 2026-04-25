---
tags:
  - tooling
created_at: 2026-04-23T23:41:19
updated_at: 2026-04-26T08:37:43
recent_editor: CODEX
---

# Agent Rules

Behavioral guidelines to reduce common agent mistakes. Merge these with Claude-specific repo rules as needed.

Tradeoff: these guidelines bias toward caution over speed. For trivial tasks, use judgment.

## Think Before Coding

Don't assume. Don't hide confusion. Surface tradeoffs.

- State assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them instead of picking silently.
- If a simpler approach exists, say so.
- If something is unclear, stop and name what is confusing.

## Simplicity First

Minimum change that solves the problem. Nothing speculative.

- No features beyond what was asked.
- No abstractions for single-use code.
- No flexibility or configurability that was not requested.
- No defensive logic for impossible scenarios.
- If the solution is larger than it needs to be, simplify it.

## Surgical Changes

Touch only what you must. Clean up only the mess your change creates.

- Don't improve adjacent content, comments, or formatting without a task reason.
- Don't refactor things that are not broken.
- Match existing repo style even if you would do it differently.
- If you notice unrelated dead code or issues, mention them instead of deleting them.
- Every changed line should trace directly to the request.

## Goal-Driven Execution

Define success criteria. Loop until verified.

- Turn vague requests into concrete, checkable outcomes.
- For multi-step tasks, state a brief plan and how each step will be verified.
- Prefer tests, diffs, searches, or direct checks over "should work" assumptions.

**Read [rules/CLAUDE.md](rules/CLAUDE.md) for the full rule set before any action.**

---

## Quick Reference

| Document | Content |
|----------|---------|
| [AGENTS.md](AGENTS.md) | Root quick-entry summary for all agents |
| [rules/AGENTS.md](rules/AGENTS.md) | Shared rules sections 1-11 |
| [rules/CLAUDE.md](rules/CLAUDE.md) | Claude Code full rules |
| [rules/01_note_structure.md](rules/01_note_structure.md) | Note format |
| [rules/02_navigation.md](rules/02_navigation.md) | Navigation rules |
| [rules/03_cross_linking.md](rules/03_cross_linking.md) | Cross-linking |
| [rules/04_security.md](rules/04_security.md) | Security hooks |
| [rules/09_ingest.md](rules/09_ingest.md) | Ingest pipeline |
| [rules/10_lint.md](rules/10_lint.md) | Wiki health check |
| [rules/11_ocr.md](rules/11_ocr.md) | OCR workflow |
| [log.md](log.md) | Chronological ingest/lint log |
| [glossary.md](glossary.md) | Abbreviations |
