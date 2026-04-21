---
tags:
  - tooling
created_at: 2026-04-21T00:00:00
updated_at: 2026-04-21T00:00:00
recent_editor: CODEX
---

# OCR

How agents extract readable text from local raw images into local Markdown drafts.

## 1. Trigger

Image text extraction runs **only when the user asks**. It is a raw-source preparation step, not an ingest.

Use this workflow when the user provides screenshots, slide photos, scanned pages, or image folders under `raw/` and wants text extracted before later note cleanup.

## 2. Output Location

Write extraction outputs under `raw/` unless the user explicitly asks for a tracked note.

Rules:
- `raw/` remains local-only and gitignored.
- Extraction output is raw evidence, not a polished concept note.
- Do not commit raw images, raw extraction output, or event-specific session maps.
- After extracted text is processed into notes, one-time configs, caches, and intermediate files under `raw/` may be deleted or moved to `raw/processed/`.

## 3. Method

Prefer direct agent visual reading over automated OCR engines.

Rules:
- Open each image directly with the image viewer tool.
- Process a small batch, usually 3-5 images, then stop or leave a clear continuation point.
- Extract only text that is visible enough to be trusted.
- Preserve the image filename and timestamp when available.
- Keep the user's requested scope strict. If the user asks for one session, ignore other sessions.
- Do not use a tracked one-off script for event-specific extraction.

## 4. Draft Format

Use this shape for raw extraction drafts:

```markdown
# <event/session> Manual Extract

## Source
- Images: `raw/<image-folder>`
- Scope: <session/time window>
- Method: Agent visual reading, not engine OCR

## Batch 1 - <time range>

### <image-file>
- 판독 상태: 양호 / 부분 판독 / 낮음
- 제목:
- 보이는 핵심 문구:
  - ...
- 비고:
  - ...
```

## 5. Quality Gate

Do not process a large image folder in one run.

Recommended flow:

1. Select a specific session, time window, or 3-5 image batch.
2. Open each image and manually transcribe slide titles, prominent text, key bullets, and reliable numbers.
3. Mark uncertain content as `[판독 불가]` instead of guessing.
4. Add a short batch review with readable themes, low-quality images, and next continuation point.
5. Continue to the next batch only when requested or when the user has approved the batch plan.

## 6. Relationship To Ingest

Image text extraction does not update study notes by itself. After extraction:

1. Review the raw Markdown with the user.
2. Decide which concepts are worth ingesting.
3. Follow [09_ingest.md](09_ingest.md) for note updates, source frontmatter, processed movement, and `log.md`.

## 7. Skill

The shared skill entry is [skills/ocr.md](skills/ocr.md). Each agent should implement its own native version from that shared procedure.
