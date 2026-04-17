---
tags:
  - tooling
created_at: 2026-04-17T00:00:00
updated_at: 2026-04-18T12:00:00
recent_editor: CLAUDE
---

# Agent Rules

Unified rules for all AI agents (Claude, Codex, Kiro) working in this repository.

## 1. Agent Permissions

| Permission | Scope |
|------------|-------|
| Read | All files |
| Write | All `.md` files |
| Web Search | Required before creating new notes |
| Git | Full access (commit, push, pull, gh) |

## 2. Core Principles

### 2.1. Think Before Editing

- State assumptions explicitly, never guess
- Present multiple interpretations when ambiguous
- Push back when simpler approaches exist
- Ask clarification before proceeding when confused

### 2.2. Simplicity First

- Deliver only requested features
- No speculative additions or abstractions
- No error handling for impossible scenarios
- Apply the senior engineer test: would this seem overcomplicated?

### 2.3. Surgical Changes

- Don't improve adjacent code, comments, or formatting
- Preserve existing style conventions
- Remove only code YOUR changes orphaned
- Every changed line traces to user request

### 2.4. Goal-Driven Execution

- Define verifiable success criteria
- Transform vague requests: "Fix bug" → "Reproduce via test, make it pass"
- Multi-step tasks need verification checkpoints

## 3. Note Structure

### 3.1. Required Sections

Every concept note must have these sections in order:

```md
# Title

## What It Is
(1-2 sentence definition - REQUIRED)

## Analogy
(Optional - only if it genuinely helps)

## How It Works
(Mechanics, steps, procedures)

## Example
(One concrete, small example - REQUIRED)

## Why It Matters
(Practical relevance - REQUIRED)
```

### 3.2. Heading Levels

| Level | Use |
|-------|-----|
| `#` | Note title only (one per file) |
| `##` | Major sections |
| `###` | Subsections |
| `####` | Never use - split the note instead |

### 3.3. Frontmatter

Every note begins with YAML frontmatter:

```yaml
---
tags:
  - aws
  - serverless
created_at: 2026-04-17T14:30:00
updated_at: 2026-04-17T15:45:00
recent_editor: CLAUDE
---
```

**AI must update `updated_at` and `recent_editor` on every edit.**

### 3.4. Lists and Emphasis

| Format | Use |
|--------|-----|
| `-` bullets | Unordered facts, properties |
| `1.` numbers | Ordered steps, study order |
| `**bold**` | Key terms, warnings |
| `*italic*` | Light emphasis |
| `` `code` `` | Commands, filenames, values |

### 3.5. What Not To Use

- No `---` horizontal rules except before navigation footer
- No `> Note:`, `> Warning:` - only `> **Tip:**`
- No raw HTML
- No emoji unless user requests it

## 4. Navigation

### 4.1. Concept Note Header

After frontmatter, before title:

```md
↑ [Overview](./00_overview.md)

# Title
```

### 4.2. Concept Note Footer

At end of file:

```md
---
← Previous: [Title](link) | [Overview](./00_overview.md) | Next: [Title](link) →
```

### 4.3. Overview Footer

Domain `00_overview.md` links up to parent:

```md
---
↑ [Parent Title](path/to/parent/00_overview.md)
```

### 4.4. README Files

READMEs are folder indexes only. No navigation footers. No study content.

### 4.5. When To Update Navigation

- Adding a note: update previous note's "Next" link
- Removing a note: repair broken links
- Renaming a note: update all references

## 5. Cross-Linking

### 5.1. Core Principles

- Explain a concept once in its canonical note
- Link from other notes instead of duplicating
- Link inline where concept is mentioned
- No separate "References" or "See Also" sections

### 5.2. First Mention Rule

On first mention of a concept with a dedicated note, add inline link. Do not repeat link on subsequent mentions in same file.

### 5.3. Abbreviation Format

First use: full name (abbreviation), then abbreviation only.

```md
Cloud Development Kit (CDK) lets you define infrastructure.
CDK supports Python and TypeScript.
```

## 6. Security

### 6.1. Delivery Rule

**"Success should be quiet, failure must be loud"**

- On success: silent completion, commit and push
- On failure: explicit error, stop and fix

### 6.2. Before Every Push

Scan for secrets:

| Pattern | Example |
|---------|---------|
| Private keys | `-----BEGIN.*PRIVATE KEY-----` |
| GitHub tokens | `ghp_`, `gho_` |
| AWS access keys | `AKIA...` |
| OpenAI keys | `sk-...` |

### 6.3. Files to Never Commit

- `.env` - Contains tokens
- `*.pem` - Private keys
- `credentials.json` - API credentials

## 7. Git Workflow

### 7.1. Environment Variables

Required in `.env`:

| Variable | Purpose |
|----------|---------|
| `GITHUB_TOKEN` | Authentication |
| `GITHUB_USERNAME` | Account name |
| `GIT_USER_NAME` | Commit author |
| `GIT_USER_EMAIL` | Commit email |

### 7.2. Push Commands

Standard push:
```bash
git push origin main
```

With content acknowledgment:
```bash
STUDY_PUSH_CONTENT_ACK=1 git push origin main
```

### 7.3. Commit Style

```
<type>: <description>
```

Types: `add`, `update`, `fix`, `refactor`, `docs`, `auto`

### 7.4. Hook Locations

| Location | Purpose |
|----------|---------|
| `.githooks/` | Shared entrypoints |
| `.claude/hooks/` | Claude-specific |
| `.codex/hooks/` | Codex-specific |

## 8. Structural Updates

When files are added, moved, renamed, or deleted:

- Update `00_overview.md` in affected domain
- Update `README.md` in affected folder
- Update navigation footers in affected notes

## 9. Conflict Resolution

- Check `recent_editor` before bulk updates
- Never overwrite another agent's recent changes
- Coordinate via commit messages

## 10. Platform Notes

### 10.1. Claude Code

- Automation hooks in `.claude/hooks/`
- Run git as individual calls, never chain `cd && git`
- See [CLAUDE.md](CLAUDE.md) for automation details

### 10.2. Codex

- Automation in `.codex/`
- Request persistent approval for bounded Git actions
- Run Git commands as simple, single-purpose commands

### 10.3. Kiro

- Automation will be in `.kiro/hooks/` when configured
