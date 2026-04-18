---
tags:
  - tooling
created_at: 2026-04-18T19:41:34
updated_at: 2026-04-18T19:41:34
recent_editor: CODEX
---

# Codex MCP

Repo-local MCP server dependencies for Codex.

## Sequential Thinking

Sequential Thinking is installed as a local npm dependency in this directory. The root `.mcp.json` points to the local package entrypoint so Codex does not rely on ad-hoc remote `npx -y` resolution each time the server starts.

Install or refresh dependencies from the repo root:

```powershell
npm install --prefix .codex/mcp
```

Do not track `.codex/mcp/node_modules/`; track `package.json` and `package-lock.json`.
