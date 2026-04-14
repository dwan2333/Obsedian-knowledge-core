# Crypto-Collateralized Stablecoins: MakerDAO's DAI — A Complete Deep Dive

*Companion document to [Stablecoin Deep Dive: Mechanisms, Dollar Impact & AI Agent Markets](Stable%20Coin%20(Main).md)*

---

## What DAI Is in One Paragraph

DAI is a stablecoin that lives on Ethereum and tries to stay worth exactly $1, just like USDC or USDT. The big difference is how it's created. USDC is issued by a company called Circle who holds real dollars in a bank for every USDC token. DAI has no company behind it — it's created entirely by smart contracts on Ethereum. Anyone can mint new DAI by locking up cryptocurrency as collateral and borrowing DAI against it, kind of like a digital pawn shop. The whole system is run by code and governed by people who hold a token called MKR. There's no CEO, no headquarters, no bank account. Everything happens transparently on the blockchain, and anyone can audit the system in real time.

---

## The Four Roles in MakerDAO

The whole MakerDAO system makes more sense when you imagine it as four characters interacting with one giant smart contract.

| Role | Who They Are | What They Do |
|---|---|---|
| **Alice the Borrower** | ETH holder who wants cash without selling | Locks ETH, mints DAI, pays Stability Fee |
| **Bob the Saver** | DAI holder looking for yield | Deposits DAI into DSR, earns ~5% APY |
| **Mike the Borrower** | Borrower who gets too close to the edge | Gets liquidated when ETH price drops |
| **Karen the Keeper** | Bot operator | Scans for unsafe vaults, buys discounted collateral |

Alice owns 1 ETH worth $3,000 and she's bullish on Ethereum's future. She doesn't want to sell, but she needs cash for a vacation. So she locks her ETH in MakerDAO and borrows 2,000 DAI against it. If Ethereum triples while her loan is open, all that appreciation stays with her ETH — the DAI loan amount is fixed.

Bob already has 1,000 DAI sitting idle. He deposits it into MakerDAO's savings contract (the DSR) and earns roughly 5% per year. By the end of one year, his balance has grown to 1,050 DAI automatically.

Mike does the same thing as Alice but cuts it too close, and his story goes wrong when the market crashes — we'll follow him through the liquidation section.

Karen runs an automated bot that scans MakerDAO 24/7 looking for vaults below the safety threshold. When she finds one, her bot jumps in and buys the discounted collateral. Anyone can run a keeper bot — no permission needed.

---

## How Minting Actually Works (Alice's Story)

When Alice deposits her 1 ETH, she can't take the full $3,000 worth of DAI. MakerDAO requires a **150% collateralization ratio** — her ETH must always be worth at least 1.5× the size of her loan. So $3,000 ÷ 1.5 = $2,000 maximum. That extra $1,000 cushion is the safety buffer against volatility.

The smart contract does two things at once: it locks her ETH (nobody, including Alice, can touch it while the loan is open), and it creates 2,000 brand-new DAI out of thin air and sends it to her wallet. That DAI didn't exist before — it was minted by the contract the moment she borrowed.

To get her ETH back, Alice returns the original 2,000 DAI plus a small **Stability Fee** (the interest on her loan). The contract burns the returned DAI — destroying it permanently — and unlocks her ETH.

---

## What Collateral MakerDAO Accepts

MakerDAO is not limited to ETH. It accepts a range of crypto assets, each with its own stability fee and liquidation ratio set by MKR governance based on that asset's risk profile.

| Collateral Type | How It Enters | Stability Fee Logic |
|---|---|---|
| **ETH, wBTC, stETH** | Standard vault (overcollateralized) | Higher risk = higher fee |
| **USDC, stablecoins** | Peg Stability Module — 1:1 swap | No ongoing fee; one-time swap fee only |
| **RWA (T-bills, bonds)** | Off-chain via institutional partners | Yield flows back to MakerDAO |

For volatile crypto assets, the vault mechanism works as described above — you overcollateralize, pay a stability fee, and get liquidated if you fall below the ratio. Riskier assets like wBTC carry higher fees than ETH because they depend on a bridge and carry additional counterparty risk. stETH may carry a slightly lower fee because it's yield-bearing.

For stablecoins like USDC, the vault model doesn't apply. Charging ongoing interest on something already pegged to $1 makes no sense — there's no risk premium to justify it. Instead, USDC enters through the **Peg Stability Module**, explained in its own section below.

---

## Why DAI Charges Interest But USDC Doesn't

When you want USDC, you don't borrow it — you buy it. You give Circle one real dollar and they give you one USDC. There's no loan, no interest, no monthly payment. When you want your dollar back, Circle sends it. They hold your dollar the whole time and earn interest on it themselves. That's Circle's entire business model — in 2024 they earned about $1.6 billion this way, 99% of their total revenue. None of that goes to USDC holders.

DAI is fundamentally different. You can't buy DAI from MakerDAO — you have to borrow it into existence. You lock up ETH, the contract creates fresh DAI, and you owe interest on that loan for as long as it's open. MakerDAO then shares most of that income with savers through the DSR, which is what makes DAI more attractive if you're just parking stablecoins long-term.

The basic rule: **USDC is a receipt for cash you already own — no interest either way. DAI is a loan you took out against your crypto — you pay to keep it open, and MakerDAO pays that forward to savers.**

---

## Key Differences from USDC and USDT

| Dimension | USDC / USDT | DAI |
|---|---|---|
| Trust model | Trust the issuing company | Trust the smart contract code |
| Censorship resistance | Issuers can freeze wallets | Nobody can freeze your tokens |
| Capital efficiency | 1:1 backing | ~1.5:1 needed to borrow $1 |
| Transparency | Periodic audit reports | Real-time, on-chain, auditable always |
| Built-in yield | None | DSR savings rate (~5% APY) |

---

## How Bob Earns Yield: The DAI Savings Rate

When Bob deposits 1,000 DAI into the savings contract and watches it grow to 1,050 DAI, that $50 isn't created from nothing. About $40 of it originated as yield from U.S. Treasury bills that MakerDAO holds in reserves. The other $10 came from borrowers like Alice paying their Stability Fees, with a small amount from liquidation penalties on borrowers like Mike.

Bob is effectively earning U.S. Treasury bond yield through a crypto wrapper. He never opens a brokerage account, never signs up with the Treasury. He just holds a token and the yield appears. MakerDAO does all the work of buying real bonds, collecting real interest, and converting it into more DAI for him.

The DSR rate isn't fixed — it moves with the U.S. Federal Reserve. When the Fed raised rates in 2023, T-bills paid more and the DSR hit 8%. When the Fed started cutting in 2025, T-bill income shrank and the DSR dropped to around 4.5%. MakerDAO can't pay savers more than they earn.

### How Often Does the Yield Compound?

The DSR does not compound monthly or daily. It compounds **continuously — every Ethereum block, roughly every 12 seconds.**

The smart contract stores a tiny per-second multiplier (approximately 1.0000000015851 at 5% APY) rather than an annual figure. Every block, the rate ticks forward by that sliver. There are no payout events or settlement dates. If you deposit at 9am and withdraw at 9pm the same day, you've earned exactly twelve hours of yield, calculated to the second. The "5% APY" figure is just the human-readable label for this continuously running mechanism.

---

## sDAI: The Tradeable Version

The standard DSR locks your DAI inside the savings contract while it earns yield. That works fine — but while it's locked, you can't trade it, post it as collateral elsewhere in DeFi, or send it to anyone without withdrawing first.

**sDAI** solves this. When you deposit DAI into the sDAI contract, you receive sDAI tokens in return. Those tokens are fully transferable ERC-20 tokens — you can trade them, use them as collateral on other protocols, or send them to a hardware wallet. The yield keeps compounding regardless of where the token sits, because it's embedded in the **exchange rate between sDAI and DAI**, which ticks upward every block.

```
Standard DSR:
  Deposit 1,000 DAI → balance grows to 1,050 DAI after 1 year
  Your DAI is locked — cannot be moved or used elsewhere

sDAI:
  Deposit 1,000 DAI → receive 1,000 sDAI (exchange rate = 1.00)
  After 1 year at 5% APY → exchange rate is now 1.05
  Your 1,000 sDAI redeems for 1,050 DAI
  But you could have traded, lent, or transferred it the entire time
```

Think of it like a savings bond you can hand to someone else mid-term. The new holder picks up the yield from that point forward. The previous holder walks away with whatever it was worth at the moment of transfer. This makes sDAI composable across all of DeFi in a way plain DSR never was.

---

## When Things Go Wrong: Mike Gets Liquidated

Mike does exactly what Alice did — locks 1 ETH worth $3,000 and borrows the maximum 2,000 DAI. His collateralization ratio starts at exactly 150%, cutting it close.

Two months later, ETH falls from $3,000 to $2,400. Mike's vault now has 1 ETH worth $2,400 backing a 2,000 DAI debt — a 120% ratio, well below the required 150%. The smart contract flags his vault immediately. Mike gets no warning. The contract just marks his vault visible to every keeper bot on the planet.

Karen's bot sees the flag and calculates: Mike owes 2,000 DAI plus a **13% liquidation penalty** (260 DAI), so his ETH must sell for at least 2,260 DAI. His ETH is worth $2,400 on the open market, leaving room for a small profit.

MakerDAO runs a **Dutch auction** — price starts high and drops gradually over minutes. Karen's bot waits for the right moment and buys 1 ETH for 2,300 DAI in a single atomic transaction. The contract splits that 2,300 DAI automatically:

- **2,000 DAI burned** → Mike's debt closed
- **260 DAI → Surplus Buffer** → MakerDAO's 13% penalty revenue
- **40 DAI → back to Mike** → the auction surplus

Karen walks away with 1 ETH (worth $2,400) for 2,300 DAI — about $100 profit. MakerDAO collected 260 DAI in protocol revenue. Mike came in with 1 ETH worth $3,000 and left with the 2,000 DAI he already spent plus 40 DAI — effectively selling his ETH at a steep discount with a 13% penalty on top.

---

## Where MakerDAO's Money Comes From

| Revenue Source | Share | How It Works |
|---|---|---|
| **U.S. Treasury bills** | ~80% | PSM USDC deployed into T-bills via Monetalis, BlockTower |
| **Stability Fees** | ~15% | Borrower interest from all active vaults |
| **Liquidation penalties** | ~5% | 13% penalty on each liquidated vault |

The T-bill number surprises most people. Starting in 2022, MakerDAO voted to take billions in USDC from the PSM and deploy it into short-term U.S. government bonds. Those bonds pay ~5% per year in real dollars, which gets converted to DAI and flows into the Surplus Buffer. In 2023, this single source generated over $13 million — roughly 80% of all MakerDAO revenue that year.

All three sources flow automatically into one treasury controlled by the smart contract. No human collects it, no company invoices anyone, and that treasury is what funds Bob's savings yield.

---

## The Peg Stability Module: Keeping DAI at $1

Day-to-day, a mechanism called the **Peg Stability Module (PSM)** does the real work of holding DAI's price. It lets anyone instantly swap DAI for USDC at exactly 1:1, creating an immediate arbitrage that forces the price back to $1.

If DAI drops to $0.99 → arbitrageurs buy cheap DAI, swap it at the PSM for USDC at 1:1, pocket the 1-cent profit, and their buying pushes DAI back up.

If DAI rises to $1.01 → arbitrageurs bring USDC to the PSM, mint fresh DAI at exactly $1.00, sell it on the open market for $1.01, and the flood of new DAI pushes the price back down.

Both directions are automatic, profitable, and open to anyone. The result is that DAI almost never strays more than a cent or two from $1 for long. The trade-off is that DAI's reserves include large amounts of USDC — a centralized stablecoin — which makes DAI less "purely decentralized" than its original design intended.

---

## How the Community Votes

All decisions — setting the DSR, adjusting Stability Fees, approving T-bill investments, adding collateral types — are made by **MKR holders**. The more MKR you hold, the more votes you have.

| Vote Type | Purpose | Duration | Effect |
|---|---|---|---|
| **Governance Poll** | Temperature check — does the community support this direction? | 2-3 days | No contract changes; signals consensus |
| **Executive Vote** | The change that actually happens on-chain | Ongoing | Whichever proposal has the most MKR locked wins |

The Executive Vote mechanic is unusual: proposals compete continuously, and whichever has the most MKR tokens locked behind it becomes the active state of the system. A new proposal has to gather more MKR support than the current winner to flip the protocol to the new state.

MKR holders take voting seriously because they have skin in the game. If everything goes well, MKR captures protocol profits. If the system ever runs a bad-debt deficit, new MKR gets minted and sold to cover it — diluting every MKR holder. So they have a direct financial incentive to vote conservatively.

---

## The Four Stages of Defense

| Stage | Trigger | Mechanism | Cost |
|---|---|---|---|
| **Over-collateralization** | Normal volatility | 150% ratio absorbs small drops | None — borrower manages their own ratio |
| **Keeper Auctions** | Vault falls below 150% | Bots liquidate + collect 13% penalty | Borrower loses collateral at a discount |
| **MKR Dilution** | Bad debt exceeds Surplus Buffer | New MKR minted and sold for DAI | All MKR holders diluted |
| **Emergency Shutdown** | System-level failure | Everything freezes; DAI redeemable for proportional collateral share | Protocol effectively ends |

Stage 3 — MKR Dilution — was triggered exactly once in MakerDAO's history. On **Black Thursday, March 2020**, ETH crashed so fast that liquidation auctions failed to find enough buyers. About $6 million in bad debt accumulated, and the protocol covered it by minting and auctioning new MKR tokens.

Stage 4 — Emergency Shutdown — has never been triggered. It exists as the ultimate guarantee that DAI is always redeemable for something real, even if everything else fails.

---

## Why It All Matters

MakerDAO is a decentralized protocol that lets people borrow stablecoins against their crypto, charges interest on those loans, invests its reserves in U.S. Treasury bills, collects 13% penalty fees from liquidated borrowers, and shares most of that combined income with DAI savers — all without any company in the middle.

Every role contributes something real. Borrowers pay interest in exchange for keeping their crypto exposure. Savers earn yield backed by real U.S. Treasury bonds. Keepers profit from liquidating risky positions. MKR holders earn protocol profits in good times and absorb losses in bad times. And because everything runs on smart contracts, nobody can freeze your tokens, change the rules on you unilaterally, or stop the system from functioning.

---

## Related Documents

- **[Stablecoin Deep Dive: Mechanisms, Dollar Impact & AI Agent Markets](Stable%20Coin%20(Main).md)** — Covers all stablecoin types, the dollar dominance feedback loop, ECB sovereignty concerns, and the emerging AI agent payment infrastructure (x402, AP2, Tempo, Agentic Wallets).
- **[Algorithmic Stablecoins: The TerraUSD / LUNA Collapse](algorithmic_stablecoins_terra_luna.md)** — The no-reserves model, the death spiral mechanics, and why confidence alone couldn't substitute for real backing.
- **[Synthetic / Hedged Stablecoins: Ethena's USDe](synthetic_stablecoins_ethena_usde.md)** — Delta-neutral hedging, funding rate mechanics, and how USDe solves DAI's capital inefficiency at the cost of exchange dependency.
- **[Hybrid Stablecoins: FRAX & the Fractional-Algorithmic Experiment](Hybrid%20Stablecoins%20Frax.md)** — Originally aimed to improve on DAI's capital inefficiency through fractional reserves, but ultimately pivoted to full collateralization.
- **[Stablecoin AI Agent Payment Infrastructure](ai_agent_payment_infrastructure.md)** — The four-layer agentic payment stack (AP2, x402/MPP, wallets, settlement chains). DAI circulates within the DeFi layer these protocols transact on.
