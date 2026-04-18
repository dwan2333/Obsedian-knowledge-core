# Chapter 1 — Probability and Counting

*Companion document to [Introduction to Probability (Main)](<../Introduction to Probability (Main).md>)*

_Research compiled 2026-04-19 — Blitzstein & Hwang, *Introduction to Probability*, Ch. 1, with NotebookLM-assisted summaries and full main-agent verification of all 62 exercises._

---

![Infographic](chapter1_infographic.png)

---

> [!info] Chapter Essence
> Chapter 1 establishes probability as a rigorous mathematical framework for quantifying uncertainty — moving beyond unreliable human intuition. When outcomes are strictly symmetric, probabilities follow from careful **counting**. When they aren't, probability must be defined by **formal axioms** that behave like mass distributed across events. The chapter's recurring warning: precisely define your sample space, label distinct objects, and verify equal-likelihood before assuming it.

---

## 1.1 Why Study Probability?

Probability is the **logic of uncertainty**, the natural counterpart to mathematics's logic of certainty. The chapter opens with ten domains where probabilistic thinking is indispensable:

| Domain | Why probability matters |
|---|---|
| **Statistics** | Foundation for all data analysis |
| **Physics** | Quantum mechanics, statistical mechanics |
| **Biology** | Genetics, evolution, epidemiology |
| **Computer Science** | Randomized algorithms, machine learning |
| **Meteorology** | Weather forecasting |
| **Gambling** | Probability's historical birthplace |
| **Finance** | Modeling stock prices, derivatives, risk |
| **Political Science** | Surveys, election forecasting |
| **Medicine** | Randomized clinical trials |
| **Everyday Life** | Avoiding fallacies, making predictions |

Even Leibniz and Newton made elementary probabilistic errors — a reminder that intuition is unreliable. The chapter offers three defenses against this:

> [!tip] Three Anti-Fallacy Strategies
> - **Simulation** — run the experiment many times and observe what actually happens
> - **Biohazards** — study common mistakes (the textbook flags them with a ☣ symbol) so you recognize invalid reasoning
> - **Sanity checks** — solve the same problem multiple ways, or check simple/extreme cases

---

## 1.2 Sample Spaces and Pebble World

Probability lives on top of **set theory**. When an experiment runs, the unknown crystallizes into a single outcome — and the structure of all possible outcomes is what we reason about.

> [!definition] Definition 1.2.1 — Sample Space and Event
> The **sample space** $S$ of an experiment is the set of all possible outcomes. An **event** $A$ is a subset of $S$. We say $A$ *occurred* if the actual outcome lies in $A$.

For finite sample spaces, the textbook introduces **Pebble World** — a visualization where each outcome is a single pebble, and an event is a collection of pebbles. Performing the experiment amounts to randomly picking up one pebble.

![Figure 1.1 — Pebble World with two events](chapter1_fig_1.1_pebble_world.png)

Set theory gives us the language for combining events: union $A \cup B$ ("at least one occurs"), intersection $A \cap B$ ("both occur"), complement $A^c$ ("does not occur").

> [!example] Example — Coin Flips
> Flip a coin 10 times. The sample space is all length-10 strings of H's and T's. Let $A_j$ = "the $j$th flip is H." Then "at least one Heads" is $\bigcup_{j=1}^{10} A_j$, and "all Heads" is $\bigcap_{j=1}^{10} A_j$.

> [!example] Example — Pick a Card
> Drawing one card from a standard deck gives $|S| = 52$. With events $A$ (ace), $B$ (black), $D$ (diamond), $H$ (heart), the event "red non-ace" can be written as $(A \cup B)^c = A^c \cap B^c$. If a joker turned up, it would mean we picked the wrong sample space.

The English ↔ set-notation translation goes both ways: "something must happen" ↔ $S$; "not $A$" ↔ $A^c$; "$A$ and $B$ are mutually exclusive" ↔ $A \cap B = \emptyset$.

---

## 1.3 Naive Definition of Probability

The historical starting point for probability was simple counting.

> [!definition] Definition — Naive Probability
> For an event $A$ with finite sample space $S$ where every outcome is equally likely:
> $$P_{\text{naive}}(A) = \frac{|A|}{|S|}$$

In Pebble World, this is just the fraction of pebbles inside $A$. A useful immediate corollary:
$$P_{\text{naive}}(A^c) = \frac{|S| - |A|}{|S|} = 1 - P_{\text{naive}}(A)$$
**Computing the complement is often easier** than computing $A$ directly — a recurring problem-solving move throughout the book.

> [!warning] When the Naive Definition Fails
> It requires *both* a finite sample space *and* equal likelihood of every outcome. The classic abuse: "the probability of life on Mars is $1/2$ because either there is or there isn't." That's a sample space of size 2, but the outcomes are not equally likely.

The naive definition is valid in three settings:

| Justification | Example |
|---|---|
| **Physical symmetry** | Fair coin, well-shuffled deck, balanced die |
| **Equal-likelihood by design** | Simple random sample of $n$ from $N$ |
| **Null model** | Baseline for comparing observed data |

---

## 1.4 How to Count

Since most naive probabilities reduce to ratios of counts, the chapter spends serious time on combinatorics.

### 1.4.1 Multiplication Rule

> [!definition] Theorem — Multiplication Rule
> If a compound experiment has two stages — the first with $a$ outcomes, the second with $b$ outcomes (for each outcome of the first) — then the compound has $a \cdot b$ outcomes. This generalizes to any number of stages.

![Figure 1.2 — Tree diagram for the multiplication rule](chapter1_fig_1.2_multiplication_rule_tree.png)

> [!example] Example — Runners, Chessboard, Subsets
> - Choosing 1st/2nd/3rd from 10 runners: $10 \cdot 9 \cdot 8 = 720$
> - Specifying a row and column on an $8 \times 8$ chessboard: $8 \cdot 8 = 64$
> - Number of subsets of an $n$-element set: $2^n$ (each element is in or out)

![Figure 1.3 — Chessboard and crossword grid](chapter1_fig_1.3_chessboard_crossword.png)

> [!example] Example — Ice Cream Cones
> 2 cones, 3 flavors → $2 \cdot 3 = 6$ combinations. Order two cones in a day → $6^2 = 36$ ordered pairs (or 21 if order doesn't matter).

![Figure 1.4 — Ice cream cone tree diagram](chapter1_fig_1.4_ice_cream_cone_tree.png)

Two specializations follow immediately:

| Sampling method | Count | When used |
|---|---|---|
| **With replacement** | $n^k$ | Each draw is independent; values can repeat |
| **Without replacement** | $n(n-1)(n-2)\cdots(n-k+1) = \dfrac{n!}{(n-k)!}$ | Each draw removes the item; order matters |

Arranging all $n$ distinct objects in order: $n!$ permutations.

> [!example] Example — Birthday Problem
> Among $k$ people with uniformly random birthdays, $P(\text{at least one match}) = 1 - \dfrac{365 \cdot 364 \cdots (365-k+1)}{365^k}$. This crosses 0.5 at $k = 23$ — far smaller than most people's intuition.

![Figure 1.5 — Birthday problem probability vs k](chapter1_fig_1.5_birthday_problem.png)

> [!example] Example — Leibniz's Mistake
> Leibniz argued sums of 11 and 12 on two dice were equally likely by treating the dice as indistinguishable. The correct approach **labels** the dice — then 11 has 2 ways ((5,6),(6,5)) and 12 has only 1 way ((6,6)).

### 1.4.2 Adjusting for Overcounting

When each possibility is counted exactly $c$ times, divide by $c$.

> [!example] Example — Committees and Teams
> Choosing 2 people from 4 as an ordered list: $4 \cdot 3 = 12$. As an unordered committee: $12/2 = 6$. Splitting 4 into two unordered teams of 2: $6/2 = 3$.

> [!definition] Definition — Binomial Coefficient
> $\binom{n}{k}$ ("$n$ choose $k$") is the number of size-$k$ subsets of an $n$-element set. The closed form:
> $$\binom{n}{k} = \frac{n(n-1)\cdots(n-k+1)}{k!} = \frac{n!}{(n-k)!\,k!}$$
> (with $\binom{n}{k} = 0$ when $k > n$).

The denominator $k!$ corrects for overcounting: each unordered subset corresponds to $k!$ ordered ones.

> [!example] Example — Permutations of a Word
> LALALAAA: $\binom{8}{5} = 56$ arrangements (choose positions for the A's). STATISTICS: $\dfrac{10!}{3!\,3!\,2!} = 50{,}400$.

> [!example] Example — Full House in Poker
> $$P(\text{full house}) = \frac{13 \cdot \binom{4}{3} \cdot 12 \cdot \binom{4}{2}}{\binom{52}{5}} \approx 0.00144$$

> [!example] Example — Newton-Pepys Problem
> $P(\geq 1\text{ six in 6 dice}) = 1 - (5/6)^6 \approx 0.665$ is the *most* likely of the three Newton-Pepys scenarios — beating $\geq 2$ in 12 and $\geq 3$ in 18.

> [!example] Example — Bose-Einstein
> Placing $k$ indistinguishable particles into $n$ distinguishable boxes: $\binom{n+k-1}{k}$ (stars-and-bars encoding).

![Figure 1.6 — Bose-Einstein stars-and-bars encoding](chapter1_fig_1.6_bose_einstein_encoding.png)

> [!note] Binomial Theorem
> $$(x+y)^n = \sum_{k=0}^{n} \binom{n}{k} x^k y^{n-k}$$
> because there are $\binom{n}{k}$ ways to pick $x$ from $k$ of the $n$ factors and $y$ from the rest.

---

## 1.5 Story Proofs

A **story proof** proves an identity by *interpretation* — typically by counting the same thing two different ways. Often easier and more illuminating than algebra.

> [!example] Example — Choosing the Complement
> $$\binom{n}{k} = \binom{n}{n-k}$$
> *Story:* Choosing a $k$-committee from $n$ people is equivalent to choosing the $n-k$ people *not* on the committee.

> [!example] Example — Team Captain
> $$n \binom{n-1}{k-1} = k \binom{n}{k}$$
> *Story:* Both sides count $k$-person teams with a designated captain. Left: pick captain ($n$ ways), then $k-1$ teammates from the rest. Right: pick the team first ($\binom{n}{k}$), then promote one member to captain ($k$ ways).

> [!example] Example — Vandermonde's Identity
> $$\binom{m+n}{k} = \sum_{j=0}^{k} \binom{m}{j} \binom{n}{k-j}$$
> *Story:* Pick a $k$-committee from $m$ juniors and $n$ seniors. Partition by exactly how many juniors $j$ end up on the committee.

> [!example] Example — Partnerships
> $$\frac{(2n)!}{2^n \cdot n!} = (2n-1)(2n-3) \cdots 3 \cdot 1$$
> *Story:* Both sides count pairings of $2n$ people. Left: line them up $(2n)!$ ways and pair sequentially, then divide out the $n!$ pair orderings and $2^n$ within-pair orderings. Right: pick a partner for person 1 ($2n-1$ choices), then for the next unpaired person ($2n-3$), and so on.

---

## 1.6 Non-Naive Definition of Probability

To handle non-symmetric or infinite sample spaces, probability is defined axiomatically.

> [!definition] Definition — Probability Space
> A **probability space** is a sample space $S$ paired with a **probability function** $P$ that takes any event $A \subseteq S$ to a real number $P(A) \in [0, 1]$, satisfying:
> 1. $P(\emptyset) = 0$ and $P(S) = 1$
> 2. **Countable additivity:** for disjoint events $A_1, A_2, \ldots$,
> $$P\!\left(\bigcup_{j=1}^{\infty} A_j\right) = \sum_{j=1}^{\infty} P(A_j)$$

This accommodates unequal weights and infinite sample spaces. It's compatible with both the **frequentist** view (long-run frequency) and the **Bayesian** view (degree of belief) — any valid probability function must satisfy these axioms regardless of interpretation.

> [!definition] Theorem — Properties of Probability
> 1. **Complement rule:** $P(A^c) = 1 - P(A)$
> 2. **Monotonicity:** if $A \subseteq B$, then $P(A) \leq P(B)$
> 3. **Inclusion-exclusion (two events):** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$

The inclusion-exclusion formula generalizes to $n$ events:

$$P\!\left(\bigcup_{i=1}^{n} A_i\right) = \sum_{i} P(A_i) - \sum_{i<j} P(A_i \cap A_j) + \cdots + (-1)^{n+1} P(A_1 \cap \cdots \cap A_n)$$

> [!example] Example — de Montmort's Matching Problem (1708)
> Shuffle a deck of $n$ numbered cards. Flip them one by one, calling out $1, 2, \ldots, n$. You win if any flip's number ever matches the count.
>
> Let $A_i$ be the event of a match on the $i$th card. Symmetry collapses inclusion-exclusion to
> $$P(\text{win}) = 1 - \frac{1}{2!} + \frac{1}{3!} - \cdots + (-1)^{n+1} \frac{1}{n!}$$
> Comparing with the Taylor series for $e^{-1}$, this approaches $1 - 1/e \approx 0.632$ as $n \to \infty$ — strikingly **independent of deck size** for any reasonably large $n$.

---

## Key Takeaways

> [!success] The Big Three
> 1. **Probability is built on set theory.** Master unions, intersections, and complements first — every later concept assumes them.
> 2. **The naive definition is a special case, not the definition.** It works only when outcomes are genuinely equally likely (physical symmetry, designed sampling, or null models). Beware "binary outcomes therefore 50/50."
> 3. **Counting is the engine.** The multiplication rule, binomial coefficients, and adjusting for overcounting solve most naive probability problems. The complement rule and inclusion-exclusion are the two most powerful shortcuts.

> [!warning] The Recurring Warning
> Human intuition about probability is famously bad. Even Leibniz and Newton stumbled. The defenses are simulation, awareness of common pitfalls (the textbook's "biohazards"), and solving problems multiple ways as a sanity check.

---

## Exercises

> [!example] 1.9 Exercises — All 62 Solved & Verified
> The complete chapter-end exercise set, with NotebookLM-generated solutions independently verified by the main agent (zero discrepancies found).
>
> See the companion: **[Chapter 1 — Exercises (1.9)](chapter1_exercises.md)**

---

### Sources

| Source | Date | Type |
| --- | --- | --- |
| Blitzstein & Hwang, *Introduction to Probability* (Chapter 1) | 2019 | Textbook (PDF, NotebookLM-ingested) |
| NotebookLM (per-section sub-agent summaries + exercise solutions) | 2026-04-19 | AI synthesis (verified) |
| Main-agent independent verification of all 62 exercises | 2026-04-19 | Manual cross-check |
