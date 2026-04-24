#!/bin/bash
# PostToolUse: normalize updated_at and recent_editor in note frontmatter to current KST.
# Reads Claude Code hook JSON from stdin, extracts the touched file, rewrites
# only those two fields inside the first frontmatter block. Silent on success.
# 실패는 요란하게, 성공은 조용하게

REPO=$(git rev-parse --show-toplevel 2>/dev/null) || exit 0
cd "$REPO" || exit 0

# Requires stdin JSON from Claude Code (PostToolUse). No JSON → no-op.
[ -t 0 ] && exit 0
STDIN_JSON=$(cat)

if command -v jq >/dev/null 2>&1; then
    FILE=$(printf '%s' "$STDIN_JSON" | jq -r '.tool_input.file_path // empty' 2>/dev/null)
else
    FILE=$(printf '%s' "$STDIN_JSON" \
        | grep -oE '"file_path"[[:space:]]*:[[:space:]]*"[^"]+"' \
        | head -1 \
        | sed -E 's/.*"file_path"[[:space:]]*:[[:space:]]*"([^"]+)".*/\1/')
fi

[[ -z "$FILE" || ! -f "$FILE" || "$FILE" != *.md ]] && exit 0

# Skip files without a top frontmatter block.
head -5 "$FILE" | grep -q '^---' || exit 0

NOW=$(TZ=Asia/Seoul date +%Y-%m-%dT%H:%M:%S)
TMP="${FILE}.ts-tmp"

awk -v now="$NOW" '
    NR==1 && /^---[[:space:]]*$/ { in_fm=1; print; next }
    in_fm && /^---[[:space:]]*$/ { in_fm=0; print; next }
    in_fm && !done_ts && /^updated_at:[[:space:]]/ { print "updated_at: " now; done_ts=1; next }
    in_fm && !done_re && /^recent_editor:[[:space:]]/ { print "recent_editor: CLAUDE"; done_re=1; next }
    { print }
' "$FILE" > "$TMP"

# Only replace if awk produced non-empty output (defensive against edge cases).
if [ -s "$TMP" ]; then
    mv "$TMP" "$FILE"
else
    rm -f "$TMP"
fi
