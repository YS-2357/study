# ocr

Extract text from raw local images into a raw Markdown draft.

**Argument:** `<raw-image-folder>`

Follow the full flow in [rules/11_ocr.md](../11_ocr.md):

1. Locate the image folder under `raw/`.
2. Confirm OCR tooling is available: `uv`, `.venv`, Python packages from `requirements.txt`, and Tesseract with needed languages.
3. Use the generic tracked OCR script when possible.
4. Run a small sample first using time-window and limit options; do not batch OCR a large folder until the sample is readable.
5. Use `--skip-empty` and `--skip-low-confidence` to keep noisy OCR out of the draft.
6. Keep event-specific session maps, temporary scripts, and OCR output under `raw/` so they remain local-only.
7. Do not hardcode one event's sessions into tracked scripts or rules.
8. Summarize OCR quality and output location to the user.
9. Treat later note creation/update as a separate ingest step.

One-time OCR helpers under `raw/` may be discarded after the final raw OCR Markdown exists.
