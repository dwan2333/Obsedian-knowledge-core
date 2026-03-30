# SOFR — Secured Overnight Financing Rate

## What Is SOFR?

SOFR stands for **Secured Overnight Financing Rate**. It is the benchmark interest rate for U.S. dollar-denominated loans, derivatives, and other financial products. It is published daily by the Federal Reserve Bank of New York.

SOFR measures the cost of borrowing cash overnight through **repurchase agreements (repos)**, where borrowers put up [U.S. Treasury bonds](<Treasury Bonds Guide.md>) as collateral. It replaced LIBOR, which was phased out after manipulation scandals.

---

## How Overnight Repo Transactions Work

1. **Bank A** needs cash overnight.
2. **Bank B** has extra cash and is willing to lend.
3. Bank A hands over [U.S. Treasury bonds](<Treasury Bonds Guide.md>) to Bank B as **collateral** — a security deposit.
4. If Bank A fails to repay the next day, Bank B keeps the bonds.
5. The small cost Bank A pays for this overnight loan is the **repo rate**.

SOFR is the **volume-weighted average** of all such overnight repo transactions across the market (over $1 trillion in daily volume).

### Why [Treasury Bonds](<Treasury Bonds Guide.md>)?

- Backed by the U.S. government — considered the safest financial asset in the world.
- Easy to value and easy to sell.
- Lenders feel comfortable accepting them as a guarantee.

---

## What Are SOFR Futures?

SOFR futures are derivatives contracts that allow market participants to **bet on what the average overnight borrowing rate will be over a future period**.

### Two Main Types

| Type | Settlement Basis |
|---|---|
| **1-Month SOFR Futures** | Arithmetic average of daily SOFR over a calendar month |
| **3-Month SOFR Futures** | Compounded daily SOFR over a calendar quarter |

### How Pricing Works

SOFR futures are quoted as:

> **Price = 100 − Expected Rate**

| Market Expects SOFR at | Futures Price |
|---|---|
| 4.00% | 96.00 |
| 4.25% | 95.75 |
| 4.50% | 95.50 |

- **Think rates will fall** → Buy the future (price rises, you profit).
- **Think rates will rise** → Sell the future (price drops, you profit).

### Why It Matters

In practice, SOFR futures are a direct bet on **what the Fed will do with interest rates**. This is why analysts say things like "SOFR futures are pricing in three rate cuts by December" — they read the implied rates from these contracts to gauge market expectations.

---

## What Drives SOFR?

### Big Moves — Fed Policy

The Federal Reserve meets roughly **8 times per year** and sets a target range for overnight rates (e.g., 4.25%–4.50%).

- **Rate cut** → More cash in the system → Overnight borrowing gets cheaper → SOFR drops.
- **Rate hike** → Less cash in the system → Overnight borrowing gets more expensive → SOFR rises.

These decisions drive the **major shifts** in SOFR.

### Small Daily Wiggles — Supply and Demand for Cash

Between Fed meetings, SOFR still fluctuates slightly day to day. This is because the rate reflects **how much cash is available versus how many borrowers need it** on any given night.

| Condition | Effect on Cash | Effect on SOFR |
|---|---|---|
| **Normal day, plenty of cash** | Lenders compete to lend → accept lower rates | SOFR ticks down slightly |
| **End of month/quarter** | Banks need cash for regulatory reporting | SOFR ticks up slightly |
| **[Treasury](<Treasury Bonds Guide.md>) auction settlement** | Buyers drain cash to pay for new bonds | SOFR ticks up slightly |
| **Tax payment deadlines** | Cash flows out of banking system to government | SOFR ticks up slightly |

**Analogy:** Think of SOFR as the price of apples. When there are too many sellers and few buyers, the price drops. When apples are scarce, the price goes up. The Fed decides how many apple trees exist (the general level), but daily weather and demand create small price fluctuations.

---

## Summary

- **SOFR** = the average cost of borrowing cash overnight, secured by [U.S. Treasury bonds](<Treasury Bonds Guide.md>).
- **Repos** = the mechanism — borrowers hand over Treasuries as collateral for short-term cash.
- **SOFR Futures** = bets on where the average overnight rate will be in a future month or quarter.
- **Fed policy** drives the big moves; **daily cash supply/demand** drives the small wiggles.
- SOFR is the foundation for pricing trillions of dollars in loans, bonds, and derivatives.

---

## Related Documents

- **[Treasury Bonds — A Beginner's Guide](<Treasury Bonds Guide.md>)** — The underlying collateral asset in every repo transaction that SOFR measures.
- **[Stablecoin Deep Dive](Stable%20Coin%20(Main).md)** — Fiat-backed stablecoins hold U.S. Treasuries as reserves; SOFR reflects the overnight cost of borrowing against those same Treasuries.
