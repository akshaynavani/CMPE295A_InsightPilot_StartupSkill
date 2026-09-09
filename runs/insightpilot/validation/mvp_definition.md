# MVP definition — two of them, kept distinct

**What this is** — The two minimum viable products, deliberately separated: a **low-fidelity** artifact that tests whether the *problem* is real, and a **high-fidelity** one that tests whether the *solution* would be adopted. Plus the earlyvangelist definition — the five things a person must already have done to count as one.
**Why it exists** — Collapsing these two into one "MVP" is the most common and most expensive error available here, because the low-fidelity test costs about six founder-hours and can invalidate the high-fidelity one entirely. This file exists to stop a semester of engineering from starting before an afternoon of measurement has run.
**How to read it** — §1 is the one that matters and it is not software. A skeptic should attack §1's claim that a static artifact can measure the pack's central premise, and §4's earlyvangelist criteria for being too strict.
**Depends on / feeds** — Tests E1 and E2 from [experiment_board.md](experiment_board.md); scoped from [product/features_prioritized.md](../product/features_prioritized.md) Now tier. Feeds [stage_gate.md](stage_gate.md) G3/G4 and the 295A plan.

---

## 1. Low-fidelity MVP — the paper investigation

> **A single static, hand-built exported investigation artifact, plus a stopwatch.**

**No software. Buildable in a day.**

### What it is

One realistic multi-source question — the carrier-cost question from the beachhead journey — worked through **by hand**, and formatted exactly as the system's exported investigation would be: the question, the analysis plan as six numbered steps, each hop with its actual SQL and row counts in and out, the verification results including one amber coverage warning, the established facts, the doubt block, and a sign-off line.

Produced in three variants: one **correct**, and three containing planted defects (wrong join grain, wrong region mapping, wrong time-window filter) for the E2 session.

### The question it answers

> **Can an analyst reach a confident accept-or-reject on an answer they did not derive, faster than they could derive it — and do they catch it when it is wrong?**

That is E1 and E2, and it is the single premise everything else in the pack rests on.

### What it deliberately omits

Everything. No orchestrator, no agents, no connectors, no UI, no model calls. **The artifact is a document, and the entire test is what a human does with it.**

That omission is the design: if verification is cheaper than re-derivation, it is cheaper because of *the artifact's structure*, not because of the software that generated it. Building the software first would test the same claim twelve weeks later at a hundred times the cost.

### The result that falsifies it

- **Median verification cost ratio > 0.8** → the differentiator is void. Trigger T1: stop and publish the negative result.
- **Seeded-defect rejection < 50%, or no lift over an answer-plus-SQL control** → worse. The trace is comfortable rather than effective, and would ship confident wrong answers wearing an audit trail. Trigger T3.

### Why this is the right low-fidelity test and a landing page is not

The instinct at this stage is a landing page measuring sign-ups. That would measure whether the *pitch* is appealing, which is not in doubt and is not the risk. **The risk is behavioural and specific: does reading a trace actually cost less than doing the work.** Only a timed task with a real analyst and a real artifact answers it, and a document is sufficient.

## 2. High-fidelity MVP — the narrow path

> **One question type, two source types, end to end, with the harness measuring it.**

**This is the 295A engineering scope** ([product/features_prioritized.md](../product/features_prioritized.md) Now tier, #1–#18).

### What it is

| Included | Why |
|---|---|
| Evaluation harness + 30–50 question fixed set | Feature #1. Without it nobody can say whether any of the rest works |
| Seeded-error set | Feature #2. The only instrument for silent-error rate |
| Postgres connector, read-only | The substrate |
| CSV/Excel via DuckDB | **The unmodelled source — the case no incumbent attempts** |
| Orchestrator: plan generation, shown and approved before execution | The mechanism, plus the cheapest error catch |
| Fetch + Analytics agents | Enough to answer a real question |
| Ambiguity interception + binding store | Attacks 81.2% of the failure mass `[S2]` |
| Per-hop verification, six structural checks | The verify beat |
| Hop-level lineage + single-hop re-run + **exportable investigation** | The differentiator's surface |
| Doubt surfacing; audit log | P3; Tom's veto condition |

### What it deliberately omits

| Omitted | Why |
|---|---|
| **Visualization agent** | A table is an acceptable answer. Charts are the most demo-visible and least evidence-bearing thing available |
| **REST connector** | Postgres + CSV already demonstrates heterogeneity; a third source proves nothing new about the mechanism |
| **ML agent** | Largest single build in the backlog, and A2 already establishes it is not the differentiator |
| **Override re-flow** | Degrades to invalidate-and-replan, which is the honest fallback anyway |
| **Semantic-layer consumption** | 295B. Important for the buyer conversation, not for the core premise |
| **Any polish** | The output is a measurement, not a demo |

### The question it answers

> **Does multi-hop planning across heterogeneous sources reach usable accuracy on a narrow path, and do cheap structural checks catch the failures that matter?**

E6 and E7 — the two engineering risks named as research risk in [tech/not_vaporware.md](../tech/not_vaporware.md) §4.

### The result that falsifies it

- **Multi-hop execution accuracy < 30%** → the architecture's mitigations do not overcome the field's baseline. Narrow to two-hop questions and publish the low number (T6).
- **Verifier catches ≈0% of the semantically-plausible defect class** → the verifier catches mechanical, not semantic, failures. Say so, and make the shown-plan gate the primary defence (T7).

### What "viable" means here

Not "usable by a customer." **Viable means: it produces a number that is true, publishable, and re-runnable by someone else.** No commercial agentic-BI product publishes an accuracy figure ([research/sources.md](../research/sources.md), *Named gaps* 2), so a working, measured, narrow system is a stronger artifact than a broad, unmeasured demo.

## 3. Why the order is non-negotiable

```
Week 1–4   LOW-FIDELITY   ~6 founder-hours, no code   → E1, E2
                │
                ├── FAIL (ratio > 0.8) ──→ STOP. Publish the negative.
                │                          Do not build the high-fidelity MVP.
                ▼
Week 5–16  HIGH-FIDELITY  a semester of engineering   → E6, E7
```

**The low-fidelity MVP can invalidate the high-fidelity one, and not the reverse.** If verification costs as much as re-derivation, a more accurate planner does not help — the analyst still cannot use an answer they did not derive.

This is the uncomfortable implication [stage_gate.md](stage_gate.md) §5 also reaches: **the correct first month of a build project contains almost no building.**

## 4. Earlyvangelist definition

The five things a person must **already have done** — past behaviour, not stated interest. Someone meeting fewer than five is a friendly conversation, not a design partner.

An earlyvangelist for this product has:

1. **Written SQL against a production source in the last week** to answer someone else's ad-hoc question.
2. **Hit a wall with an existing copilot or NL-query feature** — tried Genie, Cortex, Copilot, Spotter or similar, and abandoned it for a specific reason they can name.
3. **Worked around a missing data source** — manually reconciled a file, an export or an API against a warehouse, and can say how long it took.
4. **Been burned by an unverified number** — shipped or received an answer that turned out wrong, and remembers what happened.
5. **Installed an open-source data tool themselves** without procurement — dbt, DuckDB, Metabase, Superset or similar.

**Why each criterion is load-bearing.** (1) establishes the queue. (2) establishes that the obvious alternative was tried and failed — they are not comparing against nothing. (3) establishes multi-source reality at the individual level, which is E3 asked one person at a time. (4) supplies the trigger; without a burn, verification is abstract. (5) proves they can adopt without a purchase order, which is the only channel with viable economics.

**Criterion 5 is the one that will disqualify the most people, and it is not negotiable.** At a $900 ACV, a user who needs procurement to try something cannot be reached by any channel this venture can afford ([strategy/channel_plan.md](../strategy/channel_plan.md) §4).

**Criterion 4 is the one most likely to be fudged.** "I worry about accuracy" is not it. The question is *"tell me about the last time you sent an answer that turned out to be wrong"* — and if there is no story, the pain is theoretical.

## 5. What neither MVP tests

Stated so the gaps are not mistaken for coverage.

1. **Whether anyone pays.** Out of scope (A1). The budget question is E4, a conversation, not an MVP.
2. **Whether the flywheel compounds.** R10 needs 90+ days of real use; no MVP reaches it.
3. **Whether the review gate scales.** A12/E5 needs multiple stakeholders submitting to one analyst over weeks. The high-fidelity MVP has one user.
4. **Whether the security posture passes a real review.** Tom's approval needs a real deployment in a real environment, and the audit log and self-hosted topology are built for it but untested against it.

## Recommended next 3

1. **Build the low-fidelity artifact this week.** One day of work, and it gates a semester of engineering. There is no cheaper decisive test in the pack.
2. **Screen every design partner against all five earlyvangelist criteria and record which they fail.** The failures are data: if nobody meets criterion 3, E3 is already answered and the multi-source thesis is in trouble.
3. **Write the high-fidelity omission list into the 295A plan as an explicit non-scope section.** Charts and the ML agent will be the two things most tempting to add mid-semester, and both are on the pre-decided cut list for reasons that will feel weaker in week eight than they do now.
