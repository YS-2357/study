---
tags:
  - tooling
created_at: 2026-04-17T14:18:47
updated_at: 2026-04-24T08:47:57
recent_editor: CODEX
---

# study

Study materials organized by domain. [Start here](home.md)

## Multi-PC Sync

This repo is designed to sync across machines. Notes, rules, hooks, and agent configs are tracked in Git so another clone can resume the same workspace state after adding local secrets.

These things stay local-only:

- `.env` - secrets and credentials
- `raw/` - source material for ingest; tracked conceptually through note `source:` slugs, not as Git content
- `.obsidian/workspace.json` - per-PC Obsidian layout and recent-file state

Agent-specific automation is separated on purpose: Codex-owned files live under `.codex/`, Claude-owned files live under `.claude/`, and shared Git entrypoints live under `.githooks/`.
When Codex works in this repo, `.claude/` is out of scope unless the user explicitly asks for Claude-specific changes.

- [rules/](rules/README.md) - Rules for agents and humans
- [raw/](raw/README.md) - Raw text inbox for source material that agents convert into structured notes
- [.claude/](.claude/README.md) - Claude Code hooks and local automation
- [.codex/](.codex/README.md) - Codex-specific repo automation and helper files
- [.githooks/](.githooks/README.md) - Local Git hooks that enforce repo checks before push
- [ai/](ai/README.md) - AI agent and LLM concepts. [Start studying](ai/00_ai_overview.md)
- [cloud/aws/](cloud/aws/README.md) - AWS service notes. [Start studying](cloud/aws/00_aws_overview.md)
- [computing/](computing/README.md) - General computing concepts. [Start studying](computing/00_computing_overview.md)
- [git/](git/README.md) - Git concepts. [Start studying](git/00_git_overview.md)
- [networking/](networking/README.md) - Networking fundamentals. [Start studying](networking/00_networking_overview.md)
- [software/](software/README.md) - Frontend, backend, database concepts. [Start studying](software/00_software_overview.md)
- [tooling/](tooling/README.md) - Developer tools and workflow notes. [Start studying](tooling/00_tooling_overview.md)

## Standards

Every note in this repo follows these rules.

### Structure

Every concept note uses this heading order:

```md
# Title
## What It Is
## Analogy
## How It Works
## Example
## Why It Matters
```

### Navigation

Navigation is associative. Every concept note uses an overview link plus footer `Related` links and tags instead of a prev/next sequence.

### Markdown Formatting

| Element | Syntax | When to use |
|---------|--------|-------------|
| Note title | `#` | One per file |
| Major section | `##` | `What It Is`, `How It Works`, and other major sections |
| Subsection | `###` | Breakdown within a section |
| Deeper | `####`+ | Never; split the note instead |
| Bullet list | `- item` | Unordered facts, properties, options |
| Numbered list | `1. item` | Ordered steps or priority |
| Bold | `**text**` | Key terms and warnings |
| Italic | `*text*` | Light emphasis, titles of external works |
| Inline code | `` `text` `` | Commands, filenames, env vars, values |
| Table | `| col |` | Comparisons, options, structured data |
| Callout | `> **Tip:**` | Practical guidance |
| Divider | `---` | Before the navigation footer only |
| Inline tag | `#tag` | Footer `Tags:` line |

### Content Rules

- Explain a concept once in the note where it belongs; other notes should link to it.
- Link inline where a concept is mentioned.
- Keep notes concise and prefer realistic examples.
- Use `> **Tip:**` for practical guidance.
- Do not use `---` except before the navigation footer.
- Do not add history sections.

### README Rules

- READMEs list files and directories in the folder.
- READMEs link to the domain's `00_{domain}_overview.md`.
- READMEs do not contain study content, study order, or cross-references.

## Push Checks

- Working rule for agents: make one logical task per commit. Push when the user asks for remote delivery or when the task explicitly includes it.
- `git push` requires acknowledgment when study-content Markdown files changed.
- The acknowledgment check ignores `.claude/`, `.codex/`, `.githooks/`, `.kiro/`, `.env`, `AGENTS.md`, and `CLAUDE.md`.
- For non-interactive pushes, first review the changed study files and then set `STUDY_PUSH_CONTENT_ACK=1` for that push.
