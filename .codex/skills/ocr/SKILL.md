---
name: ocr
description: Manually extract readable text from local raw image folders into raw Markdown drafts. Use when Codex needs to inspect screenshots, slide photos, scanned pages, or image batches under raw/ before later ingest, while keeping outputs local-only.
---

# OCR

Use the canonical workflow in `rules/skills/ocr.md` and the full procedure in `rules/11_ocr.md`.

Before extracting text:

- Run `git pull --ff-only origin main`.
- Locate the raw image folder under `raw/`.
- Confirm the user-selected scope, such as a session, time window, or small image batch.
- Prefer direct visual reading with `view_image`; do not default to engine OCR.

While working:

- Process images in small batches, usually 3-5 images.
- Extract slide titles, prominent text, key bullets, and numbers that are visibly reliable.
- Mark uncertain text as `[판독 불가]` or omit it rather than inventing missing words.
- Put manual extraction drafts under `raw/`.
- Do not commit raw images or raw extraction output.

After extraction:

- Report the raw Markdown path, processed image range, and any low-quality images.
- Continue with the next batch only when requested or when the user has already approved that batch plan.
- Use the ingest skill only after the user asks to convert extracted text into study notes.
