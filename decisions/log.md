# Decisions Log

Append-only record of meaningful decisions and why they were made. `/level-up` Phase 2 (Method interview) writes scoped automation specs here. You can also append manually whenever you decide something worth remembering.

**Format per entry:**

```
## YYYY-MM-DD — Short title

**Decision:** what was decided.

**Why:** the reasoning, constraints, and what would change your mind.

**Alternatives considered:** what else was on the table.

**Owner:** who's accountable.
```

Keep it terse. Future-you will thank present-you for capturing the *why*, not just the *what*.

---

## 2026-09-15 - Touch 4 reverted to unresolved after two failed drafts and an honest "I don't know"

**Decision:** Reverted `draft-outreach/SKILL.md` and `references/follow-up-messaging.md`'s touch-4 (day 21) guidance from "name the discovery call directly" back to the same signal+question shape as every other touch. Marked it explicitly unresolved rather than picking a third guess.

**Why:** Two drafted attempts at "name the offer directly" both missed Nithish's voice — first as a pitch-slap (multi-sentence value-prop + a Calendly link), then as two fragmented clauses stapled together with a dash. Asked to write the actual line himself, his answer was a referral ask ("who do you know who'd be interested in this?") — a different move entirely, not personalized to the lead, and inconsistent with the personalization bar the rest of the skill enforces. He then said directly: he doesn't know what actually works yet, because none of this has been tested against real replies. Rather than keep guessing at wording, the honest move is to default to the one pattern with any real grounding (signal + question, consistent with touches 1-3) and flag "name the offer" / "ask for a referral" as hypotheses to A/B test once real leads reach touch 4 — not ship a guess as a decided rule.

**Alternatives considered:** A third rewrite attempt at the "name the offer" wording. Rejected — two misses plus an explicit "I don't have a clue what works" is a signal to stop guessing, not try harder at the same approach.

**Not done:** The skill-creator eval for this case (`eval-touch4-names-the-offer`, since renamed `touch4-defaults-to-signal-and-question`) was updated to test the new expected behavior, but the full 10-run benchmark from earlier today was not re-run — only a targeted single-case check. `iteration-1/benchmark.json`'s touch-4 finding (new skill 4/4 vs old skill 2/4) is now stale; it graded against the "name the offer" rule that no longer stands.

**Owner:** Nithish.

## 2026-09-15 - Voice/self-presentation interview: resolved two live conflicts, closed the follow-up-content gap

**Decision:** Ran a `/grill-me` session on voice, thinking, and self-presentation to feed a `skill-creator` update of `/draft-outreach`. Captured and merged into canonical pages:
- Sharper voice blocklist (permission-asking, hedging, generic questions, enthusiasm markers, filler compliments) and the actual line that matters: never show uncertainty about *ability to solve the problem*, uncertainty about journey/problem itself is fine → `references/voice.md`.
- Confirmed opener formula: `"Saw [specific signal]. [Binary question]."` — one binary question, not open-ended → `references/voice.md`.
- **Resolved a real conflict**: `raw/dm-writing-context.md`'s "one follow-up only" rule was a placeholder (he didn't know what to put in touches 2-5), not a considered preference — the 5-touch day 0/4/11/21/35 cadence already shipped is correct. Closes the "Open, not decided" note in the follow-up-messaging-guide entry below.
- **Resolved a second real conflict**: offer pricing. Neither `raw/dm-writing-context.md` (10%-of-savings) nor the pre-existing `context/about-business.md` (50%-upfront-refund, no pricing %) had the full current offer. Corrected `about-business.md`: 24h turnaround → 2-week pilot priced at 10% of annual savings → 50% upfront → if it doesn't work, a second 2-week extension before any refund → retainer upsell if it works.
- Filled the actual gap behind the cadence: what goes in each follow-up touch, sourced from the previously-clipped follow-up guide, adapted to voice not copied → `references/follow-up-messaging.md`.
- Installed `blader/humanizer` (global skill, 6.8K installs, clean Gen/Socket/Snyk checks) as a complementary post-draft polish pass — strips generic AI tells, doesn't replace the voice-specific rules above.

**Why:** Two contradictions between working docs and shipped behavior would have kept getting silently guessed at (or silently overridden) every time `/draft-outreach` ran, without ever being decided on purpose. Interviewing surfaced both explicitly instead of picking one myself.

**Not done this session:** `draft-outreach/SKILL.md` itself not yet rewritten — that's the next step, via `skill-creator`, briefed with everything above. Reply-mode voice (once a prospect responds) and discovery-call conduct weren't covered — flagged as future `/grill-me` candidates.

**Owner:** Nithish.

## 2026-09-15 - Ingested follow-up messaging guide, new reference page for `/draft-outreach`

**Decision:** Clipped "LinkedIn Outreach Follow-Up Messages That Don't Feel Pushy" to `raw/articles/`. Created `references/follow-up-messaging.md` as the interpreted summary (value-add rule, non-pushy psychology, follow-up-specific personalization, objection handling, anti-patterns) and linked it from `/draft-outreach`'s SKILL.md Inputs (both `.claude/` and `.agents/` mirrors) as required reading before drafting touch 2+.

**Why:** Nithish flagged it as a learning resource for follow-up copy in the outreach system, not a spec change — this fills a real gap, since the existing `references/signal-pain-point-map.md` only covers opener signal-matching, nothing follow-up-specific.

**Open, not decided:** the source's suggested cadence (day 4/7/10/14) differs from the fixed 4/11/21/35-day schedule already implemented in `scripts/sheets_client.py`. Left as a noted discrepancy in the new reference page, not applied — one source isn't enough to justify changing a shipped, tested schedule.

**Owner:** Nithish.

## 2026-09-15 - Ingested the actual "LLM Wiki" source, grounding the earlier paraphrase

**Decision:** Nithish clipped the actual source doc (Karpathy's gist) to `raw/assets/llm-wiki.md`. Created [[llm-wiki-pattern]] in `references/` as the interpreted summary, and linked it from the "How the wiki grows" section in `CLAUDE.md`/`AGENTS.md`. Left the two prior same-day decisions (below) standing — the real text confirms both calls (skip `index.md`, reuse `decisions/log.md`) since the source itself says everything in it is optional and expects divergence.

**Why:** The earlier two entries below adapted this pattern from memory/paraphrase before the source file existed anywhere in the repo. Now that it's actually in `raw/`, the wiki page can cite it directly instead of resting on a secondhand description.

**Open, not decided:** the source suggests three things this AIOS hasn't adopted or rejected yet — a parseable `## [date] type | Title` log prefix, filing good query answers back into the wiki as new pages, and two extra lint checks (concept mentioned but has no page; data gaps fillable by search). Left as open questions in [[llm-wiki-pattern]] rather than auto-adopted.

**Owner:** Nithish.

## 2026-09-15 - Added `raw/` after all, correcting the same-day "no raw folder" call

**Decision:** Reversed part of the same-day decision below. Added a gitignored `raw/` folder for immutable source material (Fireflies call transcripts, clipped articles, prospect notes worth keeping verbatim). `context/`/`references/` stay interpreted-only; `raw/` is what they're built from.

**Why:** Nithish pushed back, correctly. The `EXPANSIONS.md` anti-pattern ("don't dump raw archives into `references/`") is a warning against polluting the interpreted layer, not a ban on having a raw layer at all — a separate `raw/` folder is the actual fix for that problem. Also, `connections.md` already earmarked "local storage" as the planned destination for Fireflies meeting notes; that need already existed, it just had no folder assigned.

**Alternatives considered:** Leaving it out per the original same-day reasoning. Rejected: it conflated "don't mix raw into the wiki" with "don't have raw material anywhere," and ignored a need already on record in `connections.md`.

**Owner:** Nithish.

## 2026-09-15 - Adopted the "LLM Wiki" pattern onto the existing structure, not a new one

**Decision:** Mapped the "LLM Wiki" pattern (immutable raw sources -> LLM-maintained wiki -> schema file, with ingest/query/lint operations) onto the AIOS as it already exists, instead of building a parallel structure. Added a "How the wiki grows" section to `CLAUDE.md`/`AGENTS.md` naming `context/`+`references/` as the wiki, `decisions/log.md` as the log, `CLAUDE.md`/`AGENTS.md` as the schema, and `/grill-me` + `brainstorms/` as the raw-capture/tentative layer. Did not add a raw-source archive folder, a new `index.md`, or a second `log.md`.

**Why:** `EXPANSIONS.md` already rules out a raw-dump layer ("don't dump raw email/Slack archives into references/, interpreted facts only") and pre-created empty structure ("don't pre-create folders you don't need yet"). At ~7 wiki pages, folder listings already work as the index, and `decisions/log.md` already covers the chronological record. Naming ingest/query/lint as explicit operations gets the benefit (a maintained, cross-referenced wiki instead of ad hoc RAG) without the folder sprawl the kit's own anti-patterns warn against.

**Alternatives considered:** Implementing the idea file literally (new `raw/`, `index.md`, `log.md` at root). Rejected: conflicts with documented anti-patterns and adds empty scaffolding ahead of need.

**Owner:** Nithish.

## 2026-09-06 - Audit evidence and routing maintenance

**Decision:** Ship audit rubric v2 and a small /link skill. Audit scores working evidence across the Four Cs, checks operating-manual routing and freshness, and passes one concrete gap into /level-up. A selected repair can improve an existing workflow instead of creating another skill.

**Why:** File counts, configured keys, named rituals, and recent edits do not prove an operational AIOS. Source findability and freshness need explicit checks.

**Alternatives considered:** Keeping presence-based scoring or requiring a hot cache. Neither reliably establishes retrieval quality or successful execution.

## 2026-09-06 - Portable skills and automatic audit history

**Decision:** Ship all four skills for Claude Code and Codex, with bundled resources, matching operating manuals, and a script for regenerating Codex copies. Audit reports are saved automatically, preserve previous runs, and track findings across comparable inspections.

**Why:** Students need the same shared guidance when switching assistants and evidence of actual improvements over time. Intentional runtime adaptations, unknown verification, and confirmed defects are reported separately.

## 2026-09-06 - Portable 3D Brain skill

**Decision:** Add `/3d-brain` for Claude Code and Codex. Ask for a name and categories, map selected local folders, and scaffold a bundled, configurable application with spherical placement, Cinema, and interactive growth replay.

**Why:** Shipping the working renderer preserves the intended appearance and interactions across AIOS installations. A prose-only prompt would produce inconsistent recreations. User config and graph data remain local; the public package includes only code, documentation, dependency notices, and fictional test inputs.

## 2026-09-10 - Outreach personalization + follow-up automation

**Decision:** Ship `/draft-outreach` — a skill that batch-drafts LinkedIn opener/follow-up messages into the outreach Sheet from raw, unstructured prospect notes, and tracks a fixed 5-touch follow-up sequence (day 0 / 4 / 11 / 21 / 35). Autonomy level **L2 (Drafted)** — AI writes into a `DRAFT` cell, human reviews, edits if needed, and sends by hand. Nothing sends automatically.

**Constraint:** Priority #1 (close 3-5 paid engagements, build a repeatable acquisition system) is blocked at the top of the funnel — manual personalization doesn't scale, generic AI drafts don't convert (per `context/about-me.md`), and today there's no system for chasing "waiting" leads before they go cold.

**EAD:** Eliminate was rejected — per `about-me.md`, dropping personalization directly costs conversion, so it's not waste. Automate: ~70% deterministic (date-math follow-up scheduling, Sheet read/write, reuses the existing `scripts/sheets_client.py` connection) + ~30% AI (matching a signal to a pain point and writing the copy — genuine judgment work, not typing).

**Process map:**
- *Trigger:* manual run of `/draft-outreach`, whenever the user sits down to batch-process leads
- *Data sources:* a new `RAW_NOTES` column (unstructured paste — About section, posts, team size, site blurb, job posting, tech stack), `references/voice.md`, `context/about-business.md` (ICP pain points)
- *Transformation:* apply the personalization bar ("couldn't have gone to 500 other people unedited") and a fallback ladder (trigger event → shared context → role/industry pain point → dig deeper / skip) to produce opener + 1-2 sentence value prop; follow-ups reference `LAST_SENT`
- *Decision points:* skip (don't force a generic line) if nothing clears the bar; stop the sequence the moment `STATUS` leaves `waiting`; flag (don't auto-continue) once all 4 follow-ups are sent with no reply
- *Destination:* `DRAFT` column in the live outreach Sheet, next to each lead

**KPI:** Bucket = **more customers** (more qualified conversations from the same/less outreach effort). Metric = reply rate, read directly off existing `waiting → replied` `STATUS` transitions — no new instrumentation needed. Secondary: hours/week freed for personal-brand content and building (Priorities #2/#3).

**Shipped (Machine, Phase 1 - manual only, no auto-trigger):**
- `scripts/sheets_client.py`: new `needs-draft`, `write-draft`, `mark-sent` commands; sheet header extended with `RAW_NOTES`, `DRAFT`, `LAST_SENT`, `TOUCH` (verified live: full draft→sent→schedule-advance round trip tested against the real Sheet, then reset to blank — no residue left)
- New skill `.claude/skills/draft-outreach/` (+ `.agents/skills/draft-outreach/` Codex mirror), registered in `CLAUDE.md`/`AGENTS.md`
- `references/google-sheets-api.md` updated with the new columns, follow-up schedule table, and commands

**Known limitation:** `DATE` is stored without a year (`DD-Mon`); follow-up offset math assumes the current year and would misfire across a year boundary. Not an issue yet at current recency/volume.

**Not done this run:** the audit's flagged repair (stale "none of these are wired up yet" line in `CLAUDE.md`/`AGENTS.md`) — user picked outreach personalization instead; still open for a future `/link` or `/level-up` pass.

**Owner:** Nithish.

## 2026-09-10 - Agency name: Atrily

**Decision:** Agency is named **Atrily** — "Automate The Rest" + "-ily". Currently used on LinkedIn; not yet legally registered. `.com` is taken; `.ai` is available and is the planned domain.

**Why:** Needed a name to build the personal brand and future website around (priorities 2 and 3 for this quarter). Name reflects the core value prop — automating the parts of a digital marketing agency's work that don't need a human.

**Alternatives considered:** None recorded — name was already in use on LinkedIn before this session.

**Owner:** Nithish.

**Note:** Business branding (Atrily) is kept separate from personal AIOS infrastructure — e.g. the Google Cloud project for API connections is named after Nithish/the AIOS, not Atrily, since the AIOS is meant to span more than just this one business.

## 2026-09-06 - Add ongoing context interviews

**Decision:** Adapt Herk-2's grill-me skill for the student kit and ship matching Claude/Codex packages. Save every answer to brainstorms/, preserve resumable Q&A history, and update canonical context only with confirmed facts during requested context-building sessions.

**Why:** Onboarding is an initial snapshot. Ongoing interviews capture changing priorities, decisions, and preferences while keeping tentative ideas distinct from current business facts.
