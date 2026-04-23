---
tags:
  - git
created_at: 2026-04-23T14:31:50
updated_at: 2026-04-23T14:31:50
recent_editor: CLAUDE
---

↑ [Overview](./00_git_overview.md)

# Remote Workflow — Push, Pull, Pull Request

## What It Is

Three operations for syncing code between your machine and GitHub:

| Operation | Direction | What it does |
|-----------|-----------|-------------|
| `git push` | Local → GitHub | Upload your commits to GitHub |
| `git pull` | GitHub → Local | Download others' commits to your machine |
| Pull Request (PR) | Feature branch → main | Ask for your branch to be reviewed and merged |

A **pull request** is not a git command — it is a GitHub feature for code review before merging.

## Analogy

Think of GitHub as a shared Google Doc in the cloud, and your machine as your local copy.

- **push** = you click "upload my changes to the cloud"
- **pull** = you click "download the latest version from the cloud"
- **pull request** = you finish your section, then ask your teammate "can you review my section and add it to the main document?"

## How It Works

### push

```
Your machine          GitHub
   [commit A] ──push──► [commit A]
   [commit B] ──push──► [commit B]
```

You run `git push` after committing. Nothing goes to GitHub until you push.

### pull

```
Your machine          GitHub
              ◄─pull── [commit C]  ← someone else pushed this
              ◄─pull── [commit D]
```

`git pull` = `git fetch` (download) + `git merge` (apply). It downloads and applies new commits from GitHub in one step.

### Pull Request

The flow:

```
1. Create a feature branch
   main ──────────────────►
         └── feature ──────►

2. Push your feature branch to GitHub
   git push origin feature

3. Open a Pull Request on GitHub
   "Please merge feature → main"

4. Teammate reviews the code

5. Approved → merged into main
   main ──────────────────────────►
         └── feature ──────────────┘ merged
```

**Why feature → main, not the other way?**

The name "pull request" comes from the maintainer's perspective: you are *requesting* that they *pull* your branch into theirs. The direction is always feature → main because main is the stable branch — nobody pushes to it directly. The PR is a review gate that keeps main clean. ([GitHub Docs](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request), [Atlassian](https://www.atlassian.com/git/tutorials/making-a-pull-request))

## Example

Solo project (no review needed):

```bash
git add note.md
git commit -m "add note"
git push                    # uploads to GitHub
```

Team project (with review):

```bash
git checkout -b feature/login   # create feature branch
git add .
git commit -m "add login page"
git push origin feature/login   # push the feature branch

# → go to GitHub, open Pull Request: feature/login → main
# → teammate reviews, approves
# → merge on GitHub
```

## Why It Matters

- **push/pull** keep your local copy and GitHub in sync — without them you are working in isolation.
- **Pull requests** are how teams collaborate safely: nobody touches `main` directly, every change is reviewed before it lands.

---
↑ [Overview](./00_git_overview.md)

**Related:** [Daily Git Workflow](02_daily_git_workflow.md), [Tracking and Status](01_tracking_and_status.md)
**Tags:** #git
