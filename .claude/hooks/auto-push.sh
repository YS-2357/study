#!/bin/bash
# Auto-push hook — stages only the file this agent touched, not the whole tree.
# Prevents race conditions when multiple agents edit simultaneously: each agent
# commits its own file instead of sweeping up work in progress from siblings.
# 실패는 요란하게, 성공은 조용하게

REPO=$(git rev-parse --show-toplevel 2>/dev/null)
cd "$REPO" || exit 0

set -a && source .env 2>/dev/null && set +a

# Read Claude Code hook JSON from stdin when piped (PostToolUse events).
# For Stop events or manual runs there's no JSON, so we fall back to `git add -A`.
STDIN_JSON=""
if [ ! -t 0 ]; then
    STDIN_JSON=$(cat)
fi

# Extract the touched file path. On PostToolUse for Write/Edit, this is
# tool_input.file_path. Use jq when available; fall back to grep.
TOUCHED_FILE=""
if [[ -n "$STDIN_JSON" ]]; then
    if command -v jq >/dev/null 2>&1; then
        TOUCHED_FILE=$(printf '%s' "$STDIN_JSON" | jq -r '.tool_input.file_path // empty' 2>/dev/null)
    else
        TOUCHED_FILE=$(printf '%s' "$STDIN_JSON" \
            | grep -oE '"file_path"[[:space:]]*:[[:space:]]*"[^"]+"' \
            | head -1 \
            | sed -E 's/.*"file_path"[[:space:]]*:[[:space:]]*"([^"]+)".*/\1/')
    fi
fi

# Stage: specific file for PostToolUse, all changes for Stop/manual.
# `git add -A <pathspec>` handles create/modify/delete uniformly.
if [[ -n "$TOUCHED_FILE" ]]; then
    git add -A -- "$TOUCHED_FILE" 2>/dev/null
else
    git add -A 2>/dev/null
fi

# Skip if nothing staged
if git diff --cached --quiet 2>/dev/null; then
    exit 0
fi

# Build commit message from staged files
CHANGED_FILES=$(git diff --cached --name-only 2>/dev/null)
FILE_COUNT=$(echo "$CHANGED_FILES" | grep -c .)
FIRST_FILE=$(echo "$CHANGED_FILES" | head -1)

if [ "$FILE_COUNT" -eq 1 ]; then
    COMMIT_MSG="auto: update $FIRST_FILE"
else
    COMMIT_MSG="auto: update $FIRST_FILE and $((FILE_COUNT - 1)) more"
fi

git commit -m "$COMMIT_MSG" -q 2>/dev/null

PUSH_OUTPUT=$(CLAUDE_AUTO_PUSH=1 git \
    -c credential.helper= \
    -c "http.https://github.com/.extraheader=AUTHORIZATION: basic $(printf '%s:%s' "$GITHUB_USERNAME" "$GITHUB_TOKEN" | base64 -w0)" \
    push origin main 2>&1)
EXIT_CODE=$?

if [ $EXIT_CODE -ne 0 ]; then
    ESCAPED=$(echo "$PUSH_OUTPUT" | head -20 | sed 's/"/\\"/g' | tr '\n' ' ')
    printf '{"systemMessage": "🚨 AUTO-PUSH FAILED — %s"}\n' "$ESCAPED"
fi
