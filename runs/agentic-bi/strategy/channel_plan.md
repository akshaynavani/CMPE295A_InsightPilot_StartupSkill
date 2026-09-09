# Channel plan

**What this is** — The channel map by segment, with **channel economics**: the discount and margin stack from list price to net, the cost to acquire through each channel, time to first revenue, and a viability verdict at this price point.
**Why it exists** — [gtm.md](gtm.md) names channels; this file computes whether they can pay for themselves. The distinction matters because a $900 ACV silently disqualifies most enterprise channels, and a plan that names a partner channel without computing the margin stack is asserting distribution rather than planning it. The specific failure prevented: a later phase proposing a reseller or cloud-marketplace motion that the arithmetic here already rules out.
**How to read it** — §2's viability column is the output; §3 shows the arithmetic that produces it. A skeptic should attack §4, which argues the only viable channel is the one with no revenue attached.
**Depends on / feeds** — Inherits price from [market_sizing.md](market_sizing.md) §2.3, channels from [gtm.md](gtm.md), and source petals from [petal_diagram.md](petal_diagram.md). Feeds [sales_roadmap.md](sales_roadmap.md) and the `financials/` unit-economics model.

---

## 1. The price point that governs everything

**List: $75/analyst/month = $900/analyst/year** *(assumption: top of the observed analyst-tool band `[S44][S52]`; a falsifiable threshold, not a validated willingness to pay — [market_sizing.md](market_sizing.md) §2.3.)*

A realistic initial account is **5–15 analysts**, since the beachhead sits in central analytics teams of roughly that size ([personas.md](personas.md) §2). That gives an **initial ACV of $4,500–13,500**, with $9,000 (10 analysts) as the working figure.

**This number disqualifies channels before any strategy is applied.** A $9,000 ACV cannot carry a field sales motion, a reseller margin, or a marketplace fee stacked on top of a partner discount. §3 shows why.

## 2. Channel map and viability

| Channel | Segment served | Time to first revenue | Cost to acquire | Viable at $900/seat? |
|---|---|---|---|---|
| **Open-source self-serve** | Priya (petal 1) | **Never directly** — produces users, not revenue | Fixed engineering cost on docs and quickstart; ≈$0 marginal | **Yes — the only fully viable channel.** §4 |
| **Analyst-led referral (internal expansion)** | Priya → Angela | 3–9 months from first install *(assumption)* | ≈$0 marginal | **Yes.** The compounding channel |
| **Community participation** | Priya, Dr. Chen | Indirect, unattributable | Founder hours | **Yes, as credibility.** Do not attribute revenue to it |
| **Technical content / published benchmark** | Priya, Dr. Chen | Indirect | Front-loaded, then amortises | **Yes.** Highest-leverage non-revenue channel |
| **Inside sales / outbound** | Angela | 3–6 months | $3,000–8,000 per closed account *(assumption: standard B2B ranges; no funnel data)* | **No — see §3.1** |
| **Field sales** | Angela at large enterprise | 6–12 months | $15,000+ fully loaded *(assumption)* | **No.** Would need a 17+ seat account just to repay acquisition |
| **Reseller / SI partner** | Enterprise | 9–18 months | Partner margin 20–35% *(assumption: standard channel ranges)* | **No — see §3.2** |
| **Cloud marketplace (AWS/Azure/GCP)** | Enterprise procurement | 6–12 months | 3–5% listing fee *(assumption)* plus engineering to list | **Not yet.** Fee is survivable; the effort is not, pre-revenue |
| **Paid acquisition** | — | — | High, poor intent match | **No.** The beachhead does not find infrastructure tools through ads |

## 3. The margin stack, computed

### 3.1 Why outbound fails

At a $9,000 ACV (10 analysts):

```
List ACV                                        $9,000
Acquisition cost (inside sales, mid estimate)  −$5,500
                                               ───────
Gross contribution, year 1                      $3,500
Less cost-to-serve (inference, support)         −  ?    → financials/
```

**Payback is ~7 months at best, on a gross basis, before any cost-to-serve** — and that assumes a 10-analyst account closes on the first attempt. At the low end of account size (5 analysts, $4,500 ACV), acquisition cost **exceeds first-year revenue**. Outbound requires either a much larger account or a much higher price, and neither is available: the price is anchored to what comparable analyst tools charge `[S44][S52]`, and the account size is bounded by how many analysts sit on a central team.

### 3.2 Why the reseller channel fails

The margin stack, using standard ranges:

| Step | Value |
|---|---|
| List | $9,000 |
| Partner discount (−28%, mid of 20–35%) | −$2,520 |
| **Net to vendor** | **$6,480** |
| Marketplace fee if stacked (−4%) | −$360 |
| **Net after both** | **$6,120 (68% of list)** |

**A 32% haircut is survivable in isolation.** What is not survivable is what the partner is being paid *for*. A reseller adds value by carrying a complex sale into an account they already own — but this product's whole GTM premise is that the analyst installs it themselves without a sale ([gtm.md](gtm.md) §3). **Paying 28% for a sales motion the product is designed not to need is paying for the wrong thing.** The channel is not disqualified by the margin; it is disqualified by redundancy.

### 3.3 Why open-source self-serve works

```
Marginal cost to acquire the next user     ≈ $0
Fixed cost                                 = engineering hours on docs + quickstart
Amortisation                               = across every install, forever
```

The economics invert the usual problem: the constraint is not cost per acquisition but **conversion quality**, which is governed by one number — median time from clone to first successful investigation. [business_model_canvas.md](business_model_canvas.md) row 4 sets the threshold at 30 minutes and makes it a falsifiable hypothesis.

**Wren AI is the proof this channel can carry a product of this shape**: 13,000+ GitHub stars and 10,000+ cloud users on an open-source-led motion `[S50]`. It is also the warning — that is the incumbent in this channel, and it has a two-year head start.

## 4. The decision, and the tension in it

**Run one channel: open-source self-serve, with analyst-led referral as its expansion path. Nothing else, for 90 days.**

The tension worth naming: **the only channel whose economics work at this price is the one that produces no revenue.** That is not a flaw in the analysis, it is the actual shape of open-core distribution — adoption precedes revenue structurally, because the source petal has no budget line ([petal_diagram.md](petal_diagram.md) §5.1).

For CMPE 295A/295B this resolves cleanly: monetisation is out of scope (A1), so a channel that produces users and evidence is exactly the right one. **For the venture framing in `narrative/`, it must be stated rather than glossed** — the honest sentence is that this business would have to convert free adoption into paid seats through internal expansion, and that conversion is untested.

**What would change the decision.** If the buyer conversation ([business_model_canvas.md](business_model_canvas.md) row 5) reveals accounts materially larger than 10 analysts — a 50-analyst central team at a large enterprise gives a $45,000 ACV — inside sales becomes viable and this file should be rewritten. That is one question in one conversation, and it is worth asking early.

## 5. Channel conflict

Minimal by construction, and worth recording so a later phase does not create it:

- **Open core versus paid seats.** The classic open-source tension. Not resolved here; A5 settles the deployment model but not the open-core boundary — which features are free and which are paid is an open question for `financials/`.
- **Self-serve versus design partners.** The first 10 get hands-on help that later users will not. This is correct for discovery and creates a false read on the quickstart metric — **instrument the two cohorts separately** or row 4's hypothesis will be measured wrong.
- **No reseller conflict**, because there is no reseller. Recorded so that adding one later is recognised as a real change to this plan rather than an incremental addition.

## Recommended next 3

1. **Instrument clone → first successful investigation from day one, split by cohort.** It is the only channel metric that matters, it decides whether the sole viable channel actually works, and it cannot be reconstructed after the fact.
2. **Ask the account-size question in the first buyer conversation.** How many analysts sit on the central team? It is the single input that determines whether §3.1's verdict on outbound holds, and it takes ten seconds to ask.
3. **Do not list on a cloud marketplace, take a partner meeting, or write a cold-outbound sequence during 295A/295B.** Each is ruled out by the arithmetic above, and each would consume engineering hours the compounding channel needs. If a later phase proposes one, this file is the reason to say no.
