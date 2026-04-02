# Study Agent Guide

This repository is a Markdown study-notes repo. Treat it as a content repository, not an application or service codebase.

## Scope

These instructions apply to the entire `study/` repository unless a deeper `AGENTS.md` overrides them for a subtree.

## Source Of Truth

- Follow the detailed note-format and README standards in [README.md](README.md).
- Use this file as the compact operating guide for agents working in this repo.

## Core Rules

- `README.md` files must stay folder indexes only. Do not add study content, study order, or concept explanations to a README.
- The nearest relevant `00_overview.md` is the study hub for its subtree. Update that overview when notes in that subtree are added, removed, renamed, or reordered.
- Explain a concept once in the note where it belongs. In other notes, link to the existing explanation instead of duplicating it.
- Prefer editing existing Markdown notes, links, and navigation over adding tooling, scripts, or structural churn.
- Preserve the repository's existing organization unless the task explicitly requires a reorganization.

Example: add concept explanations to a note, not to `README.md`.
Example: if you add `aws/101/aws_services/` content, update `aws/101/aws_services/00_overview.md`.

## Primary Artifacts

- `README.md`: folder index and directory description
- `00_overview.md`: study hub and ordered navigation for a subtree
- concept notes: the main study content
- walkthrough notes: step-by-step operational or console guides
- image references: screenshots and image assets used by notes

## Editing Checklist

- If you edit a note, preserve the required structure defined in [README.md](README.md).
- If you edit a note, preserve or repair the navigation footer.
- If you add or rename a note, update the nearest relevant `00_overview.md`.
- If a folder's contents change materially, update that folder's `README.md`.
- If a concept is already documented elsewhere, link to the existing note instead of re-explaining it.
- Do not put study content into `README.md`.

## Subtree Policy

- Add a nested `AGENTS.md` only when a subtree needs materially different instructions from the repo root.
- Keep subtree files narrow. They should extend or override root behavior only for that subtree.
