---
tags:
  - tooling
created_at: 2026-04-17T00:00:00
updated_at: 2026-04-24T08:47:57
recent_editor: CODEX
---

# Agent Rules

Unified rules for all AI agents (Claude, Codex, Kiro) working in this repository.

## Agent Files

| File | Agent | Purpose |
|------|-------|---------|
| [CLAUDE.md](CLAUDE.md) | Claude Code | Platform-specific notes |
| [CODEX.md](CODEX.md) | OpenAI Codex | Platform-specific notes |
| [KIRO.md](KIRO.md) | AWS Kiro | Platform-specific notes |

All agents follow the shared rules in this file.

## 1. Permissions

- **Read**: All files in repo
- **Write**: All `.md` files
- **Web Search**: Required before creating new notes
- **Git/GH**: Full access (commit, push, pull, gh)

## 2. Core Principles

### 2.1 Think Before Editing
- State assumptions explicitly and do not guess
- Present multiple interpretations when ambiguity matters
- Push back when a simpler approach is better
- Ask for clarification when ambiguity cannot be resolved from the repo or system

### 2.2 Same Topic, Different Domain Focus
A concept can have notes in multiple domains. Each note should focus on the angle relevant to its domain. Do not deduplicate or convert those into redirects.

### 2.3 Simplicity First
- Deliver only the requested change
- No speculative additions or abstractions
- No single-use abstractions
- No defensive logic for impossible scenarios

### 2.4 Surgical Changes
- Do not improve adjacent content without a reason tied to the request
- Do not refactor functioning content without need
- Preserve existing style conventions
- Remove only content your change makes obsolete
- Every changed line should trace back to the task

### 2.5 Goal-Driven Execution
- Define verifiable success criteria
- Turn vague requests into concrete checks when possible
- Use verification checkpoints for multi-step tasks

## 3. Delivery Rule

**"Success should be explicit, failure must be loud"**

- On success: give a short explicit summary of what changed and what was verified
- On failure: give an explicit error message with context, then stop and fix before proceeding

## 4. Research Before Writing

- Web search is required before creating new notes
- Cite official sources inline
- No placeholder or speculative content
- Verify facts before committing

### 4.1. Citation Quality Standards

When citing research papers or academic claims, use sources that meet at least one condition below.

**Tier 1 - Top venue (no citation count required)**
Published at: NeurIPS, ICML, ICLR, ACL, EMNLP, CVPR, JMLR, Nature, Science

**Tier 2 - arXiv preprint**
Accepted if 50+ citations or authored at a major lab (Google, Meta, Anthropic, OpenAI, DeepMind, NVIDIA, Microsoft Research, MIT, Stanford, CMU, Oxford, Cambridge)

**Exception - papers under 1 year old**
Citation count waived; Tier 1 venue or major-lab affiliation still required

Always link the original paper (arXiv URL or DOI), not an unofficial summary.

## 5. Session Start

**Sync before mutation when the task needs current remote state.**

```bash
git pull --ff-only origin main
```

Reading and local inspection do not require a pull first. Pull before editing when the branch may be stale, before commit/push work, or when the task depends on the latest remote content.

## 6. Atomic Commits

- One logical change per commit or commit set
- Descriptive commit messages
- Push when the user requests remote delivery or when the task explicitly includes it
- Never batch unrelated changes into one commit

## 7. Link Maintenance

- Check for broken links after renaming or moving
- Update all references when paths change
- Link glossary items on first use when needed
- Cross-domain links are encouraged when helpful

## 8. Structural Document Updates

Whenever files are added, moved, renamed, or deleted, update:
- `home.md`
- `00_{domain}_overview.md`
- `README.md`
- `rules/02_navigation.md` if domain structure changes

## 9. Ingesting Raw Sources

Raw source material lives in `raw/` and is gitignored. Ingest runs only on user request via `/ingest <source>` or a conversational equivalent. Full flow: [09_ingest.md](09_ingest.md).

## 10. Conflict Resolution

- Check `recent_editor` before bulk updates
- Do not overwrite another agent's recent changes casually
- Coordinate through commit messages or explicit notes
- Ask when conflict risk is unclear

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

- All timestamps use Korean time (UTC+9 / Asia-Seoul)
- `created_at` is set once on creation
- `updated_at` must be refreshed on every edit
- `recent_editor` must be set to the editing agent

## 12. Skills

Canonical skill definitions live in `rules/skills/`. Each agent implements them in its own platform directory.

| Skill | Description |
|-------|-------------|
| ingest | Ingest a raw source file into the wiki |
| lint | Run the wiki health check |
| nav-update | Sync structural documents after file changes |
| ocr | Extract text from raw local images |
| split | Split an oversized or mixed-theme note |

Each agent implements these in its own native format:
- **Claude** -> `.claude/commands/`
- **Kiro** -> `.kiro/skills/`
- **Codex** -> `.codex/skills/`

## 13. Rule Sync

Sections 1-11 must stay identical across:
- `rules/AGENTS.md`
- `rules/CLAUDE.md`
- `rules/CODEX.md`
- `rules/KIRO.md`

Root-level `AGENTS.md` and `CLAUDE.md` are pointer files and should not duplicate the shared sections.

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
