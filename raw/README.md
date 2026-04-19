---
tags:
  - tooling
created_at: 2026-04-18T12:05:28
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
---

# raw

Raw source inbox for the ingest pipeline. **This folder is gitignored** — sources live here locally and are never pushed. Only this README is tracked.

## Purpose

Drop source material here that you want turned into structured study notes. The LLM does not watch this folder; it processes a file only when you ask.

## Usage

1. Save the source file somewhere under `raw/`. Any name is fine.
2. Run `/ingest <source-slug>` (or ask conversationally: "ingest X").
3. The LLM follows the pipeline in [../rules/09_ingest.md](../rules/09_ingest.md): reads the source, discusses takeaways, updates or creates notes, adds a `source:` frontmatter entry on every touched note, moves the source to `raw/processed/`, and appends a line to [../log.md](../log.md).
4. After ingest, the source file lives in `raw/processed/` as a local audit trail (still gitignored).

## Supported Input Types

| Type | Notes |
|------|-------|
| `.md`, `.txt`, `.csv`, `.log` | Read directly |
| `.pdf` | Use `pages` parameter for PDFs >10 pages |
| Images (`.png`, `.jpg`) | Claude reads directly |
| URLs | Put the URL in a `.txt` file, or paste in chat |
| `.docx`, `.pptx`, audio | Convert to plain text first |

## Why Gitignored

Sources are often heavy (PDFs, images, transcripts), copyrighted, or personal. Syncing them across PCs is usually unwanted. The `source:` frontmatter field on each note carries the reference — the file itself may or may not exist on any given PC.
