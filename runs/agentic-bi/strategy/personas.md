# Personas

**What this is** — Five persona cards spanning the full user spectrum declared in [BRIEF.md](../BRIEF.md) — low edge, beachhead core, high edge — plus the economic buyer, who is not a user, and the internal blocker, who can stop a purchase without ever being a user.
**Why it exists** — ASSUMPTIONS A7 is flagged `kills-pack-if-wrong: yes`: the PRD, UX spec, journeys and this file are all written against a user spectrum the generator derived rather than the founder supplied. If the spectrum is wrong, five artifacts are wrong together. This file is where the spectrum stops being an abstraction and becomes people with objections — which is the only form in which it can be checked, and the only form a PRD can be written against.
**How to read it** — Read Priya (§2) first; she is the beachhead and the pack is written for her. A skeptic should attack the *objection* line on every card — if an objection is weak, the persona was written to be sold to rather than observed. §7 states what these cards are not.
**Depends on / feeds** — Inherits the spectrum from [BRIEF.md](../BRIEF.md) *Users & spectrum* (ASSUMPTIONS A7) and the positioning from [positioning.md](positioning.md). Feeds [value_prop_canvas.md](value_prop_canvas.md), [sales_roadmap.md](sales_roadmap.md), the PRD, all four journeys, and the discovery guide in `validation/`.

---

## 1. The spectrum, and the two people who are not on it

BRIEF.md declares three edges served by one adaptive system. Sizing and selling require two more people who are not users at all:

| Card | Role | On the spectrum? | Why they are here |
|---|---|---|---|
| §2 **Priya** | Senior data analyst | **Beachhead** | The user the pack is written for |
| §3 **Marcus** | Regional sales director | Low edge | Consumes answers, cannot judge correctness — makes conversation load-bearing |
| §4 **Dr. Chen** | Staff data scientist | High edge | Audits lineage, overrides ML choices — makes traceability load-bearing |
| §5 **Angela** | VP Data & Analytics | No — **economic buyer** | Holds the budget. User ≠ payer, per BRIEF.md |
| §6 **Tom** | Data platform lead / security | No — **blocker** | Can veto without ever using it. The reason A5's self-hostable decision matters commercially |

## 2. Priya Raghunathan — Senior Data Analyst *(beachhead)*

**Context.** 31, six years in analytics, three at a 4,000-person logistics company. Sits inside a five-person central analytics team serving finance, ops and commercial. Fluent in SQL, comfortable in Python, owns eleven dbt models. Her company runs Postgres for the operational system, Snowflake for the warehouse, a monthly carrier-cost CSV that arrives by email, and a REST API for the shipment-tracking vendor.

**Day-in-the-life pain moment.** 4:10pm Thursday. Slack from the ops director: *"Why did our cost per shipment jump in the Southwest last month?"* Priya knows the shape of the answer — join the warehouse shipment table to the carrier-cost CSV, split by region and carrier, check whether it is mix or rate. She also knows it is ninety minutes she does not have, because the carrier CSV has never been modelled and she will spend twenty of those minutes just reconciling its region codes against the warehouse's. She replies *"let me look tomorrow."* It is the fourth time this week she has said that.

**Current workaround.** She writes the SQL herself. Her BI tool's Copilot cannot help, because the answer needs a metric that is not in the semantic model — cost per shipment by carrier by region does not exist as a measure `[S42]`.

**Trigger to switch.** Not curiosity. A specific bad week: the queue outruns her, she ships an answer she has not fully checked, and someone makes a call on it. What she wants after that week is not speed — it is a way to hand back an answer she can defend.

**Must-have language, as she would actually say it.** *"I need to see what it did. If I can't check the joins, I'm just going to rewrite it myself, and then what was the point."* And: *"Don't give me a number. Give me a number and the query."*

**Objection you must overcome.** *"Verifying your reasoning is not obviously faster than writing it myself. I read SQL faster than I read explanations."* — This is the strongest objection in this file, it is correct as stated, and the entire differentiator rests on answering it. It is why the validation layer's first experiment measures verification cost rather than accuracy ([research/competitors.md](../research/competitors.md) §4).

**Second objection.** *"We already pay for Copilot and nobody uses it."* Roughly 25% of employees use the BI tools their company bought, flat across seven years `[S22]`. Priya has watched a rollout fail before.

## 3. Marcus Delgado — Regional Sales Director *(low edge)*

**Context.** 44, runs the Southwest region, 60 people. Owns a P&L. Has a Power BI dashboard he opens twice a month and does not trust, because the last time he cited a number from it in a QBR the finance team corrected him.

**Day-in-the-life pain moment.** Preparing for Monday's forecast call, he wants to know whether his pipeline slippage is worse than last quarter or just feels worse. The dashboard shows pipeline by stage but not stage-transition timing. He messages Priya. It is Thursday. The call is Monday. He builds the slide from memory and hedges the language.

**Current workaround.** He asks a person, or he guesses. He is part of the 76% of businesses that have made a decision without consulting data because it was too difficult to access `[S15]`, and he is why *doing nothing* is the market leader ([research/competitors.md](../research/competitors.md) §2, row 1).

**Trigger to switch.** Being wrong in front of his boss, once, in a way that was avoidable.

**Must-have language.** *"I don't want to learn a tool. I want to ask the question the way I'd ask Priya, and I want to know whether the answer is solid enough to put on a slide."*

**Objection you must overcome.** *"How do I know it's right? I can't read a query."* — He cannot verify, and he knows it. **This is why he is a design constraint and not the first customer:** the honest answer to Marcus is that an analyst signed off, which means the product must make analyst sign-off cheap. Selling Marcus directly is the ThoughtSpot bet, and that bet was marked down 73.67% `[S46]`.

## 4. Dr. Wei Chen — Staff Data Scientist *(high edge)*

**Context.** 38, PhD, eight years in industry, the person the analytics team escalates to. Owns the demand-forecasting model. Deeply sceptical of automated ML, having spent a year cleaning up a previous team's AutoML pipeline that had quietly leaked target information through a date column.

**Day-in-the-life pain moment.** Not a queue problem — a review problem. An analyst brings him a churn-driver analysis produced by an AI tool and asks whether it is sound. He cannot tell without redoing it. He redoes it. It takes two hours and it was fine, which is the worst outcome: he has spent two hours confirming something and has no way to spend less next time.

**Current workaround.** He re-derives. Always.

**Trigger to switch.** A trace detailed enough that he can spot-check the one step he doubts — the join grain, the train/test split, the target definition — instead of re-running the whole chain.

**Must-have language.** *"Show me the target definition and the split. If it picked the algorithm, tell me what else it tried and why it didn't pick those. And I want to be able to override it."*

**Objection you must overcome.** *"Automated modelling on business data is how you ship leakage into production."* — Legitimate and technically well-founded. It is also why the ML agent is deliberately not the differentiator (ASSUMPTIONS A2), and why any modelling output must arrive with its uncertainty and its choices exposed. Note the honest constraint from research: MLE-bench-class agents reach a 36.4% medal rate under a **12-hour budget** `[S9]`, which is not a conversational latency budget — the PRD must specify what the ML agent does in minutes.

## 5. Angela Osei — VP Data & Analytics *(economic buyer, not a user)*

**Context.** 47, owns a $3.1M annual budget covering the warehouse contract, BI licences, four engineers and the five-person analytics team. Reports to the CFO. Two years into a "data trust" initiative after a board-level incident where two teams reported different revenue numbers.

**Day-in-the-life pain moment.** Her problem is not the queue; it is being asked by the CFO whether the numbers in the board deck can be relied upon, and not having a clean answer. She is the reason trust in data as a stated priority rose from 66% to 83% in a year `[S16]`, and she is currently spending against that need on a semantic layer — which is what 59% of organisations at her scale are doing `[S17]`.

**Current workaround.** Governance process, and hiring. Neither scales, and both are slow.

**Trigger to switch.** A demonstrated reduction in the review burden on her senior people — Dr. Chen's two hours — or a governance story she can take to an audit conversation.

**Must-have language.** *"I don't need my analysts to be faster. I need to be able to answer 'where did this number come from' without a two-day investigation."*

**Objection you must overcome.** *"I'm already buying a semantic layer for exactly this. Why is this not that?"* — **The hardest commercial objection in this file**, and the one [market_type.md](market_type.md) §2.3 names as the case against the entire market-type declaration. The answer: a semantic layer defines what a metric *means*; it does not tell you what happened, why, or what was done to find out. They are complements, and this product should consume hers rather than replace it `[S66]`.

**Her second question, which decides the deal.** *"Where does our data go?"* — answered by A5: open-core, self-hostable, running inside her boundary against her own model key.

## 6. Tom Bradley — Data Platform Lead *(blocker, not a user)*

**Context.** 39, owns the warehouse, the connections and the security review. Not hostile — busy, and accountable if something leaks.

**Pain moment.** He is asked to approve a tool that will hold credentials to Postgres, the warehouse and a vendor API, and send schema information to a model provider. He has approved three AI tools this year and revoked one.

**Trigger to approve.** Self-hosted deployment, credentials that never leave the boundary, and a readable audit log. This is the commercial content of the A5 decision — it is not only a positioning argument, it is what gets past Tom.

**Must-have language.** *"Does it run in our VPC, and can I see every query it issued?"*

**Objection you must overcome.** *"Another agent with broad read access to production data, and I'm the one who signs off."* — Note that Gartner attributes half of projected AI agent deployment failures by 2030 to insufficient governance runtime enforcement `[S29]`. Tom is right to be careful, and the product's lineage is as much his artifact as Priya's.

## 7. What these cards are and are not

Stated plainly because it bears on how much weight they can carry.

**These personas are constructed, not observed.** No analyst was interviewed. They are synthesised from the sourced evidence — turnaround times `[S15]`, trust priorities `[S16][S17]`, adoption rates `[S22]`, the documented limits of the incumbent tools `[S42][S44]` — and from the spectrum in ASSUMPTIONS A7, which was itself derived rather than supplied. **Every quote is plausible language, not recorded language.**

That is the correct standard for a pre-discovery pack, and it is exactly what customer discovery exists to replace. The discovery guide in `validation/` should treat each card as a **hypothesis about a person**, and the *objection* line on each as the specific thing to go and test. Priya's objection in §2 is the one that decides the venture.

## 8. Ranking — who to serve, in order

1. **Priya (beachhead).** Everything is built for her. If she does not adopt, nothing downstream matters.
2. **Angela (buyer).** She signs. Reached through Priya's advocacy, not around it — user-led, buyer-closed.
3. **Tom (blocker).** He cannot say yes to a purchase, but he can end one. The self-hostable decision is largely for him.
4. **Dr. Chen (high edge).** Small population, disproportionate influence: he is the internal credibility test, and his approval unlocks Angela's.
5. **Marcus (low edge).** Served by the system's design, not sold to. His questions arrive through Priya. Selling to Marcus first is the bet the market already marked down `[S46]`.

## Recommended next 3

1. **Write [value_prop_canvas.md](value_prop_canvas.md) against Priya, Angela and Dr. Chen only.** Marcus and Tom shape the design and the security posture; they do not shape the value proposition.
2. **Make Priya's objection — "verifying isn't faster than rewriting" — the headline hypothesis in `validation/riskiest_assumptions.md`.** It is the differentiator restated as something a person would say, and it is falsifiable in a single afternoon with five analysts.
3. **Carry Angela's semantic-layer objection into [sales_roadmap.md](sales_roadmap.md) as a required objection-handling artifact.** It is the one that ends deals, and the answer — complement, consume, do not replace — needs to be a demo, not a sentence.
