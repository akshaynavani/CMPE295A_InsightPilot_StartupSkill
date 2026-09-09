# Metrics by stage — and the vanity metrics to ignore

**What this is** — The three to five metrics that matter at each stage, and — equally important — the metrics that will look like progress at that stage and mean nothing, with the reason each is misleading *here specifically*.
**Why it exists** — This product has an unusual property: **its most flattering metrics are its least informative ones.** An open-source repo generates stars, a demo generates enthusiasm, and a verification surface generates a hop-inspection rate that looks best when it is in the middle. Without this file, a team under review pressure will report the numbers that go up. The failure it prevents is optimising a metric whose improvement is indistinguishable from failure.
**How to read it** — The *Ignore* column carries more information than the *Track* column. A skeptic should attack §2's hop-inspection band, which is the only metric here where both extremes are failures, and §5, which names the one metric the team will most want to report.
**Depends on / feeds** — Stage placement from [stage_gate.md](stage_gate.md), funnel metrics from [get_keep_grow.md](get_keep_grow.md), outcome metrics from [product/PRD.md](../product/PRD.md) §7. Feeds the 295A/295B reporting cadence.

---

## 1. Discovery *(current stage)*

**The question this stage answers: is the problem real, and is our reading of it right?**

### Track — 5 metrics

| # | Metric | Threshold | Why it matters |
|---|---|---|---|
| 1 | **Median % of an analyst's last 20 real requests that span >1 source** | ≥ 25% | Decides whether the neutrality argument has content and whether SAM halves (E3) |
| 2 | **Verification cost ratio** — minutes to accept/reject ÷ minutes to derive | ≤ 0.5 | The single number the venture rests on (E1) |
| 3 | **Seeded-defect rejection rate with the trace, vs. control** | ≥ 70%, ≥ 2× control | Whether verification *works*, not what it costs (E2) |
| 4 | **Buyers naming a specific budget line** | ≥ 3 of 5 | Decides whether this is a company or a feature (E4) |
| 5 | **Surprise count** — findings per interview that contradicted the pack | **> 0 per 3 interviews** | The pack was written with no domain experience. Zero surprises means the interviewer was steering |

**Metric 5 is unusual and deliberate.** In a pack whose problem statement is researched rather than lived, *rate of being wrong* is a leading indicator of interview quality. Ten confirmatory interviews are worth less than three that overturned something.

### Ignore at this stage

| Vanity metric | Why it misleads **here** |
|---|---|
| **GitHub stars / repo traffic** | Measures whether the README is interesting, not whether the problem is real. Wren AI has 13,000+ stars `[S50]` and that tells you nothing about whether *this* thesis holds |
| **"Analysts said they liked it"** | Enthusiasm in a problem interview usually means the interviewer pitched. See [discovery_guide.md](discovery_guide.md) §8 anti-pattern 1 |
| **Number of interviews conducted** | 20 unscreened conversations are worth less than 8 screened ones. Count *qualified* interviews or nothing |
| **Artifact count in this pack** | Fifty documents is not progress. [stage_gate.md](stage_gate.md) §5 says this in plain terms |
| **Demo requests** | There is nothing to demo, and wanting to see something is not wanting to use it |

## 2. Validation

**The question: does the thing work, and will they adopt it unaided?**

### Track — 5 metrics

| # | Metric | Threshold | Why it matters |
|---|---|---|---|
| 1 | **Multi-hop execution accuracy** on the fixed question set | ≥ 50% | The only number no commercial agentic-BI product publishes. Baseline: DABstep Hard ≈15% `[S4]` |
| 2 | **Silent-error rate (O4)** — seeded defects that escape every check | as low as possible; **report it regardless** | P3's failure mode. The metric most likely to be quietly dropped because it makes the system look bad |
| 3 | **Clone → first successful investigation, median** | < 30 min | The gate on the only channel with viable economics (E8) |
| 4 | **Hop-inspection rate** | **20–60%** | See below — the band, not the direction, is the signal |
| 5 | **Analyst review-time per week** | < 4 h, flat or falling | A12's tripwire (E5) |

### The hop-inspection band — the one metric where both extremes are failures

| Reading | What it means | Verdict |
|---|---|---|
| **~0%** | Nobody opens the trace. They are trusting blind — which P3 says is unsafe, and which makes the differentiator decorative | **Failure** |
| **20–60%** | They check when something feels off, guided by doubt surfacing | **Healthy** |
| **~100%** | They check everything. That is re-derivation wearing a nicer interface, and the verification cost ratio is ~1.0 | **Failure** |

**This is why "engagement" is the wrong frame for this product.** A metric that goes up is normally good; here, driving inspection rate toward 100% would mean the system had lost their trust entirely. No competitor has an analogous metric because no competitor has a verify beat to instrument.

### Ignore at this stage

| Vanity metric | Why it misleads |
|---|---|
| **Total investigations run** | Design partners run investigations because you asked them to. Split cohorts or the number is meaningless |
| **Accuracy on the *easy* question subset** | Spider 2.0-Snow tops 96.70% and its DBT setting drops to 65.60% `[S1]`. Reporting only the easy split is the exact selective reading the pack criticises incumbents for |
| **Time-to-answer alone** | A fast wrong answer scores well. This is why the outcome metric is time-to-*verified*-answer |
| **Doubt-surfacing frequency** | Surfacing lots of doubt looks conscientious. Only calibration — does surfaced doubt predict actual error — makes it meaningful, and that is currently unmeasured |
| **Installs** | An install that never reaches a successful investigation is a download, not a user |

## 3. Customer Creation

**The question: does one user become two without us?**

### Track — 4 metrics

| # | Metric | Threshold |
|---|---|---|
| 1 | **Deployments reaching a second analyst without founder intervention** | ≥ 20% by week 12 |
| 2 | **Override rate per source, trend over 90 days** | Falling — the only evidence for the A3 moat candidate (R10) |
| 3 | **Exports per active analyst per week** | ≥ 1 — the compounding loop's only edge |
| 4 | **Deployments where a budget owner is asked to fund it** | ≥ 10% by week 24 |

### Ignore

| Vanity metric | Why |
|---|---|
| **Cumulative installs** | Growth without retention. Metric 1 is the real one |
| **Community size / Slack members** | Correlates with interest, not with use |
| **Feature request volume** | Reads as engagement, often signals the core loop is unfinished |

## 4. Company Building

Beyond the honest planning horizon of a two-semester capstone. One metric is worth fixing now because its instrumentation must exist from day one:

**Verification cost ratio, measured in production rather than in a lab.** If [narrative/future_press.md](../narrative/future_press.md)'s 2033 framing is right, this becomes the category's procurement metric — and it is measurable only if sign-off timing is captured from the first deployment ([tech/architecture/D04](../tech/architecture/D04_memory_schema.md)).

## 5. The metric this team will most want to report, and should not

**A working demo.**

It is the most natural thing to show an advisor, it feels like the strongest evidence available, and it is nearly uninformative here. A demo shows one path working once. τ-bench shows agents above 60% on a single attempt falling below 25% when eight consecutive attempts must all succeed `[S5]` — **so a demo that works is consistent with a system that fails three times in four.**

The honest substitute is the harness number with its question set published. It is less impressive, it is harder to produce, and it is the only claim that survives someone re-running it.

**Second most tempting: reporting E6's accuracy without E7's silent-error rate.** Accuracy alone is the flattering half. P3 says the dangerous failures look like successes, so an accuracy figure unaccompanied by a silent-error figure is precisely the selective reporting this pack criticises the incumbents for — none of whom publish either ([research/sources.md](../research/sources.md), *Named gaps* 2).

## Recommended next 3

1. **Instrument the hop-inspection band before the first external deployment.** It is the retention predictor, both extremes are failures, and it cannot be reconstructed after the fact.
2. **Commit to publishing E6 and E7 together, in writing, now.** Deciding in advance to report the silent-error rate alongside the accuracy figure is the only reliable defence against dropping the unflattering one under review pressure.
3. **Track the surprise count from interview one.** It is the cheapest available check on whether discovery is genuinely learning or quietly confirming — and this pack, written without domain experience, should expect to be wrong repeatedly.
