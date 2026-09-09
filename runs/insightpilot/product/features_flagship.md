# Flagship features — the 20 highest-leverage

**What this is** — The twenty features that carry the product, each as: name → mechanism → principle(s) it obeys → the visible product moment the user literally sees. Closes with the argument for why the power is the closed loop rather than any one of them.
**Why it exists** — A feature list without a mechanism is a wish list, and a feature list without the *visible moment* is a spec no designer can build from. The specific failure this prevents: shipping "lineage" as a collapsible JSON blob nobody opens, which would satisfy the word and none of the value. Every row below has to survive the question *what does the analyst actually see?*
**How to read it** — The **P** column is the credibility check: a feature mapping to no principle would be cut. A skeptic should attack §3, the integration argument, and features 13 and 17, which are the two whose value is asserted rather than demonstrated.
**Depends on / feeds** — Principles from [PRD.md](PRD.md) §3; ranked value mappings from [strategy/value_prop_canvas.md](../strategy/value_prop_canvas.md) §5. Feeds [features_prioritized.md](features_prioritized.md), [ux_spec.md](ux_spec.md) and the `tech/` architecture set.

---

## 1. The twenty

### ASK

**1. Investigation thread**
*Mechanism.* A durable unit holding the original question, every follow-up, the resolved vocabulary bindings, and the facts established so far. Not a chat log — a chat log has no state worth reusing.
*Principle.* P5, P1.
*Visible moment.* Priya's sidebar shows *"Southwest cost per shipment — 4 questions, 2 verified facts"* — she reopens it Monday and the system still knows what "cost per shipment" resolved to.

**2. Ambiguity interception**
*Mechanism.* Before planning, every term in the question is resolved against schema and any semantic layer. A term resolving to more than one column, grain or time basis halts and asks. **The system never guesses silently on a term it cannot resolve uniquely.**
*Principle.* **P1** (schema errors are 81.2% of failures `[S2]`), P3.
*Visible moment.* *"'Cost' matches two things: `carrier_invoice.total_usd` (billed) and `shipment.est_cost` (estimated). Which?"* — with row counts and date ranges for each, so the choice is informed rather than a coin flip.

**3. Vocabulary binding, shown and correctable**
*Mechanism.* Resolved terms render as editable chips above the plan. Corrections persist to the organisation's binding store (PRD §6).
*Principle.* **P1**, P8.
*Visible moment.* A row of chips: `cost per shipment = SUM(carrier_invoice.total_usd) / COUNT(DISTINCT shipment.id)` — Priya clicks it, fixes the denominator, and it stays fixed for everyone.

### PLAN

**4. The analysis plan, shown before execution**
*Mechanism.* The Orchestrator emits an ordered, human-readable list of agent tasks with named sources, and waits for approval on first run against a source.
*Principle.* P2, P3, **P5**.
*Visible moment.* Six numbered steps, each naming its agent and its source. Priya reads it in fifteen seconds and deletes step 4 before anything runs — **catching the error before it costs a query, not after it reaches a slide.**

**5. Plan-length discipline**
*Mechanism.* The Orchestrator reports hop count and the compounding implication, and flags plans beyond a configured ceiling for narrowing.
*Principle.* **P2** — 95% per hop is ≈74% over six `[S13]`.
*Visible moment.* *"7 hops. Long plans compound error — consider splitting this into two questions."* The system arguing against its own ambition is the point.

**6. Plan caching and pinned bindings**
*Mechanism.* An approved plan and its resolved bindings are cached against the question's semantic signature; re-asking reuses rather than re-derives.
*Principle.* **P4** — `pass^8` below 25% `[S5]` means re-derivation is a source of drift.
*Visible moment.* *"Same plan as Tuesday. Re-running against current data."* Two analysts asking the same question get the same answer, which is not otherwise guaranteed.

### EXECUTE

**7. Heterogeneous fetch — CSV/Excel, REST JSON, Postgres**
*Mechanism.* Connectors behind one interface; MCP where a server exists `[S62]`.
*Principle.* P8, **P6**.
*Visible moment.* One plan whose step 1 reads the warehouse and step 2 reads the carrier CSV that has never been modelled — the thing no incumbent will attempt `[S32][S36]`.

**8. Semantic layer consumption**
*Mechanism.* Where a dbt or Cube layer exists, its metric definitions and join paths are read and take precedence over inferred ones `[S66]`.
*Principle.* **P6**, P1.
*Visible moment.* *"Using your dbt definition of `active_customer` (models/marts/customers.yml, updated 12 days ago)."* This is also the demo that answers Angela's deal-ending objection ([strategy/personas.md](../strategy/personas.md) §5).

**9. Per-hop verification by decomposition**
*Mechanism.* After each hop, a cheaper and **structurally different** query checks the result — row-count reconciliation, grain check, null-rate, boundary totals. Not the model asserting confidence in itself.
*Principle.* **P7** (Genie's *Inspect* independently `[S32]`), P2, P3.
*Visible moment.* A green or amber tick beside each step: *"Step 3 ✓ join preserved row count (14,201 → 14,201)"* and *"Step 4 ⚠ 8% of shipments had no matching invoice."*

**10. Replanning on invalidation**
*Mechanism.* A failed verification or an empty/degenerate result invalidates the plan; the Orchestrator revises the remaining steps rather than continuing into nonsense.
*Principle.* **P2**.
*Visible moment.* *"Step 4 found 8% unmatched. Revised plan: split by matched/unmatched before comparing regions."* — with the change diffed against the original.

**11. ML agent, time-boxed in minutes**
*Mechanism.* Given a predictive question, it produces a baseline model, named features, an honest uncertainty statement, and **an explicit list of what it did not have time to try** — inside a minutes-long budget.
*Principle.* **P9** — MLE-bench's 36.4% medal rate runs on a 12-hour budget `[S9]`.
*Visible moment.* *"Baseline gradient boosting, 5-fold CV, MAE 4.2 (±0.6). Not attempted in budget: feature interactions, hyperparameter search, alternative targets."* The renunciation is the credibility.

**12. Chart selection justified by data shape**
*Mechanism.* The Visualization agent selects from shape — cardinality, time basis, distribution — and states why.
*Principle.* P3.
*Visible moment.* *"Small multiples by carrier rather than a stacked bar — 9 carriers, stacking would hide the two that moved."*

### ANSWER

**13. Doubt surfacing**
*Mechanism.* The answer names the hops it is least sure of, with the reason — an unresolved binding, a failed verification, a low-coverage join — and never presents a confidence percentage as accuracy.
*Principle.* **P3**, P5.
*Visible moment.* *"Least certain: the region mapping in step 2. The CSV uses 4 region codes; the warehouse uses 6. I mapped SW→Southwest and dropped 2 rows."*
*Weakest link, flagged honestly.* **What the system is uncertain about is not the same as what it is wrong about.** P3 says failure looks plausible — so a plausible wrong answer may surface no doubt at all. This feature narrows the failure surface; it does not close it, and O4 (silent-error rate) is the metric that measures the gap.

**14. Established facts, not just a number**
*Mechanism.* The answer carries the intermediate facts it depended on, each independently checkable.
*Principle.* P3, P5.
*Visible moment.* *"Cost per shipment rose 11%. Volume fell 3%. Rate per shipment rose 14%. The move is rate, not mix."* — three checkable claims instead of one unfalsifiable summary.

### VERIFY

**15. Hop-level lineage**
*Mechanism.* Every handoff emits sources touched, query issued, transform applied, method chosen, and row counts in and out — rendered as an inspectable step, not a JSON dump.
*Principle.* **P5** — the differentiator.
*Visible moment.* Priya clicks step 3, sees the exact SQL and the row counts, thinks *"that join grain is wrong,"* and has spent forty seconds rather than ninety minutes.

**16. Single-hop re-run**
*Mechanism.* Any hop re-executes in isolation against current data, with its output diffed against the stored one.
*Principle.* **P4**, P7.
*Visible moment.* *"Re-ran step 3. Same result, 14,201 rows."* — this is how Dr. Chen's two-hour re-derivation becomes a five-minute spot-check.

**17. Override a hop, re-flow downstream**
*Mechanism.* The analyst edits a hop's query, join or method; downstream hops re-execute against the corrected output; the override is recorded to the organisation's binding store.
*Principle.* P2, P5, and it feeds the flywheel (PRD §6).
*Visible moment.* Priya rewrites the join in step 3; steps 4–6 re-run; the answer updates; the correction persists so nobody hits it again.
*Weakest link, flagged honestly.* Re-flowing an override cleanly is **hard** — a changed grain can invalidate every downstream assumption, and the honest fallback is to invalidate and replan rather than pretend the plan survives. Specified as a real requirement precisely because it is the one most likely to be quietly downgraded to "edit and re-run everything."

**18. Exportable self-contained investigation**
*Mechanism.* An investigation exports as a single readable artifact — question, plan, every hop with its query and counts, the answer, the sign-off state — openable without the product running.
*Principle.* **P5**.
*Visible moment.* Priya attaches one file to the ops director's thread. He can read the answer; Dr. Chen can read the joins; Angela can answer *"where did this number come from"* six months later.
*Why this is disproportionately important.* It is simultaneously the differentiator's proof, the GTM compounding loop's edge ([strategy/gtm.md](../strategy/gtm.md) §3), Angela's provenance requirement, and O2's measurement instrument. **One artifact, four jobs** — the highest leverage-to-effort ratio in this list.

**19. Sign-off state**
*Mechanism.* An investigation is explicitly marked reviewed, by whom, when — and unreviewed answers are visibly marked and cannot be exported without acknowledgement.
*Principle.* P5, P3; enforces PRD non-goal 1.
*Visible moment.* Marcus opens a shared answer and sees *"Not yet reviewed by an analyst"* in amber. He asks Priya before it reaches his slide, which is the entire mechanism by which the low edge is served without being sold to.

### FOLLOW UP

**20. Context inheritance**
*Mechanism.* The next question inherits resolved bindings, source scope and established facts, so a follow-up is a short plan rather than a fresh investigation.
*Principle.* P1, P4, P2 (fewer hops).
*Visible moment.* *"And by carrier?"* → three steps instead of six, because the region mapping and the cost definition are already settled.

## 2. Principle coverage check

Every principle carries at least one flagship feature, and the two most load-bearing carry the most.

| Principle | Flagship features |
|---|---|
| P1 schema grounding | 1, 2, 3, 8, 20 |
| P2 error compounding | 4, 5, 10, 17, 20 |
| P3 plausible failure | 2, 4, 9, 12, 13, 14, 19 |
| P4 consistency | 6, 16, 20 |
| **P5 verification cost** | 1, 4, 13, 14, **15, 16, 17, 18, 19** |
| **P6 pre-encoding narrows scope** | 7, **8** |
| P7 verify by decomposition | 9, 16 |
| P8 access standardised, semantics not | 3, 7 |
| P9 modelling not at conversational latency | 11 |
| P10 multi-hop is weak | *(no feature — see below)* |

**P10 has no flagship feature, deliberately.** It is not satisfied by a feature but by a *practice*: building the evaluation harness and fixed question set before the agents, and publishing O3. That is scoped in [features_prioritized.md](features_prioritized.md) as a Now-tier engineering item, and it is the recommendation the PRD leads with.

## 3. The integration argument — why the loop, not the feature

Every feature above is individually copyable, and several already exist elsewhere. Genie verifies within a query `[S32]`. Cortex reads a semantic model `[S36]`. Hex shows every step `[S54]`. Wren AI is open source with a modelling layer `[S50]`. **No single row in this list is defensible on its own**, which is ASSUMPTIONS A3 stated in product terms.

What is not copyable piecemeal is the closure:

> **The plan is visible before it runs (4), so errors are caught before they cost anything. Each hop is verified by a different query (9), so failures surface rather than propagate. Failure triggers replanning (10) rather than continuation. The trace is emitted per handoff (15) and re-runnable in isolation (16), so checking costs seconds. An override corrects the organisation's semantics permanently (17), so the next question is cheaper. The whole thing exports as one artifact (18), so it can be shared, challenged and archived. And nothing reaches a stakeholder unmarked (19).**

Each element makes the next one cheaper. Visible plans make verification shorter; per-hop verification makes overrides targeted; overrides feed bindings; better bindings shorten plans; shorter plans compound less error (P2). **That is a loop, and a competitor who ships hop-level lineage without the plan-first, verify-per-hop, override-persisting structure has shipped a log file.**

**The concession that keeps this honest.** The loop's value rests on one untested claim — that verification is cheaper than re-derivation (O2). Priya's own objection denies it ([strategy/personas.md](../strategy/personas.md) §2). If that claim is false, features 15 through 18 are ceremony, and the product is a slower path to an answer she would have written herself. **This is not a 10x claim, and A2 stands.**

## Recommended next 3

1. **Build 18 (exportable investigation) in the first sprint.** Four jobs, one artifact, and retrofitting export onto a stateful chat UI is expensive.
2. **Prototype 9 (per-hop verification) against the fixed question set before building 15–17.** It is the mechanism P7 rests on and the only one that improves O4; if a cheaper structurally-different check cannot catch seeded errors, the whole verify beat is decorative.
3. **Specify 17's failure mode explicitly in [ux_spec.md](ux_spec.md).** When an override invalidates downstream assumptions the honest behaviour is to invalidate and replan — and saying so in the spec is what stops it degrading into "re-run everything and hope."
