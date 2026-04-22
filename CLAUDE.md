# Claude Code — Study Repository

**Read [rules/CLAUDE.md](rules/CLAUDE.md) for the full rule set before any action.**

---

## Quick Reference

| Document | Content |
|----------|---------|
| [rules/AGENTS.md](rules/AGENTS.md) | Shared rules §1–§11 |
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

---

## Session Start

Always `git pull` before any read or write operation:

```bash
git -C "C:\Users\user\study" pull origin main
```

## Automation Hooks

| Hook | Trigger | Action |
|------|---------|--------|
| `PostToolUse` on `Write\|Edit` | File write/edit | Stage, commit, push |
| `Stop` | Session end | Final push (async) |

Hook scripts in `.claude/hooks/`.

## Git Commands

Run git as individual calls (never chain `cd && git`):

```bash
git -C "C:\Users\user\study" add file.md
git -C "C:\Users\user\study" commit -m "message"
git -C "C:\Users\user\study" push origin main
```

## Subtree Overrides

- `cloud/aws/AGENTS.md` — AWS-specific viewpoint framework
