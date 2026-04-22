---
tags:
  - tooling
created_at: 2026-04-19T09:11:51
updated_at: 2026-04-22T09:57:48
recent_editor: CLAUDE
---

# Log

Append-only chronological record of ingest, query, and lint operations.

## [2026-04-20T13:59:45] ingest | anthropic-mythos (web research)
- Source: anthropic.com official pages, research papers, credible news
- Created: ai/claude/01_anthropic.md, 02_claude_models.md, 03_constitutional_ai.md, 04_rsp.md, 05_interpretability.md, 06_claude_character.md
- Updated: ai/claude/00_claude_overview.md (hub rewrite), ai/00_ai_overview.md (Claude row)

## Format

```
## [YYYY-MM-DDTHH:MM:SS] ingest|query|lint | <source-or-topic>
- note: what was touched
- note: what was decided
```

Newest entries at the bottom. Each entry starts with `## [` so the log is parseable with plain Unix tools:

```bash
grep "^## \[" log.md | tail -5        # last 5 entries
grep "^## \[.*ingest" log.md | wc -l  # total ingests
```

## Entries

## [2026-04-19T09:11:51] bootstrap | log.md created
- Established log format.
- Part of Karpathy LLM Wiki pattern adoption.

## [2026-04-19T09:11:51] bootstrap | Karpathy LLM Wiki pattern adopted
- Source: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Added: `/ingest` and `/lint` slash commands, `rules/09_ingest.md`, `rules/10_lint.md`, root `log.md`.
- Navigation: dropped prev/next chains; new footer is `↑ Overview` + `Related` list + `Tags` list.
- Numbering: `NN_` is now an identifier only, not a study-order rank.
- Frontmatter: added optional `source:` field for ingested sources.
- Repo sync: `raw/` is now gitignored (sources local-only); only `raw/README.md` tracked.
- Migration: 98 concept notes and 19 overviews rewritten in this session.
- Pre-push: updated `.codex/hooks/pre-push` footer check to accept the new multi-line footer shape.

## [2026-04-19T09:11:51] lint | post-migration review
- Agents reviewed `rules/`, concept notes, and overviews against the new navigation model.
- Fixed: stale "study order" wording in `rules/01_note_structure.md`, `rules/06_content_diagrams.md`, `ai/README.md`, `git/README.md`.
- Fixed: L4 navigation diagram in `rules/06_content_diagrams.md` still showed old prev/next footer.
- Fixed: `rules/01_note_structure.md` §1 required-sections block and §2 heading table were ambiguous on numeric prefixes — clarified that `## Section` is verbatim, no `## 1. Section`.
- Fixed: `How It Works` missing from §1.1 Section Rules enumeration.
- Fixed: added `How It Works` section to `ai/09_profiles.md` (was missing).
- Fixed: `aws/ai/12_amazon_bedrock_integration_patterns.md` renumbered H2/H3 to bare section names (was the only note literal-following the old `## 1.` style).
- Fixed: legacy `YYMMDD-HHMMSS` timestamps in `computing/00_computing_overview.md`, `git/00_git_overview.md`, `.claude/README.md`, `.githooks/README.md`.
- Fixed: empty `tags:` and missing `recent_editor:` in `.claude/README.md`, `.githooks/README.md`.
- Fixed: hardcoded GitHub username `YS-2357` in token-based push snippets replaced with `$GITHUB_USERNAME` in `.claude/README.md`, `.codex/README.md`, `git/02_daily_git_workflow.md`.
- Fixed: duplicate Fargate link in `aws/compute/03_aws_lambda.md` Related list; added `.claude/dedup_related.py` for future passes.
- Verified: no other concept-note footers carry duplicate targets.

## [2026-04-19T15:16:34] maintenance | log.md validation
- Fixed: `.codex/hooks/pre-push` now treats root `log.md` as special Markdown, not a concept note.
- Reason: `log.md` is an append-only operational timeline and should keep frontmatter/security checks without requiring concept-note sections or footer.

## [2026-04-19T15:56:25] ingest | agentcore_runtime_intro_2026_04
- Touched: aws/ai/agentcore/01_runtime.md (update)
- Added: MicroVM isolation, deploy pipeline (Docker to ECR to CodeBuild ARM64), HTTP Agent vs MCP Server protocol choice, stateless_http=True requirement, streaming SSE pattern, 100MB large payload, session lifecycle tuning, Stateless vs Stateful, workload decision matrix.

## [2026-04-19T16:16:10] ingest | agentcore_memory_intro_2026_04
- Touched: aws/ai/agentcore/02_memory.md (update)
- Added: Short-term vs Long-term distinction, 4 strategies (UserPreference/Semantic/Episodic/Custom), core API flow, extract_memories() async caveat, MemoryClient vs MemoryManager, Strands/LangGraph/LlamaIndex integration patterns, Multi-Agent Shared Memory with namespace isolation.

## [2026-04-19T16:16:39] ingest | agentcore_gateway_intro_2026_04
- Touched: aws/ai/agentcore/03_gateway.md (update)
- Added: 6 Gateway roles, 3 deployment steps, 3 Target types (Lambda/OpenAPI/Smithy), inbound auth comparison, outbound credential_provider structures (IAM/API Key/OAuth), Semantic Search strategy, workload decision matrix, production rules.

## [2026-04-19T16:16:40] ingest | agentcore_intro_korean_2026_04
- Touched: aws/ai/agentcore/01_runtime.md, aws/ai/agentcore/02_memory.md, aws/ai/agentcore/03_gateway.md (source slug added to all three)
- Decision: General intro PDF; specific service content absorbed into respective service notes above.

## [2026-04-19T17:22:51] ingest | strands_jhrhee_2026_04
- Touched: aws/ai/11_strands_agents_sdk.md (update)
- Added: structured_output() Pydantic API, SlidingWindowConversationManager constructor params (window_size, should_truncate_results), production checklist (Secrets Manager, OTEL, CI/CD, access control, unit+E2E tests).

## [2026-04-19T18:39:20] query | repo orientation
- Read: README.md, rules/*.md, aws/AGENTS.md, glossary.md.
- Decision: follow associative navigation, concept-note structure, source-aware ingest, on-demand lint, and one-file delivery rules.

## [2026-04-19T19:06:00] lint | post-ingest review fixes
- Fixed: missing AgentCore `Analogy` sections, non-ASCII source slugs, log chronology, unsupported exact claims, and Strands draft wording.
- Deferred: unrelated local `.claude/settings.local.json` and `.obsidian/workspace.json` changes.

## [2026-04-20T08:29:39] ingest | langchain_langgraph_2026_meaning
- Touched: ai/15_langchain_langgraph.md (new), ai/00_ai_overview.md, ai/README.md
- Decision: create a general AI framework note for LangChain/LangGraph rather than editing AWS-specific agent framework notes.

## [2026-04-20T14:15:06] nav-update | organize ai overview by current path structure
- Touched: ai/00_ai_overview.md, ai/concepts/00_concepts_overview.md, ai/README.md, log.md
- Decision: parent AI overview now lists immediate subdomains; concept note links moved into the concepts overview.

## [2026-04-20T14:33:31] query | perplexity developer deep dive
- Touched: ai/perplexity/00_perplexity_overview.md, log.md
- Added: Sonar API, official SDKs, OpenAI-compatible client usage, LangChain support, and developer use cases.

## [2026-04-20T14:47:19] query | perplexity korean search caveat
- Touched: ai/perplexity/00_perplexity_overview.md, log.md
- Added: Korean-language search caveat; use Perplexity for source discovery and cross-check Korean-local topics with NAVER, Google, and official Korean sources.

## [2026-04-22T09:57:48] ingest | aws-partner-summit-seoul-2026
- Source: raw/AWS Partner Summit Seoul 2026/ (10 OCR extract .md files + 1 notetaking .md)
- Created: cloud/aws/ai/13_llm_evaluation.md, cloud/aws/ai/14_physical_ai.md, cloud/aws/ai/15_agentic_modernization.md, cloud/aws/database/07_amazon_neptune.md, cloud/aws/devtools/04_sap_aws.md, cloud/aws/01_aws_partner_summit_seoul_2026.md
- Updated: cloud/aws/ai/agentcore/08_evaluations.md (3-level monitoring, silent failure, Judge Gate), cloud/aws/analytics/04_amazon_sagemaker.md (SageMaker Catalog section), cloud/aws/00_aws_overview.md (new notes + Events section)
- Moved: raw/AWS Partner Summit Seoul 2026/ → raw/processed/AWS Partner Summit Seoul 2026/
