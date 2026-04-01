# Harness

## What It Is
The harness is the controlled runtime environment around the agent.

It defines what the agent can access and how it is allowed to operate.

Typical harness concerns:
- filesystem access
- network access
- approval policy
- sandbox mode
- available tools
- model configuration
- runtime profiles

## Analogy
If the agent is a worker, the harness is the workshop:
- which rooms are unlocked
- which tools are on the wall
- what actions require approval
- what safety rules apply

## Example
A harness may allow:
- reading files in a repo
- editing only inside the workspace
- running shell commands
- asking for approval before internet access or destructive actions

That means the same agent can behave very differently depending on the harness.

## What Usually Lives in the Harness

- config files such as `~/.codex/config.toml`
- tool definitions
- MCP server connections
- approval and sandbox settings
- profiles like `safe` or `balanced`

## What People Commonly Mean by "Harness"

In everyday use, people often use "harness" as a broad term for:
- the local Codex runtime
- the tool execution layer
- sandbox and approvals
- session environment and config

That is broader than just one file or one process.

## Why It Matters

Many beginner questions are really harness questions:
- Why could the agent read this file but not write there?
- Why did it ask for approval?
- Why can one setup browse the web and another cannot?

Those are usually harness differences, not agent differences.
