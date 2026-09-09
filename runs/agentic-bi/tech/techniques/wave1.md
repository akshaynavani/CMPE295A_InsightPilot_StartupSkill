# Technique wave 1 — established practice

**What this is** — 44 techniques from the established practice of data engineering, analytics, database systems and applied statistics that this system uses or could use. Clustered by sub-discipline, each with a one-line mechanism and an evidence anchor.
**Why it exists** — [deep_dives.md](../deep_dives.md) names seven components; this is the vocabulary those components are built from, and it is where a reviewer checks that the system rests on decades-old, well-understood methods rather than on prompting. The specific failure it prevents: an architecture whose only named technique is "LLM."
**How to read it** — The **Used** column separates what the design actually calls for from what is available and unused. A skeptic should attack the orphans — techniques listed but not used are either padding or a missed opportunity, and [technique_feature_matrix.md](technique_feature_matrix.md) adjudicates which.
**Depends on / feeds** — Anchored to [research/capability_table.md](../../research/capability_table.md) and [deep_dives.md](../deep_dives.md). Feeds [decision_tree.md](decision_tree.md) and [technique_feature_matrix.md](technique_feature_matrix.md).

---

**Wave scope.** Established techniques — things a competent data engineer or analyst would recognise and that predate the current generation of language models. Wave 2 covers advanced and theory-grounded methods; wave 3 covers AI-native and cross-domain imports.

**Count: 44**, across 7 clusters. **This wave stopped short of 50 deliberately**: the remaining candidates were either duplicates under different names (a dozen variants of "profile the data") or belong to adjacent fields this system does not touch (stream processing, OLAP cube design, MDM). Padding to 50 would have meant listing the same technique three ways, which is the red flag this file exists to avoid.

## Cluster 1 — Schema understanding and linking (8)

| # | Technique | Mechanism | Evidence anchor | Used |
|---|---|---|---|---|
| 1.1 | **Schema introspection** | Read tables, columns, types, comments, FK constraints from the catalogue | Standard DB practice | ✅ deep dive §1 |
| 1.2 | **BM25 retrieval over schema text** | Lexical ranking of columns against question terms | Classical IR | ✅ §1 |
| 1.3 | **Dense embedding retrieval over schema** | Semantic ranking where names and question vocabulary diverge | Standard | ✅ §1 |
| 1.4 | **Reciprocal rank fusion** | Combine lexical and dense rankings without tuning a weight | Standard IR ensemble | ✅ §1 |
| 1.5 | **Value-based linking** | Match question literals against sampled distinct column values | Text-to-SQL literature; addresses part of the 81.2% schema-error mass `[S2]` | ✅ §1 |
| 1.6 | **Foreign-key graph traversal** | Derive join paths from declared constraints | Standard | ✅ §5 |
| 1.7 | **Column-comment and documentation mining** | Use human-written descriptions as retrieval corpus | Standard | ✅ §1 |
| 1.8 | **Margin thresholding for ambiguity** | Halt when top-2 candidates are within a margin rather than taking argmax | The design's answer to `[S2]` | ✅ §1 |

## Cluster 2 — Data profiling and reconciliation (9)

| # | Technique | Mechanism | Evidence anchor | Used |
|---|---|---|---|---|
| 2.1 | **Cardinality profiling** | Count distinct values per column to infer key candidacy | Classical | ✅ §5 |
| 2.2 | **Uniqueness / key-candidate detection** | Test whether a column or tuple uniquely identifies rows | Classical | ✅ §5 |
| 2.3 | **Jaccard overlap on sampled domains** | Estimate joinability between two columns by value-set overlap | Standard data-integration | ✅ §5 |
| 2.4 | **Functional-dependency discovery** | Infer `A → B` relationships to detect grain | Classical DB theory | ✅ §5 |
| 2.5 | **Grain inference** | Determine the entity one row represents, before joining | Dimensional-modelling practice | ✅ §5, D02 |
| 2.6 | **Anti-join coverage measurement** | Count and sample unmatched keys on both sides | Standard | ✅ D02 check C3 |
| 2.7 | **Null-rate and completeness profiling** | Baseline null rates to detect transform damage | Standard | ✅ D02 check C4 |
| 2.8 | **Value normalisation for domain alignment** | Case-fold, trim, strip separators before comparison | Standard ETL | ✅ §5 |
| 2.9 | **Edit-distance / fuzzy domain matching** | Propose that `SW`, `SOUTHWEST`, `SW-1` are one domain | Standard record-linkage | ✅ §5 — **proposed, never auto-applied** |

## Cluster 3 — Query construction and repair (7)

| # | Technique | Mechanism | Evidence anchor | Used |
|---|---|---|---|---|
| 3.1 | **Parameterised statement construction** | Separate structure from literals; prevents injection and enables replay | Standard | ✅ §3, D04 |
| 3.2 | **Execution-feedback repair** | Feed DB error text back for bounded repair attempts | Arctic-Text2SQL-R1 makes small models competitive this way `[S14]` | ✅ §3 |
| 3.3 | **`EXPLAIN`-based cost estimation** | Estimate before executing; guard against runaway queries | Standard | ✅ §3, D05 |
| 3.4 | **Dialect adaptation** | Per-connector SQL generation | Standard | ✅ §3 |
| 3.5 | **Predicate pushdown** | Filter at source rather than after transfer | Standard query optimisation | ✅ §3 |
| 3.6 | **LIMIT-first exploratory execution** | Run bounded before running full | Standard analyst practice | ✅ §3 |
| 3.7 | **Constrained decoding to a column whitelist** | Generation scoped to columns a binding named | Removes hallucinated-column failures by construction | ✅ §3 |

## Cluster 4 — Verification and data quality (8)

| # | Technique | Mechanism | Evidence anchor | Used |
|---|---|---|---|---|
| 4.1 | **Row-count reconciliation** | Compare input and output counts across a join | Standard ETL testing | ✅ D02 C1 |
| 4.2 | **Grain assertion** | Assert the declared key is unique in the output | Dimensional-modelling practice | ✅ D02 C2 |
| 4.3 | **Boundary-total reconciliation** | Disaggregated sum must equal the undisaggregated one | Standard accounting control | ✅ D02 C5 |
| 4.4 | **Referential-integrity checking** | Verify FK values exist in the referenced table | Classical | ✅ D02 |
| 4.5 | **Range and domain constraint testing** | Assert values fall in plausible ranges | dbt tests, Great Expectations | ✅ D02 C6 |
| 4.6 | **Cardinality plausibility against source statistics** | Detect over-restrictive predicates | Standard | ✅ D02 C7 |
| 4.7 | **Reconciliation by independent path** | Compute the same quantity a second, different way | The core of P7 | ✅ D02 — **the technique the whole verify beat rests on** |
| 4.8 | **Golden-dataset regression testing** | Fixed inputs with known outputs, run continuously | Standard; becomes the harness | ✅ D08, feature #1 |

## Cluster 5 — Analytical methods (6)

| # | Technique | Mechanism | Evidence anchor | Used |
|---|---|---|---|---|
| 5.1 | **Period-over-period comparison** | Same measure across aligned windows | Standard analytics | ✅ Analytics agent |
| 5.2 | **Mix vs. rate decomposition** | Separate volume effects from unit-price effects | Standard financial analysis — produces the journey's *"the move is rate, not mix"* | ✅ Analytics agent |
| 5.3 | **Cohort construction** | Group entities by entry period and track forward | Standard | ✅ Analytics agent |
| 5.4 | **Contribution analysis** | Rank dimension members by contribution to a total change | The technique Sisu Data commercialised `[S56]` | ✅ Analytics agent |
| 5.5 | **Segmentation by dimensional split** | Break a measure across a dimension to localise a movement | Standard | ✅ Analytics agent |
| 5.6 | **Outlier detection by IQR / z-score** | Flag values outside expected dispersion | Classical statistics | ⬜ available, unused |

## Cluster 6 — Statistical and predictive baselines (6)

| # | Technique | Mechanism | Evidence anchor | Used |
|---|---|---|---|---|
| 6.1 | **Regularised linear / logistic regression** | Interpretable baseline with coefficient-level explanation | Classical | ✅ §7 |
| 6.2 | **Gradient-boosted decision trees** | Strong tabular baseline at low tuning cost | The standard tabular workhorse | ✅ §7 |
| 6.3 | **K-fold cross-validation with dispersion** | Estimate generalisation and report uncertainty | Classical | ✅ §7 |
| 6.4 | **Entity-grouped splitting with time embargo** | Prevent temporal and entity leakage | Standard defence in churn/forecasting | ✅ §7 — **Dr. Chen's specific check** |
| 6.5 | **Permutation feature importance** | Attribute predictive contribution without model-internal assumptions | Classical | ✅ §7 |
| 6.6 | **Seasonal decomposition (STL)** | Separate trend, seasonality and residual in a time series | Classical | ✅ §7 |

## Cluster 7 — Lineage, provenance and systems hygiene (5)

| # | Technique | Mechanism | Evidence anchor | Used |
|---|---|---|---|---|
| 7.1 | **Append-only event logging** | Immutable record of every handoff | Standard | ✅ D04 |
| 7.2 | **Content-addressed artifact storage** | Hash outputs so a re-run can diff rather than merely re-execute | Standard build-system practice | ✅ §6 |
| 7.3 | **Deterministic replay from recorded statement** | Re-issue the exact statement with recorded parameters | Standard | ✅ §6 |
| 7.4 | **Column-level lineage capture** | Record which source columns fed which output | Data-catalogue practice; Angela's provenance requirement | ✅ §6 |
| 7.5 | **Least-privilege role provisioning** | Read-only role scoped to what the analyst can already see | Standard security practice | ✅ D06 |

## Coverage summary

| Cluster | Count | Used | Orphans |
|---|---|---|---|
| 1 Schema understanding | 8 | 8 | 0 |
| 2 Profiling and reconciliation | 9 | 9 | 0 |
| 3 Query construction | 7 | 7 | 0 |
| 4 Verification | 8 | 8 | 0 |
| 5 Analytical methods | 6 | 5 | 1 |
| 6 Statistical baselines | 6 | 6 | 0 |
| 7 Lineage and hygiene | 5 | 5 | 0 |
| **Total** | **44** | **43** | **1** |

**The single orphan (5.6, outlier detection) is a real gap, not padding.** The Analytics agent has no anomaly-detection path, which means a question like *"is anything unusual in last month's data"* has no technique behind it. That is a defensible scope decision — it is a different product shape, closer to Tableau Pulse's inverted loop `[S48]` — and it is recorded here rather than hidden.

**What this wave establishes.** Forty-three of forty-four techniques in the system's foundation are established practice a data engineer would recognise, most of them decades old. **The novel content of this system is not its techniques — it is the composition** (D03) and the decision to spend a frontier model on planning while spending plain SQL on verification (D05). Any narrative artifact claiming algorithmic novelty at this layer is overclaiming.
