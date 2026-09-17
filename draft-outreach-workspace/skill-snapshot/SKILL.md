---
bike-method-phase: 1  # Phase 1 — Training wheels. Run manually first.
three-ms-attribution: |
  Adapted from The Three Ms of AI™ © 2026 Nate Herk.
name: draft-outreach
description: Use when someone wants to draft outreach openers/follow-ups for the Atrily outreach tracker, batch-draft LinkedIn DMs from raw prospect notes, or check who's due for a follow-up. Triggers on "draft outreach", "who needs a follow-up", "/draft-outreach".
---

# Draft Outreach

Batch-drafts personalized openers and scheduled follow-ups into the live outreach Google Sheet, from raw notes you've already pasted in. You review and send by hand — this never sends anything itself.

Shipped by `/level-up` on 2026-09-10. Spec and reasoning: `decisions/log.md` entry "Outreach personalization + follow-up automation".

## What this solves

Signal-finding and matching-signal-to-pain-point is the actual bottleneck, not typing. You paste a raw, unstructured dump of whatever you found (LinkedIn About/posts, team size, site blurb, job posting, tech stack — no pre-filtering). This skill does the harder synthesis: pick the strongest signal, apply the fallback ladder if nothing jumps out, write the opener + value prop, and queue it in the Sheet for you to review and send.

## Inputs

- `references/signal-pain-point-map.md` — the actual synthesis tool: which raw signal maps to which pain point, and the diagnostic question that tests it. Read this in full before drafting; it's the difference between a generic line and one that couldn't have gone to anyone else.
- `context/about-business.md` — ICP and the offer, for context on who these prospects are (not pain points — that's the map above)
- `references/voice.md` — tone: lowercase-casual, short lines, self-aware, no generic pitch energy. Sample 2 (the opener that actually got a reply) is the target shape: one observation, then one open question.
- `references/follow-up-messaging.md` — for follow-up touches specifically: the value-add rule (never a purely logistical "just circling back"), how to personalize using `LAST_SENT`/`RAW_NOTES`, and patterns that kill a sequence. Read before drafting touch 2+.
- `scripts/sheets_client.py needs-draft` — the queue: who needs an initial DM or a follow-up right now
- Full column reference and follow-up schedule: `references/google-sheets-api.md`

## The personalization bar

The output shape is **signal + one open question** — not a value-prop pitch. A pitch invites silence; a specific question invites a reply. This is what Nithish's one message that actually got a reply looked like, and it's why the map exists: matching a real signal to the pain point it implies, then asking the question that tests whether that pain is real for them.

**How to find it:**
1. Read the lead's `RAW_NOTES` closely — it's an unfiltered dump, so several rows in the map may look like they apply. Match against `references/signal-pain-point-map.md` and pick the single strongest hit: named/specific beats vague, something they said themselves beats something you inferred.
2. If more than one signal matches, prefer the one that routes to a primary pain point (#3 ROI proof or #5 fragmented systems — see the map's legend) over an advanced one (#1, #2, #6, or the HR-angle read of #4). If nothing points anywhere specific, #5 is the default — it's the easiest to verify and lowest-friction to ask about.
3. Write the opener: the specific detail, then the map's question for that pain point, adapted to sound like Nithish (lowercase, short, curious — not interrogating). The map's sample questions are starting points, not scripts to copy verbatim.
4. Test it: *could this exact line have gone to 500 other people unedited?* If yes, it fails — go back to step 1 and look for a sharper signal, or don't send it.

**Fallback ladder** when nothing in `RAW_NOTES` matches a row in the map:
1. A trigger event mentioned in the notes (recent hire, new tool, expansion) — ask what changed for them, in their own words
2. Shared context (same LinkedIn group, mutual connection, same location)
3. If none of the above clear the bar even after re-reading `RAW_NOTES` closely — don't force it. Write `SKIP` with a one-line reason instead of sending something generic.

Follow-ups reference `LAST_SENT` (what actually went out last time) — pick a *different* signal/question from the map if one exists in `RAW_NOTES`, so it doesn't repeat the same ask. If no second signal exists, keep it a light nudge continuing the thread rather than restating the opener.

## Execution

1. Run `.venv/bin/python3 scripts/sheets_client.py needs-draft`. This lists every lead due for a draft right now — either a brand-new lead with `RAW_NOTES` filled in, or a `waiting` lead whose next follow-up (day 4 / 11 / 21 / 35 from the initial DM) is due. It skips anyone who already has a queued `DRAFT`, and anyone no longer `waiting` (they replied — sequence stops).
2. For each lead in the list, using their `RAW_NOTES` (and `LAST_SENT` if this is a follow-up):
   - Match against `references/signal-pain-point-map.md` per the process above, or fall back per the ladder
   - Write the opener (signal + question, in voice), or `SKIP — <reason>` if nothing clears the bar
3. Write each result with `.venv/bin/python3 scripts/sheets_client.py write-draft "Full Name" "drafted text"` (or leave `SKIP — reason` as plain text in the same DRAFT cell if nothing qualified — don't call `mark-sent` on a skip).
4. Report a one-line summary: how many drafted, how many skipped and why, how many hit "sequence complete" (4 follow-ups sent, no reply — flagged by `needs-draft`, needs your manual call on whether to keep going).

## After you review and send

You review each `DRAFT` in the Sheet — edit the cell directly if you want to change the wording before sending, that's the whole "confirm/edit" mechanism, no separate step needed. Once actually sent, run:

```
.venv/bin/python3 scripts/sheets_client.py mark-sent "Full Name"
```

This copies the sent text into `LAST_SENT`, clears `DRAFT`, advances `TOUCH`, and — only on the very first send — sets `DATE` to today and `STATUS` to `waiting` (this anchors the whole day-0/4/11/21/35 schedule, so don't touch `DATE` by hand after that).

If a `SKIP` was written instead of a real draft, don't run `mark-sent` — just add more to `RAW_NOTES` (dig into their site/news/job posts) and re-run `needs-draft` later, or leave them and move to the next prospect.

## Boundaries

- Never sends a message itself — `DRAFT`/`LAST_SENT` are text in a spreadsheet cell, sending is always manual.
- Never overwrites a `DRAFT` that's already queued — `needs-draft` skips those on purpose so you don't lose an edit you made before sending.
- Never advances `TOUCH` or touches `DATE` except through `mark-sent`, and only when a real draft was pending.
