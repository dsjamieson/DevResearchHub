# Pilot: try the research hub in about an hour

> **The pilot runs on the `demo` branch.** Everything you do here merges into `demo`, never `main`, so the pilot can be thrown away afterwards.

Thanks for testing this. We want to find out what works and what gets in the way **before** anyone relies on it, so friction is the most useful thing you can report. Whenever something confuses you, annoys you or surprises you, write it down (step 7).

**What you'll do:** together we'll solve a small physics problem using the hub. You'll write notes yourself, ask Claude to help, and let Claude handle all the git. You shouldn't need to type a single git command. If you end up needing to, that's a finding.

| Step | What it tests | Time | When |
|---|---|---|---|
| 1. Setup | Getting started from nothing | 15 min | on your own |
| 2. Daily log | Writing and sharing your own notes | 5 min | on your own |
| 3. Your role in the problem | Derivations, results, provenance | 20 min | on your own |
| 4. Everyone edits one file | Simultaneous edits and conflicts | 10 min | together |
| 5. Validate the result | Review before a result counts | 10 min | together |
| 6. Group meeting | Minutes and task assignment | 15 min | together |
| 7. Feedback | | 5 min | on your own |

---

## 1. Setup (15 min)

1. Install [VS Code](https://code.visualstudio.com/), [Git](https://git-scm.com/downloads) and the [GitHub CLI](https://cli.github.com/).
2. In a terminal, run `gh auth login` and follow the prompts. Then run:
   ```
   gh repo clone dsjamieson/DevResearchHub DevResearchHub-demo -- -b demo
   ```
   This downloads the `demo` branch into a folder called `DevResearchHub-demo`.
3. In VS Code, use **File → Open Folder** to open the `DevResearchHub-demo` folder. Install the recommended extensions when prompted, including **Claude Code**.
4. Open the Claude panel and start a session. If asked whether to trust the folder, say yes. That lets the repo's automatic sync run.
5. Ask Claude: **"What's the state of the vault?"**

**Should happen:** Claude says you're up to date and on `demo`.
**Note:** how long setup took, and anything that failed or needed help.

## 2. Daily log (5 min)

Ask Claude: **"Start today's log. Today I set up the research hub."** Look at the file it creates and edit it yourself if you like. Then say **"sync"**.

**Should happen:** your log appears on GitHub under `logs/<your-username>/`. It's yours, so Claude merges it without review.
**Note:** did you understand what Claude told you it had done?

## 3. Your role in the problem (20 min)

**The problem.** A driven, damped oscillator obeys

$$
\ddot x + 2\gamma\,\dot x + \omega_0^2 x = \frac{F}{m}\cos\omega t .
$$

At what driving frequency is the steady-state amplitude largest, and how does that compare with $\omega_0$? Use $\omega_0 = 1$ and $\gamma = 0.1$.

The project page is [projects/pilot-resonance/index.md](projects/pilot-resonance/index.md). The organizer will tell you your role:

- **Deriver:** derive the amplitude-resonance frequency analytically. Ask Claude to start a derivation note, then write or check the steps yourself. Mark it `checked` only if someone else has verified it.
- **Computer:** find the peak numerically with any short script you like. Put the script somewhere outside the vault (your own repo or a GitHub gist) and ask Claude to **"record a new result for the pilot-resonance project"**. Claude will ask for the code commit and parameters, so have them ready.
- **Reviewer:** read the Deriver's and Computer's notes on GitHub once they've synced. Do they agree with each other? You'll approve the result in step 5.
When your part is done, say **"sync"**.

**Should happen:** your notes go into a pull request reviewed by the project owner, because the project isn't yours.
**Note:** was it clear what Claude needed from you? Did the derivation's math render properly?

## 4. Everyone edits one file (10 min, together)

At the same moment, everyone edits the **Current status** paragraph of [the project page](projects/pilot-resonance/index.md) to say something different, then says **"sync"**. The organizer merges the pull requests one at a time. When yours is next, say **"sync"** again.

**Should happen:** the first person's change goes in cleanly. Everyone after that gets a plain-language explanation from Claude of the two versions, and a question about which to keep or how to combine them.
**Note:** did you understand the conflict? Did you trust the result?

## 5. Validate the result (10 min, together)

- **Computer:** ask Claude to **"mark the resonance result as validated"**.
- **Reviewer:** you'll be asked to review the pull request on GitHub. Check the result against the derivation, then approve it or request changes. You can also ask your own Claude session to **"review the open pull request for the resonance result"**.

**Should happen:** Claude won't merge this on its own. The result shows as `validated` only after the Reviewer approves.
**Note:** was the review step useful, or just in the way?

## 6. Group meeting (15 min, together)

Hold a short meeting about the problem. One scribe types rough notes in any format. Agree on at least two follow-up tasks, each with an owner. Afterwards the scribe pastes the notes and asks Claude to **"write up the minutes for today's meeting"**.

**Should happen:** minutes appear in `meetings/`. Claude confirms the action items with the scribe, then files them as GitHub Issues assigned to their owners.
**Note:** were the minutes accurate? Was anything invented or lost?

## 7. Feedback (5 min)

Open a **Pilot feedback** issue on GitHub (Issues → New issue → Pilot feedback) and answer its questions. Short answers are fine.

---

## For the organizer

Before the pilot:

- [ ] Add each participant as a collaborator with write access (repo Settings → Collaborators).
- [ ] Assign the roles, and put the Reviewer's GitHub username in [.github/CODEOWNERS](.github/CODEOWNERS) for `projects/pilot-resonance/results/`.
- [ ] Turn on branch protection for `demo` (and `main`): require a pull request and require review from Code Owners. Code owners can't approve their own PRs, so as the repo admin you'll need to merge your own project PRs with the admin override.
- [ ] Create the `pilot-resonance` and `pilot-feedback` labels.

During steps 4–6, merge PRs one at a time and watch where people hesitate. That's often more informative than the written feedback.

**Answer for checking:** the amplitude peaks at $\omega_r = \sqrt{\omega_0^2 - 2\gamma^2} = \sqrt{0.98} \approx 0.98995$, slightly below $\omega_0$.
