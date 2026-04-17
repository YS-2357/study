# Glossary Subtree Guide

## Scope

Overrides the root note structure rule for all files under `glossary/`.

## Format

- All terms live in a single `glossary.md` as an alphabetically sorted Markdown table.
- Do not create per-term note files.
- Do not apply the standard note structure (`## What It Is`, `## How It Works`, etc.) here.
- No navigation footer is required in `glossary.md`.

## Table Columns

| Column | Content |
|--------|---------|
| Term | The abbreviation or short form |
| Full Name | The expanded name |
| Definition | One sentence — what it is, not how it works |
| Note | Inline link to the canonical note in this repo, or `—` if none exists |

## Editing Rules

- Keep rows sorted A–Z by Term.
- One row per term. Do not add sub-rows or nested tables.
- If a dedicated note exists elsewhere in the repo, always link it in the Note column.
- When a new note is created for a term already in the glossary, update the Note column to link it.
