# Lean canvas

**What this is** — Maurya's nine-block lean canvas for Agentic BI, one table, each cell at most three bullets, with the riskiest cell marked ⚠.
**Why it exists** — The pack now spans a brief, five research files and four strategy documents. This is the one page that has to hold together on its own, and its job is to make an inconsistency visible: if the problem, the solution and the unfair advantage cannot be stated in three bullets each without contradicting each other, something upstream is wrong. It is also the compression test — a venture that needs a page to explain its problem does not have one.
**How to read it** — The ⚠ cell is the venture. A skeptic should attack *Unfair advantage*, which is deliberately close to empty, and *Revenue streams*, which is hypothetical by decision rather than by oversight.
**Depends on / feeds** — Compresses [BRIEF.md](../BRIEF.md), [positioning.md](positioning.md), [market_sizing.md](market_sizing.md) and [personas.md](personas.md); cross-links to [business_model_canvas.md](business_model_canvas.md), which keeps the three blocks Maurya drops. Feeds `narrative/one_pager.md` and `validation/riskiest_assumptions.md`.

---

## The canvas

| Block | Content |
|---|---|
| **1. Problem** | • Every ad-hoc business question costs the same fixed manual sequence — locate source, inspect schema, write and debug query, clean, join, chart, interpret — and the requester waits one to four weeks at enterprise scale `[S15]`<br>• Answers that arrive fast are not trusted: 71% of practitioners name incorrect or hallucinated output reaching stakeholders as a top concern `[S16]`, and verifying an answer you did not derive may cost as much as deriving it<br>• The predictive question — *will this continue* — is usually not attempted at all, not because it is slow but because it is a different job |
| **2. Existing alternatives** | • **Doing nothing** — 76% of businesses have decided without consulting data because access was too hard `[S15]`. The market leader<br>• **The analyst writes the SQL** — correct, unverifiable-by-others, does not scale past one person's attention<br>• **Warehouse-native assistants** — Genie, Cortex Analyst, Copilot, Pulse: single-source, single-hop, bounded by a pre-authored semantic artifact `[S32][S36][S42]` |
| **3. Solution** | • An Orchestrator that decomposes a question into an *analysis plan* spanning heterogeneous sources, and replans when a result invalidates the plan<br>• Four specialist agents — Data Fetch/Integration, Analytics, Visualization, ML — each handoff emitting inspectable, re-runnable lineage<br>• Open-core, self-hostable: runs inside the customer's boundary against their own model key (A5) |
| **4. Key metrics** | • **Time-to-verified-answer** — wall-clock from question asked to an answer the analyst will stake their name on. The outcome metric; contains both speed and trust<br>• Verification cost: minutes for an analyst to accept or reject an answer, versus minutes to re-derive it<br>• Multi-hop execution accuracy on a fixed question set — the number no commercial product publishes ([research/sources.md](../research/sources.md), *Named gaps* 2) |
| **5. Unique value proposition** | • *The only conversational analytics layer that answers a question spanning your real sources and hands back an investigation you can verify hop by hop*<br>• Not faster. **Checkable** — which is what makes an answer you did not derive worth having<br>• For the enterprise analyst who can already write the query, not the business user who cannot |
| **6. Unfair advantage** ⚠ | • **None yet, and the pack does not claim one** (ASSUMPTIONS A3). Open-source core means the code is not the asset<br>• Strongest candidate: a **learned semantic layer** — accumulated disambiguation of one organisation's schema, metric definitions and vocabulary. Copyable code, non-copyable semantics<br>• Confirming evidence would be: repeat users' answer-acceptance rate rising over time with no model change. **Not yet observed** → `validation/riskiest_assumptions.md` |
| **7. Channels** | • Open-source distribution: repository, documentation, the analyst communities where the beachhead already reads<br>• Analyst-led adoption, buyer-closed — Priya advocates, Angela signs ([personas.md](personas.md) §8)<br>• Academic and conference channel during 295A/295B; a published multi-hop accuracy number is the credible artifact |
| **8. Customer segments** | • **Beachhead:** enterprise data analysts at organisations with a deployed BI stack, an ad-hoc queue, and questions spanning more than one source — ≈74,600 in the US `[S69][S70]` plus assumptions<br>• **Economic buyer:** the data/analytics function's budget owner<br>• **Early adopters:** analysts who have already tried a warehouse copilot and hit its bounded-scope wall |
| **9. Cost structure** | • Model inference per investigation — several agents, several hops, retries. Anchored against Cortex Analyst at ≈$0.134 per message `[S38][S39]`<br>• Connector engineering and maintenance; MCP makes access a configuration problem `[S62]` but not semantics<br>• Zero data-storage cost in the self-hosted model — the customer runs it (A5) |
| **10. Revenue streams** | • **Hypothetical only.** Monetisation is out of scope for the academic project (ASSUMPTIONS A1)<br>• Modelled threshold: $75/analyst/month, at the top of the observed analyst-tool band `[S44][S52]` — a price to falsify, not a forecast<br>• The incumbents price the *question* — Cortex per message `[S37][S38]`, ThoughtSpot capping Spotter at 25 queries/user/month `[S44]` — which matches this product's unit of value |

## The riskiest cell

**⚠ Block 6, Unfair advantage — and it is risky for the opposite of the usual reason.** Most canvases fail here by asserting a moat that does not exist. This one fails by having nothing to assert, and saying so.

That is the honest position (A3) and it has a real cost the pack should own: **with an open-source core and no compounding loop yet evidenced, a well-executed copy is a legitimate outcome.** The learned-semantic-layer candidate is the only entry with a mechanism behind it — an organisation's accumulated schema disambiguation is genuinely not copyable — but it is unevidenced, and the evidence that would confirm it requires repeat users the project does not have.

**Second-riskiest is block 5**, because the UVP asserts that verification is cheaper than re-derivation and Priya's objection in [personas.md](personas.md) §2 says the opposite in the beachhead's own words. That claim is testable in an afternoon and has not been tested.

## Cross-link

This canvas drops **Key Partners, Key Activities and Customer Relationships** — Maurya's deliberate simplification. Those three are covered in [business_model_canvas.md](business_model_canvas.md), where each of the nine Osterwalder blocks additionally carries a falsifiable hypothesis and the cheapest test that would kill it. Read the two together; neither is complete alone.

## Recommended next 3

1. **Do not attempt to fill block 6 in a later phase.** If the narrative layer manufactures a moat to make the canvas look complete, it violates A3 and the pack loses the credibility that the empty cell earns it.
2. **Take block 4's third metric — published multi-hop accuracy — into the 295A spike scope.** It is the one key metric that is both measurable this semester and unavailable anywhere in the commercial market.
3. **Test block 5 before building against it.** Priya's objection is the UVP inverted; five analysts and one afternoon settle it.
