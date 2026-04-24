---
tags:
  - tooling
created_at: 2026-04-24T09:38:47
updated_at: 2026-04-24T09:38:47
recent_editor: CODEX
---

# Karpathy Guidelines

Canonical editing posture for agents working in this repository. These guidelines apply when an agent is interpreting a note-editing request, narrowing scope, and deciding how much to change.

## Think Before Acting

Before editing or creating any note, state your interpretation of the request explicitly. If the scope is ambiguous, surface the realistic alternatives instead of guessing. Prefer one focused clarifying question over making a broad assumption.

## Simplicity First

Do exactly what was requested and nothing more. Do not add new notes, new sections, new tags, or new cross-links unless they are required by the task. A note that was not mentioned should not be touched.

## Surgical Changes

Change only the specific lines, sentences, or links that the task requires. Preserve surrounding prose, heading order, frontmatter shape, and navigation unless the task requires a structural change. Do not reword healthy content just because you are nearby.

## Goal-Driven Execution

Turn vague requests into a concrete, verifiable scope before editing. Name the files you plan to touch, state what you will change in each, and verify against that stated scope after the work is complete.
