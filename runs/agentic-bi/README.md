# Agentic BI

Conversational BI for enterprise data analysts: a multi-agent system that turns a business question into a planned, executed and fully traceable analytical workflow. An Orchestrator decomposes intent into an *analysis plan*, shows it before anything runs, and dispatches it to four specialist agents — Data Fetch/Integration, Analytics, Visualization and ML — across the analyst's real sources: the warehouse, the operational database, and the file nobody has ever modelled. Every handoff emits its own *lineage*, so the answer arrives with a trace the analyst can check hop by hop. Built for the analyst who can already write the query, on the bet that **the binding constraint is not how fast an answer arrives but what it costs to verify one you did not derive.**

> **Status** — 2026-09-09 · run slug `agentic-bi` · **54 / 54 in-scope required artifacts · 0 / 78 visuals rendered**
> **COMPLETE for the document scope.** 7 manifest rows are excluded or deferred by founder decision (see [audit/COVERAGE.md](audit/COVERAGE.md) §5). Visuals and website phases are deferred, not cancelled.
> **The count above is documents, not evidence:** twelve assumptions remain untested and no customer has been interviewed.

## Start here — 60 seconds

1. **[narrative/one_pager.md](narrative/one_pager.md)** — the whole venture on one page, every figure sourced.
2. **[narrative/pitch_deck.md](narrative/pitch_deck.md)** — 14 slides. Read the titles alone first; they carry the argument.
3. **[tech/whitepaper.md](tech/whitepaper.md)** — the mechanism arithmetic, and §5 for what it honestly totals.

## Reading paths by audience

**Project advisor / evaluator** — [BRIEF.md](BRIEF.md) for the venture framing, then [ASSUMPTIONS.md](ASSUMPTIONS.md), which separates deliberate scope decisions from open gaps. Then [validation/stage_gate.md](validation/stage_gate.md), which places the venture honestly at *Customer Discovery, not exited* and explains why a complete pack is not traction. The two places this project knowingly declines to make a startup claim are A2 (no 10× differentiator) and A3 (no moat), and both were argued before being accepted.

**Investor lens** — [narrative/vc_memo.md](narrative/vc_memo.md) end to end: §2 is the category-by-category demolition, §6 the three risks that would sink it. Then [research/landscape.md](research/landscape.md) §6, the graveyard — four prior attempts, none of which died of bad technology. Then [financials/risk_matrix.md](financials/risk_matrix.md), where no risk mitigates to Low.

**Engineer** — [tech/not_vaporware.md](tech/not_vaporware.md) first: named stack, real prices, and an explicit line between what two people build in a semester and what is research risk. Then [tech/architecture/00_INDEX.md](tech/architecture/00_INDEX.md) — D02, D03, D06 and D08 are the ones that show a mechanism — and [tech/deep_dives.md](tech/deep_dives.md) for the seven components with their failure modes. [product/features_prioritized.md](product/features_prioritized.md) has the build order and the pre-decided cut list.

**Operator / founder** — [strategy/positioning.md](strategy/positioning.md) §5 for the statement and §5.1 for the do-not-say list, then [strategy/channel_plan.md](strategy/channel_plan.md), where the arithmetic disqualifies most of go-to-market at a $900 ACV. Then [validation/experiment_board.md](validation/experiment_board.md) — nine experiments with pass/fail thresholds declared before any data exists.

**Practitioner / analyst** — [product/journeys/beachhead.md](product/journeys/beachhead.md) is the product as a real Thursday afternoon. Then [product/ux_spec.md](product/ux_spec.md), twelve screens; §5's verification-tick treatment and §14's three admissions are the parts worth arguing with.

**Skeptic** — [research/survey.md](research/survey.md) §5.2 lists the eight strongest arguments *against* this project, including the benchmark evidence that its core capability measures ≈15% on hard real-world tasks. §5.3 answers them architecturally.

## Full artifact map

| Path | Holds | Files | Owning skill |
|---|---|---|---|
| [`BRIEF.md`](BRIEF.md) | Founder brief — the source of truth every artifact is written against | 1 | grill-me |
| [`ASSUMPTIONS.md`](ASSUMPTIONS.md) | 13-entry decision ledger: what was decided without confirmation, what closed when, what would break if wrong | 1 | grill-me |
| [`research/`](research/) | Landscape, competitor teardown, capability table, dated survey, and 71 graded sources | 5 | startup-research |
| [`strategy/`](strategy/) | Market type, positioning, bottom-up sizing, personas, both canvases, value proposition, GTM, petal, channel economics, sales roadmap | 11 | startup-strategy |
| [`product/`](product/) | PRD, flagship and prioritised features, four end-to-end journeys, UX spec | 8 | startup-product |
| [`tech/`](tech/) | Whitepaper, deep dives, 11 architecture diagrams, three technique waves, decision tree, technique×feature matrix, not-vaporware | 19 | startup-tech |
| [`narrative/`](narrative/) | One-pager, VC memo, pitch deck, future press release, founder story, mission | 6 | startup-narrative |
| [`validation/`](validation/) | Riskiest assumptions, experiment board, discovery guide, get/keep/grow, stage gates, metrics by stage, pivot log, MVP definitions, decision-making unit | 9 | startup-validation |
| [`financials/`](financials/) | Pricing threshold, unit economics, risk matrix — **cost side only** | 3 | startup-financials |
| [`audit/`](audit/) | Coverage report | 1 | startup-audit |
| | **Total** | **65** | |

## Visual index

**None rendered.** The visuals phase is deferred by decision ([ASSUMPTIONS.md](ASSUMPTIONS.md) A4) — `node` is not installed on this machine and the visuals skill requires it. Nothing is embedded below because nothing exists to embed.

Two things are already on disk for when it resumes:

- **Eleven Mermaid diagrams** in [`tech/architecture/`](tech/architecture/00_INDEX.md), which render live in any GitHub-flavoured Markdown viewer. Per the manifest's own guidance, rows whose source artifact already ships a Mermaid diagram do not need a duplicate HTML infographic.
- **A `visual:` line on every slide** of [narrative/pitch_deck.md](narrative/pitch_deck.md) — these are the future rows of the visual manifest.

## Top 5 sharpest claims

Each traces to [research/sources.md](research/sources.md).

1. **The better an incumbent's correctness mechanism, the narrower the set of questions it will attempt.** Databricks Genie caps at 30 tables per agent `[S32]`; Snowflake Cortex Analyst runs on a hand-authored ~32K-token YAML model `[S36]`; Power BI Copilot cannot compute a metric that is not already a measure `[S42]`. These are not bugs — they are the reliability mechanism, and an ad-hoc question is by definition the one nobody modelled.
2. **Failure looks like a plausible but incorrect answer.** Schema-level errors — wrong column, wrong meaning — are **81.2% of 4,602 analysed incorrect text-to-SQL queries** `[S2]`.
3. **The benchmark spread is the finding, not the headline.** Top Spider 2.0 systems reach 96.70% on the Snow setting and **65.60% on the DBT setting** `[S1]` — a 31-point drop when semantic-layer indirection and real project structure appear.
4. **This project's core dependency is the field's weakest measured capability.** Multi-step data reasoning measures **≈14.55–16% on DABstep's Hard split against 76.39% on Easy**, over 450+ tasks from a real financial-analytics workload `[S4]`. The pack states this itself, in [research/survey.md](research/survey.md) §5.2.
5. **The arithmetic comes to ≈2.9×, not 10×** — and to ≈1.0× or below on single-source familiar questions, where the analyst should keep writing SQL ([tech/whitepaper.md](tech/whitepaper.md) §5). The larger queueing effect was computed and **withdrawn**, because induced demand consumes it.

## Completeness

**COMPLETE for the document scope.** All 54 in-scope required rows are present with no stubs; the audit found eleven defects and fixed them, and accepted three deviations with stated reasons. Seven rows are excluded or deferred by founder decision rather than omission — the three revenue-side financial artifacts (no revenue, no CAC, no funnel, so any projection would be fabricated) and the visuals and website phases (deferred, not cancelled). Row-by-row status, the defects found, and what to do next are in [audit/COVERAGE.md](audit/COVERAGE.md).

**What is finished is the pack, not the venture.** Twelve assumptions remain untested, nine experiments are all status `planned`, and no customer has been interviewed. Four of those assumptions can end the project and three of the four are answerable in roughly twenty-five founder-hours without writing any code — which is why [validation/stage_gate.md](validation/stage_gate.md) places this at *Customer Discovery, not exited*, and why the honest one-line summary is: **sixty-five artifacts, twelve untested assumptions, zero customers interviewed.**
