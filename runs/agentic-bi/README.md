# Agentic BI

An AI-powered conversational business intelligence platform: a multi-agent system that turns a business question asked in natural language into a planned, executed and fully traceable analytical workflow. An Orchestrator decomposes intent into an *analysis plan* and dispatches it to four specialist agents — Data Fetch/Integration, Analytics, Visualization and ML — recombining their outputs into an *answer* that carries its *lineage*. Built for the enterprise data analyst: the goal is to compress the fixed overhead of every ad-hoc question without taking away the analyst's control or their ability to verify the result.

> **Status** — updated 2026-09-08 · run slug `agentic-bi` · **7 / 61 required artifacts** · 0 / 78 visuals rendered
> **PARTIAL — phases 0 and 1 of 8 complete.** This run is scoped to documents only: 54 of the 61 required manifest rows are in scope, 7 are deliberately excluded (see [ASSUMPTIONS.md](ASSUMPTIONS.md) A1, A4).

## Start here

The 60-second path will be one-pager → pitch deck → whitepaper once phase 5 lands. Until then:

1. **[BRIEF.md](BRIEF.md)** — who this is for, what it does, and which claims are deliberately not made. Every other artifact is written against this file.
2. **[research/competitors.md](research/competitors.md)** — the teardown, and §4 the differentiator. This is where the pack stops being a proposal and starts being an argument.
3. **[research/survey.md](research/survey.md)** §5.2 — the strongest case *against* this project's own mechanism, stated at full strength and then answered.
4. **[ASSUMPTIONS.md](ASSUMPTIONS.md)** — what was decided without confirmation, what closed in phase 1, and what would break if an inference is wrong.

## What phase 1 established

Four findings that change what downstream artifacts may claim:

1. **The differentiator, derived from failure mechanisms** (closes A6). *The investigation, not the query, is the unit — and it ships with a hop-level trace that makes verification cheaper than re-derivation.* Every incumbent buys correctness with a bounded, pre-authored artifact — 30 tables per Databricks Genie Agent, a ~32K-token Snowflake YAML model, existing-measures-only in Power BI Copilot — so the better their correctness mechanism, the narrower the set of questions they will attempt. An ad-hoc question is by definition the one nobody anticipated.
2. **The problem is trust, not speed** (closes A8, partially). Turnaround time is sourceable at one to four weeks but only second-hand; per-analyst queue length is **not publicly measured anywhere**, and the circulating "80% of a data team's time" figure was traced to unsourced vendor marketing and rejected. The High-confidence current evidence is about trust instead: 83% now prioritise trust in data, up from 66% in a year, and 71% fear hallucinated output reaching stakeholders. Positioning should lead with verifiability.
3. **"Why now" is half-right and now dated** (closes A9). Tool-access standardisation is fully supported — MCP shipped 2024-11-25 and was adopted by OpenAI, Google, Microsoft and AWS within thirteen months. Reliability "crossing a usable threshold" is **not** supported and must be restated: agents became reliable enough for the workflow to be *worth building and measuring*, not to be trusted unverified.
4. **The gravity question is open** (raises A11). Sisu Data raised ≈$128.7M attacking the highest-value part of this loop and became a Snowflake division. Narrative Science was folded into Tableau. Neither failed technically. *Why does this not end as a Databricks feature?* is unanswered, and phase 2 must claim cross-source neutrality or concede it.

## Reading paths by audience

**Project advisor / evaluator** — [BRIEF.md](BRIEF.md) for the venture framing, then [ASSUMPTIONS.md](ASSUMPTIONS.md), which distinguishes deliberate scope decisions from open gaps. The two places this pack knowingly declines to make a startup claim (no 10x differentiator, no declared moat) are A2 and A3, and both were argued before being accepted. [research/survey.md](research/survey.md) §6 shows what happened when the pack tried to source its own problem statement and could only half-succeed.

**Engineer** — [research/capability_table.md](research/capability_table.md) is the fastest orientation: eleven capabilities the mechanism depends on, with measured performance and the residual gap on each. Then [BRIEF.md](BRIEF.md) *Mechanism & moat* and *Vocabulary* — the nouns the whole pack uses. `tech/` (phase 4) will carry the architecture set.

**Investor lens** — [research/competitors.md](research/competitors.md) for the teardown and the positioning read, then [research/landscape.md](research/landscape.md) §6, the graveyard. Note that ThoughtSpot — the purest market test of this thesis — was marked down 73.67% in June 2024, and that this pack states so itself rather than waiting to be asked.

**Skeptic** — [research/survey.md](research/survey.md) §5.2 lists the eight strongest arguments against this project, including the benchmark evidence that its core capability measures ≈15% on hard real-world tasks. §5.3 answers them architecturally.

## Full artifact map

| Path | Holds | Files | Owning skill |
|---|---|---|---|
| `BRIEF.md` | Founder brief — source of truth | 1 | grill-me |
| `ASSUMPTIONS.md` | Assumptions and open decisions | 1 | grill-me |
| [`research/`](research/) | Market landscape, competitor teardown, capability survey, sources | **5 / 5 ✓** | startup-research |
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

Each traces to [research/sources.md](research/sources.md).

1. **The better an incumbent's correctness mechanism, the narrower the question set it will attempt.** Genie caps at 30 tables `[S32]`; Cortex Analyst's semantic model caps near 32K tokens `[S36]`; Power BI Copilot cannot compute a metric that is not already a measure or column `[S42]`. This is a design tension, not a bug, and it does not close with better models.
2. **Failure looks like a plausible but incorrect answer.** Schema-level errors — wrong column, semantic misinterpretation — are **81.2% of 4,602 analysed incorrect text-to-SQL queries** `[S2]`.
3. **The benchmark spread, not the headline, is the finding.** Top Spider 2.0 systems reach 96.70% on the Snow setting and **65.60% on the DBT setting** `[S1]` — a 31-point drop when semantic-layer indirection and real project structure are introduced.
4. **Multi-step data reasoning, this project's core dependency, is the field's weakest measured capability.** ≈14.55–16% on DABstep's Hard split against 76.39% on Easy, over 450+ tasks drawn from a real financial analytics workload `[S4]`. The pack states this itself, in [survey.md](research/survey.md) §5.2.1.
5. **Error compounding is arithmetic, not engineering debt.** 95% per hop over the four-to-six-hop fetch → analyze → model → visualize chain yields ≈74%; 90% yields ≈53% `[S13]`. No model improvement removes multiplicativity — only per-hop verification, replanning, and short chains do.

## Completeness

**PARTIAL — 7 of 54 in-scope required artifacts.** Phases 0 and 1 complete: the founder brief, the assumptions ledger, and the full research layer (landscape, competitor teardown, capability table, survey, sources). Phases 2–7 — strategy, product, tech, narrative, validation, financials — and the phase 9 audit remain. This run is deliberately scoped to documents only: the visuals and website phases are deferred, not cancelled (A4), and the three revenue-side financial artifacts are excluded by decision rather than omission (A1). Row-by-row status will live in `audit/COVERAGE.md` once phase 9 runs.

Three assumptions closed in phase 1 (A6, A8 partially, A9 with a required restatement) and one was newly raised (A11, the gravity question). Five research gaps were searched for and not found; they are named in [research/sources.md](research/sources.md) so a later phase does not spend budget re-searching them blind.
