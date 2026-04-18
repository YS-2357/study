---
tags:
  - tooling
  - git
  - ai
created_at: 2026-04-12T00:00:00
updated_at: 2026-04-18T18:37:25
recent_editor: CODEX
---

↑ [Overview](./00_tooling_overview.md)

# Obsidian + GitHub as a Second Brain

## What It Is

A personal knowledge system where notes live as plain Markdown files in an Obsidian vault, synced to GitHub, and read directly by AI tools. The vault is the memory — persistent across sessions, version-controlled, and grounded in your own content.

## Analogy

A notebook you carry everywhere, except every page is a plain text file, every edit is tracked in Git, and any AI tool can read it without an API.

## How It Works

### The core loop

```
You write a note in Obsidian (plain .md file on disk)
    ↓
[Git commits and pushes](../git/02_daily_git_workflow.md) to GitHub (version history, accessible anywhere)
    ↓
AI tool (Claude, Cursor, Copilot) reads the .md files directly
    ↓
AI answers questions grounded in your personal knowledge base
```

Because files are plain Markdown, no export or conversion is needed — any tool that can read text can consume the vault.

### Why it is called "local memory"

| Property | What it means |
|----------|--------------|
| Local | Files live on your machine, not in a vendor's database |
| Persistent | Survives context window resets, model changes, new chat sessions |
| Git-versioned | Every change tracked — you can diff how your thinking evolved |
| AI-readable | Plain Markdown — any tool reads it without an API |
| Searchable | grep, Obsidian search, or vector-embed the files for semantic search |

### Common folder structure: PARA + Zettelkasten hybrid

| Folder | Purpose |
|--------|---------|
| `00-Inbox/` | Capture everything first, sort later |
| `01-Projects/` | Active work with deadlines |
| `02-Areas/` | Ongoing responsibilities |
| `03-Resources/` | Reference material — study notes, domain knowledge |
| `04-Archive/` | Completed content |
| `MOC/` | Maps of Content — index notes linking related notes (like `home.md` or `00_{domain}_overview.md`) |
| `Templates/` | Note templates |

**PARA** (Projects, Areas, Resources, Archive) is action-oriented — organizes by what you are doing. **Zettelkasten** is idea-oriented — organizes by atomic concepts linked to each other. Most practical vaults combine both: PARA folders for project context, Zettelkasten-style linking for knowledge.

### Claude Code integration

Claude Code reads `CLAUDE.md` at session start automatically. Placing a `CLAUDE.md` in the vault root gives Claude rules, structure, and context before the first prompt — so it knows who you are and how the vault is organized without being told each session.

```
vault/
  CLAUDE.md          ← rules Claude follows every session
  MEMORY.md          ← index of persistent memory files
  .claude/memory/    ← individual memory files (user, project, feedback)
  03-Resources/      ← study notes, domain knowledge
  01-Projects/       ← active work
```

This repo (`study/`) follows this pattern: `CLAUDE.md` defines rules, `home.md` is the root MOC with `00_{domain}_overview.md` files as per-domain MOCs, and all notes are plain Markdown.

### Notable open-source implementations

| Repo | What it does |
|------|-------------|
| [sean-esk/second-brain-gtd](https://github.com/sean-esk/second-brain-gtd) | Second brain using Obsidian + Claude Code with skills |
| [heyitsnoah/claudesidian](https://github.com/heyitsnoah/claudesidian) | Obsidian plugin that turns vault into Claude-powered second brain |
| [voidashi/obsidian-vault-template](https://github.com/voidashi/obsidian-vault-template) | Minimalist two-level hierarchy + tagging system |
| [DuskWasHere/dusk-obsidian-vault](https://github.com/DuskWasHere/dusk-obsidian-vault) | PARA + Zettelkasten hybrid with task tracking |

## Example

Daily workflow with Claude Code:

1. Write a note in Obsidian — saved as `03-Resources/aws/bedrock.md`
2. Git auto-push commits it to GitHub
3. Next Claude session: Claude reads `CLAUDE.md`, knows the vault structure
4. Ask "what do I know about Bedrock?" — Claude reads `bedrock.md` directly, answers from your notes

No copy-paste, no re-explaining context. The vault is the memory.

## Why It Matters

LLM context windows reset. Cloud-based AI memory is vendor-locked. A Git-backed Markdown vault is permanent, portable, and readable by any tool — today and in ten years. The notes compound: the more you write, the better grounded your AI answers become.

> **Tip:** Start with `CLAUDE.md` in the vault root and one overview file per domain (e.g., `00_{domain}_overview.md`). Let structure grow from the notes, not the other way around.

---
← Previous: [Obsidian vs Notion](04_obsidian_vs_notion.md) | [Overview](./00_tooling_overview.md) | Next: [VS Code Remote SSH with EC2](06_vscode_remote_ssh_with_ec2.md) →
