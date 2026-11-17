# Research Hub: instructions for Claude

This repository is a shared research vault for a physics collaboration: derivations, results, meeting minutes, and personal logs, written in Markdown and versioned with git. Researchers edit files directly while talking to you. **You handle all git operations so they never have to.**

## Who you're working with

Physicists, many of them new to git. Talk about their work in research terms:

- Say "your changes are saved and shared", not "pushed to origin".
- Say "this is waiting for Alice to review", not "PR #12 is open".
- Name the branch, commit, or PR only when they ask or when it helps them find something.

## Layout

```
projects/<slug>/index.md          goals, owner, status, linked issues
projects/<slug>/derivations/      one derivation per note (Markdown + LaTeX math)
projects/<slug>/results/          one result per note, with provenance
projects/<slug>/figures/          small PNG/PDF plots (no raw data)
meetings/YYYY-MM-DD-<topic>.md    minutes; action items link to GitHub Issues
logs/<github-username>/YYYY-MM-DD.md   personal lab notebook, one file per day
references/                       paper notes
templates/                        starting points for each note type
tools/check_vault.py              validator (run before every merge)
```

## Note conventions

- **Links:** standard relative Markdown links, `[text](../results/foo.md)`. Never `[[wikilinks]]`; they don't render on GitHub or in the workbench.
- **Math:** `$...$` inline, `$$...$$` display. Long or paper-bound derivations go in `.tex` with a short Markdown note linking to them.
- **Code and data live elsewhere.** Cite code as `repo@commit` (e.g. `analysis-pipeline@a3f9c21`) and data by path or DOI. Never commit raw data, simulation output, or files over ~5 MB.
- **Frontmatter** is required on every note except `README.md`/`index` files in `references/`. Start from the matching file in `templates/`.

### Frontmatter schema

| type | required fields |
|---|---|
| `project` | `title`, `owner`, `status` (`active`/`paused`/`done`) |
| `derivation` | `title`, `owner`, `status` (`draft`/`checked`) |
| `result` | `title`, `owner`, `status` (`preliminary`/`validated`/`superseded`), `code`, `data` |
| `meeting` | `title`, `date`, `attendees` |
| `log` | `date`, `owner` |

A `superseded` result also needs `superseded_by`. `code` and `data` may be `n/a` only with a reason in the body.

## Results rules (the most important rules here)

1. **Never delete or overwrite a result.** To change a result, create a new note, set the old one to `status: superseded` with `superseded_by:` pointing to the new note, and link back with `supersedes:`.
2. **Never set `status: validated` yourself on someone's behalf.** Promotion to validated happens only through a reviewed pull request (see below).
3. Every result must say how to reproduce it: code commit, data location, and parameters.

## Git workflow (you do this automatically)

**Shared branch.** Work merges into the branch named in `.claude/trunk`, or `main` if that file is missing. In this checkout it is **`demo`**: the pilot runs there, and `main` holds the clean prototype. Never commit to, push to, merge into, or open PRs against `main` from a demo checkout. "The shared branch" below means this branch.

Hooks in `.claude/settings.json` already:
- pull the latest changes when a session starts (and tell you the state),
- autosave-commit after each of your turns, **on work branches only** (never on `main` or the shared branch),
- push the current work branch when the session ends.

Your job on top of that:

1. **Before the first edit in a session**, if you're on the shared branch or `main`, create a branch named `<github-username>/<short-topic>` (e.g. `dsjamieson/oscillator-check`). Get the username with `gh api user -q .login`. If the user already has an unmerged branch for the same topic, continue on that one instead.
2. **Commit at logical checkpoints** with a clear message describing the research change ("Add second-order correction to pendulum period"), not "update files". The autosave hook is a safety net, not a substitute.
3. **When the user says the work is done** (or asks to share/sync), use the `sync` skill: run the validator, push, and open a pull request.
   - **Merge it yourself** (`gh pr merge --squash --delete-branch`) only if every changed file is in the user's own `logs/<username>/`, or in a project they own (`owner:` in its `index.md`), **and** no result changed to `validated`.
   - Otherwise leave the PR open for the CODEOWNER and tell the user who will review it.
4. **Merge conflicts:** never resolve conflicts in someone else's notes silently. Show the user both versions in plain language and ask which to keep.
5. **Never** force-push, push directly to `main` or the shared branch, rewrite published history, or run `git reset --hard`. These are also blocked in settings and by branch protection.

## Skills in this repo

- `sync`: save, check, share, and merge or request review.
- `new-result`: record a result note with full provenance.
- `meeting-minutes`: turn rough notes into minutes and file action items as GitHub Issues.

## Related project

The Mattermost-based collaboration workbench (TheoryBench, in the sibling `SabrinaAIRetreat` repo) can bind this repository through its GitHub adapter to show issues and files to collaborators. That workbench does no git writes; this repository's Claude workflow is the writing side.
