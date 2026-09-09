# Technique wave 2 — advanced and theory-grounded

**What this is** — 38 techniques with a formal or theoretical grounding — from database theory, program synthesis, statistical decision theory, reliability engineering and queueing theory — that this system uses, could use, or deliberately declines to use.
**Why it exists** — Wave 1 establishes that the foundation is standard practice. This wave is where a technical reviewer looks for evidence that the harder problems have been thought about with the right tools: the plausible-wrong-answer problem is a *coverage* problem in the formal sense, error compounding is a *reliability* problem, and the review queue is a *queueing* problem. The failure it prevents: solving hard problems with prompt engineering when a formal method exists.
**How to read it** — The **Status** column distinguishes used, candidate, and *declined with a reason*. A skeptic should attack the declines — an unjustified decline is a gap wearing a decision's clothing.
**Depends on / feeds** — Builds on [wave1.md](wave1.md); anchored to [research/survey.md](../../research/survey.md) and [deep_dives.md](../deep_dives.md). Feeds [decision_tree.md](decision_tree.md) and [technique_feature_matrix.md](technique_feature_matrix.md).

---

**Count: 38**, across 6 clusters. **Stopped short of 50 honestly** — the remaining candidates were from formal-verification and distributed-systems literature with no plausible application to a single-tenant read-only analytics tool. Listing them would have been padding.

## Cluster 1 — Program synthesis and constrained generation (7)

| # | Technique | Mechanism | Anchor | Status |
|---|---|---|---|---|
| 2.1.1 | **Grammar-constrained decoding** | Generation restricted to a formal grammar so output is syntactically valid by construction | Standard in structured generation | ✅ used — the typed plan DAG (§2) |
| 2.1.2 | **Type-directed synthesis** | Use column types to prune candidate expressions before generation | Program-synthesis literature | ✅ used — §3 |
| 2.1.3 | **Synthesis from input-output examples** | Infer a transform from example rows | FlashFill lineage | 🔶 candidate — would strengthen the override path |
| 2.1.4 | **Candidate generation with execution-based reranking** | Generate *n* programs, execute all, rank by agreement | Salesforce lifted a production text-to-SQL agent from ~50% to ~80% efficacy by generating 10 candidates per prompt `[S2]` | 🔶 **strong candidate — the highest-value unimplemented technique in this file** |
| 2.1.5 | **Self-consistency by majority vote over samples** | Sample multiple times, take the modal answer | Standard | 🔶 candidate — cheaper than 2.1.4, weaker signal |
| 2.1.6 | **Sketch-based synthesis** | Fix the query skeleton, synthesise only the holes | Program-synthesis literature | ⬜ declined — the plan DAG already plays this role |
| 2.1.7 | **Abstract interpretation over query semantics** | Reason about what a query *can* return without running it | Formal methods | ⬜ declined — cost far exceeds value when execution is cheap and available |

**On 2.1.4.** The evidence is unusually direct and comes from a production system at scale `[S2]`. It trades cost for accuracy — *n* generations and *n* executions per step — which D05's cost model must absorb. It belongs on the roadmap as the first accuracy upgrade after the harness can measure whether it helps.

## Cluster 2 — Reliability and error propagation (7)

| # | Technique | Mechanism | Anchor | Status |
|---|---|---|---|---|
| 2.2.1 | **Per-step verification with early abort** | Check each hop; stop rather than propagate | Error propagation is the primary agent reliability bottleneck `[S10]` | ✅ used — D02 |
| 2.2.2 | **Compounding-budget analysis** | Compute expected end-to-end reliability from per-hop rates and cap plan length | 95% over six hops ≈ 74% `[S13]` | ✅ used — plan-length discipline |
| 2.2.3 | **`pass^k` reliability measurement** | Measure whether *k* repeated attempts all succeed, not whether one does | τ-bench: >60% `pass^1` falls below 25% `pass^8` `[S5]` | 🔶 **candidate — belongs in the harness.** The right metric for P4, and currently unmeasured |
| 2.2.4 | **Bounded retry with failure as context** | Cap replanning; pass the failure into the next attempt | Standard; D02's cap | ✅ used |
| 2.2.5 | **Graceful degradation to partial results** | Return what succeeded with honest lineage rather than synthesising | D02's `PARTIAL` exit | ✅ used |
| 2.2.6 | **Failure-mode taxonomy for diagnosis** | Classify errors into named categories to find systematic weaknesses | AgentErrorTaxonomy `[S10]`; 12-category tool-invocation taxonomy `[S11]` | 🔶 candidate — would structure the harness's error analysis |
| 2.2.7 | **Circuit breaking on repeated source failure** | Stop hammering a failing source | Standard resilience | ✅ used |

## Cluster 3 — Statistical decision theory and uncertainty (6)

| # | Technique | Mechanism | Anchor | Status |
|---|---|---|---|---|
| 2.3.1 | **Conformal prediction** | Distribution-free prediction intervals with a coverage guarantee | Modern uncertainty quantification | 🔶 **candidate for the ML agent** — gives a defensible interval rather than a point estimate, which is what Dr. Chen actually needs |
| 2.3.2 | **Calibration measurement (reliability diagrams)** | Test whether stated confidence matches observed frequency | Classical | 🔶 candidate — **the only principled way to know whether doubt surfacing is honest** |
| 2.3.3 | **Bootstrap confidence intervals** | Resample to estimate dispersion without distributional assumptions | Classical | ✅ used — §7 metric uncertainty |
| 2.3.4 | **Bonferroni / FDR correction** | Adjust for multiple comparisons when scanning many dimensions | Classical | 🔶 **candidate, and a real gap.** Contribution analysis (1.5.4) scans many dimension members; without correction it manufactures spurious "drivers" |
| 2.3.5 | **Power analysis before a comparison** | Determine whether the data can support the question asked | Classical | 🔶 candidate — would let the system say *"this segment is too small to answer that"* |
| 2.3.6 | **Presenting confidence as a score to users** | — | P3 forbids it | ⬜ **declined by principle.** Never present a confidence percentage as accuracy |

**On 2.3.4.** This is the sharpest technical gap wave 2 surfaces. Contribution analysis over a high-cardinality dimension is a multiple-comparisons problem, and an uncorrected scan will confidently name a "driver" that is noise. Sisu commercialised this class of analysis `[S56]`; a system doing it without correction produces exactly the plausible-wrong-answer P3 warns about, and no structural check in D02 would catch it.

## Cluster 4 — Retrieval and ranking (6)

| # | Technique | Mechanism | Anchor | Status |
|---|---|---|---|---|
| 2.4.1 | **Hybrid sparse-dense retrieval with RRF** | Fuse lexical and semantic ranking | Standard | ✅ used — §1 |
| 2.4.2 | **Cross-encoder reranking** | Re-score top-*k* candidates with a more expensive joint model | Standard IR | 🔶 candidate — improves schema linking on wide schemas, where accuracy is 30–36% `[S2]` |
| 2.4.3 | **Hard-negative mining** | Train retrieval on confusable column pairs | Standard | ⬜ declined for now — requires training infrastructure the system does not have |
| 2.4.4 | **Query expansion from the binding store** | Expand terms using confirmed organisational synonyms | The flywheel applied to retrieval | ✅ used — §1 |
| 2.4.5 | **Learning-to-rank from override signal** | Use analyst corrections as relevance labels | Feeds on D04's `override_count` | 🔶 **candidate — the most direct path from the flywheel to measurable accuracy gain** |
| 2.4.6 | **Schema summarisation for context budgeting** | Compress a wide schema to fit model context | Necessary above a few hundred columns | 🔶 candidate — Cortex's semantic model caps near 32K tokens for this reason `[S36]` |

## Cluster 5 — Database and dimensional theory (6)

| # | Technique | Mechanism | Anchor | Status |
|---|---|---|---|---|
| 2.5.1 | **Normalisation theory (BCNF reasoning)** | Reason about grain and redundancy formally | Classical DB theory | ✅ used — grain inference (§5) |
| 2.5.2 | **Conjunctive-query containment** | Determine whether one query's results subsume another's | Classical DB theory | 🔶 candidate — a formal basis for "verify by independent path" (1.4.7) |
| 2.5.3 | **Join-order and cardinality estimation** | Estimate intermediate sizes to avoid explosions | Classical query optimisation | ✅ used — via `EXPLAIN` |
| 2.5.4 | **Slowly-changing-dimension awareness** | Recognise that a dimension's history changes its join semantics | Dimensional modelling | 🔶 **candidate, and a real gap** — SCD Type 2 tables joined naively produce silently wrong grain |
| 2.5.5 | **Semantic-layer metric algebra** | Compose metrics from governed definitions rather than raw SQL | dbt/Cube model `[S66]` | ✅ used — consumed, not authored (D07) |
| 2.5.6 | **Materialised-view matching** | Rewrite a query against an existing aggregate | Classical | ⬜ declined — an optimisation for a system with volume this one does not have |

**On 2.5.4.** SCD Type 2 is the second-sharpest gap. A dimension table with `valid_from`/`valid_to` rows joined without a temporal predicate fans out silently — and unlike a coverage failure, the row-count check *does* fire, so it looks like a caught error rather than a semantic one. Worth an explicit detection rule in the reconciler.

## Cluster 6 — Queueing and operations (6)

| # | Technique | Mechanism | Anchor | Status |
|---|---|---|---|---|
| 2.6.1 | **Queueing-theoretic service-time analysis** | Model wait as ρ/(1−ρ) to reason about latency gains | [whitepaper.md](../whitepaper.md) §3.1 | ✅ used — **and its result deliberately not claimed** (§3.2) |
| 2.6.2 | **Induced-demand modelling** | Recognise that λ rises when service time falls | 76% currently decide without data `[S15]` — suppressed demand | ✅ used — the reason §3.1's multiplier is withdrawn |
| 2.6.3 | **Priority queue discipline** | Order review by severity rather than arrival | [ux_spec.md](../../product/ux_spec.md) §10 sorts amber first | ✅ used |
| 2.6.4 | **Little's Law for queue depth** | L = λW; relate depth, arrival rate and wait | Classical | 🔶 **candidate — the right instrument for the A12 risk.** Review-queue depth is the leading indicator |
| 2.6.5 | **Utilisation-based overload warning** | Warn before the queue becomes unrecoverable rather than after | Operations practice | 🔶 candidate — D08 tracks queue depth; this turns it into an alert |
| 2.6.6 | **Batch processing to reduce switching cost** | Group reviews to avoid context-switch overhead | The day-in-life journey's 11:40 batching | ✅ used |

## Summary

| Status | Count |
|---|---|
| ✅ Used | 17 |
| 🔶 Candidate | 16 |
| ⬜ Declined with reason | 5 |
| **Total** | **38** |

## The three gaps this wave surfaces

Ranked by how badly they would bite, and none of them is visible from wave 1.

1. **No multiple-comparisons correction (2.3.4).** Contribution analysis over a high-cardinality dimension will name spurious drivers, and no structural check in D02 catches it. **This is a plausible-wrong-answer generator sitting inside a feature the Analytics agent already has.**
2. **No slowly-changing-dimension handling (2.5.4).** SCD Type 2 joins fan out silently, and the row-count check misfires as a caught error rather than a semantic one.
3. **No `pass^k` measurement (2.2.3).** P4 asserts consistency matters; nothing in the harness currently measures it, and τ-bench shows the gap between `pass^1` and `pass^8` is where reliability actually lives `[S5]`.

**All three belong in the harness or the reconciler before the ML agent is built.** They are cheaper than the ML agent and they attack the failure class that decides whether the product is trustworthy.
