---
tags:
  - ai
  - networking
---
# MCP

## What It Is

MCP (Model Context Protocol) is a standard way for an agent runtime to connect to external [tools](04_tools.md), prompts, and resources. It provides a common contract so that every tool doesn't need a custom integration.

## Analogy

Think of MCP like a standardized adapter system. Instead of every tool inventing a custom integration shape, MCP provides a uniform protocol — like USB for peripherals.

## How It Works

1. Some capability exists (e.g., a browser automation library, a GitHub API, a database)
2. An MCP server wraps it and exposes it in the MCP-defined format (tools, resources, prompts)
3. The agent runtime connects to the MCP server and discovers what is available

An MCP server standardizes a custom-shaped capability into the common MCP contract.

## Example

An MCP server may expose tools the agent can call, resources the agent can read, and reusable prompts. Browser automation, external docs, or service integrations all look uniform to the agent runtime.

## Why It Matters

MCP explains why one agent environment can access GitHub, browser controls, or docs while another cannot. That is usually a connection and [harness](02_harness.md) question, not a core agent intelligence question.

---
← Previous: [Plugins](06_plugins.md) | [Overview](00_overview.md) | Next: [Profiles](09_profiles.md) →
