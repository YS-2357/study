---
tags:
  - tooling
created_at: 2026-04-18T12:05:28
updated_at: 2026-04-18T12:05:28
recent_editor: CODEX
---

# raw

Raw text inbox for study-note source material. Put unsorted raw text here; AI agents decide what is worth turning into structured notes.

## Files

- `README.md`: This file.
- `processed/`: Raw text files after useful content has been converted into notes.
- `images/`: Legacy/optional image staging folder.
- `documents/`: Legacy/optional document staging folder.
- `markdown/`: Legacy/optional markdown staging folder.
- `extracted/`: Legacy/optional extracted-text staging folder.

## Workflow

1. Add raw text files directly under `raw/`.
2. AI agents read text files only.
3. Agents extract clear standalone study concepts and skip weak fragments or duplicates.
4. Agents search existing notes first and update a canonical note when one fits.
5. Agents use web search before creating new notes and cite reliable official or primary sources inline.
6. Agents create notes in the proper domain, creating a new domain only when no existing domain fits.
7. Agents move handled raw files into `raw/processed/`.

## Text Files Only

Agents process readable text files such as `.txt`, `.md`, `.csv`, `.log`, and extensionless plain-text files. Binary files, images, PDFs, DOCX, PPTX, and other non-text files are ignored unless the user explicitly asks for extraction.
