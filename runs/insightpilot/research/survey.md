# A survey of conversational and agentic business intelligence

**Dated 2026-09-08.** All sources accessed on that date and registered in [sources.md](sources.md).

**What this is** — A short survey paper on automating the path from business question to trustworthy analytical answer: the classical foundations, a taxonomy of approaches, the enabling technology, how the field measures itself, and the evidence for and against the brief's core mechanism.
**Why it exists** — This is the scientific grounding the `tech/` whitepaper and the PRD cite instead of asserting. It exists because the project's own brief concedes that the problem is *researched, not lived*, which makes an unsourced technical claim the pack's most likely point of collapse under review. It also fixes the standard the whitepaper must clear: a claim here without a citation is a defect, not a stylistic choice.
**How to read it** — §5 (evidence for and against) and §6 (problem magnitude) carry the load; §2–§4 are grounding. A skeptic should attack §5.2, which argues *against* the brief's own mechanism using the strongest evidence available, and §6, which closes ASSUMPTIONS A8 with a partial rather than a clean result.
**Depends on / feeds** — Grounded on [BRIEF.md](../BRIEF.md); shares evidence with [landscape.md](landscape.md), [competitors.md](competitors.md) and [capability_table.md](capability_table.md); cites through [sources.md](sources.md). Feeds the whitepaper, the PRD's non-functional requirements, and the validation layer's assumption ranking.

---

## Abstract

Natural-language access to enterprise data has been attempted continuously since at least 2014 and has an unusually well-documented graveyard: IBM Watson Analytics discontinued in 2019 `[S59]`, Narrative Science absorbed into Tableau in 2021 `[S58]`, Sisu Data absorbed into Snowflake in 2023 after raising ≈$128.7M `[S56][S57]`, and Power BI Q&A — shipped inside the most widely deployed BI tool in the enterprise — fully retired by December 2026 `[S40]`. The current generation differs in one respect that matters: large language models removed the linguistic-parsing bottleneck that defeated the previous generation, replacing it with a semantic-grounding bottleneck that the field has converged on solving through hand-authored semantic layers `[S36][S42][S48][S51]`, with 59% of large enterprises now funding that layer directly `[S17]`. This convergence buys correctness at the price of scope: every incumbent's reliability mechanism restricts it to questions someone anticipated well enough to model in advance. Meanwhile the measured capability frontier shows a sharp split. Single-hop text-to-SQL on realistic schemas is strong — top Spider 2.0-Snow systems reach 96.70% `[S1]` — while multi-step data reasoning remains largely unsolved, at roughly 14.55–16% on DABstep's Hard split against 76.39% on its Easy split `[S4]`, with agent consistency collapsing from above 60% `pass^1` to below 25% `pass^8` `[S5]` and error propagation identified as the primary reliability bottleneck for LLM agents `[S10]`. This survey concludes that a multi-agent orchestration layer over heterogeneous sources is well posed and currently unbuilt, that its central risk is correctly identified by the brief, and that the evidence supports building **verification affordances** rather than betting on end-to-end reliability.

## 1. Scope and method

This survey covers systems that take a business question expressed in natural language and return an analytical answer over structured enterprise data. It excludes conversational assistants over documents, general-purpose coding agents, and dashboard tooling without a natural-language surface.

**Method and its limits.** Thirty-three web searches and six direct page fetches on 2026-09-08 across four tracks: direct competitors and their pricing and funding; adjacent and dead attempts; enabling technology, papers and benchmarks; and market structure. Primary sources were preferred — leaderboards, arXiv papers, vendor documentation and pricing pages, named surveys with disclosed samples. Where only vendor content marketing was available, the figure is graded Low in [sources.md](sources.md) and is used as a range indicator or not at all. **This is desk research: no analyst was interviewed, no product was installed, and no measurement here is the authors' own.** Five specific gaps that were searched for and not found are recorded in [sources.md](sources.md), *Named gaps*.

## 2. Classical foundations

Four lines converge on the present problem.

**Natural-language interfaces to databases (NLIDB).** A research programme running since the 1970s, whose recurring finding is that parsing was never the hard part — mapping a user's vocabulary onto a schema's vocabulary was. Power BI Q&A is the clearest production expression: it required modellers to curate synonyms, linguistic relationships and explicit "teach Q&A" corrections `[S41]`. It is being retired in December 2026 `[S40]`, and the retirement is instructive precisely because distribution was never its problem.

**Semantic layers and the metrics store.** The discipline of defining a business metric once, in one governed place. Now organised into four categories: pure semantic layers (dbt Semantic Layer, Cube, AtScale, Honeydew), warehouse-native semantic views (Snowflake, Databricks Metric Views), BI-native models (LookML, GoodData, MicroStrategy ONE), and a context layer governing agent consumption `[S66]`. Predates LLMs; became load-bearing because of them.

**Augmented analytics and automated diagnosis.** Systems that explain *why* a metric moved rather than reporting that it did. Sisu Data was the strongest commercial attempt `[S56]`. The category's technical content — automated hypothesis generation over dimensional data — is directly relevant to what the brief calls the Analytics agent.

**AutoML.** Automated model selection, feature engineering and hyperparameter search. Now benchmarked agentically on MLE-bench's 75 Kaggle competitions `[S8]`, where agents reach a 36.4% medal rate under a 12-hour budget `[S9]`.

## 3. A taxonomy of current approaches

Organised by **where correctness is established**, which [competitors.md](competitors.md) §3.1 identifies as the axis that actually separates behaviour.

### 3.1 Pre-encoded correctness (semantic-model-first)

**Mechanism.** A human authors an artifact — YAML semantic model, Genie space, Power BI model, Pulse metric definition, Wren AI MDL — before any question is asked. Generation is constrained to it.

**Instances.** Snowflake Cortex Analyst `[S36]`, Databricks Genie `[S33]`, Power BI Copilot `[S42]`, Tableau Pulse `[S48]`, Wren AI `[S51]`.

**Evidence for.** The strongest mechanism argument in the field. Schema-level errors — wrong column selection and semantic misinterpretation — are **81.2% of 4,602 analysed incorrect queries** `[S2]`; a semantic layer attacks exactly that class. Enterprises are funding it: 59% directing incremental budget, 44.5% increasing spend and 14.4% newly adopting `[S17]`.

**Evidence against.** The artifact is bounded and expensive. Snowflake's semantic model is hand-authored YAML capped near 1 MB / ~32K tokens `[S36]`; Genie Agents cap at 30 tables `[S32]`; Copilot cannot compute a metric that is not already a measure or column `[S42]`; Pulse handles single-number metrics with clear dimensions and fails on composite metrics and multi-step reasoning `[S49]`. **The tighter the correctness mechanism, the narrower the answerable question set** — and an ad-hoc question is by construction one nobody anticipated.

### 3.2 Post-hoc verification by the human (notebook-first)

**Mechanism.** The agent works inside an artifact whose every step is visible, editable and re-runnable; the human verifies by reading.

**Instances.** Hex Notebook Agent `[S54]`; and, in its unautomated form, the analyst writing their own SQL.

**Evidence for.** Auditability is structural rather than added. There is no lineage feature to build because nothing was hidden.

**Evidence against.** It does not compress the analyst's attention, which the brief identifies as the actual pain. The human still directs every hop, and there is no plan to replan.

### 3.3 Correctness carried with the answer (essentially unoccupied)

**Mechanism.** The system emits a trace structured so verification is cheaper than re-derivation.

**Instances.** None complete. The nearest move is Databricks' *Inspect* (Beta), where Genie reviews its own generated SQL, authors smaller statements to verify specific aspects, and regenerates `[S32]` — self-verification by decomposition, but within a single query rather than across a plan.

**Why it is empty.** Not oversight. It requires multi-step reasoning that the benchmarks say is unsolved (§5.2). This is the position the brief occupies, and §5 assesses whether that is brave or reckless.

### 3.4 Metric-push (inverted loop)

Tableau Pulse `[S48]`. The system pushes changes in subscribed metrics rather than answering asked questions. Included because it is a legitimate answer to the same business need — an analyst's queue shortens if the routine questions answer themselves before being asked — and because it fails cleanly outside the scorecard layer `[S49]`.

## 4. Enabling technology

Detail and citations are in [capability_table.md](capability_table.md); this section states only what the whitepaper needs.

**Text-to-SQL is strong and unevenly so.** Top Spider 2.0 systems reach 96.70% on Snow, 76.23% on Lite and **65.60% on DBT** `[S1]`; BIRD's leader is at 80.04% against 92.96% human `[S3]`. **The 31-point Snow→DBT spread is the finding** — the same class of system loses roughly a third of its accuracy when semantic-layer indirection and real project structure are introduced. Production analysis is harsher still: 30–36% on ~1,000-column, 54-table schemas, and up to 24 points lost to schema evolution `[S2]`.

**Multi-step data reasoning is the weak point.** DABstep draws 450+ tasks from a real financial analytics workload, classes 84% as Hard, and reports roughly 14.55–16% on that split against 76.39% on Easy `[S4]`.

**Consistency degrades faster than capability.** τ-bench's `pass^k` decays as `p^k`; an agent above 60% `pass^1` falls below 25% `pass^8` `[S5]`.

**Error compounding is structural.** Multiplicative — 95% per step gives 59% at ten steps, 90% gives 35% `[S13]` — and error propagation is named the primary reliability bottleneck across agent failure taxonomies `[S10][S11]`. No model improvement removes multiplicativity.

**Horizon is growing fast.** 50%-reliability task length doubling every ~7 months over six years `[S6]`, and closer to every 4 months across 2024–2025 `[S7]`. Note the 50% reliability level: it establishes a trend, not a fitness threshold.

**Tool access standardised, on the record.** MCP announced 2024-11-25 with a Postgres reference server; OpenAI March 2025; Google DeepMind and Microsoft mid-2025; AWS late 2025; donated to the Linux Foundation's Agentic AI Foundation December 2025 `[S62]`. It standardises access, not semantics `[S65]`.

**Inference cost falls unevenly.** ≈$60 → ≈$0.06 per million tokens for a fixed benchmark score between November 2021 and late 2024 `[S63]`, with per-year declines ranging 9×–900× by capability milestone `[S64]`.

**Automated ML is real but slow.** 36.4% medal rate and 18.7% gold on MLE-bench under a **12-hour budget** `[S9]`.

## 5. Evidence for and against the core mechanism

The mechanism under test: *an Orchestrator decomposes a question into an analysis plan, dispatches tasks to specialist fetch, analytics, visualization and ML agents, replans when a result invalidates the plan, and returns an answer carrying its lineage.*

### 5.1 For

1. **The decomposition-verification insight is independently confirmed by the strongest incumbent.** Databricks' Inspect decomposes a query into smaller verification statements and regenerates on failure `[S32]`. Databricks arrived at decompose-then-verify from the opposite direction, which is meaningful corroboration of the architectural bet.
2. **The connector layer is now a configuration problem.** MCP's standardisation is dated, multi-vendor and neutrally stewarded `[S62]`, which is precisely the brief's stated condition for a pluggable connector layer being tractable for a small team.
3. **Demand for verifiability is measured, not assumed.** 71% of practitioners name incorrect or hallucinated outputs reaching stakeholders as a top concern `[S16]`; 24.9% name accuracy and hallucination risk as their top reservation about GenAI in analytics `[S17]`; trust in data as a stated priority rose from 66% to 83% year over year `[S16]`. Lineage addresses the market's own top-ranked objection.
4. **The multi-hop, cross-source position is genuinely unoccupied.** Every warehouse-native assistant is single-warehouse and effectively single-hop ([landscape.md](landscape.md) §2), and the semantic-layer market is an integration surface rather than a rival `[S66]`.
5. **The predictive step is absent from every shipped product.** MLE-bench-class capability exists `[S9]` and no BI product exposes it.
6. **The problem predates the hype.** 44% of data engineers' time spent building and rebuilding pipelines, measured in 2021 `[S18]`, before the generative-AI cycle. The overhead is not an artifact of current enthusiasm.

### 5.2 Against — the strongest case that can be made

Stated at full strength, because a survey that only argues for its sponsor's mechanism is advocacy.

1. **The benchmark evidence contradicts the mechanism's central requirement.** The brief's Orchestrator is exactly the capability DABstep measures at ≈14.55–16% on hard real tasks `[S4]`. Not "early" — measured, and low. A reviewer can find this in one search.
2. **Compounding is arithmetic, not engineering debt.** Four to six hops at 95% per hop yields ≈74%; at 90%, ≈53% `[S13]`. Every hop added to make the system more capable makes it less reliable, and error propagation is confirmed as the primary bottleneck `[S10]`. The architecture's ambition is in direct tension with its trustworthiness.
3. **The incumbents' restriction is a considered answer, not a limitation.** Genie's 30-table ceiling `[S32]` and Cortex's 32K-token semantic model `[S36]` look like weaknesses and read better as the field's settled answer to §5.2.1: constrain scope until reliability is acceptable. A system that removes the constraints inherits the unreliability they were bought to prevent.
4. **Gravity has taken every standalone attempt so far.** Sisu raised ≈$128.7M and became a Snowflake division `[S56][S57]`; Narrative Science was folded into Tableau `[S58]`. Neither failed technically. The structural question — why does this not end as a Databricks feature — is unanswered anywhere in this pack.
5. **The purest market test of the low edge was marked down 73.67%** `[S46]`. ThoughtSpot was well funded, early and technically credible. The natural-language-for-non-analysts thesis has not paid off at the price it was funded at.
6. **The nearest neighbour is open source, two years ahead, and has a community.** Wren AI: 13,000+ stars, 10,000+ cloud users `[S50]`. The difference is scope of the loop, which is quantitative.
7. **The commodity trap at the entry point.** The brief's day-one CSV/Excel path is served by Julius at $35/month `[S53]`.
8. **Forecasts cut both ways.** The same analysts predicting 40% agent penetration by end-2026 `[S30]` predict >40% of agentic projects cancelled by end-2027 `[S31]` and half of agent deployment failures traced to governance `[S29]`.

### 5.3 Assessment

The case against is stronger than the case for on **end-to-end reliability**, and weaker on **whether the position is worth occupying**. Both readings survive the evidence, and the resolution is architectural rather than rhetorical.

If multi-hop reliability is measured at ≈15% on hard tasks `[S4]` and compounding is multiplicative `[S13]`, then a system that promises trustworthy autonomous answers is promising something the field cannot currently deliver — and a pack claiming otherwise would be the graveyard's next entry. But that is not the only available product. The same evidence supports a system whose **design centre is making failure cheap to detect**: per-hop verification, replanning on invalidation, and a trace structured so the analyst checks the one hop they doubt rather than re-deriving the chain. On that reading the low reliability numbers are the *reason* for the architecture, not an objection to it — and the market's own top-ranked concern `[S16][S17]` is the demand signal for exactly that.

Three consequences follow, and they bind the downstream artifacts:

1. **Lineage is not a feature. It is the product's answer to §5.2.1** and must be specified as load-bearing in the PRD, with the bar set by Hex's notebook `[S54]`, not by "we show the SQL."
2. **The outcome metric is right and should not move.** *Time-to-verified-answer* prices verification into the measurement. An accuracy-only metric would hide the failure mode that actually matters, which is plausible-but-wrong `[S2]`.
3. **The 295A spike should measure multi-hop accuracy on one narrow path and publish the number.** No commercial product publishes one ([sources.md](sources.md), *Named gaps* 2). Measuring it is both the honest response to §5.2.1 and the most credible artifact the project could produce.

## 6. Problem magnitude — closing ASSUMPTIONS A8

A8 is flagged `kills-pack-if-wrong: yes` on the condition that the magnitude either be sourced or its absence stated explicitly. **The result is partial, and reported as partial.**

### 6.1 What is sourceable

| Claim | Figure | Source | Confidence |
|---|---|---|---|
| Data-request turnaround, enterprise | **One to four weeks** | IBM, attributing Sigma Computing `[S15]` | Medium — citation chain, not primary |
| BI request turnaround, <500 employees | **Five to ten business days** | Forrester, via IBM `[S15]` | Medium |
| Decisions made without data because access was too hard | **76% of businesses** | Sisense, via IBM `[S15]` | Medium |
| Enterprise data never used for analytics | **60–73%** | Forrester, via IBM `[S15]` | Medium |
| Data-engineer time rebuilding pipelines | **44%** | Fivetran / Wakefield, n=300 VP+, fielded Sept–Oct 2021 `[S18]` | High but **dated** |
| Time to prepare data for a revenue-impacting decision | **Days to a week, for 76% of companies** | Fivetran / Wakefield `[S18]` | High but dated |
| Hallucinated or incorrect output reaching stakeholders as a top concern | **71% of practitioners** | dbt Labs, n=363, fielded 2025-12-05 → 2026-02-01 `[S16]` | High |
| Trust in data as a stated priority | **66% (2025) → 83% (2026)** | dbt Labs `[S16]` | High |
| Accuracy/hallucination as top GenAI reservation | **24.9%** | Futurum, n=818, 1H 2026 `[S17]` | High |
| Employees actively using purchased BI tools | **≈25%, flat over seven years** | BARC / Eckerson, n=214, via ThoughtSpot `[S22]` | Medium |

### 6.2 What is not sourceable

**No per-analyst ad-hoc queue measurement from a disclosed study exists in the public record.** Every located figure for requests-per-analyst-per-week traces to consultancy or vendor content marketing with no stated methodology: 15–25 requests per week at 30–90 minutes each `[S19]`, and an unsourced "80% of a data team's time" `[S20]` that this pack **rejects and uses nowhere**.

Per `startup-research`'s own quality bar — unfindable facts are stated as unfindable — the pack's position is:

> Queue *length* per analyst is not publicly measured. Request *turnaround* is, at one to four weeks in the enterprise `[S15]`. No artifact in this pack may state a requests-per-week figure.

### 6.3 Verdict on A8, and the reframe it forces

**A8 is closed as partially sourced, and the partial result is better for the pack than a clean one would have been.**

The brief asserts that the pain is *latency and analyst attention*. The sourceable evidence supports the latency half strongly — one to four weeks `[S15]`, days to a week just for preparation `[S18]` — and the attention half only weakly, because per-analyst load is unmeasured.

But the evidence discloses something the brief did not claim, and it is stronger than what the brief did claim. The load-bearing measured facts are about **trust**: 83% now prioritise trust in data, up from 66% `[S16]`; 71% fear hallucinated output reaching stakeholders `[S16]`; 24.9% name accuracy as their top GenAI reservation `[S17]`; 59% are funding semantic layers to constrain AI output `[S17]`; and 76% of businesses have decided without data at all `[S15]` while roughly 25% of employees use the BI tools already bought `[S22]`. Latency evidence is Medium-confidence and second-hand. **Trust evidence is High-confidence, current, and from two independent disclosed surveys.**

The reframe this forces, and which phase 2 should adopt:

> The measured, current, well-sourced problem is not that answers are slow. It is that **fast answers are not yet trustworthy** — and that the organisation's response so far has been to fund a semantic layer `[S17]` or to decide without data at all `[S15]`. Latency is the symptom the analyst feels; verifiability is the constraint the market is actually spending against.

This does not overturn the brief — the beachhead, the mechanism and the vocabulary all stand — and *time-to-verified-answer* already contains both halves. But it changes emphasis: the strongest sourceable argument for this product is verification, not speed, and it should be positioned that way.

## 7. Risks

Ordered by severity, mapped to what would falsify each.

1. **Multi-hop planning does not reach usable reliability.** ≈14.55–16% on DABstep Hard `[S4]`. *Falsified by:* the 295A spike measuring materially higher on a narrow fixed question set. **Kills the venture.**
2. **Error compounding across four to six hops.** Multiplicative `[S13]`; propagation is the primary bottleneck `[S10]`. *Falsified by:* per-hop verification measurably raising end-to-end accuracy over an unverified baseline. **Kills the mechanism; not the product, if lineage makes failure cheap to catch.**
3. **Plausible-but-wrong answers destroy trust faster than correct answers build it.** 81.2% of failures are schema-level and look reasonable `[S2]`. *Falsified by:* analysts detecting seeded wrong answers faster with a hop-level trace than without. **This is the validation layer's first experiment.**
4. **Gravity — absorbed as a warehouse feature.** Sisu `[S56][S57]`, Narrative Science `[S58]`. *Falsified by:* nothing empirically; must be answered structurally by cross-source neutrality. **Kills the venture, not the capstone.**
5. **The semantic-layer dependency reappears.** If acceptable accuracy requires a curated model, the product inherits incumbent failure mode 1 `[S36][S42]`. *Falsified by:* comparable accuracy against an unmodelled Postgres schema versus a modelled one.
6. **Self-hosting is not viable on small models.** Tool-initialisation failure is the leading agent bottleneck and is catastrophic in small models — 89% in qwen2.5:3b `[S11]`. *Falsified by:* a working spike on a self-hostable model. **Directly constrains ASSUMPTIONS A5.**
7. **The ML agent does not fit the loop.** MLE-bench's headline runs on a 12-hour budget `[S9]` against a wall-clock outcome metric. *Falsified by:* a useful modelling result inside a conversational latency budget.
8. **Category timing risk.** >40% of agentic projects forecast cancelled by end-2027 `[S31]`, low confidence; half of agent deployment failures attributed to governance by 2030 `[S29]`.

## 8. Open questions

1. Does a hop-level trace actually make verification cheaper than re-derivation, or does reading someone else's reasoning cost as much as doing it? **Unmeasured anywhere in the literature, and the pack's differentiator depends on the answer.**
2. Does per-hop verification recover enough accuracy to offset compounding at four to six hops? Genie's Inspect `[S32]` suggests a vendor believes so; no published number exists.
3. Can a semantic layer be *learned* from an organisation's query history rather than authored? This is the brief's strongest moat candidate and nothing in this research evidences it either way.
4. What is the real cost per investigation — several agents, several hops, retries — when the incumbent charges per message `[S37][S38]` and caps at 25 queries per user per month `[S44]`?
5. Why has no commercial agentic-BI product published an accuracy benchmark ([sources.md](sources.md), *Named gaps* 2)? Either the numbers are unflattering or the benchmarks are considered unrepresentative — both readings matter, and both favour a project willing to publish one.
6. Does cross-source neutrality actually resist gravity, or does the first serious customer's data simply live in one warehouse anyway?

## Recommended next 3

1. **Adopt §6.3's reframe in `strategy/positioning.md`.** Lead with verifiability, support with latency. The trust evidence is High-confidence and current `[S16][S17]`; the latency evidence is Medium and second-hand `[S15]`. The pack is stronger led by its stronger evidence.
2. **Make open question 1 the validation layer's first experiment.** It is cheap, it is measurable with the beachhead directly, and it is the single assumption beneath the differentiator settled in [competitors.md](competitors.md) §4.
3. **Cite this file's §5.2 in the whitepaper's teardown, unsoftened.** A whitepaper that states the case against its own mechanism and answers it architecturally is more credible than one that omits it — and a reviewer will find DABstep `[S4]` regardless.
