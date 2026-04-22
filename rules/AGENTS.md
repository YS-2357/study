---
tags:
  - tooling
created_at: 2026-04-17T00:00:00
updated_at: 2026-04-22T09:57:48
recent_editor: CLAUDE
---

# Agent Rules

Unified rules for all AI agents (Claude, Codex, Kiro) working in this repository.

## Agent Files

| File | Agent | Purpose |
|------|-------|---------|
| [CLAUDE.md](CLAUDE.md) | Claude Code | Platform-specific notes |
| [CODEX.md](CODEX.md) | OpenAI Codex | Platform-specific notes |
| [KIRO.md](KIRO.md) | AWS Kiro | Platform-specific notes |

**All agents follow the rules in this file.**

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

Raw source material lives in `raw/` (gitignored). Ingest runs **only on user request** via `/ingest <source>` or a conversational equivalent. Full pipeline in [09_ingest.md](09_ingest.md).

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

On first use of a skill with no local implementation, read `rules/skills/<skill>.md` and create your platform-native version.

## Rule Documents

| File | Content |
|------|---------|
| [01_note_structure.md](01_note_structure.md) | Note format, headings, frontmatter |
| [02_navigation.md](02_navigation.md) | Navigation header and footer |
| [03_cross_linking.md](03_cross_linking.md) | Cross-linking and terminology |
| [04_security.md](04_security.md) | Security hooks and delivery |
| [05_git_guide.md](05_git_guide.md) | Git workflow and push commands |
| [06_content_diagrams.md](06_content_diagrams.md) | ASCII diagrams of architecture, hierarchy, flows |
| [07_scalability.md](07_scalability.md) | Split thresholds, sed-friendly renames, subdomain rules |
| [09_ingest.md](09_ingest.md) | Ingest pipeline |
| [10_lint.md](10_lint.md) | Wiki health check |
| [11_ocr.md](11_ocr.md) | OCR workflow |
| [../log.md](../log.md) | Append-only chronological log |
| [../glossary.md](../glossary.md) | Abbreviations and terms |
