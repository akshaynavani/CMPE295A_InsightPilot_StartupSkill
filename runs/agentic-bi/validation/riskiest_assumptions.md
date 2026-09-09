# Riskiest assumptions — ranked board

**What this is** — Every load-bearing assumption in the pack as one ranked board: what it is, whether it kills the company, what evidence currently exists, the cheapest decisive test, its cost and time, and its status.
**Why it exists** — The pack now runs to fifty artifacts and its claims are distributed across all of them. This board is the single place where a reader — or the team in week nine — can see **what is actually still unknown**, ranked. The specific failure it prevents: building for a semester against a premise nobody tested because it was stated confidently in five different files.
**How to read it** — Rank order is by *kills-company × cheapness to test*, so the top rows are both the most dangerous and the least expensive to resolve. A skeptic should attack the *Current evidence* column, which is mostly empty by design, and R7, where the pack's own whitepaper discounts a number on judgement.
**Depends on / feeds** — Consolidates [ASSUMPTIONS.md](../ASSUMPTIONS.md), [strategy/lean_canvas.md](../strategy/lean_canvas.md) ⚠ cells, [strategy/business_model_canvas.md](../strategy/business_model_canvas.md), [narrative/vc_memo.md](../narrative/vc_memo.md) §6, and BRIEF's riskiest-assumption line. Feeds [experiment_board.md](experiment_board.md), [stage_gate.md](stage_gate.md) and [pivot_log.md](pivot_log.md).

---

## The board

**Status is `untested` on every row.** That is the honest state of a pre-traction pack and stating it plainly is the point of this file. Cost is in founder-hours; there is no budget (ASSUMPTIONS A1).

| # | Assumption | Kills company? | Current evidence | Cheapest decisive test | Cost | Time | Status |
|---|---|---|---|---|---|---|---|
| **R1** | **An analyst can accept a correct answer they did not derive faster than they could derive it** (verification cost ratio < 1.0) | **YES** — everything collapses to 1.0× | **None.** Unmeasured anywhere in the literature ([research/survey.md](../research/survey.md) §8.1). The beachhead's own stated objection denies it: *"I read SQL faster than I read explanations"* | Timed task, 5 analysts, one question, two conditions: (a) answer + hop-level trace, (b) derive from scratch. Measure minutes to a confident accept/reject | ~6 h | 1 week | **untested** |
| **R2** | **Multi-hop planning is reliable enough end-to-end that error compounding does not make output untrustworthy** (BRIEF's stated riskiest assumption) | **YES** | **Negative.** DABstep puts multi-step data reasoning at ≈14.55–16% on hard real-world tasks vs 76.39% easy `[S4]`; error propagation is the primary agent bottleneck `[S10]` | Build the harness + 30–50 question fixed set; measure multi-hop execution accuracy on one narrow path | ~3 wk | 295A | **untested** |
| **R3** | **A material share of real ad-hoc questions require more than one source** (≥25%) | No, but **halves SAM and voids the neutrality argument** | **None.** Structural argument only ([strategy/positioning.md](../strategy/positioning.md) §4 residual) | Ask 10 analysts to classify their **last 20 actual requests** as single- or multi-source. Past behaviour, not opinion | ~5 h | 1 week | **untested** |
| **R4** | **A budget owner can name a line item this comes out of** | No, but **invalidates the market-type declaration** | **Counter-evidence.** The same buyers who fear hallucination `[S16][S17]` are spending on semantic layers instead — 59% funding them `[S17]` ([strategy/market_type.md](../strategy/market_type.md) §2.3) | One question to 5 buyers: *"if you bought this, what line does it come from and what does it displace?"* A buyer who cannot name one has answered | ~4 h | 2 weeks | **untested** |
| **R5** | **The analyst champion is not made worse off by the review burden** (A12) | No, but **kills adoption**, which is worse | **Negative, modelled.** Across one day the analyst captures the least value of five actors while absorbing the review load ([product/journeys/day_in_life.md](../product/journeys/day_in_life.md) §3) | Track analyst review-time-per-week from first deployment; leading indicator is review-queue depth | ~0 (instrumentation) | ongoing | **untested** |
| **R6** | **Cheap structural checks catch the failures that matter** — verifier coverage of *plausible* failures, not just countable ones | **YES in effect** — without it the trace is a log file | **Partial and judgement-based.** [tech/whitepaper.md](../tech/whitepaper.md) §2.3 discounts 6.7× → 4.0× purely on judgement because coverage is unmeasured | Seeded-error set: plant wrong joins, grains, region mappings; measure what escapes every check (O4) | ~1 wk | 295A | **untested** |
| **R7** | **The three-edge user spectrum is right** (low = business manager, beachhead = analyst, high = staff data scientist) — ASSUMPTIONS **A7** | **YES for the pack** — PRD, UX spec, all four journeys and the persona set are written against it | **None.** Derived by the generator, not supplied by the founder. Flagged `kills-pack-if-wrong: yes` | Discovery interviews: does the analyst actually field questions from a non-technical requester *and* get reviewed by a senior scientist? | ~0 (rides R1/R3 interviews) | 2 weeks | **untested** |
| **R8** | **Analysts will install a self-hosted open-source tool without a vendor relationship**, reaching first successful investigation in < 30 min | No, but **kills the only viable channel** ([strategy/channel_plan.md](../strategy/channel_plan.md) §4) | **Adjacent positive.** Wren AI reached 13,000+ stars and 10,000+ cloud users on this motion `[S50]` | Publish the repo with a working quickstart; instrument clone → first successful investigation, split by cohort | ~1 wk | 295B | **untested** |
| **R9** | **Consuming an existing dbt/Cube semantic layer materially improves accuracy** over raw schema introspection | No — but decides whether P6 is the roadmap's centre or its edge | **None.** 59% of enterprises fund semantic layers `[S17]`, which establishes demand, not lift | A/B the same question set against one schema, with and without its dbt layer attached | ~4 d | 295B | **untested** |
| **R10** | **The learned semantic layer compounds** — override rate falls per source with no model change (the A3 moat candidate) | No — pack explicitly declines to claim it | **None, by admission.** ASSUMPTIONS A3 names this as the confirming observation and declines to assert it | Instrument override rate per source from day one; check the slope after 90 days of real use | ~0 (instrumentation) | 90 d post-deploy | **untested** |
| **R11** | **A realistic account is 5–15 analysts**, not 50 | No, but **flips the channel verdict** — a 50-analyst team gives a $45K ACV and makes inside sales viable | **None.** Assumed in [strategy/channel_plan.md](../strategy/channel_plan.md) §1 | Ask in the first buyer conversation: *how many analysts sit on the central team?* | ~0 | rides R4 | **untested** |
| **R12** | **Self-hosting is viable on a customer's own frontier-model key** (not a small local model) | No — already constrained | **Positive, and it bounds the claim.** Tool-initialisation failure is catastrophic in small models — 89% in qwen2.5:3b, absent in large `[S11]` | Already answered by evidence. Re-test only if a customer demands a fully local deployment | — | — | **constrained, not open** |

## Reading the board

**Four rows can end this, and three of them need no code.**

R1, R3, R4 and R7 are all answerable with **interviews and about nineteen founder-hours in three weeks.** R2 and R6 need the harness, which is 295A engineering. **That ratio is the most important thing on this page**: the cheapest tests attack the largest risks, and the pack has been built without running any of them.

**Two rows carry negative evidence already.** R2's benchmark evidence points the wrong way — the field measures this capability at ≈15% on hard tasks `[S4]` — and R5 was modelled as a problem rather than discovered as one. Neither is a reason not to proceed; both are reasons the 295A scope leads with measurement rather than with agents.

**One row is a decline rather than an assumption.** R10 is the moat candidate. ASSUMPTIONS A3 refuses to claim it and this board refuses to promote it — it sits here so the instrumentation exists to test it later, not so it can be counted as evidence now.

## What the board says about sequencing

1. **R1 before anything else.** It gates R2, R6 and the whole architecture: if verification costs re-derivation, a more accurate planner does not help.
2. **R3 and R4 in the same conversations.** Both are single questions inside a discovery interview, and between them they decide whether the segment and the budget are real.
3. **R2 and R6 together in the harness.** Accuracy without a silent-error measurement is a half-answer, because P3 says the dangerous failures look like successes.
4. **R7 rides along free.** Every discovery interview tests the spectrum implicitly — ask who sends the analyst questions and who reviews their work.

## Recommended next 3

1. **Run R1 this month.** Five analysts, one afternoon, a stopwatch. It is the single cheapest test of the single largest risk in the pack, and every downstream artifact assumes its answer.
2. **Do not start agent development before the harness exists.** R2 and R6 are the two engineering risks and both are measurement problems first — [product/features_prioritized.md](../product/features_prioritized.md) already puts the harness at #1 for this reason.
3. **Add R11 to the R4 conversation as a single extra question.** It costs ten seconds and it decides whether [strategy/channel_plan.md](../strategy/channel_plan.md)'s verdict on outbound holds.
