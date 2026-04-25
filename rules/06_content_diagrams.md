---
tags:
  - tooling
created_at: 2026-04-18T12:00:15
updated_at: 2026-04-26T08:37:43
recent_editor: CODEX
---

# Content Diagrams

Visual reference for the repo's content architecture, hierarchy, and flow. Each
diagram stands alone. Skim top to bottom to grasp everything without reading
rules 01-05 first.

## 1. Repo Tree

```text
study/
|-- home.md                        root hub
|-- glossary.md                    abbreviations, repo-wide
|-- README.md                      repo index for humans on GitHub
|-- CLAUDE.md and AGENTS.md        root agent entrypoints
|-- rules/                         how to write and maintain notes
|   |-- AGENTS.md / CLAUDE.md / CODEX.md / KIRO.md
|   |-- 01_note_structure.md
|   |-- 02_navigation.md
|   |-- 03_cross_linking.md
|   |-- 04_security.md
|   |-- 05_git_guide.md
|   `-- 06_content_diagrams.md     this file
|-- ai/                            concept domain
|   |-- 00_ai_overview.md          domain study hub
|   |-- README.md                  folder index
|   `-- 01_*.md to 15_*.md         concept notes; NN_ is an identifier, not a rank
|-- cloud/aws/                     domain with optional subdomains
|   |-- 00_aws_overview.md
|   |-- README.md / CLAUDE.md / AGENTS.md
|   |-- 01_*.md to 50_*.md
|   |-- agentcore/
|   |   |-- 00_agentcore_overview.md
|   |   `-- 01_*.md to 09_*.md
|   `-- images/console/*.png
|-- computing/, git/, networking/, tooling/
|   `-- same pattern as ai/
|-- raw/                           text inbox for source material
|   `-- processed/                 handled raw text files
|-- .claude/ / .codex/ / .kiro/    per-agent automation
`-- .githooks/                     shared git hook entrypoints
```

## 2. Content Layers

Each layer is built on the one below. Read bottom-up.

```text
L7  HUB         home.md and glossary.md
L6  INDEX       {domain}/00_{domain}_overview.md; README.md is a human folder index
L5  CROSS-LINK  inline [note](../other/NN_x.md) references; `../other/NN_x.md` is a placeholder example
L4  NAVIGATION  header: [Overview](./00_{domain}_overview.md)
                footer: [Overview] + **Related:** + **Tags:**
                associative navigation, no prev/next
L3  BODY        # Title
                ## What It Is / Analogy / How It Works
                ## Example / Why It Matters
L2  FRONTMATTER tags / created_at / updated_at / recent_editor
L1  FILE        {domain}/NN_name.md on disk, git-tracked
```

## 3. Hierarchy

```text
home.md
|-- ai/00_ai_overview.md
|   `-- ai/01_*.md to 15_*.md
|-- cloud/aws/00_aws_overview.md
|   |-- cloud/aws/01_*.md to 50_*.md
|   `-- cloud/aws/agentcore/00_agentcore_overview.md
|       `-- cloud/aws/agentcore/01_*.md to 09_*.md
|-- computing/00_computing_overview.md
|-- git/00_git_overview.md
|-- networking/00_networking_overview.md
`-- tooling/00_tooling_overview.md
```

## 4. Note Anatomy

Single concept-note file, top to bottom:

```text
---
tags:
  - aws
  - serverless
created_at: 2026-04-17T14:30:00
updated_at: 2026-04-18T11:46:13
recent_editor: CLAUDE
---

[Overview](./00_aws_overview.md)

# Title

## What It Is
1-2 sentence definition.

## Analogy

## How It Works

## Example

## Why It Matters

---
[Overview](./00_aws_overview.md)

**Related:** X -> x.md, Y -> y.md
**Tags:** #aws #serverless
```

## 5. Navigation Flow

What a reader can do from any concept note:

```text
you are on a concept note
|-- [Overview] -> 00_{domain}_overview.md
|   `-- parent overview footer -> home.md
|-- inline link in prose -> jump by concept
|-- Related list -> neighboring notes
`-- #tag pane -> grouped notes with shared tags

From the overview, the reader can move back to home.md or into any other linked domain.
glossary.md remains reachable from any note via inline links.
```

## 6. Cross-Link Example

Canonical note explains once. Related notes link in.

```text
ai/11_kv_cache.md                   cloud/aws/database/04_amazon_elasticache.md
+-------------------+               +----------------------------------------+
| KV Cache          |<------------->| ElastiCache                            |
| canonical note    |               | AWS managed form; link back on first   |
| explain theory    |               | relevant mention                       |
+-------------------+               +----------------------------------------+
           \                                   /
            \                                 /
             +----------- glossary.md --------+

Rule: explain once. Inline link on first mention. No "See Also" section.
```

## 7. Push Pipeline

What happens when an AI agent writes to a note:

```text
Write/Edit tool call on note.md
  -> PostToolUse hook fires (matcher: Write|Edit)
  -> .claude/hooks/auto-push.sh
  -> parse stdin JSON and extract tool_input.file_path
  -> git add -A -- "$file_path"        only that file, no repo-wide sweep
  -> git commit                        msg: "auto: update <file>"
  -> git push
     -> .githooks/pre-push             dispatcher
        -> .githooks/pre-push-study-content
           ack check; auto-ACKed for AI
        -> .codex/hooks/pre-push
           frontmatter, structure, footer, security
        -> .claude/hooks/pre-push
           quiz skipped for CLAUDE_AUTO_PUSH=1
  -> remote: GitHub
```
