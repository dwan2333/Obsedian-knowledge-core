# Crypto-Collateralized Stablecoins: MakerDAO's DAI — A Complete Deep Dive

*Companion document to [Stablecoin Deep Dive: Mechanisms, Dollar Impact & AI Agent Markets](Stable%20Coin%20(Main).md)*

---

**What DAI Is in One Paragraph**

DAI is a stablecoin that lives on Ethereum and tries to stay worth exactly $1, just like USDC or USDT. The big difference is how it's created. USDC is issued by a company called Circle who holds real dollars in a bank for every USDC token. DAI has no company behind it — it's created entirely by smart contracts on Ethereum. Anyone can mint new DAI by locking up cryptocurrency (usually ETH) as collateral and borrowing DAI against it, kind of like a digital pawn shop. The whole system is run by code and governed by people who hold a token called MKR. There's no CEO, no headquarters, no bank account. Everything happens transparently on the blockchain, and anyone can audit the system in real time.

---

**Meet the People in Our Story**

The whole MakerDAO system makes a lot more sense when you imagine it as a handful of characters interacting with one giant smart contract. There are four roles worth knowing.

The first is Alice the Borrower. Alice owns 1 ETH worth $3,000 and she's bullish on Ethereum's future. She doesn't want to sell her ETH because she thinks the price will go up, but she needs cash for a vacation. So she goes to MakerDAO, locks up her ETH, and borrows 2,000 DAI against it. She agrees to pay back the loan plus a Stability Fee every year. Now she has $2,000 in cash to spend, and her ETH stays safely locked up until she pays back the loan. If Ethereum triples in price while her loan is open, she still only owes back the original 2,000 DAI plus interest — so all that appreciation stays with her ETH, which is the whole reason she borrowed instead of selling.

The second is Bob the Saver. Bob already has 1,000 DAI sitting in his wallet doing nothing. Instead of letting it sit there, he deposits it into MakerDAO's savings contract (called the DSR) and earns roughly 5% per year just for holding it there. At the end of one year, his balance has automatically grown to 1,050 DAI. He didn't do anything — the yield just appeared.

The third is Mike the Borrower. Mike does the same thing Alice did, but his story goes wrong when the market crashes. We'll follow Mike later to see what happens when a borrower can't keep their loan safe.

The fourth is Karen the Keeper. Karen runs an automated bot that scans MakerDAO 24/7 looking for borrowers whose collateral has dropped below the safety threshold. When she finds one, her bot jumps in and buys the discounted ETH from the system, making a small profit on each liquidation. Anyone can run a keeper bot — there's no permission needed.

These four roles are the entire ecosystem. Everyone else just trades DAI on exchanges or uses it in DeFi apps.

---

**How Minting Actually Works (Alice's Story)**

When Alice deposits her 1 ETH and wants to borrow DAI, she can't just take the full $3,000 worth. MakerDAO requires what's called a 150% collateralization ratio, meaning her ETH must always be worth at least 1.5 times the size of her loan. So $3,000 divided by 1.5 equals $2,000 — that's the maximum she can borrow. That extra $1,000 cushion is the safety buffer against crypto price volatility.

The moment Alice confirms the transaction, the smart contract does two things at once. It locks her ETH in a vault that nobody (including Alice) can touch while the loan is open. And it creates 2,000 brand-new DAI out of thin air and sends them to her wallet. That DAI didn't exist before Alice took the loan. It was literally invented by the smart contract the moment she borrowed it.

Alice takes her 2,000 DAI and uses it however she wants — swapping it for dollars, paying a contractor, buying NFTs, whatever. The DAI is fungible with all other DAI in existence, so it doesn't matter what she does with her specific tokens.

To get her ETH back, Alice has to return the original 2,000 DAI plus a small Stability Fee (the interest on her loan). The smart contract burns the DAI she returns — destroying it permanently and removing it from circulation — and unlocks her ETH. If ETH appreciated while the loan was open, she benefits from that appreciation on her ETH, not on the DAI itself. DAI is a borrowing tool, not an investment.

---

**Why DAI Charges Interest But USDC Doesn't**

This is one of the most important conceptual differences between stablecoins and worth understanding clearly.

When you want USDC, you don't borrow it. You buy it. You give Circle one real U.S. dollar and they give you one USDC token in exchange. There's no loan, no interest, no monthly payment. You simply swapped one form of dollar (paper) for another form of dollar (a token on Ethereum). When you want your dollar back, you give Circle the USDC and they send you a dollar. Circle holds your dollar in their reserves the entire time you have the USDC. That's why they can earn interest on it themselves. But you, as the USDC holder, never owe anyone anything.

DAI is fundamentally different. You can't buy DAI directly from MakerDAO. You have to borrow it into existence. You lock up your ETH as collateral, the smart contract creates brand-new DAI for you, and you owe interest on that loan for as long as it's open. If you want to get your ETH back, you have to return the DAI plus the Stability Fee. That's why Alice pays interest and a USDC buyer doesn't.

This also explains why USDC doesn't have a built-in savings rate. Circle's business model is to keep the interest earned on their reserves as profit. In 2024 they earned about $1.6 billion from this — 99% of their total revenue. None of that goes to USDC holders. MakerDAO does the opposite: they share most of their income with savers through the DSR, which is what makes DAI more attractive if you're just parking stablecoins long-term.

So the basic rule is: USDC is a receipt for cash you already own, no interest charged either way. DAI is a loan you took out against your crypto, you pay interest to keep it open, and MakerDAO turns around and uses that fee revenue to pay savers a yield.

---

**Key Differences from USDC and USDT**

| Dimension | USDC / USDT | DAI |
|---|---|---|
| Trust model | Trust the issuing company (Circle, Tether) | Trust that the smart contract code works correctly |
| Censorship resistance | Issuers can freeze wallets (Circle has done so under government order) | Nobody can freeze your tokens — fully decentralized |
| Capital efficiency | 1:1 backing — deposit $1, get $1 | Capital inefficient — need ~$1.50 locked to get $1 out |
| Transparency | Periodic attestation reports | Real-time, on-chain, auditable by anyone at any time |
| Core tradeoff | Simplicity and efficiency | Decentralization and transparency |

---

**When Things Go Wrong: Mike Gets Liquidated**

Now let's watch what happens when a borrower can't keep their loan safe.

Mike does exactly what Alice did. He locks his 1 ETH worth $3,000 into MakerDAO and borrows the maximum of 2,000 DAI to renovate his kitchen. His collateralization ratio starts at exactly 150%, which is the absolute minimum allowed. He's cutting it close.

Two months later, the crypto market crashes. ETH falls from $3,000 to $2,400 per coin. Mike's vault now has 1 ETH worth $2,400 backing a 2,000 DAI debt, which is a 120% ratio — well below the required 150%. The smart contract notices this immediately and flags his vault as eligible for liquidation. Mike doesn't get a warning email or a phone call. The contract just marks his vault and makes it visible to every keeper bot on the planet.

Karen the Keeper's bot sees the flag instantly and does the math. "Mike owes 2,000 DAI plus a 13% liquidation penalty (260 DAI), so whoever wants his ETH has to pay at least 2,260 DAI. His ETH is worth $2,400 on the open market, so there's $140 of room for profit." Her bot decides to bid.

MakerDAO uses a Dutch auction format where the price starts high and drops gradually over a few minutes. Karen's bot waits for the right moment and buys when the price reaches roughly 2,300 DAI for the entire 1 ETH. She pays 2,300 DAI to the contract and receives 1 ETH in return. All of this happens in a single atomic transaction on the blockchain.

Now the smart contract automatically splits up that 2,300 DAI into three destinations. The first 2,000 DAI gets burned, which destroys Mike's outstanding debt — his loan is officially closed. The next 260 DAI flows into MakerDAO's Surplus Buffer as the 13% liquidation penalty. The remaining 40 DAI is sent back to Mike's wallet as the leftover from the auction (since Karen paid more than the strict minimum).

Let me total up where everyone ends up. Karen walks away with 1 ETH worth $2,400 for which she paid 2,300 DAI — a profit of about $100 on this single transaction. She runs this bot 24/7 and catches dozens of liquidations per week, so this is a real business. MakerDAO collected 260 DAI in pure protocol revenue, which gets added to the same Surplus Buffer that funds the DSR. Mike is the loser. He came in with 1 ETH worth $3,000, and after liquidation he's left with the 2,000 DAI he already spent on his kitchen plus the 40 DAI of auction leftover. Effectively he sold his ETH at a steep discount and paid a 13% penalty for the privilege.

One detail worth understanding is that MakerDAO doesn't need Mike's specific DAI back to close his loan. DAI is fungible — all DAI tokens are interchangeable. Karen supplied her own DAI to buy Mike's ETH. Mike is free to keep or spend whatever DAI he originally borrowed. What he loses is the ETH, not the DAI. He walked away with cash and lost the underlying asset. This is why getting liquidated is so painful — you effectively sold your ETH for a price well below market value, with a 13% tax on top.

---

**Where MakerDAO's Huge Pile of Money Actually Comes From**

A natural question is: if MakerDAO is decentralized with no company, where does its giant reserve of money come from? The answer is that it came from three real revenue sources, accumulated automatically by the smart contracts over many years.

The first source is borrower interest (Stability Fees). Every time someone like Alice borrows DAI, she pays interest on the loan. Multiply this by hundreds of thousands of borrowers over many years and you get a massive accumulated pile. All of it flows into a treasury called the Surplus Buffer through the smart contracts — no human collects it, no company invoices anyone, the code just routes the payments automatically.

The second source, and this is the surprising one, is U.S. Treasury bills. Starting in 2022, the MakerDAO community voted to take billions of dollars from their reserves and use it to buy short-term U.S. government bonds through partnerships with companies like Monetalis and BlockTower. Those T-bills pay roughly 5% per year in interest, paid by the U.S. government in real dollars. That interest gets converted into DAI and flows back into the Surplus Buffer. In 2023, this single source generated about 80% of all of MakerDAO's revenue — over $13 million. So MakerDAO is basically a U.S. Treasury bond fund wearing a crypto costume. Most of their income comes from being a creditor to the U.S. government.

The third source is liquidation penalties. As we just saw with Mike, every time a borrower gets wiped out, MakerDAO collects a 13% penalty on top of recovering the debt. This isn't a constant flow — it spikes during market crashes — but over time it adds millions of dollars to the Surplus Buffer. In fact, when you hear about a "wave of liquidations" during a crypto crash, that's actually good for DAI savers, because every liquidation pumps more revenue into the pile that funds their yield.

Put all three sources together and MakerDAO has a self-sustaining revenue machine. Borrowers pay fees, T-bills generate interest, and liquidations collect penalties. Every dollar of this flows into one big pool controlled by the smart contract, ready to be deployed wherever the community votes to send it.

---

**How Bob Earns Yield From the DSR**

Now we can answer where Bob's 5% savings yield actually comes from. When Bob deposits 1,000 DAI into the savings contract and watches it grow to 1,050 DAI over the year, that extra $50 isn't created out of thin air. It comes directly from the Surplus Buffer. Roughly $40 of his $50 in yield originated as interest from U.S. Treasury bills that MakerDAO holds in reserves. The other $10 or so came from borrowers like Alice paying their Stability Fees. A small amount came from liquidation penalties on unlucky borrowers like Mike.

The really interesting insight is that Bob is effectively earning U.S. Treasury bond yield through a crypto wrapper. He never opens a brokerage account, never signs up with the U.S. Treasury, never deals with tax forms tied to bond purchases. He just holds a token in his wallet and the yield appears automatically. MakerDAO is doing all the work of buying real bonds, collecting real interest, and converting it into more DAI for him.

Bob's month-by-month balance during his year in the DSR looks like this. In January he deposits 1,000 DAI. By June he has 1,025 DAI — the first half of his yield. By December he has 1,050 DAI — the full year's yield. Of that $50 gain, about $40 originated from U.S. Treasury interest and the rest from crypto borrowers. All of it flowed through MakerDAO's Surplus Buffer before landing in his wallet.

There is a catch: the DSR rate isn't fixed. It moves up and down based on what the U.S. Federal Reserve is doing with interest rates. When the Fed raises rates, T-bills pay more, MakerDAO's income goes up, and the community can vote to raise the DSR. When the Fed cuts rates, T-bills pay less, MakerDAO's income drops, and the DSR has to come down to match. In 2023 the DSR was as high as 8% because the Fed had pushed rates above 5%. By 2025 the Fed started cutting, MakerDAO's T-bill income shrunk, and the DSR dropped to around 4.5%. MakerDAO can't pay savers more than they earn, so the math has to balance.

---

**The Peg Stability Module: Keeping DAI Exactly at $1**

Long-term, interest rates (the Stability Fee and the DSR) adjust supply and demand for DAI to keep it near $1. But day-to-day, a different mechanism does the real work of holding the peg. It's called the Peg Stability Module, or PSM.

The PSM is a special vault that lets anyone instantly swap DAI for centralized stablecoins like USDC at exactly a 1:1 ratio. This creates an immediate, risk-free arbitrage opportunity that forces the price back to $1.

Here's how it plays out. If DAI ever drops to $0.99 on a regular exchange, arbitrageurs rush in to buy the cheap DAI, bring it to the PSM, and swap it for USDC at 1:1. They make a 1-cent profit per coin, and their buying pressure on the open market pushes DAI back up toward $1.00. In the opposite direction, if DAI rises to $1.01, arbitrageurs take USDC, use the PSM to mint fresh DAI at exactly $1.00, and immediately sell that DAI on the open market for $1.01. This floods the market with new DAI and pushes the price back down. The beauty of the PSM is that both of these are automatic and profitable, so anyone with capital can do it, and the result is that DAI almost never strays more than a cent or two from $1 for very long.

---

**How the Community Actually Votes**

All of these decisions — setting the DSR, adjusting Stability Fees, approving T-bill investments, deciding collateral types — are made by people who hold a token called MKR. If you own MKR, you get a vote. The more MKR you hold, the more votes you have. MKR holders are essentially the shareholders of MakerDAO.

Voting happens in two stages. The first is a Governance Poll, which is basically a community temperature check. Someone proposes an idea, people discuss it on the MakerDAO forum, and everyone votes on whether they like the direction. Polls usually run for 2-3 days. Nothing happens to the actual smart contracts at this stage — it's just to see if there's enough consensus to move forward.

If the poll passes, the proposal moves to an Executive Vote, which is the one that actually changes the protocol. The way Executive Votes work is unusual: instead of a yes/no on a single proposal, all proposals compete continuously, and whichever has the most MKR locked behind it becomes the active state of the system. It's like a tug-of-war that never officially ends — a new proposal has to gather more MKR support than the current winning one in order to flip the system to its new state.

To actually vote, MKR holders have to lock their tokens into a special voting contract. While the tokens are locked, they count toward whatever proposal you're supporting. You can withdraw them anytime, but while they're locked they're tied up in your vote.

So when you read a headline like "MakerDAO raised the DSR from 4% to 5%," the real sequence is this. Someone (often a core contributor or risk team) wrote up a proposal explaining why the rate should change. The community discussed it on the forum. A Governance Poll ran for a few days and passed. Someone wrote the actual code change and submitted it as an Executive Vote. MKR holders locked their tokens behind the new proposal, and once enough MKR voted in favor, the smart contract automatically updated the DSR rate. Anyone holding DAI in the savings contract started earning the new rate immediately.

MKR holders take all of this seriously because they have skin in the game. If everything goes well, MKR captures protocol profits. But if MakerDAO ever has bad debt that can't be covered, the smart contract mints new MKR tokens and sells them to fill the hole — which dilutes everyone who holds MKR. So they have a direct financial incentive to vote responsibly: set rates that bring in enough revenue, manage risk carefully, and keep the system solvent.

---

**The Four Stages of Defense**

MakerDAO has a four-stage defense system designed to handle increasingly bad situations. Each stage is more painful than the last.

The first stage is over-collateralization. The 150% requirement means borrowers always have a buffer between their loan and their collateral. This handles normal everyday volatility without any drama at all. Most borrowers never see any of the later stages because their positions stay healthy.

The second stage is keeper auctions, which is what happened to Mike. When ETH falls enough to eat through the buffer, keeper bots like Karen step in and liquidate the vault. They pay off the debt, collect their profit, and MakerDAO collects the 13% penalty. This works fine under moderate stress and is the normal way the system handles crashes.

The third stage is MKR dilution. When a crash is so violent that auctions fail to recover enough DAI — because ETH is falling so fast that even discounted auctions can't find buyers — MakerDAO accumulates what's called bad debt, meaning DAI in circulation that isn't backed by enough collateral. The smart contract then mints brand-new MKR tokens and auctions them for DAI to fill the hole. MKR holders absorb the loss through dilution. This was triggered exactly once in MakerDAO's history, during Black Thursday in March 2020, when about $6 million in bad debt accumulated and was covered through MKR minting.

The fourth stage is Emergency Shutdown, which is the nuclear option. If nobody will buy MKR either, the entire system freezes. No more minting, no more liquidations, no more auctions. Every DAI holder claims a proportional share of whatever collateral remains. If there's only $0.80 of backing per DAI, everyone gets $0.80. The system effectively dies in an orderly wind-down rather than a chaotic collapse. This has never been triggered.

---

**Why It All Matters**

If you only remember one thing about MakerDAO, it's this: it's a decentralized protocol that lets people borrow stablecoins against their crypto, charges them interest on those loans, invests its reserves in U.S. Treasury bills for safe yield, collects 13% penalty fees from liquidated borrowers, and shares most of that combined income with people who park their DAI in the savings contract — all without any company in the middle, governed by a community of MKR token holders who vote on every important decision.

The genius of the system is that every role contributes something real. Borrowers pay interest in exchange for keeping their crypto exposure. Savers earn yield that's mostly backed by real U.S. Treasury bonds. Keepers profit from liquidating risky positions. MKR holders earn protocol profits in good times and absorb losses in bad times. And because everything runs on smart contracts, nobody can freeze your tokens, change the rules on you unilaterally, or stop the system from functioning. The only way MakerDAO dies is if enough people stop believing in it that nobody will buy MKR — at which point the Emergency Shutdown kicks in and everyone gets a fair share of whatever's left.

---

## Related Documents

- **[Stablecoin Deep Dive: Mechanisms, Dollar Impact & AI Agent Markets](Stable%20Coin%20(Main).md)** — Covers all stablecoin types, the dollar dominance feedback loop, ECB sovereignty concerns, and the emerging AI agent payment infrastructure (x402, AP2, Tempo, Agentic Wallets).
- **[Algorithmic Stablecoins: The TerraUSD / LUNA Collapse](algorithmic_stablecoins_terra_luna.md)** — The no-reserves model, the death spiral mechanics, and why confidence alone couldn't substitute for real backing.
- **[Synthetic / Hedged Stablecoins: Ethena's USDe](synthetic_stablecoins_ethena_usde.md)** — Delta-neutral hedging, funding rate mechanics, and how USDe solves DAI's capital inefficiency at the cost of exchange dependency.
- **[Hybrid Stablecoins: FRAX & the Fractional-Algorithmic Experiment](Hybrid%20Stablecoins%20Frax.md)** — Originally aimed to improve on DAI's capital inefficiency through fractional reserves, but ultimately pivoted to full collateralization.
- **[Stablecoin AI Agent Payment Infrastructure](ai_agent_payment_infrastructure.md)** — The four-layer agentic payment stack (AP2, x402/MPP, wallets, settlement chains). DAI circulates within the DeFi layer these protocols transact on.
