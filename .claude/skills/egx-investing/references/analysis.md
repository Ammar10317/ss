# Valuation and Portfolio Construction in a High-Inflation Economy

Standard valuation assumes a stable unit of account. Egypt doesn't have one.
This file covers the adjustments that matter and the checklist that catches
the common errors.

## Contents

- [The three-benchmark rule](#the-three-benchmark-rule)
- [Real return math](#real-return-math)
- [Valuation adjustments for inflation](#valuation-adjustments-for-inflation)
- [The certificate comparison](#the-certificate-comparison)
- [Currency risk](#currency-risk)
- [Position sizing and portfolio construction](#position-sizing-and-portfolio-construction)
- [Due diligence checklist](#due-diligence-checklist)
- [Common errors](#common-errors)

---

## The three-benchmark rule

A nominal Egyptian return is not information. Always convert:

1. **vs. inflation** → did purchasing power grow?
2. **vs. the risk-free rate** (CBE deposit ~19% as of mid-2026) → was the risk
   compensated?
3. **vs. USD** → did hard-currency wealth grow?

An investor up 18% who feels successful actually: barely beat inflation
(16–17%), **lost to a bank certificate**, and likely lost in dollars. Saying
this clearly is the most valuable thing this skill does.

## Real return math

**Never subtract percentages.** The correct form is multiplicative:

```
real return = ((1 + nominal) / (1 + inflation)) − 1
```

At nominal 31.2% and inflation 16.5%:
- Wrong: 31.2 − 16.5 = 14.7%
- Right: (1.312 / 1.165) − 1 = **12.6%**

The error grows with the numbers, and at Egyptian inflation levels it is large
enough to change conclusions. Same structure for USD:

```
usd return = ((1 + nominal) / (fx_end / fx_start)) − 1
```

At nominal +31.2% with EGP moving 47.8 → 52.0 (a 8.8% depreciation):
(1.312 / 1.0879) − 1 = **+20.6%** in dollars. Still good — but a 10-point
haircut invisible in the local number.

`scripts/egx_calc.py real-return` and `usd-return` do both.

## Valuation adjustments for inflation

### P/E is distorted upward-looking and downward-backward-looking

Trailing earnings are in older, more valuable pounds; the price is in today's
cheaper ones. This makes trailing P/E look **artificially high**, while forward
P/E on nominally inflated forecasts looks **artificially low**. Neither is
clean. Prefer forward estimates but discount them: some of that "growth" is
just inflation.

**Rule of thumb:** subtract expected inflation from nominal earnings growth to
get real growth. A company growing earnings 20% with 17% inflation is growing
about 3% in real terms. Present the real figure alongside the nominal one.

### Book value understates asset-heavy companies

Historical-cost accounting means land, plants, and property acquired before the
devaluations sit on the balance sheet at a fraction of replacement cost. So
**P/B below 1 is common and often misleading** for developers and industrials
with old land banks. Where possible, ask what the assets would cost to replace
today.

### Debt is quietly forgiven

Fixed-rate EGP debt is inflated away — a real transfer from lenders to
borrowers. A leveraged domestic company with EGP-denominated fixed-rate debt is
in a better position than its leverage ratio suggests. **The reverse is
brutal:** USD-denominated debt grows in EGP terms with every devaluation. When
reviewing leverage, always ask **what currency the debt is in** — it matters
more than the amount.

### Dividend yield is the cleanest local signal

Cash is cash and cannot be accounting-inflated. Egyptian blue chips commonly
yield **5–15%**. Compare that directly to the certificate rate — that's a
comparison of two cash streams with no accounting judgment in between.

Caveats: check payout **sustainability** (is it covered by earnings and cash
flow?), and never model income off a *proposed* dividend — Eastern Company's
board proposed EGP 2.85 and the assembly approved EGP 1.45.

## The certificate comparison

This is the calculation Egyptian retail investors most often skip.

**Earnings yield = 1 ÷ P/E.** At a market P/E of 8, that's **12.5%** — below a
19% bank certificate. So on a static basis, the certificate wins.

Equities only win through **growth**. The rough comparison:

```
equity expected return ≈ dividend yield + real earnings growth + multiple change
certificate return     = ~19% nominal, 2–3% real, zero USD protection
```

The equity case in Egypt rests on three things the certificate cannot offer:

1. **Earnings growing faster than inflation** — CIB +28.6%, Abu Qir +119%,
   Juhayna +77% all comfortably clear a 16–17% bar.
2. **Currency protection through USD earners** — a certificate is 100% EGP
   exposure with no hedge.
3. **Multiple expansion** — at 6–10x versus 15–20x for emerging markets
   generally, there is room, though it may never close.

And the honest counterpoints: the certificate is **capital-guaranteed**,
requires no analysis, and 19% is genuinely high. **For an investor who needs
the money within a couple of years, the certificate is usually the better
answer** — equities need time for the growth argument to play out, and Egyptian
equities are volatile enough that a two-year horizon is closer to a coin flip.

`scripts/egx_calc.py compare` runs this comparison.

## Currency risk

The most under-modeled risk in Egyptian portfolios. EGP was around **46.8/USD**
in August 2026 (up ~2% YTD, strongest since May 2024) with forecasting models
pointing toward **52–55**.

Egypt's history is of **long stable periods punctuated by sharp step
devaluations**, not gradual drift. So "the pound has been stable this year" is
not evidence of safety — it is often what the run-up to a step looks like.

### Managing it

- **Hold bucket-one companies** (USD earners — see `sectors.md`). This is the
  only hedge available *inside* an EGX portfolio.
- **Match currency to liability.** Someone saving for local expenses in EGP has
  far less currency risk than someone saving for tuition abroad. Ask what the
  money is *for* before assessing exposure.
- **Report returns in both currencies.** Always.
- **Diversify outside Egypt** where the investor legally can — though note
  that capital controls and remittance restrictions have periodically limited
  this in practice.

## Position sizing and portfolio construction

### Size by risk, not conviction

```
position size = (capital × risk %) / (entry − stop)
```

Risking 1.5% of EGP 500,000 (= EGP 7,500) on a stock entered at 95 with a stop
at 86 (EGP 9 of risk per share) gives 833 shares ≈ EGP 79,167, about 16% of
capital. `scripts/egx_calc.py position-size` handles this.

Conviction is not a sizing input. The positions people feel most certain about
are disproportionately represented in large losses.

### Egypt-specific sizing constraints

- **Liquidity cap.** Never hold more than a small fraction of a stock's average
  daily traded value. If exiting takes more than a day or two of normal volume,
  the position is too big regardless of what the risk formula says.
- **Gap risk breaks stops.** The Sunday–Thursday week means two days of global
  news hit at once on Sunday's open. Stops do not protect across a gap. Size
  assuming the stop may fill materially worse than intended.
- **Index concentration.** If the portfolio holds CIB, TMG, and Elsewedy plus
  an EGX 30 tracker, it is far more concentrated than the position count
  suggests — those three are roughly half the index.
- **Correlation clustering.** Egyptian stocks are heavily driven by common
  macro factors (EGP, CBE rates, fiscal policy). Ten Egyptian stocks are not
  ten independent bets. Genuine diversification comes mainly from the
  **currency-bucket** split, not from the number of holdings.

### A sane structure

Rather than prescribing an allocation — which depends on circumstances only the
investor knows — the dimensions that matter:

- **Certificate/cash vs. equity split** driven by time horizon. Money needed
  within ~2 years generally does not belong in EGX equities.
- **Within equities: currency-bucket balance.** Some USD-earner exposure to
  offset the EGP-domestic majority.
- **Dividend payers** as a partial inflation-income offset.
- **Position count** high enough to survive one blow-up, low enough to actually
  monitor.

## Due diligence checklist

Before any Egyptian position:

**Macro frame**
- [ ] Current inflation rate and CBE policy rates verified (not recalled)
- [ ] Current EGP level and recent trajectory
- [ ] Is the rate cycle cutting or hiking?

**Company financials**
- [ ] Earnings growth **vs. inflation** — real or nominal-only?
- [ ] Margin direction — expanding or compressing?
- [ ] Revenue growth decomposed: price vs. volume
- [ ] Currency bucket classified (USD earner / domestic / USD cost base)
- [ ] Debt: how much, **what currency**, fixed or floating
- [ ] Cash flow supports reported earnings
- [ ] Dividend covered and **declared** (not merely proposed)

**Sector-specific** (see `sectors.md`)
- [ ] Real estate: backlog, collection period, down payment %, land basis
- [ ] Banks: NII vs fee mix, sovereign exposure, asset quality
- [ ] Fertilizers/chemicals: gas supply and pricing policy, commodity cycle position
- [ ] Consumer: pricing power evidence, imported input exposure

**Valuation**
- [ ] Earnings yield vs. certificate rate
- [ ] P/E against the company's own history and sector peers
- [ ] Dividend yield and sustainability
- [ ] Is the low multiple cheapness or a warning?

**Risk**
- [ ] Average daily traded value vs. intended position size
- [ ] Governance: free float, controlling shareholder, related-party dealings
- [ ] Regulatory/political exposure (gas pricing, excise taxes, price controls,
      government contracts)
- [ ] What would have to be true for this to lose half its value?

**Portfolio fit**
- [ ] Position sized by stop distance and risk budget
- [ ] Currency-bucket balance across holdings
- [ ] Correlation with existing positions
- [ ] Time horizon matches the thesis

## Common errors

**Subtracting inflation instead of dividing.** Overstates real return at
Egyptian inflation levels by enough to change decisions.

**Quoting EGP returns to someone who thinks in dollars.** Ask which currency
the investor's goals are denominated in before reporting performance.

**Treating a low P/E as automatic value.** Egyptian multiples are low for
reasons — currency, liquidity, governance, sovereign risk. Cheap and risky are
usually the same sentence here.

**Ignoring the certificate.** A 19% guaranteed alternative is the hurdle rate.
Any equity recommendation has to clear it explicitly.

**Confusing contracted sales with revenue** in real estate. See `sectors.md`.

**Celebrating revenue growth in an inflationary economy.** Revenue rises with
inflation automatically. Margins are the signal.

**Assuming the index is diversified.** Three names, roughly half the weight.

**Extrapolating a strong run.** A market up 31% in seven months is a fact about
the past. Strong starts are frequently followed by consolidation, and the
sharper the run the more violent the eventual correction tends to be.

**Using stale figures.** Egyptian financial articles resurface constantly and
market-cap and index numbers from months ago read as current. Date-stamp
everything.
