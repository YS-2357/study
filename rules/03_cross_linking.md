---
tags:
  - tooling
created_at: 2026-04-17T00:00:00
updated_at: 2026-04-18T12:00:00
recent_editor: CLAUDE
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
The [Lambda](../aws/08_aws_lambda.md) function uses
an IAM role. Lambda automatically handles scaling.
```

Second mention of "Lambda" has no link.

## 3. Cross-Domain Links

Links between domains are encouraged when they help the reader:

| From | To | Example |
|------|----|---------|
| `ai/` | `computing/` | Agent note linking to API interface |
| `computing/` | `aws/` | Cache note linking to ElastiCache |
| `aws/` | `aws/agentcore/` | Bedrock note linking to AgentCore subtree |

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
The [VPC](../aws/04_amazon_vpc.md) contains multiple subnets.
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

## 8. What Not To Do

- No separate "References" section at end of note
- No "See Also" section
- No repeated links to same concept in one file
- No links to external URLs for concepts in this repo
