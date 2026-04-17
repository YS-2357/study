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

↑ [Overview](00_overview.md)

# Title
```

### 2.2. Footer (End of File)

```md
---
← Previous: [Title](link) | [Overview](00_overview.md) | Next: [Title](link) →
```

### 2.3. Footer Variations

First note in sequence:
```md
---
[Overview](00_overview.md) | Next: [Title](link) →
```

Last note in sequence:
```md
---
← Previous: [Title](link) | [Overview](00_overview.md)
```

## 3. Overview Navigation

### 3.1. Domain Overview (00_overview.md)

Footer links up to parent overview:

```md
---
↑ [Parent Title](path/to/parent/00_overview.md)
```

### 3.2. Root Overview

The root `00_overview.md` is the top of the hierarchy and has no parent link.

### 3.3. Nested Domain Example

```
aws/agentcore/00_overview.md
↑ [Amazon Bedrock AgentCore](../32_amazon_bedrock_agentcore.md)
```

## 4. README Files

READMEs do not have navigation footers. They are folder indexes only.

## 5. File Numbering

| File | Purpose |
|------|---------|
| `00_overview.md` | Study hub for domain |
| `01_filename.md` | First concept note |
| `02_filename.md` | Second concept note |
| ... | Continue in study order |

Files without numbers:
- `README.md` - Folder index
- `AGENTS.md` - Agent rules
- `CLAUDE.md` - Claude-specific rules

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
| `docs/` | Agent and human rules |
| `raw/` | Raw source materials |

## 7. When To Update Navigation

1. Adding a new note - update previous note's "Next" link
2. Removing a note - repair broken links
3. Renaming a note - update all references
4. Reordering notes - update all affected footers
