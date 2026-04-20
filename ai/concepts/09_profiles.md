---
tags:
  - ai
created_at: 2026-04-01T00:00:00
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
---

↑ [Overview](../00_ai_overview.md)

# Profiles

## What It Is

A profile is a named runtime configuration for the agent environment. It may change approval policy, sandbox mode, web access behavior, model defaults, and reasoning settings.

## Analogy

Profiles are like operating modes on a machine: safer inspection mode, normal working mode, or more permissive experimental mode. The machine is the same, but the operating rules change.

## How It Works

At session start the agent loads a profile definition (usually a YAML or TOML block in the harness config) and applies its overrides on top of the baseline runtime. Switching profiles does not change the agent's code, tools, or model weights — only the enforcement policies around them: which actions auto-approve, whether the sandbox is read-only, whether network access is allowed, which model is called, and how much reasoning budget is granted. A profile can be named (`default`, `readonly`, `yolo`) and selected at launch via a flag or config entry.

## Example

A safer profile might keep the filesystem read-only, disable web access, and require more approvals. A normal working profile allows writing in the workspace, normal web lookups, and asks only for higher-risk approvals.

## Why It Matters

Profiles explain why the same agent may seem cautious in one session and more capable in another. That difference comes from runtime policy, not from the model becoming smarter or weaker. Most people only need two modes: a safer read-oriented mode and a normal working mode.

---
↑ [Overview](../00_ai_overview.md)

**Related:** [Hooks](08_hooks.md), [Attention](10_attention.md)
**Tags:** #ai
