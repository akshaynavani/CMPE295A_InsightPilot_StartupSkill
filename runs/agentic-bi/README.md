# Agentic BI

An AI-powered conversational business intelligence platform: a multi-agent system that turns a business question asked in natural language into a planned, executed and fully traceable analytical workflow. An Orchestrator decomposes intent into an *analysis plan* and dispatches it to four specialist agents — Data Fetch/Integration, Analytics, Visualization and ML — recombining their outputs into an *answer* that carries its *lineage*. Built for the enterprise data analyst: the goal is to compress the fixed overhead of every ad-hoc question without taking away the analyst's control or their ability to verify the result.

> **Status** — generated 2026-09-08 · run slug `agentic-bi` · **2 / 61 required artifacts** · 0 / 78 visuals rendered
> **PARTIAL — phase 0 of 8 complete.** This run is scoped to documents only: 54 of the 61 required manifest rows are in scope, 7 are deliberately excluded (see [ASSUMPTIONS.md](ASSUMPTIONS.md) A1, A4).

## Start here

Only phase 0 exists so far. The 60-second path will be one-pager → pitch deck → whitepaper once phases 1–7 land.

1. **[BRIEF.md](BRIEF.md)** — who this is for, what it does, and which claims are deliberately not made. Every other artifact is written against this file.
2. **[ASSUMPTIONS.md](ASSUMPTIONS.md)** — what was decided without confirmation, what was deferred, and what would break if an inference is wrong.
3. *(pending)* `narrative/one_pager.md` — phase 5.

## Reading paths by audience

**Project advisor / evaluator** — [BRIEF.md](BRIEF.md) for the venture framing, then [ASSUMPTIONS.md](ASSUMPTIONS.md), which distinguishes deliberate scope decisions from open gaps. The two places this pack knowingly declines to make a startup claim (no 10x differentiator, no declared moat) are A2 and A3, and both were argued before being accepted.

**Engineer** — [BRIEF.md](BRIEF.md) *Mechanism & moat* for the agent decomposition and connector scope, then *Vocabulary* — the nouns the whole pack uses. `tech/` (phase 4) will carry the architecture set.

**Investor lens** — [BRIEF.md](BRIEF.md) *Problem*, *Users & spectrum*, *Riskiest assumption*. Note that problem magnitude is unquantified by design until phase 1 sources it (A8).

## Full artifact map

| Path | Holds | Files | Owning skill |
|---|---|---|---|
| `BRIEF.md` | Founder brief — source of truth | 1 | grill-me |
| `ASSUMPTIONS.md` | Assumptions and open decisions | 1 | grill-me |
| `research/` | Market landscape, competitor teardown, capability survey, sources | 0 / 5 | startup-research |
| `strategy/` | Positioning, market type, sizing, personas, canvases, GTM, channels, sales roadmap | 0 / 11 | startup-strategy |
| `product/` | PRD, feature sets, four journeys, UX spec | 0 / 8 | startup-product |
| `tech/` | Whitepaper, deep dives, 11 architecture diagrams, technique waves | 0 / 18 | startup-tech |
| `narrative/` | One-pager, VC memo, pitch deck, future press, founder story, mission | 0 / 6 | startup-narrative |
| `validation/` | Riskiest assumptions, experiment board, discovery guide, funnel, stage gates, MVP, DMU | 0 / 9 | startup-validation |
| `financials/` | Pricing threshold, unit economics, risk matrix — **cost side only** | 0 / 3 | startup-financials |
| `audit/` | Coverage report | 0 / 1 | startup-audit |

*Counts are targets from `references/artifact-manifest.md`; the present column is derived from the glob at each checkpoint.*

## Visual index

None rendered. The visuals phase is deferred (A4) — it resumes cleanly once phases 3–5 exist, since its prerequisites are `product/`, `tech/`, `strategy/` and `narrative/`.

## Top 5 sharpest claims

Deferred until phase 1 supplies sourced claims. Phase 0 asserts nothing it can't attribute; the three founder-asserted positions currently carrying no citation are tagged A8 and A9.

## Completeness

**PARTIAL.** Phase 0 of 8 complete — the founder brief and assumptions ledger exist; no research, strategy, product, tech, narrative, validation or financial artifacts have been generated yet. This run is deliberately scoped to documents only: the visuals and website phases are deferred, not cancelled, and the three revenue-side financial artifacts are excluded by decision rather than omission. Row-by-row status will live in `audit/COVERAGE.md` once phase 9 runs.
