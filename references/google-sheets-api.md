# Google Sheets API — Outreach Tracker

Live connection to the Atrily outreach tracker. Read and update prospect status directly instead of pasting rows into chat.

## What's connected

- **Sheet:** "outreach" tab in [this Google Sheet](https://docs.google.com/spreadsheets/d/1q8e6SnYRsyl_1iolDQ77ANj50zuNgXj0hlNwvAO0Gt8/edit)
- **Columns:** `NAME | DATE | STATUS | LINKEDIN | NOTES | RAW_NOTES | DRAFT | LAST_SENT | TOUCH`
- **Auth:** Service account `aios-sheets@nithish-aios.iam.gserviceaccount.com`, key at `credentials/aios-sheets-key.json` (gitignored, never commit).
- **Scope:** `https://www.googleapis.com/auth/spreadsheets` — read/write on any sheet explicitly shared with this service account. No project-level IAM role granted; no access beyond this one Sheet.
- **Script:** `scripts/sheets_client.py`

## Column reference

| Column | Meaning |
|---|---|
| `NAME` / `LINKEDIN` | Prospect identity |
| `DATE` | **Day-0 anchor** — the date the initial DM was sent. Set once by `mark-sent` on the first send; never edited by hand after that, since every follow-up due-date is computed from it. |
| `STATUS` | `waiting` / `replied` / `booked` / etc. Anything other than blank or `waiting` stops the follow-up sequence — set it the moment someone replies. |
| `NOTES` | Free-text human notes (unchanged, e.g. "Call booked for Thu 3pm") |
| `RAW_NOTES` | Your unstructured paste dump per lead — About section, a post, team size, site blurb, job posting, tech stack. No pre-filtering; `/draft-outreach` does the synthesis. |
| `DRAFT` | Queued message awaiting your review/send. Edit the cell directly if you want to change the wording — that's the whole confirm/edit mechanism. |
| `LAST_SENT` | The actual text of the last message sent (copied from `DRAFT` by `mark-sent`) — gives the next follow-up something real to reference. |
| `TOUCH` | How many messages have gone out (0-5). Drives the follow-up schedule below. |

## Follow-up schedule

Fixed offsets from `DATE` (day 0), not gaps between touches:

| Touch sent so far | Next due | Offset from day 0 |
|---|---|---|
| 0 (nothing sent) | Initial DM | day 0, once `RAW_NOTES` is filled |
| 1 | Follow-up 1 | day 4 |
| 2 | Follow-up 2 | day 11 |
| 3 | Follow-up 3 | day 21 |
| 4 | Follow-up 4 | day 35 |
| 5 | Sequence complete | flagged for a manual call, not auto-continued |

**Known limitation:** `DATE` is stored as `DD-Mon` with no year; offset math assumes the current year. A thread that spans a year boundary (e.g. sent in December, followed up in January) will compute the wrong day count. Not an issue at current volume/recency — revisit if that changes.

## Drafting workflow (`/draft-outreach`)

1. `needs-draft` lists who's due right now (new leads with `RAW_NOTES`, or `waiting` leads past their next threshold) — skips anyone with a `DRAFT` already queued or no longer `waiting`.
2. The skill drafts each one (personalization bar + fallback ladder, using `references/voice.md`) and writes it back with `write-draft`.
3. You review/edit `DRAFT` directly in the Sheet, send by hand, then confirm with `mark-sent` — which records `LAST_SENT`, clears `DRAFT`, advances `TOUCH`, and (only on the first send) sets `DATE`/`STATUS`.

Full design reasoning: `decisions/log.md`, "Outreach personalization + follow-up automation".

## Setup (already done, for reference)

1. GCP project `nithish-aios`, Sheets API enabled.
2. Service account `aios-sheets` created, JSON key downloaded, moved to `credentials/aios-sheets-key.json`.
3. Outreach Sheet shared with the service account's email as **Editor**.
4. Python deps installed in a project-local venv: `python3 -m venv .venv && .venv/bin/pip install google-api-python-client google-auth`.

## Common commands

```bash
# List all prospects
.venv/bin/python3 scripts/sheets_client.py read

# Filter by status
.venv/bin/python3 scripts/sheets_client.py read --status waiting

# Update a prospect's status
.venv/bin/python3 scripts/sheets_client.py update "Sunesh Krishnan" --status replied

# Update status and notes together
.venv/bin/python3 scripts/sheets_client.py update "Sunesh Krishnan" --status booked --notes "Call booked for Thu 3pm"
```

`update` matches on exact `NAME` text (case-insensitive). If a name appears more than once, it updates the first match and warns.

```bash
# See who needs an initial DM or follow-up drafted right now
.venv/bin/python3 scripts/sheets_client.py needs-draft

# Write a drafted message into a lead's DRAFT cell
.venv/bin/python3 scripts/sheets_client.py write-draft "Sunesh Krishnan" "drafted opener text"

# Confirm a queued DRAFT was actually sent — advances the follow-up sequence
.venv/bin/python3 scripts/sheets_client.py mark-sent "Sunesh Krishnan"
```

## Extending

To add more sheets or tabs, share them with the same service account email and add a new `TAB_NAME`/range constant — no new credentials needed. To read a different range (e.g. a specific column subset), pass a custom `range` to `values().get()` instead of the whole tab name.
