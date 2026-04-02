# Tracking and Status

## What It Is

Git tracks file state by comparing three things: the last committed snapshot, the staging area (index), and your working tree.

## Analogy

Think of Git like packing luggage: the working tree is everything lying around in your room, the staging area is items you put into the suitcase, and a commit is the suitcase after you zip and label it.

## How It Works

### Core States

| State | Meaning |
|-------|---------|
| **Untracked** | File exists on disk but Git is not tracking it (`??` in short status, `U` in editors) |
| **Tracked** | Git knows about the file — it was added before and is part of history |
| **Staged** | File's current version is in the index, ready for the next commit |
| **Committed** | The staged snapshot has been saved into Git history |

### Status Letters

| Letter | Meaning |
|--------|---------|
| `U` | Untracked (editor UI) — file exists but Git hasn't started tracking it |
| `M` | Modified — tracked file's contents changed |
| `A` | Added — file is staged as a new tracked file |
| `D` | Deleted — tracked file was removed |
| `R` | Renamed — Git detected a tracked file became another path |

### Splits and Renames

When you split or rename files, editor badges can briefly look confusing: old file shows `D`, new file shows `U`. After `git add -A`, Git may understand the relationship as a delete + add or a rename, depending on similarity.

## Example

You create `notes.md` and have not run `git add` yet. Git sees the file in your working tree but not in the index, so it shows as untracked.

```bash
git status          # see full state
git status --short  # compact view
git add <file>      # stage a file
git add -A          # stage everything
git commit -m "msg" # commit staged changes
```

## Why It Matters

Many Git mistakes come from misunderstanding the difference between "file exists," "file is tracked," "file is staged," and "file is committed." If you know those four states clearly, `git status` becomes easy to read.

> **Tip:** Git is the version control system. GitHub is a hosting platform built around Git. Tracked, untracked, staged, and committed are Git concepts, not GitHub concepts.

---
[Overview](00_overview.md)
