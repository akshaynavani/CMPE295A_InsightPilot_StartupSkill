# Customer discovery guide

**What this is** — The interview kit: screening criteria per persona, problem-interview questions that ask only about the past, the solution-interview script, the timed-task protocol for E1, and the synthesis template.
**Why it exists** — Three of the four venture-ending assumptions are answerable by talking to about fifteen people ([riskiest_assumptions.md](riskiest_assumptions.md)), and the team has **no lived experience inside an analytics function** — so these conversations are not a formality, they are where the domain knowledge the pack lacks actually comes from. The specific failure it prevents: interviews that pitch the product, which return enthusiasm instead of information and are worse than no interviews at all.
**How to read it** — §3 is the discipline; every question there is about something that already happened. A skeptic should attack §3's question list for anything hypothetical, and §5, which is the protocol carrying the pack's most consequential number.
**Depends on / feeds** — Screens against [strategy/personas.md](../strategy/personas.md); tests E1, E2, E3, E4 and R7/R11 from [experiment_board.md](experiment_board.md). Feeds [pivot_log.md](pivot_log.md) and every downstream revision.

---

## 1. The one rule

**Ask about the past. Never about the future.**

"Would you use a tool that…" produces a polite yes that predicts nothing. "Walk me through the last time you…" produces a story with times, tools and workarounds in it. Every question in §3 obeys this, and any question added later must too.

**Corollary: do not describe the product in a problem interview.** The moment the interviewee knows what you are building, they start being helpful, and helpfulness is noise. The solution interview (§4) is where the product appears, and it is a separate session.

## 2. Screening criteria

### 2.1 Beachhead analyst — target 10

Must have **all five**:

1. Writes SQL at least weekly against a production data source.
2. Receives ad-hoc analytical requests from someone who is not on the data team.
3. Works at an organisation with a deployed BI tool (Power BI, Tableau, Looker, Databricks, Snowflake).
4. Has access to more than one system of record — a warehouse *and* something else.
5. Is not on the data-platform or infrastructure team. This person answers questions; they do not maintain pipelines.

**Disqualify if:** they are a solo analyst at a company under ~50 people (no queue), or a pure BI-report builder who does not write ad-hoc SQL.

### 2.2 Budget owner — target 5

1. Owns or materially influences a data/analytics budget line.
2. Has approved at least one analytics tool purchase in the last 18 months.
3. Has at least three analysts reporting into their function.

### 2.3 Staff data scientist — target 3 *(tests R7's high edge)*

1. Has reviewed someone else's analysis in the last month and can describe it.
2. Owns at least one model that other people depend on.

### 2.4 Business stakeholder — target 3 *(tests R7's low edge)*

1. Has requested data from an analyst in the last 30 days.
2. Does not write SQL.

## 3. Problem interview — analyst *(45 minutes)*

Do not mention the product. Ask 1–8 of everyone; 9–14 as time allows.

**Opening — establish the queue.**

1. "Walk me through last Thursday. What did people ask you for?"
2. "How many ad-hoc requests came to you last week? Where do they arrive — Slack, tickets, email?"
3. "Which of those did you actually finish, and which are still open?"

**The last real question — the core of it.**

4. "Take the last ad-hoc question you finished. What was it?"
5. "Walk me through what you did, step by step, from reading the request to sending the answer."
6. "How long did that take, start to finish? How much of it was waiting versus working?"
7. "Which step took longest? Where did you get stuck or have to redo something?"

**Sources — this is E3/R3.**

8. **"For that question, how many separate systems did you have to pull from? Which ones?"**
9. **"Open your last 20 requests. How many needed data from more than one system?"** *(Ask them to actually look. This is the measurement, not an estimate.)*
10. "When did you last work with a data source nobody had modelled — a file, an export, an API? What did that cost you?"

**Verification — the setup for E1.**

11. "Before you sent that answer, what did you do to check it?"
12. "Tell me about the last time you sent an answer that turned out to be wrong. What happened, and how did you find out?"
13. **"When someone hands you an analysis they did — not you — how do you decide whether to trust it? Walk me through the last time."** *(This is the closest a problem interview gets to E1, and it is the most valuable single question in the guide.)*

**Existing tools.**

14. "What AI or copilot features are available in your BI stack? When did you last use one, and what happened?"
15. "What did you do the last time it couldn't answer something?"

**Spectrum — free test of R7.**

16. "Who sends you these questions? Do they ever try to answer them themselves?"
17. "Does anyone review your work before it goes out? Who, and when did that last happen?"

## 4. Problem interview — budget owner *(30 minutes)*

1. "What analytics tools has your team bought in the last 18 months? Walk me through the most recent decision."
2. "What line did that come out of? What did it displace, if anything?"
3. "How do you find out whether a tool you bought is actually being used?"
4. "Tell me about the last time someone asked you whether a number could be relied on. What did you do?"
5. **"If your team adopted a tool like this, what line would it come from and what would it displace?"** *(E4 — the deal question. Record verbatim.)*
6. **"How many analysts sit on your central team?"** *(R11 — ten seconds, flips the channel plan.)*
7. "What are you currently spending on semantic-layer or metrics tooling?" *(Tests the [strategy/market_type.md](../strategy/market_type.md) §2.3 counter-case directly.)*
8. "What would have to be true for you to stop funding something you already bought?"

## 5. The timed task — E1 protocol *(60 minutes, separate session)*

**This is the most consequential hour in the pack.** Run it as a measurement, not a demo.

**Setup.** Two matched questions of equal complexity, each spanning a warehouse table and an unmodelled CSV, built on a realistic sample schema. Counterbalance: half the participants get condition A first.

- **Condition A — verify.** They receive a *correct* answer with hop-level lineage: plan, six hops with queries and row counts, verification results, established facts. Task: "Decide whether you would put your name on this." Stopwatch stops when they commit.
- **Condition B — derive.** They receive the question and database access. Task: "Answer this to the point where you'd put your name on it." Stopwatch stops when they commit.

**Record:** minutes per condition; which hops they opened in A and in what order; what they said aloud; whether they accepted or rejected; and — importantly — **what they did *not* look at.**

**Primary measure:** median A ÷ median B. Threshold declared in [experiment_board.md](experiment_board.md) E1: pass ≤ 0.5, fail > 0.8.

**Do not:** explain the product, defend the lineage design, or answer questions about the interface until the stopwatch stops. **Confusion is data.**

**Second session, later — E2.** Six investigations, three with planted defects (wrong join grain, wrong region mapping, wrong time window). Same instruction: accept or reject. Measures whether verification *works*, not what it costs.

## 6. Solution interview *(after problem interviews, 45 minutes)*

Only after the problem interviews are done and synthesised. The product may now be shown.

1. Show one exported investigation artifact. **Say nothing.** Watch what they open first and how long they spend. Then: "What is this? What would you do with it?"
2. "Where would you be suspicious?"
3. Show the analysis plan before execution. "What would you do with this screen?"
4. Show an amber verification result. "What does this tell you? What would you do next?"
5. "What would have to be true for you to install this on Friday?"
6. "What would stop you?" — then: **"Who else would have to say yes?"** *(Feeds [decision_making_unit.md](decision_making_unit.md).)*
7. "What's the smallest version of this that would be useful?"
8. **"If this existed and worked, what would you stop doing?"** — the best available proxy for real value.

**Do not ask "would you pay for this."** Ask §4 question 5 of the budget owner instead. Analysts do not know their budget and their guess is worthless.

## 7. Synthesis template

Complete within 24 hours of each interview, then aggregate.

```
INTERVIEW #___    Persona: ___    Date: ___    Duration: ___
Screening: passed all criteria? Y/N    If N, which failed:

TOP 3 PAINS (their words, verbatim)
1.
2.
3.

CURRENT WORKAROUND — what they do today, in what tool, how long

TRIGGER — the last time the pain was bad enough to act. What happened?

MUST-HAVE LANGUAGE — a sentence they said that a landing page could use verbatim

OBJECTION — the thing they said that would stop them buying or installing

MEASUREMENTS
  Last-20 requests, multi-source count:      ___ / 20        → E3
  Reported turnaround, typical:              ___             → context for [S15]
  How they verify others' work today:        ___             → E1 context
  Budget line named (buyers only):           ___             → E4
  Central team size (buyers only):           ___             → R11

SPECTRUM CHECK (R7)
  Receives questions from a non-technical requester?   Y / N
  Work reviewed by a senior scientist?                 Y / N

SURPRISE — the thing that contradicted the pack. **Always fill this in.**
```

### Aggregate view

| Question | Threshold | Result |
|---|---|---|
| Median % of last-20 requests multi-source | ≥ 25% | |
| Buyers naming a specific budget line | ≥ 3 of 5 | |
| Analysts confirming both spectrum edges (R7) | ≥ 7 of 10 | |
| Median verification cost ratio (E1) | ≤ 0.5 | |
| Median central-team size (R11) | 5–15 | |

## 8. Anti-patterns

Named because they are the ways this guide gets ruined in practice.

1. **Pitching in a problem interview.** Once they know what you are building, everything after is politeness.
2. **Accepting an estimate where a record exists.** "Maybe half are multi-source" is worthless; ask them to open the queue and count. §3 question 9 is the whole of E3.
3. **Interviewing whoever will talk to you.** A solo analyst at a 30-person startup has no queue, no buyer and no reviewer — they will be friendly and they will teach you nothing about this segment.
4. **Not writing the SURPRISE line.** If ten interviews produce no surprises, the interviews were confirmatory. The pack was written with **no domain experience**; it should be surprised repeatedly, and a synthesis with an empty surprise field is evidence the interviewer was steering.
5. **Explaining during the timed task.** Confusion is the measurement.

## Recommended next 3

1. **Recruit ten analysts before writing another line of the pack.** Three venture-ending questions are answerable in three weeks and the pack has been built without asking any of them.
2. **Run §5's timed task with the first five who qualify.** It is the pack's most consequential hour and it needs no product — a static exported artifact and a stopwatch are sufficient.
3. **Treat the SURPRISE field as the primary output.** The pack's problem statement is researched, not lived; the value of these interviews is disproportionately in what it got wrong, not in what it got confirmed.
