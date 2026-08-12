#!/usr/bin/env python3
"""EGX investing calculations.

The arithmetic in this file is easy to get subtly wrong by hand — real returns
compound rather than subtract, and at Egyptian inflation levels the difference
is large enough to flip a conclusion. Use these commands instead of estimating
inline.

Run `python3 egx_calc.py --help` for the command list, or
`python3 egx_calc.py <command> --help` for a specific one.
"""

from __future__ import annotations

import argparse
import sys

# Defaults reflect the Egyptian macro backdrop as of August 2026. They are
# starting points, not current truth — rates and FX move, so pass explicit
# values whenever the real figures are known.
DEFAULT_INFLATION = 16.5
DEFAULT_CERTIFICATE = 19.0
STAMP_DUTY_PCT = 0.05
STAMP_DUTY_INTRADAY_PCT = 0.025


def _pct(x: float) -> str:
    return f"{x:+.2f}%"


def _egp(x: float) -> str:
    return f"EGP {x:,.2f}"


def _verdict(real: float) -> str:
    if real > 5:
        return "Grew purchasing power meaningfully."
    if real > 0:
        return "Grew purchasing power, but only just."
    return "LOST purchasing power despite a positive nominal return."


def real_return(args: argparse.Namespace) -> None:
    """Inflation-adjusted return. Divide, never subtract."""
    nominal, inflation = args.nominal / 100, args.inflation / 100
    real = ((1 + nominal) / (1 + inflation) - 1) * 100
    naive = args.nominal - args.inflation

    print("Real (inflation-adjusted) return")
    print("=" * 46)
    print(f"  Nominal return       {_pct(args.nominal)}")
    print(f"  Inflation            {args.inflation:.2f}%")
    print("-" * 46)
    print(f"  REAL RETURN          {_pct(real)}")
    print()
    print(f"  Naive subtraction would say {_pct(naive)} — overstating by")
    print(f"  {abs(naive - real):.2f} points. Real returns compound:")
    print("  ((1 + nominal) / (1 + inflation)) - 1")
    print()
    print(f"  {_verdict(real)}")

    if args.certificate is not None:
        cert_real = ((1 + args.certificate / 100) / (1 + inflation) - 1) * 100
        gap = real - cert_real
        print()
        print(f"  vs. a {args.certificate:.2f}% bank certificate:")
        print(f"    certificate real return   {_pct(cert_real)}")
        print(f"    difference                {_pct(gap)}")
        if gap < 0:
            print("    -> The risk-free certificate BEAT this. The risk")
            print("       taken was not compensated.")
        else:
            print("    -> Beat the risk-free alternative.")


def usd_return(args: argparse.Namespace) -> None:
    """Return converted into USD terms via the EGP/USD move."""
    nominal = args.nominal / 100
    fx_ratio = args.fx_end / args.fx_start
    usd = ((1 + nominal) / fx_ratio - 1) * 100
    depreciation = (fx_ratio - 1) * 100

    print("USD-adjusted return")
    print("=" * 46)
    print(f"  Nominal EGP return   {_pct(args.nominal)}")
    print(f"  EGP/USD start        {args.fx_start:.3f}")
    print(f"  EGP/USD end          {args.fx_end:.3f}")
    print(f"  EGP depreciation     {depreciation:+.2f}%")
    print("-" * 46)
    print(f"  USD RETURN           {_pct(usd)}")
    print()
    print(f"  Currency cost this period: {args.nominal - usd:.2f} points.")
    if usd < 0 < args.nominal:
        print("  WARNING: positive in pounds, NEGATIVE in dollars.")
    print()
    print("  Which number matters depends on what the money is for.")
    print("  Local spending -> EGP. Travel, tuition, imports -> USD.")


def position_size(args: argparse.Namespace) -> None:
    """Risk-based sizing: how many shares to buy given a stop-loss."""
    risk_per_share = args.entry - args.stop
    if risk_per_share <= 0:
        sys.exit("Error: stop must be below entry for a long position.")

    risk_budget = args.capital * args.risk_pct / 100
    shares = int(risk_budget / risk_per_share)
    value = shares * args.entry
    pct_of_capital = value / args.capital * 100
    stop_pct = risk_per_share / args.entry * 100

    print("Risk-based position size")
    print("=" * 46)
    print(f"  Capital              {_egp(args.capital)}")
    print(f"  Risk budget          {args.risk_pct:.2f}% = {_egp(risk_budget)}")
    print(f"  Entry / stop         {args.entry:.2f} / {args.stop:.2f}")
    print(f"  Risk per share       {_egp(risk_per_share)} ({stop_pct:.2f}%)")
    print("-" * 46)
    print(f"  SHARES               {shares:,}")
    print(f"  POSITION VALUE       {_egp(value)}")
    print(f"  % of capital         {pct_of_capital:.2f}%")

    if pct_of_capital > 100:
        print()
        print("  IMPOSSIBLE: exceeds total capital. The stop is too tight")
        print("  for this risk budget — widen the stop or cut risk %.")
    elif pct_of_capital > 25:
        print()
        print("  CAUTION: a large share of capital in one name. A tight stop")
        print("  makes this look safe, but a gap through the stop turns it")
        print("  into a concentrated loss. EGX gaps on Sunday opens after")
        print("  two days of global news — stops do not protect across gaps.")

    if args.adv:
        adv_share = value / args.adv * 100
        print()
        print(f"  Average daily traded value  {_egp(args.adv)}")
        print(f"  Position as % of ADV        {adv_share:.1f}%")
        if adv_share > 25:
            print("  -> TOO BIG for this stock's liquidity. Exiting would")
            print("     move the price against you. Size down.")
        elif adv_share > 10:
            print("  -> Exit would take roughly a day of normal volume.")
        else:
            print("  -> Liquidity looks adequate.")


def cost(args: argparse.Namespace) -> None:
    """Round-trip transaction cost including stamp duty."""
    duty_pct = STAMP_DUTY_INTRADAY_PCT if args.intraday else STAMP_DUTY_PCT

    commission = args.value * args.commission_pct / 100 + args.flat_fee
    duty = args.value * duty_pct / 100
    one_way = commission + duty
    round_trip = one_way * 2
    rt_pct = round_trip / args.value * 100

    label = "intraday" if args.intraday else "standard"
    print(f"Round-trip cost ({label})")
    print("=" * 46)
    print(f"  Trade value          {_egp(args.value)}")
    print()
    print(f"  Commission           {_egp(commission)}"
          f"  ({args.commission_pct}% + {_egp(args.flat_fee)})")
    print(f"  Stamp duty           {_egp(duty)}  ({duty_pct}%)")
    print(f"  One way              {_egp(one_way)}")
    print("-" * 46)
    print(f"  ROUND TRIP           {_egp(round_trip)}")
    print(f"  As % of trade        {rt_pct:.3f}%")
    print()
    print(f"  Break-even move needed: {rt_pct:.3f}%")

    if args.spread_pct:
        spread_cost = args.value * args.spread_pct / 100
        total = round_trip + spread_cost
        print()
        print(f"  Bid-ask spread ({args.spread_pct}%)  {_egp(spread_cost)}")
        print(f"  TRUE ROUND TRIP      {_egp(total)}"
              f"  ({total / args.value * 100:.3f}%)")
        print("  In illiquid names the spread exceeds every explicit fee.")

    if args.trades_per_year:
        annual = round_trip * args.trades_per_year
        print()
        print(f"  {args.trades_per_year} round trips/year: {_egp(annual)}"
              f" = {annual / args.value * 100:.2f}% of capital")
        print("  paid before a single decision is judged right or wrong.")


def compare(args: argparse.Namespace) -> None:
    """Equity expected return vs. a guaranteed bank certificate."""
    earnings_yield = 100 / args.pe
    real_growth = ((1 + args.growth / 100) / (1 + args.inflation / 100) - 1) * 100
    expected = args.div_yield + real_growth
    cert_real = ((1 + args.certificate / 100)
                 / (1 + args.inflation / 100) - 1) * 100

    print("Equity vs. bank certificate")
    print("=" * 46)
    print(f"  P/E                  {args.pe:.2f}")
    print(f"  Earnings yield       {earnings_yield:.2f}%  (1 / P/E)")
    print(f"  Dividend yield       {args.div_yield:.2f}%")
    print(f"  Earnings growth      {args.growth:.2f}% nominal")
    print(f"  Inflation            {args.inflation:.2f}%")
    print(f"  Real growth          {_pct(real_growth)}")
    print("-" * 46)
    print(f"  EQUITY (real, approx)     {_pct(expected)}")
    print("    = dividend yield + real earnings growth")
    print("      (excludes any multiple re-rating)")
    print()
    print(f"  Certificate nominal       {args.certificate:.2f}%")
    print(f"  CERTIFICATE (real)        {_pct(cert_real)}")
    print("-" * 46)

    gap = expected - cert_real
    print(f"  EDGE TO EQUITY            {_pct(gap)}")
    print()
    if gap <= 0:
        print("  The certificate wins on these assumptions — guaranteed,")
        print("  no analysis required, no volatility. The equity case needs")
        print("  faster growth or multiple expansion to justify the risk.")
    elif gap < 5:
        print("  A thin edge for a risky asset. Ask whether a few points")
        print("  compensate for volatility, liquidity risk, and the chance")
        print("  the growth assumption is simply wrong.")
    else:
        print("  A meaningful edge — but it rests entirely on the growth")
        print("  assumption holding. Stress-test it: what if growth is half?")

    half = args.growth / 2
    half_real = ((1 + half / 100) / (1 + args.inflation / 100) - 1) * 100
    print()
    print(f"  Stress test at {half:.1f}% growth: equity real ="
          f" {_pct(args.div_yield + half_real)}"
          f" vs cert {_pct(cert_real)}")
    print()
    print("  Note: the certificate carries zero USD protection. If goals")
    print("  are dollar-denominated, neither figure tells the whole story.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="EGX investing calculations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("real-return", help="inflation-adjusted return")
    p.add_argument("--nominal", type=float, required=True, help="nominal return %%")
    p.add_argument("--inflation", type=float, default=DEFAULT_INFLATION,
                   help=f"inflation %% (default {DEFAULT_INFLATION})")
    p.add_argument("--certificate", type=float, default=None,
                   help="optional: compare against a certificate rate %%")
    p.set_defaults(func=real_return)

    p = sub.add_parser("usd-return", help="return in USD terms")
    p.add_argument("--nominal", type=float, required=True, help="nominal EGP return %%")
    p.add_argument("--fx-start", type=float, required=True, help="EGP/USD at start")
    p.add_argument("--fx-end", type=float, required=True, help="EGP/USD at end")
    p.set_defaults(func=usd_return)

    p = sub.add_parser("position-size", help="risk-based position sizing")
    p.add_argument("--capital", type=float, required=True, help="total capital EGP")
    p.add_argument("--risk-pct", type=float, required=True, help="%% of capital at risk")
    p.add_argument("--entry", type=float, required=True, help="entry price")
    p.add_argument("--stop", type=float, required=True, help="stop-loss price")
    p.add_argument("--adv", type=float, default=None,
                   help="optional: average daily traded value EGP")
    p.set_defaults(func=position_size)

    p = sub.add_parser("cost", help="round-trip transaction cost")
    p.add_argument("--value", type=float, required=True, help="trade value EGP")
    p.add_argument("--commission-pct", type=float, default=0.1,
                   help="broker commission %% (default 0.1)")
    p.add_argument("--flat-fee", type=float, default=2.0,
                   help="flat fee per order EGP (default 2)")
    p.add_argument("--intraday", action="store_true",
                   help="same-session buy and sell (halved stamp duty)")
    p.add_argument("--spread-pct", type=float, default=None,
                   help="optional: estimated bid-ask spread %%")
    p.add_argument("--trades-per-year", type=int, default=None,
                   help="optional: annualize the cost drag")
    p.set_defaults(func=cost)

    p = sub.add_parser("compare", help="equity vs bank certificate")
    p.add_argument("--pe", type=float, required=True, help="price/earnings ratio")
    p.add_argument("--div-yield", type=float, required=True, help="dividend yield %%")
    p.add_argument("--growth", type=float, required=True,
                   help="expected nominal earnings growth %%")
    p.add_argument("--certificate", type=float, default=DEFAULT_CERTIFICATE,
                   help=f"certificate rate %% (default {DEFAULT_CERTIFICATE})")
    p.add_argument("--inflation", type=float, default=DEFAULT_INFLATION,
                   help=f"inflation %% (default {DEFAULT_INFLATION})")
    p.set_defaults(func=compare)

    return parser


def main() -> None:
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
