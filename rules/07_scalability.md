---
tags:
  - tooling
created_at: 2026-04-18T12:45:44
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
---

# Scalability Rules

The repo is designed so adding notes, subdomains, or renames lands without manual pain. Every concrete rule (naming, navigation, path conventions) exists to serve this goal. This file states the principle and the patterns that protect it.

## 1. Principle

**New content is addable without restructuring existing content. Renames and splits are sed-friendly, not hand-surgery.** If a proposed change requires editing dozens of files by hand, the design is wrong — fix the design before committing to the change.

## 2. Numbering Resets Per Subdomain

Every subdomain numbers its concept notes `01_*.md … NN_*.md` independently. Foundation has its own `01_`, compute has its own `01_`, and so on. The `NN_` prefix is a **stable identifier** — it keeps filenames unique and sort-stable; it does not imply a reading order (navigation is associative, see [02_navigation.md §1](02_navigation.md)).

Consequence: adding a new subdomain never forces renumbering of siblings, and skipping numbers is fine.

See [rules/02_navigation.md §3.3](02_navigation.md) for the subdomain pattern and [§5](02_navigation.md) for file numbering.

## 3. Hub Points Down, Concepts Point Up

| Level | Direction | Example |
|-------|-----------|---------|
| `home.md` (root) | points **down** to domain overviews | `[AWS](aws/00_aws_overview.md)` |
| `00_{domain}_overview.md` | points **down** to subdomain overviews or concept notes | `[Compute](compute/00_compute_overview.md)` or `[EC2](01_amazon_ec2.md)` |
| `00_{subdomain}_overview.md` | points **down** to concept notes, **up** to parent overview in footer | `↑ [AWS](../00_aws_overview.md)` |
| Concept note | points **up** to subdomain overview (header + footer), **outward** to Related notes via inline links and the footer list | `↑ [Overview](./00_compute_overview.md)` |

Consequence: adding a new concept = touch exactly the parent overview + README. Nothing upstream changes.

## 4. When To Split A Domain Into Subdomains

See [rules/02_navigation.md §3.4](02_navigation.md) — don't duplicate the threshold here.

Summary: split when **both** apply — ≥15 notes AND ≥2 distinct themes where intra-theme cross-links outnumber inter-theme ones.

## 5. No Single-File Subdomains

A subdomain must contain ≥2 notes. If a single note doesn't fit any existing subdomain and you can't name ≥2 peers that would form a new subdomain, **put it in the closest existing subdomain** — even if the fit is imperfect.

Why: single-file subdomains have low information density (one overview for one note is noise) and high maintenance cost (every directory adds a README + overview to keep in sync).

## 6. New Top-Level Domains

Existing domains are not catch-alls. Choose domain placement by the concept's long-term family, not by the nearest current folder.

A single note may start a new top-level domain when it represents a broad study area and you can name at least 3 plausible future sibling notes. If no future cluster is clear, place the material in `raw/` first instead of forcing it into an existing domain.

This exception applies only to top-level domains. Subdomains still need multiple notes; don't create a single-file subdomain.

## 7. Relative Paths Only

Never use absolute paths in notes. All cross-references use relative paths so the tree can be moved without breaking. See [rules/03_cross_linking.md §3.1](03_cross_linking.md) for the depth table.

Consequence: moving a whole subdomain under a new parent requires only fixing the links that leave the subtree — internal links survive unchanged.

## 8. Sed-Friendly Renames

When renaming a file across the repo:

```bash
git mv aws/OLD.md aws/new_subdomain/NEW.md
find . -name "*.md" -not -path "./.git/*" -print0 \
  | xargs -0 sed -i 's|aws/OLD\.md|aws/new_subdomain/NEW.md|g'
```

Two commands, any number of cross-references fixed. This works because:
- Every filename is unique repo-wide.
- Paths are relative with stable depth patterns.
- No HTML anchors, no absolute URLs, no alternate linking conventions.

Preserve this property when adding features. If a new tool (e.g., a TOC generator) depends on a different link format, add it alongside — don't replace the relative-path convention.

## 9. Automation Boundaries

The repo's hooks enforce scalability-safe conventions:

| Hook | Checks | File |
|------|--------|------|
| `pre-push-study-content` | ack on study-content changes | `.githooks/pre-push-study-content` |
| Codex pre-push | frontmatter present, note structure, footer format, security patterns | `.codex/hooks/pre-push` |
| Claude auto-push | stages only the touched `tool_input.file_path`, not the whole tree | `.claude/hooks/auto-push.sh` |

Don't add rules hooks can't enforce. If a convention can't be machine-checked, it will drift. When introducing a new rule, either teach the hook to check it or accept it as guidance-only (marked as such in the rule file).

## 10. Signals That It's Time To Reorganize

Watch for these and reorganize when ≥2 apply:

- A single domain has >15 concept notes (threshold from §4).
- A domain's `00_{domain}_overview.md` has three or more section headings grouping notes (`### Compute`, `### Storage`, etc.) — the groups are begging to be subdomains.
- Cross-references between specific note clusters within a domain outnumber references to the rest of the domain.
- `find` or tab-completion in the directory is slow or painful to scan.
- Cross-links within the domain cluster into disconnected subgraphs — Obsidian's graph view shows isolated islands sharing no bridges.

When you reorganize, **update the rules** if you discover a pattern that should become a convention. Rules evolve alongside the repo.
