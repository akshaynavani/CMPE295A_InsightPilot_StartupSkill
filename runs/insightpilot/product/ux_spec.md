# UX specification — the twelve key screens

**What this is** — A text specification of the twelve screens that carry the product: purpose, primary action, information hierarchy, empty/loading/error states, and the micro-interactions that produce the feel. Visual treatment belongs to `startup-visuals` (deferred, ASSUMPTIONS A4).
**Why it exists** — The differentiator is a *beat* — Verify — and beats live or die in interface. [PRD.md](PRD.md) P3 says failure looks plausible, and P5 says verification cost is the adoption gate; both are UX problems before they are engineering problems. The specific failure this prevents: shipping lineage as a collapsible JSON blob that satisfies the word "traceable" and delivers none of the value, which is what every incumbent's "show the SQL" already is.
**How to read it** — Screens 5, 7 and 8 are the product; the rest support them. A skeptic should attack §5's verification tick treatment, which must convey *"these structural checks passed"* and never *"the answer is right"*, and §14, which lists the three places this spec is most likely to be wrong.
**Depends on / feeds** — Features by number from [features_flagship.md](features_flagship.md) and [features_prioritized.md](features_prioritized.md); adaptive-surface requirement from [PRD.md](PRD.md) §4; the four [journeys](journeys/). Feeds `tech/` component design and the deferred visuals phase.

---

## 0. Three rules that govern every screen

1. **One adaptive system, no tiers.** Marcus and Priya see the *same* screens. Three things adapt: what renders expanded by default, whether ambiguity is phrased in business terms or column names, and whether export is gated on sign-off. There is no "business edition" — PRD §4.
2. **Never present confidence as accuracy.** P3. No percentage scores, no "94% confident." The system reports *what it checked* and *what it is unsure about*, which are different claims.
3. **Doubt is more prominent than reassurance.** An amber verification result outranks a green one in the visual hierarchy. A product whose failures are quiet is the failure mode the whole pack is built against.

---

## 1. Investigation surface *(Ask, Follow up)*

**Purpose.** Start or continue an investigation. The durable home of a question and everything established while answering it.

**Primary action.** Type a question.

**Hierarchy.** (1) Question input, full width, no chrome. (2) Investigation title and the established-facts strip — two or three confirmed claims from earlier turns, e.g. *"cost per shipment = billed/distinct shipments · region mapping confirmed."* (3) Turn history, collapsed to answers with plans hidden. (4) Source scope chips. (5) Investigation list in a sidebar.

**States.**
- *Empty:* one input, one line of guidance, and **three example questions drawn from the connected sources' actual table names** — not generic samples. First-run credibility depends on the system already knowing something about their data.
- *Loading:* n/a — this screen does not load, it hands off to screen 4 or 5.
- *Error (no sources connected):* becomes a connector setup prompt. Do not show an input that cannot work.

**Micro-interactions.** Established facts are clickable and jump to the hop that established them. The sidebar shows verified-fact count per investigation, not message count — *"4 questions, 2 verified facts"* tells an analyst what is reusable.

## 2. Clarification *(Ambiguity interception, #11)*

**Purpose.** Stop before planning when a term resolves to more than one column, grain or time basis. **The single highest-leverage screen in the product** — it attacks the 81.2% of failures that are schema-level `[S2]`.

**Primary action.** Choose a resolution.

**Hierarchy.** (1) The ambiguous term, quoted from the question. (2) Candidates as cards — each with the column or expression, row count, date range, and a three-row sample. **The evidence is what makes this a decision rather than a coin flip.** (3) "None of these" escape, which routes to manual definition.

**Adaptive rule.** For an analyst: column names and expressions. For a stakeholder: business phrasing — *"deals whose close date moved"* vs *"deals that missed their forecast quarter"* — with the technical detail behind a disclosure. Same screen, different default depth.

**States.**
- *Empty:* n/a — never renders without candidates.
- *Error (nothing resolves):* *"I can't find anything in your sources that matches 'slippage'"* plus the closest matches by name similarity, and an offer to define it. **Failing to resolve must never silently become a guess.**

**Micro-interactions.** Hovering a candidate previews sample rows inline. Choosing one animates it into a binding chip on screen 3 — showing the user they have just taught the system something durable.

## 3. Vocabulary bindings *(#12)*

**Purpose.** Make resolved terms visible and correctable, and show that corrections persist.

**Primary action.** Edit a binding.

**Hierarchy.** (1) Chip row above the plan: `cost per shipment = SUM(carrier_invoice.total_usd) / COUNT(DISTINCT shipment.id)`. (2) Provenance on each chip: *confirmed by Priya, Aug 14* · *from your dbt semantic layer* · *inferred, unconfirmed*. (3) Expanded editor on click.

**The three provenance states are load-bearing.** A binding from dbt carries the organisation's authority `[S66]`; one confirmed by an analyst carries theirs; an inferred one carries none and must look like it. A stakeholder's choice (Marcus, [journeys/edge_low.md](journeys/edge_low.md) beat 4) is stored **unconfirmed** and visibly so.

**States.** *Empty:* no chips — acceptable for a trivial question. *Error:* a binding that no longer resolves (schema changed) renders struck-through with *"column no longer exists"* — the 24-point schema-evolution failure `[S2]` made visible instead of silent.

**Micro-interactions.** Editing a chip shows a one-line diff and *"this will apply to future questions across your team"* — making the flywheel legible at the moment of contribution.

## 4. Analysis plan review *(#6)*

**Purpose.** Show the plan before anything executes, so errors cost an edit rather than a query.

**Primary action.** Approve, or edit and approve.

**Hierarchy.** (1) Numbered steps, each one line: verb, agent, named source. *"3. Join shipments to carrier invoices on region+month — Analytics agent."* (2) Hop count with the compounding note when above the ceiling (#26). (3) Cost and latency estimate (#34). (4) Approve, prominent. (5) Per-step edit and delete affordances.

**The fifteen-second constraint.** [journeys/beachhead.md](journeys/beachhead.md) assumes Priya reads a six-step plan in about fifteen seconds. **That is a design budget, not an observation** — one line per step, no nesting, no prose. If a step needs a paragraph, the plan is too complex and #26 should have flagged it.

**Adaptive rule.** Renders **collapsed** for stakeholders — *"4 steps across 2 sources"* — expandable but not demanded.

**States.**
- *Empty:* n/a.
- *Loading:* plan generation is the one genuinely slow pre-execution step; show the steps streaming in as they are decided rather than a spinner.
- *Error:* *"I can't plan this with your connected sources"* plus what is missing. **Never produce a degraded plan silently.**

**Micro-interactions.** Deleting a step shows what downstream steps depend on it before confirming. Approval is per-source on first run only — never a modal on every question.

## 5. Execution with per-hop verification *(#13, #17)*

**Purpose.** Show work happening and surface failures the moment they occur — not at the end.

**Primary action.** Watch, or intervene on an amber hop.

**Hierarchy.** (1) The plan from screen 4, now live, each step gaining a state. (2) **Verification results inline per step**, in plain language with numbers: *"✓ join preserved row count (14,201 → 14,201)"* · *"⚠ 8% of shipments had no matching invoice"*. (3) Running elapsed time. (4) Cancel.

**Verification tick treatment — the most consequential detail in this spec.** A green tick must read as *"these specific structural checks passed"* and never as *"this step is correct."* Enforced three ways: the tick is **always accompanied by the named check and its numbers**, never standing alone; hovering states what was *not* checked; and amber outranks green in weight, colour and position. Dr. Chen read them correctly ([journeys/edge_high.md](journeys/edge_high.md) §5.2) — **a less careful reviewer must be unable to read them wrongly**, and that is a UX obligation, not a documentation one.

**States.** *Loading:* this screen *is* the loading state — which is why execution is shown step-wise rather than behind a progress bar. *Error (hop fails):* the step goes red, execution halts, and replanning (#20) is offered with a diff. **Failure is a first-class state with its own affordance, not an error toast.**

**Micro-interactions.** An amber verification is immediately clickable into screen 7 — the gap between noticing a problem and inspecting it should be one click and no navigation.

## 6. Answer *(#27, #13, #24)*

**Purpose.** Deliver the answer with its established facts and its doubts, in a form defensible to a third party.

**Primary action.** Accept, inspect, or send for review.

**Hierarchy.** (1) **Sign-off state banner** — amber *"not yet reviewed by an analyst"* or green *"reviewed by Priya Raghunathan, 11:21."* Above everything, because it governs what may be done with what follows. (2) The answer as **established facts**, several checkable claims rather than one summary: *"Cost per shipment rose 11.4%. Volume fell 3.1%. Rate rose 14.0%. The move is rate, not mix."* (3) **Doubt block** — least-certain hops and why. (4) Chart, if one earns its place (#22). (5) Actions: inspect lineage, export, sign off, ask a follow-up.

**Why doubt sits above the chart.** P3. The chart is the most persuasive element and the least informative about correctness; putting doubt beneath it would let the persuasive thing win.

**States.** *Empty (no result):* *"The plan ran but returned no rows"* with the hop where data ran out — an empty answer is a finding, not a failure. *Error:* execution failed; retain partial lineage, since a half-finished investigation is still evidence.

**Micro-interactions.** Each established fact links to the hop that produced it. Export is disabled with an explanatory tooltip when unreviewed and the user cannot sign off — never a silent disabled button.

## 7. Hop detail — the lineage inspector *(#10, #14)*

**Purpose.** Let someone check the one hop they doubt, in seconds. **This is the differentiator's surface.**

**Primary action.** Read the query; re-run it.

**Hierarchy.** (1) What this hop did, one sentence. (2) **The actual query or transform, syntax-highlighted, copyable** — no paraphrase, no summary. (3) Row counts in and out, grain in and out. (4) Verification checks performed, each named with its result, **and what was not checked**. (5) Re-run this hop. (6) Override this hop. (7) Inputs — which upstream hops fed it.

**The forty-second budget.** [journeys/beachhead.md](journeys/beachhead.md) beat 9 assumes Priya diagnoses a bad join in forty seconds. That requires the query visible without scrolling and counts adjacent to it. **No accordion, no tabs, no "view details."**

**States.** *Loading (re-run):* show the previous output alongside, so the diff is the point. *Error (re-run fails):* *"Re-running now fails — the source changed"* with a diff of what changed. **This is a valuable finding, not an error condition**, and should read as such.

**Micro-interactions.** Re-run diffs old against new and highlights any changed number. Copying the query copies it runnable, with resolved parameters — so an analyst can paste it into their own editor, which is the escape hatch that makes the whole thing trustworthy.

## 8. Override editor *(#21, #40)*

**Purpose.** Correct a hop and push the correction downstream and into the organisation's memory.

**Primary action.** Edit and re-flow.

**Hierarchy.** (1) The hop's current query or method, editable. (2) **Impact preview: which downstream hops will re-run, and which will be invalidated.** (3) Annotation field with a type selector — *data-provenance issue* · *wrong join* · *wrong grain* · *business-rule correction*. (4) Persist-to-bindings toggle, default on, with *"applies to future questions across your team."* (5) Apply.

**The honest failure mode, specified rather than hidden.** When an override changes grain, downstream assumptions may not survive re-flow. **The system must say so and offer replanning instead of silently re-running into nonsense**: *"Changing the grain here invalidates steps 4–6. Re-plan from step 4?"* Feature #21's flagged weak point ([features_flagship.md](features_flagship.md) #17) is made explicit here so it cannot degrade into "re-run everything and hope."

**Why the annotation type matters.** Dr. Chen's April ticketing migration ([journeys/edge_high.md](journeys/edge_high.md) beat 10) is not a model error — it is a fact about the world. Typing it separates *the system got it wrong* from *the data does not mean what it appears to mean*, and only the second kind should teach the bindings store a permanent lesson.

**States.** *Error:* invalid SQL is caught before apply, against the source, with the message inline.

## 9. Exported investigation artifact *(#15)*

**Purpose.** One self-contained readable file: the differentiator's proof, the GTM loop's edge, Angela's provenance record, and O2's measurement instrument. **Four jobs, one artifact.**

**Not a screen in the product — a document that opens without it.** That is the requirement.

**Hierarchy.** (1) Question and asker, date. (2) Sign-off state and reviewer. (3) Answer with established facts. (4) Doubt block. (5) The plan. (6) Every hop: query, row counts, verification results, any override with its annotation. (7) Source list with the exact objects touched. (8) Model card, if an ML hop ran.

**Readable at three depths, by design.** Marcus reads sections 1–3 and stops. Priya reads through 6. Dr. Chen opens it in a text editor to confirm it is genuinely self-contained ([journeys/edge_high.md](journeys/edge_high.md) §2) — **and that act of verification is the first thing that earns his attention**, so the format must be plain and inspectable rather than a rendered bundle.

**States.** *Unreviewed:* exports only with an explicit acknowledgement and carries a persistent visible watermark in the artifact itself.

## 10. Review queue *(#24, #36)*

**Purpose.** Let an analyst batch review requests without being interrupted by them.

**Primary action.** Review the next one.

**Hierarchy.** (1) Pending requests: requester, question, age, **and a pre-computed triage signal — any amber verification results**. (2) The nearly-finished investigation, not a question. (3) Sign off / override / return with a note.

**Design intent: this must never feel like a ticket queue**, because the bottleneck it replaces was a ticket queue. Requests arrive as artifacts, never as notifications demanding a context switch ([journeys/day_in_life.md](journeys/day_in_life.md) 10:30).

**States.** *Empty:* genuinely empty and celebrated, not filled with suggestions. *Overloaded:* **when the queue exceeds a threshold, say so** — *"12 pending, ~2h at your current pace."* The 11:40 risk in [journeys/day_in_life.md](journeys/day_in_life.md) is that the gate recreates the bottleneck; the interface should make that visible early rather than let it accumulate silently.

**Micro-interactions.** Amber-flagged requests sort first — the ones needing real judgement, not the ones that arrived first.

## 11. Model card — method-level ML lineage *(#32, #39, #40)*

**Purpose.** Let a data scientist find leakage in minutes, or confirm its absence.

**Primary action.** Inspect the target definition and the excluded features.

**Hierarchy.** (1) **Target definition in full** — *"`churned_90d`: no usage event in the 90 days following observation date."* (2) Split strategy, including any embargo. (3) Features used, with importances. (4) **Features excluded, each with its reason** — *"`last_login_date` excluded: leakage candidate."* (5) Algorithms tried. (6) **"Not attempted in budget"** — feature interactions, hyperparameter search, alternative targets. (7) Metric with its uncertainty. (8) Override.

**The not-attempted list is the credibility engine and must be exhaustive.** P9 says a minutes-long budget cannot do what MLE-bench does in twelve hours `[S9]`. **An omission here converts the list from an honest renunciation into a lie by omission**, and Dr. Chen's §7.1 stopping condition is exactly that.

**States.** *Error (insufficient data):* refuse to model and say why. **Producing a weak model silently is the worst available outcome** — it is P3 in the most dangerous place.

## 12. Record view — audit log and history *(#18, #28)*

**Purpose.** Serve the two actors who never author an investigation: Tom, who audits, and Angela, who needs provenance.

**Primary action.** Filter and read.

**Hierarchy.** (1) Filters: date, source, role, investigation, analyst. (2) Query log — timestamp, source, role, statement, investigation ID. (3) Investigation history, searchable by question text and by source touched. (4) Export the log itself.

**Requirement that shapes the implementation.** The audit log must be **readable without the product running** — a file Tom can grep. His 8-minute quarterly review ([journeys/day_in_life.md](journeys/day_in_life.md) 07:50) is the entire content of the security approval that unblocks every sale, and it must not depend on a UI being up.

**States.** *Empty:* only before first use.

---

## 13. What carries the product's feel

Four micro-interaction principles, each traceable to a principle rather than to taste.

1. **Nothing happens without a visible reason.** Every state change names its cause. A hop turning amber says which check failed and by how much. → P3.
2. **The system argues against itself.** Plan-length warnings, not-attempted lists, doubt above charts, "what was not checked" on every green tick. **A product whose interface only ever reassures is one whose failures will be silent.** → P3, P5.
3. **Corrections visibly persist.** Every override shows *"applies to future questions across your team."* The flywheel must be felt at the moment of contribution, or nobody contributes. → PRD §6.
4. **The escape hatch is always one click.** Copy the query, run it yourself. **A verification surface that cannot be bypassed is not trusted** — and an analyst who can leave at any moment is the one most likely to stay. → P5.

## 14. Where this spec is most likely wrong

1. **The fifteen-second plan read and the forty-second hop diagnosis are design budgets, not measurements.** Both come from [journeys/beachhead.md](journeys/beachhead.md) and both are assumptions. If a six-step plan takes two minutes to read, screen 4's economics collapse and the plan-length ceiling becomes hard rather than advisory. **Measure both in the first usability session.**
2. **The green-tick problem may not be solvable by hierarchy alone.** §5 leans on treatment — accompanying numbers, hover disclosure, amber outranking green — to stop a tick reading as "correct." That may be insufficient against a busy user's pattern-matching, and the fallback is to remove green ticks entirely and show only amber and red. Worth testing rather than assuming.
3. **Screen 10 may be the wrong shape entirely.** It is specified as a queue because that is the obvious form, and [journeys/day_in_life.md](journeys/day_in_life.md) 11:40 shows a queue nearly recreating the bottleneck the product exists to remove. If review load scales badly, the answer is not a better queue — it is fewer reviews, via the flywheel or via a trust level that lets repeat question shapes auto-approve. **That is a product question this spec cannot settle.**
