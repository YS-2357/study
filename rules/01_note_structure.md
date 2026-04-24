---
tags:
  - tooling
created_at: 2026-04-17T00:00:00
updated_at: 2026-04-24T08:47:57
recent_editor: CODEX
---

# Note Structure

Rules for formatting study notes in this repository.

## 1. Required Sections

Every concept note has these sections in order:

```md
# Title

## What It Is

## Analogy

## How It Works

## Example

## Why It Matters
```

### 1.1. Section Rules

- `What It Is` - required, 1-2 sentence definition
- `Analogy` - required, 1-3 sentences; if no clean analogy fits, say so briefly
- `How It Works` - required; describe mechanics, steps, or procedures
- `Example` - required, concrete and small
- `Why It Matters` - required

### 1.2. Additional Sections

Extra `##` sections are allowed when content warrants them, such as:
- `## Name`
- `## Prerequisites`

## 2. Heading Levels

| Level | Use |
|-------|-----|
| `#` | Note title only |
| `##` | Major sections |
| `###` | Subsections inside a major section |
| `####` | Never use; split the note instead |

## 3. Frontmatter

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

### 3.1. Frontmatter Fields

| Field | Format | Rule |
|-------|--------|------|
| `tags` | lowercase, hyphen-separated | Required, minimum 1 tag |
| `created_at` | `YYYY-MM-DDTHH:MM:SS` | Set once on creation |
| `updated_at` | `YYYY-MM-DDTHH:MM:SS` | Update on every edit |
| `recent_editor` | `CLAUDE`, `CODEX`, `KIRO`, `HUMAN` | Update on every edit |
| `source` | list of slugs | Optional |

**KST enforcement:** All timestamps use Korean time (UTC+9 / Asia-Seoul). Use the machine's real local Seoul timestamp when setting `created_at` or `updated_at`; do not invent `T00:00:00` placeholders.

**Source tracking:** When a note absorbs content from a raw source, append a short filename-safe slug to the `source:` list. The slug is the authoritative pointer even if the raw file itself is only present on one machine.

### 3.2. Tags

- Use lowercase, hyphen-separated tags from the repo taxonomy
- Assign all applicable tags
- Add a new tag only when no existing tag fits

## 4. Lists

| Type | Use |
|------|-----|
| `-` bullets | Unordered facts, properties, options |
| `1.` numbers | Ordered steps or priority |

Indent nested items with 2 spaces.

## 5. Emphasis

| Format | Use |
|--------|-----|
| `**bold**` | Key terms, important warnings |
| `*italic*` | Light emphasis, external work titles |
| `` `code` `` | Commands, filenames, env vars, values |

## 6. Tables

- Use tables for comparisons, option sets, and structured data
- Every table needs a header row and separator row

## 7. What Not To Use

- No `---` horizontal rules except before the navigation footer
- No `> Note:` or `> Warning:`; use only `> **Tip:**`
- No raw HTML
- No emoji unless the user requests it
