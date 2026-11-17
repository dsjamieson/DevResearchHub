#!/usr/bin/env bash
# SessionEnd hook: final autosave, then back up the work branch to GitHub so
# nothing is lost if the laptop dies. Never pushes main or the shared branch.
set -u
cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0
git rev-parse --git-dir >/dev/null 2>&1 || exit 0

"$(dirname "$0")/autosave.sh" >/dev/null 2>&1

branch=$(git symbolic-ref --short HEAD 2>/dev/null) || exit 0
trunk=$(tr -d '[:space:]' < .claude/trunk 2>/dev/null); trunk=${trunk:-main}
[ "$branch" = "main" ] || [ "$branch" = "$trunk" ] && exit 0
git remote get-url origin >/dev/null 2>&1 || exit 0
git push -q -u origin "$branch" 2>/dev/null || true
exit 0
