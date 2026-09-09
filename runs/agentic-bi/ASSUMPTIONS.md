# Agentic BI — Assumptions & Open Decisions

**What this is** — Every choice in this pack that was made without founder confirmation, plus every decision deliberately deferred, each with its basis and its blast radius.
**Why it exists** — Six weeks from now nobody will remember whether "no moat declared" was an oversight or a judgment call. Without this file the audit reads deliberate scope decisions as defects and regenerates work that was cut on purpose, and the project advisor cannot distinguish a gap from a choice. That distinction is the whole point of the file.
**How to read it** — `kills-pack-if-wrong: yes` rows first; those invalidate downstream artifacts if they turn out false. A skeptic should attack A2 and A7, the two places this pack knowingly declines to make a startup claim.
**Depends on / feeds** — Derived alongside [BRIEF.md](BRIEF.md) during phase 0. Read by every generator skill and by `startup-audit`, which must treat the *deliberate exclusions* below as closed rather than missing.

---

## Deliberate scope decisions (founder-confirmed — NOT gaps)

These were raised, discussed, and decided. The audit must not reopen them.

**A1: The financials layer is cost-side only.** Excluded manifest rows: **A44** `revenue_build.md`, **A46** `use_of_funds.md`, **A48** `comps_exits.md`.
— basis: academic capstone with no revenue, no CAC data and no funnel. Any revenue projection would be fabricated, and `references/quality-bar.md` property 2 treats unsourced numbers as a defect. Retained instead: A43 pricing as a *falsifiable price threshold*, A45 unit economics, A47 risk matrix — all computable from the system's own architecture.
— kills-pack-if-wrong: **no**

**A2: No single 10x claim is made; all four agents are built as integrated breadth.**
— basis: founder decision, made after the tension was explicitly raised. The beachhead (enterprise analyst) can already query, chart and analyze, so automating those three stages is convenience rather than leverage; the defensible 10x candidates were the ML layer and diagnostic decomposition. Founder chose breadth for capstone technical scope and accepted the tradeoff.
— consequence: `startup-critic` will flag the absent differentiator at every phase gate from 2 onward. It is logged here once as an accepted deviation and must not be re-litigated per phase, nor papered over with a manufactured claim.
— kills-pack-if-wrong: **no** (weakens the narrative layer; invalidates nothing)

**A3: No moat is declared.**
— basis: founder selected "no durable moat yet" over asserting one. With an open-source core the code is not the asset. Three candidate compounding loops are stated in BRIEF.md with the evidence that would confirm the strongest.
— kills-pack-if-wrong: **no**

**A4: Visuals and website phases are deferred, not cancelled.** Open manifest rows: **A49**, **A50**, **A51**, **A52b** (required); **A52**, **A56**, **A57** (optional).
— basis: run scoped to documents only. Prerequisites for both phases are fully satisfied by phases 0–7, so they resume cleanly later. Note: `node` is not installed on this machine and both skills shell out to it.
— kills-pack-if-wrong: **no**

## Open decisions (deferred by choice, to be closed downstream)

**A5: Self-hosting is undecided.** Open source is settled; whether the product is self-hosted, managed, or both is not. — **CLOSED 2026-09-08 by founder decision, at the phase 1 → 2 gate.**
— basis: founder was explicitly unsure at phase 0. Phase 1 forced the decision by coupling it to A11: a managed-only product cannot make the cross-source neutrality argument, which is the only structural answer to the gravity question the research supports.
— **decision: open-core, self-hostable first.** The product runs inside the customer's own boundary and spans Postgres, files and APIs precisely because it belongs to no warehouse.
— **constraint that travels with it:** "self-hostable" means the *orchestration layer* runs in the customer's environment against their own model API key — **not** that the system runs on a small local model. Tool-initialisation failure is the leading agent reliability bottleneck and is catastrophic in small models (89% error rate in qwen2.5:3b, absent in large models), so a small-local-model deployment is not currently viable for this architecture. Any artifact implying otherwise is wrong. See [research/capability_table.md](research/capability_table.md) row 7.
— kills-pack-if-wrong: **no**

**A6: The competitive differentiator is deferred to the phase 1 teardown.** — **CLOSED 2026-09-08, phase 1.**
— basis: founder declined to assert one pre-research. The teardown of Power BI Copilot, Databricks Genie, ThoughtSpot, Snowflake Cortex Analyst and Tableau Pulse — plus "analyst writes SQL" and "do nothing" — must establish it from failure mechanisms rather than marketing gaps.
— **resolution** ([research/competitors.md](research/competitors.md) §4): *the investigation, not the query, is the unit — and it ships with a hop-level trace that makes verification cheaper than re-derivation.* Derived from two failure mechanisms, not marketing gaps: (1) pre-encoded correctness cannot answer an unanticipated question — every incumbent's reliability mechanism is a bounded pre-authored artifact (30 tables per Genie Agent, ~32K-token Cortex YAML, existing measures only in Copilot); (2) plausible-but-wrong is undetectable at delivery — schema-level errors are 81.2% of analysed text-to-SQL failures, and every incumbent's answer is "show the SQL," which returns the verification cost to the analyst.
— **constraints that travel with it** (must not be dropped downstream): this is a *positioning* differentiator, **not** a 10x claim — A2 stands unchanged; the bar for the lineage mechanism is Hex's notebook, not "we show the SQL"; the ML agent is deliberately not the differentiator; and no head-to-head accuracy claim is permitted, because no commercial agentic-BI product publishes a benchmark figure.
— consumed by: phase 2 (`strategy/positioning.md`)
— kills-pack-if-wrong: **no**

**A11: The gravity question is unanswered.** Why does this end as a product rather than as a feature of Databricks or Snowflake? — **RAISED 2026-09-08 by phase 1; not present in phase 0.**
— basis: the phase 1 graveyard shows that every well-funded standalone attempt at analytical intelligence was absorbed by whoever owned the data, and none failed technically. Sisu Data raised ≈$128.7M attacking the diagnostic question — the highest-value part of the loop — and became a Snowflake division in October 2023, with the standalone product in wind-down. Narrative Science was folded into Tableau in December 2021. Meanwhile ThoughtSpot, the purest market test of natural-language analytics, was marked down 73.67% in a June 2024 secondary against its November 2021 Series F.
— the only structural answer this research supports is **cross-source neutrality**: being the layer that spans Postgres, files and APIs precisely because it belongs to no warehouse. That is implied by the brief's connector-layer design but is nowhere claimed. Note that it also forces A5 — a managed-only product has no neutrality argument, so self-hosting and the gravity answer must resolve together.
— **founder decision 2026-09-08, at the phase 1 → 2 gate: answer A11 with cross-source neutrality, and back it with the open-core self-hostable deployment model chosen in A5.** The two resolve together, as phase 1 required. The claim phase 2 must make and defend: this is not absorbable as a warehouse feature because its value is *spanning* warehouses, files and APIs — which is a thing no warehouse vendor can ship without arguing against its own gravity.
— **the honest residual**, which `strategy/positioning.md` must state rather than bury: neutrality is a *structural* answer, not an empirical one. It has not been tested that a real customer's questions actually span sources — if the first serious customer's data all lives in one warehouse anyway, the neutrality argument is true and worthless. That is a discovery question, and it belongs in the validation layer.
— closes in: phase 2 (`strategy/positioning.md`) — **now closed by the decision above; the residual is carried to `validation/`**
— kills-pack-if-wrong: **no for the capstone, yes for the venture framing.** The 295A/295B build is unaffected; the narrative layer's "why this is a company" claim is not.

## Unconfirmed inferences (made by the generator, not the founder)

**A7: The user spectrum was derived, not supplied.** Low edge = business manager who consumes answers; beachhead = enterprise analyst; high edge = staff data scientist who audits lineage and overrides ML choices.
— basis: founder delegated this choice. Selected over the tighter junior↔senior-analyst spectrum because a SQL-fluent beachhead does not by itself justify a natural-language interface — the non-technical consumer at the low edge is what makes conversation load-bearing, and the data scientist at the high edge is what makes traceability load-bearing. Both signature features then earn their place instead of being asserted.
— kills-pack-if-wrong: **yes** — the PRD, UX spec, journeys (A17–A20) and persona set (A10) are all written against these three edges.

**A8: Problem magnitude is unquantified.** No figure for analyst queue length, median turnaround, or cost per ad-hoc question appears anywhere in phase 0. — **CLOSED PARTIAL 2026-09-08, phase 1.**
— basis: the founder team has no lived experience inside an enterprise analytics function, so any number here would be invented. Phase 1 must source it.
— **resolution** ([research/survey.md](research/survey.md) §6): **turnaround is sourceable; queue length is not.** Sourced: one-to-four-week enterprise data-request turnaround and five-to-ten business days below 500 employees (IBM, attributing Sigma and Forrester — Medium confidence, a citation chain rather than a primary source); days-to-a-week data preparation for 76% of companies and 44% of data-engineer time on pipeline rebuild (Fivetran/Wakefield, n=300, but fielded 2021 and therefore dated). **Not sourceable:** no per-analyst requests-per-week measurement exists in the public record from any study with a disclosed methodology — every located figure is consultancy or vendor content marketing. The widely circulated "80% of a data team's time" figure was found, traced to unsourced vendor marketing, and is **rejected**; it supports nothing in this pack.
— **standing rule for all downstream artifacts:** no artifact may state a requests-per-analyst-per-week figure. Turnaround may be cited, always attributed as *reported by IBM, attributed to Sigma*.
— **reframe this forces** (adopt in phase 2): the High-confidence, current, independently-surveyed evidence is about **trust**, not latency — 83% now prioritise trust in data, up from 66% year over year, and 71% fear hallucinated output reaching stakeholders (dbt Labs, n=363, fielded Dec 2025–Feb 2026); 24.9% name accuracy and hallucination as their top GenAI reservation and 59% are funding semantic layers to constrain AI output (Futurum, n=818, 1H 2026). Latency evidence is Medium-confidence and second-hand; trust evidence is High-confidence and first-hand. **Positioning should lead with verifiability and support with latency.** The brief, beachhead, mechanism and vocabulary all stand; only the emphasis changes, and `time-to-verified-answer` already contains both halves.
— kills-pack-if-wrong: **resolved to no.** The premise survives on stronger evidence than it was originally argued from.

**A9: The "why now" shifts are founder-asserted and undated.** Tool-use/replanning reliability and standardized tool access (MCP, agent frameworks). — **CLOSED 2026-09-08, phase 1, with one shift restated.**
— basis: plausible and widely held, but stated without citation. `quality-bar.md` property 2 requires a source or an explicit tag.
— **Shift 2 (tool access standardised) — fully supported, now dated.** MCP announced and open-sourced 2024-11-25 with a Postgres reference server among the originals; OpenAI adopted March 2025; Google DeepMind and Microsoft mid-2025; AWS late 2025; donated to the Linux Foundation's Agentic AI Foundation December 2025. Four named adopters, a neutral steward, inside the brief's stated 18–24 month window. One correction: it standardises *access*, not *semantics* — it makes the connector layer tractable, which is the brief's actual claim, and does nothing for the schema-understanding problem behind 81.2% of text-to-SQL failures.
— **Shift 1 (reliability "crossed a usable threshold") — partially supported. MUST BE RESTATED.** The trend is real and dated (METR: 50%-reliability task-horizon doubling ≈ every 7 months over six years, ≈ every 4 months across 2024–2025). The *threshold* claim is contradicted for this task class: ≈14.55–16% on DABstep's Hard split, `pass^8` below 25% on τ-bench, error propagation named the primary agent reliability bottleneck. Required wording, to be used verbatim wherever a "why now" appears: *agentic tool-use became reliable enough that a chained fetch → analyze → model → visualize workflow is worth building and measuring — not reliable enough to trust unverified; which is why lineage is load-bearing rather than cosmetic, and why the 295A spike tests one narrow path.* The phrase "crossed a usable threshold" must not appear in any artifact.
— note: the restatement is *stronger* than the original — it converts the pack's central risk into the justification for its signature feature.
— kills-pack-if-wrong: **no** (weakens the narrative; the mechanism stands regardless)

**A10: Run slug is `agentic-bi`; the working name is "Agentic BI".**
— basis: taken from the proposal title. No naming exercise was run.
— kills-pack-if-wrong: **no**
