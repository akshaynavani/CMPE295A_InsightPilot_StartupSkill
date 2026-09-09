# Technique wave 3 — frontier AI-native and cross-domain imports

**What this is** — 31 techniques from the current agent/LLM frontier and from adjacent disciplines that solved a structurally similar problem first. Each carries a status and, where declined, the reason.
**Why it exists** — Waves 1 and 2 establish the system rests on established practice. This wave is where the genuinely new options live — and where the temptation to overclaim is highest. It exists to name what the frontier actually offers this system, separate it from what merely sounds impressive, and record the cross-domain imports that are more useful than most of the frontier list. The failure it prevents: a technique catalogue that reads as a survey of everything published in the last eighteen months, connected to nothing.
**How to read it** — §2 (cross-domain imports) is the section with the most actual value, which is the opposite of what the section ordering suggests. A skeptic should attack §1's declines and §3's honest assessment that most of the frontier list does not apply.
**Depends on / feeds** — Builds on [wave1.md](wave1.md) and [wave2.md](wave2.md); anchored to [research/capability_table.md](../../research/capability_table.md). Feeds [decision_tree.md](decision_tree.md) and [technique_feature_matrix.md](technique_feature_matrix.md).

---

**Count: 31**, across 4 clusters. **This wave stopped well short of 50, and the shortfall is the finding.** The frontier agent literature is large, and most of it addresses problems this system does not have — long-horizon autonomy, tool discovery, open-ended web navigation, multi-agent negotiation. A system whose core loop is six steps against read-only structured data with a human gate at three points does not need most of it. Padding this wave to 50 would have meant listing techniques with no application, which is precisely the red flag.

## Cluster 1 — Agent and LLM frontier (13)

| # | Technique | Mechanism | Anchor | Status |
|---|---|---|---|---|
| 3.1.1 | **Tool use via standardised protocol (MCP)** | Connector integration as configuration rather than bespoke engineering | Announced 2024-11-25; OpenAI, Google, Microsoft, AWS within 13 months; Linux Foundation Dec 2025 `[S62]` | ✅ used — D07 adapter |
| 3.1.2 | **Plan-then-execute separation** | Produce a full plan as a data structure before acting | The design's core; enables the D01 approval gate | ✅ used |
| 3.1.3 | **Self-verification by decomposition** | Check a result by authoring smaller, different checks | Databricks *Inspect* independently `[S32]`; P7 | ✅ used — D02 |
| 3.1.4 | **Replanning on invalidation** | Revise the remaining plan when a result contradicts an assumption | `[S10]` | ✅ used — D02 |
| 3.1.5 | **Structured output / function calling** | Typed responses rather than parsed prose | Standard | ✅ used |
| 3.1.6 | **Execution-feedback reinforcement learning** | Train on whether the query ran and returned correctly | Arctic-Text2SQL-R1 `[S14]` | ⬜ declined — requires training infrastructure; the system uses frontier models via API (A5) |
| 3.1.7 | **Multi-candidate generation with execution reranking** | *n* candidates, execute, rank by agreement | ~50% → ~80% in a production agent `[S2]` | 🔶 **top candidate** (also wave 2, 2.1.4) |
| 3.1.8 | **Reflection / self-critique loops** | Model critiques its own output and revises | Widely used | ⬜ **declined by principle.** P7: a model checking itself shares the failure that produced the output. Verification must run different code |
| 3.1.9 | **Chain-of-thought / extended reasoning** | Allocate more inference compute to planning | Reasoning models lead DABstep `[S4]` | ✅ used — frontier class for planning (D05) |
| 3.1.10 | **Context engineering / schema summarisation** | Fit wide schemas into a bounded context | Cortex's ~32K-token semantic model cap `[S36]` | 🔶 candidate — binds above a few hundred columns |
| 3.1.11 | **Retrieval-augmented generation over schema** | Retrieve relevant schema rather than sending all of it | Wren AI's architecture `[S51]` | ✅ used — §1 |
| 3.1.12 | **Long-horizon autonomous agent loops** | Agent runs for hours without human contact | METR horizon doubling `[S6][S7]` | ⬜ **declined by design.** Three mandatory human gates (D10); PRD non-goal 5 forbids autonomous action |
| 3.1.13 | **Multi-agent debate / adversarial critique** | Two models argue toward a better answer | Active research area | ⬜ declined — same objection as 3.1.8, at twice the cost |

**On 3.1.8 and 3.1.13.** These are the two most fashionable techniques in the list and both are declined for the same principled reason. It is worth stating plainly because a reviewer will expect to see them: **self-critique and debate both keep verification inside the model that produced the output.** P7's entire claim is that verification must come from running something structurally different — cheap SQL against the same source — and Databricks reached the same conclusion in production `[S32]`. Adopting reflection would be adopting a technique that sounds like verification and is not.

## Cluster 2 — Cross-domain imports (9)

The most useful section in this wave. Each is a discipline that faced *"how do you trust a result you did not derive"* and answered it decades ago.

| # | Technique | Imported from | Mechanism | Status |
|---|---|---|---|---|
| 3.2.1 | **Audit trail as a first-class deliverable** | **Financial audit** | The workpaper, not the number, is the product. An auditor's output is a trail another auditor can re-walk | ✅ used — **this is the differentiator's intellectual ancestor**, and naming it is more honest than presenting lineage as novel |
| 3.2.2 | **Four-eyes principle** | **Accounting controls** | A material figure is signed by someone other than its preparer | ✅ used — sign-off (D10 H4) |
| 3.2.3 | **Reproducible research / literate computing** | **Scientific computing** | Result, code and data provenance travel as one artifact | ✅ used — the exportable investigation (#15). Hex's notebook is the same idea `[S54]` |
| 3.2.4 | **Pre-registration** | **Clinical trials** | State the analysis plan before seeing results, so the plan cannot be fitted to the answer | 🔶 **strong candidate.** The shown-plan gate (D01) is *already* pre-registration; naming it as such gives the feature a rationale stronger than convenience, and suggests recording plan-vs-outcome divergence |
| 3.2.5 | **Chain of custody** | **Forensics** | Every handoff signed and attributed, so a break is locatable | ✅ used — D04's per-handoff record |
| 3.2.6 | **Blameless post-mortem** | **Site reliability engineering** | Failures are analysed by mechanism, not by fault | 🔶 candidate — the annotation-type field (D04) already separates system error from data-provenance issue |
| 3.2.7 | **Statistical process control** | **Manufacturing** | Track a process metric over time; act on trend, not on a single point | 🔶 **candidate — the right frame for override-rate trend** (D08's `FLY`), which is the only evidence for the A3 moat candidate |
| 3.2.8 | **Defence in depth** | **Security engineering** | Independent layers, each assuming the others fail | ✅ used — plan gate, hop verification, analyst inspection, sign-off (D10) |
| 3.2.9 | **Checklist / read-back confirmation** | **Aviation and surgery** | Read the critical parameter back before acting | ✅ used — binding chips are a read-back (#3) |

**On 3.2.1.** Financial audit solved the trust-a-result-you-did-not-derive problem centuries ago and its answer was to make the trail the deliverable. The system's lineage claim is that idea applied to analytical work. **Saying so is stronger than implying novelty** — it means the design rests on a mechanism with a very long track record rather than on an untested intuition, and it gives Angela's governance conversation a vocabulary she already has.

**On 3.2.4.** Pre-registration is the sharpest unexploited import. The shown-plan gate already *is* a pre-registration ritual; formalising it would mean recording where the executed investigation diverged from the approved plan, which is both a quality signal and a defence against the plan being retrofitted to a desired answer.

## Cluster 3 — Evaluation frontier (5)

| # | Technique | Mechanism | Anchor | Status |
|---|---|---|---|---|
| 3.3.1 | **Execution-accuracy benchmarking on a fixed set** | Score whether generated SQL returns the ground-truth result | Spider 2.0 `[S1]`, BIRD `[S3]` | ✅ used — feature #1 |
| 3.3.2 | **Multi-step data-agent benchmarking** | Score end-to-end multi-hop tasks, not single queries | DABstep `[S4]` | ✅ used — the O3 baseline |
| 3.3.3 | **`pass^k` consistency measurement** | Whether *k* repeats all succeed | τ-bench `[S5]` | 🔶 candidate — the P4 gap (wave 2, 2.2.3) |
| 3.3.4 | **Fault injection / seeded-error evaluation** | Plant known faults; measure what escapes | Standard in reliability engineering | ✅ used — feature #2, the only instrument for O4 |
| 3.3.5 | **LLM-as-judge scoring** | A model grades another model's output | Widely used | ⬜ **declined.** Same objection as 3.1.8, and the harness has ground truth — a judge would add noise where an exact comparison exists |

## Cluster 4 — Emerging and speculative (4)

Labelled research risk, and listed so that a later phase does not rediscover them as if they were free.

| # | Technique | Mechanism | Status |
|---|---|---|---|
| 3.4.1 | **Learned semantic layer from query history** | Infer an organisation's metric definitions from what analysts historically wrote, rather than from confirmations | 🔬 **research risk — and the A3 moat candidate.** Nothing in [research/](../../research/) evidences it either way ([survey.md](../../research/survey.md) §8.3) |
| 3.4.2 | **Learning-to-rank schema linking from override signal** | Use accumulated corrections as relevance labels | 🔬 research risk — needs deployment volume a single tenant may never reach (D09) |
| 3.4.3 | **Automated causal discovery on observational data** | Infer causal structure to answer *why* rather than *what changed* | ⬜ declined — the assumptions required are rarely met in business data, and a wrong causal claim is the most damaging plausible-wrong-answer this system could produce |
| 3.4.4 | **Small-model self-hosting for the full loop** | Run the orchestration on a locally hosted model | ⬜ **declined on evidence.** Tool-initialisation failure is catastrophic in small models — 89% in qwen2.5:3b, absent in large `[S11]`. A5's "self-hostable" means the orchestration layer, on the customer's own frontier-model key |

**On 3.4.3.** Worth the explicit decline because "explains *why* a metric moved" is exactly the category Sisu Data commercialised `[S56]` and exactly what a business user wants. The system does **contribution analysis** (wave 1, 5.4) — which decomposes *what* changed — and must not present that as causal. Conflating the two is the single easiest way for this product to produce confident, consequential nonsense.

## Summary and the honest assessment

| Cluster | Count | Used | Candidate | Declined | Research risk |
|---|---|---|---|---|---|
| 1 Agent/LLM frontier | 13 | 6 | 2 | 5 | 0 |
| 2 Cross-domain imports | 9 | 6 | 3 | 0 | 0 |
| 3 Evaluation frontier | 5 | 3 | 1 | 1 | 0 |
| 4 Emerging | 4 | 0 | 0 | 2 | 2 |
| **Total** | **31** | **15** | **6** | **8** | **2** |

**Three observations a reviewer should take from this wave.**

1. **Eight declines, five of them from the fashionable end of the agent literature.** Reflection, debate, LLM-as-judge, long-horizon autonomy and small-model self-hosting are all declined, and four of the five for the same principled reason: they keep verification inside the thing being verified, or they remove the human gates that make the product trustworthy. **A technique catalogue that declined nothing would be a survey, not a design.**

2. **The cross-domain cluster has the highest hit rate — six used, three candidates, zero declines.** The system's central problem is not new. Audit, accounting, forensics, aviation and reproducible research have all answered *"how do you trust work you did not do"*, and their answers are better tested than anything in cluster 1. **The differentiator's ancestor is the auditor's workpaper**, and the pack is stronger for saying so.

3. **Only two genuine research-risk items, and one of them is the moat.** 3.4.1 is the learned semantic layer that ASSUMPTIONS A3 declines to claim. That it appears here, in the speculative cluster, labelled research risk and unevidenced, is consistent with A3 and must stay that way.
