# Crypto-Collateralized Stablecoins: MakerDAO's DAI — A Deep Dive

*Companion document to [Stablecoin Deep Dive: Mechanisms, Dollar Impact & AI Agent Markets](stablecoin_deep_dive.md)*

---

## Overview

DAI takes a fundamentally different approach from fiat-backed stablecoins like USDC or USDT. There's no company, no bank account, no CEO. Everything runs through smart contracts on Ethereum — transparent code that nobody can alter.

---

## How Minting Works

- You lock cryptocurrency (typically ETH) into a MakerDAO smart contract as collateral.
- The system requires **over-collateralization** — roughly **$150 in ETH to mint $100 of DAI**. That extra $50 is a safety buffer against crypto price volatility.
- You can then use your DAI however you want while your ETH stays locked.

## Getting Your ETH Back

- You return 100 DAI (plus a small stability fee) to the smart contract. It burns the DAI and releases your ETH.
- If ETH appreciated while locked, you benefit from that appreciation — but you don't get extra DAI. The profit is in your ETH being worth more, not in the stablecoin itself.
- **DAI is a borrowing tool, not an investment.**

---

## Key Differences from USDC / USDT

| Dimension | USDC / USDT | DAI |
|---|---|---|
| **Trust model** | Trust the issuing company (Circle, Tether) | Trust that the smart contract code works correctly |
| **Censorship resistance** | Issuers can freeze wallets (Circle has done so under government order) | Nobody can freeze your tokens — fully decentralized |
| **Capital efficiency** | 1:1 backing — deposit $1, get $1 | Capital inefficient — need ~$1.50 locked to get $1 out |
| **Transparency** | Periodic attestation reports | Real-time, on-chain, auditable by anyone at any time |
| **Core tradeoff** | Simplicity and efficiency | Decentralization and transparency |

---

## The Liquidation System — Three Actors

### 1. The Smart Contract

Just code on the blockchain. It monitors every collateralized position and flags any that fall below the safety threshold. It doesn't sell anything itself — it simply marks positions as available for liquidation.

### 2. The Keepers

Independent profit-seeking bots run by people and firms worldwide. Anyone can run one. They constantly watch for flagged positions and race to participate in auctions, bidding DAI to buy discounted ETH. Their competition pushes auction prices toward fair value.

### 3. The Auction Process

When a keeper pays DAI to buy liquidated ETH, that DAI returns to the smart contract and gets burned, closing the borrower's debt. The borrower gets back whatever leftover ETH remains after the debt plus a roughly **13% liquidation penalty**. Often very little is left.

**What if you already spent your DAI?** It doesn't matter. The system doesn't need *your* specific tokens back. DAI is fungible. The keeper bots supply their own DAI to buy your collateral. You simply lose your locked ETH and keep whatever you did with the DAI you minted. Effectively you sold $150 of ETH for $100 — a bad deal, but the system stays whole.

---

## MakerDAO's Backup Plan — Four Stages of Defense

### Stage 1 — Over-Collateralization

The $150-to-$100 buffer absorbs normal price swings. Experienced users maintain even higher ratios for extra safety. This is the first and most common line of defense — it handles everyday volatility without any intervention.

### Stage 2 — Keeper Auctions

When positions breach the threshold, keeper bots buy the discounted collateral with DAI, which gets burned. This works well under normal conditions and moderate stress. The competitive auction mechanism ensures fair pricing and efficient debt recovery.

### Stage 3 — MKR Token Dilution

If ETH crashes so hard and fast that keepers hesitate to buy (why buy a falling asset?), auctions fail to recover enough DAI. The system accumulates **"bad debt"** — unbacked DAI floating in the world.

The smart contract then mints brand new **MKR governance tokens** and auctions them for DAI to fill the hole. This dilutes existing MKR holders — more tokens exist, so each is worth less.

MKR holders are essentially the insurance fund: **earning fees in good times and absorbing losses in bad times.**

> This was triggered during **Black Thursday (March 2020)**, when roughly $6 million in bad debt accumulated and was covered through MKR minting.

### Stage 4 — Emergency Shutdown

If nobody will buy MKR either — the nuclear option. The entire system freezes: no minting, no liquidations, no auctions. Every DAI holder claims a proportional share of whatever collateral remains.

If there's only $0.80 backing per DAI, everyone gets $0.80. The system effectively dies in an orderly wind-down rather than a chaotic collapse.

> **This has never been triggered.**

---

## Visual Summary: Defense Cascade

```
Normal Operation
    │
    ▼
┌─────────────────────────────┐
│  Stage 1: Over-Collateral   │  ← $150 buffer per $100 DAI
│  Absorbs everyday swings    │
└─────────────┬───────────────┘
              │ Collateral ratio breached
              ▼
┌─────────────────────────────┐
│  Stage 2: Keeper Auctions   │  ← Bots buy discounted ETH with DAI
│  DAI burned, debt closed    │     Borrower penalized ~13%
└─────────────┬───────────────┘
              │ Auctions fail to cover debt
              ▼
┌─────────────────────────────┐
│  Stage 3: MKR Dilution      │  ← New MKR minted, auctioned for DAI
│  MKR holders absorb loss    │     Triggered: Black Thursday 2020
└─────────────┬───────────────┘
              │ Nobody buys MKR
              ▼
┌─────────────────────────────┐
│  Stage 4: Emergency Shutdown│  ← System freezes, orderly wind-down
│  Pro-rata collateral claims │     Never triggered
└─────────────────────────────┘
```

---

## Related Documents

- **[Stablecoin Deep Dive: Mechanisms, Dollar Impact & AI Agent Markets](stablecoin_deep_dive.md)** — Covers all stablecoin types, the dollar dominance feedback loop, ECB sovereignty concerns, and the emerging AI agent payment infrastructure (x402, AP2, Tempo, Agentic Wallets).
- **[Algorithmic Stablecoins: The TerraUSD / LUNA Collapse](algorithmic_stablecoins_terra_luna.md)** — The no-reserves model, the death spiral mechanics, and why confidence alone couldn't substitute for real backing.
- **[Synthetic / Hedged Stablecoins: Ethena's USDe](synthetic_stablecoins_ethena_usde.md)** — Delta-neutral hedging, funding rate mechanics, and how USDe solves DAI's capital inefficiency at the cost of exchange dependency.
- **[Hybrid Stablecoins: FRAX & the Fractional-Algorithmic Experiment](hybrid_stablecoins_frax.md)** — Originally aimed to improve on DAI's capital inefficiency through fractional reserves, but ultimately pivoted to full collateralization.
- **[Stablecoin AI Agent Payment Infrastructure](ai_agent_payment_infrastructure.md)** — The four-layer agentic payment stack (AP2, x402/MPP, wallets, settlement chains). DAI circulates within the DeFi layer these protocols transact on.
