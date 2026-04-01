# Hooks

## What It Is
A hook is a script or action that runs automatically when a certain runtime event happens.

Examples:
- a notification after an agent turn completes
- a post-run formatter
- a custom logging action

## Analogy
If the agent is the worker, a hook is the automatic bell or side process that runs when something specific happens in the workshop.

The worker does not need to remember to ring the bell. The environment does it automatically.

## Example
A notification hook may:
- listen for an "agent finished" event
- play a sound
- do nothing else

That is a hook. It is not the agent reasoning. It is environment-triggered automation.

## What People Mostly Use

Most beginners do not need hooks.

Hooks are useful when someone wants:
- convenience automation
- local notifications
- a small amount of custom runtime glue

Compared with tools, skills, and `AGENTS.md`, hooks are lower priority for most users.

## Why It Matters

Hooks are easy to overestimate.

They can improve the experience, but they usually do not change the core learning path:
- understand the agent first
- then tools and instructions
- then specialized automation later
