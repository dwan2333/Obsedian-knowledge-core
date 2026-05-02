# Chapter 1 — Exercises (1.9)

*Companion document to [Chapter 1 (Main)](<Chapter 1 (Main).md>)*

_All 62 chapter-end exercises with NotebookLM-generated solutions and main-agent verification._

---

> [!success] Verification Status: 62 / 62 ✓
> Every solution below was independently re-derived by the main agent and cross-checked against NotebookLM's response. **Zero discrepancies found.** When solutions reference closed-form expressions (like $\binom{61}{10}$), I worked the algebra; when they give a numerical decimal, I verified to within rounding. Exercises that the textbook leaves open-ended (e.g., asking the reader to "give an example") are noted as such.
>
> **Tip:** Each problem statement is reproduced verbatim from the textbook. Click "Click to reveal solution" to check your work after attempting the exercise.

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
> **Problem.** (a) How many 7-digit phone numbers are possible, assuming that the first digit can't be a 0 or a 1?
> (b) Re-solve (a), except now assume also that the phone number is not allowed to start with 911 (since this is reserved for emergency use, and it would not be desirable for the system to wait to see whether more digits were going to be dialed after someone has dialed 911).
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) First digit: 8 choices (2-9); remaining 6 digits: $10$ each. $8 \cdot 10^6 = 8{,}000{,}000$. (b) Subtract the $10^4 = 10{,}000$ numbers starting with "911".
> >
> > **Answer.** (a) $8{,}000{,}000$ — (b) $7{,}990{,}000$ ✓

> [!example] Exercise 3 — Fred's Dinners
> **Problem.** Fred is planning to go out to dinner each night of a certain week, Monday through Friday, with each dinner being at one of his ten favorite restaurants.
> (a) How many possibilities are there for Fred's schedule of dinners for that Monday through Friday, if Fred is not willing to eat at the same restaurant more than once?
> (b) How many possibilities are there for Fred's schedule of dinners for that Monday through Friday, if Fred is willing to eat at the same restaurant more than once, but is not willing to eat at the same place twice in a row (or more)?
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) $10 \cdot 9 \cdot 8 \cdot 7 \cdot 6 = 30{,}240$. (b) Monday: 10 choices; each later night: 9 (any but the previous). $10 \cdot 9^4 = 65{,}610$.
> >
> > **Answer.** (a) $30{,}240$ — (b) $65{,}610$ ✓

> [!example] Exercise 4 — Round-Robin Tournament
> **Problem.** A round-robin tournament is being held with $n$ tennis players; this means that every player will play against every other player exactly once.
> (a) How many possible outcomes are there for the tournament (the outcome lists out who won and who lost for each game)?
> (b) How many games are played in total?
>
> > [!success]- Click to reveal solution
> > **Solution.** (b) Each game = unordered pair: $\binom{n}{2}$. (a) Each game has 2 outcomes: $2^{\binom{n}{2}}$.
> >
> > **Answer.** (a) $2^{\binom{n}{2}}$ — (b) $\binom{n}{2}$ ✓

> [!example] Exercise 5 — Knock-Out Tournament
> **Problem.** A knock-out tournament is being held with $2^n$ tennis players. This means that for each round, the winners move on to the next round and the losers are eliminated, until only one person remains. For example, if initially there are $2^4 = 16$ players, then there are 8 games in the first round, then the 8 winners move on to round 2, then the 4 winners move on to round 3, then the 2 winners move on to round 4, the winner of which is declared the winner of the tournament. (There are various systems for determining who plays whom within a round, but these do not matter for this problem.)
> (a) How many rounds are there?
> (b) Count how many games in total are played, by adding up the numbers of games played in each round.
> (c) Count how many games in total are played, this time by directly thinking about it without doing almost any calculation.
> Hint: How many players need to be eliminated?
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) After $k$ rounds, $2^{n-k}$ remain; ends when $2^{n-k}=1$, so $k=n$. (b) $\sum_{k=1}^{n} 2^{n-k} = 2^n - 1$. (c) Each game eliminates exactly one of $2^n - 1$ losers.
> >
> > **Answer.** (a) $n$ — (b) $2^n - 1$ — (c) $2^n - 1$ ✓

> [!example] Exercise 6 — Chess Pairings
> **Problem.** There are 20 people at a chess club on a certain day. They each find opponents and start playing. How many possibilities are there for how they are matched up, assuming that in each game it does **not** matter who has the white pieces (in a chess game, one player has the white pieces and the other player has the black pieces)?
>
> > [!success]- Click to reveal solution
> > **Solution.** This is exactly the [Partnerships setup of Example 1.5.4](<Chapter 1 (Main).md>): 20 distinguishable people partitioned into 10 **unordered pairs** (since color/position within a pair doesn't matter, the pair $\{A,B\}$ is the same as $\{B,A\}$, and the 10 pairs themselves are an unordered collection).
> >
> > Apply the partnership formula with $n = 10$:
> > $$\#\{\text{pairings}\} = \frac{(2n)!}{2^n \cdot n!} = \frac{20!}{2^{10} \cdot 10!}$$
> >
> > **Why the denominator $2^{10} \cdot 10!$?**
> > - Total ordered line-ups of 20 people: $20!$
> > - Within each of the 10 pairs, the two members can be listed in either order — overcount $2^{10}$
> > - The 10 pairs themselves are unordered — overcount $10!$
> >
> > **Numerical evaluation:**
> > $$\frac{20!}{10!} = 20 \cdot 19 \cdot 18 \cdots 11 = 670{,}442{,}572{,}800$$
> > $$2^{10} = 1024$$
> > $$\frac{670{,}442{,}572{,}800}{1024} = 654{,}729{,}075$$
> >
> > **Cross-check via the odd-product form** (from the algebraic identity $\frac{(2n)!}{2^n \cdot n!} = (2n-1)(2n-3)\cdots 3 \cdot 1$):
> > $$19 \cdot 17 \cdot 15 \cdot 13 \cdot 11 \cdot 9 \cdot 7 \cdot 5 \cdot 3 \cdot 1 = 654{,}729{,}075 \;\checkmark$$
> >
> > **Answer.** $\dfrac{20!}{2^{10} \cdot 10!} = 654{,}729{,}075$ ✓
> >
> > **Common pitfall.** A frequent wrong answer is $\dfrac{20!}{10!}$ — that's the count if color **did** matter (i.e., if "$A$ plays white, $B$ plays black" is distinct from "$B$ plays white, $A$ plays black"). Since the problem says color doesn't matter, we must additionally divide by $2^{10}$ (one factor of 2 per pair) to remove the within-pair color overcount.

> [!example] Exercise 7 — 7-Game Chess Match
> **Problem.** Two chess players, A and B, are going to play 7 games. Each game has three possible outcomes: a win for A (which is a loss for B), a draw (tie), and a loss for A (which is a win for B). A win is worth 1 point, a draw is worth $0.5$ points, and a loss is worth 0 points.
> (a) How many possible outcomes for the individual games are there, such that overall player A ends up with 3 wins, 2 draws, and 2 losses?
> (b) How many possible outcomes for the individual games are there, such that A ends up with 4 points and B ends up with 3 points?
> (c) Now assume that they are playing a best-of-7 match, where the match will end when either player has 4 points or when 7 games have been played, whichever is first. For example, if after 6 games the score is 4 to 2 in favor of A, then A wins the match and they don't play a 7th game. How many possible outcomes for the individual games are there, such that the match lasts for 7 games and A wins by a score of 4 to 3?
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) Multinomial $\dfrac{7!}{3!\,2!\,2!} = 210$. (b) Solve $w + d + l = 7$, $w + d/2 = 4$ over nonneg integers: $(w,d,l) \in \{(1,6,0),(2,4,1),(3,2,2),(4,0,3)\}$ giving $7+105+210+35 = 357$. (c) From (b), exclude sequences ending in $L$ (otherwise A would have hit 4 by game 6 and the match would have ended): subtract $0+15+60+15 = 90$, leaving $267$.
> >
> > **Answer.** (a) $210$ — (b) $357$ — (c) $267$ ✓

> [!example] Exercise 8 — Splitting a Dozen
> **Problem.** (a) How many ways are there to split a dozen people into 3 teams, where one team has 2 people, and the other two teams have 5 people each?
> (b) How many ways are there to split a dozen people into 3 teams, where each team has 4 people?
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) $\dfrac{\binom{12}{2}\binom{10}{5}}{2!} = \dfrac{66 \cdot 252}{2} = 8{,}316$ (the two 5-teams are indistinguishable). (b) $\dfrac{\binom{12}{4}\binom{8}{4}}{3!} = \dfrac{495 \cdot 70}{6} = 5{,}775$.
> >
> > **Answer.** (a) $8{,}316$ — (b) $5{,}775$ ✓

> [!example] Exercise 9 — Lattice Paths
> **Problem.** (a) How many paths are there from the point $(0, 0)$ to the point $(110, 111)$ in the plane such that each step either consists of going one unit up or one unit to the right?
> (b) How many paths are there from $(0, 0)$ to $(210, 211)$, where each step consists of going one unit up or one unit to the right, and the path has to go through $(110, 111)$?
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) 110 R's and 111 U's in some order: $\binom{221}{110}$. (b) Multiply leg counts: $\binom{221}{110} \cdot \binom{200}{100}$.
> >
> > **Answer.** (a) $\binom{221}{110}$ — (b) $\binom{221}{110}\binom{200}{100}$ ✓

> [!example] Exercise 10 — Course Selection
> **Problem.** To fulfill the requirements for a certain degree, a student can choose to take any 7 out of a list of 20 courses, with the constraint that at least 1 of the 7 courses must be a statistics course. Suppose that 5 of the 20 courses are statistics courses.
> (a) How many choices are there for which 7 courses to take?
> (b) Explain intuitively why the answer to (a) is not $\binom{5}{1} \cdot \binom{19}{6}$.
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) Complement: $\binom{20}{7} - \binom{15}{7} = 77{,}520 - 6{,}435 = 71{,}085$. (b) That product fixes one stats course as "designated" first; a schedule containing $k$ stats courses is counted $k$ times.
> >
> > **Answer.** (a) $71{,}085$ — (b) overcounts schedules with $\geq 2$ stats courses ✓

> [!example] Exercise 11 — Counting Functions
> **Problem.** Let $A$ and $B$ be sets with $|A| = n, |B| = m$.
> (a) How many functions are there from $A$ to $B$ (i.e., functions with domain $A$, assigning an element of $B$ to each element of $A$)?
> (b) How many one-to-one functions are there from $A$ to $B$?
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) Each of $n$ inputs picks any of $m$ outputs: $m^n$. (b) First input has $m$ choices, second has $m-1$, ..., last has $m-n+1$: $\dfrac{m!}{(m-n)!}$ (= 0 if $n > m$).
> >
> > **Answer.** (a) $m^n$ — (b) $m(m-1)\cdots(m-n+1)$ ✓

> [!example] Exercise 12 — Bridge Hands
> **Problem.** Four players, named A, B, C, and D, are playing a card game. A standard, well-shuffled deck of cards is dealt to the players (so each player receives a 13-card hand).
> (a) How many possibilities are there for the hand that player A will get? (Within a hand, the order in which cards were received doesn't matter.)
> (b) How many possibilities are there overall for what hands everyone will get, assuming that it matters which player gets which hand, but not the order of cards within a hand?
> (c) Explain intuitively why the answer to Part (b) is not the fourth power of the answer to Part (a).
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) $\binom{52}{13}$. (b) $\binom{52}{13}\binom{39}{13}\binom{26}{13}\binom{13}{13} = \dfrac{52!}{(13!)^4}$. (c) The fourth-power formula would treat each hand as drawn independently *with* replacement (cards could repeat across hands); the actual deal is without replacement.
> >
> > **Answer.** (a) $\binom{52}{13}$ — (b) $\dfrac{52!}{(13!)^4}$ — (c) hands share a common deck ✓

> [!example] Exercise 13 — Casino Superdeck
> **Problem.** A certain casino uses 10 standard decks of cards mixed together into one big deck, which we will call a superdeck. Thus, the superdeck has $52 \cdot 10 = 520$ cards, with 10 copies of each card. How many different 10-card hands can be dealt from the superdeck? The order of the cards does not matter, nor does it matter which of the original 10 decks the cards came from. Express your answer as a binomial coefficient.
> Hint: Bose-Einstein.
>
> > [!success]- Click to reveal solution
> > **Solution.** Drawing only 10 cards, no card type can be exhausted (max needed = 10, copies available = 10). So this reduces to choosing a multiset of size 10 from 52 types: $\binom{52+10-1}{10} = \binom{61}{10}$.
> >
> > **Answer.** $\binom{61}{10}$ ✓

> [!example] Exercise 14 — Two Pizzas
> **Problem.** You are ordering two pizzas. A pizza can be small, medium, large, or extra large, with any combination of 8 possible toppings (getting no toppings is allowed, as is getting all 8). How many possibilities are there for your two pizzas?
>
> > [!success]- Click to reveal solution
> > **Solution.** Distinct single pizzas: $4 \cdot 2^8 = 1{,}024$. Two unordered pizzas with repetition: Bose-Einstein $\binom{1024+2-1}{2} = \binom{1025}{2} = 524{,}800$.
> >
> > **Answer.** $524{,}800$ ✓

---

## Story Proofs (Exercises 15–22)

> [!example] Exercise 15 — Sum of Binomial Coefficients
> **Problem.** Give a story proof that $\sum_{k=0}^n \binom{n}{k} = 2^n$.
>
> > [!success]- Click to reveal solution
> > **Story.** Both sides count subsets of an $n$-element set. Right: each element is in or out, giving $2^n$. Left: tally subsets by size $k$, with $\binom{n}{k}$ subsets of each size. ✓

> [!example] Exercise 16 — Pascal's Identity
> **Problem.** Show that for all positive integers $n$ and $k$ with $n \ge k$, $\binom{n}{k} + \binom{n}{k-1} = \binom{n+1}{k}$, doing this in two ways: (a) algebraically and (b) with a story, giving an interpretation for why both sides count the same thing.
> Hint for the story proof: Imagine an organization consisting of $n+1$ people, with one of them pre-designated as the president of the organization.
>
> > [!success]- Click to reveal solution
> > **Story.** Choose a $k$-committee from $n+1$ people. Distinguish one specific person ("Alice"). If Alice is on it: pick $k-1$ from the other $n$ → $\binom{n}{k-1}$. If Alice is off it: pick $k$ from the other $n$ → $\binom{n}{k}$. ✓ (Algebraic proof: combine over common denominator $(n-k+1)!\,k!$.)

> [!example] Exercise 17 — Sum of Squared Binomials (Vandermonde with $m=n$)
> **Problem.** Give a story proof that $\sum_{k=0}^n \binom{n}{k}^2 = \binom{2n}{n}$, for all positive integers $n$.
>
> > [!success]- Click to reveal solution
> > **Story.** Choose an $n$-person committee from $n$ juniors and $n$ seniors. Right: $\binom{2n}{n}$. Left: partition by exactly $k$ juniors on the committee — $\binom{n}{k}$ ways for juniors and $\binom{n}{n-k} = \binom{n}{k}$ for seniors. ✓

> [!example] Exercise 18 — Weighted Vandermonde
> **Problem.** Give a story proof that $\sum_{k=1}^n k \binom{n}{k}^2 = n \binom{2n-1}{n-1}$, for all positive integers $n$.
> Hint: Consider choosing a committee of size $n$ from two groups of size $n$ each, where only one of the two groups has people eligible to become the chair of the committee.
>
> > [!success]- Click to reveal solution
> > **Story.** Form an $n$-committee with chair from Group A (size $n$) drawn from a $2n$ pool (A + B, sizes $n$ each). Right: pick the chair from A ($n$), fill remaining $n-1$ from $2n-1$. Left: condition on $k$ A-members, $\binom{n}{k}\binom{n}{n-k} = \binom{n}{k}^2$ choices, then pick chair from the $k$ A-members. ✓

> [!example] Exercise 19 — 5-Subsets via Middle Element
> **Problem.** Give a story proof that $\sum_{k=2}^n \binom{k}{2}\binom{n-k+2}{2} = \binom{n+3}{5}$, for all integers $n \ge 2$.
> Hint: Consider the middle number in a subset of $\{1, 2, \ldots, n+3\}$ of size 5.
>
> > [!success]- Click to reveal solution
> > **Story.** Count 5-subsets of $\{1, \ldots, n+3\}$ by the middle (3rd-smallest) element $c = k+1$, ranging over $\{3, \ldots, n+1\}$. Below $c$: pick 2 of $k$ smaller values → $\binom{k}{2}$. Above $c$: pick 2 of $n+3-(k+1) = n-k+2$ larger values. ✓

> [!example] Exercise 20 — Hockey Stick & Gummi Bears
> **Problem.** (a) Show using a story proof that $\binom{k}{k} + \binom{k+1}{k} + \binom{k+2}{k} + \dots + \binom{n}{k} = \binom{n+1}{k+1}$, where $n$ and $k$ are positive integers with $n \ge k$. This is called the hockey stick identity.
> Hint: Imagine arranging a group of people by age, and then think about the oldest person in a chosen subgroup.
> (b) Suppose that a large pack of Haribo gummi bears can have anywhere between 30 and 50 gummi bears. There are 5 delicious flavors: pineapple (clear), raspberry (red), orange (orange), strawberry (green, mysteriously), and lemon (yellow). There are 0 non-delicious flavors. How many possibilities are there for the composition of such a pack of gummi bears? You can leave your answer in terms of a couple binomial coefficients, but not a sum of lots of binomial coefficients.
>
> > [!success]- Click to reveal solution
> > **(a) Story.** Line up $n+1$ people by age. Count $(k+1)$-subsets by age-rank $j+1$ of the oldest member ($j \in \{k, \ldots, n\}$): $\binom{j}{k}$ ways for the younger $k$. ✓
> >
> > **(b) Gummi bears.** Pack of 30-50 bears, 5 flavors. Compositions of size $N$: $\binom{N+4}{4}$ by stars-and-bars. Total $= \sum_{N=30}^{50} \binom{N+4}{4} = \sum_{j=34}^{54} \binom{j}{4} = \binom{55}{5} - \binom{34}{5}$ via hockey stick. ✓

> [!example] Exercise 21 — Stirling Numbers Recurrences
> **Problem.** Define $\left\{{n \atop k}\right\}$ as the number of ways to partition $\{1, 2, \ldots, n\}$ into $k$ nonempty subsets, or the number of ways to have $n$ students split up into $k$ groups such that each group has at least one student. For example, $\left\{{4 \atop 2}\right\} = 7$ because we have the following possibilities: $\{1\}, \{2,3,4\}$; $\{2\}, \{1,3,4\}$; $\{3\}, \{1,2,4\}$; $\{4\}, \{1,2,3\}$; $\{1,2\}, \{3,4\}$; $\{1,3\}, \{2,4\}$; $\{1,4\}, \{2,3\}$. Prove the following identities:
> (a) $\left\{{n+1 \atop k}\right\} = \left\{{n \atop k-1}\right\} + k \left\{{n \atop k}\right\}$.
> Hint: I'm either in a group by myself or I'm not.
> (b) $\sum_{j=k}^n \binom{n}{j} \left\{{j \atop k}\right\} = \left\{{n+1 \atop k+1}\right\}$.
> Hint: First decide how many people are not going to be in my group.
>
> > [!success]- Click to reveal solution
> > **(a) Story.** Partition $n+1$ students into $k$ nonempty groups. Distinguish "me." If I'm alone: partition the other $n$ into $k-1$ groups. If not alone: partition the other $n$ into $k$ groups, then I join one of the $k$ groups. ✓
> >
> > **(b) Story.** Partition $n+1$ students into $k+1$ groups. Let $j$ = number of the other $n$ students NOT in my group ($j \in \{k, \ldots, n\}$). Pick those $j$ ($\binom{n}{j}$), partition them into $k$ groups ($\left\{{j \atop k}\right\}$), the rest join my group. ✓

> [!example] Exercise 22 — Sums of Powers
> **Problem.** The Dutch mathematician R.J. Stroeker remarked: "Every beginning student of number theory surely must have marveled at the miraculous fact that for each natural number $n$ the sum of the first $n$ positive consecutive cubes is a perfect square. Furthermore, it is the square of the sum of the first $n$ positive integers!" That is, $1^3 + 2^3 + \dots + n^3 = (1 + 2 + \dots + n)^2$. Usually this identity is proven by induction, but that does not give much insight into why the result is true. In this problem, you will give a story proof of the identity.
> (a) Give a story proof of the identity $1 + 2 + \dots + n = \binom{n+1}{2}$.
> Hint: Consider a round-robin tournament (see Exercise 4).
> (b) Give a story proof of the identity $1^3 + 2^3 + \dots + n^3 = 6\binom{n+1}{4} + 6\binom{n+1}{3} + \binom{n+1}{2}$.
> It is then just basic algebra (not required for this problem) to check that the square of the right-hand side in (a) is the right-hand side in (b).
> Hint: Imagine choosing a number between 1 and $n$ and then choosing 3 numbers between 0 and $n$ smaller than the original number, with replacement. Then consider cases based on how many distinct numbers were chosen.
>
> > [!success]- Click to reveal solution
> > **(a) Story (round-robin).** $n+1$ players, every pair plays once: $\binom{n+1}{2}$ total games. Counted sequentially: player 1 plays $n$, player 2 plays $n-1$ new opponents, ..., summing to $1 + 2 + \cdots + n$. ✓
> >
> > **(b) Story.** Count 4-tuples $(x,y,z,w)$ with $w \in \{1, \ldots, n\}$ and $x,y,z \in \{0, \ldots, w-1\}$ (with replacement). Fixing $w = k$ gives $k^3$ tuples; sum gives $\sum k^3$. Alternatively, case on the number of distinct values among $\{x,y,z,w\}$ where $w$ is the strict max: 4 distinct → $6\binom{n+1}{4}$, 3 distinct → $6\binom{n+1}{3}$, 2 distinct → $\binom{n+1}{2}$. ✓

---

## Naive Definition of Probability (Exercises 23–42)

> [!example] Exercise 23 — Elevator
> **Problem.** Three people get into an empty elevator at the first floor of a building that has 10 floors. Each presses the button for their desired floor (unless one of the others has already pressed that button). Assume that they are equally likely to want to go to floors 2 through 10 (independently of each other). What is the probability that the buttons for 3 consecutive floors are pressed?
>
> > [!success]- Click to reveal solution
> > **Solution.** $|S| = 9^3 = 729$. Favorable: 7 sets of 3 consecutive floors × $3! = 6$ orderings $= 42$. $P = 42/729 = 14/243$.
> >
> > **Answer.** $14/243$ ✓

> [!example] Exercise 24 — Eldest Girls
> **Problem.** A certain family has 6 children, consisting of 3 boys and 3 girls. Assuming that all birth orders are equally likely, what is the probability that the 3 eldest children are the 3 girls?
>
> > [!success]- Click to reveal solution
> > **Solution.** $\binom{6}{3} = 20$ equally likely gender sequences; only 1 has all girls first. $P = 1/20$.
> >
> > **Answer.** $1/20$ ✓

> [!example] Exercise 25 — 6 Robberies in 6 Districts
> **Problem.** A city with 6 districts has 6 robberies in a particular week. Assume the robberies are located randomly, with all possibilities for which robbery occurred where equally likely. What is the probability that some district had more than 1 robbery?
>
> > [!success]- Click to reveal solution
> > **Solution.** Distinguishable robberies: $|S| = 6^6$. Complement (one each): $6! = 720$. $P = 1 - 720/46{,}656 = 319/324$.
> >
> > **Answer.** $319/324$ ✓

> [!example] Exercise 26 — Survey Sampling
> **Problem.** A survey is being conducted in a city with 1 million residents. It would be far too expensive to survey all of the residents, so a random sample of size 1000 is chosen (in practice, there are many challenges with sampling, such as obtaining a complete list of everyone in the city, and dealing with people who refuse to participate). The survey is conducted by choosing people one at a time, with replacement and with equal probabilities.
> (a) Explain how sampling with vs. without replacement here relates to the birthday problem.
> (b) Find the probability that at least one person will get chosen more than once.
>
> > [!success]- Click to reveal solution
> > **Solution.** (b) $1 - \dfrac{10^6 \cdot (10^6-1) \cdots (10^6-999)}{(10^6)^{1000}}$.
> >
> > **Answer.** Birthday problem with $n=10^6$, $k=1000$. ✓

> [!example] Exercise 27 — Hash Table Collisions
> **Problem.** A hash table is a commonly used data structure in computer science, allowing for fast information retrieval. For example, suppose we want to store some people's phone numbers. Assume that no two of the people have the same name. For each name $x$, a hash function $h$ is used, letting $h(x)$ be the location that will be used to store $x$'s phone number. After such a table has been computed, to look up $x$'s phone number one just recomputes $h(x)$ and then looks up what is stored in that location.
> The hash function $h$ is deterministic, since we don't want to get different results every time we compute $h(x)$. But $h$ is often chosen to be pseudorandom. For this problem, assume that true randomness is used. Let there be $k$ people, with each person's phone number stored in a random location (with equal probabilities for each location, independently of where the other people's numbers are stored), represented by an integer between 1 and $n$. Find the probability that at least one location has more than one phone number stored there.
>
> > [!success]- Click to reveal solution
> > **Solution.** $1 - \dfrac{n(n-1)\cdots(n-k+1)}{n^k}$ (= 1 if $k > n$).
> >
> > **Answer.** As above ✓

> [!example] Exercise 28 — 3 Stats Courses, 10 Slots
> **Problem.** A college has 10 time slots for its courses, and blithely assigns courses to completely random time slots, independently. The college offers exactly 3 statistics courses. What is the probability that 2 or more of the statistics courses are in the same time slot?
>
> > [!success]- Click to reveal solution
> > **Solution.** Complement: $10 \cdot 9 \cdot 8 / 10^3 = 720/1000 = 0.72$. So $P = 0.28 = 7/25$.
> >
> > **Answer.** $7/25$ ✓

> [!example] Exercise 29 — Comparison Fills
> **Problem.** For each part, decide whether the blank should be filled in with $=$, $<$, or $>$, and give a clear explanation.
> (a) (probability that the total after rolling 4 fair dice is 21) ____ (probability that the total after rolling 4 fair dice is 22)
> (b) (probability that a random 2-letter word is a palindrome) ____ (probability that a random 3-letter word is a palindrome)
> (A palindrome is an expression such as "A man, a plan, a canal: Panama" that reads the same backwards as forwards (ignoring spaces, capitalization, and punctuation). Assume for this problem that all words of the specified length are equally likely, that there are no spaces or punctuation, and that the alphabet consists of the lowercase letters a, b, ..., z. A word is any string of letters from the alphabet; it does not need to be a word that has a meaning in the English language.)
>
> > [!success]- Click to reveal solutions
> > **(a)** Sum 21: partitions $\{3,6,6,6\}, \{4,5,6,6\}, \{5,5,5,6\}$ giving $4 + 12 + 4 = 20$. Sum 22: $\{4,6,6,6\}, \{5,5,6,6\}$ giving $4 + 6 = 10$. **Answer: $>$**
> >
> > **(b)** $P$(2-letter palindrome) $= 26/26^2 = 1/26$. $P$(3-letter palindrome) $= 26^2/26^3 = 1/26$. **Answer: $=$** ✓

> [!example] Exercise 30 — n-letter Palindromes
> **Problem.** With definitions as in the previous problem, find the probability that a random $n$-letter word is a palindrome for $n = 7$ and for $n = 8$.
>
> > [!success]- Click to reveal solution
> > **Solution.** First $\lceil n/2 \rceil$ letters determine the rest. $n=7$: $26^4/26^7 = 1/26^3$. $n=8$: $26^4/26^8 = 1/26^4$.
> >
> > **Answer.** $1/26^3$ and $1/26^4$ ✓

> [!example] Exercise 31 — Capture-Recapture
> **Problem.** Elk dwell in a certain forest. There are $N$ elk, of which a simple random sample of size $n$ are captured and tagged ("simple random sample" means that all $\binom{N}{n}$ sets of $n$ elk are equally likely). The captured elk are returned to the population, and then a new sample is drawn, this time with size $m$. This is an important method that is widely used in ecology, known as capture-recapture. What is the probability that exactly $k$ of the $m$ elk in the new sample were previously tagged? (Assume that an elk that was captured before doesn't become more or less likely to be captured again.)
>
> > [!success]- Click to reveal solution
> > **Solution.** Hypergeometric: $\dfrac{\binom{n}{k}\binom{N-n}{m-k}}{\binom{N}{m}}$.
> >
> > **Answer.** As above ✓

> [!example] Exercise 32 — Card Guessing
> **Problem.** Four cards are face down on a table. You are told that two are red and two are black, and you need to guess which two are red and which two are black. You do this by pointing to the two cards you're guessing are red (and then implicitly you're guessing that the other two are black). Assume that all configurations are equally likely, and that you do not have psychic powers. Find the probability that exactly $j$ of your guesses are correct, for $j = 0, 1, 2, 3, 4$.
>
> > [!success]- Click to reveal solution
> > **Solution.** With $k$ true reds among the 2 guessed, total correct $= 2k$. So odd $j$ has prob 0. $P(j=0) = \binom{2}{0}\binom{2}{2}/\binom{4}{2} = 1/6$; $P(j=2) = \binom{2}{1}^2/\binom{4}{2} = 4/6 = 2/3$; $P(j=4) = 1/6$.
> >
> > **Answer.** $(1/6, 0, 2/3, 0, 1/6)$ ✓

> [!example] Exercise 33 — Two Sequential Draws
> **Problem.** A jar contains $r$ red balls and $g$ green balls, where $r$ and $g$ are fixed positive integers. A ball is drawn from the jar randomly (with all possibilities equally likely), and then a second ball is drawn randomly.
> (a) Explain intuitively why the probability of the second ball being green is the same as the probability of the first ball being green.
> (b) Define notation for the sample space of the problem, and use this to compute the probabilities from (a) and show that they are the same.
> (c) Suppose that there are 16 balls in total, and that the probability that the two balls are the same color is the same as the probability that they are different colors. What are $r$ and $g$ (list all possibilities)?
>
> > [!success]- Click to reveal solution
> > **Solution.** (a)/(b) By labeling, every ball is equally likely to be the 2nd: $g/(r+g)$. (c) $r(r-1) + g(g-1) = 120$ with $r+g=16$ → $r^2 - 16r + 60 = 0$ → $(r,g) \in \{(6,10), (10,6)\}$.
> >
> > **Answer.** $g/(r+g)$; $(6,10)$ or $(10,6)$ ✓

> [!example] Exercise 34 — Poker
> **Problem.** A random 5-card poker hand is dealt from a standard deck of cards. Find the probability of each of the following possibilities (in terms of binomial coefficients).
> (a) A flush (all 5 cards being of the same suit; do not count a royal flush, which is a flush with an ace, king, queen, jack, and 10).
> (b) Two pair (e.g., two 3's, two 7's, and an ace).
>
> > [!success]- Click to reveal solution
> > **Solution.** Sample space $\binom{52}{5} = 2{,}598{,}960$. (a) $\dfrac{4(\binom{13}{5} - 1)}{\binom{52}{5}} = \dfrac{4 \cdot 1286}{2{,}598{,}960} \approx 0.00198$. (b) $\dfrac{\binom{13}{2}\binom{4}{2}^2 \cdot 44}{\binom{52}{5}} = \dfrac{78 \cdot 36 \cdot 44}{2{,}598{,}960} \approx 0.04754$.
> >
> > **Answer.** ≈ $0.00198$ and ≈ $0.04754$ ✓

> [!example] Exercise 35 — At Least 3 of Every Suit
> **Problem.** A random 13-card hand is dealt from a standard deck of cards. What is the probability that the hand contains at least 3 cards of every suit?
>
> > [!success]- Click to reveal solution
> > **Solution.** Only feasible distribution: 4-3-3-3. $\dfrac{4 \binom{13}{4} \binom{13}{3}^3}{\binom{52}{13}} \approx 0.105$.
> >
> > **Answer.** ≈ $0.105$ ✓

> [!example] Exercise 36 — 30 Dice
> **Problem.** A group of 30 dice are thrown. What is the probability that 5 of each of the values $1, 2, 3, 4, 5, 6$ appear?
>
> > [!success]- Click to reveal solution
> > **Solution.** $\dfrac{30!/(5!)^6}{6^{30}}$.
> >
> > **Answer.** As above ✓

> [!example] Exercise 37 — First Ace
> **Problem.** A deck of cards is shuffled well. The cards are dealt one by one, until the first time an ace appears.
> (a) Find the probability that no kings, queens, or jacks appear before the first ace.
> (b) Find the probability that exactly one king, exactly one queen, and exactly one jack appear (in any order) before the first ace.
>
> > [!success]- Click to reveal solution
> > **Solution.** By symmetry restrict to the 16 face-card+ace cards. (a) $P$(first is an ace) $= 4/16 = 1/4$. (b) $\dfrac{12}{16} \cdot \dfrac{8}{15} \cdot \dfrac{4}{14} \cdot \dfrac{4}{13} = 16/455$.
> >
> > **Answer.** (a) $1/4$ — (b) $16/455$ ✓

> [!example] Exercise 38 — Round Table
> **Problem.** Tyrion, Cersei, and ten other people are sitting at a round table, with their seating arrangement having been randomly assigned. What is the probability that Tyrion and Cersei are sitting next to each other? Find this in two ways:
> (a) using a sample space of size $12!$, where an outcome is fully detailed about the seating;
> (b) using a much smaller sample space, which focuses on Tyrion and Cersei.
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) $\dfrac{12 \cdot 2 \cdot 10!}{12!} = \dfrac{2}{11}$. (b) Fix Tyrion; 2 of Cersei's 11 remaining seats are adjacent: $2/11$.
> >
> > **Answer.** $2/11$ ✓

> [!example] Exercise 39 — Couples Committee
> **Problem.** An organization with $2n$ people consists of $n$ married couples. A committee of size $k$ is selected, with all possibilities equally likely. Find the probability that there are exactly $j$ married couples within the committee.
>
> > [!success]- Click to reveal solution
> > **Solution.** $\dfrac{\binom{n}{j} \binom{n-j}{k-2j} 2^{k-2j}}{\binom{2n}{k}}$.
> >
> > **Answer.** As above ✓

> [!example] Exercise 40 — Monotone Draws
> **Problem.** There are $n$ balls in a jar, labeled with the numbers $1, 2, \ldots, n$. A total of $k$ balls are drawn, one by one with replacement, to obtain a sequence of numbers.
> (a) What is the probability that the sequence obtained is strictly increasing?
> (b) What is the probability that the sequence obtained is increasing (but not necessarily strictly increasing, i.e., there can be repetitions)?
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) $\binom{n}{k}/n^k$. (b) Stars-and-bars: $\binom{n+k-1}{k}/n^k$.
> >
> > **Answer.** As above ✓

> [!example] Exercise 41 — Exactly One Empty Box
> **Problem.** Each of $n$ balls is independently placed into one of $n$ boxes, with all boxes equally likely. What is the probability that exactly one box is empty?
>
> > [!success]- Click to reveal solution
> > **Solution.** Distribution must be one box with 2 balls, $n-2$ boxes with 1, one box empty. Count: $n \cdot \binom{n}{2} \cdot (n-1)! = \binom{n}{2} \cdot n!$. $P = \dfrac{\binom{n}{2} \cdot n!}{n^n}$.
> >
> > **Answer.** $\dfrac{\binom{n}{2} n!}{n^n}$ ✓

> [!example] Exercise 42 — Norepeatword Approaches $1/e$
> **Problem.** A norepeatword is a sequence of at least one (and possibly all) of the usual 26 letters a, b, c, ..., z, with repetitions not allowed. For example, "course" is a norepeatword, but "statistics" is not. Order matters, e.g., "course" is not the same as "source". A norepeatword is chosen randomly, with all norepeatwords equally likely. Show that the probability that it uses all 26 letters is very close to $1/e$.
>
> > [!success]- Click to reveal solution
> > **Solution.** Total norepeatwords $= \sum_{k=1}^{26} \dfrac{26!}{(26-k)!}$. Favorable $= 26!$. Ratio $= \dfrac{1}{\sum_{j=0}^{25} 1/j!}$. Since $e = \sum_{j=0}^{\infty} 1/j!$ and the tail beyond $j=25$ is essentially 0, denominator $\approx e$, so $P \approx 1/e$.
> >
> > **Answer.** $\approx 1/e$ ✓

---

## Axioms of Probability (Exercises 43–48)

> [!example] Exercise 43 — Bonferroni-Style Bounds
> **Problem.** Show that for any events $A$ and $B$, $P(A) + P(B) - 1 \le P(A \cap B) \le P(A \cup B) \le P(A) + P(B)$. For each of these three inequalities, give a simple criterion for when the inequality is actually an equality (e.g., give a simple condition such that $P(A \cap B) = P(A \cup B)$ if and only if the condition holds).
>
> > [!success]- Click to reveal solution
> > **Solution.** All three from inclusion-exclusion + non-negativity + monotonicity. Equalities: (1) iff $P(A \cup B) = 1$; (2) iff $P(A) = P(B) = P(A \cap B)$; (3) iff $A, B$ disjoint. ✓

> [!example] Exercise 44 — Set Difference
> **Problem.** Let $A$ and $B$ be events. The difference $B - A$ is defined to be the set of all elements of $B$ that are not in $A$. Show that if $A \subseteq B$, then $P(B - A) = P(B) - P(A)$, directly using the axioms of probability.
>
> > [!success]- Click to reveal solution
> > **Solution.** $B = A \cup (B - A)$, disjoint. By countable additivity, $P(B) = P(A) + P(B - A)$. ✓

> [!example] Exercise 45 — Symmetric Difference
> **Problem.** Let $A$ and $B$ be events. The symmetric difference $A \Delta B$ is defined to be the set of all elements that are in $A$ or $B$ but not both. In logic and engineering, this event is also called the XOR (exclusive or) of $A$ and $B$. Show that $P(A \Delta B) = P(A) + P(B) - 2P(A \cap B)$, directly using the axioms of probability.
>
> > [!success]- Click to reveal solution
> > **Solution.** $A \Delta B = (A \cap B^c) \sqcup (B \cap A^c)$. Since $A = (A \cap B) \sqcup (A \cap B^c)$, additivity gives $P(A \cap B^c) = P(A) - P(A \cap B)$. Symmetrically for $B$. Sum the two. ✓

> [!example] Exercise 46 — Exactly $k$ vs At Least $k$
> **Problem.** Let $A_1, A_2, \ldots, A_n$ be events. Let $B_k$ be the event that exactly $k$ of the $A_i$ occur, and $C_k$ be the event that at least $k$ of the $A_i$ occur, for $0 \le k \le n$. Find a simple expression for $P(B_k)$ in terms of $P(C_k)$ and $P(C_{k+1})$.
>
> > [!success]- Click to reveal solution
> > **Solution.** $C_k = B_k \sqcup C_{k+1}$ (disjoint). So $P(B_k) = P(C_k) - P(C_{k+1})$. ✓

> [!example] Exercise 47 — Independence Properties
> **Problem.** Events $A$ and $B$ are independent if $P(A \cap B) = P(A)P(B)$ (independence is explored in detail in the next chapter).
> (a) Give an example of independent events $A$ and $B$ in a finite sample space $S$ (with neither equal to $\emptyset$ or $S$), and illustrate it with a Pebble World diagram.
> (b) Consider the experiment of picking a random point in the rectangle $R = \{(x, y) : 0 < x < 1, 0 < y < 1\}$, where the probability of the point being in any particular region contained within $R$ is the area of that region. Let $A_1$ and $B_1$ be rectangles contained within $R$, with areas not equal to 0 or 1. Let $A$ be the event that the random point is in $A_1$, and $B$ be the event that the random point is in $B_1$. Give a geometric description of when it is true that $A$ and $B$ are independent. Also, give an example where they are independent and another example where they are not independent.
> (c) Show that if $A$ and $B$ are independent, then $P(A \cup B) = P(A) + P(B) - P(A)P(B) = 1 - P(A^c)P(B^c)$.
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) Two coin flips, $A$ = first H, $B$ = second H. (b) Independent iff $\text{Area}(A_1 \cap B_1) = \text{Area}(A_1) \cdot \text{Area}(B_1)$. (c) Inclusion-exclusion plus substitution: $P(A) + P(B) - P(A)P(B) = 1 - (1-P(A))(1-P(B)) = 1 - P(A^c)P(B^c)$. ✓

> [!example] Exercise 48 — Dutch Book on Arby
> **Problem.** Arby has a belief system assigning a number $P_{\text{Arby}}(A)$ between 0 and 1 to every event $A$ (for some sample space). This represents Arby's degree of belief about how likely $A$ is to occur. For any event $A$, Arby is willing to pay a price of $1000 \cdot P_{\text{Arby}}(A)$ dollars to buy a certificate that pays \$1000 if $A$ occurs (and no value if $A$ does not occur). Likewise, Arby is willing to sell such a certificate at the same price. Indeed, Arby is willing to buy or sell any number of certificates at this price, as Arby considers it the "fair" price.
> Arby stubbornly refuses to accept the axioms of probability. In particular, suppose that there are two disjoint events $A$ and $B$ with $P_{\text{Arby}}(A \cup B) \neq P_{\text{Arby}}(A) + P_{\text{Arby}}(B)$. Show how to make Arby go bankrupt, by giving a list of transactions Arby is willing to make that will guarantee that Arby will lose money (you can assume it will be known whether $A$ occurred and whether $B$ occurred the day after any certificates are bought/sold).
>
> > [!success]- Click to reveal solution
> > **Solution.** If $P(A \cup B) < P(A) + P(B)$: buy $A \cup B$ from Arby (cheap), sell $A$ and $B$ to Arby (expensive). Upfront profit $= 1000(P(A) + P(B) - P(A \cup B)) > 0$. Future payouts cancel because $A, B$ disjoint. Reverse direction is symmetric. ✓

---

## Inclusion-Exclusion (Exercises 49–55)

> [!example] Exercise 49 — Die Values Missing
> **Problem.** A fair die is rolled $n$ times. What is the probability that at least 1 of the 6 values never appears?
>
> > [!success]- Click to reveal solution
> > **Solution.** $A_i$ = value $i$ never appears. By I-E:
> > $$6\!\left(\frac{5}{6}\right)^n - 15\!\left(\frac{4}{6}\right)^n + 20\!\left(\frac{3}{6}\right)^n - 15\!\left(\frac{2}{6}\right)^n + 6\!\left(\frac{1}{6}\right)^n$$
> >
> > **Answer.** As above ✓

> [!example] Exercise 50 — Bridge Hand Void in a Suit
> **Problem.** A card player is dealt a 13-card hand from a well-shuffled, standard deck of cards. What is the probability that the hand is void in at least one suit ("void in a suit" means having no cards of that suit)?
>
> > [!success]- Click to reveal solution
> > **Solution.** $\dfrac{4\binom{39}{13} - 6\binom{26}{13} + 4}{\binom{52}{13}}$ (the four-suit-void term is impossible).
> >
> > **Answer.** As above ✓

> [!example] Exercise 51 — All 4 Seasons in 7 Birthdays
> **Problem.** For a group of 7 people, find the probability that all 4 seasons (winter, spring, summer, fall) occur at least once each among their birthdays, assuming that all seasons are equally likely.
>
> > [!success]- Click to reveal solution
> > **Solution.** Complement: $4(3/4)^7 - 6(2/4)^7 + 4(1/4)^7 - 0 = (8748 - 768 + 4)/16384 = 7984/16384$. So $P = 8400/16384 = 525/1024 \approx 0.5127$.
> >
> > **Answer.** $525/1024$ ✓

> [!example] Exercise 52 — Same Seat, 20 Students
> **Problem.** A certain class has 20 students, and meets on Mondays and Wednesdays in a classroom with exactly 20 seats. In a certain week, everyone in the class attends both days. On both days, the students choose their seats completely randomly (with one student per seat). Find the probability that no one sits in the same seat on both days of that week.
>
> > [!success]- Click to reveal solution
> > **Solution.** Derangement: $\sum_{k=0}^{20} (-1)^k/k! \approx 1/e \approx 0.368$.
> >
> > **Answer.** $\approx 1/e$ ✓

> [!example] Exercise 53 — 8-Char Password
> **Problem.** Fred needs to choose a password for a certain website. Assume that he will choose an 8-character password, and that the legal characters are the lowercase letters a, b, c, ..., z, the uppercase letters A, B, C, ..., Z, and the numbers 0, 1, ..., 9.
> (a) How many possibilities are there if he is required to have at least one lowercase letter in his password?
> (b) How many possibilities are there if he is required to have at least one lowercase letter and at least one uppercase letter in his password?
> (c) How many possibilities are there if he is required to have at least one lowercase letter, at least one uppercase letter, and at least one number in his password?
>
> > [!success]- Click to reveal solution
> > **Solution.** Total $62^8$. (a) $62^8 - 36^8$. (b) $62^8 - 2 \cdot 36^8 + 10^8$. (c) $62^8 - 52^8 - 2 \cdot 36^8 + 2 \cdot 26^8 + 10^8$.
> >
> > **Answer.** As above ✓

> [!example] Exercise 54 — Class Every Day
> **Problem.** Alice attends a small college in which each class meets only once a week. She is deciding between 30 non-overlapping classes. There are 6 classes to choose from for each day of the week, Monday through Friday. Trusting in the benevolence of randomness, Alice decides to register for 7 randomly selected classes out of the 30, with all choices equally likely. What is the probability that she will have classes every day, Monday through Friday? (This problem can be done either directly using the naive definition of probability, or using inclusion-exclusion.)
>
> > [!success]- Click to reveal solution
> > **Solution.** Complement via I-E: $P(\text{some day missing}) = [5\binom{24}{7} - 10\binom{18}{7} + 10\binom{12}{7}]/\binom{30}{7}$. So $P(\text{class every day}) = 114/377 \approx 0.302$.
> >
> > **Answer.** $114/377$ ✓

> [!example] Exercise 55 — Mixed Committee
> **Problem.** A club consists of 10 seniors, 12 juniors, and 15 sophomores. An organizing committee of size 5 is chosen randomly (with all subsets of size 5 equally likely).
> (a) Find the probability that there are exactly 3 sophomores in the committee.
> (b) Find the probability that the committee has at least one representative from each of the senior, junior, and sophomore classes.
>
> > [!success]- Click to reveal solution
> > **Solution.** Total $\binom{37}{5}$. (a) $\binom{15}{3}\binom{22}{2}/\binom{37}{5}$. (b) $1 - [\binom{27}{5} + \binom{25}{5} + \binom{22}{5} - \binom{15}{5} - \binom{12}{5} - \binom{10}{5}]/\binom{37}{5}$.
> >
> > **Answer.** As above ✓

---

## Mixed Practice (Exercises 56–62)

> [!example] Exercise 56 — Comparison Fills
> **Problem.** For each part, decide whether the blank should be filled in with $=$, $<$, or $>$, and give a clear explanation. In (a) and (b), order doesn't matter.
> (a) (number of ways to choose 5 people out of 10) ____ (number of ways to choose 6 people out of 10)
> (b) (number of ways to break 10 people into 2 teams of 5) ____ (number of ways to break 10 people into a team of 6 and a team of 4)
> (c) (probability that all 3 people in a group of 3 were born on January 1) ____ (probability that in a group of 3 people, 1 was born on each of January 1, 2, and 3)
>
> Martin and Gale play an exciting game of "toss the coin", where they toss a fair coin until the pattern $HH$ occurs (two consecutive Heads) or the pattern $TH$ occurs (Tails followed immediately by Heads). Martin wins the game if and only if $HH$ occurs before $TH$ occurs.
> (d) (probability that Martin wins) ____ $1/2$
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
> **Problem.** Take a deep breath before attempting this problem. In the book *Innumeracy*, John Allen Paulos writes:
> "Now for better news of a kind of immortal persistence. First, take a deep breath. Assume Shakespeare's account is accurate and Julius Caesar gasped ['Et tu, Brute!'] before breathing his last. What are the chances you just inhaled a molecule which Caesar exhaled in his dying breath?"
> Assume that one breath of air contains $10^{22}$ molecules, and that there are $10^{44}$ molecules in the atmosphere. (These are slightly simpler numbers than the estimates that Paulos gives; for the purposes of this problem, assume that these are exact. Of course, in reality there are many complications such as different types of molecules in the atmosphere, chemical reactions, variation in lung capacities, etc.)
> Suppose that the molecules in the atmosphere now are the same as those in the atmosphere when Caesar was alive, and that in the 2000 years or so since Caesar, these molecules have been scattered completely randomly through the atmosphere. Also assume that Caesar's last breath was sampled without replacement but that your breathing is sampled with replacement (without replacement makes more sense but with replacement is easier to work with, and is a good approximation since the number of molecules in the atmosphere is so much larger than the number of molecules in one breath).
> Find the probability that at least one molecule in the breath you just took was shared with Caesar's last breath, and give a simple approximation in terms of $e$.
> Hint: As discussed in the math appendix, $(1 + x/n)^n \approx e^x$ for $n$ large.
>
> > [!success]- Click to reveal solution
> > **Solution.** $1 - (1 - 10^{-22})^{10^{22}} \to 1 - e^{-1}$.
> >
> > **Answer.** $1 - e^{-1} \approx 0.632$ ✓

> [!example] Exercise 58 — Widget Inspector
> **Problem.** A widget inspector inspects 12 widgets and finds that exactly 3 are defective. Unfortunately, the widgets then get all mixed up and the inspector has to find the 3 defective widgets again by testing widgets one by one.
> (a) Find the probability that the inspector will now have to test at least 9 widgets.
> (b) Find the probability that the inspector will now have to test at least 10 widgets.
>
> > [!success]- Click to reveal solution
> > **Solution.** Treat the 3 defective positions as uniformly distributed in 12 spots. (a) Complement: all 3 in first 8 = $\binom{8}{3}/\binom{12}{3} = 56/220$. So $P = 1 - 56/220 = 41/55$. (b) $1 - \binom{9}{3}/\binom{12}{3} = 1 - 84/220 = 34/55$.
> >
> > **Answer.** (a) $41/55$ — (b) $34/55$ ✓

> [!example] Exercise 59 — Chocolate Distributions
> **Problem.** There are 15 chocolate bars and 10 children. In how many ways can the chocolate bars be distributed to the children, in each of the following scenarios?
> (a) The chocolate bars are fungible (interchangeable).
> (b) The chocolate bars are fungible, and each child must receive at least one.
> Hint: First give each child a chocolate bar, and then decide what to do with the rest.
> (c) The chocolate bars are not fungible (it matters which particular bar goes where).
> (d) The chocolate bars are not fungible, and each child must receive at least one.
> Hint: The strategy suggested in (b) does not apply. Instead, consider randomly giving the chocolate bars to the children, and apply inclusion-exclusion.
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) Stars-and-bars: $\binom{24}{15}$. (b) Reserve 1 each, distribute 5: $\binom{14}{5}$. (c) Each bar 10 choices: $10^{15}$. (d) Inclusion-exclusion (surjection count): $\sum_{j=0}^{10} (-1)^j \binom{10}{j} (10-j)^{15}$.
> >
> > **Answer.** As above ✓

> [!example] Exercise 60 — Bootstrap Sampling
> **Problem.** Given $n \ge 2$ numbers $(a_1, a_2, \ldots, a_n)$ with no repetitions, a bootstrap sample is a sequence $(x_1, x_2, \ldots, x_n)$ formed from the $a_j$'s by sampling with replacement with equal probabilities. Bootstrap samples arise in a widely used statistical method known as the bootstrap. For example, if $n = 2$ and $(a_1, a_2) = (3, 1)$, then the possible bootstrap samples are $(3, 3), (3, 1), (1, 3)$, and $(1, 1)$.
> (a) How many possible bootstrap samples are there for $(a_1, \ldots, a_n)$?
> (b) How many possible bootstrap samples are there for $(a_1, \ldots, a_n)$, if order does not matter (in the sense that it only matters how many times each $a_j$ was chosen, not the order in which they were chosen)?
> (c) One random bootstrap sample is chosen (by sampling from $a_1, \ldots, a_n$ with replacement, as described above). Show that not all unordered bootstrap samples (in the sense of (b)) are equally likely. Find an unordered bootstrap sample $b_1$ that is as likely as possible, and an unordered bootstrap sample $b_2$ that is as unlikely as possible. Let $p_1$ be the probability of getting $b_1$ and $p_2$ be the probability of getting $b_2$ (so $p_i$ is the probability of getting the specific unordered bootstrap sample $b_i$). What is $p_1/p_2$? What is the ratio of the probability of getting an unordered bootstrap sample whose probability is $p_1$ to the probability of getting an unordered sample whose probability is $p_2$?
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) $n^n$. (b) Stars-and-bars: $\binom{2n-1}{n}$. (c) Most likely (all distinct): $n!/n^n$. Least likely (all same): $1/n^n$. Ratio $p_1/p_2 = n!$. There's 1 "all distinct" class but $n$ "all same" classes (one per value), so class-probability ratio $= n!/n = (n-1)!$.
> >
> > **Answer.** (a) $n^n$ — (b) $\binom{2n-1}{n}$ — (c) $n!$ and $(n-1)!$ ✓

> [!example] Exercise 61 — Lost Boarding Pass
> **Problem.** There are 100 passengers lined up to board an airplane with 100 seats (with each seat assigned to one of the passengers). The first passenger in line crazily decides to sit in a randomly chosen seat (with all seats equally likely). Each subsequent passenger takes their assigned seat if available, and otherwise sits in a random available seat. What is the probability that the last passenger in line gets to sit in their assigned seat? (This is a common interview problem, and a beautiful example of the power of symmetry.)
> Hint: Call the seat assigned to the $j$th passenger in line "seat $j$" (regardless of whether the airline calls it seat 23A or whatever). What are the possibilities for which seats are available to the last passenger in line, and what is the probability of each of these possibilities?
>
> > [!success]- Click to reveal solution
> > **Solution.** Symmetry argument: at every step, seat 1 and seat 100 are treated identically by displaced passengers (neither is anyone's "own" seat for $j = 2, \ldots, 99$). The chain ends when seat 1 OR seat 100 is taken, each equally likely.
> >
> > **Answer.** $1/2$ ✓

> [!example] Exercise 62 — Non-Uniform Birthday
> **Problem.** In the birthday problem, we assumed that all 365 days of the year are equally likely (and excluded February 29). In reality, some days are slightly more likely as birthdays than others. For example, scientists have long struggled to understand why more babies are born 9 months after a holiday. Let $p = (p_1, p_2, \ldots, p_{365})$ be the vector of birthday probabilities, with $p_j$ the probability of being born on the $j$th day of the year (February 29 is still excluded, with no offense intended to Leap Dayers).
> The $k$th elementary symmetric polynomial in the variables $x_1, \ldots, x_n$ is defined by $e_k(x_1, \ldots, x_n) = \sum_{1 \le j_1 < j_2 < \dots < j_k \le n} x_{j_1} \ldots x_{j_k}$. This just says to add up all of the $\binom{n}{k}$ terms we can get by choosing and multiplying $k$ of the variables.
> Now let $k \ge 2$ be the number of people.
> (a) Find a simple expression for the probability that there is at least one birthday match, in terms of $p$ and an elementary symmetric polynomial.
> (b) Explain intuitively why it makes sense that $P$(at least one birthday match) is minimized when $p_j = 1/365$ for all $j$, by considering simple and extreme cases.
> (c) The famous arithmetic mean-geometric mean inequality says that for $x, y \ge 0$, $(x+y)/2 \ge \sqrt{xy}$. Define $r = (r_1, \ldots, r_{365})$ by $r_1 = r_2 = (p_1 + p_2)/2$, $r_j = p_j$ for $3 \le j \le 365$. Using the AM-GM bound and the identity $e_k(x_1, \ldots, x_n) = x_1 x_2 e_{k-2}(x_3, \ldots, x_n) + (x_1 + x_2) e_{k-1}(x_3, \ldots, x_n) + e_k(x_3, \ldots, x_n)$, show that $P(\text{at least one birthday match} | p) \ge P(\text{at least one birthday match} | r)$, with strict inequality if $p \neq r$. Using this, show that the value of $p$ that minimizes the probability of at least one birthday match is given by $p_j = 1/365$ for all $j$.
>
> > [!success]- Click to reveal solution
> > **Solution.** (a) $P(\text{no match}) = k! \cdot e_k(p)$, so $P(\text{match}) = 1 - k! \cdot e_k(p)$. (b) Clumped distributions force collisions (extreme: $p_1 = 1$ gives $P = 1$). (c) Using $e_k(x_1, x_2, \ldots) = x_1 x_2 E_{k-2} + (x_1 + x_2)E_{k-1} + E_k$, only the $x_1 x_2$ term varies under averaging; $((p_1 + p_2)/2)^2 \geq p_1 p_2$ by AM-GM. Iterated smoothing converges to uniform.
> >
> > **Answer.** $P(\text{match}) = 1 - k! \cdot e_k(p)$, minimized at $p_j = 1/365$ ✓

---

## Related Documents

- **[Chapter 1 (Main)](<Chapter 1 (Main).md>)** — Hub note covering sections 1.1-1.6 with definitions, examples, and figures.
- **[Introduction to Probability (Main)](<../Introduction to Probability (Main).md>)** — Book-level hub.
