# Agentic BI

An AI-powered conversational business intelligence platform: a multi-agent system that turns a business question asked in natural language into a planned, executed and fully traceable analytical workflow. An Orchestrator decomposes intent into an *analysis plan* and dispatches it to four specialist agents — Data Fetch/Integration, Analytics, Visualization and ML — recombining their outputs into an *answer* that carries its *lineage*. Built for the enterprise data analyst: the goal is to compress the fixed overhead of every ad-hoc question without taking away the analyst's control or their ability to verify the result.

> **Status** — updated 2026-09-08 · run slug `agentic-bi` · **26 / 61 required artifacts** · 0 / 78 visuals rendered
> **PARTIAL — phases 0, 1, 2 and 3 of 8 complete.** This run is scoped to documents only: 54 of the 61 required manifest rows are in scope, 7 are deliberately excluded (see [ASSUMPTIONS.md](ASSUMPTIONS.md) A1, A4).

## Start here

The 60-second path will be one-pager → pitch deck → whitepaper once phase 5 lands. Until then:

1. **[BRIEF.md](BRIEF.md)** — who this is for, what it does, and which claims are deliberately not made. Every other artifact is written against this file.
2. **[strategy/positioning.md](strategy/positioning.md)** §5 — the one-sentence positioning statement, and §5.1 the list of things it deliberately does not say.
3. **[research/competitors.md](research/competitors.md)** — the teardown, and §4 the differentiator. This is where the pack stops being a proposal and starts being an argument.
4. **[research/survey.md](research/survey.md)** §5.2 — the strongest case *against* this project's own mechanism, stated at full strength and then answered.
5. **[ASSUMPTIONS.md](ASSUMPTIONS.md)** — what was decided without confirmation, what closed in phases 1 and 2, and what would break if an inference is wrong.

## What phase 3 established

1. **The loop gained a named beat: ASK → PLAN → EXECUTE → ANSWER → VERIFY → FOLLOW UP.** *Verify* was previously folded inside "answer + lineage." Naming it is what stops verification becoming the analyst's unpaid work — which is the state they are already in with every incumbent.
2. **Ten first-principles, every feature mapped to one.** Each is an empirical finding, not a design preference: schema grounding dominates language understanding (81.2% of failures); error compounds multiplicatively; failure is plausible not obvious; consistency degrades faster than capability; pre-encoded correctness narrows the question set. A feature mapping to no principle gets cut.
3. **Ten real non-goals**, including three that cost something: no unsupervised self-service for non-technical users (the category's largest revenue segment), no semantic layer of our own, and **no claim to beat incumbents on single-source single-hop accuracy** — on Genie's home turf, Genie is expected to win.
4. **The backlog is ordered by leverage on the riskiest claim, not by visibility.** The evaluation harness is #1; three of the four specialist agents are in Next or Later. The cut list is decided in advance: visualization, then REST, then the ML agent, then override re-flow.
5. **A12 raised — the beachhead captures the least value on any given day.** Running all five personas against one shared Tuesday showed Dr. Chen going from 2 hours to 19 minutes and Tom from 1.5 days to 8 minutes, while Priya absorbs the review burden the other four shed. Since GTM routes entirely through analyst advocacy, this is a plausible mechanism for adoption stalling at exactly the person it cannot stall at.

## What phase 2 established

Five decisions every later artifact inherits:

1. **Re-segmented market, by different attribute — verifiability across sources.** Not a new market (the graveyard proves demand was repeatedly found) and not an existing one (on "answer my question about my warehouse," bundled incumbents win on distribution before this product starts). The dominant risk is **segment reality**, not competition.
2. **Positioning axes: hops executed autonomously × where correctness is established.** The open quadrant is *many hops × correctness carried with the answer*, and it is empty because it is hard — multi-step data reasoning measures ≈15% on hard real tasks. The inversion that makes it a strategy: because multi-hop is unreliable, the trace is what makes the hops usable at all.
3. **Deployment resolved: open-core, self-hostable** (closes A5), which is simultaneously the answer to the gravity question (closes A11) — neutrality asserted by a hosted service is a claim; neutrality backed by code the customer runs is a property.
4. **The market is small, and the pack says so.** TAM $1.1B, SAM $123M, pessimistic-corner SAM $38M, capstone SOM $0. Built bottom-up from BLS headcount × observed price, with three of four factors tagged as assumptions. A "1% of a $40B BI market" figure would have falsified the whole market-type declaration.
5. **One channel, and it earns no revenue.** At a $900 ACV the arithmetic disqualifies outbound, field sales, resellers and paid acquisition outright. Only open-source self-serve plus internal referral survive — so adoption precedes revenue structurally, which is right for a capstone and a stated constraint for the venture framing.

## What phase 1 established

Four findings that change what downstream artifacts may claim:

1. **The differentiator, derived from failure mechanisms** (closes A6). *The investigation, not the query, is the unit — and it ships with a hop-level trace that makes verification cheaper than re-derivation.* Every incumbent buys correctness with a bounded, pre-authored artifact — 30 tables per Databricks Genie Agent, a ~32K-token Snowflake YAML model, existing-measures-only in Power BI Copilot — so the better their correctness mechanism, the narrower the set of questions they will attempt. An ad-hoc question is by definition the one nobody anticipated.
2. **The problem is trust, not speed** (closes A8, partially). Turnaround time is sourceable at one to four weeks but only second-hand; per-analyst queue length is **not publicly measured anywhere**, and the circulating "80% of a data team's time" figure was traced to unsourced vendor marketing and rejected. The High-confidence current evidence is about trust instead: 83% now prioritise trust in data, up from 66% in a year, and 71% fear hallucinated output reaching stakeholders. Positioning should lead with verifiability.
3. **"Why now" is half-right and now dated** (closes A9). Tool-access standardisation is fully supported — MCP shipped 2024-11-25 and was adopted by OpenAI, Google, Microsoft and AWS within thirteen months. Reliability "crossing a usable threshold" is **not** supported and must be restated: agents became reliable enough for the workflow to be *worth building and measuring*, not to be trusted unverified.
4. **The gravity question is open** (raises A11). Sisu Data raised ≈$128.7M attacking the highest-value part of this loop and became a Snowflake division. Narrative Science was folded into Tableau. Neither failed technically. *Why does this not end as a Databricks feature?* is unanswered, and phase 2 must claim cross-source neutrality or concede it.

## Reading paths by audience

**Project advisor / evaluator** — [BRIEF.md](BRIEF.md) for the venture framing, then [ASSUMPTIONS.md](ASSUMPTIONS.md), which distinguishes deliberate scope decisions from open gaps. The two places this pack knowingly declines to make a startup claim (no 10x differentiator, no declared moat) are A2 and A3, and both were argued before being accepted. [research/survey.md](research/survey.md) §6 shows what happened when the pack tried to source its own problem statement and could only half-succeed.

**Engineer** — [product/PRD.md](product/PRD.md) §3 for the ten principles every feature obeys, then [product/features_prioritized.md](product/features_prioritized.md) for what gets built in what order and what gets cut first. [research/capability_table.md](research/capability_table.md) is the fastest orientation on what the field can actually do. `tech/` (phase 4) will carry the architecture set.

**Designer** — [product/ux_spec.md](product/ux_spec.md), twelve screens. §5's verification-tick treatment and §14's three admissions of where the spec is probably wrong are the parts worth arguing with.

**Investor lens** — [research/competitors.md](research/competitors.md) for the teardown and the positioning read, then [research/landscape.md](research/landscape.md) §6, the graveyard. Note that ThoughtSpot — the purest market test of this thesis — was marked down 73.67% in June 2024, and that this pack states so itself rather than waiting to be asked.

**Skeptic** — [research/survey.md](research/survey.md) §5.2 lists the eight strongest arguments against this project, including the benchmark evidence that its core capability measures ≈15% on hard real-world tasks. §5.3 answers them architecturally.

## Full artifact map

| Path | Holds | Files | Owning skill |
|---|---|---|---|
| `BRIEF.md` | Founder brief — source of truth | 1 | grill-me |
| `ASSUMPTIONS.md` | Assumptions and open decisions | 1 | grill-me |
| [`research/`](research/) | Market landscape, competitor teardown, capability survey, sources | **5 / 5 ✓** | startup-research |
| [`strategy/`](strategy/) | Positioning, market type, sizing, personas, canvases, GTM, channels, sales roadmap | **11 / 11 ✓** | startup-strategy |
| [`product/`](product/) | PRD, feature sets, four journeys, UX spec | **8 / 8 ✓** | startup-product |
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

**PARTIAL — 26 of 54 in-scope required artifacts.** Phases 0–3 complete: the founder brief, the assumptions ledger, the full research layer (landscape, competitor teardown, capability table, survey, sources), the full strategy layer (market type, positioning, sizing, personas, both canvases, value proposition, GTM, petal, channel economics, sales roadmap) and the full product layer (PRD, flagship and prioritised features, four journeys, UX spec). Phases 4–7 — tech, narrative, validation, financials — and the phase 9 audit remain. This run is deliberately scoped to documents only: the visuals and website phases are deferred, not cancelled (A4), and the three revenue-side financial artifacts are excluded by decision rather than omission (A1). Row-by-row status will live in `audit/COVERAGE.md` once phase 9 runs.

Three assumptions closed in phase 1 (A6, A8 partially, A9 with a required restatement) and one was newly raised (A11, the gravity question). Phase 2 then closed A5 and A11 together by founder decision at the gate — **every open decision in the ledger is now closed**; what remains is unconfirmed inferences (A7) and deliberate scope decisions (A1–A4), which the audit must treat as closed rather than missing. Five research gaps were searched for and not found; they are named in [research/sources.md](research/sources.md) so a later phase does not spend budget re-searching them blind.

**The three untested claims the whole pack now rests on**, all of them conversation-cheap to settle and none of them settled: (1) an analyst can accept a correct answer they did not derive faster than they could derive it — the differentiator, and the beachhead's own stated objection denies it; (2) a material share of real ad-hoc questions actually span more than one source — if not, the neutrality argument is true and worthless and the SAM halves; (3) a budget owner can name a line item this comes from — if not, the market-type declaration is wrong. They are ranked in [strategy/business_model_canvas.md](strategy/business_model_canvas.md) rows 2, 1 and 5.
