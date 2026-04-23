---
tags:
  - tooling
created_at: 2026-04-17T00:00:00
updated_at: 2026-04-23T23:41:19
recent_editor: CODEX
---

# Cross-Linking Rules

Rules for linking between notes and to the glossary.

## 1. Core Principles

1. Explain a concept once in its canonical note by default
2. Link from other notes instead of duplicating unless a domain-specific sibling note is justified
3. Link inline where concept is mentioned
4. No separate "References" or "See Also" sections

### 1.1. Domain-Specific Sibling Notes

Notes with overlapping content may exist under different domains when each note answers a different reader question. The overlap must be intentional, not accidental copy-paste.

Example: Amazon Kiro can have an AWS-facing note under `cloud/aws/` and an AI-agent-facing note under `ai/`.

Rules:
- State the domain lens clearly in each sibling note.
- Repeat only the minimum shared facts needed for the local explanation.
- Cross-link sibling notes on first mention so readers can jump between lenses.
- Prefer one canonical note plus links when the second domain would add no distinct perspective.

## 2. First Mention Rule

On first mention of a concept with a dedicated note:
- Add inline Markdown link
- Do not repeat link on subsequent mentions in same file

### 2.1. Example

```md
The [Lambda](../cloud/aws/compute/03_aws_lambda.md) function uses
an IAM role. Lambda automatically handles scaling.
```

Second mention of "Lambda" has no link.

## 3. Cross-Domain Links

Links between domains are encouraged when they help the reader:

| From | To | Example |
|------|----|---------|
| `ai/` | `computing/` | Agent note linking to API interface |
| `computing/` | `cloud/aws/database/` | Cache note linking to ElastiCache |
| `cloud/aws/compute/` | `cloud/aws/ai/agentcore/` | Lambda note linking to AgentCore |

### 3.0. Cross-Cloud Equivalents

A service note in `cloud/aws/`, `gcp/`, or `azure/` that has a direct counterpart in another cloud should link the equivalent on first mention. Example, in `cloud/aws/compute/01_amazon_ec2.md`:

> EC2 is AWS's virtual machine service — equivalent to Compute Engine on GCP and Virtual Machines on Azure once those counterpart notes exist.

Rules:
- Link **only when the equivalent note actually exists.** Don't create stub notes just to satisfy links.
- Apply to **new notes only.** Don't retrofit existing notes in bulk — add the link the next time you're editing that note for another reason.
- Skip when there's no clean 1:1 mapping (e.g., managed services that differ substantially in scope).

### 3.1. Relative Path Rules

| Target is in… | Path prefix |
|---------------|-------------|
| Same folder | `./` (or bare filename) |
| Sibling subdomain (same parent) | `../{subdomain}/` |
| Different top-level domain | `../../{domain}/` or `../{domain}/` from a top-level note |
| Root `home.md` or `glossary.md` | depth-appropriate `../…/` |

Examples:
```md
Same folder:      Auto Scaling -> ./02_auto_scaling.md
Sibling subdir:   S3 -> ../storage/01_amazon_s3.md
Across domains:   OSI Model -> ../../networking/03_osi_model.md
Root glossary:    VPC -> ../../glossary.md
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
The [VPC](../cloud/aws/foundation/04_amazon_vpc.md) contains multiple subnets.
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

### 5.1. Glossary Capture Rule

Add an abbreviation to [glossary.md](../glossary.md) when it appears in tracked notes, or when it appears in chat and is likely to recur in future notes.

Do not add common casual abbreviations such as `e.g.`, `etc.`, or one-off chat shorthand unless they become study terms.

When adding a new abbreviation to a note, use `Full Name (ABBR)` on first use and make sure `glossary.md` has an entry.

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
