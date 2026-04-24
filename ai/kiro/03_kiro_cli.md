---
tags:
  - ai
  - kiro
  - tooling
created_at: 2026-04-24T08:47:57
updated_at: 2026-04-24T13:14:59
recent_editor: CODEX
source:
  - kiro_first_call_deck_korean
  - kiro_commands_guide
---

[Overview](00_kiro_overview.md)

# Kiro CLI

## What It Is

Kiro CLI is the terminal interface for Kiro. It lets the user work from a shell while still using Kiro's agentic workflow, command system, session management, and tool integrations instead of relying only on the IDE surface.

## Analogy

If Kiro IDE is the full workshop, Kiro CLI is the same worker reporting to the terminal desk. You still have the same assistant, but you operate it through commands, context controls, and terminal-native workflows.

## How It Works

Kiro CLI starts from a shell command such as `kiro-cli chat`, then mixes two kinds of interaction:

1. **Normal prompts** go to the AI as ordinary chat input.
2. **Slash commands** like `/chat`, `/context`, or `/agent` control the CLI itself.
3. **Session and context commands** manage saved conversations, compression, and which files are in scope.
4. **Execution-profile commands** switch models, agents, plans, prompts, and tool permissions.
5. **Integration commands** connect the CLI to code intelligence, knowledge indexes, MCP servers, and configured hooks.

The command guide shows that Kiro CLI is not just one command runner. It is a terminal control surface for the same broader Kiro system: chat, planning, tool use, project context, and external integrations. That makes CLI usage the shell-first counterpart to the IDE's spec-driven workflow.

## Command Categories

The guide organizes Kiro CLI around a few durable command families:

- **Conversation control**: `/chat`, `/clear`, `/compact`, and `/context`
- **Agent and model control**: `/agent`, `/model`, `/plan`, `/guide`, and `/prompts`
- **Work execution and code understanding**: `/tools`, `/code`, and `/knowledge`
- **External connectivity**: `/mcp` and `/hooks`
- **Terminal ergonomics**: `/editor`, `/reply`, `/paste`, `/copy`, `/transcript`, `/theme`, and `/spawn`

These categories matter more than memorizing every individual command because they explain what kinds of control Kiro CLI exposes from the terminal.

## Example

A terminal-focused developer could run `kiro-cli chat`, add the current repo files with `/context`, switch to a planning-oriented profile with `/plan`, inspect tool permissions with `/tools`, and connect extra capability through `/mcp` without ever leaving the shell. The same user could also save or resume the conversation with `/chat` and spawn parallel work with `/spawn` in TUI mode.

## Why It Matters

Many engineering workflows already live in the terminal. Kiro CLI matters because it brings Kiro's agent model into that environment without reducing it to plain text chat. It gives the user explicit control over sessions, context windows, agents, tools, code intelligence, and integrations, which is exactly what shell-first engineering teams usually need.

---
[Overview](00_kiro_overview.md)

**Related:** [Kiro - Overview](00_kiro_overview.md), [Spec-Driven Development with Kiro](01_spec_driven_development.md), [Kiro Hooks and Context Management](02_hooks_and_context.md), [tools](../concepts/04_tools.md)
**Tags:** #ai #kiro #tooling
