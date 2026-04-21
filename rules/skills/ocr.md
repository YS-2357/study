# ocr

Manually extract readable text from raw local images into a raw Markdown draft.

**Argument:** `<raw-image-folder>`

Follow the full flow in [rules/11_ocr.md](../11_ocr.md):

1. Locate the image folder under `raw/`.
2. Confirm the user-selected scope, such as a session, time window, or small image batch.
3. Open each image directly and read the visible text.
4. Process only a small batch at a time, usually 3-5 images.
5. Extract slide titles, prominent text, key bullets, and reliable numbers.
6. Mark uncertain text as `[판독 불가]`; do not guess.
7. Keep extraction output under `raw/` so it remains local-only.
8. Summarize quality, output location, and the next continuation point to the user.
9. Treat later note creation/update as a separate ingest step.

One-time extraction helpers under `raw/` may be discarded after the final raw Markdown exists.
