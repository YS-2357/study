# Data And Retrieval

<!-- planner:flow:start -->
## Flow Role

- Order: `06`
- Depends on: [05_entry-and-ui.md](./05_entry-and-ui.md)
- Enables / Affects: [07_agent-runtime.md](./07_agent-runtime.md)
- Purpose Fit: Explain how this file advances the user goal without drifting outside scope.
<!-- planner:flow:end -->

## Objective

- Turn the Zendesk export into a retrieval-ready knowledge source and constrain the agent to grounded support content.

## Decisions

- The initial knowledge source is [zendesk_articles.csv](../data/zendesk_articles.csv).
- Article HTML must be cleaned into normalized text before chunking and indexing.
- Retrieval results should carry article title, URL, update time, and source snippet into the agent/reviewer flow.
- Inquiry text and retrieved knowledge should stay request-scoped; no long-lived memory store is needed in this first cut.

## Plan

- Build a preprocessing step:
  - parse CSV rows
  - strip or normalize HTML
  - preserve article metadata
  - chunk long article bodies for retrieval
- Index the cleaned chunks in a retrieval layer suitable for the POC.
- At runtime:
  - query the retrieval layer with the normalized inquiry
  - pass top relevant chunks plus metadata to the agent
  - return the same evidence to the reviewer UI
- Keep retrieval narrow and auditable; avoid mixing customer-specific ticket history into the knowledge base in v1.

## Risks / Questions

- HTML tables and product-option price lists may chunk poorly if preprocessing is naive.
- Retrieval quality may degrade if article freshness or section metadata is not surfaced to the reviewer.
- The final implementation still needs a concrete indexing technology choice.
