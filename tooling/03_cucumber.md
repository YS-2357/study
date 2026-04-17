---
tags:
  - tooling
created_at: 260409-000000
updated_at: 260417-141847
---

# Cucumber

## What It Is

Cucumber is an open-source tool for running automated acceptance tests written in plain language, so the expected behavior can be read by both developers and non-developers, according to the official [Cucumber homepage](https://cucumber.io/). It is closely associated with Behavior-Driven Development (BDD), which [Cucumber describes](https://cucumber.io/docs/bdd/) as a process for discovering, specifying, and testing behavior from the user's or business's point of view.

## Analogy

Most test tools are like writing a machine-checkable checklist directly in code. Cucumber is like writing the checklist in short, structured sentences first, then wiring those sentences to executable test code underneath.

## How It Works

Cucumber scenarios are usually written in the Gherkin format with `Feature`, `Scenario`, `Given`, `When`, and `Then` steps. The [official Cucumber documentation](https://cucumber.io/docs/gherkin/reference/) uses this structure so the test reads like a description of behavior instead of only like code.

That creates a different workflow from code-first testing:

- In a code-first framework such as Jest, Pytest, or Playwright, the main artifact is the test code.
- In Cucumber, the main artifact is the behavior description, and step-definition code exists to make that description executable.

This is why BDD matters here. BDD is not just "writing tests in English." It is the idea that the team should first clarify what behavior is expected, then implement and verify it against that shared description. Even in a solo project, that process can force clearer thinking because vague requirements become visible before implementation starts.

Main effects of this approach:

- It improves communication because the scenario is easier to read than raw test code.
- It can expose missing edge cases earlier because each step must state the expected behavior explicitly.
- It adds ceremony and maintenance cost because the plain-language layer and the step-definition layer both need to stay accurate.

You can apply the same idea outside automated testing by writing task or feature notes in a behavior-first format before implementation. For example, instead of writing "build password reset," write the expected behavior first with short `Given`, `When`, and `Then` statements, then use that note as the source of truth for both coding and review.

That is also useful for [large language model (LLM)](../ai/01_agent.md)-assisted work. An LLM benefits from the same clarity humans do: explicit behavior, constraints, and edge cases give it a more precise target than a vague prompt. In practice, a Cucumber-style note can work as a structured prompt, an acceptance checklist, and a review artifact at the same time.

For note-taking tools, a file-first app is usually a better fit than a workspace-first app when you want behavior notes to live in Git and be easy for AI tools to read. See [Obsidian vs Notion](04_obsidian_vs_notion.md) for the detailed comparison.

## Example

A solo developer wants to build a password reset flow. Before writing the feature, they write a small Cucumber scenario:

```gherkin
Feature: Password reset
  Scenario: Registered user requests a reset link
    Given a registered user exists
    When the user requests a password reset
    Then the user receives a reset link
```

Writing the scenario first can reveal open questions before code is written: what happens for an unknown email, how long the token should stay valid, and whether reset requests need rate limiting. That is the practical BDD effect: the test description helps clarify the feature idea, not just verify the implementation later.

The same pattern works for personal notes in [Obsidian](04_obsidian_vs_notion.md). A note such as `password-reset.md` can contain the scenarios, be linked to related implementation notes, and be versioned in Git. An LLM can then use that note as a concrete input: implement the feature, generate tests from the scenarios, or point out missing edge cases.

## Why It Matters

The key difference between Cucumber and most other testing tools is that Cucumber makes behavior descriptions the center of the workflow instead of only test code. That changes the impact of testing: the test is not only a regression check, but also a tool for clarifying requirements.

This can help teams align on business rules, but it can also help solo developers think more clearly. Writing expected behavior in plain language often exposes ambiguity, missing rules, and unhandled edge cases earlier than code-first tests do. The tradeoff is that Cucumber is usually more verbose and heavier to maintain than direct unit or integration tests, so it is most valuable when the clarity benefit outweighs the extra structure.

That same structure can improve AI-assisted development. If the note says exactly what should happen in the happy path and in the edge cases, the AI is less likely to invent missing requirements or implement the wrong thing. In that sense, "Cucumber philosophy" can be valuable even when you never run Cucumber itself: the behavior spec still improves implementation quality because both the human and the model are working from the same explicit contract.

> **Tip:** Use Cucumber when the hardest part is agreeing on behavior. If the behavior is already obvious and you only need a fast technical check, a code-first test framework is usually simpler.

---
← Previous: [Vim and Neovim](02_vim_and_neovim.md) | [Overview](00_overview.md) | Next: [Obsidian vs Notion](04_obsidian_vs_notion.md) →
