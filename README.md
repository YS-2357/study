# study
Study materials organized by subject and topic.

- `README.md`: Overview of the `study/` folder and its direct contents.
- `aws/`: AWS study materials grouped by level and purpose.
- `computing/`: General computing study notes.
- `networking/`: Networking study notes.

## Operating Rules

### Purpose

- `study/` is the reusable knowledge workspace for notes, walkthroughs, reference material, and structured study artifacts.
- Do not use `study/` as a general scratch area for temporary files with no long-term value.

### Top-level structure

- Top-level directories are organized by domain.
- New top-level folders should represent stable domains, not short-lived tasks, dates, or one-off experiments.
- Subtrees may choose their own local organizing model if the subtree README explains it clearly.

### Source of truth

- This root `README.md` is the canonical rule document for the `study/` repo.
- Child `README.md` files may add tighter local rules for their subtree, but they should not weaken the root policy.
- `.gitignore` is the enforcement layer for anything designated local-only.

### Artifact classification

- Always track reusable notes, glossaries, walkthroughs, diagrams, indexes, and documentation that should remain part of the study corpus.
- Never track private material, rehearsal content, credentials, local exports, recordings, or audience-specific presentation prep.
- Review before tracking screenshots, generated assets, large binaries, and third-party material with unclear reuse value.

### Naming and placement

- Use stable, semantic folder names.
- Use date-based filenames only when the document is intentionally time-specific, such as rehearsal logs or session notes.
- Keep one reusable concept per file when possible.
- Put new material in the most specific existing subtree that already fits instead of creating parallel ad hoc folders.

### Working flow

- Create new material in the intended subtree first.
- Decide whether it is tracked or local-only before adding it to Git.
- If a new tracked subtree is introduced, add or update its `README.md` immediately.
- Before commit, confirm that file names, placement, and Git status match these rules.

## Local-only areas

- `aws/101/ppt/` contains local presentation practice materials and is excluded from Git.
- `aws/201/ppt/` is also kept as a local-only presentation workspace.
- `aws/certificate/` contains private certification materials and is excluded from Git.
