---
tags:
  - ai
created_at: 2026-04-01T00:00:00
updated_at: 2026-04-17T14:18:47
recent_editor: CLAUDE
---

↑ [Overview](./00_overview.md)

# Profiles

## What It Is

A profile is a named runtime configuration for the agent environment. It may change approval policy, sandbox mode, web access behavior, model defaults, and reasoning settings.

## Analogy

Profiles are like operating modes on a machine: safer inspection mode, normal working mode, or more permissive experimental mode. The machine is the same, but the operating rules change.

## Example

A safer profile might keep the filesystem read-only, disable web access, and require more approvals. A normal working profile allows writing in the workspace, normal web lookups, and asks only for higher-risk approvals.

## Why It Matters

Profiles explain why the same agent may seem cautious in one session and more capable in another. That difference comes from runtime policy, not from the model becoming smarter or weaker. Most people only need two modes: a safer read-oriented mode and a normal working mode.

---
← Previous: [Hooks](08_hooks.md) | [Overview](./00_overview.md) | Next: [Attention](10_attention.md) →
