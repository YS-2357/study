# Skills

## What It Is
A skill is a reusable instruction bundle that teaches the agent how to handle a specialized kind of task.

A skill usually contains:
- `SKILL.md`
- optional scripts
- optional references or assets

## Analogy
If the agent is a worker and tools are the instruments, a skill is a playbook for a recurring job.

Examples:
- how to debug CI failures
- how to work from a Figma design
- how to edit a spreadsheet safely

## Example
A generic agent can already edit code.

A CI-debugging skill adds a repeatable workflow like:
- inspect failing checks
- read logs
- isolate likely cause
- reproduce locally
- patch the minimal fix

That is more structured than a normal free-form prompt.

## When to Use a Skill

Use a skill when:
- the task type repeats often
- the workflow benefits from fixed steps
- special scripts or references are helpful
- generic prompting would be noisy or inconsistent

Do not think of skills as mandatory for every task. Many normal coding tasks do not need one.

## What People Mostly Use

Most people use:
- built-in or installed skills for specialized workflows
- no skill at all for ordinary repo exploration and editing

So skills are important, but they are not the main thing you interact with every minute.

## Why It Matters

Beginners often over-focus on skills.

In practice:
- agent + tools + `AGENTS.md` cover most work
- skills become useful when the workflow gets specialized
