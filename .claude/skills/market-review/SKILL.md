---
name: market-review
description: >
  Produce a structured, evidence-based review of stock markets — global indices,
  macro drivers, sectors, commodities, and risk scenarios — grounded in current
  data pulled fresh rather than recalled from training. Use this skill whenever
  the user asks to review, analyze, or summarize the market, wants a read on
  "how markets are doing", asks about the S&P 500 / Nasdaq / Dow / STOXX / Nikkei
  or any index level, asks what's driving stocks right now, wants a macro
  outlook, asks about the Fed / interest rates / inflation in a market context,
  or asks to act as a market or investment expert (including in Arabic —
  "راجع السوق", "تحليل البورصة", "خبير بورصة", "وضع الأسهم"). Also use it for
  weekly/daily market wraps and for scenario analysis around a geopolitical or
  policy event.
---

# Market Review

A market review is only as good as its weakest number. The failure mode isn't
bad analysis — it's confident analysis built on a stale index level or a rate
that changed two meetings ago. Everything below is organized around preventing
that.

## Non-negotiable: refresh the data

**Market data decays faster than almost any other kind of fact.** Index levels,
policy rates, and inflation prints from training data are wrong by default.

Before writing anything, search for current figures. At minimum:

1. Major index levels and the latest close
2. Central bank policy rate and the most recent decision (including the vote
   split — dissents signal where policy is heading)
3. Latest inflation print and the next release date
4. Whatever single factor is currently dominating the tape (an energy shock,
   an election, a credit event, an AI capex cycle)

Run these searches in parallel. Then **date-stamp every figure** in the output.
"S&P 500 at 7,728 (close, 11 Aug 2026)" is verifiable; "the S&P is around 7,700"
is not, and quietly becomes wrong.

If a figure can't be verified, say so rather than filling the gap from memory.
A review with an acknowledged gap is useful; one with a confident wrong number
is worse than nothing.

## Find the dominant variable

Most of the time markets are driven by one thing, and everything else is
commentary. In mid-2026 that was the Strait of Hormuz: it set oil, oil set
inflation, inflation set the Fed, and the Fed set equity multiples. A review
discussing sector rotation without naming that chain would be describing
symptoms.

So before structuring the review, ask: **what single variable, if it changed
tomorrow, would reprice everything?** Build the review around that, and make
the causal chain explicit rather than listing factors side by side.

## Structure

Adapt to the question, but this ordering earns its keep — it moves from what
happened, through why, to what it means:

```
1. Executive summary        — the picture in one table plus one core idea
2. Macro backdrop           — the dominant variable and its transmission chain
3. Regional equity markets  — levels, YTD, valuation, what's moving
4. Sectors                  — where the dislocations are
5. Commodities / safe havens — oil, gold, volatility
6. Risks                    — ranked by expected impact, not listed randomly
7. Scenarios                — 3 branches with probabilities and winners/losers
8. Practical conclusions    — what actually follows from the analysis
9. Sources                  — linked, so every claim is checkable
```

Prefer **tables for numbers, prose for causation**. A wall of figures without
a mechanism is a data dump; a mechanism without figures is an opinion.

## What separates a real review from a market summary

**Name the dislocations.** The value is in finding where price and fundamentals
disagree. "Energy trades at 13.1x forward earnings while growing profits 71%"
is an observation someone can act on. "Energy performed well" is not. Then
explain *why* the market is pricing it that way — usually the market has a
reason, and stating it honestly is more useful than implying the market is
simply wrong.

**Give both sides of every dislocation.** If energy is cheap because the market
expects oil to fall, then the cheap multiple is either an opportunity or a
value trap depending on an unknowable. Say that. Present the conditions under
which each reading is correct.

**Distinguish signal from noise.** A single day's move is usually noise. What
matters: divergences (small caps hitting records while large caps fall),
breadth, reactions that contradict the news (a stock falling on good results),
and cross-asset disagreement (equities calm while bonds or oil are not).

**Watch for internal contradictions in the data.** When semiconductor stocks
sell off hard while hyperscalers guide capex to $750bn, one of those is wrong.
Flag the contradiction rather than reporting both as facts — the resolution is
usually where the interesting analysis lives.

**Rank risks by expected impact.** An unordered risk list is filler. Order by
probability × severity and say which one you'd actually watch.

**Make scenarios falsifiable.** Each branch needs a rough probability, specific
triggers, and named winners and losers. "Markets could go up or down" is not a
scenario.

## Scenario framework

Three branches, always with what would confirm each:

| Branch | Content |
|---|---|
| **Resolution** | The dominant variable resolves favorably. Transmission chain, winners, losers. |
| **Muddle through** | Status quo persists. Usually the highest-probability branch, and the least discussed. |
| **Escalation** | Tail risk. Low probability, high impact. Name the hedges. |

State probabilities explicitly, even roughly. "Most likely" is doing hidden
work that a number makes honest.

## Handling advice

Reviews shade into advice, and this needs care:

- **Analyze the market, not the person.** Explain what's cheap, what's
  expensive, what the risks are. Framing that as what someone *should* do
  requires knowledge of their horizon, obligations, and risk capacity that
  hasn't been shared.
- **Include the bear case for anything presented favorably.** Every dislocation
  has a reason it exists.
- **Never present past performance as forecast.** "Up 31% in seven months" is
  history. Strong starts frequently precede consolidation.
- **Flag the review's own shelf life.** A review written the day before a CPI
  print may be obsolete within hours. Say when the next repricing event is.

## Regional coverage

Cover what's relevant to the asker. Someone in Cairo asking to "review the
market" usually wants both the global picture and Egypt — global markets set
the risk backdrop, but their portfolio is local. Cover both rather than
guessing which they meant.

**For anything involving Egyptian equities, use the `egx-investing` skill** —
Egyptian analysis requires inflation-adjusted returns, currency-bucket
classification, and comparison against the ~19% bank certificate, none of which
apply to developed markets.

Match the output language to the user's. If they write in Arabic, write the
review in Arabic — including Egyptian dialect where they use it. Keep ticker
symbols and index names in their standard form regardless of language.

## Data sourcing

- **WebSearch is the reliable path.** Many financial data sites (investing.com,
  exchange sites, data aggregators) are blocked by egress proxies in sandboxed
  environments. Search results return summarized figures and work consistently.
- **Prefer primary sources for the number that matters most:** central bank
  statements for rates, statistics bureaus for inflation, exchange sites for
  index levels, company IR pages for results.
- **When sources conflict, report the conflict.** Foreign-flow data for the EGX,
  for instance, routinely disagrees depending on whether off-exchange deals are
  counted. Picking one silently is the wrong call — the disagreement is itself
  information.
- **Check article dates.** Financial content resurfaces constantly; a figure
  from months ago reads as current and will corrupt the analysis.
