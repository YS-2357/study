---
tags:
  - ai
  - kiro
created_at: 2026-04-20T13:50:42
updated_at: 2026-04-24T08:47:57
recent_editor: CODEX
source:
  - kiro_first_call_deck_korean
---

# Kiro - Overview

Kiro is AWS's AI IDE for agentic software development. These notes focus on Kiro from the coding-agent and workflow angle: moving from prompt-driven prototypes toward structured, spec-driven delivery.

> For Kiro as an AWS infrastructure product, see [cloud/aws/](../../cloud/aws/).

## Core Workflow

- [Spec-Driven Development with Kiro](01_spec_driven_development.md) - Turn a prompt into requirements, design, and development tasks instead of stopping at code generation.

## Execution Environment

- [Kiro Hooks and Context Management](02_hooks_and_context.md) - Use hooks, steering files, native MCP connections, and checkpoints to keep the agent aligned with the project.
- [Kiro CLI](03_kiro_cli.md) - Use Kiro from the terminal while keeping a shell-first workflow.

## Why It Matters

The deck frames Kiro as more than an autocomplete or chat assistant. It is positioned as an environment for shipping higher-quality software with tighter collaboration, stronger control, and more structure across prototype, test, and production work.

## Cross-references

- Core LLM concepts - [AI Concepts](../concepts/)
- Shared protocol and runtime concepts - [MCP](../concepts/07_mcp.md), [Hooks](../concepts/08_hooks.md), [Harness](../concepts/02_harness.md)
- AWS infra angle - [AWS](../../cloud/aws/00_aws_overview.md)

---
[AI Overview](../00_ai_overview.md)
