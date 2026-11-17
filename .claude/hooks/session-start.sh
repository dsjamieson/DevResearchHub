#!/usr/bin/env bash
# SessionStart hook: bring the vault up to date and tell Claude the git state.
# Anything printed to stdout is added to Claude's context.
set -u
cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0
git rev-parse --git-dir >/dev/null 2>&1 || exit 0

branch=$(git symbolic-ref --short HEAD 2>/dev/null || echo "(detached)")
# The shared branch work merges into: .claude/trunk if present, else main.
default=$(tr -d '[:space:]' < .claude/trunk 2>/dev/null); default=${default:-main}

if git remote get-url origin >/dev/null 2>&1; then
  if git fetch --quiet --prune origin 2>/dev/null; then
    if git rev-parse --verify --quiet "origin/$branch" >/dev/null; then
      if ! git pull --quiet --rebase --autostash origin "$branch" 2>/dev/null; then
        git rebase --abort 2>/dev/null
        echo "WARNING: automatic update of '$branch' hit a conflict and was undone. Use the sync skill to resolve it with the user."
      fi
    fi
  else
    echo "Note: could not reach GitHub; working offline. Changes will be shared later."
  fi
fi

echo "Vault git state (shared branch: $default):"
echo "- current branch: $branch"
echo "- uncommitted files: $(git status --porcelain | wc -l | tr -d ' ')"
if [ "$branch" != "$default" ] && git rev-parse --verify --quiet "origin/$default" >/dev/null; then
  behind=$(git rev-list --count "HEAD..origin/$default" 2>/dev/null || echo "?")
  echo "- commits on $default not yet in this branch: $behind"
fi
if [ "$branch" = "$default" ]; then
  echo "- on $default: create a <username>/<topic> branch before the first edit (see CLAUDE.md)."
fi
if [ "$branch" = "main" ] && [ "$default" != "main" ]; then
  echo "- WARNING: on main, but this checkout's shared branch is $default. Switch to $default before working."
fi
mine=$(git branch --format='%(refname:short)' | grep -vE "^($default|main)\$" | head -10 | tr '\n' ' ')
[ -n "$mine" ] && echo "- local work branches: $mine"
exit 0
