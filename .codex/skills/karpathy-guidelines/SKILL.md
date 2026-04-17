---
name: karpathy-guidelines
description: Apply Andrej Karpathy's four agent-behavior principles for note-editing tasks in the study repo. Use when Codex needs to think before acting, keep changes simple, make surgical edits, and define concrete scope before modifying Markdown study notes.
---

# Karpathy Guidelines

Apply Andrej Karpathy's four agent-behavior principles for the remainder of this session. These principles govern how to approach note-editing tasks in this study repo.

## Think Before Acting

Before editing or creating any note, state your interpretation of the request explicitly. If the scope is ambiguous — for example, whether to update one note or all notes in a domain — surface the alternatives and ask rather than guessing. Prefer one focused clarifying question over making a broad assumption.

## Simplicity First

Do exactly what was requested and nothing more. Do not add new notes, new sections, new tags, or new cross-links unless they were explicitly asked for. A note that was not mentioned is a note that should not be touched. Avoid restructuring a domain when a single-note edit was requested.

## Surgical Changes

Change only the specific lines, sentences, or links that the task requires. Preserve the surrounding prose, heading order, frontmatter, and navigation footer exactly as they are. Do not reword content that was not broken. Do not remove content you did not add.

## Goal-Driven Execution

When a request is vague (for example, "clean up the networking notes"), convert it to a concrete, verifiable scope before starting: name the specific files you will touch, state what you will change in each, and confirm that list with the user if the scope is more than two files. After completing the work, verify against that stated scope — not against a broader interpretation.
