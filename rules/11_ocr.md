---
tags:
  - tooling
created_at: 2026-04-21T00:00:00
updated_at: 2026-04-21T00:00:00
recent_editor: CODEX
---

# OCR

How agents extract text from local raw images into local Markdown drafts.

## 1. Trigger

OCR runs **only when the user asks**. It is a raw-source preparation step, not an ingest.

Use OCR when the user provides screenshots, slide photos, scanned pages, or image folders under `raw/` and wants text extracted before later note cleanup.

## 2. Output Location

Write OCR outputs under `raw/` unless the user explicitly asks for a tracked note.

Rules:
- `raw/` remains local-only and gitignored.
- OCR output is raw evidence, not a polished concept note.
- Do not commit raw images, raw OCR output, or event-specific session maps.
- After OCR is processed into notes, one-time scripts, configs, caches, and intermediate files under `raw/` may be deleted or moved to `raw/processed/`.

## 3. Environment

Use repo-local Python packages and system Tesseract:

```powershell
winget install astral-sh.uv
winget install UB-Mannheim.TesseractOCR
uv venv .venv --python 3.12
uv pip install -r requirements.txt
tesseract --version
tesseract --list-langs
```

For Korean/English sources, `tesseract --list-langs` should include `kor` and `eng`.
If `kor` is missing, place `kor.traineddata` under ignored `.ocr-cache/tessdata/`, copy `eng.traineddata` there too, and pass `--tessdata-dir ".ocr-cache/tessdata"` to the OCR script.

## 4. Generic OCR Script

The tracked script must stay generic:

```powershell
.venv\Scripts\python.exe scripts\ocr_images_to_markdown.py `
  "raw\<image-folder>" `
  --output "raw\<ocr-output>.md" `
  --title "<OCR title>" `
  --lang "kor+eng" `
  --tessdata-dir ".ocr-cache\tessdata" `
  --start-time "11:30" `
  --end-time "11:40" `
  --limit 5 `
  --psm 11 `
  --skip-empty `
  --skip-low-confidence
```

If a source needs session grouping, place a local JSON map under `raw/` and pass it with `--sessions`.

Example shape:

```json
{
  "sessions": [
    {"group": "Keynote", "title": "Opening", "start": "10:00", "end": "10:15"}
  ]
}
```

Do not hardcode event names, speaker names, or session times in tracked scripts. Put those details in raw-local configs or temporary raw-local scripts.

## 5. Quality Gate

Do not OCR a large image folder in one run until a sample passes review.

Recommended flow:

1. Run 3-5 images from one time window with `--limit`.
2. Open the raw OCR output and confirm that slide titles and key bullets are readable.
3. Use `--skip-empty` and `--skip-low-confidence` so bad images do not flood the Markdown with noise.
4. Use `--psm 11` for sparse slide photos; try `--psm 6` for clean document-like screenshots.
5. Process only useful time windows. Skip stage, audience, hallway, and distant screen photos when OCR quality is poor.
6. If Tesseract output is still unreadable on clear slide photos, try different preprocessing/page segmentation settings or evaluate another OCR engine before running the full folder.

## 6. Relationship To Ingest

OCR does not update study notes by itself. After OCR:

1. Review the raw OCR Markdown with the user.
2. Decide which concepts are worth ingesting.
3. Follow [09_ingest.md](09_ingest.md) for note updates, source frontmatter, processed movement, and `log.md`.

## 7. Skill

The shared skill entry is [skills/ocr.md](skills/ocr.md). Each agent should implement its own native version from that shared procedure.
