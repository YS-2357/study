---
tags:
  - ai
created_at: 2026-04-01T00:00:00
updated_at: 2026-04-17T14:18:47
recent_editor: CLAUDE
---

↑ [Overview](./00_ai_overview.md)

# Tools

## What It Is

Tools are concrete capabilities the [agent](01_agent.md) can call while working. A tool is an executable capability — not a concept note or instruction file.

## Analogy

If the agent is the worker, tools are the instruments on the workbench. A smart worker with no tools is limited. A smart worker with the right tools can inspect, change, verify, and report.

## Example

If you ask "Find every place this API key is referenced," the agent uses a search tool like `rg`. If you ask "Check whether the UI is broken," the agent uses a browser automation tool.

## How It Works

| Category | Example use |
|----------|-------------|
| Shell | Run tests, inspect files, search text |
| Web | Check latest docs or current information |
| Browser | Verify pages, click flows, inspect UI |
| Repo/SCM | PRs, issues, CI status |
| Docs/Data | Read or edit documents, spreadsheets |

Most day-to-day work relies on shell tools, file search, Git-aware commands, and web lookup. Tools are made available through the [harness](02_harness.md) and often connected via [MCP](07_mcp.md).

## Why It Matters

The agent's quality depends not only on reasoning but also on what tools are available and how well it uses them.

---
← Previous: [AGENTS.md](03_agents_md.md) | [Overview](./00_ai_overview.md) | Next: [Skills](05_skills.md) →
