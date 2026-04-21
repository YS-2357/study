---
tags:
  - tooling
created_at: 2026-04-17T00:00:00
updated_at: 2026-04-21T00:00:00
recent_editor: CODEX
---

# Agent Rules

Unified rules for all AI agents (Claude, Codex, Kiro) working in this repository.

## 1. Agent Identification

| File | Agent | Purpose |
|------|-------|---------|
| [CLAUDE.md](CLAUDE.md) | Claude Code | Platform-specific notes |
| [CODEX.md](CODEX.md) | OpenAI Codex | Platform-specific notes |
| [KIRO.md](KIRO.md) | AWS Kiro | Platform-specific notes |

**All agents follow the rules in this file.**

## 2. Permissions

All AI agents have these permissions:

- **Read**: All files in repo
- **Write**: All `.md` files
- **Web Search**: Required before creating new notes
- **Git/GH**: Full access (commit, push, pull, gh)

## 3. Core Principles

### 3.1. Think Before Editing

- State assumptions explicitly, never guess
- Present multiple interpretations when ambiguous
- Push back when simpler approaches exist
- Ask clarification before proceeding when confused

### 3.2. Same Topic, Different Domain Focus

A concept can have notes in multiple domains — this is intentional. Each note focuses on the angle relevant to its domain. Example: Kiro in `cloud/aws/` covers infrastructure setup; `ai/kiro/` covers it as a coding tool. No deduplication, merging, or "see only" redirects required. When deciding where to put a note, choose the focus angle that fits the domain.

### 3.3. Simplicity First

- Deliver only requested features
- No speculative additions or abstractions
- No single-use abstractions
- No error handling for impossible scenarios
- Apply the senior engineer test: would this seem overcomplicated?

### 3.3. Surgical Changes

- Don't improve adjacent code, comments, or formatting
- Don't refactor functioning code
- Preserve existing style conventions
- Remove only code YOUR changes orphaned
- Every changed line traces to user request

### 3.4. Goal-Driven Execution

- Define verifiable success criteria
- Transform vague requests: "Fix bug" → "Reproduce via test, make it pass"
- Multi-step tasks need verification checkpoints
- Autonomous looping requires strong success criteria

## 4. Delivery Rule

**"Success should be quiet, failure must be loud"**

On success:
- No output, silent completion
- Commit and push without fanfare

On failure:
- Explicit error message with context
- Log to system message
- Stop and fix before proceeding

## 5. Research Before Writing

- Web search required before creating new notes
- Cite official sources inline
- No placeholder or speculative content
- Verify facts before committing

## 6. Session Start

**Always `git pull` before any read or write operation.**

This repo is synced across multiple PCs. Stale local state causes merge conflicts.

```bash
git pull origin main
```

## 7. Atomic Commits

- One logical change per commit
- Descriptive commit messages
- Push after each file change
- Never batch unrelated changes

## 8. Link Maintenance

- Check for broken links after renaming/moving
- Update all references when paths change
- Glossary links for abbreviations on first use
- Cross-domain links encouraged when helpful

## 9. Structural Document Updates

Whenever files are added, moved, renamed, or deleted:

- Update `00_{domain}_overview.md` in the affected domain (or `home.md` at root)
- Update `README.md` in the affected folder
- Update `rules/02_navigation.md` if domain structure changes
- Update navigation footers in affected notes

Structural documents that must reflect current file structure:
- `home.md` - Root study hub
- `00_{domain}_overview.md` - Study hub for each domain
- `README.md` - Folder index for each directory
- `rules/02_navigation.md` - Domain layout table

## 10. Ingesting Raw Sources

Raw source material lives in `raw/` (gitignored — local-only). Ingest runs **only on user request** via `/ingest <source>` or a conversational equivalent.

Full pipeline — trigger, input types, update-vs-create, `source:` frontmatter, movement to `raw/processed/`, `log.md` append — is defined in [09_ingest.md](09_ingest.md).

## 11. Conflict Resolution

- Check `recent_editor` before bulk updates
- Never overwrite another agent's recent changes
- Coordinate via commit messages
- When in doubt, ask

## 12. Frontmatter Requirements

Every `.md` file must have:

```yaml
---
tags:
  - domain-tag
created_at: YYYY-MM-DDTHH:MM:SS
updated_at: YYYY-MM-DDTHH:MM:SS
recent_editor: CLAUDE
---
```

**AI must update `updated_at` and `recent_editor` on every edit.**

## 13. Rule Documents

| File | Content |
|------|---------|
| [01_note_structure.md](01_note_structure.md) | Note format, headings, frontmatter |
| [02_navigation.md](02_navigation.md) | Navigation header and footer |
| [03_cross_linking.md](03_cross_linking.md) | Cross-linking and terminology |
| [04_security.md](04_security.md) | Security hooks and delivery |
| [05_git_guide.md](05_git_guide.md) | Git workflow and push commands |
| [06_content_diagrams.md](06_content_diagrams.md) | ASCII diagrams of architecture, hierarchy, flows |
| [07_scalability.md](07_scalability.md) | Split thresholds, sed-friendly renames, subdomain rules |
| [09_ingest.md](09_ingest.md) | Ingest pipeline: triggers, inputs, update-vs-create, source tracking |
| [10_lint.md](10_lint.md) | Wiki health check: broken links, orphans, missing cross-refs, stale claims |
| [11_ocr.md](11_ocr.md) | Image text extraction workflow for raw local images |
| [../log.md](../log.md) | Append-only chronological log of ingests/queries/lints |
| [../glossary.md](../glossary.md) | Abbreviations and terms |

## 14. Skills

Canonical skill definitions live in `rules/skills/`. Each agent implements these in their platform's native skill directory:

| Skill | Description |
|-------|-------------|
| [ingest](skills/ingest.md) | Ingest a raw source file into the wiki |
| [lint](skills/lint.md) | Run the wiki health check |
| [nav-update](skills/nav-update.md) | Sync structural documents after file changes |
| [ocr](skills/ocr.md) | Manually extract readable text from raw local images into raw Markdown drafts |
| [split](skills/split.md) | Split an oversized or mixed-theme note |

Each agent implements these in their own native format — do not copy another agent's files:

- **Claude** → `.claude/commands/`
- **Kiro** → `.kiro/skills/`
- **Codex** → platform's native skill/command directory

On first use of a skill that has no local implementation, read `rules/skills/<skill>.md` and create your own platform-native version.
