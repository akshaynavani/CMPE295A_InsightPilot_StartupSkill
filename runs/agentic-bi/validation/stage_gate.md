# Stage gate — where this actually sits

**What this is** — The company's position in Blank's four stages (Customer Discovery → Validation → Creation → Building), the evidence supporting that placement, and the numbered exit criteria required to pass the next gate.
**Why it exists** — Fifty artifacts create an impression of progress that the evidence does not support. This file is the corrective: **a complete pack is not traction**, and the specific failure it prevents is a team that has documented a venture thoroughly concluding it has therefore validated one. It also gives the 295A/295B project plan a definition of done that is not "we built the thing."
**How to read it** — §1 is the placement and it is deliberately unflattering. A skeptic should attack §3's exit criteria for being too lenient, and §5, which names what a complete pack is and is not evidence of.
**Depends on / feeds** — Placement argued from [riskiest_assumptions.md](riskiest_assumptions.md) (all rows `untested`) and [experiment_board.md](experiment_board.md) (all results `planned`). Feeds [metrics_by_stage.md](metrics_by_stage.md), [pivot_log.md](pivot_log.md) and the capstone project plan.

---

## 1. Current placement

> ### Customer Discovery — Phase 1 of 4. Not yet exited.

Specifically: **hypotheses stated, none tested.** In Blank's terms this venture has completed the *state your hypotheses* step and has not begun *test the problem*.

### 1.1 Evidence supporting the placement

| Signal | State |
|---|---|
| Hypotheses stated and falsifiable | ✅ Nine, with pre-declared thresholds ([experiment_board.md](experiment_board.md)) |
| Customers interviewed | **0** |
| Problem validated with anyone outside the team | **No** |
| Working software | **None** |
| Revenue, pipeline, LOIs | **None** — and out of scope (A1) |
| Riskiest assumptions tested | **0 of 12** ([riskiest_assumptions.md](riskiest_assumptions.md)) |
| Problem statement source | **Desk research, not lived experience** — BRIEF states this explicitly |

### 1.2 What the pack *is* evidence of

Not nothing, and worth stating precisely so the placement is not read as dismissal:

- **A defensible market map.** The teardown names real systems with measured limits and a documented graveyard `[S32][S36][S42][S46][S56][S58]`.
- **A sourced problem statement** where sourcing was possible — and an explicit record of where it was not, including a widely circulated figure traced to vendor marketing and **rejected** ([research/sources.md](../research/sources.md), *Named gaps*).
- **A buildable architecture** with two components labelled research risk rather than hidden ([tech/not_vaporware.md](../tech/not_vaporware.md) §4).
- **Arithmetic that came out at ≈2.9× and was published as ≈2.9×** rather than inflated ([tech/whitepaper.md](../tech/whitepaper.md) §5).

**That is a well-founded set of hypotheses. It is not validation, and the distinction is the whole point of this file.**

## 2. Why not further along

The tempting misreading is that a fifty-artifact pack, a specified architecture and a costed market represent Customer Validation. They do not, for one reason:

> **Every claim in this pack about what a customer wants is an inference from public evidence about the market, not an observation of a customer.**

The pack knows what Databricks ships `[S32]`, what practitioners tell surveys `[S16][S17]`, and what the benchmarks measure `[S4]`. It does not know what any individual analyst would actually do, and the single claim everything rests on — that verification is cheaper than re-derivation — is **denied by the beachhead persona's own stated objection** and unmeasured anywhere in the literature.

## 3. Exit criteria — Discovery → Validation

All six required. Thresholds declared here before any data exists.

| # | Criterion | Threshold | Source experiment |
|---|---|---|---|
| **G1** | **Problem interviews completed** | **≥ 10 analysts + 5 budget owners**, screened against [discovery_guide.md](discovery_guide.md) §2 | — |
| **G2** | **Multi-source reality confirmed** | Median **≥ 25%** of analysts' last-20 actual requests span more than one system of record | E3 |
| **G3** | **Verification cost ratio measured and favourable** | Median **≤ 0.5**; hard fail above 0.8 | E1 |
| **G4** | **Verification demonstrably works** | **≥ 70%** of seeded defects rejected, and **≥ 2×** the no-trace control rate | E2 |
| **G5** | **Budget line identified** | **≥ 3 of 5** buyers name a specific existing line item this would come from or displace | E4 |
| **G6** | **User spectrum confirmed** | **≥ 7 of 10** analysts confirm both edges — they field questions from a non-technical requester *and* their work is reviewed by a senior scientist | R7 |

**Estimated cost to clear all six: ~25 founder-hours over 4 weeks. No engineering.**

**G3 and G4 must both pass.** Passing G3 alone means checking is cheap; passing G4 alone means checking works but costs too much to do. **The dangerous combination is G3 pass with G4 fail** — cheap verification that does not verify, which would ship confident wrong answers wearing an audit trail. That is a worse product than having no trace at all, and the gate is written to catch it.

## 4. Subsequent gates

Stated so the whole path is visible, with the honest caveat that gates 3 and 4 lie beyond the capstone's scope.

### Validation → Customer Creation

| # | Criterion | Threshold |
|---|---|---|
| V1 | Published multi-hop execution accuracy on a fixed question set | ≥ 50% (E6) |
| V2 | Verifier coverage measured, including the semantically-plausible defect class | ≥ 60% overall, ≥ 30% plausible (E7) |
| V3 | Time from clone to first successful investigation | Median < 30 min (E8) |
| V4 | Deployments reaching a **second** analyst without founder intervention | ≥ 3 |
| V5 | Analyst review-time per week, stable | < 4 h, flat or falling over 8 weeks (E5 / A12) |
| V6 | At least one buyer asks unprompted what it would cost | ≥ 1 |

### Customer Creation → Company Building

Deliberately sparse: it is beyond the honest planning horizon of a two-semester capstone, and specifying it in detail would be theatre. The one criterion worth fixing now — **override rate falling per source with no model change over 90+ days (R10)** — is the only observation that would ever evidence the A3 moat candidate, and the instrumentation for it exists from day one ([tech/architecture/D04](../tech/architecture/D04_memory_schema.md)).

## 5. What this means for CMPE 295A / 295B

The academic and the venture timelines do not align, and pretending otherwise would distort both.

| | 295A | 295B |
|---|---|---|
| **Venture stage** | Discovery → exit Discovery | Validation, partially |
| **Primary deliverable** | The **harness, the fixed question set, and a published accuracy number** — plus G1–G6 cleared | Working narrow-path system; V1–V3 |
| **What would count as success** | Six gate criteria answered honestly, **including if the answer is no** | A measured, published number no commercial product publishes |
| **What would count as failure** | Building four agents with no measurement of whether any of it works | Shipping a demo without the accuracy figure |

**The uncomfortable implication, stated plainly:** the correct first month of a build project contains almost no building. G1–G6 need about twenty-five founder-hours and zero code, and they can invalidate the architecture that the rest of the semester would implement.

**A genuinely good capstone outcome includes the branch where G3 fails.** The field has no public measurement of verification cost in either direction; a rigorous negative result would be a real contribution and is explicitly the honest ending in [narrative/future_press.md](../narrative/future_press.md) and [narrative/mission_vision.md](../narrative/mission_vision.md) §5.

## Recommended next 3

1. **Put G1–G6 in the 295A project plan as milestones with dates**, ahead of any engineering milestone. A gate that lives only in this file will be skipped when the build gets interesting.
2. **Do not let the pack's completeness be read as progress in any review.** The honest sentence is: *"fifty artifacts, twelve untested assumptions, zero customers interviewed"* — and saying it first is far stronger than being asked.
3. **Write the G3-fails plan now, while it is still hypothetical.** Deciding in advance what happens if verification is not cheaper than re-derivation is the difference between a pivot and a scramble — [pivot_log.md](pivot_log.md) holds it.
