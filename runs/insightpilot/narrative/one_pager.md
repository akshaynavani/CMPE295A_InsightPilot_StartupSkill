# InsightPilot — one page

**What this is** — The single page: what it is, the problem with its sharpest sourced number, the mechanism, why now, the evidence, the market, the team edge, and the ask.
**Why it exists** — This is the artifact handed to an advisor, a design partner or a reviewer who will give the project ninety seconds. It exists because a pack of forty-four documents has no front door for a stranger, and because the temptation at this layer is to reach for the biggest number in `tech/` rather than the most defensible one. Every figure below traces to [research/sources.md](../research/sources.md).
**How to read it** — Top to bottom, once. A skeptic should attack *Evidence* — it is deliberately thin, because the project has no customers yet and says so.
**Depends on / feeds** — Arranges [strategy/positioning.md](../strategy/positioning.md) §5, [tech/whitepaper.md](../tech/whitepaper.md) §5, [research/survey.md](../research/survey.md) §6, [strategy/market_sizing.md](../strategy/market_sizing.md). Invents nothing.

---

## InsightPilot

**An Agentic Platform for Conversational Business Intelligence**

**Conversational BI for enterprise data analysts that turns a business question into a planned, executed and fully traceable analytical workflow.**

---

### The problem

An enterprise analyst's ad-hoc question takes **one to four weeks** to come back `[S15]`. So people stop asking: **76% of businesses have made a decision without consulting data because it was too hard to get** `[S15]`.

The obvious fix — put a chat box on the warehouse — has been tried by every major vendor, and it has a specific failure. **Schema-level errors, wrong column and wrong meaning, are 81.2% of analysed text-to-SQL failures** `[S2]`, and *"failure looks like a plausible but incorrect answer"* `[S2]`. That is why **71% of data practitioners name hallucinated output reaching stakeholders as a top concern** `[S16]`, and why trust in data as a stated priority jumped from 66% to 83% in a single year `[S16]`.

**The market's problem is not that answers are slow. It is that fast answers are not yet trustworthy.**

### What we do

An Orchestrator turns a question into an **analysis plan**, shows it before running anything, and dispatches it to four specialist agents — Data Fetch, Analytics, Visualization, ML — across the analyst's *real* sources: the warehouse, the operational Postgres, and the carrier CSV nobody has ever modelled.

Every handoff emits its own **lineage**: the source touched, the query run, the transform applied, the row counts in and out. Each hop is separately inspectable and re-runnable, and the whole investigation exports as one self-contained file.

**The unit is the investigation, not the query — and it ships with a trace that makes verification cheaper than re-derivation.**

### Why now

- **Tool access standardised.** MCP shipped 2024-11-25 and was adopted by OpenAI, Google, Microsoft and AWS within thirteen months, then donated to the Linux Foundation `[S62]`. A pluggable connector layer became a configuration problem rather than bespoke engineering per source.
- **Agentic tool-use became reliable enough to build and measure — not to trust unverified.** Multi-step data reasoning still measures ≈15% on hard real-world tasks `[S4]`. **That is precisely why the trace is load-bearing rather than cosmetic**, and why the 295A spike tests one narrow path.

### Why the incumbents cannot follow

Every incumbent buys correctness by bounding scope before the question is asked: **Databricks Genie caps at 30 tables per agent** `[S32]`, **Snowflake Cortex Analyst runs on a hand-authored ~32K-token YAML model** `[S36]`, **Power BI Copilot cannot compute a metric that is not already a measure** `[S42]`.

Those are not bugs. They are the reliability mechanism. **The better the guardrail, the narrower the set of questions attempted — and an ad-hoc question is by definition the one nobody anticipated.**

### Evidence — thin, and honestly so

No customers. No revenue. What exists:

- A **mechanism arithmetic** that decomposes a representative multi-source question at **90 minutes → 31 minutes, ≈2.9× (band 1.8×–4.2×)** — and **≈1.0× or below on single-source familiar questions, where the analyst should keep writing SQL** ([tech/whitepaper.md](../tech/whitepaper.md) §5).
- A **buildable stack** with two components named as research risk rather than hidden ([tech/not_vaporware.md](../tech/not_vaporware.md) §4).
- The 295A deliverable: **a published multi-hop accuracy number on a fixed question set.** No commercial agentic-BI product publishes one ([research/sources.md](../research/sources.md), *Named gaps* 2).

### Market

Bottom-up from BLS occupational data `[S69][S70]`: **≈1.24M beachhead analysts globally, ≈74,600 in the US** meeting the day-one criteria. At $75/analyst/month — the top of the observed analyst-tool band `[S44][S52]` — **TAM $1.1B, SAM $123M**, pessimistic corner $38M.

**This is a small market by venture standards, and the pack says so** ([strategy/market_sizing.md](../strategy/market_sizing.md) §5.2). It is more than sufficient to justify a two-semester build.

### Team edge

Agent and LLM engineering: hands-on orchestration, tool-calling loops, and the failure modes of multi-step agent systems — which is exactly where the riskiest assumption lives.

**The team has no lived experience inside an enterprise analytics function.** The problem statement is researched, not lived, and every number on this page is sourced rather than asserted for that reason.

### The ask

Not funding — monetisation is out of scope for CMPE 295A/295B ([ASSUMPTIONS.md](../ASSUMPTIONS.md) A1). Three things:

1. **Ten analysts for one hour each.** Specifically: can you accept an answer you did not derive faster than you could derive it? That single question decides the venture, and it is untested.
2. **One heterogeneous stack to test against** — a warehouse plus an operational database plus a file feed.
3. **Advisor challenge on the two research risks**: the planner's accuracy on real schemas, and whether cheap structural checks catch the failures that actually matter.

### The riskiest thing about this

> **If verifying an answer costs as much as writing it, this product is a slower way to get where the analyst was going anyway.**

The beachhead's own words: *"I read SQL faster than I read explanations."* That objection is correct as stated, it is unmeasured anywhere in the literature, and everything above depends on the answer.
