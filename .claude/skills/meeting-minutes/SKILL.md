---
name: meeting-minutes
description: Turn rough meeting notes, a transcript, or a chat thread into structured minutes in meetings/, and file each action item as a GitHub Issue. Use when the user shares meeting notes or asks to write up a meeting.
---

# Write up meeting minutes

1. **Create** `meetings/<YYYY-MM-DD>-<topic>.md` from `templates/meeting.md`. Fill attendees and scribe (ask if unclear).
2. **Organize** the raw notes into Discussion (by topic), Decisions, and Action items. Keep physics content precise: preserve equations, numbers, and who said what when it matters. Don't add conclusions that weren't reached.
3. **Link** discussed projects, results, and derivations with relative Markdown links.
4. **Confirm action items with the user** (task, owner, due date) before filing anything.
5. **File each action item** as an issue:
   `gh issue create --title "<task>" --assignee <owner> --label <project-label> --body "From [meeting <date>](<path to minutes>)"`
   Record the returned issue number in the minutes (`#<n>`). If a label doesn't exist yet, skip `--label` and say so.
6. Run `python3 tools/check_vault.py`, then offer to sync.
