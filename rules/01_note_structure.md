---
tags:
  - tooling
created_at: 2026-04-17T00:00:00
updated_at: 2026-04-18T14:00:00
recent_editor: CLAUDE
---

# Note Structure

Rules for formatting study notes in this repository.

## 1. Required Sections

Every concept note must have these sections in order:

```md
# Title

## 1. What It Is
(1-2 sentence definition - REQUIRED)

## 2. Analogy
(Optional - only if it genuinely helps understanding)

## 3. How It Works
(Mechanics, steps, procedures)

## 4. Example
(One concrete, small example - REQUIRED)

## 5. Why It Matters
(Practical relevance - REQUIRED)
```

### 1.1. Section Rules

- `What It Is` - Required, 1-2 sentence definition
- `Analogy` - Optional, include only if genuinely helpful
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
| `##` | Major sections (numbered: 1., 2., 3.) |
| `###` | Subsections (numbered: 1.1., 1.2.) |
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
| `created_at` | `YYYY-MM-DDTHH:MM:SS` | Set once on creation |
| `updated_at` | `YYYY-MM-DDTHH:MM:SS` | AI must update on every edit |
| `recent_editor` | `CLAUDE`, `CODEX`, `KIRO`, `HUMAN` | AI must set on every edit |

### 3.2. Tags

- Use lowercase, hyphen-separated tags from the taxonomy below
- Assign all applicable tags — cross-domain notes carry multiple (e.g., `ai` + `aws`)
- Add a new tag only if no existing tag fits; if added, update this taxonomy
- Tags power Obsidian's graph view, tag pane, and cross-domain search

#### Taxonomy

| Tag | Covers | Example notes |
|-----|--------|---------------|
| `ai` | AI/ML, LLMs, agents, attention, KV cache | ai/ domain, Bedrock notes |
| `aws` | AWS services in general | All aws/ notes |
| `computing` | CPU, GPU, virtualization, caching, storage | computing/ domain |
| `container` | ECR, Docker, Lambda container images | Fargate, ECR, Lambda containers |
| `database` | RDS, DynamoDB, Aurora, ElastiCache | aws/ DB notes |
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
| `1.` numbers | Ordered steps, priority, study order |

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
