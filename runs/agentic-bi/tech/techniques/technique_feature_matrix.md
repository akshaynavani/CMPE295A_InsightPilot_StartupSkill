# Technique × feature matrix

**What this is** — Which techniques power which flagship features, with orphan techniques (catalogued but unused) and unsupported features (no technique behind them) called out explicitly.
**Why it exists** — A technique catalogue and a feature list can each look complete while failing to connect. This matrix is the join, and both kinds of mismatch it exposes are findings: an orphan technique is either padding or a missed opportunity, and an unsupported feature is a promise with no mechanism. The specific failure it prevents: a matrix where every technique powers every feature, which is the signature of a document written to look thorough.
**How to read it** — §3 and §4 are the output; the matrix itself is evidence. A skeptic should attack §4's three unsupported features, one of which is in the Now tier.
**Depends on / feeds** — Features from [product/features_flagship.md](../../product/features_flagship.md); techniques from [wave1.md](wave1.md), [wave2.md](wave2.md), [wave3.md](wave3.md). Feeds implementation sequencing and the `validation/` risk register.

---

## 1. The matrix

Techniques are referenced by wave and number: `W1 1.5` = wave 1, technique 1.5. **✅ = implemented dependency · 🔶 = candidate technique that would strengthen this feature.**

| # | Flagship feature | Techniques that power it |
|---|---|---|
| 1 | Investigation thread | W1 7.1 append-only logging · W1 2.x profiling cached per source |
| 2 | **Ambiguity interception** | W1 1.2 BM25 · 1.3 dense · 1.4 RRF · **1.5 value linking** · **1.8 margin thresholding** · W2 2.4.4 query expansion from bindings · 🔶 W2 2.4.2 cross-encoder rerank |
| 3 | Vocabulary binding | W1 1.7 comment mining · W3 3.2.9 read-back confirmation · W2 2.5.5 metric algebra |
| 4 | **Analysis plan shown before execution** | W2 2.1.1 grammar-constrained decoding · 2.1.2 type-directed synthesis · W3 3.1.2 plan-then-execute · **🔶 W3 3.2.4 pre-registration** (the rationale it currently lacks) |
| 5 | Plan-length discipline | W2 2.2.2 compounding-budget analysis |
| 6 | Plan caching + pinned bindings | W1 3.1 parameterised statements · W3 3.1.5 structured output · 🔶 W2 2.2.3 `pass^k` (to prove caching actually improves consistency) |
| 7 | Heterogeneous fetch | W1 3.4 dialect adaptation · 3.5 pushdown · W3 3.1.1 MCP |
| 8 | **Semantic layer consumption** | W2 2.5.5 metric algebra · W1 1.6 FK traversal |
| 9 | **Per-hop verification** | W1 **4.1** row counts · **4.2** grain assertion · 4.3 boundary totals · 4.4 referential integrity · 4.5 range constraints · 4.6 cardinality plausibility · **4.7 independent path** · W1 2.6 anti-join coverage · 2.7 null-rate · **🔶 W2 2.5.4 SCD detection** |
| 10 | Replanning on invalidation | W3 3.1.4 replanning · W2 2.2.4 bounded retry · 2.2.5 graceful degradation |
| 11 | **ML agent, time-boxed** | W1 6.1 regularised linear · 6.2 GBDT · 6.3 k-fold CV · **6.4 embargoed split** · 6.5 permutation importance · 6.6 STL · 🔶 W2 2.3.1 conformal prediction |
| 12 | Chart selection by data shape | W1 2.1 cardinality profiling |
| 13 | **Doubt surfacing** | W1 2.6 coverage · 2.7 null-rate · **🔶 W2 2.3.2 calibration measurement** — currently no way to know whether stated doubt is honest |
| 14 | Established facts, not a number | W1 5.1 period-over-period · **5.2 mix vs rate** · 5.4 contribution · 5.5 segmentation · **🔶 W2 2.3.4 multiple-comparisons correction** |
| 15 | **Hop-level lineage** | W1 7.1 append-only · **7.4 column-level lineage** · W3 **3.2.1 audit trail as deliverable** · 3.2.5 chain of custody |
| 16 | Single-hop re-run | W1 **7.2 content-addressed storage** · **7.3 deterministic replay** · 3.1 parameterised statements |
| 17 | Override, re-flow downstream | W1 2.5 grain inference (decides re-flow vs replan) · W3 3.2.6 blameless post-mortem (annotation types) |
| 18 | **Exportable investigation** | W3 **3.2.3 reproducible research** · 3.2.1 audit trail · W1 7.4 column-level lineage |
| 19 | Sign-off state | W3 **3.2.2 four-eyes principle** · W2 2.6.3 priority queue discipline |
| 20 | Context inheritance | W2 2.4.4 query expansion from bindings · W1 7.1 logging |

## 2. Cross-cutting techniques

Four techniques underpin the whole system rather than any single feature, and are listed separately so they do not read as orphans:

| Technique | Underpins |
|---|---|
| W1 4.8 golden-dataset regression testing | The evaluation harness (feature #1 in the backlog) — every accuracy claim in the pack |
| W3 3.3.4 fault injection / seeded errors | O4, the silent-error rate — the only instrument for P3 |
| W3 3.2.8 defence in depth | The four-gate structure of D10 |
| W1 7.5 least-privilege provisioning | The D06 trust boundary — Tom's approval |

## 3. Orphan techniques — catalogued, unused

Out of 113 techniques across three waves, **five are genuinely orphaned.** Each is a finding rather than padding.

| Technique | Why unused | Verdict |
|---|---|---|
| **W1 5.6 outlier detection (IQR / z-score)** | No anomaly-detection path exists; *"is anything unusual in last month's data"* has no technique behind it | **Real gap, defensible scope decision.** That question shape is closer to Tableau Pulse's inverted loop `[S48]` — a different product. Recorded, not fixed |
| **W2 2.3.5 power analysis** | Nothing checks whether a segment is large enough to support the question asked | **Real gap.** The system will happily compare two segments of eleven rows. Cheap to add, and it would strengthen doubt surfacing (#13) |
| **W2 2.5.2 conjunctive-query containment** | The formal basis for "verify by independent path" is used informally, not formally | **Acceptable.** The informal version (run a different cheap query) delivers most of the value at a fraction of the implementation cost |
| **W2 2.5.6 materialised-view matching** | An optimisation for query volume this system does not have | **Correctly declined** at this scale |
| **W3 3.4.2 learning-to-rank from override signal** | Requires deployment volume a single tenant may never reach (D09) | **Correctly deferred.** It is also the mechanism that would make the A3 moat real, which is why D09 names single-tenancy's cost to the moat |

**Two of the five are real gaps** (5.6, 2.3.5) and both concern the system's inability to say *"I cannot answer that reliably from this data."* That is a coherent weakness worth naming as one.

## 4. Unsupported features — promised with no technique behind them

The more serious direction of mismatch. **Three features have thin or absent technique support.**

| Feature | The gap | Severity |
|---|---|---|
| **#13 Doubt surfacing** | The system reports *which hops it is least sure of*, but there is **no technique that establishes whether that self-assessment is honest.** Calibration measurement (W2 2.3.2) is the technique, and it is a candidate rather than a dependency. Without it, doubt surfacing is an assertion — and P3 says a plausible wrong answer may surface no doubt at all | **HIGH.** This is flagged as the weak link in [features_flagship.md](../../product/features_flagship.md) #13 and the matrix confirms it mechanically |
| **#14 Established facts (diagnostic questions)** | Contribution analysis (W1 5.4) scans many dimension members for "drivers." **Without multiple-comparisons correction (W2 2.3.4) it will confidently name noise**, and no structural check in D02 catches a statistically wrong answer | **HIGH.** Both the highest-demand question type and the least defended — see [decision_tree.md](decision_tree.md) §3 |
| **#12 Chart selection by data shape** | Backed by one technique (cardinality profiling). The rest of "justified by data shape" is unspecified | **LOW.** Charts are first on the pre-decided cut list, so thin support here is consistent with priority rather than an oversight |

## 5. What the matrix says

**1. The two highest-severity unsupported features share a shape.** #13 and #14 both concern **statistical honesty rather than mechanical correctness.** The verification layer (D02) is well covered — nine techniques on feature #9 — because mechanical failures are countable. Statistical failures are not, and the matrix shows the defence thinning exactly where P3 says the danger is.

**2. The lineage cluster is the best-supported, and it is supported mostly by imports.** Features #15, #16 and #18 draw on audit trails, chain of custody and reproducible research (W3 3.2.1, 3.2.3, 3.2.5) — disciplines that solved the trust-what-you-did-not-derive problem long ago. **The differentiator's technique support is old and well-tested**, which is a stronger position than novelty.

**3. Feature #4 has a rationale it is not using.** The plan-approval gate is currently justified as convenience — catch errors before they cost queries. Pre-registration (W3 3.2.4) is the same ritual with a stronger argument: **state the analysis before seeing the result so the analysis cannot be fitted to the answer.** Adopting the framing costs nothing and suggests a genuinely new measurement — plan-versus-outcome divergence.

**4. No technique powers more than four features, and no feature draws on more than nine.** The matrix is sparse, which is what a real one looks like.

## Recommended next 3

1. **Add multiple-comparisons correction (W2 2.3.4) before the Analytics agent ships diagnostic questions.** It is the highest-severity gap, it sits in the most-wanted question type, and no other layer of the system catches it.
2. **Add calibration measurement (W2 2.3.2) to the evaluation harness.** Doubt surfacing is currently unfalsifiable, and the harness already has the ground truth needed to check whether stated doubt predicts actual error.
3. **Adopt the pre-registration framing (W3 3.2.4) for feature #4 and record plan-versus-outcome divergence.** Free to adopt, gives the plan gate a defensible rationale, and produces a quality signal the pack does not currently have.
