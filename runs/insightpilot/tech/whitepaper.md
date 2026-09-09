# Whitepaper — the mechanism arithmetic

**Version 0.1 · 2026-09-08**

**What this is** — The technical case, structured as arithmetic: the frictions in today's per-question sequence with magnitudes, the mechanism that removes each one, the multiplier each mechanism produces with a confidence band, and what those multipliers come to when a skeptic multiplies them back together.
**Why it exists** — This is the document a technical reviewer opens to decide whether the project is a wrapper. It exists in a specific tension the reader should know about up front: the generator that produces this artifact is designed to build a 10x argument, and [ASSUMPTIONS.md](../ASSUMPTIONS.md) **A2 forbids manufacturing one**. The resolution is to do the arithmetic honestly and report what it comes to. **It does not come to 10x**, and §5 says so in the same words A2 does.
**How to read it** — §2 is the arithmetic; §5 is the total and the concession. A skeptic should attack §2.3 (the reconciliation multiplier, the largest single claim) and §4, which names the conditions under which the gain goes to zero or below.
**Depends on / feeds** — Frictions and magnitudes from [research/survey.md](../research/survey.md) §6 and [product/journeys/beachhead.md](../product/journeys/beachhead.md); mechanisms from [product/PRD.md](../product/PRD.md) §3; capability evidence from [research/capability_table.md](../research/capability_table.md). Feeds [deep_dives.md](deep_dives.md), the [architecture set](architecture/00_INDEX.md), and `narrative/`.

---

## Executive summary

An enterprise analyst's ad-hoc question costs a fixed sequence — locate source, inspect schema, author and debug query, reconcile across sources, chart, interpret, verify — that does not amortise across questions. Decomposed against a representative multi-source question, that sequence is **≈90 minutes of work time** sitting inside **one to four weeks of queue latency** `[S15]`.

Four mechanisms attack four of the six frictions. Multiplied conservatively they produce **≈2.9× on work time for a multi-source question against an unmodelled source**, with a plausible band of 1.8×–4.2×. Queue latency responds superlinearly to service-time reduction — the arithmetic is in §3 — but most of that gain is expected to be consumed by induced demand, and §3.2 argues that is the correct outcome rather than a loss.

Two results matter more than the multiplier. First, **for a single-source familiar question the multiplier is ≈1.0 and may be below it** — the analyst should keep writing SQL, and the product should not fight that. Second, the modelling step is not sped up; it goes from *not attempted* to *attempted in minutes*, which is a category change and not a multiplier at all.

**This is not a 10x argument, and no arithmetic in this document is arranged to become one.** A2 recorded that decision before this file existed; §5 confirms the arithmetic agrees with it.

## §1 The current inefficiency

Six frictions. Magnitudes are from the beachhead journey's decomposition of a representative question — an unmodelled carrier CSV joined to warehouse shipments — cross-checked against the sourced turnaround figures. **The 90-minute figure is the analyst's own estimate of her own task** and is tagged accordingly.

| # | Friction | What it costs | Magnitude | Source |
|---|---|---|---|---|
| **F1** | **Source location and schema inspection** | Finding which tables hold the answer; reading a schema nobody documented | ~10 min | *(assumption: journey decomposition)* |
| **F2** | **Query authoring and debugging** | Writing SQL, running it, fixing it | ~25 min | *(assumption: journey decomposition)* |
| **F3** | **Cross-source reconciliation** | Making two sources agree — key mapping, grain, coverage. Region codes in a CSV against a warehouse dimension | **~20 min** | *(assumption: journey decomposition; the single largest work-time component and the one the incumbents will not attempt)* |
| **F4** | **Verification and defensibility** | Checking the work well enough to sign your name to it | ~15 min | *(assumption; cheap when self-derived — the analyst *is* the verification step)* |
| **F5** | **Queue latency** | Dead time between question asked and answer delivered | **1–4 weeks** enterprise; 5–10 business days under 500 employees | IBM, attributing Sigma and Forrester `[S15]` |
| **F6** | **The modelling step** | Not slow — **not attempted.** The predictive question is a different job | ∞ (not done) | BRIEF.md; `[S9]` for what is technically possible |

**Work time per question ≈ 80–90 minutes** (F1–F4). **Wall-clock ≈ 1–4 weeks** (F5). These are different quantities and conflating them is the standard way this argument gets inflated.

### 1.1 How the frictions compound

They are not independent, and the compounding runs in the direction that makes them worse:

**F3 multiplies F2.** Every reconciliation problem discovered mid-query sends the analyst back to authoring. A region-code mismatch is not 20 minutes added to 25 — it is 20 minutes plus a partial rewrite.

**F4 gates F5.** An answer the analyst will not sign is not delivered, so verification failures return the question to the queue. This is why 76% of businesses report having decided without data at all `[S15]` — the queue is long enough that the rational move is to skip it.

**F6 is invisible in the arithmetic and largest in effect.** A question that is never attempted has no cost line. The predictive half of the analyst's request stream simply does not get answered, which understates F1–F5 as a description of the problem.

## §2 Core mechanisms

Each mechanism attacks a named friction, cites its evidence, and carries a multiplier with a confidence band. Bands are wide because the underlying magnitudes are journey estimates, not measurements.

### 2.1 Mechanism A — planning over heterogeneous sources without a pre-authored artifact

**Attacks F1 and part of F2.**

**Mechanism.** The Orchestrator resolves the question's terms against live schema and any available semantic layer, then emits an ordered plan naming sources and operations. No pre-authored semantic model is required, which is the structural difference from every incumbent — Genie caps at 30 tables per agent `[S32]`, Cortex Analyst at a ~1 MB hand-authored YAML `[S36]`, Copilot cannot compute a metric that is not already a measure `[S42]`.

**Evidence.** Text-to-SQL on realistic schemas is strong enough to carry this: top Spider 2.0-Snow systems reach 96.70% `[S1]`. The honest counterweight is the same benchmark's spread — 65.60% on the DBT setting, a 31-point drop when semantic indirection and real project structure appear `[S1]` — and 30–36% on ~1,000-column, 54-table schemas `[S2]`.

**Multiplier on F1+F2 (35 min).** Schema inspection largely disappears; query authoring becomes plan review plus targeted correction. **35 min → ~12 min. 2.9× (band 2.0×–4.0×).**

**Why not higher.** Plan review is not free, and the 15-second plan-read budget in [product/ux_spec.md](../product/ux_spec.md) §4 is itself an assumption. The ambiguity interception step (feature #11) *adds* time on first encounter with a source and repays it later.

### 2.2 Mechanism B — semantic grounding by interception and persistence

**Attacks the error rate underneath F2 and F3, and shortens both over time.**

**Mechanism.** Terms are resolved before planning; anything resolving to more than one column, grain or time basis halts and asks rather than guessing. Confirmed resolutions persist to an organisation-scoped binding store and are inherited by every later question.

**Evidence.** This is the highest-leverage intervention available: **schema-level errors — wrong column selection and semantic misinterpretation — are 81.2% of 4,602 analysed incorrect queries** `[S2]`. Attacking the dominant error class beats attacking any other.

**Multiplier.** Two distinct effects, and only the first is claimed:

- *First encounter with a source:* **~0.85× — this is slower**, because clarification costs time before any value is returned.
- *Subsequent questions against that source:* bindings are inherited, so F1 and part of F3 are already paid. **~1.4× (band 1.1×–1.9×)**, growing with binding coverage.

**Claimed multiplier: 1.0×.** The first-encounter penalty and the steady-state gain are reported separately and **not multiplied into the total**, because the steady-state figure depends on the flywheel, which ASSUMPTIONS A3 declines to claim as evidenced.

### 2.3 Mechanism C — cross-source reconciliation with per-hop verification

**Attacks F3, the largest work-time friction.**

**Mechanism.** Every hop is checked by a cheaper, structurally different query — row-count reconciliation, grain preservation, null rate, coverage, key-collision detection. A failed check surfaces immediately and triggers replanning rather than propagating.

**Evidence.** Verification by decomposition is independently corroborated by the strongest incumbent: Databricks' *Inspect* reviews its own generated SQL, authors smaller statements to verify specific aspects, and regenerates `[S32]`. Necessity is established by the compounding arithmetic — error propagation is the primary agent reliability bottleneck `[S10]`, and 95% per hop over six hops is ≈74% `[S13]`.

**Multiplier on F3 (20 min).** In the journey, the 8% region-code coverage failure surfaced in ~40 seconds against the ~20 minutes it took the analyst to find manually. **20 min → ~3 min. 6.7× — reduced to a claimed 4.0× (band 2.0×–7.0×).**

**Why the claim is discounted below the observed figure.** The journey's failure was *countable* — a row-count mismatch, which is exactly what a cheap structural check finds. P3 says the dangerous failures are the plausible ones `[S2]`: a clean-looking join at the wrong grain produces no count anomaly. **This mechanism's real coverage of the failure space is unmeasured**, which is why [product/features_prioritized.md](../product/features_prioritized.md) puts a seeded-error test set at #2. The discount from 6.7× to 4.0× is a judgement, not a measurement, and it is the single largest soft number in this document.

### 2.4 Mechanism D — lineage that makes verification cheaper than re-derivation

**Attacks F4, and is the differentiator.**

**Mechanism.** Every handoff emits sources touched, query issued, transform applied, method chosen, and row counts in and out — each hop separately inspectable and re-runnable in isolation, and the whole investigation exportable as one self-contained artifact.

**Evidence.** Demand is measured: 71% of practitioners name incorrect or hallucinated output reaching stakeholders as a top concern `[S16]`, and 24.9% name accuracy and hallucination as their top reservation about GenAI in analytics `[S17]`.

**Multiplier on F4 — and this is where the argument is most exposed.** For a *self-derived* answer, verification is nearly free: the analyst already knows what they did. For an answer produced by a system, verification is new work that did not previously exist. **The comparison is therefore not "15 minutes → less" but "0 minutes of checking someone else's work → 9 minutes of it."**

The mechanism does not reduce F4. **It creates a smaller F4 than the alternative it replaces**, which is re-derivation. The honest framing:

```
Trust the answer blind                    → unacceptable (P3: failure is plausible)
Re-derive to check                        → 80–90 min, i.e. no gain at all
Inspect hop-level lineage                 → ~9 min      ← the claim
```

**Multiplier: 1.0× on F4 as a line item, and it is load-bearing for the whole model** — because without it the rest of the arithmetic is void. If verification costs re-derivation, mechanisms A and C deliver an answer the analyst cannot use, and the total multiplier is 1.0× regardless of how fast the answer arrived.

**This is the pack's untested claim**, denied by the beachhead's own stated objection ([strategy/personas.md](../strategy/personas.md) §2) and unmeasured anywhere in the literature ([research/survey.md](../research/survey.md) §8.1).

### 2.5 Mechanism E — the modelling step, time-boxed

**Attacks F6.**

**Mechanism.** A time-boxed ML agent produces a baseline model, named features, an honest uncertainty statement, and an explicit list of what it did not have time to try.

**Evidence and its limit.** MLE-bench-class agents reach a 36.4% medal rate — under a **12-hour budget** `[S9]`. P9 forbids promising that behaviour inside a conversational loop.

**Multiplier: undefined, and deliberately so.** F6 is currently *not attempted*, so there is no baseline to divide by. Reporting this as an infinite multiplier would be the exact dishonesty A2 exists to prevent. **It is a category change — a question that was not asked becomes a question that gets a screening answer** — and it is worth stating in those words and not in arithmetic.

## §3 Queue latency — the superlinear term, and why most of it is not claimed

### 3.1 The arithmetic

Work time and wall-clock are different quantities, and F5 is where the large numbers live. Analyst queues behave like a single-server queue at high utilisation, where waiting time is acutely sensitive to service time.

For utilisation ρ = λ/μ, expected wait scales as ρ/(1−ρ). An analyst at 85% utilisation whose per-question service time falls by 2.9× sees utilisation drop toward 0.29:

```
ρ = 0.85  →  ρ/(1−ρ) = 5.67
ρ = 0.29  →  ρ/(1−ρ) = 0.41
                        ─────
                        ≈13.8× reduction in expected wait
```

*(assumption: single-server M/M/1 approximation, steady arrival rate, no priority classes. Real analyst queues have none of these properties — the model is directional only.)*

That would take a one-to-four-week turnaround `[S15]` toward same-day, which matches what the day-in-life journey shows.

### 3.2 Why this multiplier is not claimed

**Because demand will expand to consume it, and that is the desired outcome.**

76% of businesses report having made decisions without consulting data because access was too difficult `[S15]`, and 60–73% of enterprise data is never used for analytics `[S15]`. That is **suppressed demand**, and it surfaces the moment the queue shortens. λ rises with μ, ρ does not fall to 0.29, and the wait does not fall 13.8×.

The honest statement:

> **Latency improves substantially and unpredictably. The right way to describe the effect is not a shorter wait but more questions answered per analyst per week** — and the pack should measure throughput, not celebrate a queueing multiplier that induced demand will eat.

Claiming §3.1's 13.8× would be the most impressive and least defensible number in this document. It is stated and then withdrawn, deliberately, so that no downstream artifact can cite it as an approved figure.

## §4 Full-spectrum applicability, and where the gain goes to zero

### 4.1 Where it holds

| Edge | Does the gain hold? | Mechanism |
|---|---|---|
| **Beachhead (Priya)** | **Yes — 2.9×** on multi-source questions against unmodelled sources | A + C, gated by D |
| **High edge (Dr. Chen)** | **Yes, and larger — ~6×** (2 hours → 19 minutes) | D alone. He uses no other mechanism; he reads and challenges ([product/journeys/edge_high.md](../product/journeys/edge_high.md) §6) |
| **Low edge (Marcus)** | **Category change, not a multiplier.** A guess or a three-day wait becomes an attributed answer in 90 seconds plus a 6-minute review | A + D, gated by sign-off |
| **Blocker (Tom)** | ~15× on audit review (1.5 days → 8 minutes) | Audit log; an incidental gain, not a designed one |

**The high edge shows the largest multiplier in this document, from a single mechanism.** That is worth noticing: the strongest arithmetic in the whitepaper belongs to the persona who uses only the lineage surface — which is the clearest available support for D being the load-bearing mechanism rather than A or C.

### 4.2 Where the gain shrinks to nothing or goes negative

Four conditions, stated as concretely as the gains.

1. **Single-source, familiar, well-modelled question → ≈1.0×, plausibly below.** The analyst already knows the schema and the query shape; plan review plus verification costs more than writing it. **The product should not fight this** — the day-in-life journey shows Priya correctly bypassing the system for exactly such a question, and PRD non-goal 9 concedes the case explicitly. On Genie's home turf, Genie wins.
2. **First encounter with any source → ~0.85×.** Mechanism B costs before it repays (§2.2).
3. **Bad data → the gain is negative.** 77% of organisations report data-quality issues and 91% say they affect performance `[S15]`. A traceable wrong answer delivered fast is worse than a slow right one, and lineage makes it *legible*, not correct. PRD non-goal 3.
4. **Verification cost ≥ re-derivation cost → the whole model collapses to 1.0×.** Mechanism D is a gate on A and C, not an addend (§2.4).

## §5 The total, and the concession

Multiplying the claimed mechanisms for the case they are designed for — a multi-source question touching an unmodelled source:

| Component | Before | After | Multiplier |
|---|---|---|---|
| F1+F2 source location, schema, query authoring (A) | 35 min | 12 min | 2.9× |
| F3 cross-source reconciliation (C) | 20 min | 5 min | 4.0× |
| F4 verification (D) | 15 min self-check | 9 min lineage inspection | 1.0× *(gate, not gain)* |
| F5 chart and interpret | 20 min | 5 min | 4.0× |
| **Total work time** | **90 min** | **31 min** | **≈2.9×** |

**Conservative corner** (A at 2.0×, C at 2.0×, verification at 15 min): 90 → 50 min, **1.8×**.
**Optimistic corner** (A at 4.0×, C at 7.0×, verification at 6 min): 90 → 21 min, **4.2×**.

### The concession

**≈2.9×, band 1.8×–4.2×, on one question type. That is not 10×, and no rearrangement of these mechanisms produces 10×.**

This is not a disappointing result that has to be explained away — it is the result [ASSUMPTIONS.md](../ASSUMPTIONS.md) A2 predicted before any of this arithmetic existed. A2 records the founder's reasoning: the beachhead can already query, chart and analyse, so **automating those three stages is convenience rather than leverage**. The arithmetic above confirms it precisely — F1, F2 and the charting step yield ordinary 3–4× improvements because the analyst was already competent at them.

The two places the number is genuinely large are the two the founder identified as the real 10x candidates and knowingly declined to lead with:

- **F3 cross-source reconciliation at 4.0×** (observed 6.7×) — the one thing no incumbent will attempt.
- **F6 the modelling step** — a category change from *not attempted*, which has no multiplier because it has no baseline.

And the largest single figure in the document — Dr. Chen's ~6× — comes from mechanism D operating alone, on a persona who is not the beachhead.

**What this whitepaper claims, in one sentence:** a defensible ≈3× on the work time of multi-source questions, a category change on questions that currently go unasked, a substantial but unquantifiable latency improvement that induced demand will partly consume, and **no claim at all on the single-source familiar question that makes up much of an analyst's day.**

**What it does not claim:** 10×; superiority over any incumbent on a measured benchmark (none publishes one — [research/sources.md](../research/sources.md), *Named gaps* 2); or that mechanism D works, which is untested and gates everything else.

## Recommended next 3

1. **Measure §2.4's ratio before anything else is built.** It is the gate on the entire model — if verification costs re-derivation, the total is 1.0× regardless of A and C. One afternoon, five analysts, a timed task.
2. **Replace §2.3's discounted 4.0× with a measured figure from the seeded-error set.** The 6.7×→4.0× discount is the largest soft number here, and the seeded-error test set (feature #2) converts it into evidence.
3. **Forbid §3.1's 13.8× in every downstream artifact.** It is the most citable number in this file and the least defensible; it is stated and withdrawn here specifically so `narrative/` cannot rediscover it as a headline.
