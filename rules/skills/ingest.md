# ingest

Ingest a raw source file into the study repo wiki.

**Argument:** `<source-slug>`

Follow the full flow in [rules/09_ingest.md](../09_ingest.md):

1. Locate the source file in `raw/` (try `raw/$ARGUMENTS*` and `raw/**/$ARGUMENTS*`). If the argument is empty, ask the user which file to ingest.
2. Read the source.
3. Summarize key takeaways to the user in 2-4 bullets and confirm scope before writing.
4. For each concept: grep existing notes; prefer update over create; split a note only if it would exceed ~150 lines or mix ≥2 themes.
5. On every touched note, append the source slug to the frontmatter `source:` list (create the field if absent).
6. Move the raw file from `raw/` to `raw/processed/`.
7. Append one entry to `log.md` summarizing what was touched.

Do not touch notes outside the scope confirmed in step 3. Do not commit raw source content.
