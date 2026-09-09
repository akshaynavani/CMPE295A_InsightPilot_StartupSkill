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

**A5: Self-hosting is undecided.** Open source is settled; whether the product is self-hosted, managed, or both is not.
— basis: founder explicitly unsure. Affects positioning, GTM and the cost model.
— closes in: phase 2 (`strategy/positioning.md`)
— kills-pack-if-wrong: **no**

**A6: The competitive differentiator is deferred to the phase 1 teardown.**
— basis: founder declined to assert one pre-research. The teardown of Power BI Copilot, Databricks Genie, ThoughtSpot, Snowflake Cortex Analyst and Tableau Pulse — plus "analyst writes SQL" and "do nothing" — must establish it from failure mechanisms rather than marketing gaps.
— closes in: phase 1 (`research/competitors.md`), consumed by phase 2
— kills-pack-if-wrong: **no**

## Unconfirmed inferences (made by the generator, not the founder)

**A7: The user spectrum was derived, not supplied.** Low edge = business manager who consumes answers; beachhead = enterprise analyst; high edge = staff data scientist who audits lineage and overrides ML choices.
— basis: founder delegated this choice. Selected over the tighter junior↔senior-analyst spectrum because a SQL-fluent beachhead does not by itself justify a natural-language interface — the non-technical consumer at the low edge is what makes conversation load-bearing, and the data scientist at the high edge is what makes traceability load-bearing. Both signature features then earn their place instead of being asserted.
— kills-pack-if-wrong: **yes** — the PRD, UX spec, journeys (A17–A20) and persona set (A10) are all written against these three edges.

**A8: Problem magnitude is unquantified.** No figure for analyst queue length, median turnaround, or cost per ad-hoc question appears anywhere in phase 0.
— basis: the founder team has no lived experience inside an enterprise analytics function, so any number here would be invented. Phase 1 must source it.
— kills-pack-if-wrong: **yes, if it cannot be sourced** — an unquantifiable problem undermines the market sizing (A09) and the whole premise that per-question overhead is worth removing.

**A9: The "why now" shifts are founder-asserted and undated.** Tool-use/replanning reliability and standardized tool access (MCP, agent frameworks).
— basis: plausible and widely held, but stated without citation. `quality-bar.md` property 2 requires a source or an explicit tag.
— closes in: phase 1 (`research/survey.md`) with dated citations
— kills-pack-if-wrong: **no** (weakens the narrative; the mechanism stands regardless)

**A10: Run slug is `agentic-bi`; the working name is "Agentic BI".**
— basis: taken from the proposal title. No naming exercise was run.
— kills-pack-if-wrong: **no**
