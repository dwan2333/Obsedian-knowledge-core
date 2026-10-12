# How Middlemen Keep Borrowing Cheap

*Part 6 of 7 · [Series overview](<Treasury Securities and the Interest Rate System (Main).md>)*

---

The dealer finds each deal and earns a small gap between two separate loans; the clearing house guarantees both loans and lets them cancel on paper, which is what keeps that gap tiny.

---

## What a dealer does

Dealers are the trading arms of big banks. About two dozen are "primary dealers," which trade directly with the Federal Reserve and must bid at every Treasury auction. A hedge fund borrows by asking a dealer's repurchase agreement desk, usually electronically: "Here is &#36;100 million of Treasury securities; lend me &#36;98 million tonight." That is a repurchase agreement, not an ordinary bank loan.

**Two separate deals, not one.** Like an airport currency exchange booth, the dealer borrows from one side and lends to the other; the money fund and the hedge fund never deal with each other.

| Deal | Who agrees | Rate (illustrative) |
|---|---|---|
| Money funds lend to the dealer | Money fund and dealer | Dealer pays 3.88% |
| Dealer lends to hedge funds | Dealer and hedge fund | Dealer charges 3.91% |

**How rates are set:** no law caps the gap; competition does, inside the Federal Reserve's band. Money funds will not accept less than 3.75%, since they can lend to the Federal Reserve instead, and big dealers will not pay much more than 4.00%, since they can borrow from it instead. Money funds shop their cash among dealers and hedge funds collect several quotes. Each rate also depends on the client's strength, the collateral, the length of the loan, and the calendar: gaps widen at each quarter's end, when banks shrink their balance sheets for regulatory reports.

---

## What the clearing house does

The Fixed Income Clearing Corporation never provides money and never finds deals; it steps in after a deal is agreed. Stock trades on Webull work the same way through their own clearing house.

| Job | What happens |
|---|---|
| Steps into every trade | Replaces each deal with two: it borrows from the lender and lends to the borrower |
| Cancels offsetting trades | Adds up each member's trades and keeps only the net amount |
| Collects safety deposits | Borrowers post extra collateral; positions are re-priced daily, with top-ups when values fall |
| Handles defaults | Uses the failed member's deposits first, then a shared fund all members pay into, then its own capital |
| Settles the exchange | Cash and securities change hands at the same instant |

It always owes exactly what it is owed, and it earns small per-trade fees rather than a spread. It is a private company owned by the Depository Trust and Clearing Corporation, which is in turn owned by the banks and brokers that use it. It is regulated by the Securities and Exchange Commission and was designated systemically important in 2012, but its obligations are not government-guaranteed; its safety comes from deposits, the shared fund, and its own capital.

---

## Sponsored clearing: why the middle gets cheaper

Hedge funds and money funds cannot join the clearing house directly, so a dealer sponsors them in, like a co-signer. Example: the dealer borrows &#36;500 million from money funds at 3.88%, lends &#36;480 million to hedge funds at 3.91%, and keeps &#36;20 million to buy its own Treasury bills.

|  | Without the clearing house | With the clearing house |
|---|---|---|
| Dealer owes | &#36;500 million to various money funds | &#36;500 million to the clearing house |
| Dealer is owed | &#36;480 million by various hedge funds | &#36;480 million by the clearing house |
| Can they cancel? | No, different parties | Yes, the same party |
| **Dealer's balance sheet** | **&#36;500 million** | **&#36;20 million** |

It works like IOUs: if you owe Alex &#36;500 and Ben owes you &#36;480, and both IOUs pass to Clara, you simply owe Clara &#36;20. The lending still happens; only the dealer's paperwork shrinks. The &#36;20 million it owes is matched by the &#36;20 million of Treasury bills it bought.

**Why the balance sheet is &#36;500 million, not &#36;20 million:** a balance sheet lists everything the dealer owns and everything it owes, not the cash in its pocket. Lending cash out turns it into a loan the hedge funds owe, which still counts as something the dealer owns.

| What the dealer owns | Amount | What the dealer owes | Amount |
|---|---|---|---|
| Treasury bills it bought | &#36;20 million | Owed to money funds | &#36;500 million |
| Loans owed by hedge funds | &#36;480 million |  |  |
| **Total** | **&#36;500 million** | **Total** | **&#36;500 million** |

**Why size matters: capital.** Without clearing, the dealer owes the money funds in full whatever happens. If a hedge fund defaults, the dealer keeps and sells its collateral, so the real risk is the shortfall: on a &#36;480 million loan, collateral that sells for &#36;470 million costs the dealer &#36;10 million. Capital is what absorbs losses like that.

Capital is not cash locked in a vault, and it is not customers' deposits, which are money the bank owes. It is the shareholders' own money, from buying the bank's stock or from profits the bank kept, and it keeps working inside the bank. For the biggest banks, a leverage rule requires roughly 5% of the balance sheet to be funded this way, however safe the assets are; the exact figure has been under revision. Shareholders expect a competitive return on that money, 10% a year in this illustration, so every business inside the bank must earn enough on the capital it uses.

|  | Without clearing | With clearing |
|---|---|---|
| Capital required | &#36;25 million | &#36;1 million |
| Yearly return shareholders expect | &#36;2.5 million | &#36;0.1 million |
| Gap needed on &#36;480 million to earn it | About 0.52% | About 0.02% |

No hedge fund would pay a half-point gap; with clearing, 0.03% covers the capital and still leaves a profit.

Put the other way: the 0.03% middleman gap on &#36;480 million earns about &#36;144,000 a year. That is only about 0.6% on &#36;25 million of shareholders' money, but about 14.4% on &#36;1 million. Clearing does not change the lending at all; it shrinks the capital the lending uses. As sponsor, the dealer still guarantees its clients to the clearing house, but the clearing house's safety deposits and shared fund make losses far less likely to reach it.

**Who pays the interest:** hedge funds pay their 3.91% and money funds receive their 3.88%, both through the clearing house, which keeps nothing and settles only each member's net amount. For the dealer, per night:

| Per night | Amount |
|---|---|
| Received from hedge funds (&#36;480 million at 3.91%) | +&#36;52,133 |
| Earned on its own Treasury bills (&#36;20 million at about 4.09%) | +&#36;2,272 |
| Paid to money funds (&#36;500 million at 3.88%) | −&#36;53,889 |
| **Total profit** | **+&#36;516** |

Of that, &#36;400 is the middleman gap on the &#36;480 million passed through, and &#36;116 is the dealer's own investment.

**Whose bonds are whose:** the hedge funds' bonds stay theirs. The dealer only holds them as collateral and passes the same bonds on to the money funds as collateral for its own borrowing, which is called re-pledging; any coupon paid meanwhile goes back to the hedge fund. The &#36;20 million of Treasury bills belong to the dealer, bought with the extra cash it borrowed.

**How the dealer's own &#36;20 million works:** it is the dealer's own overnight loan, rolled every morning just like a hedge fund's. Bills pay no interest along the way; their 4.09% builds up in their price, while the dealer pays its 3.88% borrowing interest in cash each night. When the bills mature, their face value repays the &#36;20 million. Over 30 days, that side earns about &#36;68,160 of built-up value against about &#36;64,680 of interest paid, roughly &#36;3,480, on top of about &#36;12,000 from the &#36;400-a-night middleman gap.

**Can hedge funds skip the dealer?** Only partly. Most money funds avoid lending to hedge funds directly, so sponsored clearing is the halfway route, and hedge funds now dominate sponsored borrowing, often for the basis trade. The Securities and Exchange Commission requires central clearing of most Treasury cash trades by December 31, 2026, and of repurchase agreements by June 30, 2027, pushing more borrowing this way. Since the basis trade earns only about 0.24% a year, saving even 0.05 points of borrowing cost is about a fifth of its profit.

---

## Related Documents

- **Previous:** [Part 5 — How Hedge Funds Use Leverage](<5 - How Hedge Funds Use Leverage.md>)
- **Next:** [Part 7 — When the System Breaks](<7 - When the System Breaks.md>)
- **Series hub:** [Treasury Securities and the Interest Rate System](<Treasury Securities and the Interest Rate System (Main).md>) — The big picture, the reading order, the rules to remember, and all sources.
