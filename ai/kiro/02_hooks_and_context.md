---
tags:
  - ai
  - kiro
created_at: 2026-04-24T08:47:57
updated_at: 2026-04-24T08:47:57
recent_editor: CODEX
source:
  - kiro_first_call_deck_korean
---

[Overview](00_kiro_overview.md)

# Kiro Hooks and Context Management

## What It Is

Kiro uses hooks, steering files, native MCP connections, and checkpoints to keep the agent connected to the project context while still giving the user control over what happens.

## Analogy

Think of it like giving a new teammate four things before they start: house rules, access to the right systems, automatic reminders for routine work, and a rollback point if they go in the wrong direction.

## How It Works

The deck shows several context and control layers working together:

1. **Agent hooks** trigger background work from events such as saving a file.
2. **Steering files** tell Kiro how to understand and interact with a specific codebase.
3. **Native MCP integration** connects Kiro to external tools, documents, databases, and APIs.
4. **Rich context inputs** such as UI design images or architecture whiteboard photos can guide implementation.
5. **Timeline checkpoints** let the user roll back to earlier execution states if an exploratory path goes wrong.

These are Kiro-specific uses of broader concepts like [Hooks](../concepts/08_hooks.md) and [MCP](../concepts/07_mcp.md).

## Example

The deck shows an agent hook running automatically on file-save-style events to extend work into documentation, unit-test generation, or code-performance improvement. Another slide shows steering files and MCP connections helping Kiro understand an existing app before making changes.

## Why It Matters

AI coding quality depends heavily on context and control. Kiro's approach is to make that context explicit and reusable instead of hoping the model infers everything from one chat prompt.

---
[Overview](00_kiro_overview.md)

**Related:** [Kiro - Overview](00_kiro_overview.md), [Spec-Driven Development with Kiro](01_spec_driven_development.md), [MCP](../concepts/07_mcp.md), [Hooks](../concepts/08_hooks.md), [Harness](../concepts/02_harness.md)
**Tags:** #ai #kiro
