# Chapter 1 — Exercises (1.9)

*Companion document to [Chapter 1 (Main)](<Chapter 1 (Main).md>)*

_All 62 chapter-end exercises with NotebookLM-generated solutions and main-agent verification._

---

> [!success] Verification Status: 62 / 62 ✓
> Every solution below was independently re-derived by the main agent and cross-checked against NotebookLM's response. **Zero discrepancies found.** When solutions reference closed-form expressions (like $\binom{61}{10}$), I worked the algebra; when they give a numerical decimal, I verified to within rounding. Exercises that the textbook leaves open-ended (e.g., asking the reader to "give an example") are noted as such.

---

## Counting (Exercises 1–14)

> [!example] Exercise 1 — MISSISSIPPI
> **Problem.** How many ways are there to permute the letters in the word MISSISSIPPI?
>
> > [!success]- Click to reveal solution
> > **Solution.** 11 letters with multiplicities M:1, I:4, S:4, P:2. Total distinct arrangements:
> > $$\frac{11!}{4!\,4!\,2!} = \frac{39{,}916{,}800}{1{,}152} = 34{,}650$$
> >
> > **Answer.** $34{,}650$ ✓

> [!example] Exercise 2 — Phone Numbers
> **Problem.** (a) How many 7-digit phone numbers if the first digit can't be 0 or 1? (b) Same as (a), but also can't start with 911.
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) First digit: 8 choices (2-9); remaining 6 digits: $10$ each. $8 \cdot 10^6 = 8{,}000{,}000$. (b) Subtract the $10^4 = 10{,}000$ numbers starting with "911".
> >
> > **Answer.** (a) $8{,}000{,}000$ — (b) $7{,}990{,}000$ ✓

> [!example] Exercise 3 — Fred's Dinners
> **Problem.** 5 nights, 10 restaurants. (a) No repeats. (b) Repeats allowed but not back-to-back.
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) $10 \cdot 9 \cdot 8 \cdot 7 \cdot 6 = 30{,}240$. (b) Monday: 10 choices; each later night: 9 (any but the previous). $10 \cdot 9^4 = 65{,}610$.
> >
> > **Answer.** (a) $30{,}240$ — (b) $65{,}610$ ✓

> [!example] Exercise 4 — Round-Robin Tournament
> **Problem.** $n$ players, each pair plays once. (a) Possible outcomes? (b) Total games?
>
> > [!success]- Click to reveal solution
> > **Solution.** (b) Each game = unordered pair: $\binom{n}{2}$. (a) Each game has 2 outcomes: $2^{\binom{n}{2}}$.
> >
> > **Answer.** (a) $2^{\binom{n}{2}}$ — (b) $\binom{n}{2}$ ✓

> [!example] Exercise 5 — Knock-Out Tournament
> **Problem.** $2^n$ players, single elimination. (a) Number of rounds? (b) Total games (by summing rounds)? (c) Total games (by reasoning about eliminations)?
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) After $k$ rounds, $2^{n-k}$ remain; ends when $2^{n-k}=1$, so $k=n$. (b) $\sum_{k=1}^{n} 2^{n-k} = 2^n - 1$. (c) Each game eliminates exactly one of $2^n - 1$ losers.
> >
> > **Answer.** (a) $n$ — (b) $2^n - 1$ — (c) $2^n - 1$ ✓

> [!example] Exercise 6 — Chess Pairings
> **Problem.** 20 players form 10 chess games where it matters who plays white. Count.
>
> > [!success]- Click to reveal solution
> > **Solution.** Choose 10 white players: $\binom{20}{10}$. Pair each white with one of the 10 blacks: $10!$. Total $= \binom{20}{10} \cdot 10! = \dfrac{20!}{10!}$.
> >
> > **Answer.** $\dfrac{20!}{10!}$ ✓

> [!example] Exercise 7 — 7-Game Chess Match
> **Problem.** A vs B over 7 games (W/D/L worth 1 / 0.5 / 0). (a) A ends with 3W, 2D, 2L. (b) A ends with 4 points (B with 3). (c) Best-of-7 lasts the full 7 with A winning 4-3.
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) Multinomial $\dfrac{7!}{3!\,2!\,2!} = 210$. (b) Solve $w + d + l = 7$, $w + d/2 = 4$ over nonneg integers: $(w,d,l) \in \{(1,6,0),(2,4,1),(3,2,2),(4,0,3)\}$ giving $7+105+210+35 = 357$. (c) From (b), exclude sequences ending in $L$ (otherwise A would have hit 4 by game 6 and the match would have ended): subtract $0+15+60+15 = 90$, leaving $267$.
> >
> > **Answer.** (a) $210$ — (b) $357$ — (c) $267$ ✓

> [!example] Exercise 8 — Splitting a Dozen
> **Problem.** Split 12 people into (a) one team of 2 and two teams of 5; (b) three teams of 4.
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) $\dfrac{\binom{12}{2}\binom{10}{5}}{2!} = \dfrac{66 \cdot 252}{2} = 8{,}316$ (the two 5-teams are indistinguishable). (b) $\dfrac{\binom{12}{4}\binom{8}{4}}{3!} = \dfrac{495 \cdot 70}{6} = 5{,}775$.
> >
> > **Answer.** (a) $8{,}316$ — (b) $5{,}775$ ✓

> [!example] Exercise 9 — Lattice Paths
> **Problem.** (a) Paths from $(0,0)$ to $(110,111)$ using only $\to$ and $\uparrow$ steps. (b) Same to $(210, 211)$ passing through $(110, 111)$.
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) 110 R's and 111 U's in some order: $\binom{221}{110}$. (b) Multiply leg counts: $\binom{221}{110} \cdot \binom{200}{100}$.
> >
> > **Answer.** (a) $\binom{221}{110}$ — (b) $\binom{221}{110}\binom{200}{100}$ ✓

> [!example] Exercise 10 — Course Selection
> **Problem.** Choose 7 of 20 courses with at least 1 statistics course (5 are stats). (a) Count. (b) Why isn't the answer $\binom{5}{1}\binom{19}{6}$?
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) Complement: $\binom{20}{7} - \binom{15}{7} = 77{,}520 - 6{,}435 = 71{,}085$. (b) That product fixes one stats course as "designated" first; a schedule containing $k$ stats courses is counted $k$ times.
> >
> > **Answer.** (a) $71{,}085$ — (b) overcounts schedules with $\geq 2$ stats courses ✓

> [!example] Exercise 11 — Counting Functions
> **Problem.** $|A| = n$, $|B| = m$. (a) Total functions $A \to B$? (b) One-to-one functions?
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) Each of $n$ inputs picks any of $m$ outputs: $m^n$. (b) First input has $m$ choices, second has $m-1$, ..., last has $m-n+1$: $\dfrac{m!}{(m-n)!}$ (= 0 if $n > m$).
> >
> > **Answer.** (a) $m^n$ — (b) $m(m-1)\cdots(m-n+1)$ ✓

> [!example] Exercise 12 — Bridge Hands
> **Problem.** 52-card deck dealt 13 each to A, B, C, D. (a) Possibilities for A's hand. (b) Total possibilities for all four hands. (c) Why isn't (b) the fourth power of (a)?
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) $\binom{52}{13}$. (b) $\binom{52}{13}\binom{39}{13}\binom{26}{13}\binom{13}{13} = \dfrac{52!}{(13!)^4}$. (c) The fourth-power formula would treat each hand as drawn independently *with* replacement (cards could repeat across hands); the actual deal is without replacement.
> >
> > **Answer.** (a) $\binom{52}{13}$ — (b) $\dfrac{52!}{(13!)^4}$ — (c) hands share a common deck ✓

> [!example] Exercise 13 — Casino Superdeck
> **Problem.** A "superdeck" of 10 standard decks (520 cards, 10 copies of each card type). How many 10-card unordered hands? (Hint: Bose-Einstein.)
>
> > [!success]- Click to reveal solution
> > **Solution.** Drawing only 10 cards, no card type can be exhausted (max needed = 10, copies available = 10). So this reduces to choosing a multiset of size 10 from 52 types: $\binom{52+10-1}{10} = \binom{61}{10}$.
> >
> > **Answer.** $\binom{61}{10}$ ✓

> [!example] Exercise 14 — Two Pizzas
> **Problem.** 4 sizes, 8 possible toppings (any subset, including empty). How many possibilities for two unordered pizzas?
>
> > [!success]- Click to reveal solution
> > **Solution.** Distinct single pizzas: $4 \cdot 2^8 = 1{,}024$. Two unordered pizzas with repetition: Bose-Einstein $\binom{1024+2-1}{2} = \binom{1025}{2} = 524{,}800$.
> >
> > **Answer.** $524{,}800$ ✓

---

## Story Proofs (Exercises 15–22)

> [!example] Exercise 15 — Sum of Binomial Coefficients
> **Identity.** $\sum_{k=0}^{n} \binom{n}{k} = 2^n$
>
> > [!success]- Click to reveal solution
> > **Story.** Both sides count subsets of an $n$-element set. Right: each element is in or out, giving $2^n$. Left: tally subsets by size $k$, with $\binom{n}{k}$ subsets of each size. ✓

> [!example] Exercise 16 — Pascal's Identity
> **Identity.** $\binom{n}{k} + \binom{n}{k-1} = \binom{n+1}{k}$
>
> > [!success]- Click to reveal solution
> > **Story.** Choose a $k$-committee from $n+1$ people. Distinguish one specific person ("Alice"). If Alice is on it: pick $k-1$ from the other $n$ → $\binom{n}{k-1}$. If Alice is off it: pick $k$ from the other $n$ → $\binom{n}{k}$. ✓ (Algebraic proof: combine over common denominator $(n-k+1)!\,k!$.)

> [!example] Exercise 17 — Sum of Squared Binomials (Vandermonde with $m=n$)
> **Identity.** $\sum_{k=0}^{n} \binom{n}{k}^2 = \binom{2n}{n}$
>
> > [!success]- Click to reveal solution
> > **Story.** Choose an $n$-person committee from $n$ juniors and $n$ seniors. Right: $\binom{2n}{n}$. Left: partition by exactly $k$ juniors on the committee — $\binom{n}{k}$ ways for juniors and $\binom{n}{n-k} = \binom{n}{k}$ for seniors. ✓

> [!example] Exercise 18 — Weighted Vandermonde
> **Identity.** $\sum_{k=1}^{n} k \binom{n}{k}^2 = n \binom{2n-1}{n-1}$
>
> > [!success]- Click to reveal solution
> > **Story.** Form an $n$-committee with chair from Group A (size $n$) drawn from a $2n$ pool (A + B, sizes $n$ each). Right: pick the chair from A ($n$), fill remaining $n-1$ from $2n-1$. Left: condition on $k$ A-members, $\binom{n}{k}\binom{n}{n-k} = \binom{n}{k}^2$ choices, then pick chair from the $k$ A-members. ✓

> [!example] Exercise 19 — 5-Subsets via Middle Element
> **Identity.** $\sum_{k=2}^{n} \binom{k}{2}\binom{n-k+2}{2} = \binom{n+3}{5}$
>
> > [!success]- Click to reveal solution
> > **Story.** Count 5-subsets of $\{1, \ldots, n+3\}$ by the middle (3rd-smallest) element $c = k+1$, ranging over $\{3, \ldots, n+1\}$. Below $c$: pick 2 of $k$ smaller values → $\binom{k}{2}$. Above $c$: pick 2 of $n+3-(k+1) = n-k+2$ larger values. ✓

> [!example] Exercise 20 — Hockey Stick & Gummi Bears
> **(a) Identity.** $\binom{k}{k} + \binom{k+1}{k} + \cdots + \binom{n}{k} = \binom{n+1}{k+1}$
>
> > [!success]- Click to reveal solution
> > **Story.** Line up $n+1$ people by age. Count $(k+1)$-subsets by age-rank $j+1$ of the oldest member ($j \in \{k, \ldots, n\}$): $\binom{j}{k}$ ways for the younger $k$. ✓
> >
> > **(b) Gummi bears.** Pack of 30-50 bears, 5 flavors. Compositions of size $N$: $\binom{N+4}{4}$ by stars-and-bars. Total $= \sum_{N=30}^{50} \binom{N+4}{4} = \sum_{j=34}^{54} \binom{j}{4} = \binom{55}{5} - \binom{34}{5}$ via hockey stick. ✓

> [!example] Exercise 21 — Stirling Numbers Recurrences
> **(a) Identity.** $\left\{{n+1 \atop k}\right\} = \left\{{n \atop k-1}\right\} + k\left\{{n \atop k}\right\}$
>
> > [!success]- Click to reveal solution
> > **Story.** Partition $n+1$ students into $k$ nonempty groups. Distinguish "me." If I'm alone: partition the other $n$ into $k-1$ groups. If not alone: partition the other $n$ into $k$ groups, then I join one of the $k$ groups. ✓
> >
> > **(b) Identity.** $\sum_{j=k}^{n} \binom{n}{j} \left\{{j \atop k}\right\} = \left\{{n+1 \atop k+1}\right\}$
> >
> > **Story.** Partition $n+1$ students into $k+1$ groups. Let $j$ = number of the other $n$ students NOT in my group ($j \in \{k, \ldots, n\}$). Pick those $j$ ($\binom{n}{j}$), partition them into $k$ groups ($\left\{{j \atop k}\right\}$), the rest join my group. ✓

> [!example] Exercise 22 — Sums of Powers
> **(a) Identity.** $1+2+\cdots+n = \binom{n+1}{2}$
>
> **Story (round-robin).** $n+1$ players, every pair plays once: $\binom{n+1}{2}$ total games. Counted sequentially: player 1 plays $n$, player 2 plays $n-1$ new opponents, ..., summing to $1 + 2 + \cdots + n$. ✓
>
> **(b) Identity.** $1^3 + 2^3 + \cdots + n^3 = 6\binom{n+1}{4} + 6\binom{n+1}{3} + \binom{n+1}{2}$
>
> > [!success]- Click to reveal solution
> > **Story.** Count 4-tuples $(x,y,z,w)$ with $w \in \{1, \ldots, n\}$ and $x,y,z \in \{0, \ldots, w-1\}$ (with replacement). Fixing $w = k$ gives $k^3$ tuples; sum gives $\sum k^3$. Alternatively, case on the number of distinct values among $\{x,y,z,w\}$ where $w$ is the strict max: 4 distinct → $6\binom{n+1}{4}$, 3 distinct → $6\binom{n+1}{3}$, 2 distinct → $\binom{n+1}{2}$. ✓

---

## Naive Definition of Probability (Exercises 23–42)

> [!example] Exercise 23 — Elevator
> **Problem.** 3 people in elevator, equally likely to want any of floors 2-10. $P$(buttons for 3 consecutive floors)?
>
> > [!success]- Click to reveal solution
> > **Solution.** $|S| = 9^3 = 729$. Favorable: 7 sets of 3 consecutive floors × $3! = 6$ orderings $= 42$. $P = 42/729 = 14/243$.
> >
> > **Answer.** $14/243$ ✓

> [!example] Exercise 24 — Eldest Girls
> **Problem.** 6 children (3 boys, 3 girls), all birth orders equally likely. $P$(3 eldest are the 3 girls)?
>
> > [!success]- Click to reveal solution
> > **Solution.** $\binom{6}{3} = 20$ equally likely gender sequences; only 1 has all girls first. $P = 1/20$.
> >
> > **Answer.** $1/20$ ✓

> [!example] Exercise 25 — 6 Robberies in 6 Districts
> **Problem.** $P$(some district has more than 1 robbery)?
>
> > [!success]- Click to reveal solution
> > **Solution.** Distinguishable robberies: $|S| = 6^6$. Complement (one each): $6! = 720$. $P = 1 - 720/46{,}656 = 319/324$.
> >
> > **Answer.** $319/324$ ✓

> [!example] Exercise 26 — Survey Sampling
> **Problem.** 1 million residents, sample 1000 with replacement. (a) Birthday-problem analog. (b) $P$(at least one repeat)?
>
> > [!success]- Click to reveal solution
> > **Solution.** (b) $1 - \dfrac{10^6 \cdot (10^6-1) \cdots (10^6-999)}{(10^6)^{1000}}$.
> >
> > **Answer.** Birthday problem with $n=10^6$, $k=1000$. ✓

> [!example] Exercise 27 — Hash Table Collisions
> **Problem.** $k$ items uniformly hashed into $n$ slots. $P$(at least one collision)?
>
> > [!success]- Click to reveal solution
> > **Solution.** $1 - \dfrac{n(n-1)\cdots(n-k+1)}{n^k}$ (= 1 if $k > n$).
> >
> > **Answer.** As above ✓

> [!example] Exercise 28 — 3 Stats Courses, 10 Slots
> **Problem.** $P$(at least 2 courses share a slot)?
>
> > [!success]- Click to reveal solution
> > **Solution.** Complement: $10 \cdot 9 \cdot 8 / 10^3 = 720/1000 = 0.72$. So $P = 0.28 = 7/25$.
> >
> > **Answer.** $7/25$ ✓

> [!example] Exercise 29 — Comparison Fills
> **Problem.** Fill in $<$, $>$, or $=$ comparing each pair of probabilities.
> **(a)** $P$(4 dice sum to 21) ___ $P$(4 dice sum to 22)
> **(b)** $P$(2-letter palindrome) ___ $P$(3-letter palindrome)
>
> > [!success]- Click to reveal solutions
> > **(a)** Sum 21: partitions $\{3,6,6,6\}, \{4,5,6,6\}, \{5,5,5,6\}$ giving $4 + 12 + 4 = 20$. Sum 22: $\{4,6,6,6\}, \{5,5,6,6\}$ giving $4 + 6 = 10$. **Answer: $>$**
> >
> > **(b)** $P$(2-letter palindrome) $= 26/26^2 = 1/26$. $P$(3-letter palindrome) $= 26^2/26^3 = 1/26$. **Answer: $=$** ✓

> [!example] Exercise 30 — n-letter Palindromes
> **Problem.** $P$(palindrome) for $n = 7$ and $n = 8$?
>
> > [!success]- Click to reveal solution
> > **Solution.** First $\lceil n/2 \rceil$ letters determine the rest. $n=7$: $26^4/26^7 = 1/26^3$. $n=8$: $26^4/26^8 = 1/26^4$.
> >
> > **Answer.** $1/26^3$ and $1/26^4$ ✓

> [!example] Exercise 31 — Capture-Recapture
> **Problem.** $N$ elk, $n$ tagged, then $m$ resampled. $P$(exactly $k$ tagged in resample)?
>
> > [!success]- Click to reveal solution
> > **Solution.** Hypergeometric: $\dfrac{\binom{n}{k}\binom{N-n}{m-k}}{\binom{N}{m}}$.
> >
> > **Answer.** As above ✓

> [!example] Exercise 32 — Card Guessing
> **Problem.** 4 cards (2R, 2B), guess 2 as red. $P$(exactly $j$ correct) for $j = 0, \ldots, 4$?
>
> > [!success]- Click to reveal solution
> > **Solution.** With $k$ true reds among the 2 guessed, total correct $= 2k$. So odd $j$ has prob 0. $P(j=0) = \binom{2}{0}\binom{2}{2}/\binom{4}{2} = 1/6$; $P(j=2) = \binom{2}{1}^2/\binom{4}{2} = 4/6 = 2/3$; $P(j=4) = 1/6$.
> >
> > **Answer.** $(1/6, 0, 2/3, 0, 1/6)$ ✓

> [!example] Exercise 33 — Two Sequential Draws
> **Problem.** Jar with $r$ red, $g$ green. (a) Why $P$(2nd green) = $P$(1st green)? (b) Formal proof. (c) If $r+g=16$ and $P$(same color) = $P$(diff color), find $r,g$.
>
> > [!success]- Click to reveal solution
> > **Solution.** (a)/(b) By labeling, every ball is equally likely to be the 2nd: $g/(r+g)$. (c) $r(r-1) + g(g-1) = 120$ with $r+g=16$ → $r^2 - 16r + 60 = 0$ → $(r,g) \in \{(6,10), (10,6)\}$.
> >
> > **Answer.** $g/(r+g)$; $(6,10)$ or $(10,6)$ ✓

> [!example] Exercise 34 — Poker
> **Problem.** (a) $P$(flush, excluding royal flush)? (b) $P$(two pair)?
>
> > [!success]- Click to reveal solution
> > **Solution.** Sample space $\binom{52}{5} = 2{,}598{,}960$. (a) $\dfrac{4(\binom{13}{5} - 1)}{\binom{52}{5}} = \dfrac{4 \cdot 1286}{2{,}598{,}960} \approx 0.00198$. (b) $\dfrac{\binom{13}{2}\binom{4}{2}^2 \cdot 44}{\binom{52}{5}} = \dfrac{78 \cdot 36 \cdot 44}{2{,}598{,}960} \approx 0.04754$.
> >
> > **Answer.** ≈ $0.00198$ and ≈ $0.04754$ ✓

> [!example] Exercise 35 — At Least 3 of Every Suit
> **Problem.** 13-card hand. $P$(all four suits have ≥ 3 cards)?
>
> > [!success]- Click to reveal solution
> > **Solution.** Only feasible distribution: 4-3-3-3. $\dfrac{4 \binom{13}{4} \binom{13}{3}^3}{\binom{52}{13}} \approx 0.105$.
> >
> > **Answer.** ≈ $0.105$ ✓

> [!example] Exercise 36 — 30 Dice
> **Problem.** $P$(each value 1-6 appears exactly 5 times)?
>
> > [!success]- Click to reveal solution
> > **Solution.** $\dfrac{30!/(5!)^6}{6^{30}}$.
> >
> > **Answer.** As above ✓

> [!example] Exercise 37 — First Ace
> **Problem.** Shuffled deck dealt until first ace. (a) $P$(no K, Q, or J before first ace). (b) $P$(exactly one of each before first ace).
>
> > [!success]- Click to reveal solution
> > **Solution.** By symmetry restrict to the 16 face-card+ace cards. (a) $P$(first is an ace) $= 4/16 = 1/4$. (b) $\dfrac{12}{16} \cdot \dfrac{8}{15} \cdot \dfrac{4}{14} \cdot \dfrac{4}{13} = 16/455$.
> >
> > **Answer.** (a) $1/4$ — (b) $16/455$ ✓

> [!example] Exercise 38 — Round Table
> **Problem.** 12 people randomly seated. $P$(Tyrion adjacent to Cersei)?
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) $\dfrac{12 \cdot 2 \cdot 10!}{12!} = \dfrac{2}{11}$. (b) Fix Tyrion; 2 of Cersei's 11 remaining seats are adjacent: $2/11$.
> >
> > **Answer.** $2/11$ ✓

> [!example] Exercise 39 — Couples Committee
> **Problem.** $n$ married couples (so $2n$ people), committee of size $k$. $P$(exactly $j$ couples on it)?
>
> > [!success]- Click to reveal solution
> > **Solution.** $\dfrac{\binom{n}{j} \binom{n-j}{k-2j} 2^{k-2j}}{\binom{2n}{k}}$.
> >
> > **Answer.** As above ✓

> [!example] Exercise 40 — Monotone Draws
> **Problem.** Draw $k$ from $n$ labeled balls with replacement. (a) $P$(strictly increasing)? (b) $P$(non-decreasing)?
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) $\binom{n}{k}/n^k$. (b) Stars-and-bars: $\binom{n+k-1}{k}/n^k$.
> >
> > **Answer.** As above ✓

> [!example] Exercise 41 — Exactly One Empty Box
> **Problem.** $n$ balls into $n$ boxes uniformly. $P$(exactly one box empty)?
>
> > [!success]- Click to reveal solution
> > **Solution.** Distribution must be one box with 2 balls, $n-2$ boxes with 1, one box empty. Count: $n \cdot \binom{n}{2} \cdot (n-1)! = \binom{n}{2} \cdot n!$. $P = \dfrac{\binom{n}{2} \cdot n!}{n^n}$.
> >
> > **Answer.** $\dfrac{\binom{n}{2} n!}{n^n}$ ✓

> [!example] Exercise 42 — Norepeatword Approaches $1/e$
> **Problem.** A "norepeatword" is a sequence of 1-26 distinct letters. Picked uniformly. Show $P$(uses all 26) $\approx 1/e$.
>
> > [!success]- Click to reveal solution
> > **Solution.** Total norepeatwords $= \sum_{k=1}^{26} \dfrac{26!}{(26-k)!}$. Favorable $= 26!$. Ratio $= \dfrac{1}{\sum_{j=0}^{25} 1/j!}$. Since $e = \sum_{j=0}^{\infty} 1/j!$ and the tail beyond $j=25$ is essentially 0, denominator $\approx e$, so $P \approx 1/e$.
> >
> > **Answer.** $\approx 1/e$ ✓

---

## Axioms of Probability (Exercises 43–48)

> [!example] Exercise 43 — Bonferroni-Style Bounds
> **Problem.** Show $P(A) + P(B) - 1 \leq P(A \cap B) \leq P(A \cup B) \leq P(A) + P(B)$. State equality conditions.
>
> > [!success]- Click to reveal solution
> > **Solution.** All three from inclusion-exclusion + non-negativity + monotonicity. Equalities: (1) iff $P(A \cup B) = 1$; (2) iff $P(A) = P(B) = P(A \cap B)$; (3) iff $A, B$ disjoint. ✓

> [!example] Exercise 44 — Set Difference
> **Problem.** If $A \subseteq B$, prove $P(B - A) = P(B) - P(A)$ from axioms.
>
> > [!success]- Click to reveal solution
> > **Solution.** $B = A \cup (B - A)$, disjoint. By countable additivity, $P(B) = P(A) + P(B - A)$. ✓

> [!example] Exercise 45 — Symmetric Difference
> **Problem.** Prove $P(A \Delta B) = P(A) + P(B) - 2P(A \cap B)$ from axioms.
>
> > [!success]- Click to reveal solution
> > **Solution.** $A \Delta B = (A \cap B^c) \sqcup (B \cap A^c)$. Since $A = (A \cap B) \sqcup (A \cap B^c)$, additivity gives $P(A \cap B^c) = P(A) - P(A \cap B)$. Symmetrically for $B$. Sum the two. ✓

> [!example] Exercise 46 — Exactly $k$ vs At Least $k$
> **Problem.** Let $B_k$ = "exactly $k$ of $A_1, \ldots, A_n$ occur," $C_k$ = "at least $k$ occur." Find $P(B_k)$ in terms of $P(C_k), P(C_{k+1})$.
>
> > [!success]- Click to reveal solution
> > **Solution.** $C_k = B_k \sqcup C_{k+1}$ (disjoint). So $P(B_k) = P(C_k) - P(C_{k+1})$. ✓

> [!example] Exercise 47 — Independence Properties
> **Problem.** $A, B$ independent means $P(A \cap B) = P(A)P(B)$. (a) Example with Pebble World. (b) Geometric in unit square. (c) Show $P(A \cup B) = 1 - P(A^c)P(B^c)$.
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) Two coin flips, $A$ = first H, $B$ = second H. (b) Independent iff $\text{Area}(A_1 \cap B_1) = \text{Area}(A_1) \cdot \text{Area}(B_1)$. (c) Inclusion-exclusion plus substitution: $P(A) + P(B) - P(A)P(B) = 1 - (1-P(A))(1-P(B)) = 1 - P(A^c)P(B^c)$. ✓

> [!example] Exercise 48 — Dutch Book on Arby
> **Problem.** Arby trades $1000$-redemption certificates at $1000 \cdot P_{\text{Arby}}$. Disjoint $A, B$ violate $P_{\text{Arby}}(A \cup B) = P_{\text{Arby}}(A) + P_{\text{Arby}}(B)$. Bankrupt Arby.
>
> > [!success]- Click to reveal solution
> > **Solution.** If $P(A \cup B) < P(A) + P(B)$: buy $A \cup B$ from Arby (cheap), sell $A$ and $B$ to Arby (expensive). Upfront profit $= 1000(P(A) + P(B) - P(A \cup B)) > 0$. Future payouts cancel because $A, B$ disjoint. Reverse direction is symmetric. ✓

---

## Inclusion-Exclusion (Exercises 49–55)

> [!example] Exercise 49 — Die Values Missing
> **Problem.** Fair die rolled $n$ times. $P$(at least one of the 6 values never appears)?
>
> > [!success]- Click to reveal solution
> > **Solution.** $A_i$ = value $i$ never appears. By I-E:
> > $$6\!\left(\frac{5}{6}\right)^n - 15\!\left(\frac{4}{6}\right)^n + 20\!\left(\frac{3}{6}\right)^n - 15\!\left(\frac{2}{6}\right)^n + 6\!\left(\frac{1}{6}\right)^n$$
> >
> > **Answer.** As above ✓

> [!example] Exercise 50 — Bridge Hand Void in a Suit
> **Problem.** 13-card hand. $P$(void in at least one suit)?
>
> > [!success]- Click to reveal solution
> > **Solution.** $\dfrac{4\binom{39}{13} - 6\binom{26}{13} + 4}{\binom{52}{13}}$ (the four-suit-void term is impossible).
> >
> > **Answer.** As above ✓

> [!example] Exercise 51 — All 4 Seasons in 7 Birthdays
> **Problem.** 7 people, equally likely seasons. $P$(all 4 seasons represented)?
>
> > [!success]- Click to reveal solution
> > **Solution.** Complement: $4(3/4)^7 - 6(2/4)^7 + 4(1/4)^7 - 0 = (8748 - 768 + 4)/16384 = 7984/16384$. So $P = 8400/16384 = 525/1024 \approx 0.5127$.
> >
> > **Answer.** $525/1024$ ✓

> [!example] Exercise 52 — Same Seat, 20 Students
> **Problem.** 20 students seat randomly Mon and Wed. $P$(no one in same seat both days)?
>
> > [!success]- Click to reveal solution
> > **Solution.** Derangement: $\sum_{k=0}^{20} (-1)^k/k! \approx 1/e \approx 0.368$.
> >
> > **Answer.** $\approx 1/e$ ✓

> [!example] Exercise 53 — 8-Char Password
> **Problem.** Password from 62 chars (26+26+10). Count passwords with: (a) ≥ 1 lowercase. (b) ≥ 1 lower AND ≥ 1 upper. (c) ≥ 1 of each type.
>
> > [!success]- Click to reveal solution
> > **Solution.** Total $62^8$. (a) $62^8 - 36^8$. (b) $62^8 - 2 \cdot 36^8 + 10^8$. (c) $62^8 - 52^8 - 2 \cdot 36^8 + 2 \cdot 26^8 + 10^8$.
> >
> > **Answer.** As above ✓

> [!example] Exercise 54 — Class Every Day
> **Problem.** Alice picks 7 of 30 classes (6/day, M-F). $P$(class every day)?
>
> > [!success]- Click to reveal solution
> > **Solution.** Complement via I-E: $P(\text{some day missing}) = [5\binom{24}{7} - 10\binom{18}{7} + 10\binom{12}{7}]/\binom{30}{7}$. So $P(\text{class every day}) = 114/377 \approx 0.302$.
> >
> > **Answer.** $114/377$ ✓

> [!example] Exercise 55 — Mixed Committee
> **Problem.** Club: 10 seniors, 12 juniors, 15 sophomores. Committee of 5. (a) $P$(exactly 3 sophomores). (b) $P$(at least one from each class).
>
> > [!success]- Click to reveal solution
> > **Solution.** Total $\binom{37}{5}$. (a) $\binom{15}{3}\binom{22}{2}/\binom{37}{5}$. (b) $1 - [\binom{27}{5} + \binom{25}{5} + \binom{22}{5} - \binom{15}{5} - \binom{12}{5} - \binom{10}{5}]/\binom{37}{5}$.
> >
> > **Answer.** As above ✓

---

## Mixed Practice (Exercises 56–62)

> [!example] Exercise 56 — Comparison Fills
> **Problem.** Fill in $<$, $>$, or $=$ comparing each pair of quantities.
> **(a)** $\binom{10}{5}$ ___ $\binom{10}{6}$
> **(b)** Number of ways to split 10 people into two teams of 5 ___ Number of ways to split 10 people into a team of 6 and a team of 4
> **(c)** $P$(all 3 people share Jan 1 birthday) ___ $P$(3 people each born on a different specific day among three given days)
> **(d)** $P$(Martin wins HH-vs-TH Penney's coin game) ___ $1/2$
>
> > [!success]- Click to reveal solutions
> > **(a)** $\binom{10}{5} = 252$ vs $\binom{10}{6} = 210$. **Answer: $>$**
> >
> > **(b)** Two teams of 5: $\binom{10}{5}/2 = 126$. Team of 6 and team of 4: $\binom{10}{4} = 210$. **Answer: $<$**
> >
> > **(c)** $P$(all on Jan 1) $= (1/365)^3$ vs $P$(one each on three specific days) $= 6 \cdot (1/365)^3$. **Answer: $<$**
> >
> > **(d)** Penney's coin game (HH vs TH): Martin (HH) wins only if first two flips are HH $= 1/4$, so $1/4 < 1/2$. **Answer: $<$** ✓

> [!example] Exercise 57 — Caesar's Last Breath
> **Problem.** $10^{22}$ molecules per breath, $10^{44}$ in atmosphere. $P$(at least one of your inhaled molecules was Caesar's)?
>
> > [!success]- Click to reveal solution
> > **Solution.** $1 - (1 - 10^{-22})^{10^{22}} \to 1 - e^{-1}$.
> >
> > **Answer.** $1 - e^{-1} \approx 0.632$ ✓

> [!example] Exercise 58 — Widget Inspector
> **Problem.** 12 widgets, 3 defective; test one by one. (a) $P$(test ≥ 9). (b) $P$(test ≥ 10).
>
> > [!success]- Click to reveal solution
> > **Solution.** Treat the 3 defective positions as uniformly distributed in 12 spots. (a) Complement: all 3 in first 8 = $\binom{8}{3}/\binom{12}{3} = 56/220$. So $P = 1 - 56/220 = 41/55$. (b) $1 - \binom{9}{3}/\binom{12}{3} = 1 - 84/220 = 34/55$.
> >
> > **Answer.** (a) $41/55$ — (b) $34/55$ ✓

> [!example] Exercise 59 — Chocolate Distributions
> **Problem.** 15 bars, 10 children. (a) Fungible bars. (b) Fungible, each child ≥ 1. (c) Distinguishable bars. (d) Distinguishable, each child ≥ 1.
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) Stars-and-bars: $\binom{24}{15}$. (b) Reserve 1 each, distribute 5: $\binom{14}{5}$. (c) Each bar 10 choices: $10^{15}$. (d) Inclusion-exclusion (surjection count): $\sum_{j=0}^{10} (-1)^j \binom{10}{j} (10-j)^{15}$.
> >
> > **Answer.** As above ✓

> [!example] Exercise 60 — Bootstrap Sampling
> **Problem.** Bootstrap sample of size $n$ from $n$ distinct values. (a) Ordered samples. (b) Unordered. (c) Ratio $p_1/p_2$ for most-/least-likely *unordered* samples; ratio of class probabilities.
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) $n^n$. (b) Stars-and-bars: $\binom{2n-1}{n}$. (c) Most likely (all distinct): $n!/n^n$. Least likely (all same): $1/n^n$. Ratio $p_1/p_2 = n!$. There's 1 "all distinct" class but $n$ "all same" classes (one per value), so class-probability ratio $= n!/n = (n-1)!$.
> >
> > **Answer.** (a) $n^n$ — (b) $\binom{2n-1}{n}$ — (c) $n!$ and $(n-1)!$ ✓

> [!example] Exercise 61 — Lost Boarding Pass
> **Problem.** 100 passengers; #1 picks a random seat; each later passenger takes their own seat if free, else random. $P$(#100 gets their own seat)?
>
> > [!success]- Click to reveal solution
> > **Solution.** Symmetry argument: at every step, seat 1 and seat 100 are treated identically by displaced passengers (neither is anyone's "own" seat for $j = 2, \ldots, 99$). The chain ends when seat 1 OR seat 100 is taken, each equally likely.
> >
> > **Answer.** $1/2$ ✓

> [!example] Exercise 62 — Non-Uniform Birthday
> **Problem.** Birthday distribution $p = (p_1, \ldots, p_{365})$, $k \geq 2$ people. (a) Express $P$(match) via elementary symmetric polynomial $e_k$. (b) Intuitive argument for uniform minimizing $P$(match). (c) Prove via AM-GM that pairwise averaging weakly increases $e_k$.
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) $P(\text{no match}) = k! \cdot e_k(p)$, so $P(\text{match}) = 1 - k! \cdot e_k(p)$. (b) Clumped distributions force collisions (extreme: $p_1 = 1$ gives $P = 1$). (c) Using $e_k(x_1, x_2, \ldots) = x_1 x_2 E_{k-2} + (x_1 + x_2)E_{k-1} + E_k$, only the $x_1 x_2$ term varies under averaging; $((p_1 + p_2)/2)^2 \geq p_1 p_2$ by AM-GM. Iterated smoothing converges to uniform.
> >
> > **Answer.** $P(\text{match}) = 1 - k! \cdot e_k(p)$, minimized at $p_j = 1/365$ ✓

---

## Related Documents

- **[Chapter 1 (Main)](<Chapter 1 (Main).md>)** — Hub note covering sections 1.1-1.6 with definitions, examples, and figures.
- **[Introduction to Probability (Main)](<../Introduction to Probability (Main).md>)** — Book-level hub.
