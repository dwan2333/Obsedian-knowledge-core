# Algorithmic Stablecoins: The TerraUSD / LUNA Collapse

*Companion document to [Stablecoin Deep Dive: Mechanisms, Dollar Impact & AI Agent Markets](Stable%20Coin%20(Main).md)*

---

## Overview

Algorithmic stablecoins attempt to maintain a $1 peg with **no reserves whatsoever** — no dollars in a bank, no crypto locked in a smart contract. They rely entirely on market incentives and token-supply mechanics to hold their value. TerraUSD (UST) was the largest and most prominent example before its catastrophic collapse in May 2022.

---

## How TerraUSD / LUNA Worked

### The Swap Mechanism

UST maintained its peg through a **mint-and-burn swap** with its sister token, LUNA:

- **Redeem 1 UST → receive $1 worth of LUNA** (at current market price)
- **Burn $1 worth of LUNA → mint 1 UST**

There was no vault, no reserve, no collateral. The entire system rested on the convertibility between UST and LUNA, and on arbitrageurs exploiting price differences.

### The Arbitrage Loop

- **UST drops below $1** (say to $0.98): Arbitrageurs buy cheap UST on the open market, redeem it for $1 worth of LUNA, sell the LUNA, pocket the $0.02 difference. Each redemption *burns* UST, reducing supply, pushing the price back toward $1.
- **UST rises above $1** (say to $1.02): Arbitrageurs burn $1 worth of LUNA to mint 1 UST, sell the UST at $1.02, pocket the $0.02. Each mint *increases* UST supply, pushing the price back down toward $1.

In theory, profit-seeking traders would always correct any deviation from the peg. In practice, this only works when people believe LUNA has lasting value.

### The Anchor Protocol — The Growth Engine

- Anchor Protocol offered **~20% annual yields** on UST deposits — vastly higher than anything in traditional finance or other DeFi protocols.
- This attracted billions of dollars into UST. At its peak, roughly 75% of all UST in circulation was deposited in Anchor.
- The yield was subsidized by the Luna Foundation Guard and was not sustainable long-term. It functioned as a growth marketing expense, pulling in capital to build network effects before yields would eventually normalize.
- **The problem**: When the yield engine is the primary reason people hold the stablecoin, any threat to that yield triggers mass exits.

---

## The Death Spiral — Step by Step

### Phase 1 — The Initial Break (May 7–8, 2022)

- Large holders began dumping UST, likely triggered by a combination of Anchor yield concerns and coordinated selling.
- UST slipped below $1 and the arbitrage mechanism activated — UST was redeemed for LUNA and that LUNA was immediately sold for real money (USD, USDC, etc.).

### Phase 2 — LUNA Flooding (May 9–10, 2022)

- As LUNA's price dropped from the sell pressure, **more LUNA had to be minted per UST redemption** to deliver "$1 worth of LUNA."
- Example: At LUNA = $50, redeeming 1 UST mints 0.02 LUNA. At LUNA = $0.50, redeeming 1 UST mints 2 LUNA. At LUNA = $0.001, redeeming 1 UST mints 1,000 LUNA.
- Each wave of new LUNA flooded the market, crashing the price further, which required even more LUNA per redemption — a textbook **hyperinflationary death spiral**.

### Phase 3 — Hyperinflation & Collapse (May 11–13, 2022)

- LUNA supply exploded from roughly **1 billion tokens to over 6 trillion** — a 6,000x dilution in days.
- Once LUNA became effectively worthless, the "redeem UST for $1 worth of LUNA" mechanism meant redeeming UST for… essentially nothing.
- UST's backing evaporated. It fell to $0.10, then pennies.
- **~$40–50 billion in combined UST and LUNA value was destroyed.**

### Phase 4 — Aftermath

- Founder **Do Kwon** was arrested and sentenced to **15 years for fraud**.
- Algorithmic stablecoins are now **banned or heavily restricted** under the EU's MiCA regulation and the U.S. GENIUS Act. Both frameworks explicitly exclude supply-based algorithmic models from licensed stablecoin issuance.
- The collapse triggered broader contagion: crypto lender Celsius, hedge fund Three Arrows Capital, and exchange FTX all faced cascading failures in the months that followed, partly traced back to Terra exposure.

---

## Why the Death Spiral Was Structural, Not Accidental

```
Normal conditions:
  UST below $1 → burn UST, mint LUNA → UST supply ↓ → price recovers ✓

Crisis conditions:
  UST below $1 → burn UST, mint LUNA → sell LUNA → LUNA price ↓
       ↓
  LUNA price ↓ → more LUNA minted per redemption → more LUNA sold
       ↓
  LUNA price ↓↓ → even more LUNA minted → LUNA floods market
       ↓
  LUNA becomes worthless → UST redemption = worthless → UST collapses
       ↓
  ~$40-50 billion destroyed
```

The mechanism that was supposed to *restore* the peg became the mechanism that *destroyed* both tokens. The arbitrage loop only works when LUNA retains value. Once confidence breaks, the correction mechanism reverses into an acceleration mechanism.

---

## The Core Lesson — Three Trust Models Compared

| Stablecoin | What You Trust | What Backs It | Failure Mode |
|---|---|---|---|
| **USDC** | A company (Circle) holding real dollars | Cash, [U.S. Treasuries](<Treasury Bonds (main).md>), repos | Circle goes bankrupt or commits fraud |
| **DAI** | Code (smart contracts) holding real crypto | Over-collateralized ETH + other assets | Catastrophic multi-asset crash overwhelming all four defense stages |
| **UST** | Confidence alone — that people will keep valuing LUNA | Nothing tangible — only the swap mechanism | Confidence breaks → death spiral → total collapse |

**UST trusted that confidence alone could substitute for actual backing — and it couldn't.**

The critical distinction: USDC and DAI have something *outside the system* backing them (real dollars, real crypto). UST was entirely **self-referential** — its value depended on the value of LUNA, whose value depended on the demand for UST. It was circular logic encoded in software.

---

## Post-Collapse Evolution (2023–2026)

- **Pure algorithmic models are essentially dead.** No major new project has attempted an uncollateralized algorithmic stablecoin since Terra.
- **Hybrid models emerged**: Projects like FRAX combine partial real-asset collateral with algorithmic supply adjustments — hedging against full death-spiral risk while retaining some decentralization benefits.
- **AI-augmented stability**: A new generation of hybrid stablecoins is incorporating AI-driven stabilization models that use data-driven decision-making to react faster to market stress and switch between stabilization strategies dynamically.
- **Regulatory exclusion is now law**: The U.S. GENIUS Act (2025) and EU MiCA explicitly exclude algorithmic stablecoins from their licensed frameworks, treating them as potential systemic threats.

---

## Related Documents

- **[Stablecoin Deep Dive: Mechanisms, Dollar Impact & AI Agent Markets](Stable%20Coin%20(Main).md)** — Covers all stablecoin types, the dollar dominance feedback loop, ECB sovereignty concerns, and the emerging AI agent payment infrastructure.
- **[Crypto-Collateralized Stablecoins: MakerDAO's DAI](crypto_collateralized_stablecoins_dai.md)** — Deep dive into the on-chain collateral model, the three-actor liquidation system, and the four-stage defense cascade.
- **[Synthetic / Hedged Stablecoins: Ethena's USDe](synthetic_stablecoins_ethena_usde.md)** — Shares Terra's 1:1 capital efficiency but avoids the death spiral by holding real collateral + a derivatives hedge.
- **[Hybrid Stablecoins: FRAX & the Fractional-Algorithmic Experiment](hybrid_stablecoins_frax.md)** — Terra's collapse directly caused FRAX to abandon its fractional-algorithmic model and move to 100% collateralization.
- **[Stablecoin AI Agent Payment Infrastructure](ai_agent_payment_infrastructure.md)** — The four-layer agentic payment stack. Terra's collapse is why reserve-backed stablecoins (USDC, USDT) — not algorithmic ones — became the settlement asset of choice.
