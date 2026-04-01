# Tools

## What It Is
Tools are concrete capabilities the agent can call while working.

A tool is not a concept note or an instruction file. It is an executable capability.

Examples:
- shell command execution
- web search
- browser automation
- GitHub queries
- Google Drive document access

## Analogy
If the agent is the worker, tools are the actual instruments on the workbench.

A smart worker with no tools is limited. A smart worker with the right tools can inspect, change, verify, and report.

## Example
If you ask:

```text
Find every place this API key is referenced.
```

The agent may use a search tool such as `rg` or an internal file-search tool.

If you ask:

```text
Check whether the UI is broken in the browser.
```

The agent may use a browser automation tool.

## Common Tool Categories

| Category | Example use |
|----------|-------------|
| Shell | Run tests, inspect files, search text |
| Web | Check latest docs or current information |
| Browser | Verify pages, click flows, inspect UI |
| Repo/SCM | PRs, issues, CI status |
| Docs/Data | Read or edit documents, spreadsheets, slides |

## What People Mostly Use

Most day-to-day agent work relies on:
- shell tools
- file search
- Git-aware commands
- web lookup when freshness matters
- browser tools for UI work

These are used more often than custom hooks or custom plugin development.

## Why It Matters

The agent’s quality is not only about reasoning. It is also about what tools are available and how well it uses them.
