---
tags:
  - tooling
created_at: 2026-04-17T00:00:00
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
---

# Navigation Rules

Rules for navigation headers and footers in study notes.

## 1. Navigation Hierarchy

Navigation is **associative, not linear**. Notes form a graph connected by inline links, shared tags, and explicit Related lists — not a prev/next sequence. Every concept note points:

- **Up**: to its domain overview (and from overview up to `home.md`).
- **Outward**: to related notes via inline links in prose and an explicit `Related` list in the footer.
- **By tag**: Obsidian's tag pane groups notes that share frontmatter tags.

Readers navigate by following their current line of thought, not a preset study order.

## 2. Concept Note Navigation

### 2.1. Header (After Frontmatter)

```md
---
tags:
  - domain
---

↑ [Overview](./00_{domain}_overview.md)

# Title
```

### 2.2. Footer (End of File)

```md
---
↑ [Overview](./00_{domain}_overview.md)

**Related:** [Title A](./a.md), [Title B](../other/b.md)
**Tags:** #tag1 #tag2
```

- **`↑ Overview`** — same target as the header, restated at the bottom so long notes don't need scrolling to go up.
- **`Related`** — explicit list of notes this one connects to conceptually. Derived from inline cross-references + anything conceptually adjacent. Links here may duplicate inline links; that's expected.
- **`Tags`** — mirror the frontmatter `tags` list as `#hash` inline tags so Obsidian's tag pane and graph view pick them up from the rendered view as well as YAML.

A note with zero related links is valid but flagged by [10_lint.md §2.2](10_lint.md) — consider whether an inbound link from another note is missing.

### 2.3. No Prev/Next

The legacy `← Previous | ... | Next →` footer has been removed. Ordered study is no longer the primary mode; readers jump by concept, not by index.

## 3. Overview Navigation

### 3.1. Domain Overview

Each domain has its own uniquely-named overview file: `00_{domain}_overview.md` (e.g., `ai/00_ai_overview.md`, `aws/00_aws_overview.md`).

Footer links up to parent overview:

```md
---
↑ [Parent Title](../home.md)
```

### 3.2. Root Overview

The root overview is named `home.md` (top of the hierarchy, no parent link).

### 3.3. Subdomain Pattern

A domain may contain subdomains (e.g., `aws/agentcore/`, `aws/compute/`). Navigation works three levels deep:

```
concept note (aws/compute/03_lambda.md)
  ↑ links to
subdomain overview (aws/compute/00_compute_overview.md)
  ↑ links to
parent overview (aws/00_aws_overview.md)
  ↑ links to
home.md (root)
```

**Naming:** subdomain overview is `{parent}/{subdomain}/00_{subdomain}_overview.md` (not prefixed with parent name).

**Numbering:** concept notes inside a subdomain are numbered per-subdomain (`01_*.md … NN_*.md`), not continuing from the parent.

**Parent overview's role:** when a domain has subdomains, `00_{domain}_overview.md` lists subdomain links (and brief descriptions), not individual concept notes. Individual notes are listed in each subdomain's own overview.

**Subdomain overview footer** links up to parent overview, not root:

```md
---
↑ [AWS](../00_aws_overview.md)
```

### 3.4. When To Split A Domain Into Subdomains

Split when **both** apply:
- The domain has ≥15 notes
- Notes fall into ≥2 distinct themes where intra-theme cross-links outnumber inter-theme ones

Don't split just because the number is big — split only when structure helps navigation.

## 4. README Files

READMEs do not have navigation footers. They are folder indexes only.

## 5. File Numbering

| File | Purpose |
|------|---------|
| `home.md` (root only) | Top-level study hub |
| `00_{domain}_overview.md` | Hub for a domain |
| `NN_filename.md` | Concept note (the `NN_` prefix is a stable identifier, not a study-order rank) |

The `NN_` prefix exists to keep filenames collision-free and sort-stable in file listings. It does **not** imply a study sequence — readers browse associatively via links, tags, and the Obsidian graph view. Numbers may skip or reorder without narrative consequence.

Files without numbers:
- `README.md` - Folder index
- `AGENTS.md` - Agent rules
- `CLAUDE.md` - Claude-specific rules
- `glossary.md` - Root-level glossary
- `log.md` - Root-level chronological log

## 6. Domain Layout

| Path | Content |
|------|---------|
| `ai/` | AI agents, LLM concepts |
| `aws/` | AWS services, grouped into subdomains by category |
| `aws/{subdomain}/` | Category subdomain (e.g., `compute/`, `storage/`, `ai/`, `agentcore/`) |
| `azure/` | Microsoft Azure services. Subdomains grow organically — create one only when the first note in it is written |
| `computing/` | CPU, GPU, virtualization |
| `gcp/` | Google Cloud services. Subdomains grow organically — create one only when the first note in it is written |
| `git/` | Git workflow |
| `networking/` | Protocols, OSI, DNS |
| `tooling/` | Dev tools, editors |
| `rules/` | Agent and human rules |
| `raw/` | Raw text inbox and processed source files |

## 7. When To Update Navigation

1. Adding a new note - update previous note's "Next" link
2. Removing a note - repair broken links
3. Renaming a note - update all references
4. Reordering notes - update all affected footers
