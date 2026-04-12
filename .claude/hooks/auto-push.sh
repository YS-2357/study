#!/bin/bash
# Auto-push hook for study repo — runs after every Write/Edit
# 실패는 요란하게, 성공은 조용하게

REPO="/home/ys2357/study"
cd "$REPO" || exit 0

set -a && source .env 2>/dev/null && set +a

git add -A 2>/dev/null

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
    -c "http.https://github.com/.extraheader=AUTHORIZATION: basic $(printf 'YS-2357:%s' "$GITHUB_TOKEN" | base64 -w0)" \
    push origin main 2>&1)
EXIT_CODE=$?

if [ $EXIT_CODE -ne 0 ]; then
    # Send error as a Claude Code system message
    ESCAPED=$(echo "$PUSH_OUTPUT" | head -20 | sed 's/"/\\"/g' | tr '\n' ' ')
    printf '{"systemMessage": "🚨 AUTO-PUSH FAILED — %s"}\n' "$ESCAPED"
fi
