# InsightPilot

**An Agentic Platform for Conversational Business Intelligence**

Conversational BI for enterprise data analysts: a multi-agent system that turns a business question into a planned, executed and fully traceable analytical workflow. An Orchestrator decomposes intent into an *analysis plan*, shows it before anything runs, and dispatches it to four specialist agents — Data Fetch/Integration, Analytics, Visualization and ML — across the analyst's real sources: the warehouse, the operational database, and the file nobody has ever modelled. Every handoff emits its own *lineage*, so the answer arrives with a trace the analyst can check hop by hop. Built for the analyst who can already write the query, on the bet that **the binding constraint is not how fast an answer arrives but what it costs to verify one you did not derive.**

> **Status** — 2026-09-11 · run slug `insightpilot` · **54 / 54 in-scope required artifacts · 64 / 64 manifest visuals satisfied · 0 rasters**
> **COMPLETE for the document and visual scope.** 7 manifest rows are excluded by founder decision (see [audit/COVERAGE.md](audit/COVERAGE.md) §5). The visuals phase is now done — 53 HTML frames plus 11 Mermaid diagrams cover all 64 rows, with zero PNG rasters recorded rather than hidden. Only the optional website phase remains.
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
| `README.md` | This file — status, reading paths, the artifact map. It is itself a manifest row, so it counts | 1 | startup-audit |
| [`BRIEF.md`](BRIEF.md) | Founder brief — the source of truth every artifact is written against | 1 | grill-me |
| [`ASSUMPTIONS.md`](ASSUMPTIONS.md) | 13-entry decision ledger: what was decided without confirmation, what closed when, what would break if wrong | 1 | grill-me |
| [`research/`](research/) | Landscape, competitor teardown, capability table, dated survey, and 71 graded sources | 5 | startup-research |
| [`strategy/`](strategy/) | Market type, positioning, bottom-up sizing, personas, both canvases, value proposition, GTM, petal, channel economics, sales roadmap | 11 | startup-strategy |
| [`product/`](product/) | PRD, flagship and prioritised features, four end-to-end journeys, UX spec | 8 | startup-product |
| [`tech/`](tech/) | Whitepaper, deep dives, 11 architecture diagrams, three technique waves, decision tree, technique×feature matrix, not-vaporware | 19 | startup-tech |
| [`narrative/`](narrative/) | One-pager, VC memo, pitch deck, future press release, founder story, mission | 6 | startup-narrative |
| [`validation/`](validation/) | Riskiest assumptions, experiment board, discovery guide, get/keep/grow, stage gates, metrics by stage, pivot log, MVP definitions, decision-making unit | 9 | startup-validation |
| [`financials/`](financials/) | Pricing threshold, unit economics, risk matrix — **cost side only** | 3 | startup-financials |
| [`visuals/`](visuals/) | Visual manifest, image prompts, and 53 self-contained HTML infographics | 2 + 53 | startup-visuals |
| [`audit/`](audit/) | Coverage report | 1 | startup-audit |
| | **Total** | **67 documents + 53 frames** | |

## Visual index

**All 64 manifest rows are satisfied.** 11 are carried by Mermaid diagrams inside their own source artifacts and need no separate file; the other 53 are self-contained HTML frames in [`visuals/infographics/`](visuals/infographics/), 1280×720, no external assets, openable directly in a browser. The plan they were built against is [`visuals/visual_manifest.md`](visuals/visual_manifest.md), and [`visuals/docimages.json`](visuals/docimages.json) records which frame illustrates which artifact: **63 documents, 67 placements, zero content artifacts left unillustrated.**

**Four frames to open first.**

| Frame | What it carries |
|---|---|
| [`V60_one_pager.html`](visuals/infographics/V60_one_pager.html) | The whole venture in one frame, every figure sourced |
| [`V33_capability_frontier.html`](visuals/infographics/V33_capability_frontier.html) | Nine measured capabilities. The spread is the finding, and the weakest bar is this project's core dependency |
| [`V50_survey_for_against.html`](visuals/infographics/V50_survey_for_against.html) | The case for the mechanism beside the case against it. The case against is the longer column |
| [`V37_stage_gate.html`](visuals/infographics/V37_stage_gate.html) | Where this actually sits: hypotheses stated, none tested, six exit criteria with thresholds |

**Zero PNG rasters, recorded rather than hidden.** No text-to-image capability existed in the session that built this phase. Prompts for all 64 rows are written in [`visuals/image_prompts.md`](visuals/image_prompts.md) so a later session renders from a specification — and eleven of those rows carry an explicit instruction **never** to generate them, because an approximated topology is worse than none.

Also on disk and worth knowing about: **eleven Mermaid diagrams** in [`tech/architecture/`](tech/architecture/00_INDEX.md) render live in any GitHub-flavoured Markdown viewer, and [narrative/pitch_deck.md](narrative/pitch_deck.md) carries a `visual:` line on every slide naming the frame that belongs to it.

## Top 5 sharpest claims

Each traces to [research/sources.md](research/sources.md).

1. **The better an incumbent's correctness mechanism, the narrower the set of questions it will attempt.** Databricks Genie caps at 30 tables per agent `[S32]`; Snowflake Cortex Analyst runs on a hand-authored ~32K-token YAML model `[S36]`; Power BI Copilot cannot compute a metric that is not already a measure `[S42]`. These are not bugs — they are the reliability mechanism, and an ad-hoc question is by definition the one nobody modelled.
2. **Failure looks like a plausible but incorrect answer.** Schema-level errors — wrong column, wrong meaning — are **81.2% of 4,602 analysed incorrect text-to-SQL queries** `[S2]`.
3. **The benchmark spread is the finding, not the headline.** Top Spider 2.0 systems reach 96.70% on the Snow setting and **65.60% on the DBT setting** `[S1]` — a 31-point drop when semantic-layer indirection and real project structure appear.
4. **This project's core dependency is the field's weakest measured capability.** Multi-step data reasoning measures **≈14.55–16% on DABstep's Hard split against 76.39% on Easy**, over 450+ tasks from a real financial-analytics workload `[S4]`. The pack states this itself, in [research/survey.md](research/survey.md) §5.2.
5. **The arithmetic comes to ≈2.9×, not 10×** — and to ≈1.0× or below on single-source familiar questions, where the analyst should keep writing SQL ([tech/whitepaper.md](tech/whitepaper.md) §5). The larger queueing effect was computed and **withdrawn**, because induced demand consumes it.

## Completeness

**COMPLETE for the document and visual scope.** All 54 in-scope required rows are present with no stubs; the audit found eleven defects and fixed them, and accepted three deviations with stated reasons. Three rows are excluded by founder decision rather than omission — the revenue-side financial artifacts, since with no revenue, no acquisition data and no funnel any projection would be fabricated. Row-by-row status, the defects found, and what to do next are in [audit/COVERAGE.md](audit/COVERAGE.md).

**The visuals phase has since closed** all 64 manifest rows, with PNG rasters the one thing still outstanding and recorded as such. **The optional website phase is the only part of the pack's scope not started.**

**What is finished is the pack, not the venture.** Twelve assumptions remain untested, nine experiments are all status `planned`, and no customer has been interviewed. Four of those assumptions can end the project and three of the four are answerable in roughly twenty-five founder-hours without writing any code — which is why [validation/stage_gate.md](validation/stage_gate.md) places this at *Customer Discovery, not exited*, and why the honest one-line summary is: **sixty-seven documents, twelve untested assumptions, zero customers interviewed.**
