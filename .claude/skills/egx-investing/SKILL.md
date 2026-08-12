---
name: egx-investing
description: >
  Analyze and invest in Egyptian stocks on the Egyptian Exchange (EGX) — how the
  market mechanically works (trading hours, T+2 settlement, stamp duty, unified
  code, brokers), how to value Egyptian companies in a high-inflation EGP economy,
  how to screen and size positions, and what the sector landscape looks like.
  Use this skill whenever the user mentions the Egyptian stock market, EGX, EGX30,
  EGX70, EGX100, البورصة المصرية, أسهم مصرية, or any Egyptian listed company
  (CIB/COMI, Talaat Moustafa/TMGH, Elsewedy/SWDY, Abu Qir/ABUK, Eastern/EAST,
  Juhayna/JUFO, Fawry, e-finance/EFIH, Palm Hills/PHDC, Ezz Steel/ESRS,
  EFG/HRHO, Telecom Egypt/ETEL). Also use it whenever someone asks how to start
  investing in Egypt, compares Egyptian stocks to bank certificates (الشهادات),
  asks about EGP currency risk in an equity portfolio, or wants an Egyptian
  company's results analyzed — even if they never say the word "EGX".
---

# Investing in Egyptian Stocks (EGX)

Egypt is not a market you can analyze with imported US habits. A 25% annual
return sounds spectacular until you learn inflation ran 16–17% and a risk-free
bank certificate paid 19%. Everything here — valuation, position sizing, what
counts as "good" — has to be measured against a moving local yardstick.

This skill exists so that analysis of Egyptian equities is done in the frame
that actually applies: **real returns in a high-inflation, currency-fragile,
high-risk-free-rate economy.**

## The one rule that governs everything

**Never quote an Egyptian return without stating what it beat.**

A nominal number is meaningless on its own. Three benchmarks matter, always:

| Benchmark | Why it matters |
|---|---|
| **Inflation** (~16–17% expected avg 2026) | Below this, purchasing power shrank |
| **Risk-free rate** (CBE deposit ~19%) | Below this, the investor took risk for nothing |
| **USD** (EGP ~46.8, models point to 52–55) | Below this, wealth fell in hard-currency terms |

So a stock up 20% in a year **lost** to a bank certificate, roughly matched
inflation, and may have lost badly in dollars. Say that plainly. This single
discipline prevents most bad advice about this market.

When the user gives a return, compute the real return and the USD-adjusted
return, and lead with those. `scripts/egx_calc.py` does this arithmetic.

## Workflow for analyzing an Egyptian stock

Work through these in order. Skip a step only when the data genuinely isn't
available, and say so rather than guessing.

### 1. Establish the macro frame first
Pull current inflation, CBE rates, and the EGP level before touching the
company. The same P/E means completely different things at 19% risk-free vs 9%.
Rates and inflation change fast in Egypt — verify, don't recall.

### 2. Earnings growth vs. inflation
This is the primary screen. A company growing profit 10% while inflation is 17%
is **shrinking in real terms** even though the headline is positive. Egyptian
income statements are inflated by definition — nominal growth is the default,
not an achievement.

The bar is: **profit growth > inflation**, ideally by a wide margin.

### 3. Currency exposure — the highest-leverage question
Classify the company:

- **Exporter / USD earner** (fertilizers, some industrials): revenue in hard
  currency, costs in EGP. **Devaluation is a tailwind.** Natural hedge.
- **Domestic EGP earner** (banks, retail, local real estate): devaluation
  compresses dollar value even when local results look fine.
- **Importer / USD cost base** (some manufacturers, distributors): devaluation
  is a direct margin hit. Most dangerous category.

This classification often matters more than valuation. Lead with it.

### 4. Margins, not just revenue
Egyptian revenue rises with inflation automatically — that tells you almost
nothing. The real question is whether margins are expanding or being crushed
by input costs.

**Revenue up + profit down is a red flag, not a mixed result.** It means the
company cannot pass costs to customers, which in a high-inflation economy is
a structural weakness, not a bad quarter.

### 5. Sector-specific accounting traps
Egyptian sectors have quirks that break naive analysis. Read
`references/sectors.md` before analyzing any company — particularly real
estate (where contracted sales and recognized revenue diverge enormously) and
banks (where high rates flatter net interest income).

### 6. Valuation against the local alternative
Convert P/E into earnings yield (`1 ÷ P/E`) and compare it directly to the bank
certificate rate. At a P/E of 8, earnings yield is 12.5% — which is *below* a
19% certificate. The equity only wins if earnings grow. Make that comparison
explicit; it's the calculation most retail investors skip.

Dividend yields of 5–15% are common in Egyptian blue chips, so include the
dividend in the comparison.

### 7. Liquidity and concentration risk
The EGX30 is heavily concentrated — the top three names have historically been
around half the index weight. Buying "the index" is closer to buying three
companies. And a position that takes days to exit isn't really liquid. Check
average traded value before sizing anything.

### 8. Size the position by risk, not conviction
Use `scripts/egx_calc.py` for position sizing from a stop-loss distance and a
fixed risk budget. Conviction is not a sizing input — it's the thing most
likely to be wrong.

## Reference material

Load these as needed rather than all at once:

- **`references/mechanics.md`** — trading hours, T+2 settlement, stamp duty
  rates, unified code, broker selection, order types, account opening. Read
  this for any "how do I actually buy" question.
- **`references/sectors.md`** — sector map, the accounting traps in each, and
  the major listed names. Read this before analyzing a specific company.
- **`references/analysis.md`** — valuation methods adapted for high inflation,
  the real-return math, currency hedging logic, and a due-diligence checklist.
  Read this for valuation or portfolio construction questions.

## Scripts

**`scripts/egx_calc.py`** — the calculations that get done wrong by hand:

```bash
python3 scripts/egx_calc.py real-return --nominal 31.2 --inflation 16.5
python3 scripts/egx_calc.py usd-return --nominal 31.2 --fx-start 47.8 --fx-end 52.0
python3 scripts/egx_calc.py position-size --capital 500000 --risk-pct 1.5 --entry 95 --stop 86
python3 scripts/egx_calc.py cost --value 100000 --commission-pct 0.1 --flat-fee 2
python3 scripts/egx_calc.py compare --pe 8 --div-yield 6 --growth 25 --certificate 19
```

Run `python3 scripts/egx_calc.py --help` for the full set. Use it rather than
doing this arithmetic inline — the compounding and fee interactions are easy to
get subtly wrong, and a wrong real-return number invalidates the whole analysis.

## Getting current data

Market data goes stale immediately, and several major financial data sites are
blocked in sandboxed environments. Practical approach:

- **WebSearch works well** and returns summarized figures — prefer it over
  fetching data-site URLs directly.
- Good Arabic sources: مصراوي, أموال الغد, البورصة نيوز, جريدة المال,
  إنتربرايز مصر, حابي. English: Enterprise, Daily News Egypt, Zawya.
- Official: the EGX site and company investor-relations pages carry the
  authoritative filings.
- **Always date-stamp figures.** Egyptian market articles resurface constantly,
  and an old market-cap or index number will silently corrupt an analysis.
  If two sources conflict (common with foreign-flow data, where scope differs
  on whether off-exchange deals are included), report the conflict rather
  than silently picking one.

## Honesty requirements

This domain touches people's savings, so a few things are non-negotiable:

- **Distinguish education from personalized advice.** Explain mechanisms,
  frameworks, and trade-offs. Don't issue buy/sell calls dressed as certainty,
  and don't imply knowledge of the user's finances, obligations, or risk
  capacity that hasn't been shared.
- **State the bear case for anything presented favorably.** A cheap multiple in
  Egypt usually reflects real risk — currency, liquidity, governance,
  concentration. Cheap and risky are not opposites here; they're usually the
  same sentence.
- **Flag when numbers are unverified or stale.** "As of [date], per [source]"
  costs one clause and prevents real harm.
- **Never present past performance as a forecast.** A market up 31% in seven
  months is a fact about the past, not a projection.
