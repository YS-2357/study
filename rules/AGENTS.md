---
tags:
  - tooling
created_at: 2026-04-17T00:00:00
updated_at: 2026-04-18T12:05:28
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

### 3.2. Simplicity First

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

## 9. Raw Text Processing

When processing files from `raw/`:

- Read text files only unless the user explicitly asks for binary extraction.
- Extract clear standalone study concepts; skip weak fragments and duplicates.
- Search existing notes first and update the canonical note when one fits.
- Web search before creating new notes and cite reliable official or primary sources inline.
- Place notes in the best existing domain, or create a new domain only when no existing domain fits.
- Move handled raw files into `raw/processed/` after useful content has been converted.

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
recent_editor: CLAUDE
---
```

**AI must update `updated_at` and `recent_editor` on every edit.**

## 12. Rule Documents

| File | Content |
|------|---------|
| [01_note_structure.md](01_note_structure.md) | Note format, headings, frontmatter |
| [02_navigation.md](02_navigation.md) | Navigation header and footer |
| [03_cross_linking.md](03_cross_linking.md) | Cross-linking and terminology |
| [04_security.md](04_security.md) | Security hooks and delivery |
| [05_git_guide.md](05_git_guide.md) | Git workflow and push commands |
| [06_content_diagrams.md](06_content_diagrams.md) | ASCII diagrams of architecture, hierarchy, flows |
| [glossary.md](../glossary.md) | Abbreviations and terms |
