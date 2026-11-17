---
name: new-result
description: Record a research result (number, fit, plot, or statement) as a vault note with full provenance. Use when the user reports a result, a plot, or a new value, or wants to replace/update an existing result.
---

# Record a result

1. **Find the project** under `projects/`. If none fits, ask whether to create one from `templates/project.md`.
2. **Gather provenance.** Ask for anything missing; don't invent it:
   - code repository and **commit hash** (offer to run `git -C <path> rev-parse --short HEAD` if the code is local);
   - exact command or parameters;
   - data location (path on cluster or storage, or DOI);
   - the figure file, if any (copy into `projects/<slug>/figures/` only if under ~5 MB).
3. **Write the note** at `projects/<slug>/results/<YYYY-MM-DD>-<short-slug>.md` from `templates/result.md`, `status: preliminary`.
4. **Replacing an older result?** Never edit its numbers. In the new note set `supersedes:`; in the old note set `status: superseded` and `superseded_by:`. Explain the difference between the two in the new note's body.
5. **Link it** from the project's `index.md` Key results table.
6. Run `python3 tools/check_vault.py` and fix any errors in the new note.
7. Tell the user it's recorded as preliminary, and that marking it validated goes through review (the `sync` skill opens the PR).
