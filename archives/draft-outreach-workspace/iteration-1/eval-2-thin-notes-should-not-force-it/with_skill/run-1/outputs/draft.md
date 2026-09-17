# Draft — Sana Okafor

## Output

SKIP — nothing in RAW_NOTES clears the personalization bar; every candidate line would read as generic template-fill, not a real observation about her specifically.

## Reasoning

Went through each line in RAW_NOTES against `references/signal-pain-point-map.md`:

- **"Runs a small marketing agency, seems to do a bit of everything"** — the "seems to" already flags this as an inference, not something stated. It's the shape of the "Full-service agency, many disciplines under one roof" row (→ #5), but that row needs the disciplines actually named (e.g. "SEO + social + paid + content") to ask a specific question like "are they talking to each other, or stitched manually?" Without named disciplines there's no specific thing to ask about — it collapses into a guess.
- **"LinkedIn photo looks professional"** — not a business signal at all, doesn't map to anything in the pain-point map.
- **"Based in Lagos"** — a location fact only, not shared context. The map's "shared context" fallback rung requires an actual shared thing (same group, mutual connection, same city as Nithish) — nothing in the notes establishes that Nithish shares Lagos or any connection there.
- **"No posts in the last year"** — the map's closest row is "Blog gone stale / no recent posts," but that's specifically about a website blog, not LinkedIn posting cadence. LinkedIn inactivity isn't a mapped signal, and stretching it there would be inventing a row that doesn't exist.
- **"Site is just a one-pager with an email address, no other detail"** — closest to the website/behavioral signals (no contact form, no booking link, no live chat), all → #5. But a bare one-pager with just an email is extremely common for a small agency with no dedicated ops person — it doesn't distinguish Sana from hundreds of other small-agency owners. Failed the test from the skill directly: *could this exact line have gone to 500 other people unedited?* Yes.

**Fallback ladder** (per SKILL.md, since no map row cleanly hit):
1. Trigger event (recent hire, new tool, expansion) — none mentioned.
2. Shared context (same LinkedIn group, mutual connection, same location) — Lagos alone isn't established as *shared* context; nothing ties it back to Nithish.
3. Neither rung clears the bar on a close re-read → per the skill, don't force a generic line. SKIP is the correct call, not the default #5 question, because even the #5 fallback lines available here ("your site's a one-pager, intentional or not?") are generic enough to fit almost any small agency, not just Sana's.

**Next step (per skill's SKIP handling):** don't send anything yet — dig further into her site or LinkedIn (recent activity elsewhere, any case studies, any named clients/tools) before re-running `needs-draft` on her.
