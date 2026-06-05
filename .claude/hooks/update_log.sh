#!/usr/bin/env bash
# Stop hook: auto-update PROJECT_LOG.md when session ends.
# Only appends if there are uncommitted changes or new untracked files
# (excluding .claude/ and this hook's own marker).

set -euo pipefail

PROJECT_ROOT="/develop/habitat-lab"
LOG_FILE="$PROJECT_ROOT/PROJECT_LOG.md"
NOW=$(date '+%Y-%m-%d %H:%M:%S')
TODAY=$(date '+%Y-%m-%d')

cd "$PROJECT_ROOT"

# Only proceed if there are changes
HAS_CHANGES=$(git status --porcelain | grep -v '^.claude/' | grep -v 'PROJECT_LOG.md' || true)
if [ -z "$HAS_CHANGES" ]; then
    exit 0
fi

# Build the log entry
ENTRY="

---

## $(date '+%Y-%m-%d %H:%M') (自动记录)

### 文件变更

\`\`\`
$(git status --porcelain | grep -v '^.claude/' | grep -v 'PROJECT_LOG.md' || echo '(无)')
\`\`\`

### 变更摘要

_(待补充 — 请在此填写本次会话做了什么，为什么做)_

"

# Append to log file
echo "$ENTRY" >> "$LOG_FILE"
