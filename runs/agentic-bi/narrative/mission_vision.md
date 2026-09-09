# Mission, vision and values

**What this is** — The mission (true today, one sentence), the vision (the world in ten years if this works), five values each stated as a **trade-off the company will actually make**, and why the company exists.
**Why it exists** — [strategy/positioning.md](../strategy/positioning.md) defines this venture *against* competitors; that definition evaporates the day Databricks changes its roadmap. This file is what survives their disappearance. It also exists to make the values falsifiable: a value phrased as a virtue ("we believe in transparency") costs nothing and predicts nothing, whereas a value phrased as a trade-off can be checked against the decisions already in the ledger.
**How to read it** — The values are the substance; each names what is given up. A skeptic should attack §3 by testing each value against a decision the pack has already made — if a value has no matching decision, it is decoration.
**Depends on / feeds** — Consistent with [BRIEF.md](../BRIEF.md), [ASSUMPTIONS.md](../ASSUMPTIONS.md) A1–A5, and [tech/whitepaper.md](../tech/whitepaper.md) §5. Feeds every other narrative artifact and any hiring or contribution guidelines.

---

## 1. Mission

> **We make an analytical answer something you can check in seconds instead of something you have to trust.**

True today, and the whole of it. Not "democratise data" — the analyst is not being democratised, they are being given back the hour that verification currently costs. Not "AI for analytics" — the AI is a means and the market is full of it. The mission names the thing that is actually different: **the cost of checking.**

## 2. Vision

> **In ten years, an analytical answer that arrives without its trace looks the way an unaudited financial statement looks now: not wrong, but not usable for anything that matters.**

This is a claim about a **norm**, not about market share. The strongest available version of success is that the practice outlives the product — that "what is your verification cost ratio" becomes a question people ask their vendors, including vendors that are not us.

It is deliberately not "every company runs Agentic BI." With an open-source core, the code is not the asset ([ASSUMPTIONS.md](../ASSUMPTIONS.md) A3), and a vision of exclusive ownership would contradict the licensing decision already made.

## 3. Values — five trade-offs

Each states what is given up. Each is checked against a decision already in the pack, because a value with no matching decision is decoration.

### 3.1 Publish the number that makes us look worse

**The trade-off: we lose the impressive headline to keep the credible one.**

The mechanism arithmetic came to **≈2.9×, not 10×**, and we published it with its band and its conservative corner. We computed a **13.8× queueing effect and withdrew it**, because induced demand will consume it. We state that on a single-source familiar question the gain is **≈1.0× or below and the analyst should keep writing SQL.**

*Already decided:* [tech/whitepaper.md](../tech/whitepaper.md) §3.2 and §5. *What it costs:* every pitch is less exciting than the one a competitor can give.

**Why we accept it:** the graveyard in this category was filled by overpromising. Watson Analytics's documented failure was overpromise versus delivery `[S60]`, and Power BI Q&A shipped inside the most widely deployed BI tool on earth and still retired `[S40]`. In a market that has been disappointed four times, the scarce asset is a claim that survives being checked.

### 3.2 Refuse the question rather than guess at it

**The trade-off: we are slower and more annoying than a system that just answers.**

When a term resolves to more than one column or grain, the system **halts and asks** instead of taking the best guess. On a first encounter with a source, this makes us *slower* — measurably, ≈0.85× — before it ever pays back.

*Already decided:* the margin-thresholding gate, [tech/deep_dives.md](../tech/deep_dives.md) §1. *What it costs:* a worse demo, and a first session that feels like an interrogation.

**Why we accept it:** schema-level errors are **81.2% of analysed text-to-SQL failures** `[S2]`, and *"failure looks like a plausible but incorrect answer"* `[S2]`. A silent guess samples directly from the dominant failure distribution, and the user has no way to detect it.

### 3.3 Verify with different code, never with the model that produced the answer

**The trade-off: we decline the most fashionable techniques in our own field.**

Reflection, self-critique, LLM-as-judge and multi-agent debate are all declined on one principle: they keep verification inside the thing being verified. Our checks are plain SQL — row counts, grain assertions, coverage, boundary totals.

*Already decided:* [tech/techniques/wave3.md](../tech/techniques/wave3.md) §1, five explicit declines. *What it costs:* we look less sophisticated to an audience that expects to hear those words.

**Why we accept it:** a model asked to check its own output shares the failure that produced it. Databricks reached the same conclusion in production `[S32]`. The side benefit is economic — verification consumes **zero model tokens**, so the differentiating mechanism is the cheapest thing in the system.

### 3.4 The person who cannot verify does not get to ship unverified

**The trade-off: we renounce the largest revenue segment in our category.**

A business stakeholder can ask anything and gets an answer in ninety seconds. They **cannot export it** without an analyst's sign-off. We are not building self-service for people who cannot judge correctness.

*Already decided:* [product/PRD.md](../product/PRD.md) non-goal 1; the sign-off gate. *What it costs:* the whole non-technical market — where the category's revenue and attention are.

**Why we accept it:** ThoughtSpot is the purest test of the opposite bet and cleared a **73.67% markdown** in a June 2024 secondary against its Series F `[S46]`. And the honest version is simpler: an answer someone cannot check, put in front of their boss, is a person set up to be wrong in public. **Gating it is not paternalism — the alternative is that they guess, which 76% of businesses already do** `[S15]`.

### 3.5 Consume what the customer already built; do not replace it

**The trade-off: we depend on artifacts we do not control.**

Where a dbt or Cube semantic layer exists, its definitions **take precedence outright** over anything we infer. We will not become the place metric definitions live.

*Already decided:* the hard precedence edge in [tech/architecture/D07](../tech/architecture/D07_connectors_ecosystem.md). *What it costs:* deeper dependence on tooling maintained for someone else's product, and a smaller surface to sell.

**Why we accept it:** 59% of large enterprises are already funding semantic layers `[S17]`. Telling a buyer the thing they are currently funding is unnecessary loses the deal and is also false — a semantic layer says what a metric *means*; it does not say what happened, why, or what was done to find out. **They are complements. Requiring one would inherit exactly the bounded-scope failure we are built against.**

## 4. Why we exist

Because the industry answered the wrong question.

Asked to make enterprise data accessible, every serious vendor built a system that answers **faster**. The measured evidence says speed was not the binding constraint: trust in data as a stated priority went from 66% to 83% in a single year `[S16]`, **71% of practitioners fear hallucinated output reaching stakeholders** `[S16]`, and the money is moving toward semantic layers to constrain AI output `[S17]`. Meanwhile roughly **25% of employees use the BI tools their employer bought, flat across seven years** `[S22]`.

A faster answer nobody will stake their name on is not an answer. It is a thing you have to go and check, which is the work you were trying to avoid.

**We exist to make checking cheap.** That is a smaller ambition than most companies in this category state, and it is the one the evidence supports.

---

## 5. What would make us abandon this

Stated because a mission that cannot be falsified is a slogan.

**If verification turns out to cost as much as re-derivation, this mission is unachievable and we should say so publicly rather than continue.** The beachhead's own objection is *"I read SQL faster than I read explanations,"* it is correct as stated, and it is untested. One afternoon with five analysts settles it.

**Publishing that negative result would be more consistent with §3.1 than quietly pivoting to a faster chat box.** It would also still be a good capstone: the field currently has no public measurement of verification cost either way.
