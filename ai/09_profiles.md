# Profiles

## What It Is
A profile is a named runtime configuration for the agent environment.

A profile may change:
- approval policy
- sandbox mode
- web access behavior
- model defaults
- reasoning settings

## Analogy
Profiles are like operating modes on a machine:
- safer inspection mode
- normal working mode
- more permissive experimental mode

The machine is the same, but the operating rules change.

## Example
A safer profile might:
- keep the filesystem read-only
- disable or reduce web access
- require more approvals

A normal working profile might:
- allow writing in the workspace
- allow normal web lookups
- ask only for higher-risk approvals

## What People Mostly Use

Most people only need two broad modes:
- a safer read-oriented mode
- a normal working mode

Highly permissive modes are useful later, but they are a poor default for beginners.

## Why It Matters

Profiles explain why the same agent may seem cautious in one session and more capable in another.

That difference often comes from runtime policy, not from the model suddenly becoming smarter or weaker.
