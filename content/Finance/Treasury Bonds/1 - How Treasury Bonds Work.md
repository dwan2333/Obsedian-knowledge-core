# How Treasury Bonds Work

*Part 1 of 7 · [Series overview](<Treasury Securities and the Interest Rate System (Main).md>)*

---

## Treasury bills, notes, and bonds

All three are loans to the United States government; they differ only in how long the loan lasts and how you are paid.

|  | Treasury bills | Treasury notes | Treasury bonds |
|---|---|---|---|
| Length | 4 weeks to 1 year | 2, 3, 5, 7, 10 years | 20 and 30 years |
| How you are paid | Buy below face value, receive full face value at the end | Interest every 6 months, plus face value at the end | Same as notes |
| Yield in early October 2026 | 3-month: about 4.09% | 2-year: 4.80%, 10-year: about 5.25% | 30-year: about 5.67% |
| Price swings when rates move | Very small | Moderate | Large |

---

## The four terms that matter

The payments on a bond are fixed when it is issued; the price you pay today is the only thing that decides your return.

| Term | What it means | Changes over time? |
|---|---|---|
| Face value | The amount the government pays back at maturity, and the base the interest is calculated on | Never |
| Coupon rate | The fixed yearly interest rate on face value, set at issue (named after paper coupons owners once clipped to collect interest) | Never |
| Price | What you pay today, quoted per 100 of face value | Constantly, with market rates |
| Yield to maturity | Your true yearly return if you buy today and hold until the end, counting coupons, the move to face value, and compounding | Constantly, opposite to price |

Yield to maturity is the one interest rate r that makes all future payments worth exactly today's price, where C is each coupon payment, F is face value, and n is the number of payments left:

$$
P = \sum_{t=1}^{n} \frac{C}{(1+r)^t} + \frac{F}{(1+r)^n}
$$

**A tiny check:** a 2-year bond with a 4% yearly coupon, priced at r = 6%, is worth 4 ÷ 1.06 + 104 ÷ 1.06² ≈ 3.77 + 92.56 = &#36;96.33. There is no formula that solves for r directly, so platforms try rates until the price matches: for the 2055 bond in the worked example, 5% gives about &#36;94.34, 6% about &#36;81.33, and 5.619% about &#36;85.96.

**The easiest way to picture it:** imagine depositing the bond's price in a savings account paying the yield to maturity, then withdrawing exactly the bond's payments on the same dates. The account ends at exactly zero. When a bond is bought below face value, each period's interest slightly exceeds the coupon withdrawn, and that small leftover slowly builds the balance back up to face value. That is how the discount gets earned, gradually rather than all at the end.

**Higher yield is good before you buy, bad after.** The yield on the day you buy is what you lock in. If the market yield rises afterward, your bond's price falls; if you hold to maturity, you still earn what you locked in.

---

## Worked example: the 4.625% bond maturing February 15, 2055

For about &#36;86.62 today, this bond pays back about &#36;231.81 by 2055, a locked-in yield to maturity of about 5.62% per year.

| Per &#36;100 of face value | Amount |
|---|---|
| Price (quoted 85.977) | &#36;85.98 |
| Accrued interest owed to the seller (51 of 184 days into the coupon period) | &#36;0.64 |
| **Total paid today** | **&#36;86.62** |
| 57 coupon payments of &#36;2.3125 each, every February 15 and August 15 | &#36;131.81 |
| Face value repaid in 2055 | &#36;100.00 |
| **Total received** | **&#36;231.81** |
| **Total profit** | **&#36;145.19** |

**Why it costs less than &#36;100:** its 4.625% coupon is below the market's 5.62%, so the price drops until the bond's return matches the market. A &#36;100 price would lock in only about 4.6%; a &#36;110 price, about 4.0%.

**Where the &#36;0.64 comes from:** the coupon period from August 15 to February 15 has 184 days (16 + 30 + 31 + 30 + 31 + 31 + 15). A trade settling Monday, October 5 is 51 days in (16 + 30 + 5), so the seller has earned 2.3125 × 51 ÷ 184 ≈ &#36;0.64 of the next coupon. You collect the full &#36;2.3125 in February, keeping your share of about &#36;1.67.

**The same bond, measured four ways:**

| Measure | Result | What it counts |
|---|---|---|
| Coupon rate | 4.625% | Interest on face value only |
| Current yield | 5.38% | Yearly coupon divided by the price you pay |
| Shortcut yield to maturity | 5.51% | Coupons plus the gain to &#36;100, without compounding |
| Exact yield to maturity | 5.62% | Everything, with compounding |

Discounting all 57 payments at 2.8095% per half-year gives a price of about &#36;85.96, then about &#36;85.98 after adjusting for the 51 days already elapsed: an exact match with the screen.

---

## Buying and selling

Treasury securities do not trade on a stock exchange; they trade over the counter between dealers, and your brokerage connects you to that market.

| Way to buy | How it works | Good to know |
|---|---|---|
| At auction (new issue) | Order through a brokerage or TreasuryDirect; individuals submit a non-competitive bid and accept the auction's rate | Your order is guaranteed to be filled |
| Secondary market (existing securities) | Search by maturity or identification number; buy at the ask price, sell at the bid price | Most stock-like experience; you can sell any time before maturity |
| Treasury exchange-traded funds | Trade all day under normal tickers, exactly like stocks | They never mature, so you cannot hold to maturity to guarantee your principal |

**Reading a quote:** prices are per 100 of face value, so 98.50 means &#36;985 per &#36;1,000. Professional screens use thirty-seconds: 99-16 means 99.50.

**Accrued interest:** buying between coupon dates means paying the seller the interest earned so far. The quoted price without it is the clean price; the total you pay is the dirty price.

**Coupon dates and older securities:** coupons are paid every six months on the day and month the security matures, so the 2055 bond pays every February 15 and August 15. Past coupons were already paid to earlier owners, so buying an older note never means paying for past years' interest, only the accrued interest since the last coupon, at most six months' worth. A 5-year note with one year left is priced like any one-year security maturing on that date, so its yield matches today's one-year rate.

**Settlement:** trades settle one business day later. Many brokerages charge no commission; the dealer's spread is built into the price.

---

## Related Documents

- **Previous:** [The big picture](<Treasury Securities and the Interest Rate System (Main).md#The big picture>) (in the series hub)
- **Next:** [Part 2 — How the Fed Moves Your Rates](<2 - How the Fed Moves Your Rates.md>)
- **Series hub:** [Treasury Securities and the Interest Rate System](<Treasury Securities and the Interest Rate System (Main).md>) — The big picture, the reading order, the rules to remember, and all sources.
- **[Treasury Bonds — A Beginner's Guide](<Treasury Bonds (main).md>)** — The introductory note in this folder: the three types, coupons versus discounts, and why prices and rates move in opposite directions.
