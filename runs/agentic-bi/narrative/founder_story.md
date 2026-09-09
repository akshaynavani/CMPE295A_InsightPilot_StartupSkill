# Founder story

**What this is** — The founder-market-fit narrative in first person, usable in applications, intros and the 295A presentation.
**Why it exists** — Every other artifact argues from evidence about the world. This one has to answer a different question: *why these people, for this problem, for the next ten years.* It exists in an unusual constraint — [BRIEF.md](../BRIEF.md) states plainly that **the team has no lived experience inside an enterprise analytics function**, so the standard founder story (*"I lived this pain for six years"*) is unavailable and would be a fabrication.
**How to read it** — §2 is the real argument. A skeptic should attack §3, where the missing domain experience is confronted rather than finessed.
**Depends on / feeds** — Built strictly on [BRIEF.md](../BRIEF.md) *Founder edge* and *Riskiest assumption*. Feeds applications, intros and the deck's team slide.

> ### ⚠ This file contains placeholders only the founder can fill
> Everything not in `[BRACKETS]` is derived from the pack and is defensible. **The bracketed items are personal specifics the generator does not have and must not invent** — a fabricated origin anecdote is the fastest way to lose a room, because the follow-up question exposes it. Fill them before use; if one cannot be filled truthfully, cut the sentence rather than soften it.

---

## 1. The story

I did not come to this from analytics. I came to it from **watching multi-agent systems fail.**

For the last [N] years I have built agent systems — orchestration loops, tool-calling chains, the kind of architecture where a model plans, calls something, reads the result, and decides what to do next. [SPECIFIC: the systems you actually built — what they did, at what scale, where.] What you learn doing that, and you learn it the hard way, is that **the interesting failures are never the loud ones.** A crashed tool call is easy. The one that costs you is the step that returned something plausible, and the next four steps built confidently on top of it.

That is not a feeling; it is arithmetic. At 95% reliability per step, a six-step chain is 74%. At 90%, it is 53% `[S13]`. Error propagation is the primary reliability bottleneck in agent systems `[S10]`, and the field's own benchmarks say so: agents scoring above 60% on a single attempt fall below 25% when you require eight attempts in a row to all succeed `[S5]`.

[SPECIFIC: the moment you saw this bite — the project, the debugging session, the plausible-wrong output that shipped. One concrete instance, two or three sentences. If there isn't one you can name, delete this paragraph — an unspecific version is worse than none.]

So when I looked at what everyone was building on top of enterprise data — a chat box on a warehouse — I did not see a product. I saw a **six-hop agent chain with no verification between the hops**, being sold to people who had no way to tell when it was wrong.

And the numbers say exactly that. Schema-level errors — the model picked the wrong column, or the right column meaning something else — are **81.2% of analysed text-to-SQL failures** `[S2]`. The way that failure presents itself: *"failure looks like a plausible but incorrect answer"* `[S2]`. Meanwhile **71% of data practitioners name hallucinated output reaching stakeholders as a top concern** `[S16]`.

That is a market watching the exact failure mode I had spent [N] years debugging, and reaching for the wrong fix. The industry's answer was to constrain the system until it could only answer pre-modelled questions — Genie caps at 30 tables `[S32]`, Cortex runs on hand-written YAML `[S36]`, Copilot cannot compute a metric that is not already a measure `[S42]`. That works, and it means the ad-hoc question, the one nobody anticipated, stays unanswered.

**My answer is the one I would have wanted for my own agent systems: stop promising the chain is right, and make it cheap to find out where it went wrong.** Show the plan before running it. Check every hop with a different, cheaper query — never the model checking itself. Emit a trace where each step can be re-run in isolation. Then the analyst does not have to trust me. They have to spend forty seconds.

## 2. Why I win the next ten years of this

Not because I know analytics better than an analyst. I do not, and §3 is about that.

**Because the hard part of this problem is the part I have already done badly, repeatedly, and learned from.** Most teams building in this space are coming from data — they know warehouses, dimensional modelling, BI tooling — and they are meeting multi-step agent reliability for the first time. That ordering matters, because the failure modes are counter-intuitive:

- **Adding capability reduces reliability.** Every hop you add to make the system smarter makes it less trustworthy `[S13]`. Teams that have not felt this build ambitious plans and cannot understand why the output degrades.
- **Self-critique is not verification.** A model asked to check its own output shares the failure that produced it. This is the single most common architectural mistake in the current agent literature, and I decline it explicitly — verification has to run structurally different code. Databricks reached the same conclusion in production `[S32]`.
- **Consistency degrades faster than capability** `[S5]`. A demo that works once is not a product. An analyst who asks the same question twice and gets two answers has been given work, not leverage.

**And there is a second edge that is about temperament rather than skill.** The whole pack is built on refusing to overclaim — the arithmetic comes to ≈2.9×, not 10×, and it says so `[tech/whitepaper.md]`; the market is $123M, and it says so; the central premise is untested, and it says so. That is not modesty. **In a category with a graveyard this specific** — Watson Analytics discontinued, Power BI Q&A retired, Narrative Science absorbed, Sisu absorbed after ≈$128.7M `[S56]` — **overclaiming is the documented cause of death.** Watson's failure was overpromise versus delivery `[S60]`. I would rather publish a modest number that survives contact with a reviewer than a large one that does not.

The ten-year version of this is not a bigger product. It is a **format**: an investigation record that any tool can emit and any auditor can read. I am well positioned for that specifically because I am not defending a warehouse.

## 3. What I do not have, and how I am handling it

**I have never worked inside an enterprise analytics function.** Not one day. My problem statement is researched, not lived — and that is the single largest risk to everything I have written.

I could paper over that. I am choosing not to, for three reasons.

**First, I have made the research do the work instead.** Every number in this pack traces to a numbered source with an access date and a confidence grade. When I went looking for how many ad-hoc requests an analyst absorbs per week — the figure a real practitioner would know from experience — **I could not find a single credible study.** The widely circulated "80% of a data team's time" figure traces to unsourced vendor marketing, and I recorded it as *rejected* rather than using it. **What I found instead was better**: turnaround time is sourceable at one to four weeks `[S15]`, and the high-confidence current evidence is about trust rather than speed — 83% now prioritise trust in data, up from 66% in a year `[S16]`. **That reframing changed the product's positioning, and I only got it because I had to source what a practitioner would have assumed.**

**Second, the risk I am best placed to judge is the one that decides everything.** The riskiest assumption in this venture is not *do analysts want this* — it is *does multi-agent planning hold up end-to-end without the output becoming untrustworthy.* That is an agent-engineering question, and it is the one I can actually answer. The market questions I cannot answer alone, I am testing by asking rather than assuming.

**Third, I know precisely what I need from other people, and I am asking for it.** Ten analysts, one hour each. One question: *can you accept an answer you did not derive faster than you could derive it?* [SPECIFIC: who you have already asked, and what they said. If nobody yet — say "I have asked none of them yet, and that is the next thing I do," which is honest and better than implying access you lack.]

The beachhead's own objection is the one I take most seriously: *"I read SQL faster than I read explanations."* **That is correct as stated, and if it holds, I have built a slower way to get where they were already going.** I would rather find that out in an afternoon with five analysts than in a year of building.

## 4. Why now, for me

[SPECIFIC: why this project, this year — the capstone framing, what made you pick this over the other things you could have built, who you are building it with and what they bring. Two or three sentences, concrete.]

What I will say is that the timing is not arbitrary. Tool access standardised on the record — MCP shipped November 2024 and OpenAI, Google, Microsoft and AWS all adopted within thirteen months `[S62]` — which turned the connector layer from bespoke engineering into configuration, and that is what makes a pluggable multi-source system tractable for two people.

The reliability did **not** cross a threshold, and I will not claim it did. Multi-step data reasoning still measures ≈15% on hard real-world tasks `[S4]`. **What changed is that the workflow became worth building and measuring.** That distinction is the whole thesis: if it were reliable, nobody would need the trace. Because it is not, the trace is the product.

---

## Usage notes

- **The bracketed items are load-bearing.** §1's second bracket and §3's last are the two that matter most — a specific failure you debugged, and specific people you have or have not spoken to. Both are the kind of detail a listener tests.
- **Do not soften §3.** The missing domain experience is going to come up. Raising it first, with the research discipline as the answer, is far stronger than being caught by it — and the rejected-"80%"-figure story is the most persuasive thing in this document precisely because it is a story about *not* using a number.
- **The voice is deliberately flat.** No hype adjectives, and the evidence carries the weight. In a category whose graveyard was filled by overpromising `[S60]`, understatement is a positioning choice.
