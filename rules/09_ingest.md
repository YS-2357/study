---
tags:
  - tooling
created_at: 2026-04-19T09:11:51
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
---

# Ingest Pipeline

How AI agents turn raw source material into structured study notes.

## 1. Trigger

Ingest runs **only when the user asks for it**. Two equivalent forms:

- `/ingest <source-name>` — slash command in `.claude/commands/ingest.md`
- Conversational: "ingest <name>", "process this", "read the file in raw/"

No auto-ingest. Agents do not watch `raw/` or batch-process uninvited.

## 2. Inputs

The `raw/` folder is the inbox. It is **gitignored** (sources are local-only) — only `raw/README.md` is tracked. Sources live in whichever form the user drops them:

| Type | Handling |
|------|----------|
| `.md`, `.txt`, `.csv`, `.log` | Read directly with Read tool |
| `.pdf` | Read with Read tool (use `pages` for >10-page PDFs) |
| Images (`.png`, `.jpg`) | Read directly (Claude is multimodal) |
| URLs (in a `.txt` file or typed in chat) | WebFetch |
| `.docx`, `.pptx`, audio | Ask the user for plain-text conversion first |

## 3. Flow

```
user drops file in raw/
        │
        ▼
user runs /ingest <name>
        │
        ▼
┌───────────────────────────────────────────┐
│ 1. Read the source                        │
│ 2. Discuss key takeaways with the user    │
│ 3. Grep existing notes for each concept   │
│ 4. Decide per-concept: update or create   │
│ 5. Update/create notes; add source: tag   │
│ 6. Move raw file to raw/processed/        │
│ 7. Append one entry to log.md             │
└───────────────────────────────────────────┘
```

### 3.1. Discuss Before Writing

After reading, summarize the takeaways to the user in 2-4 bullets and confirm scope before touching notes. This catches misreads early and lets the user redirect emphasis.

### 3.2. Update vs. Create

**Prefer update.** A new source usually refines or extends an existing concept; file it into the canonical note rather than spawning a parallel one.

Create a new note only when **both** apply:
- The concept does not exist in any current note (verified by grep).
- The concept fits an existing domain or warrants a new domain (see [02_navigation.md §3.4](02_navigation.md) and [07_scalability.md §6](07_scalability.md)).

### 3.3. Split When One Note Gets Too Big

Split an existing note into two when the update would make it:
- Longer than ~150 lines of body content, **or**
- Mix two distinct themes where intra-theme links would outnumber inter-theme links.

When splitting, follow [07_scalability.md §8](07_scalability.md) (sed-friendly renames).

## 4. Source Tracking

Every note that absorbs content from a source gets a `source:` field in its frontmatter. Multiple sources accumulate as a list.

```yaml
---
tags:
  - aws
  - serverless
created_at: 2026-04-17T14:30:00
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
source:
  - karpathy_llm_wiki_gist
  - aws_lambda_docs_2026-04
---
```

Rules:
- Use a short, stable, filename-safe slug (no spaces, lowercase, underscores).
- The source file may or may not exist under `raw/processed/` on any given PC — that's fine; the slug is the authoritative pointer.
- Append to the list on each ingest that touches the note. Don't overwrite existing sources.

## 5. After Processing

1. Move the raw file from `raw/` to `raw/processed/` locally (git-ignored, but keeps a local audit trail).
2. Append one entry to `log.md`:

   ```md
   ## [2026-04-19T09:11:51] ingest | karpathy_llm_wiki_gist
   - Touched: rules/09_ingest.md (new), rules/10_lint.md (new), rules/02_navigation.md
   - Decision: adopt associative navigation, drop prev/next
   ```

3. Let the existing auto-push hook commit and push each touched file individually (one file = one commit).

## 6. Multi-File Ingests

A single source can touch many notes. The auto-push hook commits per file, so a 10-note ingest produces 10 commits. That's expected and reviewable.

If conflicts are likely (e.g., another agent is editing the same domain), finish the ingest in one session rather than pausing mid-way.

## 7. What Not To Do

- Don't ingest without user request.
- Don't fabricate content to fill a section; if the source doesn't cover it, leave the section unchanged.
- Don't touch notes outside the source's scope ("while I'm here" refactors).
- Don't delete a source file from `raw/` — move it to `raw/processed/` so the user can verify.
- Don't commit raw source files (the gitignore prevents this; don't override).
