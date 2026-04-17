# Study Agent Guide

This file provides shared guidance to coding agents working in this repository.

## Scope

These instructions apply to the entire `study/` repository unless a deeper `AGENTS.md` or `CLAUDE.md` overrides them for a subtree.

## Source Of Truth

- Follow the detailed note-format and README standards in [README.md](README.md).
- Use this file as the compact operating guide for agents working in this repo.

## Sources

- Always cite the official source when adding or correcting factual content.
- Link inline at the point where the claim is made, not in a separate references section.

## Language

- Always respond in English unless the user explicitly asks otherwise.
- File content such as notes and reports may be in Korean, English, or both.

## What This Repo Is

- A personal study notes repo.
- All content is Markdown.
- No build system, no tests, no dependencies.

## Core Rules

- `README.md` files must stay folder indexes only. Do not add study content, study order, or concept explanations to a README.
- The nearest relevant `00_overview.md` is the study hub for its subtree. Update that overview when notes in that subtree are added, removed, renamed, or reordered.
- Explain a concept once in the note where it belongs. In other notes, link to the existing explanation instead of duplicating it.
- On first use in a note, write the full name before the abbreviation in parentheses, then use the short form afterward. Example: `Cloud Development Kit (CDK)`.
- Link inline where a concept is mentioned, not in a separate cross-references section.
- Use `> **Tip:**` for practical guidance. No other callout formats.
- No `---` horizontal rules except before the navigation footer.
- No history sections such as inventor names or creation dates.
- Keep examples small and concrete, not abstract placeholders.
- Prefer editing existing Markdown notes, links, and navigation over adding tooling, scripts, or structural churn.
- Preserve the repository's existing organization unless the task explicitly requires a reorganization.

## Cross-Linking

- When editing or reviewing a note, scan notes in the same domain and adjacent domains for concepts mentioned but not yet linked to their canonical note.
- When creating a new note, search existing notes for unlinked mentions of that concept and add backward links.
- On first mention of any concept that has a dedicated note elsewhere in the repo, add an inline Markdown link. Do not repeat the link on subsequent mentions in the same file.
- Cross-domain links (e.g., an `ai/` note linking to a `networking/` concept) are encouraged when the connection genuinely helps the reader.

## Markdown Formatting

### Headings

- `#` — note title only. One per file.
- `##` — major sections (`What It Is`, `How It Works`, etc.).
- `###` — subsections within a section.
- Never use `####` or deeper. If you need it, split the note.

### Lists

- Bullets (`-`) — unordered facts, properties, options.
- Numbers (`1.`) — ordered steps, priority order, study order.
- Indent nested items with 2 spaces.

### Emphasis

- `**bold**` — key terms, important warnings.
- `*italic*` — light emphasis, titles of external works.
- `` `inline code` `` — commands, filenames, env vars, values.

### Tables

- Use tables for comparisons, option sets, and structured data.
- Every table needs a header row and a separator row.

### What not to use

- No `---` horizontal rules except immediately before the navigation footer.
- No `> Note:`, `> Warning:`, or other callout formats — only `> **Tip:**`.
- No raw HTML.
- No emoji unless the user explicitly requests it.

## Note Structure

Every note file must follow this heading order:

```md
# Title
## What It Is
## Analogy
## How It Works
## Example
## Why It Matters
```

Rules:
- `What It Is` is required and should be a 1-2 sentence definition.
- `Analogy` is optional and should appear only if it genuinely helps.
- `Example` is required and should be concrete and small.
- `Why It Matters` is required.
- Additional `##` sections are allowed between required sections when the content genuinely warrants it (e.g. `## Name` for etymology, `## Prerequisites` for complex setup).

Every note ends with a navigation footer preceded by `---`:

```md
---
← Previous: [Title](link) | [Overview](00_overview.md) | Next: [Title](link) →
```

## Obsidian Frontmatter Tags

- Every note file must begin with a YAML frontmatter block with a `tags` field, placed before the `# Title` heading.
- Tags use lowercase, hyphen-separated words.
- When creating or editing a note, assign all applicable tags from the taxonomy below. Add a new tag to the taxonomy only if no existing tag fits.

Format:

```yaml
---
tags:
  - aws
  - serverless
---
```

Tag taxonomy:

| Tag | Covers |
|-----|--------|
| `ai` | AI/ML, LLMs, agents, attention, KV cache |
| `aws` | AWS services in general |
| `networking` | Protocols, OSI, DNS, HTTP, proxies |
| `computing` | CPU, GPU, virtualization, caching, storage |
| `git` | Git workflow, staging, tracking |
| `tooling` | Dev tools, editors, terminal setup |
| `security` | IAM, Shield, WAF, auth, secrets |
| `storage` | S3, EFS, EBS |
| `database` | RDS, DynamoDB, Aurora, ElastiCache |
| `serverless` | Lambda, Fargate, API Gateway |
| `container` | ECR, Docker, Lambda container images |
| `monitoring` | CloudWatch, observability |
| `ml` | SageMaker, Bedrock, model training |
| `infrastructure` | VPC, regions, AZs, subnets, CDK |

## Domain Layout

| Path | Content |
|------|---------|
| `ai/` | AI agents, LLM concepts such as harness, tools, MCP, attention, and KV cache |
| `aws/101/aws_services/` | AWS 101 service notes |
| `aws/101/console_workthrough/` | Console walkthrough notes per service |
| `aws/201/aws_services/` | AWS 201 deep-dives |
| `computing/` | CPU, virtualization, storage, GPU, caching, interfaces, endpoints |
| `git/` | Git tracking, staging, daily workflow |
| `networking/` | Protocols, addressing, OSI, DNS, HTTP |
| `tooling/` | Developer tools, editors, note apps, and workflow methods |
| `glossary/` | Abbreviations and domain terms used across the repo |

Each domain has a `00_overview.md` as the study hub with navigation links.

## Primary Artifacts

- `README.md`: folder index and directory description only
- `00_overview.md`: study hub and ordered navigation for a subtree
- concept notes: the main study content
- walkthrough notes: step-by-step operational or console guides
- image references: screenshots and image assets used by notes

## Agent Behavior

These four principles, derived from Andrej Karpathy's observations on LLM agent mistakes, govern how this agent approaches note-editing tasks in this repo.

### Think Before Acting

Before editing or creating any note, state your interpretation of the request explicitly. If the scope is ambiguous — for example, whether to update one note or all notes in a domain — surface the alternatives and ask rather than guessing. Prefer one focused clarifying question over making a broad assumption.

### Simplicity First

Do exactly what was requested and nothing more. Do not add new notes, new sections, new tags, or new cross-links unless they were explicitly asked for. A note that was not mentioned is a note that should not be touched. Avoid restructuring a domain when a single-note edit was requested.

### Surgical Changes

Change only the specific lines, sentences, or links that the task requires. Preserve the surrounding prose, heading order, frontmatter, and navigation footer exactly as they are. Do not reword content that was not broken. Do not remove content you did not add.

### Goal-Driven Execution

When a request is vague (for example, "clean up the networking notes"), convert it to a concrete, verifiable scope before starting: name the specific files you will touch, state what you will change in each, and confirm that list with the user if the scope is more than two files. After completing the work, verify against that stated scope — not against a broader interpretation.

## Editing Checklist

- If you edit a note, preserve the required structure defined in [README.md](README.md).
- If you edit a note, preserve or repair the navigation footer.
- If you add or rename a note, update the nearest relevant `00_overview.md`.
- If a folder's contents change materially, update that folder's `README.md`.
- If a concept is already documented elsewhere, link to the existing note instead of re-explaining it.
- Do not put study content into `README.md`.

## README Rules

- READMEs list files and directories with one-line descriptions.
- READMEs do not contain study content, study order, or cross-references.
- Every domain README links to its `00_overview.md` for study order.
- When adding a new note, add it to both the domain README and the relevant `00_overview.md`.

## Subtree Policy

- Add a nested `AGENTS.md` or `CLAUDE.md` only when a subtree needs materially different instructions from the repo root.
- Keep subtree files narrow. They should extend or override root behavior only for that subtree.

## Agent Delivery Hooks

- Working rule: `"실패는 요란하게, 성공은 조용하게"` ("fail loudly, succeed quietly").
- Push rule: one file change, one git push. After any file create, edit, rename, move, or delete, the agent should treat that write as requiring its own full delivery loop in the same turn when feasible: update related docs, verify rules, commit, and push.
- When an agent creates, fixes, renames, moves, or deletes a file, it must finish the delivery loop in the same turn when feasible: update the relevant docs, verify repo and folder rules, check security, commit, and push.
- Relevant docs usually include the nearest `00_overview.md`, the folder `README.md`, navigation footers, and any note links affected by the change.
- Before pushing, the agent must confirm that changed files follow this repo's Markdown structure, README rules, and navigation rules.
- Before pushing study-content Markdown, the agent must review the changed study files and explicitly acknowledge that it knows their contents. Repo plumbing such as `.claude/`, `.codex/`, `.githooks/`, `.kiro/`, `.env`, `AGENTS.md`, and `CLAUDE.md` is excluded from this acknowledgment check.
- Before pushing, the agent must check for security problems such as secrets, tokens, credentials, private keys, or unsafe command snippets that accidentally embed real sensitive values. If a security issue is found, stop and fix it before pushing.
- Codex only manages shared Git hook entrypoints in `.githooks/` and Codex-owned logic in `.codex/`.
- `.claude/` is out of scope for Codex. Do not inspect, edit, organize, or rely on Claude-owned hooks, skills, or helper files unless the user explicitly asks for Claude-specific work.
- The hook enforces the mechanical checks, but the agent is still responsible for deciding which related docs need updates.

## Git Push

Credentials are handled automatically via `.githooks/git-credential-env.sh`, which reads `GITHUB_TOKEN` and `GITHUB_USERNAME` from `.env`. Plain push works:

```bash
git push origin main
```

If git identity is missing, set it once from `.env`:

```bash
set -a && source .env && set +a
git config --local user.name "$GIT_USER_NAME"
git config --local user.email "$GIT_USER_EMAIL"
```
