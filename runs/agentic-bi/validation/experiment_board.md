# Experiment board

**What this is** — The learning log for the top nine assumptions: hypothesis stated as a falsifiable number, experiment design, **pass/fail threshold declared before the result exists**, then result, learning and decision.
**Why it exists** — A threshold set after seeing data is not a threshold, it is a rationalisation. This board exists to fix the numbers in writing while they are still uncomfortable, so that in week ten nobody can quietly decide that 0.9 was "close enough" to the 0.5 they hoped for. Every Result row below says **`planned`**, and that is the honest state.
**How to read it** — The *Threshold* column is the commitment; the *Decision if fail* column is what makes it real. A skeptic should attack E1's threshold, which is the pack's most consequential number, and E5, where the failure decision is a design change rather than an abandonment.
**Depends on / feeds** — Consumes the ranked board in [riskiest_assumptions.md](riskiest_assumptions.md) and the nine falsifiable hypotheses in [strategy/business_model_canvas.md](../strategy/business_model_canvas.md). Feeds [stage_gate.md](stage_gate.md), [pivot_log.md](pivot_log.md) and the 295A project plan.

---

## E1 — Verification cost ratio *(R1 — kills the company)*

| | |
|---|---|
| **Hypothesis** | An analyst can reach a confident accept-or-reject on a correct multi-source answer they did not derive in **less than half** the time it takes them to derive the same answer from scratch. Verification cost ratio **< 0.5**. |
| **Design** | 5 enterprise analysts, within-subject, counterbalanced. Two matched questions of equal complexity, each spanning a warehouse table and an unmodelled CSV. Condition A: they receive an answer with hop-level lineage and must accept or reject it. Condition B: they derive from scratch. Stopwatch on both. Half do A first. Correct answers only — this measures cost, not detection. |
| **Threshold (declared in advance)** | **PASS: median ratio ≤ 0.5.** AMBER: 0.5 – 0.8. **FAIL: > 0.8.** |
| **Result** | `planned` |
| **Learning** | — |
| **Decision if PASS** | Proceed. Lineage is load-bearing and the whitepaper's mechanism D holds. |
| **Decision if AMBER** | Proceed, but re-scope: the differentiator becomes cross-source reach rather than verification cost, and [tech/whitepaper.md](../tech/whitepaper.md) §5 must be recomputed without mechanism D as a gate. |
| **Decision if FAIL** | **Stop and publish the negative result.** The differentiator is void, and a faster wrong-answer generator is not worth building. The field has no public measurement of verification cost either way, so a rigorous negative is a genuine contribution ([narrative/mission_vision.md](../narrative/mission_vision.md) §5). |

**Why 0.5 and not 0.8.** At 0.8 the analyst saves twenty minutes an hour and still has to think hard about every answer — that is a productivity tool, not a change in how work is done. The pack's arithmetic assumes 9 minutes against 90 (a ratio of 0.1) in the beachhead journey; 0.5 is already a large concession to reality.

## E2 — Silent-error detection *(R1's dangerous twin)*

| | |
|---|---|
| **Hypothesis** | With hop-level lineage, an analyst detects a **seeded wrong answer** at a materially higher rate than without it. Detection **≥ 70%** with the trace, and the trace at least doubles the no-trace rate. |
| **Design** | Same 5 analysts, separate session, later. 6 investigations, 3 containing a planted defect: one wrong join grain, one wrong region mapping, one wrong time-window filter. Analysts accept or reject each. Compare against a control group seeing answer-plus-SQL only (the incumbent experience). |
| **Threshold** | **PASS: ≥ 70% of seeded defects rejected, and ≥ 2× the control rate.** FAIL: < 50%, or no significant lift over control. |
| **Result** | `planned` |
| **Decision if FAIL** | The trace is *comfortable* rather than *effective* — a worse outcome than E1 failing, because it means the product would ship confident wrong answers wearing an audit trail. Redesign the verify surface before any further build. |

**Why this is separate from E1.** E1 measures the cost of checking a *correct* answer. E2 measures whether checking *works* on a wrong one. **A product could pass E1 and fail E2**, and that combination is the most dangerous outcome available — cheap verification that does not verify.

## E3 — Do real questions span sources *(R3)*

| | |
|---|---|
| **Hypothesis** | At least **25%** of an enterprise analyst's last 20 ad-hoc requests required data from more than one source, where "source" means separate systems of record, not two tables in one warehouse. |
| **Design** | 10 analysts. Ask them to open their actual request queue or ticket history and classify their **last 20 real requests**. Past behaviour, not estimation. Record the source count per request and which sources. |
| **Threshold** | **PASS: median ≥ 25% multi-source.** AMBER: 15–25%. **FAIL: < 15%.** |
| **Result** | `planned` |
| **Decision if FAIL** | The neutrality argument answering the gravity question is true and worthless ([strategy/positioning.md](../strategy/positioning.md) §4 residual); SAM halves to ≈$61M ([strategy/market_sizing.md](../strategy/market_sizing.md) §5.1); and the product should be rescoped toward single-warehouse depth — where it competes directly with Genie and loses on distribution. **This is a rescope trigger, not a stop.** |

## E4 — Can a buyer name a budget line *(R4)*

| | |
|---|---|
| **Hypothesis** | At least **3 of 5** analytics budget owners can name a specific existing line item this purchase would come from or displace. |
| **Design** | 5 conversations with VP/Director-level analytics budget owners. One question, asked without pitching: *"If your team adopted a tool like this, what line would it come out of, and what would it displace?"* Record the answer verbatim. Follow up: *"what did you buy most recently against that line?"* |
| **Threshold** | **PASS: ≥ 3 of 5 name a specific line.** FAIL: ≤ 1 of 5, or the modal answer is "we'd have to create one." |
| **Result** | `planned` |
| **Decision if FAIL** | The re-segmentation declaration in [strategy/market_type.md](../strategy/market_type.md) is wrong, and the honest conclusion is that this is a **feature, not a company** — which for a capstone is an acceptable finding and for a venture is decisive. |

**Bundled question (R11), same conversation:** *"How many analysts sit on your central team?"* If the modal answer is materially above 15, [strategy/channel_plan.md](../strategy/channel_plan.md) §3.1's verdict against outbound is wrong and the channel plan is rewritten.

## E5 — Analyst review load *(R5 / A12)*

| | |
|---|---|
| **Hypothesis** | In a deployment where stakeholders submit questions, an analyst's **review time stays below 10% of their working week** — under 4 hours — and does not trend upward over 8 weeks. |
| **Design** | Instrument review events from first deployment: time from opening a review to sign-off, review count per analyst per week, and queue depth. Split design-partner cohort from self-serve cohort so hand-holding does not contaminate the signal. |
| **Threshold** | **PASS: < 4 h/week, flat or falling over 8 weeks.** AMBER: 4–8 h/week. **FAIL: > 8 h/week, or rising.** |
| **Result** | `planned` |
| **Decision if FAIL** | A12 is firing: the champion has been given work while everyone else got leverage, and adoption stalls at the person it cannot stall at. **The fix is a design change, not an abandonment** — trust levels per question-shape, so repeat investigations auto-approve and only novel shapes require review. Rebuild the sign-off gate before scaling deployments. |

**Why this experiment exists at all.** No earlier phase would have found it. It came from running all five personas against one shared day and tallying who gained what ([product/journeys/day_in_life.md](../product/journeys/day_in_life.md) §3).

## E6 — Multi-hop execution accuracy *(R2 — the engineering risk)*

| | |
|---|---|
| **Hypothesis** | On a fixed 30–50 question set over a known two-source schema, the system achieves **≥ 50% execution accuracy** on multi-hop questions — materially above the ≈14.55–16% DABstep Hard baseline `[S4]`, on an easier and narrower task. |
| **Design** | Build the harness first (feature #1). Questions with ground-truth results, spanning Postgres plus CSV. Score strict execution accuracy. Report per-hop-count breakdown so compounding is visible. Publish the number and the question set. |
| **Threshold** | **PASS: ≥ 50%.** AMBER: 30–50%. **FAIL: < 30%.** |
| **Result** | `planned` |
| **Decision if FAIL** | The architecture's mitigations — typed plan DAG, static validation, short plans, per-hop verification — do not overcome the field's baseline. Narrow the spike to two-hop questions and report honestly. **Publishing a low number is still the pack's only public contribution**, since no commercial product publishes one at all. |

**Note on the threshold.** 50% is deliberately not compared to Spider 2.0-Snow's 96.70% `[S1]`, which is a different task on a single curated warehouse. The honest comparator is DABstep Hard, and this task is easier than DABstep by design.

## E7 — Verifier coverage *(R6)*

| | |
|---|---|
| **Hypothesis** | The six structural checks catch **≥ 60%** of seeded defects, including **≥ 30% of *semantically* plausible ones** (right cardinality, wrong meaning). |
| **Design** | Seeded-error set (feature #2), two classes: *countable* defects (fan-out, coverage loss, null spikes) and *plausible* defects (correct row counts, wrong grain semantics, wrong time basis). Measure catch rate per class. |
| **Threshold** | **PASS: ≥ 60% overall AND ≥ 30% on the plausible class.** FAIL: < 30% overall, or ≈0% on the plausible class. |
| **Result** | `planned` |
| **Decision if FAIL on the plausible class only** | Replace [tech/whitepaper.md](../tech/whitepaper.md) §2.3's judgement-based 4.0× with the measured figure and **state that the verifier catches mechanical, not semantic, failures.** That is a narrower and still useful claim — and it makes the shown-plan gate, not the verifier, the primary defence. |

**This is the experiment that resolves the pack's largest soft number.** The whitepaper currently discounts 6.7× to 4.0× on judgement alone and says so.

## E8 — Time to first successful investigation *(R8 — the channel gate)*

| | |
|---|---|
| **Hypothesis** | A competent analyst goes from `git clone` to **one successful investigation against their own data in under 30 minutes**, unaided. |
| **Design** | Publish repo with Docker Compose quickstart. Instrument: clone timestamp, first connector configured, first plan approved, first answer signed off. **Split self-serve from design-partner cohort.** |
| **Threshold** | **PASS: median < 30 min.** AMBER: 30–60 min. **FAIL: > 60 min, or < 50% reach a successful investigation at all.** |
| **Result** | `planned` |
| **Decision if FAIL** | The self-serve motion does not work and the real motion is design-partner-led — which rewrites [strategy/gtm.md](../strategy/gtm.md) and [strategy/channel_plan.md](../strategy/channel_plan.md), since **that was the only channel with viable economics at a $900 ACV.** |

## E9 — Semantic-layer lift *(R9)*

| | |
|---|---|
| **Hypothesis** | Attaching an existing dbt semantic layer improves execution accuracy on the fixed question set by **≥ 15 percentage points** over raw schema introspection. |
| **Design** | Same question set, same schema, two configurations. One with the dbt manifest available to the resolver, one without. |
| **Threshold** | **PASS: ≥ 15 pp lift.** AMBER: 5–15 pp. **FAIL: < 5 pp.** |
| **Result** | `planned` |
| **Decision if FAIL** | The semantic-layer story is weaker than [research/landscape.md](../research/landscape.md) §5.2 assumes. P6 moves from the roadmap's centre to its edge — **and the answer to the buyer's hardest objection ("I'm already buying a semantic layer") weakens**, because "we consume yours" delivers less than claimed. |

---

## Sequencing and total cost

| Wave | Experiments | Prerequisite | Founder-hours | Elapsed |
|---|---|---|---|---|
| **1 — no code** | E1, E3, E4 (+R11) | 5–10 analysts, 5 buyers | ~19 h | 3 weeks |
| **2 — no code** | E2 | Wave 1 recruits | ~6 h | 1 week |
| **3 — harness** | E6, E7 | Harness + seeded set (features #1, #2) | 295A eng. | 4 weeks |
| **4 — deployed** | E5, E8, E9 | Working system + first installs | 295B eng. | ongoing |

**Waves 1 and 2 cost about twenty-five founder-hours and can invalidate the venture.** Waves 3 and 4 are a semester of engineering. **Running them in that order is the single most consequential process decision in the pack**, and the ordering is not intuitive — it means the first month of a build project contains almost no building.

## What this board deliberately does not contain

- **No traction metrics.** There are no users, no revenue and no pipeline. A board reporting any would be inventing them.
- **No "validate demand" row.** That is not a hypothesis. E3 and E4 are what "validate demand" decomposes into once it is made falsifiable.
- **No A/B tests of copy, pricing or onboarding.** Those are optimisation experiments and they presuppose a validated premise this pack does not yet have.
