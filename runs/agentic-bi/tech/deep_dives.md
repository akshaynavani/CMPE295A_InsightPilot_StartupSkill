# Deep dives — the tier-1 algorithms and systems

**What this is** — The seven algorithmic components that carry the mechanisms in [whitepaper.md](whitepaper.md), each as: the one question it answers → algorithmic approach with real method names → inputs and outputs → the key design choice and why → failure modes and fallbacks.
**Why it exists** — The whitepaper claims mechanisms; this file is where a reviewer checks whether they are implementable with named methods rather than assertions. The specific failure it prevents: a "multi-agent orchestration layer" that turns out on inspection to be one prompt calling a model in a loop. Every entry below either names a real method or is labelled research risk.
**How to read it** — The *Failure modes* row on each is the honest half. A skeptic should attack §2 (the planner, which is the component with the most research risk and the weakest benchmark support) and §4's coverage claim, which is the largest soft number in the whitepaper.
**Depends on / feeds** — Mechanisms from [whitepaper.md](whitepaper.md) §2; capability evidence from [research/capability_table.md](../research/capability_table.md); principles from [product/PRD.md](../product/PRD.md) §3. Feeds the [architecture set](architecture/00_INDEX.md), [techniques/](techniques/decision_tree.md) and [not_vaporware.md](not_vaporware.md).

---

## Component map

| # | Component | Answers | Whitepaper mechanism | Research risk |
|---|---|---|---|---|
| 1 | **Semantic resolver** | *What do the words in this question mean in this schema?* | B | Low |
| 2 | **Plan synthesiser** | *What ordered steps answer this, over which sources?* | A | **High** |
| 3 | **Query generator + repair loop** | *What SQL implements this step, and does it run?* | A | Low–Medium |
| 4 | **Hop verifier** | *Did this step do what the plan said?* | C | **Medium–High** |
| 5 | **Cross-source reconciler** | *Do these two sources agree on keys, grain and coverage?* | C | Medium |
| 6 | **Lineage recorder and replayer** | *What exactly happened, and can it be re-run?* | D | Low |
| 7 | **Time-boxed modelling agent** | *Will this continue, and what would I not trust about that?* | E | Medium |

---

## 1. Semantic resolver

**Goal.** Given a question and a set of connected sources, bind every business term to a concrete expression over concrete columns — or refuse and ask.

**Algorithmic approach.**
- **Schema linking** by hybrid retrieval: BM25 over column names, comments and dbt descriptions, plus dense embedding retrieval over the same corpus, fused with **reciprocal rank fusion**. Schema linking is the standard term for this sub-problem in the text-to-SQL literature and is where the dominant error class lives.
- **Value-based linking**: sample distinct values from candidate columns and match against literals in the question (`"Southwest"` → the column that actually contains it). This resolves cases pure name-matching cannot.
- **Semantic-layer precedence**: where a dbt or Cube definition exists for a term, it wins outright over any inferred binding `[S66]`. Not a tiebreak — a hard override.
- **Ambiguity detection** by margin thresholding on the fused ranking: when the top-2 candidates are within a margin, or resolve to different grains, halt and ask rather than take the argmax.
- **Binding persistence**: confirmed resolutions are written to an organisation-scoped store, keyed by normalised term, and take precedence on later questions.

**Inputs.** Question text; live schema (tables, columns, types, comments, FKs); sampled distinct values; dbt/Cube manifests when present; the binding store.
**Outputs.** A set of `term → expression` bindings each with provenance (`from_semantic_layer` | `confirmed_by_analyst` | `inferred`), or an ambiguity event with ranked candidates and evidence.

**Key design choice: halt-and-ask on margin, rather than take the top candidate and proceed.**
*Rationale.* Schema-level errors — wrong column selection and semantic misinterpretation — are **81.2% of 4,602 analysed incorrect queries** `[S2]`. Any silent argmax on an ambiguous term samples directly from the dominant failure distribution. Asking costs the user seconds; guessing costs them a plausible wrong answer they cannot detect (P3).

**Failure modes and fallbacks.**
| Failure | Fallback |
|---|---|
| No candidate above threshold | Report unresolvable with nearest matches by name similarity; offer manual definition. **Never silently proceed** |
| Ambiguity fires on every question — user fatigue | Margin threshold is tunable per deployment; confirmed bindings suppress repeats. If fatigue persists, the schema genuinely is ambiguous and that is a finding |
| Binding goes stale when schema changes | Bindings validate on load; a broken one renders struck-through with *"column no longer exists"* rather than failing silently. Execution accuracy drops up to 24 points under schema evolution `[S2]` — this is that failure, surfaced |
| Sampled values contain PII | Columns flagged sensitive are excluded from value-based linking and from model context (PRD §8) |

---

## 2. Plan synthesiser

**Goal.** Decompose a question into an ordered set of agent tasks over named sources, with explicit data dependencies.

**Algorithmic approach.**
- **Constrained generation into a typed plan schema** — a DAG of typed steps (`fetch`, `join`, `aggregate`, `compare`, `model`, `render`), each naming its source and its inputs — rather than free-text reasoning. The plan is a data structure that can be validated, diffed and cached, not a paragraph.
- **Static validation before execution**: every referenced source is connected, every step's inputs exist upstream, no cycles, no step reads a column no binding resolved.
- **Plan caching by semantic signature**: normalised question plus resolved bindings plus source set hashes to a key; a hit reuses the approved plan. This is the determinism mechanism for P4 — `pass^k = p^k` decay means re-derivation is itself a source of drift `[S5]`.
- **Replanning on invalidation**: a failed hop verification or a degenerate result (empty, or coverage below threshold) invalidates the remaining sub-DAG, which is regenerated with the failure as context.
- **Hop-count ceiling** with an explicit warning above it, from the compounding arithmetic — 95% per hop is ≈74% over six `[S13]`.

**Inputs.** Question; bindings; connected source catalogue; conversation context (established facts, source scope).
**Outputs.** A validated plan DAG; or a refusal naming what is missing.

**Key design choice: the plan is shown and approved before any query runs.**
*Rationale.* It converts the dominant cost of a wrong plan from *queries executed and a wrong answer delivered* to *one edit*. In the beachhead journey this catches an over-broad fetch in 15 seconds. It is also the only intervention that acts on error compounding **before** it starts rather than detecting it afterwards.

**Failure modes and fallbacks.**
| Failure | Fallback |
|---|---|
| **Plan is plausible and wrong** — the central risk | Per-hop verification (§4) is the second line; the shown-plan review is the first. Neither is sufficient alone, and this is the residual risk the 295A spike must measure |
| Question needs more hops than the ceiling | Warn, and suggest splitting into two investigations. Do not silently exceed |
| Replanning loops — each revision fails verification | Hard iteration cap, then surface partial results with the failure. **A partial investigation with honest lineage is a better outcome than a confident synthesis** |
| Cache returns a stale plan after a schema change | Signature includes a schema-version component; changed schema misses the cache |

**Research risk: HIGH — and this is the component the venture rests on.** DABstep measures the best agents at **≈14.55–16% on its Hard split against 76.39% on Easy**, over 450+ tasks drawn from a real financial analytics workload `[S4]`. Multi-step data reasoning is the field's weakest measured capability (P10). Constrained plan schemas, static validation and short plans are mitigations, not solutions. **Labelled research risk rather than presented as solved.**

---

## 3. Query generator and repair loop

**Goal.** Turn one plan step into SQL that runs and returns what the step promised.

**Algorithmic approach.**
- **Constrained decoding against the resolved bindings** — generation is scoped to columns a binding named, which removes most of the hallucinated-column failure mode by construction.
- **Execution-feedback repair**: on a database error, feed the error text and the failing statement back for a bounded number of repair attempts. This is the mechanism behind Snowflake's Arctic-Text2SQL-R1, where execution-feedback RL makes small models competitive with much larger ones `[S14]`.
- **Dialect adaptation** per connector (Postgres, DuckDB for file sources, Snowflake later).
- **Cost guard**: `EXPLAIN` before execute; a plan exceeding a configured cost threshold is surfaced rather than run.

**Inputs.** One plan step; bindings; source dialect and schema.
**Outputs.** Executed result set with row counts and grain; or a repair-exhausted failure with the attempts recorded.

**Key design choice: repair on execution feedback, not on model self-critique.**
*Rationale.* A database error is ground truth. Model self-assessment of its own SQL is not, and P7 says verification must come from running something different rather than from asking the model whether it is confident.

**Failure modes and fallbacks.**
| Failure | Fallback |
|---|---|
| Runs cleanly, returns wrong data | **Not caught here** — this is §4's job, and it is the failure mode P3 warns about |
| Repair loop exhausts | Surface the step as failed with all attempts in the lineage. The attempts are diagnostic information for the analyst |
| Query too expensive | Cost guard surfaces the estimate and asks before running |

---

## 4. Hop verifier

**Goal.** Establish whether a step did what the plan said, using something other than the model's own opinion.

**Algorithmic approach.** A battery of cheap, structurally different checks per step type:

| Check | Applies to | Catches |
|---|---|---|
| **Row-count reconciliation** | joins | Fan-out and row loss |
| **Grain assertion** — is the declared key unique in the output? | joins, aggregations | The classic silent fan-out |
| **Coverage / anti-join count** | cross-source joins | Unmatched keys (the journey's 8% region-code failure) |
| **Null-rate delta** | any transform | Columns silently emptied by a bad join |
| **Boundary totals** — does a disaggregated sum reconcile to the undisaggregated one? | aggregations, splits | Double-counting, dropped rows |
| **Type and range sanity** | any | Unit errors, sign flips, impossible dates |
| **Cardinality plausibility** vs. source statistics | filters | Over-restrictive predicates |

Checks are **declarative and cheap** — separate SQL against the same source — not model calls.

**Inputs.** Step output; the step's declaration (expected grain, expected keys); source statistics.
**Outputs.** Per-check pass/fail with numbers; an aggregate hop state (green / amber / red); the list of checks *not* performed.

**Key design choice: verify by running a different, cheaper query — never by asking the model.**
*Rationale.* P7, corroborated by Databricks arriving at the same insight independently: *Inspect* authors smaller SQL statements to verify specific aspects of a generated query and regenerates `[S32]`. A model asked to check its own output shares the failure mode that produced the output.

**Failure modes and fallbacks.**
| Failure | Fallback |
|---|---|
| **All checks pass and the answer is wrong** | The residual failure mode, and it is the important one. A correct-looking join at the wrong *semantic* grain — right cardinality, wrong meaning — passes every check above. Mitigated only by the shown plan and the analyst's own inspection |
| Amber fatigue — too many warnings, all ignored | Thresholds tuned per source; verification results feed the doubt block ranked by severity, not listed flat |
| A check is more expensive than the step | Skip and record as not-performed. **The not-performed list must be visible** — an unlisted skipped check is a false reassurance |

**Research risk: MEDIUM–HIGH, and it carries the whitepaper's largest soft number.** The whitepaper discounts this mechanism from an observed 6.7× to a claimed 4.0× precisely because **coverage of the failure space is unmeasured**. The checks above provably catch *countable* failures. P3's dangerous failures are the plausible ones `[S2]`. The seeded-error test set (feature #2) exists to convert this judgement into a measurement, and until it runs, this row is the honest weak point of the architecture.

---

## 5. Cross-source reconciler

**Goal.** Determine whether two sources can be joined at all, and on what.

**Algorithmic approach.**
- **Key candidate discovery**: profile candidate join columns for cardinality, uniqueness and value-overlap (Jaccard on sampled distinct values).
- **Fuzzy domain alignment** on low-cardinality dimensions: detect that `SW` / `SOUTHWEST` / `SW-1` are one domain expressed three ways, via normalisation plus edit distance plus co-occurrence, and **propose** the mapping rather than applying it.
- **Grain inference** on each side before joining, so a many-to-many is caught before it fans out.
- **Coverage reporting** as a first-class output, not a diagnostic: matched, unmatched-left, unmatched-right, with sample unmatched keys.

**Inputs.** Two result sets with profiles; any existing semantic-layer join paths (which take precedence `[S66]`).
**Outputs.** Proposed join key and mapping, with coverage; or a refusal to join with the reason.

**Key design choice: propose the domain mapping, never apply it silently.**
*Rationale.* A region-code mapping is a business fact, not a string-similarity result. The system's job is to surface the candidate mapping with evidence and let the analyst confirm — after which it persists as a binding (§1) and never needs proposing again. This is the single highest-value thing to persist, because it is the friction the whitepaper measures at 20 minutes.

**Failure modes and fallbacks.**
| Failure | Fallback |
|---|---|
| Fuzzy alignment produces a plausible wrong mapping | Analyst confirmation is mandatory before first use; coverage is always reported alongside |
| No viable join key | Refuse, and say what was profiled. **"These two sources cannot be joined on anything I can find" is a valid and useful answer** |
| Semantic drift — same key, different meaning across sources | Not detectable from data. Surfaced only if the analyst knows, which is why annotation types include *data-provenance issue* ([product/ux_spec.md](../product/ux_spec.md) §8) |

---

## 6. Lineage recorder and replayer

**Goal.** Record what happened in a form that is inspectable, re-runnable and portable — and make checking one hop cost seconds.

**Algorithmic approach.**
- **Structured event log per handoff**: source identifiers, exact statement issued, parameters resolved, row counts in/out, grain in/out, verification results, timing, and any override with its annotation type.
- **Content-addressed step outputs** so a re-run can diff against the stored result rather than merely re-execute.
- **Deterministic replay** of a single hop: re-issue the recorded statement with recorded parameters against current data, and diff.
- **Self-contained export**: the full record serialised into one file that renders without the application — question, plan, hops, queries, counts, verification, answer, sign-off, model card.

**Inputs.** Every agent handoff.
**Outputs.** The investigation record; a single-hop replay result with diff; the export artifact.

**Key design choice: the export must be readable without the product running.**
*Rationale.* Four independent jobs depend on it — differentiator proof, the GTM compounding loop's edge, the buyer's provenance requirement, and the instrument that measures verification cost. It is also what earns the high edge's attention: Dr. Chen's first act is to open it in a text editor to confirm it is genuinely self-contained ([product/journeys/edge_high.md](../product/journeys/edge_high.md) §2).

**Failure modes and fallbacks.**
| Failure | Fallback |
|---|---|
| Replay fails because the source changed | **A finding, not an error** — surface the diff. Non-reproducibility of a prior answer is exactly what an analyst needs to know |
| Record grows large on wide result sets | Store row counts, schemas and samples rather than full result sets; full outputs are re-derivable from the recorded statement |
| Recorded statement contains embedded credentials | Parameters are recorded separately from secrets; secrets never enter the record |

---

## 7. Time-boxed modelling agent

**Goal.** Answer *will this continue* well enough to guide investigation, inside a conversational latency budget, while being explicit about everything it did not do.

**Algorithmic approach.**
- **Automatic target construction** from the question, stated explicitly in the model card as a definition the human can reject.
- **Leakage screening** before fitting: exclude features whose availability postdates the observation window, correlate suspiciously with the target, or derive from it. Each exclusion is recorded **with its reason**.
- **Split strategy by entity with a time embargo**, not random — the standard defence against temporal leakage in churn and forecasting problems.
- **Small model portfolio**: regularised linear/logistic baseline plus gradient-boosted trees; k-fold cross-validation with reported dispersion. No architecture search.
- **Explicit budget accounting**: what was tried, and what was not, with the not-attempted list published as part of the output.

**Inputs.** A prepared feature table from upstream hops; the question; a wall-clock budget in minutes.
**Outputs.** Model card — target definition, split strategy, features used with importances, features excluded with reasons, algorithms tried, **not-attempted list**, metric with uncertainty.

**Key design choice: publish the not-attempted list, and make it exhaustive.**
*Rationale.* P9. MLE-bench's 36.4% medal rate runs on a **12-hour budget** `[S9]`; a minutes-long budget cannot approach it, and the only honest response is to say what the budget bought and what it did not. The renunciation is what makes the rest credible to the person who has to approve it — and an omission converts the list from an honest disclosure into a lie by omission, which is Dr. Chen's stated stopping condition ([product/journeys/edge_high.md](../product/journeys/edge_high.md) §7.1).

**Failure modes and fallbacks.**
| Failure | Fallback |
|---|---|
| Insufficient data to model | **Refuse and say why.** Producing a weak model silently is the worst available outcome — P3 in the most dangerous place |
| Leakage screening misses a leak | The model card's feature list and target definition are exactly what a data scientist reviews; the design assumption is human review at this hop, not automated safety |
| Analyst reads a screening baseline as a production forecast | Model card states its scope; the high-edge journey shows the correct reading and the product must not imply more |

---

## What is buildable and what is research

| Component | Status |
|---|---|
| 1 Semantic resolver | **Buildable.** Established methods, well-understood failure modes |
| 3 Query generator + repair | **Buildable.** Execution-feedback repair is standard practice `[S14]` |
| 5 Cross-source reconciler | **Buildable.** Data-profiling techniques, decades old |
| 6 Lineage recorder | **Buildable.** Engineering, not research |
| 7 Modelling agent | **Buildable**, with the P9 time-box honestly enforced |
| **4 Hop verifier** | **Partly research.** The checks are trivial; their *coverage of the plausible-failure space* is unmeasured and is the whitepaper's largest soft number |
| **2 Plan synthesiser** | **Research risk.** ≈14.55–16% on DABstep Hard `[S4]`. Constrained schemas and short plans are mitigations, not solutions |

**The honest summary.** Five of seven components are engineering. The two that are not — the planner and the verifier — are exactly the two the venture depends on, and both are named as research risk here rather than presented as solved. That is the same conclusion [research/survey.md](../research/survey.md) §5.3 reached from the evidence side, arrived at independently from the architecture side.

## Recommended next 3

1. **Prototype component 4 against the seeded-error set before building 2.** The verifier is cheap to build and its coverage number determines whether the whole verify beat is real. Building the planner first means a year of work resting on an unmeasured assumption.
2. **Implement component 1's binding persistence in the first sprint.** It attacks 81.2% of the failure mass `[S2]`, it is low-risk, and it is the only component that produces the compounding effect the flywheel depends on.
3. **Write component 7's model card format before writing component 7.** The not-attempted list is the credibility mechanism, and a format designed after the modelling code will quietly omit whatever was inconvenient to track.
