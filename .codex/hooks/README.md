# .codex/hooks

Codex-specific hook implementations for this repository.

- `README.md`: This file.
- `pre-push`: Codex validation checks that run before `git push`.

The Codex `pre-push` hook also enforces the repo rule that pushes normally contain only one outgoing commit. For exceptional cases, set `STUDY_ALLOW_MULTI_COMMIT_PUSH=1` for that push.
