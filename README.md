# study

Study materials organized by domain.

Agent-specific automation and skills are separated on purpose: Codex-owned files belong under `.codex/`, Claude-owned files belong under `.claude/`, and shared Git entrypoints belong under `.githooks/`.
When Codex works in this repo, `.claude/` is out of scope unless the user explicitly asks for Claude-specific changes.

- [.claude/](.claude/README.md) — Claude Code hooks: auto-push after every write/edit, session-end push, hook scripts.
- [.codex/](.codex/README.md) — Codex-specific repo automation and helper files.
- [.githooks/](.githooks/README.md) — Local Git hooks that enforce repo checks before push.
- [ai/](ai/README.md) — AI agent and LLM concepts. [Start studying →](ai/00_overview.md)
- [aws/](aws/README.md) — AWS study materials grouped by level.
  - [aws/101/aws_services/](aws/101/aws_services/README.md) — AWS service notes. [Start studying →](aws/101/aws_services/00_overview.md)
  - [aws/201/aws_services/](aws/201/aws_services/README.md) — AWS 201 deep-dives. [Start studying →](aws/201/aws_services/00_overview.md)
- [computing/](computing/README.md) — General computing concepts. [Start studying →](computing/00_overview.md)
- [git/](git/README.md) — Git concepts. [Start studying →](git/00_overview.md)
- [networking/](networking/README.md) — Networking fundamentals. [Start studying →](networking/00_overview.md)
- [tooling/](tooling/README.md) — Developer tools and workflow notes. [Start studying →](tooling/00_overview.md)

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

Every note has a footer:

```
---
← Previous: [Title](link) | [Overview](00_overview.md) | Next: [Title](link) →
```

Every domain has a `00_overview.md` that serves as the study hub with links to all notes in study order.

### Content rules

- Explain a concept once, in the note where it belongs. Other notes link to it instead of re-explaining.
- Link inline where a concept is mentioned, not in a separate cross-references section.
- Keep notes concise. Prefer small, realistic examples over abstract placeholders.
- Use `> **Tip:**` for practical guidance. No other tip/recommendation formats.
- No `---` horizontal rules except before the navigation footer.
- No history sections (creation dates, inventor names).

### README rules

- READMEs list files and directories in the folder. One-line description per entry.
- READMEs link to the domain's `00_overview.md` for study content.
- READMEs do not contain study content, study order, or cross-references.

## Push Checks

- Working rule for agents: one file change, one git push. Any file write should be followed by the full delivery loop in the same turn when feasible.
- `git push` requires acknowledgment when study-content Markdown files changed.
- The acknowledgment check ignores `.claude/`, `.codex/`, `.githooks/`, `.kiro/`, `.env`, `AGENTS.md`, and `CLAUDE.md`.
- For non-interactive pushes, first review the changed study files and then set `STUDY_PUSH_CONTENT_ACK=1` for that push.
