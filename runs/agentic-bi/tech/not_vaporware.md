# Not vaporware — stack, evaluation, cost, and what is actually buildable

**What this is** — One page of concrete commitments: the named stack, how quality gets measured continuously against named benchmarks, the cost model at current API prices, and an explicit split between what a two-person team builds this semester and what is research risk.
**Why it exists** — Everything else in `tech/` describes a system that does not exist. This file is the check on whether it could — with real library names, real prices, and a line drawn between engineering and research. The failure it prevents: a pack whose technical layer is internally consistent and unbuildable, which is the most common way a capstone proposal fails its advisor.
**How to read it** — §4 is the honest split. A skeptic should attack §3's cost model, whose dominant term is a number nobody can currently estimate, and §4's claim that the 295A scope is achievable.
**Depends on / feeds** — Components from [deep_dives.md](deep_dives.md); build order from [product/features_prioritized.md](../product/features_prioritized.md); cost shape from [D05](architecture/D05_model_routing_cost.md). Feeds `financials/` unit economics and the 295A project plan.

---

## 1. The stack — named choices

| Layer | Choice | Why this one |
|---|---|---|
| **Language** | Python 3.12 | The data ecosystem is Python; every profiling, statistics and modelling library below is Python-native |
| **Orchestrator** | Custom, built on a typed plan DAG | Deliberately **not** an off-the-shelf agent framework. The plan must be a validatable, diffable, cacheable data structure (deep dive §2); most frameworks make the plan implicit in control flow, which forfeits the D01 approval gate |
| **Model access** | Provider-agnostic client, customer's own key | ASSUMPTIONS A5. Frontier class for planning and SQL generation; small/fast class for prose and chart choice (D05) |
| **File/CSV engine** | **DuckDB** | In-process, reads CSV/Excel/Parquet directly, real SQL. Turns "the unmodelled CSV" into a queryable source with no ETL step — the single highest-leverage dependency choice in the stack |
| **Warehouse/DB access** | SQLAlchemy + psycopg | Standard, dialect-aware |
| **Profiling** | DuckDB SQL + `pandas` for sampling | Cardinality, uniqueness, overlap and null-rate profiling are all SQL; no profiling framework needed |
| **Modelling** | `scikit-learn` + `lightgbm` | Regularised linear/logistic and gradient-boosted trees (W1 6.1, 6.2). No AutoML framework — P9's minutes-long budget makes search infeasible anyway |
| **Time series** | `statsmodels` STL | Seasonal decomposition (W1 6.6) |
| **App store** | Postgres | Bindings, lineage, investigations (D04) |
| **Audit log** | Append-only JSONL on disk | **Deliberately a file, not a table.** Tom must be able to `grep` it without the application running (D06) |
| **API / web** | FastAPI + a React front end | Conventional; nothing here is differentiating |
| **Packaging** | Docker Compose | Feature #29's under-30-minute quickstart is the gate on the only viable channel |
| **Harness** | `pytest` + a question-set fixture | Feature #1. Ordinary test infrastructure, run as an evaluation loop |

**Two choices worth defending.** *No agent framework* — the plan-as-data-structure requirement is incompatible with frameworks that hide the plan in control flow, and the D01 gate is the cheapest error-catch in the system. *DuckDB* — it makes heterogeneous source handling tractable for two people, because a CSV, a Parquet file and a query result all become the same thing.

## 2. The evaluation loop

Continuous, not a one-off benchmark run.

| What | How | Named benchmark / baseline |
|---|---|---|
| **Multi-hop execution accuracy (O3)** | 30–50 question fixed set over a known schema with ground-truth results; run on every merge | Baseline to beat: **DABstep Hard ≈14.55–16%** `[S4]`. Contextual reference: Spider 2.0-Snow 96.70% / DBT 65.60% `[S1]`, BIRD 80.04% vs 92.96% human `[S3]` |
| **Silent-error rate (O4)** | Seeded-error set — planted wrong joins, grains, region mappings; measure what escapes every check | No external benchmark exists. **This number is the pack's own contribution** |
| **Verifier coverage** | % of seeded errors caught by any D02 check | Replaces the whitepaper's judgement-based 6.7×→4.0× discount with a measurement |
| **Consistency** | `pass^k` over repeated runs of the same question | τ-bench: >60% `pass^1` → <25% `pass^8` `[S5]`. Currently unmeasured — wave 2's 2.2.3 gap |
| **Expected attempts per investigation** | Byproduct of harness runs | Feeds §3's cost model, whose dominant term this is |
| **Calibration** | Does surfaced doubt predict actual error? | Reliability diagram against harness ground truth. Currently **unimplemented** — the matrix's HIGH-severity gap |

**The whole loop runs offline against fixtures.** No customer data, no deployment required, and it produces every number the pack claims except O1 and O2 — which need humans and belong to `validation/`.

## 3. Cost model at current prices

Per investigation, and the honest version of it.

**The shape.**

```
cost = (plan synthesis + schema linking + SQL generation) × expected_attempts
     + small-model calls (prose, chart choice)
     + warehouse compute for queries AND verification
```

**What is knowable.** Verification is pure SQL — **zero model tokens** (D05). Statistical modelling is `scikit-learn` — zero model tokens. The frontier-model surface is narrow: planning, term resolution, SQL generation, replanning.

**Reference anchor.** Snowflake Cortex Analyst bills ≈6.7 credits per 100 messages at $2.00–2.20 per AI credit — **≈$0.134 per message**, with warehouse compute billed separately `[S38][S39]`. That is a real market price for a single-hop text-to-SQL exchange.

**A defensible estimate.** A six-hop investigation issues roughly one planning call, one resolution call and six generation calls — call it eight frontier exchanges. At Cortex-comparable per-exchange economics that is **≈$1.10 per investigation at one attempt each**.

**The term that dominates and cannot be estimated.** `expected_attempts`. DABstep puts multi-step data reasoning at ≈14.55–16% on hard tasks `[S4]`, which implies **retries are the common case, not the exception.** At three attempts per failing step the figure is not $1.10 but several times that.

> **A cost model assuming one clean pass will be wrong by a large multiple. `financials/` must model cost per attempt × expected attempts, and expected attempts is a number the 295A harness produces — not one this document can supply.**

Inference prices fall unevenly — a fixed benchmark score went from ≈$60 to ≈$0.06 per million tokens between late 2021 and late 2024 `[S63]`, with per-year declines of 9×–900× depending on the capability milestone `[S64]`. That trend helps and is not a substitute for measuring the retry count.

**Cost lands on the customer's provider bill**, not in a hosted margin (A5), which changes the conversation from *our unit economics* to *your cost per question* — and makes the per-investigation meter (D05) a customer-facing feature rather than internal telemetry.

## 4. Buildable this semester vs. research risk

### Buildable — 295A, two people, one semester

| Item | Confidence |
|---|---|
| Evaluation harness + fixed question set + seeded errors | **High** — `pytest` and fixtures |
| Postgres connector, read-only | **High** |
| CSV/Excel via DuckDB | **High** |
| Semantic resolver: hybrid retrieval, value linking, margin thresholding | **High** — established IR |
| Binding store with provenance and schema-version invalidation | **High** — a data model |
| SQL generation with execution-feedback repair | **High** — the loop is standard `[S14]` |
| Hop verifier: the six structural checks | **High** — they are SQL |
| Lineage capture + single-hop replay + export artifact | **High** — engineering |
| Plan surface with approval gate | **Medium-high** — the UI is the work, not the logic |

### Research risk — named, not hidden

| Item | Risk | Why |
|---|---|---|
| **Plan synthesiser quality on real schemas** | **HIGH** | ≈14.55–16% on DABstep Hard `[S4]`. Constrained schemas, static validation and short plans are mitigations, not solutions. **This is the venture's central risk and the spike exists to measure it** |
| **Verifier coverage of plausible failures** | **MEDIUM-HIGH** | The checks provably catch *countable* failures. P3's dangerous failures are the plausible ones `[S2]`. Coverage is unmeasured — the whitepaper's largest soft number |
| **Verification cheaper than re-derivation (O2)** | **HIGH — and not a technical risk** | Needs humans, not code. Gates the entire model ([whitepaper.md](whitepaper.md) §2.4) |
| **Override re-flow across a grain change** | MEDIUM | Honest fallback is invalidate-and-replan (D02). Pre-decided cut #4 |
| **Useful modelling inside a minutes budget** | MEDIUM | MLE-bench's 36.4% runs on 12 hours `[S9]`. The minutes-long version is unspecified anywhere |

### The honest summary

**Nine of nine Now-tier items are ordinary engineering.** The system's substrate — connectors, profiling, verification checks, lineage, export — is buildable by two competent people in a semester, because it is built from techniques that are mostly decades old (wave 1: 43 of 44 established practice).

**The two things that are not engineering are the two the venture depends on**: whether the planner works on real schemas, and whether the verifier catches the failures that matter. Both are measurement problems before they are research problems, which is exactly why the harness is feature #1 and not feature #20.

**What a reviewer should conclude:** this is not a wrapper — the verification layer, the lineage model and the cross-source reconciler are real engineering with named methods. It is also **not solved**, and the two unsolved parts are named here rather than buried.

## Recommended next 3

1. **Build the harness and the seeded-error set in week one**, before any agent. Every number the pack claims depends on it, and it is the only artifact that converts research risk into a measurement.
2. **Measure `expected_attempts` explicitly and publish it.** It is the dominant unknown in the cost model and nobody in the market publishes it.
3. **Run the O2 timed task with five analysts in parallel with week-one engineering.** It needs no code, it gates the entire model, and discovering in month four that verification costs re-derivation would invalidate the build rather than merely delay it.
