# Tracking and Status

## What It Is
Git tracks file state by comparing three things:
- the last committed snapshot
- the staging area (index)
- your working tree

That is why the same file can look different depending on whether it is untracked, modified, staged, or already committed.

## Analogy
Think of Git like packing luggage for a trip:
- **working tree** = everything lying around in your room
- **staging area** = the items you already put into the suitcase
- **commit** = the suitcase after you zip it and label it as one finished snapshot

A file can exist in your room without being in the suitcase yet. That is what untracked usually means.

## Example
You create `notes.md` and have not run `git add notes.md` yet.

Git sees:
- the file exists in your working tree
- but it is not in the index

So Git shows it as untracked.

---

## Core States

### Untracked
A file exists on disk, but Git is not tracking it yet.

Common sign:
- `U` in some editors
- `??` in `git status --short`

Meaning:
- Git sees the file
- Git has not added it to the index
- it is not part of history yet

### Tracked
Git already knows about the file.

That means the file was added before and is now part of the repo history or staging workflow.

Tracked files can still be:
- modified
- staged
- deleted
- renamed

### Staged
The file’s current version has been added to the index and is ready to become part of the next commit.

### Committed
The staged snapshot has been saved into Git history.

---

## Common Status Letters

### `U`
Usually means **Untracked** in an editor UI.

It does **not** mean updated. It means:
- the file exists
- Git has not started tracking it yet

### `M`
Modified.

Git already tracks the file, and its working-tree contents changed.

### `A`
Added.

The file is staged as a new tracked file.

### `D`
Deleted.

Git thinks the tracked file was removed.

### `R`
Renamed.

Git detected that one tracked file became another tracked path.

---

## Why Splits and Renames Sometimes Look Weird

When you split or rename files, editor badges can briefly look confusing.

Example:
- old file shows `D`
- new file shows `U`

This usually means:
- Git still sees the old tracked file as deleted
- Git sees the new file as not yet added

After `git add -A`, Git may understand the relationship as:
- delete + add
- or a rename, depending on similarity

So a temporary `U` after a split is normal.

## Why It Matters

This matters because many Git mistakes come from misunderstanding the difference between:
- file exists
- file is tracked
- file is staged
- file is committed

If you know those four ideas clearly, `git status` becomes much easier to read.

## Quick Commands

```bash
git status
git status --short
git add <file>
git add -A
git commit -m "message"
```

## Git vs GitHub

- **Git** = the version control system
- **GitHub** = a hosting/collaboration platform built around Git

Tracked, untracked, staged, and committed are Git concepts, not GitHub concepts.
