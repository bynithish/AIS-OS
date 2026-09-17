# AIS-OS Intake

This is the source-of-truth file for your AIOS. Fill it in by typing, voice-pasting (Wispr Flow / OS dictation), or running `/onboard` for a guided conversation. Whichever mode, this file is what `/onboard` reads to scaffold your Day-1 setup.

**Hard cap: 7 questions.** Each answerable in under 60 seconds. Don't overthink — you can edit and re-run `/onboard` any time.

---

## Q1 — Who are you, what do you sell, who do you sell it to?

Identity, offer, ICP. One paragraph each is fine.

```
Nithish, 21, based in India. Bachelor's in Data Science and Applications (in progress — treating it as runway, not the path). Parents cover living expenses. Building an AI agency as my real path because I don't buy into the traditional education system.

Co-founder: my older brother, doing his Master's in AI and Engineering Systems in the Netherlands. He genuinely enjoys the academic side and isn't actively building the agency day-to-day, but will invest time on any task I hand him with a clearly defined scope.

ICP: digital marketing agencies, ~5-50 employees. I have 500+ first-degree LinkedIn connections with DMA owners (connection requests accepted, but no real conversations yet). Chose this niche because (1) I previously tried to build a full-service digital marketing agency and spent real time learning the industry, and (2) market research suggests marketing services have strong potential to go AI-native — I want to sell the shovels, not compete as another agency.

Positioning: "help digital marketing agencies become AI-native — higher client capacity, higher margins, faster delivery." I know that's aspirational without credibility yet, so the actual offer is a low-risk "proof of value" engagement:
- Free 45-min discovery call to understand their business, pre-book a follow-up call for the next day.
- Using an AI-consultant Claude skill, identify one high-ROI, low-risk opportunity (lowest-hanging fruit).
- Build a custom offer around it within 24 hours: a 2-week sprint, project-based pricing, 50% upfront, keep working for free until it works, full refund if it still doesn't work after another 2 weeks.
- If it works by week 2/4, upsell to a retainer: ongoing identification, implementation, and management of AI-powered improvements across the agency.

No case studies yet, no first client yet. Plan to build a personal brand as leverage in parallel: posts on building an AI-native agency, traditional vs. AI-native agency comparisons, and how DMAs specifically can go AI-native. I'm my own case study — proof I can find problems and build solutions, which builds trust in the absence of a client portfolio.
```

---

## Q2 — Paste 1-2 things you've written recently. Don't edit them.

An email, a LinkedIn post, a DM, a doc — anything that sounds like you when you're not trying. **Paste verbatim.** Do not type these mid-conversation with Claude — chat-shaped samples are worse than no samples (voice contamination).

```
[LinkedIn post, ~4 months ago, best-performing post]

I learnt more from a 10-minute call with an agency owner than from weeks of “research”

I thought I had a “Grand Slam Offer”.
I started pitching my offer.
I booked a few calls.
I got on a few calls. 
then boom…

NOT. A. BURNING. PROBLEM!

they were right.
I was stuck in my confirmation bias.
same for the million offers before, too.

here’s how I’m healing:

1. talk to agency owners first
2. ask how their team works
3. find whether AI can help

if you run a digital marketing agency, like this post & i’ll reach out to you

P.S. this is not to say I finally figured it out, but to show that I’m (messily) iterating to strengthen my hero’s journey.

P.P.S. it’s not a mistake if you learn from it 🥲
```

```
[Cold DM opener — got a reply, almost booked a call, then he ghosted]

Saw you recent post about AI reshaping branding. Has that shown up in your own work yet, or is it still more theory at this stage?
```

---

## Q3 — What are your 2-3 biggest priorities for the next 90 days?

Quarterly priorities. Not yearly aspirations. Things that, if not done by July, would make you say "I wasted Q2."

```
1. Close 3-5 paid proof-of-value engagements; convert at least 2 into recurring monthly retainers; establish a repeatable client-acquisition system (targeted outreach → discovery calls → qualified opportunities → proof-of-value engagements) and identify which problem/offer patterns produce the highest conversion and ROI.

2. Become known on LinkedIn for a strong point of view on how digital marketing agencies become AI-native. Build a content system that converts real work/learnings into: 3-5 LinkedIn posts/week, 1-2 LinkedIn/Substack articles/month, 1 newsletter/week, 1 lead magnet/month, 4-8 company-page posts/month (mostly adapted from strongest personal posts).

3. Build a simple, credible digital presence that supports sales and builds authority. Launch a website that clearly communicates who I serve, the problem I solve, the initial offer, and how prospects start a conversation. Refine continuously as I learn from prospects, publish more content, and build a track record of results/case studies.
```

---

## Q4 — Where does revenue actually land, and where is it tracked?

Multiple answers OK. Stripe? Skool? GoHighLevel? QuickBooks? A spreadsheet?

```
Pre-revenue (no clients yet). Expected payment rails: Google Pay, Wise, or bank transfer. Planned tracking: QuickBooks.
```

---

## Q5 — Where do you talk to customers, your team, and the outside world day-to-day?

Email (which one — Gmail / Outlook)? Slack? Teams? DMs (Skool / Discord / iMessage)? Phone?

```
Primary outreach channel: LinkedIn DMs (cold outreach to agency owners). Once a prospect is in the talking stage, Indian agency owners tend to shift to WhatsApp. Meeting links get shared via email, which opens up an email follow-up channel too. Team (brother/co-founder): WhatsApp for casual updates today; will move to Slack once there's an actual need for a shared workspace/channel.
```

---

## Q6 — Where do meeting recordings, notes, and important docs live?

Granola? Otter? Fireflies? Google Drive? Notion? Dropbox? A folder on your desktop you keep meaning to organize?

```
Plan: Fireflies for meeting recordings/transcripts, plus a local copy stored on-device. Purpose beyond the meeting itself: reused as context for content creation and next-steps/follow-up planning.
```

---

## Q7 — What's the one task that eats your week, and where do you currently track work?

The single biggest time-suck or recurring drudgery. Plus where tasks/projects live (ClickUp / Asana / Linear / Notion / a notebook).

```
Biggest bottleneck: outreach execution. Most time-consuming parts: researching prospects, finding meaningful personalization signals, drafting openers, tracking conversations, managing follow-ups. Core challenge: maintaining high-volume, relevant, personalized outreach while making sure no opportunities fall through the cracks — this is the task I dread most and tend to procrastinate on. Current workaround: paste context into Claude chat and ask for a drafted message, but output reads generic and lacks human touch. Tracking: everything currently lives in Google Sheets.
```

---

When this file is filled, run `/onboard` (or re-run it) and the wizard will scaffold your Day-1 file set: `context/`, `references/voice.md`, populated `connections.md`, and a filled `CLAUDE.md`.
