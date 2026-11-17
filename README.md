# DevResearchHub (working name)

A shared, version-controlled research notebook for physics collaborations: derivations, results with provenance, meeting minutes, and personal logs in Markdown, with Claude handling all of the git.

**Prototype.** The conventions and tooling are being tried out; expect changes.

## How it works

- **You write; Claude keeps things in sync.** Open this folder in VS Code with the Claude Code extension. Edit notes yourself, or ask Claude to. When a session starts, Claude pulls collaborators' changes. While you work, your changes are autosaved to your own branch. When you're done, say "sync" and Claude checks your notes, shares them, and either merges them or asks the right person to review.
- **Results have provenance and history.** Every result records the code commit and data that produced it. Results are never deleted: a newer one *supersedes* the older one, and both stay linked.
- **Tasks live in GitHub Issues.** Action items from meetings become issues with an owner, so they can't get lost in the minutes.
- **Validated means reviewed.** Changing a result to `validated` requires a pull request approved by the project's owner.

## Getting started

1. Install [VS Code](https://code.visualstudio.com/), the Claude Code extension, [Git](https://git-scm.com/), and the [GitHub CLI](https://cli.github.com/). Then run `gh auth login`.
2. Clone this repo and open the folder in VS Code. Accept the recommended extensions.
3. Start a Claude session in the side panel. Try these:
   - "Start today's log."
   - "Record a new result for the pendulum project."
   - "Here are my notes from today's meeting: ..."
   - "Sync."

## Layout

| Folder | Contents |
|---|---|
| `projects/<name>/` | `index.md`, plus `derivations/`, `results/`, `figures/` |
| `meetings/` | `YYYY-MM-DD-topic.md` minutes |
| `logs/<username>/` | personal daily notebook |
| `references/` | paper notes |
| `templates/` | starting points for each note type |
| `tools/check_vault.py` | validator: frontmatter, provenance, and broken links |

`projects/example-pendulum/` shows every convention in a small worked example.

## Conventions in brief

- Use relative Markdown links (`[text](../results/x.md)`), not `[[wikilinks]]`.
- Write math as `$...$` and `$$...$$`.
- Keep code in its own repos and cite it as `repo@commit`. Keep data outside the vault and cite it by path or DOI.
- Files over 5 MB are refused by the autosave.

The full rules are in [CLAUDE.md](CLAUDE.md), which also tells Claude how to behave here.

## Repository admin (one-time)

- **Branch protection on `main`:** require a pull request, require review from Code Owners, and block force pushes.
- **`.github/CODEOWNERS`:** add each project's owner.
- **Labels:** add one per project (matching `label:` in the project's `index.md`).

## Related

- `SabrinaAIRetreat` (TheoryBench workbench): a Mattermost-based collaboration space whose GitHub adapter can show this repo's issues and files to collaborators.
