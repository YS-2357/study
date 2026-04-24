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

# Spec-Driven Development with Kiro

## What It Is

Spec-driven development with Kiro is a workflow where a natural-language prompt becomes explicit requirements, system design, and implementation tasks before the main coding work begins.

## Analogy

Instead of starting with "just write the code," Kiro tries to act like a team that writes the ticket, drafts the design, breaks the work into tasks, and only then starts implementing.

## How It Works

Kiro's deck positions spec-driven development as the bridge between prototype speed and production discipline.

1. The user describes the feature or product idea in natural language.
2. Kiro expands that request into structured artifacts such as requirements and design notes.
3. The user iterates on the spec and architecture with Kiro before large code changes happen.
4. Kiro uses that approved structure to implement work while the user keeps control over the process.

The deck contrasts this with "vibe coding," where fast implementation starts early but validation and QA happen later in a more traditional SDLC path.

## Example

One Kiro IDE slide shows a prompt being turned into `requirements.md`, `design.md`, and implementation-oriented files before the feature build continues. The point is not only faster coding, but a clearer path from idea to test and release.

## Why It Matters

This workflow makes Kiro useful for teams that want AI help without giving up engineering structure. It aims to reduce the gap between a quick prototype and software that can survive QA, deployment, and ongoing maintenance.

---
[Overview](00_kiro_overview.md)

**Related:** [Kiro - Overview](00_kiro_overview.md), [Kiro Hooks and Context Management](02_hooks_and_context.md), [Kiro CLI](03_kiro_cli.md), [Harness](../concepts/02_harness.md)
**Tags:** #ai #kiro
