---
name: sync
description: Save, check, and share the user's vault work. Use when the user says they're done, asks to save/share/sync/publish/push, wants others to see their changes, or asks to get the latest from collaborators.
---

# Sync the vault

Goal: the user's work is checked, shared on GitHub, and either merged or waiting for the right reviewer. Report the outcome in research terms.

## Steps

1. **Where are we?** `git status --short` and `git symbolic-ref --short HEAD`.
   - On `main` with changes: create `<username>/<topic>` (username from `gh api user -q .login`) and move the changes there with `git switch -c`.
2. **Commit** any uncommitted work with a descriptive message about the research change. Earlier `autosave:` commits are fine: the PR is squash-merged.
3. **Bring in collaborators' changes:** `git fetch origin`, then `git merge origin/main`.
   - **Conflict?** For each conflicted file, explain both versions to the user in plain language and ask which to keep, or propose a combination. Never pick silently in a note someone else owns. After resolving: `git add` and `git commit`.
4. **Check:** `python3 tools/check_vault.py`. Fix errors in files the user changed; mention (don't fix) errors in others' files.
5. **Share:** `git push -u origin <branch>`.
6. **Pull request:** if none exists for this branch (`gh pr view` fails), open one with `gh pr create --fill` plus a short body summarizing the research changes.
7. **Merge or request review.** Merge yourself with `gh pr merge --squash --delete-branch` only if **all** of these hold:
   - every changed file is under `logs/<username>/`, or in a project whose `index.md` lists the user as `owner`;
   - no result's `status` changed to `validated` (`git diff origin/main -- '*/results/*' | grep '^+status: validated'` finds nothing);
   - the validator passed.

   Otherwise leave it open, and tell the user who will review it (from `.github/CODEOWNERS` or the project owner).
8. **After merging,** `git switch main && git pull --ff-only`.

## Getting the latest only

If the user just wants collaborators' latest work: commit their changes on their branch, then `git fetch origin && git merge origin/main`, and summarize what arrived in plain language.
