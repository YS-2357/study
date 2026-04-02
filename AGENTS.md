# /home/user/study Agent Guide

This repository is a Markdown study-notes repo. Treat it as a content repository, not an application or service codebase.

## Scope

These instructions apply to the entire `/home/user/study` repository unless a deeper `AGENTS.md` overrides them for a subtree.

## Source of Truth

- Follow the detailed note-format and README standards in [README.md](README.md).
- Use this file as the compact operating guide for agents working in this repo.

## Repo Rules

- Keep `README.md` files as folder indexes only. Do not add study content, study order, or concept explanations to a README.
- Keep each domain's `00_overview.md` as the study hub for that domain.
- Explain a concept once in the note where it belongs. In other notes, link to the existing explanation instead of duplicating it.
- Prefer editing existing Markdown notes, links, and navigation over adding tooling, scripts, or structural churn.
- Preserve the repository's existing organization by domain unless the task explicitly requires a reorganization.

## Primary Artifacts

- `README.md`: folder index and directory description
- `00_overview.md`: study hub and ordered navigation for a domain
- concept notes: the main study content
- walkthrough notes: step-by-step operational or console guides
- image references: screenshots and image assets used by notes

## Before Finishing

- If you add or rename a note, update the relevant `00_overview.md`.
- If a folder's contents change materially, update that folder's `README.md`.
- If you edit a note, preserve the required structure defined in [README.md](README.md).
- If you edit a note, preserve or repair the navigation footer.
- If a concept is already documented elsewhere, link to the existing note instead of re-explaining it.
- Do not put study content into `README.md`.

## Subtree Policy

- Add a nested `AGENTS.md` only when a subtree needs materially different instructions from the repo root.
- Keep subtree files narrow. They should extend or override root behavior only for that subtree.
