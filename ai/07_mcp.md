# MCP

## What It Is
MCP stands for Model Context Protocol.

It is a standard way for an agent runtime to connect to external tools, prompts, and resources.

For beginners, the main idea is simple:
- MCP is how many external capabilities are wired into the agent

## Analogy
Think of MCP like a standardized adapter system for tools.

Instead of every tool inventing a custom integration shape, MCP provides a common contract.

## MCP Server

An MCP server is a wrapper around some external capability that exposes it through the MCP protocol's standard shape.

The flow:
1. Some capability exists (e.g., a browser automation library, a GitHub API, a database)
2. An MCP server wraps it and exposes it in the MCP-defined format (tools, resources, prompts)
3. The agent runtime connects to the MCP server and discovers what is available, without needing to know anything about the underlying implementation

In short, an MCP server standardizes a custom-shaped capability into the common MCP contract.

## Example
An MCP server may expose:
- tools the agent can call
- resources the agent can read
- reusable prompts

That means browser automation, external docs, or service integrations can look more uniform to the agent runtime.

## What You Usually See as a User

You often do not interact with MCP directly.

You notice it indirectly through:
- available tools
- connected services
- agent capabilities that appear in the session

## When Beginners Should Care

Care about MCP when:
- you want to understand how integrations are attached
- you want to add a new external tool source
- docs mention MCP servers and resources and the terms feel opaque

Otherwise, it is enough to know that MCP is part of the integration layer.

## Why It Matters

MCP explains why one agent environment can access GitHub, browser controls, or docs while another cannot.

That is usually a connection and harness question, not a core agent intelligence question.
