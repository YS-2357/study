---
tags:
  - tooling
created_at: 2026-04-17T00:00:00
updated_at: 2026-04-23T14:21:23
recent_editor: CLAUDE
---

# Codex

I am **Codex**, OpenAI's agent.

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

### 4.1 Citation Quality Standards

When citing research papers or academic claims, use sources that meet at least one condition below.

**Tier 1 — Top venue (no citation count required)**
Published at: NeurIPS, ICML, ICLR, ACL, EMNLP, CVPR, JMLR, Nature, Science

**Tier 2 — arXiv preprint**
Accepted if 50+ citations **or** authored at a major lab (Google, Meta, Anthropic, OpenAI, DeepMind, NVIDIA, Microsoft Research, MIT, Stanford, CMU, Oxford, Cambridge)

**Exception — papers < 1 year old**
Citation count waived; Tier 1 venue or major lab affiliation still required

**Always**
- Link the original paper (arXiv URL or DOI) — not a blog post or summary site
- Do not use Medium articles, YouTube, or unofficial summaries as primary citations

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
recent_editor: CODEX
---
```

**Update `updated_at` and `recent_editor: CODEX` on every edit, no exceptions.**

## 12. Skills

Canonical skill definitions in `rules/skills/`. Codex implements them in `.codex/skills/`.

| Skill | Description |
|-------|-------------|
| ingest | Ingest a raw source file into the wiki |
| lint | Run the wiki health check |
| nav-update | Sync structural documents after file changes |
| ocr | Extract text from raw local images |
| split | Split an oversized or mixed-theme note |

On first use of a skill, read `rules/skills/<skill>.md` and create a Codex-native implementation. Do not copy `.claude/commands/` files.

## 13. Rule Sync

Sections §1–§11 must be **identical** across all four rules/ files:

- `rules/AGENTS.md`
- `rules/CLAUDE.md`
- `rules/CODEX.md`
- `rules/KIRO.md`

Root-level `AGENTS.md` and `CLAUDE.md` are pointer files — they route agents to the rules/ files and must not duplicate §1–§11.

**When any shared rule changes, update all four rules/ files.** §12+ are agent-specific and may differ (git commands, skill directories, platform hooks).

## 14. Automation Location

- Codex keeps repo-local automation in `.codex/`
- Shared Git hook entrypoints in `.githooks/`

## 15. Permission Style

Request persistent approval only for bounded Git actions:

- `git add <specific paths>`
- `git commit -m "<message>"`
- `git push origin main`

Run Git commands as simple, single-purpose commands. Avoid wrappers.

## 16. Write Commands

Run Git write commands with escalated permissions:
- `git add`, `git commit`, `git push`, `git pull`

Windows may fail on `.git/index.lock` if sandbox tried first.

## 17. OCR

For raw image text extraction, use [11_ocr.md](11_ocr.md) and the Codex skill in `.codex/skills/ocr/`. Prefer direct visual reading in small batches, and keep extraction outputs under `raw/`.
