# Future press release — working backwards

**Dated 14 March 2033. Written 2026-09-09.**

**What this is** — An Amazon-style working-backwards press release from seven years out: the outcome achieved, quotes that sound like the personas, the metric the world now uses, and the timeline of how it happened.
**Why it exists** — Working backwards forces a decision the pack has so far deferred: **what does success actually look like, and is it a company or a practice?** The failure it prevents is a vision that quietly contradicts the evidence — a press release announcing a $2B ARR SaaS business would be inconsistent with a $123M SAM and a channel that produces users rather than revenue.
**How to read it** — The release is the vision; §*How we got here* is the constraint check. A skeptic should attack the 2029 entry, where the moat either materialised or did not, and §*What this deliberately does not claim*.
**Depends on / feeds** — Must stay consistent with [strategy/market_sizing.md](../strategy/market_sizing.md), [strategy/channel_plan.md](../strategy/channel_plan.md), [ASSUMPTIONS.md](../ASSUMPTIONS.md) A1/A3, and [tech/whitepaper.md](../tech/whitepaper.md) §5. Vivid, but it invents no capability the pack has not argued for.

---

## The signed answer becomes the default unit of analytical work

**SAN JOSE, 14 March 2033** — InsightPilot today announced that the **signed investigation** — an analytical answer shipped with a hop-level trace and a named human reviewer — has passed 50% adoption among Fortune 500 data organisations, according to the third annual *State of Verified Analytics* survey.

Seven years ago, an enterprise analyst's ad-hoc question took one to four weeks to answer, and 76% of businesses admitted making decisions without consulting data because access was too hard. The industry's response was to put chat interfaces on data warehouses. Those interfaces answered quickly and were bounded to questions someone had modelled in advance, which meant the ad-hoc question — the one nobody anticipated — remained unanswered or unverifiable.

InsightPilot took a different position: that the constraint was never speed, but **the cost of checking an answer you did not derive yourself.**

"We stopped trying to convince people our answers were right," said [Founder], who began the project as a two-person master's capstone at San José State University in 2026. "We built a system that assumes it will sometimes be wrong and makes that cheap to discover. It turns out that is what analysts were actually asking for. They never wanted to be told to trust a black box. They wanted to check it in forty seconds instead of ninety minutes."

### What changed for the people doing the work

"I used to spend two hours re-deriving someone else's analysis to tell them whether it was sound," said Wei Chen, a staff data scientist at a logistics company that deployed the open-source release in 2027. "The worst outcome was that it turned out fine — because I'd spent two hours confirming something and had no way to spend less next time. Now I open the trace, check the target definition and the split, and spot-check the one join I don't like. Nineteen minutes. I got a whole category of my week back."

For requesters, the change was categorical rather than incremental. "Before, I either waited three days or I guessed and hedged the language on my slide," said a regional sales director at the same company. "Now I ask, I get an answer in ninety seconds with an amber bar that says no analyst has looked at this yet, and I send it for review. Six minutes of someone's time instead of ninety. And when it comes back, my analyst's name is next to the number. That's what lets me put it in front of my boss."

Data leaders point to a different benefit. "The question I could never answer was 'where did this number come from,'" said a VP of data and analytics. "Not because nobody knew — because reconstructing it took two days. Now provenance is a property of the artifact. My quarterly review with the CFO takes an afternoon."

### The metric that did not exist in 2026

The survey's headline measure — **time-to-verified-answer**, the wall-clock from a question being asked to an answer a named human will stake their reputation on — did not exist as a tracked metric before 2027. Analytics organisations measured query latency and dashboard adoption, both of which could improve while trust fell.

A second measure has proven more consequential: **verification cost ratio**, the time to accept or reject an answer divided by the time to derive it. The 2033 survey reports a median of 0.31 across deployments running the full trace, against a baseline near 1.0 where the practice began — where checking cost as much as doing.

"Verification cost ratio is now in procurement requirements," said an industry analyst. "Five years ago vendors competed on how confident their AI sounded. Now they compete on how fast you can prove it wrong. That reframing is the company's real legacy, and most of the market has adopted it without adopting their software."

### The shape of the company

InsightPilot remains an open-core project. The orchestration layer, connectors, verification checks and lineage format are Apache-licensed and self-hosted; the company sells support, managed deployment for regulated customers, and a hosted binding-review service. It reports roughly **$74M ARR across 1,900 customer organisations**, having never raised beyond a Series B.

"We were told repeatedly that our market was too small," said [Founder]. "Our own analysis in 2026 put the serviceable market at $123M, and we published that number rather than reaching for a slice of a $40 billion category. We were right that it was small. We were wrong about which part would grow — it turned out the lineage format mattered more than the product."

The **Open Investigation Format**, contributed to a neutral foundation in 2030, is now emitted by four competing analytics tools including two warehouse-native assistants.

---

## How we got here

| Year | What happened | Consistent with |
|---|---|---|
| **2026** | Two-person CMPE 295A/295B capstone. The team builds the evaluation harness before the agents, publishes a multi-hop accuracy number on a fixed question set — the first public figure of its kind in commercial agentic BI — and runs the timed verification-cost study with eleven analysts. **The study is the reason there is a company: the ratio comes back at 0.4, not above 1.0** | The 295A scope; the single claim everything rested on |
| **2027** | Open-source release. Postgres, CSV/Excel, REST. First deployment via an analyst who found the repo in a dbt Slack thread. Second analyst in that company installs after receiving an exported investigation — **the compounding loop closes for the first time** | The GTM loop; the zero-CAC channel |
| **2028** | The review-queue problem nearly kills adoption. Analysts absorb the verification burden their colleagues shed and stop advocating. **Fixed by making trust levels per question-shape**, so repeat investigations auto-approve and only novel shapes need review | **A12, the risk phase 3 raised.** It fired, and was survived by design change rather than by luck |
| **2029** | Override rate per source falls measurably across long-running deployments with no model change. **The learned semantic layer is evidenced for the first time** — five years after it was named as an unproven candidate and deliberately not claimed | A3's confirming observation, finally observed |
| **2030** | Open Investigation Format contributed to a neutral foundation. Two warehouse vendors adopt it. **The company loses exclusivity over its differentiator and gains the standard** | The honest end state of an open-core position |
| **2031** | Managed deployment for regulated customers. Neutrality is preserved contractually because the format is now a standard the company does not own | A5's self-hosted commitment, extended rather than abandoned |
| **2033** | Verification cost ratio enters procurement requirements. The practice outgrows the product | §*The metric that did not exist* |

---

## What this deliberately does not claim

Working backwards is where a vision quietly contradicts its own evidence. Four checks:

1. **No hypergrowth, and no venture-scale outcome.** $74M ARR across 1,900 organisations is consistent with a $123M SAM sized in 2026, not with a slice of the $40B BI category. Announcing a $2B business would have contradicted [strategy/market_sizing.md](../strategy/market_sizing.md) §5.2, which states plainly that this market is small.
2. **No 10× claim, in 2033 either.** The 2026 arithmetic came to ≈2.9× on multi-source questions and ≈1.0× on familiar single-source ones. The 2033 outcome is a *practice* change — verification cost ratio from ~1.0 to 0.31 — which is a different kind of claim and the one the mechanism actually supports.
3. **The moat is evidenced in 2029, not asserted in 2026.** ASSUMPTIONS A3 named the confirming observation — override rate falling per source with no model change — and declined to claim it. The timeline observes it three years after launch, which is how long a compounding semantic asset would actually take.
4. **The company loses control of the differentiator and that is the good ending.** With an open-source core the code was never the asset. A release in which the company still exclusively owns hop-level lineage in 2033 would be inconsistent with its own licensing decision.

**And one thing the release cannot do:** it assumes the 2026 verification study came back below 1.0. If that ratio had been above 1.0, none of this happens — the honest press release for that branch is one paragraph long, and it says the team measured the thing that mattered, found the premise false, and published the negative result. **That would still have been a good capstone.**
