---
name: ocr
description: Extract text from local raw image folders into local raw Markdown drafts. Use when Codex needs to OCR screenshots, slide photos, scanned pages, or image batches under raw/ before later ingest, while keeping event-specific scripts/configs and outputs local-only.
---

# OCR

Use the canonical workflow in `rules/skills/ocr.md` and the full procedure in `rules/11_ocr.md`.

Before running OCR:

- Run `git pull --ff-only origin main`.
- Locate the raw image folder under `raw/`.
- Confirm `uv`, `.venv`, Python packages from `requirements.txt`, and Tesseract are available.
- Confirm needed Tesseract languages with `tesseract --list-langs`.

While working:

- Use `scripts/ocr_images_to_markdown.py` as the generic tracked script.
- Run a 3-5 image sample before processing a large folder.
- Prefer `--start-time`, `--end-time`, `--limit`, `--skip-empty`, and `--skip-low-confidence` for controllable OCR batches.
- Put source-specific session maps, temporary scripts, caches, and OCR output under `raw/`.
- Do not commit raw images or raw OCR output.
- Do not hardcode a single event's schedule or speakers into tracked scripts.

After OCR:

- Report the raw OCR Markdown path and basic quality counts.
- Discard one-time helpers under `raw/` when they are no longer needed.
- Use the ingest skill only after the user asks to convert OCR output into study notes.
