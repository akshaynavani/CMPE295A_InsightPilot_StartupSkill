# Pitch deck — InsightPilot

**14 slides. Every title is a claim, not a category.**

**What this is** — The deck, one section per slide: the takeaway as a full sentence, a payload of 3–5 bullets, and the supporting visual named.
**Why it exists** — The advisor review and the 295A presentation both need a spoken arc, and a deck built from the pack's own evidence is the only defence against the version that gets assembled the night before from memory. It also fixes the arc: **cold-open on the problem, demolish the status quo, then show the mechanism** — teardown before build, because credibility is earned by demonstrating you know why everything else falls short.
**How to read it** — Titles alone should carry the argument; read them in sequence first. A skeptic should attack slides 9 and 13, which are where a deck normally inflates and where this one concedes.
**Depends on / feeds** — Arranges [one_pager.md](one_pager.md), [vc_memo.md](vc_memo.md), [research/](../research/competitors.md), [tech/whitepaper.md](../tech/whitepaper.md), [strategy/](../strategy/market_sizing.md). **Invents nothing.**

> **Visuals note.** The visuals phase is deferred ([ASSUMPTIONS.md](../ASSUMPTIONS.md) A4), so `visuals/visual_manifest.md` does not exist yet. Each `visual:` line below names the intended asset and, where one already exists, points at the Mermaid diagram in `tech/architecture/` that should be rendered for it. These are the manifest's future rows.

---

## Slide 1 — People stop asking questions when the answer takes a month

- An enterprise analyst's ad-hoc question comes back in **one to four weeks** `[S15]`
- So requesters route around it: **76% of businesses have made a decision without consulting data because it was too hard to get** `[S15]`
- **60–73% of enterprise data is never used for analytics at all** `[S15]`
- The market leader in this category is *doing nothing*, and it is free and instant

`visual:` cold-open — a single Slack message timestamped Thursday 4:10pm, answered the following Tuesday

## Slide 2 — Every vendor tried a chat box, and it fails in a specific, documented way

- **Schema-level errors — wrong column, wrong meaning — are 81.2% of 4,602 analysed text-to-SQL failures** `[S2]`
- *"Failure looks like a plausible but incorrect answer"* `[S2]` — you cannot see it coming
- **71% of practitioners name hallucinated output reaching stakeholders as a top concern** `[S16]`
- Power BI Q&A shipped inside the most widely deployed BI tool on earth and is **fully retired by December 2026** `[S40]`. Distribution was never its problem

`visual:` the graveyard — Watson Analytics 2019, Narrative Science 2021, Sisu 2023, Power BI Q&A 2026, with cause of death

## Slide 3 — The market's problem is not slow answers, it is that fast answers cannot be trusted

- Trust in data as a stated priority rose **66% → 83% in a single year** `[S16]`
- **24.9% name accuracy and hallucination risk as their top reservation about GenAI in analytics** `[S17]`
- **59% of large enterprises are funding semantic layers** to constrain AI output `[S17]`
- The budget is already moving toward verifiability. It is currently going to a different answer than ours

`visual:` two bars — the sourced latency evidence (medium confidence, second-hand) beside the sourced trust evidence (high confidence, two independent surveys)

## Slide 4 — Incumbents buy correctness by refusing the questions nobody anticipated

- **Databricks Genie: 30 tables per agent** `[S32]`
- **Snowflake Cortex Analyst: a hand-authored ~32K-token YAML semantic model** `[S36]`
- **Power BI Copilot cannot compute a metric that is not already a measure** `[S42]`
- These are not bugs — they are the reliability mechanism. **The better the guardrail, the narrower the set of questions attempted**
- An ad-hoc question is, by definition, the one nobody modelled in advance

`visual:` the constraint table — each incumbent's bound, stated in its own documentation

## Slide 5 — The insight: stop promising correctness, start making failure cheap to catch

- Multi-step data reasoning measures **≈15% on hard real-world tasks** `[S4]`. Nobody can promise reliable autonomous answers today
- Agents above **60% `pass^1` fall below 25% `pass^8`** `[S5]` — consistency degrades faster than capability
- So: show the plan before running it, verify every hop with a *different* query, and emit a trace that makes checking cost seconds
- **If multi-hop execution were reliable, nobody would need a trace. Because it is not, the trace is what makes the hops usable at all**

`visual:` the two-axis map — hops executed autonomously × where correctness is established, with the open quadrant empty

## Slide 6 — The unit is the investigation, and it ships with its own audit trail

- A question becomes an **analysis plan**, shown and approved before a single query runs
- Four specialist agents execute across the *real* sources — warehouse, operational Postgres, and the CSV nobody ever modelled
- **Every handoff emits its own lineage**: source touched, query run, transform applied, row counts in and out
- Each hop is separately re-runnable; the whole investigation exports as one self-contained file
- **Verification consumes zero model tokens — the checks are plain SQL**

`visual:` render of `tech/architecture/D01_investigation_pipeline.md`

## Slide 7 — In the demo, the system catches its own join failure in 40 seconds

- *"Why did cost per shipment go up in the Southwest last month?"* — needs the warehouse joined to an unmodelled carrier CSV
- The system halts before planning: *"'Cost' matches billed invoice total and estimated shipment cost. Which?"*
- **Step 3 returns amber: *"join preserved 13,061 of 14,201 rows — 8% unmatched. CSV has 4 region codes, warehouse has 6"***
- That is the failure that takes an analyst **20 minutes to find by hand.** Surfaced in 40 seconds
- Answer: *"Rate rose 14.0%, volume fell 3.1% — the move is rate, not mix."* Four checkable claims, then sign-off, then one exported file

`visual:` the amber hop — the actual verification line as the analyst sees it

## Slide 8 — Verification by decomposition, corroborated by the strongest incumbent

- After every handoff: row-count reconciliation, grain assertion, anti-join coverage, null-rate delta, boundary totals — **cheap SQL, never the model checking itself**
- Databricks reached the same conclusion independently: *Inspect* authors smaller SQL statements to verify aspects of a generated query and regenerates `[S32]`
- We decline reflection, self-critique and LLM-as-judge on principle — **all keep verification inside the model that produced the output**
- The intellectual ancestor is financial audit: **the workpaper, not the number, is the deliverable**

`visual:` render of `tech/architecture/D02_verify_replan_loop.md`

## Slide 9 — The honest arithmetic is ≈2.9×, and on familiar single-source questions it is 1.0×

- A representative multi-source question: **90 minutes → 31 minutes. ≈2.9×, band 1.8×–4.2×** `[S15]`-anchored, decomposed in [tech/whitepaper.md](../tech/whitepaper.md) §5
- **Cross-source reconciliation is the big one at 4.0×** — the one thing no incumbent will attempt
- The staff data scientist reviewing someone else's work: **2 hours → 19 minutes**, from lineage alone
- **On a single-source, familiar, well-modelled question the gain is ≈1.0× or below — the analyst should keep writing SQL, and we say so**
- **This is not a 10× claim and we do not make one.** The queueing effect is larger and we decline to quote it, because induced demand will consume it

`visual:` the friction decomposition — six frictions, four attacked, with the conservative and optimistic corners shown

## Slide 10 — The addressable market is $123M, built bottom-up, and we are not calling it bigger

- **≈1.24M beachhead analysts globally**, from BLS occupational data `[S69][S70]` plus three tagged assumptions
- At **$75/analyst/month** — top of the observed analyst-tool band `[S44][S52]` — **TAM $1.1B, SAM $123M**
- Pessimistic corner: **$38M.** Sensitivity table published rather than buried
- **A "1% of a $40B BI market" slide would contradict our own market-type analysis.** This is a niche analyst tool and the number reflects that
- Monetisation is out of scope for 295A/295B — **capstone SOM is $0** `[A1]`

`visual:` the bottom-up build, one sourced factor and three tagged assumptions, with the sensitivity corners

## Slide 11 — At a $900 ACV only zero-CAC channels survive, so we ship open source

- Open-core, self-hostable: runs in the customer's environment on their own model key
- **Outbound would need a 4–9 seat account just to repay acquisition.** Resellers, field sales and paid acquisition are ruled out by arithmetic, not preference
- The compounding loop: an analyst installs → runs a real investigation → **the exported artifact is shareable and checkable** → a colleague installs
- Wren AI proves the channel carries a product of this shape: **13,000+ stars, 10,000+ cloud users** `[S50]`
- **Adoption precedes revenue structurally.** We say that rather than modelling a funnel we do not have

`visual:` the compounding loop, with the exportable investigation as the edge that closes it

## Slide 12 — This does not become a Databricks feature, because the value is in spanning

- **Sisu Data raised ≈$128.7M attacking the highest-value part of this loop and became a Snowflake division** `[S56][S57]`. Narrative Science was folded into Tableau `[S58]`. Neither failed technically
- A warehouse feature that treats Postgres, a file and a REST API as equal peers **is a feature arguing against its own vendor's gravity**
- Cross-source neutrality is the answer, and **self-hosted open source is what makes it a property rather than a claim**
- **The residual, stated:** if a real customer's questions all live in one warehouse anyway, this argument is true and worthless. That is the first thing discovery tests

`visual:` the petal diagram — five adjacent markets, with which budget each customer actually comes from

## Slide 13 — Our evidence is thin, and the one number that matters is untested

- **No customers, no revenue, no accuracy measurement yet.** Stating otherwise would make this the graveyard's next entry
- The 295A deliverable is a **published multi-hop accuracy number on a fixed question set** — something **no commercial agentic-BI product publishes** `[S1]`-class baseline: DABstep Hard ≈15% `[S4]`
- **The claim the whole thing rests on is untested:** can an analyst accept an answer they did not derive faster than deriving it?
- The beachhead's own objection: *"I read SQL faster than I read explanations."* **That is correct as stated**
- One afternoon, five analysts, a timed task settles it — and it precedes further building

`visual:` the three untested claims, ranked by how much of the strategy each can invalidate

## Slide 14 — What we are asking for is ten analysts and one heterogeneous stack

- **Not funding.** Monetisation is out of scope for the capstone `[A1]`
- **Ten analysts, one hour each** — can you accept an answer you did not derive faster than you could derive it?
- **One heterogeneous stack** to test against: a warehouse, an operational database, and a file feed
- **Advisor challenge on the two research risks:** the planner's accuracy on real schemas, and whether cheap structural checks catch the failures that actually matter
- Team edge: agent and LLM engineering — **hands-on orchestration and the failure modes of multi-step agent systems**, which is exactly where the riskiest assumption lives

`visual:` the 295A/295B timeline — harness first, then the narrow path, then the published number

---

## Speaker notes on the arc

**Slides 1–4 are the teardown and they take a third of the time.** Credibility here is earned by demonstrating you know why everything else falls short — the architecture then reads as the obvious recombination rather than as a proposal. Do not rush to the product.

**Slide 5 is the hinge.** The ≈15% figure looks like an argument *against* the venture and is the argument *for* it. If the room does not follow the inversion, nothing after it lands.

**Slides 9, 10 and 13 are where a normal deck inflates and this one concedes.** That is deliberate and it is the deck's strongest asset in an advisor review: an audience that has watched three slides decline to overclaim will believe slide 6.

**Two numbers must never appear**, and both are tempting:
- The **13.8× queueing multiplier** from [tech/whitepaper.md](../tech/whitepaper.md) §3.1 — computed and withdrawn there because induced demand consumes it.
- Any **head-to-head accuracy claim** against Genie, Cortex or Copilot. None publishes a benchmark, so no comparison is supportable.
