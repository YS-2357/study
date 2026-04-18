---
tags:
  - tooling
created_at: 2026-04-17T00:00:00
updated_at: 2026-04-18T18:55:00
recent_editor: CODEX
---

# Cross-Linking Rules

Rules for linking between notes and to the glossary.

## 1. Core Principles

1. Explain a concept once in its canonical note
2. Link from other notes instead of duplicating
3. Link inline where concept is mentioned
4. No separate "References" or "See Also" sections

## 2. First Mention Rule

On first mention of a concept with a dedicated note:
- Add inline Markdown link
- Do not repeat link on subsequent mentions in same file

### 2.1. Example

```md
The [Lambda](../aws/compute/03_aws_lambda.md) function uses
an IAM role. Lambda automatically handles scaling.
```

Second mention of "Lambda" has no link.

## 3. Cross-Domain Links

Links between domains are encouraged when they help the reader:

| From | To | Example |
|------|----|---------|
| `ai/` | `computing/` | Agent note linking to API interface |
| `computing/` | `aws/database/` | Cache note linking to ElastiCache |
| `aws/compute/` | `aws/ai/agentcore/` | Lambda note linking to AgentCore |

### 3.1. Relative Path Rules

| Target is in… | Path prefix |
|---------------|-------------|
| Same folder | `./` (or bare filename) |
| Sibling subdomain (same parent) | `../{subdomain}/` |
| Different top-level domain | `../../{domain}/` or `../{domain}/` from a top-level note |
| Root `home.md` or `glossary.md` | depth-appropriate `../…/` |

Examples:
```md
Same folder:      [Auto Scaling](./02_auto_scaling.md)
Sibling subdir:   [S3](../storage/01_amazon_s3.md)
Across domains:   [OSI Model](../../networking/03_osi_model.md)
Root glossary:    [VPC](../../glossary.md)
```

## 4. Glossary Links

### 4.1. When To Link

Link to glossary entries for:
- Abbreviations on first use
- Domain-specific terms readers may not know

### 4.2. How To Link

```md
The [VPC](../glossary.md) contains multiple subnets.
```

Or link to the full note if one exists:
```md
The [VPC](../aws/foundation/04_amazon_vpc.md) contains multiple subnets.
```

### 4.3. Glossary Note Column

When a dedicated note exists for a term:
- Update glossary's "Note" column with link
- Prefer linking to the note, not the glossary

## 5. Abbreviation Format

First use: full name (abbreviation), then abbreviation only

```md
Cloud Development Kit (CDK) lets you define infrastructure.
CDK supports Python and TypeScript.
```

## 6. When Editing Notes

### 6.1. Scan For Missing Links

Check notes in same and adjacent domains for:
- Concepts mentioned but not linked
- Terms that have canonical notes elsewhere

### 6.2. When Creating New Notes

Search existing notes for:
- Unlinked mentions of the new concept
- Add backward links to the new note

## 7. Link Maintenance

### 7.1. After Renaming

Update all references to the renamed file.

### 7.2. After Moving

Update all references to the new path.

### 7.3. After Deleting

Remove or update links to deleted notes.

## 8. Validation Before Commit

Before committing link changes:
- Run an internal Markdown link check across all `.md` files
- Include image links in the check
- Ignore placeholder examples only inside rule docs
- Scan for malformed relative paths such as `././`, stale renamed filenames, and over-deep `../../../` paths
- Fix repeated same-target links in body text; navigation/footer links may repeat

## 9. What Not To Do

- No separate "References" section at end of note
- No "See Also" section
- No repeated links to same concept in one file
- No links to external URLs for concepts in this repo
