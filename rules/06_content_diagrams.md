---
tags:
  - tooling
created_at: 2026-04-18T12:00:15
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
---

# Content Diagrams

Visual reference for the repo's content architecture, hierarchy, and flow. Each
diagram stands alone. Skim top to bottom to grasp everything without reading
rules 01–05 first.

## 1. Repo Tree

```
study/
├── home.md                         ← root hub
├── glossary.md                     ← abbreviations, repo-wide
├── README.md                       ← repo index (for humans on GitHub)
├── CLAUDE.md · AGENTS.md           ← agent entrypoints
│
├── rules/                          ← how to write and maintain notes
│   ├── AGENTS.md · CLAUDE.md · CODEX.md · KIRO.md
│   ├── 01_note_structure.md
│   ├── 02_navigation.md
│   ├── 03_cross_linking.md
│   ├── 04_security.md
│   ├── 05_git_guide.md
│   └── 06_content_diagrams.md      ← this file
│
├── ai/                             ← concept domain
│   ├── 00_ai_overview.md           ← domain study hub
│   ├── README.md                   ← folder index
│   └── 01_*.md … 15_*.md           ← concept notes (study order)
│
├── aws/                            ← flat concept domain
│   ├── 00_aws_overview.md
│   ├── README.md · CLAUDE.md · AGENTS.md
│   ├── 01_*.md … 50_*.md
│   ├── agentcore/                  ← nested subdomain
│   │   ├── 00_agentcore_overview.md
│   │   └── 01_*.md … 09_*.md
│   └── images/console/*.png
│
├── computing/ · git/ · networking/ · tooling/
│   └── (same pattern as ai/)
│
├── raw/                            ← text inbox for source material
│   └── processed/                  ← handled raw text files
├── .claude/ · .codex/ · .kiro/     ← per-agent automation
└── .githooks/                      ← shared git hook entrypoints
```

## 2. Content Layers

Each layer is built on the one below. Read bottom-up.

```
╭─── L7  HUB ─────────────────────────────────────────╮
│   home.md  ←→  glossary.md                          │
╰─────────────────────────────────────────────────────╯
╭─── L6  INDEX ───────────────────────────────────────╮
│   {domain}/00_{domain}_overview.md                  │
│   README.md (folder index, humans only)             │
╰─────────────────────────────────────────────────────╯
╭─── L5  CROSS-LINK ──────────────────────────────────╮
│   inline [note](../other/NN_x.md) refs              │
│   — explain once, link from elsewhere               │
╰─────────────────────────────────────────────────────╯
╭─── L4  NAVIGATION ──────────────────────────────────╮
│   header:  ↑ [Overview](./00_{domain}_overview.md)  │
│   footer:  ← Prev | [Overview] | Next →             │
╰─────────────────────────────────────────────────────╯
╭─── L3  BODY ────────────────────────────────────────╮
│   # Title                                           │
│   ## What It Is · Analogy · How It Works            │
│   ## Example · Why It Matters                       │
╰─────────────────────────────────────────────────────╯
╭─── L2  FRONTMATTER ─────────────────────────────────╮
│   tags · created_at · updated_at · recent_editor    │
╰─────────────────────────────────────────────────────╯
╭─── L1  FILE ────────────────────────────────────────╮
│   {domain}/NN_name.md on disk, git-tracked          │
╰─────────────────────────────────────────────────────╯
```

## 3. Hierarchy

```
                       home.md
                          │
         ┌────────┬───────┼───────┬───────────┐
         ▼        ▼       ▼       ▼           ▼
        ai/     aws/  computing/  git/   networking/  … tooling/
         │       │       │        │          │
         ▼       ▼       ▼        ▼          ▼
     00_ai_  00_aws_  00_comp_ 00_git_   00_net_
     overview overview overview overview overview
         │       │        │        │         │
     01…15   01…50    01…09    01…02    01…06
                │
                ▼
          aws/agentcore/
                │
                ▼
       00_agentcore_overview
                │
           01…09
```

## 4. Note Anatomy

Single concept-note file, top to bottom:

```
┌────────────────────────────────────────────────┐
│ ---                                            │ ← frontmatter open
│ tags:                                          │
│   - aws                                        │
│   - serverless                                 │
│ created_at: 2026-04-17T14:30:00                │ ← ISO 8601
│ updated_at: 2026-04-18T11:46:13                │
│ recent_editor: CLAUDE                          │
│ ---                                            │ ← frontmatter close
│                                                │
│ ↑ [Overview](./00_aws_overview.md)             │ ← up-nav header
│                                                │
│ # Title                                        │ ← H1, exactly once
│                                                │
│ ## What It Is                                  │ ← required
│ 1-2 sentence definition.                       │
│                                                │
│ ## Analogy                                     │ ← optional
│                                                │
│ ## How It Works                                │ ← required
│                                                │
│ ## Example                                     │ ← required
│                                                │
│ ## Why It Matters                              │ ← required
│                                                │
│ ---                                            │ ← footer divider
│ ↑ [Overview](./00_aws_overview.md)             │ ← up-nav (restated)
│                                                │
│ **Related:** [X](x.md), [Y](y.md)              │ ← associative links
│ **Tags:** #aws #serverless                     │ ← mirror of frontmatter
└────────────────────────────────────────────────┘
```

## 5. Navigation Flow

What a reader can do from any concept note:

```
               you are on a concept note
                         │
        ┌────────────────┼──────────────────┬──────────────┐
        │                │                  │              │
        ▼                ▼                  ▼              ▼
    ↑ Overview    inline link in prose   Related list   #tag pane
        │                │                  │              │
        │                └── jump by concept, not order ───┘
        ▼
  00_{domain}_
   overview.md
        │
        │ (overview footer)
        ▼
     home.md
        │
        ▼
  any other domain's overview
        │
        ▼
     glossary.md   ←  reachable from any note via inline link
```

## 6. Cross-Link Example

Canonical note explains once. Related notes link in.

```
  ai/11_kv_cache.md                 aws/database/04_amazon_elasticache.md
  ┌──────────────────┐              ┌──────────────────┐
  │ KV Cache         │              │ ElastiCache      │
  │ (canonical note) │              │                  │
  │                  │◄─────────────│ "see [KV cache]  │
  │                  │              │    for theory"   │
  │ "see [           │──────────────►                  │
  │  ElastiCache]    │              │                  │
  │  for the AWS     │              │                  │
  │  managed form"   │              │                  │
  └──────────────────┘              └──────────────────┘
           ▲                                 ▲
           │                                 │
           │       glossary.md               │
           │       ┌───────────┐             │
           └───────│ KV cache  │─────────────┘
                   │ ElastiCache│
                   └───────────┘

 Rule: explain once. Inline link on first mention. No "See Also" section.
```

## 7. Push Pipeline

What happens when an AI agent writes to a note:

```
  Write/Edit tool call on note.md
              │
              ▼
   PostToolUse hook fires  (matcher: Write|Edit)
              │
              ▼
  .claude/hooks/auto-push.sh
              │
              ├── parse stdin JSON → extract tool_input.file_path
              │
              ▼
   git add -A -- "$file_path"         ← only that file, no sweep
              │
              ▼
         git commit  (msg: "auto: update <file>")
              │
              ▼
         git push   ───►  .githooks/pre-push  (dispatcher)
                              │
                              ├─► .githooks/pre-push-study-content
                              │     (ack check, auto-ACKed for AI)
                              │
                              ├─► .codex/hooks/pre-push
                              │     (frontmatter · structure ·
                              │      footer · security)
                              │
                              └─► .claude/hooks/pre-push
                                    (quiz — skipped for
                                     CLAUDE_AUTO_PUSH=1)
              │
              ▼
         remote: GitHub
```
