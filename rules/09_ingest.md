---
tags:
  - tooling
created_at: 2026-04-19T09:11:51
updated_at: 2026-04-24T08:47:57
recent_editor: CODEX
---

# Ingest Pipeline

How AI agents turn raw source material into structured study notes.

## 1. Trigger

Ingest runs only when the user asks for it.

- `/ingest <source-name>`
- Conversational equivalents such as "ingest this", "process this", or "read the file in raw/"

No auto-ingest. Agents do not watch `raw/` or batch-process uninvited.

## 2. Inputs

The `raw/` folder is the inbox. It is gitignored, so only `raw/README.md` is tracked.

| Type | Handling |
|------|----------|
| `.md`, `.txt`, `.csv`, `.log` | Read directly |
| `.pdf` | Read directly when possible |
| Images (`.png`, `.jpg`) | Read directly or extract manually |
| URLs | Web fetch or browser tools |
| `.docx`, `.pptx`, audio | Ask for plain-text conversion first if direct reading is not reliable |

## 3. Flow

1. Read the source.
2. Discuss the key takeaways with the user in 2-4 bullets before writing.
3. Search existing notes for each concept.
4. Decide per concept whether to update or create.
5. Update or create notes and add `source:` frontmatter slugs.
6. Move the raw source to `raw/processed/`.
7. Append one entry to `log.md`.

### 3.1. Discuss Before Writing

After reading, summarize the takeaways to the user in 2-4 bullets and confirm scope before touching notes.

### 3.2. Update vs. Create

Prefer update. Create a new note only when both are true:
- The concept does not exist in any current note
- The concept fits an existing domain or clearly warrants a new one

### 3.3. Split When One Note Gets Too Big

Split an existing note when the update would make it:
- longer than about 150 lines of body content, or
- mix two distinct themes where intra-theme links would outnumber inter-theme links

## 4. Source Tracking

Every touched note that absorbs source material gets a `source:` field in frontmatter. Multiple sources accumulate as a list.

Rules:
- Use a short, stable, filename-safe slug
- The slug is the authoritative pointer even if the raw source is only present on one machine
- Append to the list; do not overwrite existing sources

## 5. After Processing

1. Move the raw file from `raw/` to `raw/processed/` locally.
2. Append one entry to `log.md`.
3. Commit and push only when the task explicitly includes Git delivery.

## 6. Multi-File Ingests

A single source can touch many notes. That may produce one commit or several commits depending on the task boundary. Keep the commits coherent and reviewable rather than forcing a per-file push pattern.

If conflicts are likely, finish the ingest in one session rather than pausing mid-way.

## 7. What Not To Do

- Do not ingest without user request
- Do not fabricate content to fill a section
- Do not touch notes outside the confirmed source scope
- Do not delete a source file from `raw/`; move it to `raw/processed/`
- Do not commit raw source files
