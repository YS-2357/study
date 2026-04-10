# .githooks

Local Git hooks used by this repository.

- `README.md`: This file.
- `pre-push`: Thin Git entrypoint that dispatches to agent-specific hook logic.
- `pre-push-study-content`: Shared study-content acknowledgment check that runs before agent-specific validation.

To activate these hooks in this clone, set:

```bash
git config core.hooksPath .githooks
```
