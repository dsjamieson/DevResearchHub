#!/usr/bin/env bash
# Stop hook: after each Claude turn, snapshot all changes (the user's and
# Claude's) on the current work branch. Never commits on main or the shared branch. Local only;
# pushing happens at session end or through the sync skill.
set -u
cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0
git rev-parse --git-dir >/dev/null 2>&1 || exit 0

branch=$(git symbolic-ref --short HEAD 2>/dev/null) || exit 0
trunk=$(tr -d '[:space:]' < .claude/trunk 2>/dev/null); trunk=${trunk:-main}
[ "$branch" = "main" ] || [ "$branch" = "$trunk" ] && exit 0
[ -z "$(git status --porcelain)" ] && exit 0
# Don't interfere with an in-progress merge or rebase.
gd=$(git rev-parse --git-dir)
[ -e "$gd/MERGE_HEAD" ] || [ -d "$gd/rebase-merge" ] || [ -d "$gd/rebase-apply" ] && exit 0

git add -A
# Unstage anything over 5 MB: data belongs outside the vault.
big=""
while IFS= read -r f; do
  [ -f "$f" ] || continue
  size=$(wc -c <"$f" | tr -d ' ')
  if [ "$size" -gt 5242880 ]; then
    git reset -q -- "$f"
    big="$big $f"
  fi
done < <(git diff --cached --name-only)

git diff --cached --quiet && exit 0
git commit -q --no-verify -m "autosave: $(date '+%Y-%m-%d %H:%M')"

if [ -n "$big" ]; then
  echo "{\"systemMessage\": \"Autosave skipped large files (over 5 MB, keep data outside the vault):$big\"}"
fi
exit 0
