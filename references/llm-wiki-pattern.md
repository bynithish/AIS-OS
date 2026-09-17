---
name: llm-wiki-pattern
description: The "LLM Wiki" pattern this AIOS's raw/wiki/schema/log structure is adapted from.
---

# LLM Wiki pattern

Source: [[llm-wiki]] (clipped from Andrej Karpathy's gist, filed in `raw/assets/llm-wiki.md`).

## The core idea

Most LLM+document setups are RAG: upload files, retrieve chunks at query time, rediscover knowledge from scratch every question. Nothing accumulates.

The alternative: the LLM **incrementally builds and maintains a persistent wiki** that sits between you and raw sources. Ingesting a new source doesn't just index it — the LLM reads it, extracts what matters, and integrates it into the existing wiki: updating pages, revising summaries, flagging contradictions with prior claims. The wiki is a compounding artifact, not a cache. The human curates sources and asks questions; the LLM does the bookkeeping (summarizing, cross-referencing, filing) that makes a knowledge base survive past week one.

## Architecture (three layers)

- **Raw sources** — immutable, curated. LLM reads, never edits. Source of truth.
- **The wiki** — LLM-owned markdown pages: summaries, entity/concept pages, an evolving synthesis. Human reads it; LLM writes it.
- **The schema** — a document (CLAUDE.md / AGENTS.md) defining structure, conventions, and workflows for ingest/query/lint. Co-evolved with the LLM over time.

## Operations

- **Ingest** — drop a source in, LLM reads it, discusses takeaways, updates relevant wiki pages, appends a log entry. One source can touch many pages.
- **Query** — LLM searches the wiki (not raw sources) for answers, cites pages. Good answers — a comparison, an analysis, a connection — should get filed back into the wiki as new pages rather than lost in chat history.
- **Lint** — periodic health check: contradictions between pages, stale claims superseded by newer sources, orphan pages with no inbound links, concepts mentioned but lacking their own page, missing cross-references, gaps a web search could fill.

## Indexing and logging

- **index.md** — content-oriented catalog: every page, one-line summary, category. Updated on every ingest. Works well up to ~100 sources / hundreds of pages before you need real search.
- **log.md** — chronological, append-only. Prefixing entries consistently (e.g. `## [YYYY-MM-DD] ingest | Title`) keeps it grep-able (`grep "^## \[" log.md | tail -5`).

## Explicit note from the source

"This document is intentionally abstract... Everything mentioned above is optional and modular — pick what's useful, ignore what isn't." The author expects each implementation to diverge.

## How this AIOS adapted it

Decided in `decisions/log.md` (2026-09-15 entries, made before this source file was actually dropped into `raw/` — this page grounds that earlier paraphrase in the real text):

| Pattern concept | This AIOS |
|---|---|
| Schema | `CLAUDE.md` + `AGENTS.md` |
| Raw sources | `raw/` |
| Wiki | `context/` + `references/` |
| Log | `decisions/log.md` (reused, not a new file) |
| index.md | **Skipped.** At ~7 pages, `ls context/ references/` works as the index. Source explicitly allows this ("your wiki might be small enough that the index file is all you need"). Revisit per `EXPANSIONS.md`. |
| Raw capture (tentative) | Not in the source pattern. Added on top: `/grill-me` sessions in `brainstorms/`, tentative until promoted. |

Open questions not yet decided (source mentions them, this AIOS hasn't ruled either way):
- Whether to adopt a parseable `## [YYYY-MM-DD] type | Title` log prefix, vs. the current freeform `## YYYY-MM-DD - Title`.
- Whether query answers worth keeping (a comparison, an analysis) should get filed back into `context/`/`references/` as new pages, not just left in chat.
- Whether `/audit`'s lint pass should also check for "concept mentioned but has no page" and "data gaps fillable by search," beyond the contradiction/staleness/orphan checks it does now.
