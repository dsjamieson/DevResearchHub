---
name: sync
description: Save, check, and share the user's vault work. Use when the user says they're done, asks to save/share/sync/publish/push, wants others to see their changes, or asks to get the latest from collaborators.
---

# Sync the vault

Goal: the user's work is checked, shared on GitHub, and either merged or waiting for the right reviewer. Report the outcome in research terms. **Finish every step or tell the user exactly which step stopped and why.** Never end with work committed locally but not shared without saying so.

**Shared branch:** `TRUNK=$(cat .claude/trunk 2>/dev/null || echo main)`. All work merges into `$TRUNK`. Never commit to, push to, or open PRs against any other base. On a demo checkout `$TRUNK` is `demo`, and `main` must not be touched.

## Steps

1. **Where are we?** `git status --short` and `git symbolic-ref --short HEAD`.
   - On `$TRUNK` (or `main`) with changes: create `<username>/<topic>` (username from `gh api user -q .login`) with `git switch -c`, which carries the changes along.
2. **Commit** any uncommitted work with a descriptive message about the research change. Earlier `autosave:` commits are fine because the PR is squash-merged.
3. **Bring in collaborators' changes:** `git fetch origin`, then `git merge origin/$TRUNK`.
   - **Conflict?** For each conflicted file, explain both versions to the user in plain language and ask which to keep, or propose a combination. Never pick silently in a note someone else owns. After resolving, `git add` and `git commit`.
4. **Check:** `python3 tools/check_vault.py`. Fix errors in files the user changed. Mention errors in other people's files, but don't fix them.
5. **Share:** `git push -u origin <branch>`.
6. **Pull request:** if none exists for this branch (`gh pr view` fails), open one with `gh pr create --base $TRUNK --fill` plus a short body summarizing the research changes.
7. **Merge or request review.** Merge it yourself with `gh pr merge --squash --delete-branch` only if **all** of these hold:
   - every changed file is under `logs/<username>/`, or in a project whose `index.md` lists the user as `owner`;
   - no result's `status` changed to `validated` (`git diff origin/$TRUNK -- '*/results/*' | grep '^+status: validated'` finds nothing);
   - the validator passed.

   Otherwise leave it open and tell the user who will review it (from `.github/CODEOWNERS` or the project owner). If GitHub refuses the merge (branch protection), say so plainly and leave it for review.
8. **After merging:** `git switch $TRUNK && git pull --ff-only`.
9. **Report:** one or two sentences: what was shared, where it is, and what (if anything) is waiting on whom.

## Getting the latest only

If the user just wants collaborators' latest work: commit their changes on their branch, then `git fetch origin && git merge origin/$TRUNK`, and summarize in plain language what came in.
