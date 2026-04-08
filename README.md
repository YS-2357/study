# study

Study materials organized by domain.

Agent-specific automation and skills are separated on purpose: keep Codex-owned files under `.codex/`, Claude-owned files under `.claude/`, and shared Git entrypoints under `.githooks/`.

- [.claude/](.claude/README.md) — Claude-specific repo automation and helper files.
- [.codex/](.codex/README.md) — Codex-specific repo automation and helper files.
- [.githooks/](.githooks/README.md) — Local Git hooks that enforce repo checks before push.
- [ai/](ai/README.md) — AI agent and LLM concepts. [Start studying →](ai/00_overview.md)
- [aws/](aws/README.md) — AWS study materials grouped by level.
  - [aws/101/aws_services/](aws/101/aws_services/README.md) — AWS service notes. [Start studying →](aws/101/aws_services/00_overview.md)
  - [aws/201/aws_services/](aws/201/aws_services/README.md) — AWS 201 deep-dives. [Start studying →](aws/201/aws_services/00_overview.md)
- [computing/](computing/README.md) — General computing concepts. [Start studying →](computing/00_overview.md)
- [git/](git/README.md) — Git concepts. [Start studying →](git/00_overview.md)
- [networking/](networking/README.md) — Networking fundamentals. [Start studying →](networking/00_overview.md)

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
