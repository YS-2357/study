---
tags:
  - tooling
created_at: 2026-04-17T00:00:00
updated_at: 2026-04-19T09:11:51
recent_editor: CLAUDE
---

# Note Structure

Rules for formatting study notes in this repository.

## 1. Required Sections

Every concept note has these sections in order. Use the headings verbatim — no numeric prefixes, no renaming:

```md
# Title

## What It Is
(1-2 sentence definition - REQUIRED)

## Analogy
(One concrete mental model - REQUIRED)

## How It Works
(Mechanics, steps, procedures - REQUIRED)

## Example
(One concrete, small example - REQUIRED)

## Why It Matters
(Practical relevance - REQUIRED)
```

### 1.1. Section Rules

- `What It Is` - Required, 1-2 sentence definition
- `Analogy` - Required, 1-3 sentences mapping the concept to something familiar. If no clean analogy fits, write one sentence stating why and move on — don't force a misleading one.
- `How It Works` - Required, mechanics / steps / procedures. For notes where there's nothing mechanical to explain, write one sentence stating that and move on.
- `Example` - Required, concrete and small
- `Why It Matters` - Required

### 1.2. Additional Sections

Extra `##` sections allowed between required sections when content warrants:
- `## Name` - Etymology or naming context
- `## Prerequisites` - Complex setup requirements

## 2. Heading Levels

| Level | Use |
|-------|-----|
| `#` | Note title only (one per file) |
| `##` | Major sections. Use the section names verbatim (`## What It Is`, not `## 1. What It Is`) |
| `###` | Subsections inside a major section |
| `####` | Never use - split the note instead |

## 3. Frontmatter

Every note begins with YAML frontmatter:

```yaml
---
tags:
  - aws
  - serverless
created_at: 2026-04-17T14:30:00
updated_at: 2026-04-17T15:45:00
recent_editor: CLAUDE
---
```

### 3.1. Frontmatter Fields

| Field | Format | Rule |
|-------|--------|------|
| `tags` | lowercase, hyphen-separated | Required, min 1 tag |
| `created_at` | `YYYY-MM-DDTHH:MM:SS` (KST, UTC+9) | Set once on creation. Not auto-corrected |
| `updated_at` | `YYYY-MM-DDTHH:MM:SS` (KST, UTC+9) | AI must update on every edit. Auto-corrected by PostToolUse hook |
| `recent_editor` | `CLAUDE`, `CODEX`, `KIRO`, `HUMAN` | AI must set on every edit |
| `source` | list of slugs | Optional. Ingested source pointers — see [09_ingest.md §4](09_ingest.md) |

**KST enforcement:** All timestamps use Korean time (UTC+9). Get the current stamp with plain `date +"%Y-%m-%dT%H:%M:%S"` — **do not** use `TZ=Asia/Seoul date`, which silently returns UTC on Git Bash for Windows. The `updated_at` field is auto-corrected after every Write/Edit by `.claude/hooks/normalize-timestamp.sh`, so minor drift from real time is fixed automatically; `created_at` is not corrected and must be set correctly at creation time.

**Source tracking:** When a note absorbs content from a raw source, append a short filename-safe slug to the `source:` list. The slug points to a file that may or may not exist in `raw/processed/` on any given PC — the slug itself is the authoritative pointer, not the file. See [09_ingest.md](09_ingest.md).

### 3.2. Tags

- Use lowercase, hyphen-separated tags from the taxonomy below
- Assign all applicable tags — cross-domain notes carry multiple (e.g., `ai` + `aws`)
- Add a new tag only if no existing tag fits; if added, update this taxonomy
- Tags power Obsidian's graph view, tag pane, and cross-domain search

#### Taxonomy

| Tag | Covers | Example notes |
|-----|--------|---------------|
| `ai` | AI/ML, LLMs, agents, attention, KV cache | ai/ domain, Bedrock notes |
| `aws` | AWS services in general | All cloud/aws/ notes |
| `computing` | CPU, GPU, virtualization, caching, storage | computing/ domain |
| `container` | ECR, Docker, Lambda container images | Fargate, ECR, Lambda containers |
| `database` | RDS, DynamoDB, Aurora, ElastiCache | cloud/aws/ DB notes |
| `git` | Git workflow, staging, tracking | git/ domain |
| `infrastructure` | VPC, regions, AZs, subnets, CDK | VPC, CDK, Region notes |
| `ml` | SageMaker, Bedrock, model training | Bedrock, SageMaker notes |
| `monitoring` | CloudWatch, observability | CloudWatch note |
| `networking` | Protocols, OSI, DNS, HTTP, proxies | networking/ domain |
| `security` | IAM, Shield, WAF, auth, secrets | IAM, WAF, Shield notes |
| `serverless` | Lambda, Fargate, API Gateway | Lambda, API GW, Mangum notes |
| `storage` | S3, EFS, EBS | Storage notes |
| `tooling` | Dev tools, editors, terminal setup | tooling/ domain, CDK, boto3 |

## 4. Lists

| Type | Use |
|------|-----|
| `-` bullets | Unordered facts, properties, options |
| `1.` numbers | Ordered steps or priority within a section |

Indent nested items with 2 spaces.

## 5. Emphasis

| Format | Use |
|--------|-----|
| `**bold**` | Key terms, important warnings |
| `*italic*` | Light emphasis, external work titles |
| `` `code` `` | Commands, filenames, env vars, values |

## 6. Tables

- Use for comparisons, option sets, structured data
- Every table needs header row and separator row

## 7. What Not To Use

- No `---` horizontal rules except before navigation footer
- No `> Note:`, `> Warning:` - only `> **Tip:**`
- No raw HTML
- No emoji unless user requests it
