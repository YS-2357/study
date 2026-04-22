# Agent Rules — Study Repository

Unified rules for all AI agents (Claude, Codex, Kiro) working in this repository.

## Quick Reference

| Document | Content |
|----------|---------|
| [rules/AGENTS.md](rules/AGENTS.md) | Detailed agent rules |
| [rules/CLAUDE.md](rules/CLAUDE.md) | Claude Code rules |
| [rules/CODEX.md](rules/CODEX.md) | Codex rules |
| [rules/KIRO.md](rules/KIRO.md) | Kiro rules |
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

## 1. Permissions

- **Read**: All files in repo
- **Write**: All `.md` files
- **Web Search**: Required before creating new notes
- **Git/GH**: Full access (commit, push, pull, gh)

## 2. Core Principles

### 2.1 Think Before Editing
- State assumptions explicitly, never guess
- Present multiple interpretations when ambiguous
- Push back when simpler approaches exist
- Ask clarification before proceeding when confused

### 2.2 Same Topic, Different Domain Focus
A concept can have notes in multiple domains — this is intentional. Each note focuses on the angle relevant to its domain. No deduplication, merging, or "see only" redirects required.

### 2.3 Simplicity First
- Deliver only requested features
- No speculative additions or abstractions
- No single-use abstractions
- No error handling for impossible scenarios

### 2.4 Surgical Changes
- Don't improve adjacent code, comments, or formatting
- Don't refactor functioning code
- Preserve existing style conventions
- Remove only code YOUR changes orphaned
- Every changed line traces to user request

### 2.5 Goal-Driven Execution
- Define verifiable success criteria
- Transform vague requests: "Fix bug" → "Reproduce via test, make it pass"
- Multi-step tasks need verification checkpoints

## 3. Delivery Rule

**"Success should be quiet, failure must be loud"**

- On success: silent completion, commit and push without fanfare
- On failure: explicit error message with context, stop and fix before proceeding

## 4. Research Before Writing

- Web search required before creating new notes
- Cite official sources inline
- No placeholder or speculative content
- Verify facts before committing

## 5. Session Start

**Always `git pull` before any read or write operation.**

```bash
git pull origin main
```

## 6. Atomic Commits

- One logical change per commit
- Descriptive commit messages
- Push after each file change
- Never batch unrelated changes

## 7. Link Maintenance

- Check for broken links after renaming/moving
- Update all references when paths change
- Glossary links for abbreviations on first use
- Cross-domain links encouraged when helpful

## 8. Structural Document Updates

Whenever files are added, moved, renamed, or deleted, update:
- `home.md` — root study hub
- `00_{domain}_overview.md` — domain study hub
- `README.md` — folder index
- `rules/02_navigation.md` — if domain structure changes

## 9. Ingesting Raw Sources

Raw source material lives in `raw/` (gitignored). Ingest runs **only on user request** via `/ingest <source>` or a conversational equivalent. Full pipeline in [rules/09_ingest.md](rules/09_ingest.md).

## 10. Conflict Resolution

- Check `recent_editor` before bulk updates
- Never overwrite another agent's recent changes
- Coordinate via commit messages
- When in doubt, ask

## 11. Frontmatter Requirements

Every `.md` file must have:

```yaml
---
tags:
  - domain-tag
created_at: YYYY-MM-DDTHH:MM:SS
updated_at: YYYY-MM-DDTHH:MM:SS
recent_editor: <AGENT>
---
```

**Update `updated_at` and `recent_editor` to your agent name on every edit, no exceptions.**

## 12. Skills

Canonical skill definitions in `rules/skills/`. Each agent implements them in their own platform directory.

| Skill | Description |
|-------|-------------|
| ingest | Ingest a raw source file into the wiki |
| lint | Run the wiki health check |
| nav-update | Sync structural documents after file changes |
| ocr | Extract text from raw local images |
| split | Split an oversized or mixed-theme note |

Each agent implements these in their own native format — do not copy another agent's files:
- **Claude** → `.claude/commands/`
- **Kiro** → `.kiro/skills/`
- **Codex** → `.codex/skills/`

## 13. Rule Sync

Sections §1–§11 must be **identical** across all agent files:

- `AGENTS.md` (root)
- `CLAUDE.md` (root)
- `rules/AGENTS.md`
- `rules/CLAUDE.md`
- `rules/CODEX.md`
- `rules/KIRO.md`

**When any shared rule changes, update all six files.** §12+ are agent-specific and may differ (git commands, skill directories, platform hooks).

## Subtree Overrides

- `cloud/aws/AGENTS.md` — AWS-specific viewpoint framework
