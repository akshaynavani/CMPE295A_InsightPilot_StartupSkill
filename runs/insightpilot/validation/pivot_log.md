# Pivot log — decisions taken, roads closed, and the standing triggers

**What this is** — The decision journal: what has already been considered and killed, why, and the standing pivot-or-persevere criteria in the form *"we pivot if X by date Y."*
**Why it exists** — Six weeks from now nobody will remember whether "no moat declared" was an oversight or a judgement, or why the business-user market was passed over. Without this journal a later reader — an advisor, a new team member, the audit — reads deliberate closures as gaps and reopens settled arguments. It also exists to fix the pivot triggers **while they are hypothetical**, because a trigger written after a disappointing result is a rationalisation.
**How to read it** — §1 is what is already closed; §3 is what would force a change. A skeptic should attack §3's triggers for being too loose, and §4, which names the pivot the team will be most tempted by and most wrong to take.
**Depends on / feeds** — Consolidates decisions from [ASSUMPTIONS.md](../ASSUMPTIONS.md), the grill session recorded in [BRIEF.md](../BRIEF.md), and phases 1–5. Triggers reference thresholds in [experiment_board.md](experiment_board.md). Feeds [stage_gate.md](stage_gate.md) and the audit.

---

## 1. Roads already closed

Each was genuinely considered. None should be reopened without new evidence of the kind named in the last column.

| # | Road considered | Decision | Why | What would reopen it |
|---|---|---|---|---|
| **P1** | **Sell to business users** — natural-language self-service for non-technical people | **Closed.** Beachhead is the analyst; stakeholders consume but cannot ship unverified (PRD non-goal 1) | ThoughtSpot is the purest test of this bet and cleared a **73.67% markdown** in a June 2024 secondary against its Series F `[S46]`. And a person who cannot verify, putting a number in front of their boss, is being set up to be wrong in public | Evidence that stakeholders will accept a mandatory analyst gate *and* that analysts can absorb the review load (E5) — i.e. an expansion, not a repositioning |
| **P2** | **Claim a single 10× differentiator** | **Closed** (ASSUMPTIONS A2). Integrated breadth chosen knowingly | The beachhead can already query, chart and analyse — automating those is convenience, not leverage. Phase 4's arithmetic later confirmed it independently at **≈2.9×**, band 1.8×–4.2× ([tech/whitepaper.md](../tech/whitepaper.md) §5) | Nothing short of a measured order-of-magnitude result. **The 13.8× queueing figure does not count** — it was computed and withdrawn because induced demand consumes it |
| **P3** | **Declare a moat** | **Closed** (A3). None declared | Open-source core means the code is not the asset. The strongest candidate — a learned semantic layer — is unevidenced | Override rate falling per source over 90+ days with no model change (R10). **That is an observation, not an argument** |
| **P4** | **Build our own semantic layer** | **Closed.** We consume dbt/Cube; we do not replace them | 59% of large enterprises are already funding semantic layers `[S17]`. Telling a buyer that spend is unnecessary loses the deal and is false — a semantic layer says what a metric *means*, not what happened | E9 showing < 5 pp accuracy lift from consuming one, which would mean the integration is not worth the dependency either way |
| **P5** | **Managed multi-tenant SaaS** | **Closed** (A5). Open-core, self-hostable | A hosted service cannot make the cross-source neutrality argument that answers the gravity question (A11). Neutrality asserted by a service that sees all your data is a claim; neutrality in code you run is a property | A regulated-customer segment demanding managed deployment *and* a contractual way to preserve neutrality — the 2031 branch in [narrative/future_press.md](../narrative/future_press.md) |
| **P6** | **Lead with the ML agent** | **Closed** (A2). It is built, not led with | Widest capability-to-product gap in the landscape, and the least trusted by the person who must approve it. MLE-bench's 36.4% medal rate runs on a **12-hour budget** `[S9]` — not a conversational latency budget | A demonstrated useful modelling result inside a minutes-long budget, reviewed and accepted by a staff data scientist |
| **P7** | **Reflection / self-critique / LLM-as-judge for verification** | **Closed on principle** ([tech/techniques/wave3.md](../tech/techniques/wave3.md) §1) | All keep verification inside the model that produced the output. Verification must run structurally different code — Databricks reached the same conclusion in production `[S32]` | Evidence that self-critique catches the *plausible* defect class that structural checks miss (E7's failure branch) — and even then as a supplement, never a replacement |
| **P8** | **Size the market top-down from the BI category** | **Closed.** Bottom-up only | "1% of a $40B market" would contradict the re-segmentation declaration and imply an existing-market play the product cannot win on distribution ([strategy/market_type.md](../strategy/market_type.md)) | Nothing. This is a methodology decision, not a strategy one |
| **P9** | **Outbound sales, resellers, cloud marketplace, paid acquisition** | **Closed by arithmetic** ([strategy/channel_plan.md](../strategy/channel_plan.md) §3) | At a $900 ACV, outbound needs a 4–9 seat account just to repay acquisition. A reseller's 28% is payment for a sales motion the product is designed not to need | **R11** — if central analytics teams turn out to be materially larger than 15 analysts, a $45K ACV makes inside sales viable and this reopens |
| **P10** | **Quantify problem magnitude from the circulating "80% of a data team's time" figure** | **Closed and rejected.** Traced to unsourced vendor marketing `[S20]` | It supports nothing anywhere in this pack. Recorded specifically so a later reader who meets it elsewhere knows it was found and refused | A disclosed study with a stated methodology |

## 2. What has *not* been decided

Named so that absence is not mistaken for closure:

- **Which features sit inside the open core versus a paid edge.** A5 settles deployment, not the open-core boundary. Deferred to `financials/`.
- **What the ML agent usefully does in five minutes.** P9 forbids the twelve-hour behaviour; nobody has specified the minutes-long version ([product/PRD.md](../product/PRD.md) §9.4).
- **Whether an unreviewed answer at the low edge should be blocked, watermarked, or auto-routed** (PRD §9.5).
- **Whether a cached plan should expire on time as well as on schema change.**

## 3. Standing pivot-or-persevere triggers

Declared before results exist. Dates assume discovery starts at the beginning of 295A.

| # | Trigger | Measured by | Deadline | Decision if triggered |
|---|---|---|---|---|
| **T1** | **Verification cost ratio > 0.8** | E1, 5 analysts | **Week 4** | **Stop and publish the negative result.** The differentiator is void and a faster wrong-answer generator is not worth building. The field has no public measurement of verification cost in either direction, so a rigorous negative is a genuine contribution |
| **T2** | Ratio in 0.5–0.8 (amber) | E1 | Week 4 | **Persevere, re-scope.** The differentiator becomes cross-source reach rather than verification cost; [tech/whitepaper.md](../tech/whitepaper.md) §5 is recomputed without mechanism D as a gate |
| **T3** | **Seeded-defect rejection < 50%, or no lift over control** | E2 | **Week 5** | **Halt product work and redesign the verify surface.** Worse than T1: it means the trace is comfortable rather than effective, and would ship confident wrong answers wearing an audit trail |
| **T4** | **< 15% of last-20 requests are multi-source** | E3, 10 analysts | **Week 3** | **Re-scope, do not stop.** Neutrality is true and worthless; SAM halves to ≈$61M; the product narrows to single-warehouse depth — where it meets Genie on its own turf and loses on distribution. That combination is a reason to reconsider the venture framing, not the capstone |
| **T5** | **≤ 1 of 5 buyers names a budget line** | E4 | **Week 4** | **Accept that this is a feature, not a company.** Correct outcome for the capstone; decisive for the venture. Record it and continue building for the academic deliverable |
| **T6** | **Multi-hop accuracy < 30% on the fixed set** | E6 | **End 295A** | Narrow the spike to two-hop questions and publish the low number. **Publishing is still the contribution** — no commercial product publishes any figure |
| **T7** | **Verifier catches ≈0% of semantically-plausible defects** | E7 | End 295A | Replace the whitepaper's judgement-based 4.0× with the measured figure and state plainly that the verifier catches mechanical, not semantic, failures. The shown-plan gate becomes the primary defence |
| **T8** | **Analyst review-time > 8 h/week or rising over 8 weeks** | E5 | Week 12 of deployment | **A12 is firing.** Redesign the sign-off gate — trust levels per question-shape so repeat investigations auto-approve. Do not scale deployments until it is flat |
| **T9** | **Median clone → first investigation > 60 min** | E8 | Week 8 of 295B | The self-serve motion fails and the real motion is design-partner-led. Rewrite [strategy/gtm.md](../strategy/gtm.md) and [strategy/channel_plan.md](../strategy/channel_plan.md) — **this was the only channel with viable economics** |
| **T10** | **Fewer than 7 of 10 analysts confirm both spectrum edges** | R7 | Week 3 | ASSUMPTIONS A7 is wrong, and the PRD, UX spec, all four journeys and the persona set are written against it. **Revise those five artifacts before building against them** |

## 4. The pivot this team will be most tempted by, and should refuse

**Pivoting to the business-user market after a disappointing analyst response.**

If E1 comes back amber and E3 comes back weak, the instinct will be that the analyst is too sophisticated a customer — they can already write SQL, so the value is thin — and that the real market is the non-technical requester who cannot. That reasoning is superficially strong and it is P1, reopened.

**Three reasons to refuse it:**

1. **It is the bet that was already priced.** ThoughtSpot ran it with real capital and real distribution and was marked down 73.67% `[S46]`.
2. **It makes the verification problem unsolvable rather than easier.** The business user cannot check anything. Removing the analyst does not remove the need for verification — it removes the only person capable of it, which is precisely the failure P3 describes `[S2]`.
3. **The pack's own evidence for the pivot would be missing.** Nothing in [research/](../research/landscape.md) suggests non-technical self-service works; the graveyard suggests the opposite four times over `[S59][S40][S58][S56]`.

**If the analyst market fails, the honest conclusion is that this thesis is wrong — not that a different customer will rescue it.**

## 5. Log format for entries from here

Every future decision gets a row: **Date · Decision · Evidence that prompted it · What it closes · What would reopen it.** A decision recorded without the last column is not a decision, it is a mood — and six weeks later nobody will be able to tell them apart.

## Recommended next 3

1. **Fix T1–T5's dates in the 295A project plan now.** All five are cheap, all five precede engineering, and a trigger without a date is a hope.
2. **Re-read §4 before any strategy meeting held after a disappointing discovery result.** It is written for that specific meeting.
3. **Add a row to §1 every time an option is closed, including in casual conversation.** The value of this file is entirely in it being complete — a closed road that was never logged is one that gets re-argued.
