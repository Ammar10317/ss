# EGX Mechanics — How the Market Actually Works

Facts current as of **August 2026**. Rules and rates in Egypt change with
budget cycles and regulatory decisions — verify anything that drives a real
decision, especially tax rates and fees.

## Contents

- [Trading calendar and hours](#trading-calendar-and-hours)
- [Settlement](#settlement)
- [Taxes and transaction costs](#taxes-and-transaction-costs)
- [Opening an account](#opening-an-account)
- [Brokers](#brokers)
- [The indices](#the-indices)
- [Order types and execution](#order-types-and-execution)
- [Total cost of a round trip](#total-cost-of-a-round-trip)

---

## Trading calendar and hours

| Item | Detail |
|---|---|
| Trading days | **Sunday to Thursday** |
| Weekend | Friday and Saturday |
| Pre-opening session | 09:30 – 10:00 Cairo time |
| Continuous trading | **10:00 – 14:30** Cairo time (EET, UTC+2) |

During the pre-opening session orders can be entered, modified, or cancelled
but **nothing executes**. Prices you see then are indicative — an order sitting
in pre-open is not a fill.

**The Sunday–Thursday week matters more than it looks.** Egypt trades while the
US and Europe are closed on Sunday, and is closed on Friday when they trade.
So global news breaking Friday afternoon hits the EGX all at once on Sunday
morning, with a two-day gap of accumulated reaction. Gap risk on Sunday opens
is structurally higher than in Western markets, and stop-loss orders offer
much weaker protection across that gap.

The exchange also closes for Egyptian public and religious holidays, which move
with the Hijri calendar. Check the EGX holiday calendar before assuming a
settlement date.

## Settlement

**T+2** for most listed equities: a trade on Sunday settles Tuesday.

Clearing runs through **MCDR** (Misr for Central Clearing, Depository and
Registry) on a **Delivery versus Payment (DvP)** basis — MCDR acts as clearing
house between the buying and selling member firms, so neither side can take
delivery without paying.

Practical consequence: **sale proceeds are not immediately withdrawable.** Sell
on Monday, cash is available Wednesday. Anyone planning around a specific cash
date needs to count settlement days, not calendar days — and Egyptian holidays
extend the chain.

## Taxes and transaction costs

Egypt made a **structural change in 2026** that materially improves the
after-tax case for equities.

### Capital gains — exempt

Capital gains realized on the trading and disposal of **securities listed on
the EGX** are **exempt from income tax**, for individuals and corporates alike.

### Stamp duty — the replacement

| Transaction | Rate |
|---|---|
| Ordinary buy or sell | **0.05%** on the buyer **and** 0.05% on the seller |
| Intraday (buy and sell in the same session) | **0.025%** each side |
| Market makers (licensed under the Capital Market Law) | Exempt |

MCDR began withholding stamp duty on settlements processed from
**3 August 2026**.

### Why this matters more than the headline rate

The old capital gains regime taxed *success* — profitable trades were penalized
and record-keeping was a burden. Stamp duty is a **known, tiny, symmetrical
cost paid regardless of outcome**. For a long-term holder it is close to
negligible: 0.05% each way on a position held for years rounds to nothing.

The halved intraday rate is a deliberate liquidity incentive. Note the
asymmetry: it rewards *closing the same day*, not frequent trading generally.
Holding overnight and selling tomorrow pays the full rate on both legs.

### Dividends

Dividend taxation is a separate regime from capital gains and has been changed
repeatedly. **Verify the current dividend withholding treatment before
modeling after-tax income** — the capital gains exemption above does not
automatically extend to dividends.

## Opening an account

Four steps, generally completable in days:

1. **Choose a broker** — see below.
2. **Submit documents** — a copy of a valid national ID (بطاقة الرقم القومي),
   completed client data forms, and signed securities dealing contracts.
   Non-Egyptians need passport and additional documentation.
3. **Obtain the unified code (الكود الموحد)** — a single investor identifier
   used across the entire market, arranged by the broker. This is the identity
   that follows the investor between brokers; it is not per-broker.
4. **Fund the account** and trade.

Many brokers now complete this **fully remotely** through their apps.

**Minimum capital:** traditional brokers typically want a portfolio of
**EGP 20,000–25,000**. App-based brokers may have **no minimum at all**.

## Brokers

Two broad categories, and the right choice depends on what the investor
actually needs:

**App-first / digital** (e.g. Thndr) — fast remote onboarding, low or no
minimum, simple interface, competitive commissions. Thndr's published pricing
is **EGP 2 per order + 0.1% of order value**. Best for smaller portfolios and
self-directed investors.

**Full-service / institutional** (e.g. EFG Hermes and its EFG Hermes ONE app,
and other established houses) — research coverage, analyst reports, IPO
access, regional products, advisory. Higher minimums. Worth it mainly for the
research if the investor will actually read it.

### What to compare

- **Commission structure** — flat fee, percentage, or both. Flat fees dominate
  the cost of small orders; percentages dominate large ones.
- **Regulatory standing** — the broker must be a licensed EGX member firm
  registered with the **FRA** (Financial Regulatory Authority). Verify this
  independently on the EGX member list. Unlicensed "brokers" promising EGX
  access are a recurring scam pattern.
- **Execution quality and platform stability** — an app that fails during a
  volatile open is a real, recurring cost.
- **Research access** — only valuable if it will be used.
- **Custody arrangements** — understand where the securities are actually held.

## The indices

| Index | What it covers |
|---|---|
| **EGX 30** | The 30 most liquid and active companies. Market-cap weighted, **adjusted by free float**. The headline index. |
| **EGX 30 Capped** | Same constituents with a cap on individual weights — a direct remedy for the concentration problem below. |
| **EGX 70** | Small and mid caps, **excluding** the EGX 30 constituents. |
| **EGX 100** | EGX 30 + EGX 70 combined — the broadest common gauge. |

### The concentration problem

The EGX 30 is meaningfully concentrated: the top three constituents —
**Commercial International Bank (CIB)**, **Talaat Moustafa Group**, and
**Elsewedy Electric** — have historically accounted for roughly **half the
index weight**.

Two consequences worth stating whenever the index is discussed:

1. **"Buying the EGX 30" is closer to buying three companies** than to
   diversified market exposure. CIB alone can move the index — the index
   rallied on CIB's results in July 2026.
2. **EGX 30 vs EGX 70/100 divergence is informative.** When the EGX 30 falls
   while the EGX 70 and EGX 100 hit records (as on 10 August 2026), money is
   rotating from large caps into small and mid caps. That is genuine market
   breadth, but it also signals a more speculative phase.

For diversified exposure, the **EGX 30 Capped** or a broader index is the more
honest instrument.

## Order types and execution

Standard order types are available — market, limit, stop. Two Egypt-specific
cautions:

**Price limits / circuit breakers.** The EGX applies daily price movement
limits on individual securities, with trading halts when breached. Thresholds
differ by security and have been revised over time. A limit order beyond the
band simply will not execute, and a halted stock cannot be exited at any price.

**Liquidity is the binding constraint outside the large caps.** Many listed
Egyptian companies trade thinly. Check **average daily traded value** before
sizing a position — a stock that trades EGP 2m a day cannot absorb an EGP 500k
exit without moving against the seller. Market orders in illiquid names are how
retail investors get filled at prices they didn't expect. **Use limit orders
outside the most liquid names.**

## Total cost of a round trip

Add these up before assuming a trade is profitable:

| Component | Typical |
|---|---|
| Broker commission (buy) | ~0.1% + any flat fee |
| Stamp duty (buy) | 0.05% |
| Broker commission (sell) | ~0.1% + any flat fee |
| Stamp duty (sell) | 0.05% |
| **Round-trip total** | **~0.3%** plus flat fees |
| Bid-ask spread | Variable — often the largest cost in illiquid names |

Additional EGX/MCDR/FRA service fees may apply depending on the broker's
schedule; check the actual contract rather than the marketing page.

**The spread is the hidden cost.** In a thinly traded stock the spread can
exceed every explicit fee combined. Use `scripts/egx_calc.py cost` to compute
explicit costs, then add a realistic spread estimate on top — and note that
frequent trading turns a 0.3% round trip into a serious annual drag: twenty
round trips a year is roughly 6% of capital before a single decision is
evaluated.
