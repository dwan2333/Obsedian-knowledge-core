# How Hedge Funds Use Leverage

*Part 5 of 7 · [Series overview](<Treasury Securities and the Interest Rate System (Main).md>)*

---

Money market funds lend their savers' cash overnight; hedge funds borrow it to hold leveraged Treasury positions for weeks or months.

---

## Money market funds

A money market fund is an investment product run by a company such as Fidelity, Vanguard, BlackRock, Charles Schwab, or JPMorgan. It is not a trading system.

- **Where the cash comes from:** savers, companies parking operating cash, and brokerage accounts that automatically "sweep" idle cash into them. United States funds hold around &#36;7 trillion or more.
- **What it buys:** only very short-term, very safe assets, mainly Treasury bills, repurchase agreements backed by Treasury securities, and the Federal Reserve's 3.75% reverse repurchase facility. Funds holding only government assets may lend only against government collateral, so they never make unsecured loans to banks.
- **What investors get:** a share price held at &#36;1, with interest close to overnight rates that builds daily and is usually credited monthly.
- **How it trades:** mostly electronically. The fund and a dealer agree on amount and rate; a custodian bank then moves cash one way and securities the other, and reverses it the next morning.

---

## How a leveraged purchase works

The hedge fund never needs to own the bonds first: like a home mortgage, the thing being bought becomes the collateral for the loan that pays for it.

|                              | Buying a house         | A leveraged Treasury purchase        |
| ---------------------------- | ---------------------- | ------------------------------------ |
| What is bought               | &#36;500,000 house     | &#36;100 million of Treasury notes   |
| Own money (the down payment) | &#36;100,000           | &#36;2 million (the haircut)         |
| Borrowed                     | &#36;400,000 mortgage  | &#36;98 million repurchase agreement |
| Collateral                   | The house being bought | The notes being bought               |

On settlement day everything happens at once, through systems that release cash only when securities move. The seller delivers &#36;100 million of notes straight into the lender's account as collateral, the lender pays &#36;98 million, the hedge fund adds &#36;2 million, and the seller receives &#36;100 million. The hedge fund now owns &#36;100 million of notes, owes &#36;98 million, and has spent &#36;2 million. In practice it simply asks its dealer to buy the notes and finance them in one step.

**Why not just sell the bonds for cash?** Selling would end the trade: the lender is repaid, the hedge fund gets its &#36;2 million back plus or minus any gain, and the position is gone. The goal is to control &#36;100 million of bonds with &#36;2 million, keeping the bonds' benefits while using borrowed cash. That combination is what leverage means.

---

## Rolling the loan every morning

The loan is overnight, but the trade is not: the loan is renewed each morning, the principal stays in place, and only the day's interest and any collateral adjustment actually move.

| Each morning                      | What happens                                                                       | What actually moves                                  |
| --------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------- |
| 1. Renewal agreed                 | Often automatic under an "open" agreement that continues until either side cancels | Nothing                                              |
| 2. Old loan ends, new loan starts | Yesterday's &#36;98 million is due and today's &#36;98 million is paid out         | The clearing house nets them to zero                 |
| 3. Interest paid                  | Yesterday's interest at 3.87%                                                      | About &#36;10,535                                    |
| 4. Collateral re-priced           | The bonds are valued at today's price                                              | A top-up if they lost value, a refund if they gained |

The bonds sit in accounts at a custodian bank, pledged in the lender's favor, while the clearing house keeps the record. The hedge fund still receives the bonds' interest and price changes, but cannot sell them without repaying. Hedge funds also borrow from dealers for a week or a month while the dealer handles the overnight rolling.

The loan lasts only while both sides agree. The hedge fund can repay and take its bonds back; lenders can refuse to renew or demand better terms. For the basis trade below, it ends naturally on the futures delivery day.

---

## Strategy 1: earning the gap with leverage ("carry")

The hedge fund buys something that earns more than its borrowing cost, using mostly borrowed money.

| Using October 2026 rates | Amount |
|---|---|
| Own money put up | &#36;2 million |
| Borrowed at 3.87% | &#36;98 million |
| 10-year Treasury notes bought, yielding about 5.25% | &#36;100 million |
| Yearly interest earned | &#36;5.25 million |
| Yearly interest paid | &#36;3.79 million |
| **Net profit, about 73% on its own &#36;2 million** | **&#36;1.46 million** |

Leverage cuts both ways. When the 10-year yield rose from about 4.95% to 5.25% in late September 2026, these notes lost roughly 2.4%, a &#36;2.4 million loss that would wipe out the fund's entire &#36;2 million.

**Paying daily, collecting twice a year:** the hedge fund pays borrowing interest every day but collects coupons only every six months. Over one six-month period, with notes paying a 5.25% coupon bought at face value:

|  | When | Amount |
|---|---|---|
| Interest paid on &#36;98 million at 3.87% | Every day, about &#36;10,535 | About &#36;1.92 million |
| Coupon on &#36;100 million at 5.25% | Once, at the end | About &#36;2.63 million |
| **Net for six months** |  | **About +&#36;0.71 million** |

It is behind for most of the period and catches up when the coupon arrives, like a landlord who pays the mortgage daily but collects rent twice a year. So hedge funds keep a cash cushion beyond the 2% haircut to cover months of interest and any margin calls, which is one reason real leverage is usually below the 50 to 1 the haircut alone allows.

---

## Strategy 2: the basis trade

The hedge fund buys a Treasury security and, at the same time, sells a futures contract on it. A futures contract is a promise to deliver the bond on a future date at a price fixed today, so the hedge fund has already locked in its selling price. It is not betting on momentum; the hedge is built to cancel price moves.

**Where the profit comes from** (simplified, per &#36;100 of face value, over three months):

| Step | Amount |
|---|---|
| Today: buy the bond with borrowed cash | −&#36;100.00 |
| Over 3 months: interest the bond earns (4% yearly coupon) | +&#36;1.00 |
| Over 3 months: interest paid to the money market fund (3.87%) | −&#36;0.97 |
| In 3 months: deliver the bond at the locked futures price | +&#36;100.03 |
| **Profit** | **+&#36;0.06** |

Given the bond's interest and the borrowing cost, a fair futures price would be about &#36;99.97. Futures often trade slightly above fair value, here &#36;100.03, because many big investors prefer holding futures. That small excess is the gap.

**Both positions together cancel price moves.** Profit is measured against the &#36;100.00 the hedge fund paid, not against the bond's later market price:

| Final bond price | The bond (bought at &#36;100.00) | Short futures (locked at &#36;100.03) | Together |
|---|---|---|---|
| Falls to &#36;98 | −&#36;2.00 | +&#36;2.03 | +&#36;0.03 |
| Stays at &#36;100 | &#36;0.00 | +&#36;0.03 | +&#36;0.03 |
| Rises to &#36;102 | +&#36;2.00 | −&#36;1.97 | +&#36;0.03 |

Add the &#36;1.00 of bond interest and subtract the &#36;0.97 of borrowing, and the total is +&#36;0.06 in every case. Selling futures alone would be a bet: +&#36;2.03 if the price fell to &#36;98, −&#36;1.97 if it rose to &#36;102. The basis trader gives up the big win to avoid the big loss, like a farmer who agrees today to sell next month's wheat at a fixed price: if wheat prices crash, the farmer does not profit, but does not lose on the wheat already in the barn.

**Leverage makes it worthwhile:** on &#36;100 million of bonds, &#36;0.06 per &#36;100 is &#36;60,000 in three months. Against &#36;2 million of its own money, that is 3% in three months, about 12% a year.

**Coupons are paid twice a year but earned daily.** When the hedge fund delivers the bond, the buyer pays the locked price plus all interest accrued while it held the bond, so it is paid for every day of ownership. Meanwhile it pays borrowing interest daily, covering that timing gap from its cash cushion.

**Futures gains and losses settle in cash every day.** If bond prices rise, the hedge fund owes cash on its futures immediately while its bond gain is only on paper. A higher bond price also means lenders will lend more against the same bonds, which usually covers the payment.

---

## Is the basis trade risk-free?

No. It is low-risk only while three things hold: borrowing costs stay where expected, the hedge fund can hold until the delivery date, and it can cover every daily cash call along the way.

**Risk 1: borrowing costs rise.** Borrowing costs do not rise because the bond loses value; they rise when overnight interest rates rise, for example after a Federal Reserve increase. The futures payoff depends only on the bond's price, so it cannot offset a higher interest bill. Using the example above, with overnight rates rising 0.30 points to 4.17% right after the trade starts:

| Scenario | Bond price | Borrowing rate | Borrowing cost | Profit |
|---|---|---|---|---|
| Plan | Stays &#36;100 | 3.87% | &#36;0.97 | +&#36;0.06 |
| A | Falls to &#36;98 | 3.87% | &#36;0.97 | +&#36;0.06 |
| B | Stays &#36;100 | 4.17% | &#36;1.04 | About −&#36;0.01 |
| C | Falls to &#36;98 | 4.17% | &#36;1.04 | About −&#36;0.01 |

The price drop changes nothing; only the borrowing cost matters. Because the fund borrows overnight and rolls daily, it pays each night's rate, and holding to the end cannot undo that cost. Borrowing for a fixed term until delivery removes the risk but costs more from the start.

**Risk 2: the gap moves before delivery.** The futures and bond prices come together only on the delivery date; before then the gap moves daily, and the position is valued at today's prices. At 50 to 1 leverage (&#36;100 million position, &#36;2 million of own money):

| Gap moves against them by | Paper loss | Share of the &#36;2 million |
|---|---|---|
| &#36;0.10 per &#36;100 | &#36;100,000 | 5% |
| &#36;0.50 per &#36;100 | &#36;500,000 | 25% |
| &#36;1.00 per &#36;100 | &#36;1,000,000 | 50% |

Held to delivery, this paper loss reverses; forced out early, it becomes real.

**Risk 3: daily cash calls.** Futures losses are paid in cash every day while bond gains stay on paper. Lenders lend only 98% of the collateral's value, so if &#36;100 million of bonds drop 1% to &#36;99 million, the most they will lend falls to &#36;97.02 million against &#36;98 million owed, and the hedge fund must hand over about &#36;0.98 million that day. In turbulent markets, exchanges also demand larger deposits and lenders demand bigger haircuts.

**Risk 4: everyone is in the same trade.** Because many large funds run it, they tend to exit together, pushing prices against each other and triggering more margin calls. In March 2020, as margins and borrowing rates rose, [basis traders sold roughly &#36;100 billion of Treasury securities](https://www.sciencedirect.com/science/article/abs/pii/S0304393225000947).

**What holding to the end fixes, and what it does not:**

| Problem | If they hold until delivery |
|---|---|
| Bond price swings | Offset by the futures; no final effect |
| Margin calls and paper losses on the gap | Reverse as the prices come together |
| Higher borrowing costs | A real expense that does not reverse |

**Staying in is not fully their choice:**

| Who can force an early exit | How |
|---|---|
| Lenders | Refuse to renew, or demand bigger haircuts |
| Futures exchanges | Raise required deposits |
| The fund's investors | Withdraw their money |
| The fund's own risk managers | Cut positions once losses pass a set limit |

**How funds reduce these risks:** borrowing for a fixed term until delivery (no borrowing-cost risk, smaller profit), using less leverage (easier to survive, lower return), and borrowing from many lenders (less chance of losing all funding at once). One smaller risk: futures can be settled with any of several similar bonds, so the bond a fund holds may track the future less closely than planned.

**Why the gap exists at all:** if the trade were truly risk-free, competition would have erased the gap. It persists as payment for bearing these funding risks, and for supplying large asset managers who prefer holding futures. Traders compare it to picking up coins in front of a steamroller: small, steady gains, with the risk of a sudden large loss.

---

## How big it is, and who does it

Hedge funds' borrowing in the repurchase agreement market reached [&#36;3.0 trillion by September 2025](https://www.federalreserve.gov/econres/notes/feds-notes/decomposing-hedge-funds-u-s-treasury-exposures-20260622.html), and their cash Treasury holdings were [about &#36;2 trillion at the end of 2025](https://www.cnbc.com/2026/09/30/us-treasury-market-is-relying-more-on-hedge-funds.html), a record 7% of marketable Treasury debt. Morgan Stanley estimates the basis trade at about &#36;1.2 trillion, down roughly 20% in 2026; estimates range [from &#36;350 billion to &#36;1.5 trillion](https://www.financialresearch.gov/the-ofr-blog/2026/08/19/hedge-funds-cash-treasury-holdings/) because hedge funds do not report it separately. Basis traders account for [more than 60% of hedge funds' Treasury positions and 70% of their repurchase agreement borrowing](https://www.sciencedirect.com/science/article/abs/pii/S0304393225000947).

There is no official profit figure. A rough illustration, assuming a yearly gap of 0.2% to 0.5% and leverage of about 15 to 1:

|  | Low | High |
|---|---|---|
| Yearly gap | 0.2% | 0.5% |
| On &#36;1.2 trillion | About &#36;2.4 billion | About &#36;6 billion |
| Return on the funds' capital | About 3% | About 7.5% |

Interest on their cash cushion adds a little more. The trade is concentrated among very large multi-strategy and relative-value funds; most smaller and stock-focused hedge funds do not run it, because it needs huge scale, reliable funding from several dealers, systems for daily margin calls, and deep cash reserves. Regulators watch it closely, and [the 2027 clearing requirement](<6 - How Middlemen Keep Borrowing Cheap.md>) is partly a response.

---

## Related Documents

- **Previous:** [Part 4 — Banks That Lend to Banks](<4 - Banks That Lend to Banks.md>)
- **Next:** [Part 6 — How Middlemen Keep Borrowing Cheap](<6 - How Middlemen Keep Borrowing Cheap.md>)
- **Series hub:** [Treasury Securities and the Interest Rate System](<Treasury Securities and the Interest Rate System (Main).md>) — The big picture, the reading order, the rules to remember, and all sources.
