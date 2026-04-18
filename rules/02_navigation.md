---
tags:
  - tooling
created_at: 2026-04-17T00:00:00
updated_at: 2026-04-18T12:24:18
recent_editor: CLAUDE
---

# Navigation Rules

Rules for navigation headers and footers in study notes.

## 1. Navigation Hierarchy

Every file participates in a two-level navigation hierarchy:
- **Up**: Link to parent overview
- **Lateral**: Links to previous/next notes in sequence

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
← Previous: [Title](link) | [Overview](./00_{domain}_overview.md) | Next: [Title](link) →
```

### 2.3. Footer Variations

First note in sequence:
```md
---
[Overview](./00_{domain}_overview.md) | Next: [Title](link) →
```

Last note in sequence:
```md
---
← Previous: [Title](link) | [Overview](./00_{domain}_overview.md)
```

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
| `00_{domain}_overview.md` | Study hub for a domain |
| `01_filename.md` | First concept note |
| `02_filename.md` | Second concept note |
| ... | Continue in study order |

Files without numbers:
- `README.md` - Folder index
- `AGENTS.md` - Agent rules
- `CLAUDE.md` - Claude-specific rules
- `glossary.md` - Root-level glossary

## 6. Domain Layout

| Path | Content |
|------|---------|
| `ai/` | AI agents, LLM concepts |
| `aws/` | AWS service notes (flat structure, 01-50) |
| `aws/agentcore/` | Bedrock AgentCore deep-dive |
| `computing/` | CPU, GPU, virtualization |
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
