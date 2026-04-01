# AI Agents - Overview

## Purpose
Foundation concepts needed to understand how Codex and similar coding agents work in practice.

## Contents

### Core Runtime Concepts
### [01. Agent](01_agent.md)
What the agent is, what it does, and when to use it:
- Reads context
- Reasons about tasks
- Calls tools
- Writes or edits files
- Reports results

### [02. Harness](02_harness.md)
The environment around the agent:
- Sandbox and approvals
- Filesystem access
- Config and profiles
- Tool availability
- MCP servers

### [03. AGENTS.md](03_agents_md.md)
Repo-specific instructions for the agent:
- Coding rules
- Test commands
- Architecture notes
- Local workflow expectations

### Working Components
### [04. Tools](04_tools.md)
Concrete capabilities the agent can call:
- Shell commands
- Web search
- Browser automation
- GitHub and Google tools

### [05. Skills](05_skills.md)
Reusable instruction bundles for specialized work:
- Figma workflows
- CI debugging
- Spreadsheet and document handling
- Deployment helpers

### [06. Plugins](06_plugins.md)
Larger bundles that expose external systems:
- GitHub
- Gmail
- Google Drive
- Google Calendar
- Vercel

### Protocol and Automation
### [07. MCP](07_mcp.md)
The protocol layer behind many external tools:
- Tool calls
- Resources
- Server connections
- Standardized integration

### [08. Hooks](08_hooks.md)
Optional local automation tied to agent events:
- Notifications
- Post-run scripts
- Environment-specific behavior

### [09. Profiles](09_profiles.md)
Named runtime modes:
- Safer inspection mode
- Normal working mode
- More permissive experimental modes

## How to Use

**If you are new to agents:**
- Start with [Agent](01_agent.md)
- Then read [Harness](02_harness.md)
- Then read [AGENTS.md](03_agents_md.md)

**If you want the practical workflow first:**
- Read [Tools](04_tools.md)
- Then [Skills](05_skills.md)
- Then [Plugins](06_plugins.md)

**If you see unfamiliar terms in docs:**
- Read [MCP](07_mcp.md) for tool protocol context
- Read [Profiles](09_profiles.md) for runtime behavior differences
- Leave [Hooks](08_hooks.md) for later unless you actually need automation

## Quick Mental Model

| Term | Short meaning |
|------|---------------|
| Agent | The worker |
| Harness | The workshop around the worker |
| `AGENTS.md` | Repo instructions for the worker |
| Tools | Things the worker can use |
| Skills | Specialized playbooks |
| Plugins | Bundles for outside systems |
| MCP | Protocol for connecting tools/resources |
| Hooks | Automatic side effects |
| Profiles | Named runtime modes |
