# Plugins

## What It Is

A plugin is a larger bundle that exposes [skills](05_skills.md), [tools](04_tools.md), and integrations for an outside system — such as GitHub, Gmail, Google Calendar, Google Drive, or Vercel.

## Analogy

If skills are playbooks, plugins are entire capability packs for a connected platform. A GitHub plugin includes PR inspection tools, issue tools, review workflows, and CI-related skills.

## Example

If you ask the agent to inspect a pull request, a GitHub plugin lets it fetch PR metadata, read review comments, inspect changed files, and help draft fixes. That goes beyond simple local file access.

## How It Works

Plugins are used when the agent needs to work across systems, not just inside the repo. A plugin may contribute several skills, but the two are not the same thing:
- Plugin = capability bundle for a platform
- Skill = reusable workflow guidance

## Why It Matters

When someone says "the agent can work with GitHub," that usually means the [harness](02_harness.md) has a GitHub-related plugin available.

---
← Previous: [Skills](05_skills.md) | [Overview](00_overview.md) | Next: [MCP](07_mcp.md) →
