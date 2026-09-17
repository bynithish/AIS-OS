---
title: "Follow-up messaging: the value-add rule"
---

# Follow-up messaging: the value-add rule

Interpreted summary of a clipped guide on LinkedIn follow-ups. Full source: `raw/articles/LinkedIn Outreach Follow-Up Messages That Don't Feel Pushy (With Real Templates).md`. This is a learning resource for writing follow-up copy in `/draft-outreach` — it doesn't change the mechanics of that skill (Sheet columns, `TOUCH` counter, `mark-sent`), just the judgment behind what goes in the `DRAFT` cell for a follow-up touch.

## The one rule that matters

**Never send a follow-up that's purely logistical.** "Just circling back" / "following up on my last message" adds zero value — a reminder that they didn't respond creates guilt, not engagement. It's the same "pitch invites silence" dynamic [[signal-pain-point-map]] already warns about for openers, just applied to touch 2+ instead of touch 1.

Every follow-up should hand the prospect something they didn't have before reading it: a stat, a case study, a specific observation, a free resource, or a genuinely interesting question — not just a hook back to the same ask.

## Why non-pushy follow-ups work (the three levers)

- **Reciprocity** — give something useful (stat, framework, case study) and the prospect feels a natural pull to acknowledge it, even briefly.
- **Curiosity gaps** — end with a real question, not a fake "thoughts?" — one that would genuinely sharpen your own understanding of their situation.
- **Low-stakes exits** — give an explicit, dignified way to say no ("no worries if the timing's off, happy to check back in a few months"). Removing pressure paradoxically raises response rates.

This lines up with the existing personalization bar in `/draft-outreach`'s SKILL.md — signal + one open question, not a pitch. The source extends that same shape across the whole follow-up sequence, not just the opener.

## Personalizing a follow-up specifically (not just the opener)

Mail-merge personalization (first name + company name) reads as fake. Four things worth referencing instead, in order of how "alive" they feel to the prospect:

1. Their recent LinkedIn post (last 30 days) — the specific argument, not "loved your post"
2. A company milestone (job change, funding, launch, award)
3. An industry trigger relevant to their business (regulation, competitor move, market shift)
4. Something they said in a prior interaction (a like, a comment, a partial reply) — proves the thread is continuous

Practical version for batch drafting: scan activity for everyone due a follow-up before writing, take one specific note per person, write from that note. This is exactly what `RAW_NOTES` + `LAST_SENT` are for in the outreach Sheet — the source is describing the same workflow `/draft-outreach` already automates the drafting half of.

## Handling a reply that isn't a yes

If a follow-up actually gets a response — pushback, an objection, a soft no — that's the best outcome a follow-up can produce; they're back in the conversation. Three common shapes:

- **Timing objection** ("not looking at this right now") — don't push. Ask when it'd become relevant and note it, rather than arguing the timing.
- **Incumbent objection** ("already have something in place") — don't compare/criticize. Ask what they're using and position as complementary, not competitive.
- **Hard no** ("looked at this, not a fit") — thank them, exit cleanly, leave the door open. A graceful exit is what gets referrals or a return later.

## Patterns that kill a sequence

- "Just following up on my last message" (see the rule above)
- Two sales-forward pitches back to back
- Passive aggression ("I guess you're not interested")
- 3 messages in one week — reads as desperation, not persistence
- Switching the core value prop mid-sequence — stay coherent across touches
- Repeating the same ask verbatim instead of changing the angle

## Timing: 5-touch cadence confirmed, and what goes in each touch

Resolved 2026-09-15 (see `brainstorms/2026-09-15-voice-and-self-presentation.md`, Q9/Q12): the fixed 4/11/21/35-day schedule `scripts/sheets_client.py` already implements is Nithish's actual preference, not a placeholder — the source's own cadence (day 4, +7, +10, +14 ≈ day 4/11/21/35) independently lands close to the same numbers, which is confirmation, not a discrepancy to resolve.

The real gap was never timing — it was not knowing what to put in each follow-up. Resolved using the source's own per-message structure (its Sequence 1, adapted to [[voice]] — never its literal template wording, which uses permission-asking/enthusiasm language Nithish's voice rules cut):

| Touch | Day | Content |
|---|---|---|
| 1 | 0 | Binary signal question — see [[signal-pain-point-map]] |
| 2 | 4 | A relevant stat or specific observation (a second `RAW_NOTES` signal can serve as the observation if one exists), ending in one binary/testable question |
| 3 | 11 | An anonymized case study tied to their pain point ("cut X by Y% for a similar agency") |
| 4 | 21 | **Unresolved, defaults to touch-1 shape.** Signal + one question, anchored to the pain point already raised earlier in the thread — no offer name, no link, no referral ask. See the note below; this row was rewritten twice on 2026-09-15 and still isn't right. |
| 5 | 35 | Graceful break-up — warm, no passive-aggression, door open, sequence-complete either way |

**Touch 4, still open (2026-09-15):** two attempts at "name the offer directly" both missed — one pitch-slapped with a link and a paragraph, the next read as two fragmented clauses stapled together. Asked to write the real line himself, Nithish's answer was a referral ask ("who do you know who'd be interested in this?"), not a self-booking pitch — and not personalized to the specific lead. His own read: he doesn't know what actually works yet, since nothing here has real reply data behind it. Defaulting touch 4 to the same signal+question shape as every other touch until leads actually reach it and there's something real to learn from. "Name the offer" and "ask for a referral" are both live hypotheses, not decided — see [[voice]] "the offer only surfaces after intensity is confirmed."

Each touch still changes the angle, never repeats the same ask, and never switches the underlying value prop mid-sequence (per the anti-patterns below).

## Multi-channel note (not yet applicable)

The source recommends layering in email or LinkedIn voice notes after LinkedIn-only follow-ups go quiet. Per `connections.md`, Gmail integration is still a Day 2 task and there's no voice-note capability in the current outreach system — noting this as a future lever, not something `/draft-outreach` can act on yet.
