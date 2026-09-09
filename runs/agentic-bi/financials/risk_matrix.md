# Risk matrix

**What this is** — The eight risks that could end this venture or materially change its shape, each with likelihood, impact, a **leading indicator** that would give warning, the mitigation, and the **residual** level after mitigation.
**Why it exists** — The pack has raised risks in eight different files; a reader needs them in one table, ranked, with the honest admission of what remains after mitigation. The specific failure it prevents: a matrix where everything mitigates to "low," which is fiction and reads as such — **five of the eight residuals below are Medium or High**, and the two most dangerous barely move.
**How to read it** — The *Leading indicator* column is the operational value: each names something observable before the risk fully materialises. A skeptic should attack the residual column, and R1's mitigation, which is a measurement rather than a fix.
**Depends on / feeds** — Consolidates [validation/riskiest_assumptions.md](../validation/riskiest_assumptions.md), [narrative/vc_memo.md](../narrative/vc_memo.md) §6, and the cost sensitivity in [unit_economics.md](unit_economics.md). Feeds the 295A project plan and any advisor review.

> **Scope note.** Cost side only (A1). **A44 `revenue_build.md`, A46 `use_of_funds.md`, A48 `comps_exits.md` are excluded by founder decision — closed, not missing.**

---

## The matrix

Likelihood and impact are assessed for the **venture**; the capstone's exposure is separated in §2 because the two differ sharply.

| # | Risk | Type | Likelihood | Impact | Leading indicator | Mitigation | **Residual** |
|---|---|---|---|---|---|---|---|
| **R1** | **Verification costs as much as re-derivation** — the analyst re-derives anyway, so the trace delivers nothing | Market / product | **Medium** | **Fatal** | Analysts in the timed task opening every hop rather than the doubted one; hop-inspection rate near 100% in any deployment | **None available — only measurement.** E1 with 5 analysts, ~6 founder-hours, before any further build. Declared stop-trigger if ratio > 0.8 | **HIGH** — a mitigation that measures a risk does not reduce it |
| **R2** | **Multi-hop planning does not reach usable accuracy on real schemas** | Technology | **Medium-High** | **Fatal** | Harness accuracy below 30% on the fixed set; replan counts climbing per investigation | Typed plan DAG, static validation, hop-count ceiling, per-hop verification, shown-plan gate. Narrow the 295A spike to one path | **HIGH** — DABstep puts the field at ≈14.55–16% on hard tasks `[S4]`; the mitigations are dampeners, not solutions |
| **R3** | **Verification catches only mechanical, not semantic, failures** — a right-cardinality wrong-meaning join passes every check | Technology | **Medium-High** | **Severe** | Seeded-error rejection near zero on the *plausible* defect class (E7) | Shown-plan gate as the first line; analyst inspection as the last. Publish the coverage number and narrow the claim accordingly | **MEDIUM-HIGH** — the whitepaper already discounts 6.7× → 4.0× on judgement for exactly this |
| **R4** | **Absorbed as a warehouse feature** — the gravity that took Sisu and Narrative Science | Competition | **Medium** | **Severe** (venture) | A major vendor shipping cross-source planning; Genie's table ceiling rising sharply; Inspect extending across a plan rather than within a query | Cross-source neutrality, made a property rather than a claim by open-core self-hosting (A5/A11). Contribute the lineage format to a neutral body | **MEDIUM** — Sisu raised ≈$128.7M and was absorbed anyway `[S56][S57]`; neutrality is structural, not proven |
| **R5** | **The champion is made worse off** — the analyst absorbs review load the other four roles shed, and stops advocating (A12) | Retention / GTM | **Medium-High** | **Severe** | **Review-queue depth**, and analyst review-time per week trending above 4 h | Trust levels per question-shape so repeat investigations auto-approve; flywheel reducing review load; queue-overload state in the UI | **MEDIUM** — the fix is a known design change, but it depends on R1 being favourable |
| **R6** | **Cost per investigation is several times the model** — `expected_attempts` far above 1 | Cost | **Medium-High** | **Moderate** | Retry counts in the harness; customer TCO complaints | Plan caching, execution-feedback repair, replan cap, `EXPLAIN` cost guard. **Verification adds zero model tokens** | **MEDIUM** — moves TCO 4.5× across the modelled range and is unmeasured, but the price threshold still clears at 5 attempts ([pricing.md](pricing.md) §4.4) |
| **R7** | **Self-serve install fails** — median clone-to-first-investigation over 60 min, killing the only viable channel | GTM | **Medium** | **Severe** | Instrumented drop-off between connector configured and first successful investigation | Docker Compose, two connectors only, seeded demo data, README answering *"how is this not Genie?"* above the fold | **MEDIUM** — at a $900 ACV there is no second channel to fall back to `[S52][S44]` |
| **R8** | **Key-person / capacity** — a two-person capstone team with a fixed two-semester window | Key-person | **High** | **Moderate** (capstone) / **Severe** (venture) | Slipping past the harness milestone; scope creep into charts or the ML agent | Pre-decided cut list (visualization → REST → ML agent → override re-flow); harness first; measurement over features | **MEDIUM** — the cut list is decided but not yet defended under pressure |

## 1. Reading the matrix

**No risk mitigates to Low.** That is the honest result and it is worth stating, because a matrix whose bottom row reads "Low, Low, Low" is a document written to reassure.

**The two fatal risks barely move under mitigation.** R1's mitigation is a *measurement*, not a fix — you cannot engineer your way out of verification being expensive; you can only find out early and cheaply. R2's mitigations are dampeners against a field-wide capability limit `[S4]`. **Both stay HIGH, and both are resolved by the same decision: measure before building.**

**Three risks share a single root.** R1, R5 and part of R6 all trace back to whether verification is genuinely cheap. If E1 passes, R5's mitigation works and R6's cost is tolerable. **If E1 fails, three rows fail together** — which is why it is the first experiment and the declared stop-trigger.

**R3 is the one most likely to be underestimated.** It does not kill the venture; it quietly narrows the claim. The failure looks like success — every check green, the answer wrong — and the only defence is that the pack already discounted its own number for it and named the measurement that would resolve it.

## 2. Capstone exposure versus venture exposure

The two timelines have different risk profiles, and conflating them would distort the project plan.

| Risk | Venture impact | **CMPE 295A/295B impact** |
|---|---|---|
| R1 verification cost | Fatal | **None — a rigorous negative is a valid contribution.** The field has no public measurement in either direction |
| R2 planning accuracy | Fatal | **Low.** Publishing a low number is still the first public figure in commercial agentic BI |
| R3 verifier coverage | Severe | **Low.** Measuring it is the deliverable |
| R4 gravity | Severe | **None.** The build is unaffected by who acquires whom |
| R5 champion burden | Severe | **Low.** Needs multiple users over weeks; likely unobservable in one semester |
| R6 cost | Moderate | **None.** No revenue to protect (A1) |
| R7 install friction | Severe | **Low.** Only matters if the open-source channel is tested during the capstone |
| R8 capacity | Severe | **HIGH — the dominant capstone risk** |

**The single most important row in this file is the last one.** For the venture, R1 and R2 are fatal. **For the capstone, they are deliverables** — measuring either honestly is a good outcome regardless of the answer. The risk that actually threatens 295A/295B is **running out of time**, and the specific mechanism is scope creep into the visible-but-uninformative work: charts and the ML agent, both first on the pre-decided cut list.

## 3. Risks deliberately not on this matrix

Named so their absence reads as a decision.

| Not listed | Why |
|---|---|
| **Regulatory** | Read-only, no write-back, no autonomous action, self-hosted, no PII processing beyond what the analyst already sees. The system's blast radius is *what the analyst could already read*. Not zero risk, but not top-eight |
| **Platform dependency on a model provider** | Real, and mitigated structurally: provider-abstracted client, customer's own key (A5), no fine-tuned assets. A provider change is a configuration change |
| **Data breach via the product** | Credentials never leave the boundary, one egress arrow, read-only role, audit log ([tech/architecture/D06](../tech/architecture/D06_security_trust_boundary.md)). The residual is *the model provider sees schema and optionally samples*, which is disclosed and configurable |
| **Competitive price war** | Cannot meaningfully compete on price against bundled incumbents at any price; the positioning already concedes distribution ([strategy/positioning.md](../strategy/positioning.md) §6.2) |
| **Market timing / category collapse** | Gartner forecasts >40% of agentic AI projects cancelled by end-2027 `[S31]`, low confidence. Directionally relevant, not actionable |

## 4. The leading indicators, collected

The operational output of this file. Each is observable before its risk fully materialises, and each has an owner in the 295A plan.

| Indicator | Watches | Threshold |
|---|---|---|
| **Verification cost ratio** (timed task) | R1 | > 0.8 → stop |
| **Hop-inspection rate** | R1, R5 | Outside 20–60% band |
| Harness multi-hop accuracy | R2 | < 30% |
| Seeded-error rejection, *plausible* class | R3 | ≈0% |
| **Review-queue depth** and analyst review-time/week | R5 | > 4 h/week or rising |
| Retries per investigation | R6 | > 3 sustained |
| Clone → first successful investigation | R7 | > 60 min median |
| Harness milestone slip | R8 | Any slip past week 6 |

## Recommended next 3

1. **Run E1 first, and treat it as the matrix's load-bearing row.** Three risks (R1, R5, R6) resolve or worsen together on its result, and it costs ~6 founder-hours.
2. **Put R8's cut list into the 295A plan as a signed scope decision.** It is the dominant capstone risk, and a cut agreed in advance is a decision while the identical cut in week ten is a failure.
3. **Instrument review-queue depth before the first stakeholder question arrives.** R5's leading indicator is the only one that becomes unobservable once the risk has materialised — by the time the champion has stopped advocating, the data explaining why is gone.
