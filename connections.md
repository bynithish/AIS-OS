# Connections

Registry of every system your AIOS can reach. Filled by `/onboard` from Q4-Q7 answers; expanded over time as you wire new tools. `/audit` checks this file for domain coverage and freshness.

| # | Domain | Tool | Mechanism | Auth | Last checked |
|---|---|---|---|---|---|
| 1 | Revenue / Financials | QuickBooks (payments via Google Pay / Wise / bank transfer) | not yet connected | — | — |
| 2 | Customer interactions | LinkedIn DMs (cold outreach) → WhatsApp once in talking stage | not yet connected | — | — |
| 3 | Calendar | Google Calendar (inferred from Gmail) | not yet connected | — | — |
| 4 | Communication | Gmail (follow-ups, meeting links); WhatsApp with co-founder; Slack planned later | not yet connected | — | — |
| 5 | Project / task tracking | Google Sheets (outreach tracker) | script (`scripts/sheets_client.py`) | service account (`credentials/aios-sheets-key.json`) | 2026-09-10 |
| 6 | Meeting intelligence | Fireflies (planned) + local storage (`raw/`) | not yet connected | — | — |
| 7 | Knowledge / files | Google Sheets (outreach tracker); local storage (`raw/` for meeting notes/transcripts) | script (`scripts/sheets_client.py`) | service account (`credentials/aios-sheets-key.json`) | 2026-09-10 |

**Mechanism options:** `mcp` (MCP server), `script` (Python/Bash hitting an API, in `scripts/`), `export` (CSV/JSON dump pipeline), `key+ref` (`.env` key + `references/{tool}-api.md` guide), `not yet connected`.

When you wire a new tool, also save `references/{tool}-api.md` capturing endpoints, auth flow, and common queries — researched-once-saved-forever.
