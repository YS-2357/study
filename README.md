---
tags:
  - tooling
created_at: 2026-04-17T14:18:47
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
---

# study

Study materials organized by domain. [Start here →](home.md)

## Multi-PC Sync

This repo is designed to sync seamlessly across machines. **Notes, rules, hooks, agent configs, and Obsidian layout (`.obsidian/workspace.json`) are tracked and pushed.** Clone on another PC, drop in an `.env`, and continue exactly where you left off: same notes, same pane layout, same automation.

Two things stay local-only:

- `.env` — secrets (tokens, credentials).
- `raw/` — source material for ingest (articles, PDFs, transcripts). Sources are often too heavy to sync and may be personal; they're tracked conceptually via the `source:` frontmatter field on the notes they produced, not as files. See [rules/09_ingest.md](rules/09_ingest.md).

Agent-specific automation and skills are separated on purpose: Codex-owned files belong under `.codex/`, Claude-owned files belong under `.claude/`, and shared Git entrypoints belong under `.githooks/`.
When Codex works in this repo, `.claude/` is out of scope unless the user explicitly asks for Claude-specific changes.

- [rules/](rules/README.md) — Rules for agents and humans.
- [raw/](raw/README.md) — Raw text inbox for source material that agents convert into structured notes.
- [.claude/](.claude/README.md) — Claude Code hooks: auto-push after every write/edit, session-end push, hook scripts.
- [.codex/](.codex/README.md) — Codex-specific repo automation and helper files.
- [.githooks/](.githooks/README.md) — Local Git hooks that enforce repo checks before push.
- [ai/](ai/README.md) — AI agent and LLM concepts. [Start studying →](ai/00_ai_overview.md)
- [aws/](aws/README.md) — AWS service notes. [Start studying →](aws/00_aws_overview.md)
- [computing/](computing/README.md) — General computing concepts. [Start studying →](computing/00_computing_overview.md)
- [git/](git/README.md) — Git concepts. [Start studying →](git/00_git_overview.md)
- [networking/](networking/README.md) — Networking fundamentals. [Start studying →](networking/00_networking_overview.md)
- [tooling/](tooling/README.md) — Developer tools and workflow notes. [Start studying →](tooling/00_tooling_overview.md)

## Standards

Every note in this repo follows these rules.

### Structure

Every note file uses this heading order:

```
# Title
## What It Is       ← 1-2 sentence definition (required)
## Analogy          ← only if it genuinely helps (optional)
## How It Works     ← mechanics, steps, diagrams (if applicable)
## Example          ← one concrete, small example (required)
## Why It Matters   ← practical relevance (required)
```

### Navigation

Navigation is associative. Every concept note has a footer like:

```
---
↑ [Overview](./00_{domain}_overview.md)

**Related:** [Title A](./a.md), [Title B](../other/b.md)
**Tags:** #tag1 #tag2
```

Every domain has a `00_{domain}_overview.md` hub that groups notes by theme. The root-level `home.md` links to every domain's overview. Readers jump by concept via inline links, the footer `Related` list, shared tags, and Obsidian's graph view — not a prev/next sequence.

### Markdown formatting

| Element | Syntax | When to use |
|---------|--------|-------------|
| Note title | `#` | One per file — the file title only |
| Extra section | `##` | Allowed between required sections when content genuinely warrants it |
| Major section | `##` | `What It Is`, `How It Works`, etc. |
| Subsection | `###` | Breakdown within a section |
| Deeper | `####`+ | Never — split the note instead |
| Bullet list | `- item` | Unordered facts, properties, options |
| Numbered list | `1. item` | Ordered steps, study order, priority |
| Bold | `**text**` | Key terms, important warnings |
| Italic | `*text*` | Light emphasis, titles of external works |
| Inline code | `` `text` `` | Commands, filenames, env vars, values |
| Table | `\| col \|` | Comparisons, option sets, structured data |
| Callout | `> **Tip:**` | Practical guidance — the only callout format |
| Divider | `---` | Before the navigation footer only |
| Inline tag | `#tag` | Footer `Tags:` line — mirrors frontmatter `tags` |

### Content rules

- Explain a concept once, in the note where it belongs. Other notes link to it instead of re-explaining.
- Link inline where a concept is mentioned, not in a separate cross-references section.
- Keep notes concise. Prefer small, realistic examples over abstract placeholders.
- Use `> **Tip:**` for practical guidance. No other tip/recommendation formats.
- No `---` horizontal rules except before the navigation footer.
- No history sections (creation dates, inventor names).

### README rules

- READMEs list files and directories in the folder. One-line description per entry.
- READMEs link to the domain's `00_{domain}_overview.md` for study content.
- READMEs do not contain study content, study order, or cross-references.

## Push Checks

- Working rule for agents: one file change, one git push. Any file write should be followed by the full delivery loop in the same turn when feasible.
- `git push` requires acknowledgment when study-content Markdown files changed.
- The acknowledgment check ignores `.claude/`, `.codex/`, `.githooks/`, `.kiro/`, `.env`, `AGENTS.md`, and `CLAUDE.md`.
- For non-interactive pushes, first review the changed study files and then set `STUDY_PUSH_CONTENT_ACK=1` for that push.
