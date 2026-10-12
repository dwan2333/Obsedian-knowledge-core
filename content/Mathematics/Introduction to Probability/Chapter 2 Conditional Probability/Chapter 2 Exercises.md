# Chapter 2 — Exercises (2.11)

*Companion document to [Chapter 2 (Main)](<Chapter 2 (Main).md>)*

_All 74 chapter-end exercises with NotebookLM-generated solutions and full main-agent verification._

---

> [!success] Verification Status: 74 / 74 ✓
> Every solution below was independently re-derived by the main agent and cross-checked against NotebookLM's response. **Zero discrepancies found.** Closed-form answers were checked algebraically; numerical answers to within rounding. Open-ended modelling parts ("give an example", "explain intuitively") are reproduced as reasoned arguments.
>
> **Tip:** Each problem statement is reproduced from the textbook. Click "Click to reveal solution" to check your work after attempting the exercise.

---

## Conditioning on evidence (Exercises 1–29)

> [!example] Exercise 1 — Spam Filter
> **Problem.** A spam filter is designed by looking at commonly occurring phrases in spam. Suppose that 80% of email is spam. In 10% of the spam emails, the phrase "free money" is used, whereas this phrase is only used in 1% of non-spam emails. A new email has just arrived, which does mention "free money". What is the probability that it is spam?
> 
> > [!success]- Click to reveal solution
> > We want to find the conditional probability that an email is spam given that it contains the phrase "free money". We apply **Bayes' rule** to reverse the conditioning, and the **Law of Total Probability** to expand the denominator. Let $S$ be the event that the email is spam, and $F$ be the event that it contains "free money". We are given the prior probabilities $P(S) = 0.8$ and $P(S^c) = 0.2$, along with the conditional probabilities $P(F|S) = 0.10$ and $P(F|S^c) = 0.01$. The posterior probability is calculated as $\frac{P(F|S)P(S)}{P(F|S)P(S) + P(F|S^c)P(S^c)}$. Substituting the values gives $\frac{0.10 \times 0.8}{0.10 \times 0.8 + 0.01 \times 0.2}$.
> > 
> > **Answer.** $\frac{40}{41}$ ✓

> [!example] Exercise 2 — Twin Boys
> **Problem.** A woman is pregnant with twin boys. Twins may be either identical or fraternal. Suppose that 1/3 of twins born are identical, that identical twins have a 50% chance of being both boys and a 50% chance of being both girls, and that for fraternal twins each twin independently has a 50% chance of being a boy and a 50% chance of being a girl. Given the above information, what is the probability that the woman's twins are identical?
> 
> > [!success]- Click to reveal solution
> > We seek the conditional probability that the twins are identical given that they are both boys. We use **Bayes' rule** and the **Law of Total Probability**. Let $I$ be the event that the twins are identical, $F$ be the event that they are fraternal, and $BB$ be the event that both are boys. The prior probabilities are $P(I) = \frac{1}{3}$ and $P(F) = \frac{2}{3}$. If they are identical, they must be both boys or both girls with equal probability, so $P(BB|I) = 0.5$. If they are fraternal, the genders of the two children are independent, so by the definition of **independence**, $P(BB|F) = 0.5 \times 0.5 = 0.25$. Applying Bayes' rule yields $P(I|BB) = \frac{P(BB|I)P(I)}{P(BB|I)P(I) + P(BB|F)P(F)} = \frac{0.5 \times (1/3)}{0.5 \times (1/3) + 0.25 \times (2/3)}$.
> > 
> > **Answer.** $\frac{1}{2}$ ✓

> [!example] Exercise 3 — Smoking and Lung Cancer
> **Problem.** According to the CDC (Centers for Disease Control and Prevention), men who smoke are 23 times more likely to develop lung cancer than men who don't smoke. Also according to the CDC, 21.6% of men in the U.S. smoke. What is the probability that a man in the U.S. is a smoker, given that he develops lung cancer?
> 
> > [!success]- Click to reveal solution
> > We must find the probability that a man is a smoker given that he develops lung cancer. Let $S$ be the event of being a smoker and $L$ be the event of developing lung cancer. We are given the prior probability $P(S) = 0.216$, so $P(S^c) = 0.784$. The relative risk is 23, meaning $P(L|S) = 23 \cdot P(L|S^c)$. We use **Bayes' rule** and the **Law of Total Probability**. The target is $P(S|L) = \frac{P(L|S)P(S)}{P(L|S)P(S) + P(L|S^c)P(S^c)}$. Substituting $23 \cdot P(L|S^c)$ for $P(L|S)$, the unknown term $P(L|S^c)$ cancels out from the numerator and denominator, leaving $\frac{23 \times 0.216}{23 \times 0.216 + 0.784}$.
> > 
> > **Answer.** $\frac{621}{719}$ ✓

> [!example] Exercise 4 — Multiple-Choice Guessing
> **Problem.** Fred is answering a multiple-choice problem on an exam, and has to choose one of n options (exactly one of which is correct). Let K be the event that he knows the answer, and R be the event that he gets the problem right (either through knowledge or through luck). Suppose that if he knows the right answer he will definitely get the problem right, but if he does not know then he will guess completely randomly. Let P(K) = p. (a) Find P(K|R) (in terms of p and n). (b) Show that P(K|R) ≥p, and explain why this makes sense intuitively. When (if ever) does P(K|R) equal p?
> 
> > [!success]- Click to reveal solution
> > Part (a): We want the conditional probability that Fred knows the answer ($K$) given that he gets it right ($R$). By the problem statement, $P(K) = p$, $P(R|K) = 1$, and $P(R|K^c) = \frac{1}{n}$. We apply **Bayes' rule** and the **Law of Total Probability** to calculate $P(K|R) = \frac{P(R|K)P(K)}{P(R|K)P(K) + P(R|K^c)P(K^c)} = \frac{1 \cdot p}{1 \cdot p + \frac{1}{n}(1-p)}$.
> > Part (b): To show $P(K|R) \geq p$, we simplify the result from part (a) to $\frac{np}{np + 1 - p}$ and set up the inequality $\frac{np}{np + 1 - p} \geq p$. Multiplying by the denominator yields $np \geq np^2 + p - p^2$, which factors to $np - p \geq p^2(n-1)$, and then $p(n-1) \geq p^2(n-1)$. Since $p$ is a probability ($0 \leq p \leq 1$), $p \geq p^2$ is always true.
> > 
> > **Answer.** (a) $\frac{np}{1 + (n-1)p}$. (b) Equality holds if $p=0$,
$p=1$, or $n=1$. ✓

> [!example] Exercise 5 — Three Cards
> **Problem.** Three cards are dealt from a standard, well-shuffled deck. The first two cards are flipped over, revealing the Ace of Spades as the first card and the 8 of Clubs as the second card. Given this information, find the probability that the third card is an ace in two ways: using the definition of conditional probability, and by symmetry.
> 
> > [!success]- Click to reveal solution
> > We are given the identities of the first two cards (Ace of Spades and 8 of Clubs) and want the conditional probability that the third card is an ace. Using the **definition of conditional probability**, we restrict our attention to the updated sample space of remaining cards. Out of the 52 cards, 2 specific cards have been removed, leaving exactly 50 cards. Alternatively, using **symmetry**, the third card is equally likely to be any of those 50 remaining cards that have not yet been revealed. Because the Ace of Spades was drawn, exactly 3 of the remaining 50 cards are aces.
> > 
> > **Answer.** $\frac{3}{50}$ ✓

> [!example] Exercise 6 — Double-Headed Coin
> **Problem.** A hat contains 100 coins, where 99 are fair but one is double-headed (always landing Heads). A coin is chosen uniformly at random. The chosen coin is flipped 7 times, and it lands Heads all 7 times. Given this information, what is the probability that the chosen coin is double-headed? (Of course, another approach here would be to look at both sides of the coin-but this is a metaphorical coin.)
> 
> > [!success]- Click to reveal solution
> > We are asked for the probability that a chosen coin is double-headed given that it lands Heads 7 times. Let $D$ be the event of choosing the double-headed coin, $F$ be the event of choosing a fair coin, and $H_7$ be the event of observing 7 Heads. The prior probabilities are $P(D) = \frac{1}{100}$ and $P(F) = \frac{99}{100}$. Due to the **independence** of the coin flips, the conditional probabilities of observing 7 Heads are $P(H_7|D) = 1^7 = 1$ and $P(H_7|F) = (\frac{1}{2})^7 = \frac{1}{128}$. We use **Bayes' rule** and the **Law of Total Probability**: $P(D|H_7) = \frac{P(H_7|D)P(D)}{P(H_7|D)P(D) + P(H_7|F)P(F)} = \frac{1 \times (1/100)}{1 \times (1/100) + (1/128) \times (99/100)}$.
> > 
> > **Answer.** $\frac{128}{227}$ ✓

> [!example] Exercise 7 — Coin in a Hat (Two-Level)
> **Problem.** A hat contains 100 coins, where at least 99 are fair, but there may be one that is doubleheaded (always landing Heads); if there is no such coin, then all 100 are fair. Let D be the event that there is such a coin, and suppose that P(D) = 1/2. A coin is chosen uniformly at random. The chosen coin is flipped 7 times, and it lands Heads all 7 times. (a) Given this information, what is the probability that one of the coins is doubleheaded? (b) Given this information, what is the probability that the chosen coin is doubleheaded?
> 
> > [!success]- Click to reveal solution
> > Let $D$ be the event that the hat contains a double-headed coin, so $P(D) = \frac{1}{2}$ and $P(D^c) = \frac{1}{2}$. Let $C$ be the event that the chosen coin is double-headed, and $H_7$ be the event of 7 Heads.
> > Part (a): We want $P(D|H_7)$. We use **Bayes' rule** and the **Law of Total Probability**. The probability of 7 Heads given $D$ requires the **Law of Total Probability with extra conditioning** on whether the chosen coin is double-headed: $P(H_7|D) = P(H_7|C)P(C|D) + P(H_7|C^c, D)P(C^c|D) = 1 \times (\frac{1}{100}) + (\frac{1}{128}) \times (\frac{99}{100}) = \frac{227}{12800}$. The probability of 7 Heads given $D^c$ is $P(H_7|D^c) = \frac{1}{128} = \frac{100}{12800}$. Applying Bayes' rule: $P(D|H_7) = \frac{P(H_7|D)P(D)}{P(H_7|D)P(D) + P(H_7|D^c)P(D^c)}$.
> > Part (b): We want $P(C|H_7)$. We use **Bayes' rule** and the **Law of Total Probability**. The prior probability of choosing the double-headed coin is $P(C) = P(C|D)P(D) = \frac{1}{100} \times \frac{1}{2} = \frac{1}{200}$. Thus $P(C|H_7) = \frac{P(H_7|C)P(C)}{P(H_7)} = \frac{1 \times (1/200)}{(327/25600)}$.
> > 
> > **Answer.** (a) $\frac{227}{327}$; (b) $\frac{128}{327}$ ✓

> [!example] Exercise 8 — Cell-Phone Screens
> **Problem.** The screens used for a certain type of cell phone are manufactured by 3 companies, A, B, and C. The proportions of screens supplied by A, B, and C are 0.5, 0.3, and 0.2, respectively, and their screens are defective with probabilities 0.01, 0.02, and 0.03, respectively. Given that the screen on such a phone is defective, what is the probability that Company A manufactured it?
> 
> > [!success]- Click to reveal solution
> > We want the conditional probability that Company A manufactured the screen given that it is defective. Let $A$, $B$, and $C$ be the events that the screen was manufactured by Company A, B, and C, respectively. Let $D$ be the event that the screen is defective. We are given prior probabilities $P(A) = 0.5$, $P(B) = 0.3$, $P(C) = 0.2$ and conditional probabilities $P(D|A) = 0.01$, $P(D|B) = 0.02$, $P(D|C) = 0.03$. Using **Bayes' rule** and the **Law of Total Probability**, $P(A|D) = \frac{P(D|A)P(A)}{P(D|A)P(A) + P(D|B)P(B) + P(D|C)P(C)} = \frac{0.01 \times 0.5}{0.01 \times 0.5 + 0.02 \times 0.3 + 0.03 \times 0.2}$.
> > 
> > **Answer.** $\frac{5}{17}$ ✓

> [!example] Exercise 9 — Equal Priors, Both Imply B
> **Problem.** (a) Show that if events $A_{1}$ and $A_{2}$ have the same prior probability P($A_{1}$) = P($A_{2}$), $A_{1}$ implies B, and $A_{2}$ implies B, then $A_{1}$ and $A_{2}$ have the same posterior probability P($A_{1}$|B) = P($A_{2}$|B) if it is observed that B occurred. (b) Explain why (a) makes sense intuitively, and give a concrete example.
> 
> > [!success]- Click to reveal solution
> > Part (a): We want to show $P(A_1|B) = P(A_2|B)$. Because $A_1$ implies $B$, the conditional probability $P(B|A_1) = 1$. Similarly, because $A_2$ implies $B$, $P(B|A_2) = 1$. By **Bayes' rule**, $P(A_1|B) = \frac{P(B|A_1)P(A_1)}{P(B)} = \frac{P(A_1)}{P(B)}$. By the exact same logic, $P(A_2|B) = \frac{P(A_2)}{P(B)}$. Since we are given that the prior probabilities $P(A_1)$ and $P(A_2)$ are equal, it mathematically follows that $P(A_1|B) = P(A_2|B)$.
> > Part (b): Intuitively, since both events guarantee the occurrence of $B$, observing that $B$ has occurred does not change their relative likelihoods; it simply updates both of their prior probabilities by the exact same scaling factor. For a concrete example, let $A_1$ be rolling a 2 on a fair die, $A_2$ be rolling a 4, and $B$ be rolling an even number.
> > 
> > **Answer.** (a) $P(A_i|B) = \frac{P(B|A_i)P(A_i)}{P(B)} = 
\frac{P(A_i)}{P(B)}$. (b) Observing $B$ scales the probabilities of $A_1$ and 
$A_2$ identically. Example: $A_1$ = roll 2, $A_2$ = roll 4, $B$ = roll even on 
a standard die. ✓

> [!example] Exercise 10 — Fred's Project Milestones
> **Problem.** Fred is working on a major project. In planning the project, two milestones are set up, with dates by which they should be accomplished. This serves as a way to track Fred's progress. Let $A_{1}$ be the event that Fred completes the first milestone on time, $A_{2}$ be the event that he completes the second milestone on time, and $A_{3}$ be the event that he completes the project on time. Suppose that P($A_{j+1}$|$A_{j}$) = 0.8 but P($A_{j+1}$|$A_{j}^c$) = 0.3 for j = 1, 2, since if Fred falls behind on his schedule it will be hard for him to get caught up. Also, assume that the second milestone supersedes the first, in the sense that once we know whether he is on time in completing the second milestone, it no longer matters what happened with the first milestone. We can express this by saying that $A_{1}$ and $A_{3}$ are conditionally independent given $A_{2}$ and they're also conditionally independent given $A_{2}^c$. (a) Find the probability that Fred will finish the project on time, given that he completes the first milestone on time. Also find the probability that Fred will finish the project on time, given that he is late for the first milestone. (b) Suppose that P($A_{1}$) = 0.75. Find the probability that Fred will finish the project on time.
> 
> > [!success]- Click to reveal solution
> > Let $A_1, A_2, A_3$ be the events of finishing milestones 1, 2, and 3 on time. We are given $P(A_2|A_1) = P(A_3|A_2) = 0.8$ and $P(A_2|A_1^c) = P(A_3|A_2^c) = 0.3$. The problem states that $A_1$ and $A_3$ are **conditionally independent** given $A_2$, and given $A_2^c$.
> > Part (a): To find $P(A_3|A_1)$, we use the **Law of Total Probability with extra conditioning** on $A_2$: $P(A_3|A_1) = P(A_3|A_2, A_1)P(A_2|A_1) + P(A_3|A_2^c, A_1)P(A_2^c|A_1)$. Due to conditional independence, $P(A_3|A_2, A_1) = P(A_3|A_2)$, so this simplifies to $0.8 \times 0.8 + 0.3 \times 0.2 = 0.64 + 0.06$. Similarly, $P(A_3|A_1^c) = P(A_3|A_2)P(A_2|A_1^c) + P(A_3|A_2^c)P(A_2^c|A_1^c) = 0.8 \times 0.3 + 0.3 \times 0.7 = 0.24 + 0.21$.
> > Part (b): To find $P(A_3)$ given $P(A_1) = 0.75$, we use the **Law of Total Probability** conditioning on $A_1$: $P(A_3) = P(A_3|A_1)P(A_1) + P(A_3|A_1^c)P(A_1^c) = 0.70 \times 0.75 + 0.45 \times 0.25$.
> > 
> > **Answer.** (a) $P(A_3|A_1) = 0.70$ and $P(A_3|A_1^c) = 0.45$; (b) 
$0.6375$ (or $\frac{51}{80}$) ✓

> [!example] Exercise 11 — Exit-Poll Selection Bias
> **Problem.** An exit poll in an election is a survey taken of voters just after they have voted. One major use of exit polls has been so that news organizations can try to figure out as soon as possible who won the election, before the votes are officially counted. This has been notoriously inaccurate in various elections, sometimes because of selection bias: the sample of people who are invited to and agree to participate in the survey may not be similar enough to the overall population of voters. Consider an election with two candidates, Candidate A and Candidate B. Every voter is invited to participate in an exit poll, where they are asked whom they voted for; some accept and some refuse. For a randomly selected voter, let A be the event that they voted for A, and W be the event that they are willing to participate in the exit poll. Suppose that P(W|A) = 0.7 but P(W|$A^c$) = 0.3. In the exit poll, 60% of the respondents say they voted for A (assume that they are all honest), suggesting a comfortable victory for A. Find P(A), the true proportion of people who voted for A.
> 
> > [!success]- Click to reveal solution
> > We want to find the prior probability $p = P(A)$ that a random voter voted for Candidate A. Let $W$ be the event of being willing to participate. We are given $P(W|A) = 0.7$ and $P(W|A^c) = 0.3$, and the posterior probability from the survey is $P(A|W) = 0.6$. We apply **Bayes' rule** and the **Law of Total Probability**: $P(A|W) = \frac{P(W|A)P(A)}{P(W|A)P(A) + P(W|A^c)P(A^c)}$. Setting this equal to the survey result gives the algebraic equation $0.6 = \frac{0.7p}{0.7p + 0.3(1-p)}$. Simplifying the denominator to $0.4p + 0.3$ and cross-multiplying yields $0.24p + 0.18 = 0.7p$, which solves to $0.46p = 0.18$.
> > 
> > **Answer.** $\frac{9}{23}$ ✓

> [!example] Exercise 12 — Noisy Binary Channel
> **Problem.** Alice is trying to communicate with Bob, by sending a message (encoded in binary) across a channel. (a) Suppose for this part that she sends only one bit (a 0 or 1), with equal probabilities. If she sends a 0, there is a 5% chance of an error occurring, resulting in Bob receiving a 1; if she sends a 1, there is a 10% chance of an error occurring, resulting in Bob receiving a 0. Given that Bob receives a 1, what is the probability that Alice actually sent a 1? (b) To reduce the chance of miscommunication, Alice and Bob decide to use a repetition code. Again Alice wants to convey a 0 or a 1, but this time she repeats it two more times, so that she sends 000 to convey 0 and 111 to convey 1. Bob will decode the message by going with what the majority of the bits were. Assume that the error probabilities are as in (a), with error events for different bits independent of each other. Given that Bob receives 110, what is the probability that Alice intended to convey a 1?
> 
> > [!success]- Click to reveal solution
> > Let $A_0, A_1$ be the events of sending 0 and 1, and $B_0, B_1$ be the events of receiving 0 and 1. We are given $P(B_1|A_0) = 0.05$ and $P(B_0|A_1) = 0.10$.
> > Part (a): We want $P(A_1|B_1)$. Using **Bayes' rule** and the **Law of Total Probability**, $P(A_1|B_1) = \frac{P(B_1|A_1)P(A_1)}{P(B_1|A_1)P(A_1) + P(B_1|A_0)P(A_0)} = \frac{0.90 \times 0.5}{0.90 \times 0.5 + 0.05 \times 0.5}$.
> > Part (b): Now $A_0$ is sending 000, $A_1$ is sending 111, and $R$ is receiving 110. Assuming **independence** of bit errors, the conditional probabilities are $P(R|A_1) = 0.90 \times 0.90 \times 0.10 = 0.081$ and $P(R|A_0) = 0.05 \times 0.05 \times 0.95 = 0.002375$. Using **Bayes' rule** again, $P(A_1|R) = \frac{P(R|A_1)P(A_1)}{P(R|A_1)P(A_1) + P(R|A_0)P(A_0)} = \frac{0.081}{0.081 + 0.002375} = \frac{0.081}{0.083375}$.
> > 
> > **Answer.** (a) $\frac{18}{19}$; (b) $\frac{648}{667}$ ✓

> [!example] Exercise 13 — The Always-Negative Test
> **Problem.** Company A has just developed a diagnostic test for a certain disease. The disease afflicts 1% of the population. As defined in Example 2.3.9, the sensitivity of the test is the probability of someone testing positive, given that they have the disease, and the specificity of the test is the probability that of someone testing negative, given that they don't have the disease. Assume that, as in Example 2.3.9, the sensitivity and specificity are both 0.95. Company B, which is a rival of Company A, offers a competing test for the disease. Company B claims that their test is faster and less expensive to perform than Company A's test, is less painful (Company A's test requires an incision), and yet has a higher overall success rate, where overall success rate is defined as the probability that a random person gets diagnosed correctly. (a) It turns out that Company B's test can be described and performed very simply: no matter who the patient is, diagnose that they do not have the disease. Check whether Company B's claim about overall success rates is true. (b) Explain why Company A's test may still be useful. (c) Company A wants to develop a new test such that the overall success rate is higher than that of Company B's test. If the sensitivity and specificity are equal, how high does the sensitivity have to be to achieve their goal? If (amazingly) they can get the sensitivity equal to 1, how high does the specificity have to be to achieve their goal? If (amazingly) they can get the specificity equal to 1, how high does the sensitivity have to be to achieve their goal?
> 
> > [!success]- Click to reveal solution
> > Use the **Law of Total Probability** to calculate the overall success rate for both tests. Let $D$ be the event of having the disease ($P(D) = 0.01$, $P(D^c) = 0.99$). Let $T_A$ and $T_B$ be the events of testing positive on test A and test B, respectively. For test B (which always returns negative), $P(T_B|D) = 0$ and $P(T_B^c|D^c) = 1$, so the success rate is $P(\text{correct}_B) = P(T_B^c|D^c)P(D^c) + P(T_B|D)P(D) = 1 \times 0.99 + 0 = 0.99$. For test A, the success rate is $P(\text{correct}_A) = P(T_A^c|D^c)P(D^c) + P(T_A|D)P(D) = 0.95 \times 0.99 + 0.95 \times 0.01 = 0.95$. Company B's claim is mathematically true. However, test A is still useful because it provides new information (by **Bayes' rule**, a positive test increases the posterior probability of having the disease), whereas test B provides zero information. For a new test to beat B's $0.99$ success rate, if sensitivity and specificity are equal to $x$, we need $x(0.01) + x(0.99) > 0.99 \implies x > 0.99$. If sensitivity is 1, $1(0.01) + \text{specificity}(0.99) > 0.99 \implies \text{specificity} > \frac{0.98}{0.99}$. If specificity is 1, $\text{sensitivity}(0.01) + 1(0.99) > 0.99 \implies \text{sensitivity} > 0$.
> > 
> > **Answer.** (a) Yes, the claim is true ($0.99 > 0.95$). (b) Test A 
provides actual information to update beliefs. (c) If sens=spec, it must be $> 
0.99$. If sens=1, spec must be $> \frac{98}{99}$. If spec=1, sens must be $> 
0$. ✓

> [!example] Exercise 14 — Alarms and Burglaries
> **Problem.** Consider the following scenario, from Tversky and Kahneman [27]: Let A be the event that before the end of next year, Peter will have installed a burglar alarm system in his home. Let B denote the event that Peter's home will be burglarized before the end of next year. (a) Intuitively, which do you think is bigger, P(A|B) or P(A|$B^c$)? Explain your intuition. (b) Intuitively, which do you think is bigger, P(B|A) or P(B|$A^c$)? Explain your intuition. (c) Show that for any events A and B (with probabilities not equal to 0 or 1), the inequality P(A|B) > P(A|$B^c$) is equivalent to P(B|A) > P(B|$A^c$). (d) Tversky and Kahneman report that 131 out of 162 people whom they posed (a) and (b) to said that P(A|B) > P(A|$B^c$) and P(B|A) < P(B|$A^c$). What is a plausible explanation for why this was such a popular opinion despite (c) showing that it is impossible for these inequalities both to hold?
> 
> > [!success]- Click to reveal solution
> > Let $A$ be installing an alarm and $B$ be a burglary occurring. Intuitively, experiencing a burglary motivates installing an alarm, so $P(A|B) > P(A|B^c)$. Conversely, an alarm deters burglaries, so $P(B|A) < P(B|A^c)$. To show equivalence, apply the **definition of conditional probability** to the first inequality: $\frac{P(A \cap B)}{P(B)} > \frac{P(A \cap B^c)}{P(B^c)}$. Substitute $P(A \cap B^c) = P(A) - P(A \cap B)$ and cross-multiply to get $P(A \cap B) > P(A)P(B)$. Because this resulting inequality is symmetric, applying the exact same algebraic steps in reverse proves it is strictly equivalent to $P(B|A) > P(B|A^c)$. The cognitive contradiction happens because people confuse conditional probability (which reflects evidence and goes symmetrically in both directions) with causality (the alarm prevents burglary).
> > 
> > **Answer.** (a) $P(A|B) > P(A|B^c)$ due to motivation from a 
burglary. (b) $P(B|A) < P(B|A^c)$ due to the deterrence of the alarm. (c) Both 
inequalities algebraically reduce to $P(A \cap B) > P(A)P(B)$, proving 
equivalence. (d) People mistakenly confuse conditional probabilities with 
causal relationships. ✓

> [!example] Exercise 15 — Happiest Evidence
> **Problem.** Let A and B be events with 0 < P(A ∩B) < P(A) < P(B) < P(A ∪B) < 1. You are hoping that both A and B occurred. Which of the following pieces of information would you be happiest to observe: that A occurred, that B occurred, or that A ∪B occurred?
> 
> > [!success]- Click to reveal solution
> > You want to maximize the posterior probability of the intersection, $P(A \cap B | E)$, where $E$ is the observed evidence. Using the **definition of conditional probability**, we substitute the three possible pieces of evidence: $A$, $B$, or $A \cup B$. $P(A \cap B | A) = \frac{P(A \cap B)}{P(A)}$ $P(A \cap B | B) = \frac{P(A \cap B)}{P(B)}$ $P(A \cap B | A \cup B) = \frac{P(A \cap B)}{P(A \cup B)}$ Since the numerators are identical, the largest fraction is the one with the smallest denominator. We are given $P(A) < P(B) < P(A \cup B)$.
> > 
> > **Answer.** You would be happiest to observe that $A$ occurred. ✓

> [!example] Exercise 16 — Conditioning Cuts Both Ways
> **Problem.** Show that P(A|B) ≤P(A) implies P(A|$B^c$) ≥P(A), and give an intuitive explanation of why this makes sense.
> 
> > [!success]- Click to reveal solution
> > Use the **Law of Total Probability**: $P(A) = P(A|B)P(B) + P(A|B^c)P(B^c)$. We can rewrite the left side $P(A)$ as $P(A)P(B) + P(A)P(B^c)$. Setting these equal gives $P(A)P(B) + P(A)P(B^c) = P(A|B)P(B) + P(A|B^c)P(B^c)$. Rearranging the terms yields $P(B^c)(P(A|B^c) - P(A)) = P(B)(P(A) - P(A|B))$. Since we are given $P(A|B) \leq P(A)$, the right side is non-negative. Because $P(B^c)$ is a non-negative probability, the factor $(P(A|B^c) - P(A))$ must also be non-negative, meaning $P(A|B^c) \geq P(A)$. Intuitively, $B$ and $B^c$ partition the sample space. Since the unconditional probability $P(A)$ is exactly the weighted average of the conditional probabilities, if one condition ($B$) pulls the average down, the other condition ($B^c$) must pull it up to maintain balance.
> > 
> > **Answer.** $P(A|B^c) \geq P(A)$. Intuitively, the unconditional 
probability is a weighted average; if $B$ decreases the likelihood of $A$, its 
complement $B^c$ must increase it. ✓

> [!example] Exercise 17 — Probabilistic Contrapositive
> **Problem.** In deterministic logic, the statement "A implies B" is equivalent to its contrapositive, "not B implies not A". In this problem we will consider analogous statements in probability, the logic of uncertainty. Let A and B be events with probabilities not equal to 0 or 1. (a) Show that if P(B|A) = 1, then P($A^c$|$B^c$) = 1. Hint: Apply Bayes' rule and LOTP. (b) Show however that the result in (a) does not hold in general if = is replaced by ≈. In particular, find an example where P(B|A) is very close to 1 but P($A^c$|$B^c$) is very close to 0. Hint: What happens if A and B are independent?
> 
> > [!success]- Click to reveal solution
> > Part (a): Assume $P(B|A) = 1$. By the **definition of conditional probability**, $P(A \cap B) = P(A)$. This implies $P(A \cap B^c) = P(A) - P(A \cap B) = 0$. By definition, $P(A^c|B^c) = \frac{P(A^c \cap B^c)}{P(B^c)}$. Using set theory, $B^c = (A \cap B^c) \cup (A^c \cap B^c)$. Thus, $P(B^c) = P(A \cap B^c) + P(A^c \cap B^c) = 0 + P(A^c \cap B^c)$. Substituting this into the fraction yields $P(A^c|B^c) = \frac{P(B^c)}{P(B^c)} = 1$.
> > Part (b): Suppose $A$ and $B$ are unconditionally **independent** events, both with probability $0.999$. Then $P(B|A) = P(B) = 0.999 \approx 1$. However, $P(A^c|B^c) = P(A^c) = 0.001 \approx 0$.
> > 
> > **Answer.** (a) $P(A^c \cap B^c) = P(B^c) - P(A \cap B^c) = P(B^c) - 
0 = P(B^c)$, so $P(A^c|B^c) = 1$. (b) Example: $A$ and $B$ are independent with
$P(A) = 0.999$ and $P(B) = 0.999$. ✓

> [!example] Exercise 18 — Cromwell's Rule
> **Problem.** Show that if P(A) = 1, then P(A|B) = 1 for any B with P(B) > 0. Intuitively, this says that if someone dogmatically believes something with absolute certainty, then no amount of evidence will change their mind. The principle of avoiding assigning probabilities of 0 or 1 to any event (except for mathematical certainties) was named Cromwell's rule by the statistician Dennis Lindley, due to Cromwell saying to the Church of Scotland, "Think it possible you may be mistaken." Hint: Write P(B) = P(B ∩A) + P(B ∩$A^c$), and then show that P(B ∩$A^c$) = 0.
> 
> > [!success]- Click to reveal solution
> > Use the **Law of Total Probability** (in its intersection form) to write $P(B) = P(B \cap A) + P(B \cap A^c)$. Because $P(A) = 1$, the complement rule states $P(A^c) = 0$. Since the event $B \cap A^c$ is a subset of $A^c$, its probability is strictly bounded: $0 \leq P(B \cap A^c) \leq P(A^c) = 0$. Therefore, $P(B \cap A^c) = 0$. Substituting this back gives $P(B) = P(B \cap A)$. Applying the **definition of conditional probability** yields $P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{P(B)}{P(B)} = 1$.
> > 
> > **Answer.** $P(B) = P(A \cap B) + P(A^c \cap B) = P(A \cap B) + 0$, 
so $P(A|B) = \frac{P(A \cap B)}{P(B)} = 1$. ✓

> [!example] Exercise 19 — Sherlock Holmes
> **Problem.** Explain the following Sherlock Holmes saying in terms of conditional probability, carefully distinguishing between prior and posterior probabilities: "It is an old maxim of mine that when you have excluded the impossible, whatever remains, however improbable, must be the truth."
> 
> > [!success]- Click to reveal solution
> > Let $T$ represent the true theory, which has a very small, but non-zero, prior probability $P(T) > 0$. Let $I_1, I_2, \dots, I_n$ be the other impossible theories. Let $E$ be the new evidence that excludes all theories except $T$. Because $E$ eliminates the others, $P(E|I_k) = 0$ for all $k$. By **Bayes' rule** and expanding the denominator with the **Law of Total Probability**, the posterior probability is $P(T|E) = \frac{P(E|T)P(T)}{P(E|T)P(T) + \sum P(E|I_k)P(I_k)}$. Since all terms in the summation are exactly $0$, this fraction simplifies to $\frac{P(E|T)P(T)}{P(E|T)P(T)} = 1$.
> > 
> > **Answer.** By Bayes' rule and LOTP, eliminating all other hypotheses
forces their likelihoods $P(E|I_k) = 0$. The posterior probability $P(T|E)$ 
becomes $\frac{P(E|T)P(T)}{P(E|T)P(T) + 0} = 1$. ✓

> [!example] Exercise 20 — Jacks and Queens
> **Problem.** The Jack of Spades (with cider), Jack of Hearts (with tarts), Queen of Spades (with a wink), and Queen of Hearts (without tarts) are taken from a deck of cards. These four cards are shuffled, and then two are dealt. Note: Literary references to cider, tarts, and winks do not need to be considered when solving this problem. (a) Find the probability that both of these two cards are queens, given that the first card dealt is a queen. (b) Find the probability that both are queens, given that at least one is a queen. (c) Find the probability that both are queens, given that one is the Queen of Hearts.
> 
> > [!success]- Click to reveal solution
> > Let $Q_1$ be the event that the first card is a Queen, $Q_2$ be the event that the second card is a Queen, and $A$ be the event that at least one is a Queen. Let $H$ be the event that the Queen of Hearts is drawn. (a) Using the **definition of conditional probability** to restrict the sample space: Given $Q_1$, exactly 3 cards remain in the deck, and only 1 of them is a Queen. (b) $P(Q_1 \cap Q_2 | A) = \frac{P(Q_1 \cap Q_2 \cap A)}{P(A)}$. Since $Q_1 \cap Q_2$ implies $A$, the numerator is $P(Q_1 \cap Q_2) = \frac{\binom{2}{2}}{\binom{4}{2}} = 1/6$. The denominator is $1 - P(\text{both Jacks}) = 1 - 1/6 = 5/6$. The fraction is $\frac{1/6}{5/6}$. (c) $P(Q_1 \cap Q_2 | H) = \frac{P(Q_1 \cap Q_2 \cap H)}{P(H)}$. The intersection means drawing both Queens, one of which is $Q_H$, which is just the single outcome $\{Q_S, Q_H\}$ with probability $1/6$. The denominator is $P(H) = \frac{3}{6} = 1/2$. The fraction is $\frac{1/6}{1/2}$.
> > 
> > **Answer.** (a) $\frac{1}{3}$; (b) $\frac{1}{5}$; (c) $\frac{1}{3}$. ✓

> [!example] Exercise 21 — Three Coins and Slips
> **Problem.** A fair coin is flipped 3 times. The toss results are recorded on separate slips of paper (writing "H" if Heads and "T" if Tails), and the 3 slips of paper are thrown into a hat. (a) Find the probability that all 3 tosses landed Heads, given that at least 2 were Heads. (b) Two of the slips of paper are randomly drawn from the hat, and both show the letter H. Given this information, what is the probability that all 3 tosses landed Heads?
> 
> > [!success]- Click to reveal solution
> > Let $H_k$ be the event of exactly $k$ Heads. (a) Let $B$ be at least 2 Heads ($H_2 \cup H_3$). By the **definition of conditional probability**, $P(H_3 | B) = \frac{P(H_3 \cap B)}{P(B)} = \frac{P(H_3)}{P(H_3) + P(H_2)} = \frac{1/8}{1/8 + 3/8}$. (b) Let $D$ be the event that two drawn slips are both Heads. We want $P(H_3|D)$. We evaluate the likelihoods: $P(D|H_3) = 1$, $P(D|H_2) = \frac{1}{3}$ (the probability of choosing the 2 H slips out of the 3 total slips), $P(D|H_1) = 0$, $P(D|H_0) = 0$. By **Bayes' rule** and the **Law of Total Probability**, $P(H_3|D) = \frac{P(D|H_3)P(H_3)}{P(D|H_3)P(H_3) + P(D|H_2)P(H_2)} = \frac{1 \times (1/8)}{1 \times (1/8) + (1/3) \times (3/8)} = \frac{1/8}{2/8}$.
> > 
> > **Answer.** (a) $\frac{1}{4}$; (b) $\frac{1}{2}$. ✓

> [!example] Exercise 22 — The Added Green Marble
> **Problem.** A bag contains one marble which is either green or blue, with equal probabilities. A green marble is put in the bag (so there are 2 marbles now), and then a random marble is taken out. The marble taken out is green. What is the probability that the remaining marble is also green?
> 
> > [!success]- Click to reveal solution
> > Let $G_0$ be the event that the initial marble is green, with prior $P(G_0) = \frac{1}{2}$ and $P(G_0^c) = \frac{1}{2}$. A green marble is added. Let $D_G$ be the event of drawing a green marble. The conditional probabilities are $P(D_G|G_0) = 1$ (the bag is $\{G,G\}$) and $P(D_G|G_0^c) = \frac{1}{2}$ (the bag is $\{B,G\}$). We want the probability that the remaining marble is green, which is equivalent to finding the probability that the initial marble was green (since the added one was green, whatever color we remove, the remaining one will match the original initial color). We use **Bayes' rule** and the **Law of Total Probability**: $P(G_0|D_G) = \frac{P(D_G|G_0)P(G_0)}{P(D_G|G_0)P(G_0) + P(D_G|G_0^c)P(G_0^c)} = \frac{1 \times (1/2)}{1 \times (1/2) + (1/2) \times (1/2)} = \frac{1/2}{3/4}$.
> > 
> > **Answer.** $\frac{2}{3}$. ✓

> [!example] Exercise 23 — Evidence That Lowers Guilt
> **Problem.** Let G be the event that a certain individual is guilty of a certain robbery. In gathering evidence, it is learned that an event $E_{1}$ occurred, and a little later it is also learned that another event $E_{2}$ also occurred. Is it possible that individually, these pieces of evidence increase the chance of guilt (so P(G|$E_{1}$) > P(G) and P(G|$E_{2}$) > P(G)), but together they decrease the chance of guilt (so P(G|$E_{1}$, $E_{2}$) < P(G))?
> 
> > [!success]- Click to reveal solution
> > By the **definition of conditional probability**, this is perfectly possible if the two pieces of evidence $E_1$ and $E_2$ are individually common among guilty people, but mutually exclusive specifically for the actual perpetrator. If $P(E_1 \cap E_2 | G) = 0$, then the posterior probability of guilt given both pieces of evidence combined must be $P(G | E_1 \cap E_2) = 0$, which is strictly less than $P(G)$.
> > 
> > **Answer.** Yes. If $E_1$ and $E_2$ are individually common among 
guilty people but mutually exclusive for the actual perpetrator, then $P(G|E_1 
\cap E_2) = 0 < P(G)$. ✓

> [!example] Exercise 24 — Union Simpson's Paradox
> **Problem.** Is it possible to have events $A_{1}$, $A_{2}$, B, C with P($A_{1}$|B) > P($A_{1}$|C) and P($A_{2}$|B) > P($A_{2}$|C), yet P($A_{1}$ ∪$A_{2}$|B) < P($A_{1}$ ∪$A_{2}$|C)? If so, find an example (with a "story" interpreting the events, as well as giving specific numbers); otherwise, show that it is impossible for this phenomenon to happen.
> 
> > [!success]- Click to reveal solution
> > This is a manifestation of Simpson's paradox involving the union of events. By the **inclusion-exclusion principle**, $P(A_1 \cup A_2 | E) = P(A_1|E) + P(A_2|E) - P(A_1 \cap A_2 | E)$. We can construct a scenario where the sum of the probabilities given $B$ is greater than the sum given $C$, but the intersection given $B$ is drastically larger than given $C$, forcing the overall union given $B$ to fall lower than the union given $C$. Consider a 9-sided die where $S=\{1,2,3,4,5,6,7,8,9\}$. Let $B = \{1, 2, 3, 4\}$ and $C = \{5, 6, 7, 8, 9\}$. Let $A_1 = \{1, 2, 5, 6\}$ and $A_2 = \{1, 2, 7, 8\}$. Conditioning on $B$: $P(A_1|B) = \frac{2}{4} = 0.5$ and $P(A_2|B) = \frac{2}{4} = 0.5$. $A_1 \cup A_2 \cap B = \{1, 2\}$, so $P(A_1 \cup A_2 | B) = \frac{2}{4} = 0.5$. Conditioning on $C$: $P(A_1|C) = \frac{2}{5} = 0.4$ and $P(A_2|C) = \frac{2}{5} = 0.4$. $A_1 \cup A_2 \cap C = \{5, 6, 7, 8\}$, so $P(A_1 \cup A_2 | C) = \frac{4}{5} = 0.8$. Thus, $P(A_1|B) > P(A_1|C)$ and $P(A_2|B) > P(A_2|C)$, but $P(A_1 \cup A_2|B) < P(A_1 \cup A_2|C)$.
> > 
> > **Answer.** Yes. Example: Let $S=\{1,2,3,4,5,6,7,8,9\}$, $B = \{1, 2,
3, 4\}$, $C = \{5, 6, 7, 8, 9\}$, $A_1 = \{1, 2, 5, 6\}$, $A_2 = \{1, 2, 7, 
8\}$. Then $0.5 > 0.4$ and $0.5 > 0.4$, but the union yields $0.5 < 0.8$. ✓

> [!example] Exercise 25 — Two Suspects, One Blood Type
> **Problem.** A crime is committed by one of two suspects, A and B. Initially, there is equal evidence against both of them. In further investigation at the crime scene, it is found that the guilty party had a blood type found in 10% of the population. Suspect A does match this blood type, whereas the blood type of Suspect B is unknown. (a) Given this new information, what is the probability that A is the guilty party? (b) Given this new information, what is the probability that B's blood type matches that found at the crime scene?
> 
> > [!success]- Click to reveal solution
> > Let $G_A$ and $G_B$ be the events that A is guilty and B is guilty, with prior probabilities $P(G_A) = 1/2$ and $P(G_B) = 1/2$. Let $M$ be the observed evidence that suspect A matches the guilty party's blood type (which has a 10% prevalence). If A is guilty, A perfectly matches his own blood type, so $P(M|G_A) = 1$. If B is guilty, A only matches the guilty blood type if A happens to be in the 10% of the population with that type, so $P(M|G_B) = 0.1$.
> > Part (a): We use **Bayes' rule** and the **Law of Total Probability**: $P(G_A|M) = \frac{P(M|G_A)P(G_A)}{P(M|G_A)P(G_A) + P(M|G_B)P(G_B)} = \frac{1 \times 0.5}{1 \times 0.5 + 0.1 \times 0.5} = \frac{1}{1.1}$.
> > Part (b): Let $T_B$ be the event B has the 10% blood type. We use the **Law of Total Probability with extra conditioning** on $M$: $P(T_B|M) = P(T_B|G_A, M)P(G_A|M) + P(T_B|G_B, M)P(G_B|M)$. If A is guilty, B's blood type is independent of the evidence, so $P(T_B|G_A, M) = 0.1$. If B is guilty, B absolutely must have the guilty blood type, so $P(T_B|G_B, M) = 1$. Substituting gives $0.1 \times \frac{10}{11} + 1 \times \frac{1}{11}$.
> > 
> > **Answer.** (a) $\frac{10}{11}$; (b) $\frac{2}{11}$. ✓

> [!example] Exercise 26 — Two Anti-Spam Programs
> **Problem.** To battle against spam, Bob installs two anti-spam programs. An email arrives, which is either legitimate (event L) or spam (event Lc), and which program j marks as legitimate (event $M_{j}$) or marks as spam (event $M_{j}^c$ ) for j ∈{1, 2}. Assume that 10% of Bob's email is legitimate and that the two programs are each "90% accurate" in the sense that P($M_{j}$|L) = P($M_{j}^c$ |Lc) = 9/10. Also assume that given whether an email is spam, the two programs' outputs are conditionally independent. (a) Find the probability that the email is legitimate, given that the 1st program marks it as legitimate (simplify). (b) Find the probability that the email is legitimate, given that both programs mark it as legitimate (simplify). (c) Bob runs the 1st program and $M_{1}$ occurs. He updates his probabilities and then runs the 2nd program. Let ˜P(A) = P(A|$M_{1}$) be the updated probability function after running the 1st program. Explain briefly in words whether or not ˜P(L|$M_{2}$) = P(L|$M_{1}$ ∩ $M_{2}$): is conditioning on $M_{1}$ ∩$M_{2}$ in one step equivalent to first conditioning on $M_{1}$, then updating probabilities, and then conditioning on $M_{2}$?
> 
> > [!success]- Click to reveal solution
> > Let $L$ be the event the email is legitimate ($P(L) = 0.1$, $P(L^c) = 0.9$). Let $M_1$ and $M_2$ be the events that the first and second programs mark it as legitimate. The accuracy is $P(M_j|L) = P(M_j^c|L^c) = 0.9$.
> > Part (a): By **Bayes' rule** and the **Law of Total Probability**, $P(L|M_1) = \frac{P(M_1|L)P(L)}{P(M_1|L)P(L) + P(M_1|L^c)P(L^c)} = \frac{0.9 \times 0.1}{0.9 \times 0.1 + 0.1 \times 0.9} = \frac{0.09}{0.18}$.
> > Part (b): By **conditional independence**, $P(M_1 \cap M_2 | L) = 0.9^2 = 0.81$, and $P(M_1 \cap M_2 | L^c) = 0.1^2 = 0.01$. Applying **Bayes' rule** again: $P(L|M_1 \cap M_2) = \frac{0.81 \times 0.1}{0.81 \times 0.1 + 0.01 \times 0.9} = \frac{0.081}{0.090}$.
> > Part (c): Yes, Bayesian updating is **coherent**. Updating sequentially on $M_1$ then $M_2$ is mathematically guaranteed to equal conditioning simultaneously on $M_1 \cap M_2$.
> > 
> > **Answer.** (a) $\frac{1}{2}$; (b) $\frac{9}{10}$; (c) Yes, because 
Bayesian updating is coherent. ✓

> [!example] Exercise 27 — Five Blood Types
> **Problem.** Suppose that there are 5 blood types in the population, named type 1 through type 5, with probabilities $p_{1}$, $p_{2}$, . . . , $p_{5}$. A crime was committed by two individuals. A suspect, who has blood type 1, has prior probability p of being guilty. At the crime scene, blood evidence is collected, which shows that one of the criminals has type 1 and the other has type 2. Find the posterior probability that the suspect is guilty, given the evidence. Does the evidence make it more likely or less likely that the suspect is guilty, or does this depend on the values of the parameters p, $p_{1}$, . . . , $p_{5}$? If it depends on these values, give a simple criterion for when the evidence makes it more likely that the suspect is guilty.
> 
> > [!success]- Click to reveal solution
> > Let $G$ be the event the suspect is guilty ($P(G) = p$). Let $E$ be the evidence that the two criminals have types 1 and 2. We know the suspect is type 1. If the suspect is guilty, the second criminal must have type 2, which occurs with probability $p_2$ (assuming independence). So $P(E|G) = p_2$. If the suspect is not guilty, the two actual criminals must randomly have types 1 and 2, which occurs in two permutations (criminal A is type 1 and criminal B is type 2, or vice versa), so $P(E|G^c) = 2p_1p_2$. Using **Bayes' rule** and the **Law of Total Probability**: $P(G|E) = \frac{P(E|G)P(G)}{P(E|G)P(G) + P(E|G^c)P(G^c)} = \frac{p_2 p}{p_2 p + 2p_1p_2(1-p)}$. Simplifying drops $p_2$. To see if guilt is more likely, set $P(G|E) > p$, which reduces to $p + 2p_1(1-p) < 1$, and further simplifies to $2p_1 < 1$.
> > 
> > **Answer.** $\frac{p}{p + 2p_1(1-p)}$. It makes guilt more likely if 
and only if $p_1 < \frac{1}{2}$. ✓

> [!example] Exercise 28 — Sensitivity vs. Specificity
> **Problem.** Fred has just tested positive for a certain disease. (a) Given this information, find the posterior odds that he has the disease, in terms of the prior odds, the sensitivity of the test, and the specificity of the test. (b) Not surprisingly, Fred is much more interested in P(have disease|test positive), known as the positive predictive value, than in the sensitivity P(test positive|have disease). A handy rule of thumb in biostatistics and epidemiology is as follows: For a rare disease and a reasonably good test, specificity matters much more than sensitivity in determining the positive predictive value. Explain intuitively why this rule of thumb works. For this part you can make up some specific numbers and interpret probabilities in a frequentist way as proportions in a large population, e.g., assume the disease afflicts 1% of a population of 10000 people and then consider various possibilities for the sensitivity and specificity.
> 
> > [!success]- Click to reveal solution
> > Part (a): Use the **odds form of Bayes' rule**. The posterior odds $\frac{P(D|T)}{P(D^c|T)} = \frac{P(T|D)}{P(T|D^c)} \frac{P(D)}{P(D^c)}$. The true positive rate $P(T|D)$ is the sensitivity. The false positive rate $P(T|D^c)$ is $1 - \text{specificity}$.
> > Part (b): Using the **frequentist interpretation**, imagine a large population. Because the disease is rare, the vast majority of people are healthy. Even a very small false positive rate ($1 - \text{specificity}$) applied to this massive pool of healthy people yields a huge number of false positives. These false positives easily overwhelm the small number of true positives (sensitivity). Therefore, minimizing the false positive rate (i.e., maximizing specificity) is essential for keeping the denominator of the positive predictive value from exploding.
> > 
> > **Answer.** (a) $\text{Posterior odds} = \text{Prior odds} \times 
\frac{\text{Sensitivity}}{1 - \text{Specificity}}$. (b) Because the healthy 
population is much larger than the diseased population, a slight drop in 
specificity generates far more false positives than the total possible number 
of true positives generated by sensitivity. ✓

> [!example] Exercise 29 — A Girl with Characteristic C
> **Problem.** A family has two children. Let C be a characteristic that a child can have, and assume that each child has characteristic C with probability p, independently of each other and of gender. For example, C could be the characteristic "born in winter" as in Example 2.2.7. Under the assumptions of Example 2.2.5, show that the probability that both children are girls given that at least one is a girl with characteristic C is 2−p 4−p. Note that this is 1/3 if p = 1 (agreeing with the first part of Example 2.2.5) and approaches 1/2 from below as p →0 (agreeing with Example 2.2.7).
> 
> > [!success]- Click to reveal solution
> > Let $GG$ be the event of both girls (prob 1/4) and $E$ be the event that at least one is a girl with characteristic $C$. We use the **definition of conditional probability**: $P(GG|E) = \frac{P(GG \cap E)}{P(E)}$. To find $P(E)$, we use the complement $1 - P(E^c)$, where $E^c$ is neither child is a girl with $C$. The probability a specific child is NOT a girl with $C$ is $1 - P(\text{Girl})P(C) = 1 - p/2$. By **independence**, $P(E^c) = (1 - p/2)^2$, so $P(E) = 1 - (1 - p/2)^2 = \frac{4p - p^2}{4}$. To find $P(GG \cap E)$, we condition on $GG$. Given both are girls, the probability neither has $C$ is $(1-p)^2$. Thus, the probability at least one has $C$ is $1 - (1-p)^2 = 2p - p^2$. So $P(GG \cap E) = \frac{1}{4}(2p - p^2)$. Dividing the numerator by the denominator completes the proof.
> > 
> > **Answer.** $\frac{(2p - p^2)/4}{(4p - p^2)/4} = 
\frac{p(2-p)}{p(4-p)} = \frac{2-p}{4-p}$. ✓

## Independence and conditional independence (Exercises 30–38)

> [!example] Exercise 30 — Three Children's Ages
> **Problem.** A family has 3 children, creatively named A, B, and C. (a) Discuss intuitively (but clearly) whether the event "A is older than B" is independent of the event "A is older than C". (b) Find the probability that A is older than B, given that A is older than C.
> 
> > [!success]- Click to reveal solution
> > Let $E_1$ be the event $A > B$, and $E_2$ be $A > C$.
> > Part (a): Intuitively, knowing that A is older than C makes A more likely to be the oldest overall, which consequently makes it more likely that A is also older than B. Thus, they are positively correlated and not independent.
> > Part (b): Using the **definition of conditional probability**: $P(E_1|E_2) = \frac{P(E_1 \cap E_2)}{P(E_2)}$. The intersection $E_1 \cap E_2$ means A is older than both B and C (A is the oldest). There are $3! = 6$ equally likely birth orders. A is the oldest in exactly 2 permutations (ABC, ACB), so $P(E_1 \cap E_2) = \frac{2}{6} = \frac{1}{3}$. The event $E_2$ ($A>C$) happens in exactly half the permutations by symmetry, so $P(E_2) = \frac{1}{2}$. The conditional probability is $\frac{1/3}{1/2}$.
> > 
> > **Answer.** (a) Not independent; knowing $A>C$ increases the chance 
that A is the oldest overall, which increases the chance that $A>B$. (b) 
$\frac{2}{3}$. ✓

> [!example] Exercise 31 — Independent of Itself
> **Problem.** Is it possible that an event is independent of itself? If so, when is this the case?
> 
> > [!success]- Click to reveal solution
> > By the **definition of independence**, an event $A$ is independent of itself if $P(A \cap A) = P(A)P(A)$. Since the intersection of a set with itself is just the set itself, $A \cap A = A$. Therefore, the equation simplifies to $P(A) = P(A)^2$. The only real numbers that satisfy $x = x^2$ are 0 and 1.
> > 
> > **Answer.** Yes, it is possible if and only if $P(A) = 0$ or $P(A) = 
1$. ✓

> [!example] Exercise 32 — Efron's Nontransitive Dice
> **Problem.** Consider four nonstandard dice (the Efron dice), whose sides are labeled as follows (the 6 sides on each die are equally likely). A: 4, 4, 4, 4, 0, 0 B: 3, 3, 3, 3, 3, 3 C: 6, 6, 2, 2, 2, 2 D: 5, 5, 5, 1, 1, 1 These four dice are each rolled once. Let A be the result for die A, B be the result for die B, etc. (a) Find P(A > B), P(B > C), P(C > D), and P(D > A). (b) Is the event A > B independent of the event B > C? Is the event B > C independent of the event C > D? Explain.
> 
> > [!success]- Click to reveal solution
> > Part (a): We evaluate all match-ups using **LOTP** and **independence** of separate rolls. A>B happens when A rolls 4 (prob 4/6), since B always rolls 3. B>C happens when C rolls 2 (prob 4/6), since B always rolls 3. C>D happens if C=6 (prob 2/6), OR if C=2 and D=1 (prob 4/6 * 3/6 = 2/6), total 4/6. D>A happens if D=5 (prob 3/6), OR if D=1 and A=0 (prob 3/6 * 2/6 = 1/6), total 4/6.
> > Part (b): Check for **independence**. Event $A>B$ strictly depends on die A. Event $B>C$ strictly depends on die C. Since dice A and C are rolled independently, the events are independent. However, $B>C$ depends on die C (requires C=2). Event $C>D$ depends on C and D. Using the **definition of conditional probability**, $P(C>D | B>C)$ means finding the probability C>D given C=2. If C=2, then C>D only happens if D=1, which has probability 1/2. Since $P(C>D|B>C) = 1/2$ is not equal to the unconditional $P(C>D) = 2/3$, the events $B>C$ and $C>D$ are dependent.
> > 
> > **Answer.** (a) $P(A>B) = \frac{2}{3}$, $P(B>C) = \frac{2}{3}$, 
$P(C>D) = \frac{2}{3}$, $P(D>A) = \frac{2}{3}$. (b) $A>B$ and $B>C$ are 
independent. $B>C$ and $C>D$ are not independent. ✓

> [!example] Exercise 33 — Alice, Bob, and 100 Friends
> **Problem.** Alice, Bob, and 100 other people live in a small town. Let C be the set consisting of the 100 other people, let A be the set of people in C who are friends with Alice, and let B be the set of people in C who are friends with Bob. Suppose that for each person in C, Alice is friends with that person with probability 1/2, and likewise for Bob, with all of these friendship statuses independent. (a) Let D ⊆C. Find P(A = D). (b) Find P(A ⊆B). (c) Find P(A ∪B = C).
> 
> > [!success]- Click to reveal solution
> > Let $x$ represent any of the 100 people in $C$. $P(x \in A) = 1/2$ and $P(x \in B) = 1/2$, and all friendships are unconditionally **independent**.
> > Part (a): For $A = D$, every person $x$ must perfectly match the inclusion/exclusion of set $D$. The probability of matching for any single person is $1/2$. By independence across 100 people, the probability is $(1/2)^{100}$.
> > Part (b): For $A \subseteq B$, it is forbidden for any person to be in $A$ but not in $B$. The probability of this forbidden state for one person is $P(x \in A)P(x \notin B) = (1/2)(1/2) = 1/4$. Thus, the probability a person is valid is $3/4$. By independence, $P(A \subseteq B) = (3/4)^{100}$.
> > Part (c): For $A \cup B = C$, it is forbidden for any person to be in neither $A$ nor $B$. The probability of this forbidden state is $P(x \notin A)P(x \notin B) = (1/2)(1/2) = 1/4$. Thus, the probability a person is valid is $3/4$. By independence, $P(A \cup B = C) = (3/4)^{100}$.
> > 
> > **Answer.** (a) $(\frac{1}{2})^{100}$; (b) $(\frac{3}{4})^{100}$; (c)
$(\frac{3}{4})^{100}$. ✓

> [!example] Exercise 34 — Good and Bad Drivers
> **Problem.** Suppose that there are two types of drivers: good drivers and bad drivers. Let G be the event that a certain man is a good driver, A be the event that he gets into a car accident next year, and B be the event that he gets into a car accident the following year. Let P(G) = g and P(A|G) = P(B|G) = $p_{1}$, P(A|$G^c$) = P(B|$G^c$) = $p_{2}$, with $p_{1}$ < $p_{2}$. Suppose that given the information of whether or not the man is a good driver, A and B are independent (for simplicity and to avoid being morbid, assume that the accidents being considered are minor and wouldn't make the man unable to drive). (a) Explain intuitively whether or not A and B are independent. (b) Find P(G|$A^c$). (c) Find P(B|$A^c$).
> 
> > [!success]- Click to reveal solution
> > Part (a): Intuitively, observing that a driver did not have an accident ($A^c$) acts as evidence that they are a good driver, which lowers the probability of an accident next year ($B$). Thus, $A$ and $B$ are unconditionally dependent.
> > Part (b): Using **Bayes' rule** and the **Law of Total Probability**: $P(G|A^c) = \frac{P(A^c|G)P(G)}{P(A^c|G)P(G) + P(A^c|G^c)P(G^c)} = \frac{(1-p_1)g}{(1-p_1)g + (1-p_2)(1-g)}$.
> > Part (c): Using the **Law of Total Probability with extra conditioning** on $G$: $P(B|A^c) = P(B|G, A^c)P(G|A^c) + P(B|G^c, A^c)P(G^c|A^c)$. Applying **conditional independence**, $P(B|G, A^c) = P(B|G) = p_1$ and $P(B|G^c, A^c) = p_2$. Substituting these and the answer from (b) yields the final equation.
> > 
> > **Answer.** (a) No, they are not independent, as observing $A$ 
updates our belief about $G$, which changes our prediction for $B$. (b) 
$\frac{(1-p_1)g}{(1-p_1)g + (1-p_2)(1-g)}$; (c) $\frac{p_1(1-p_1)g + 
p_2(1-p_2)(1-g)}{(1-p_1)g + (1-p_2)(1-g)}$. ✓

> [!example] Exercise 35 — Two Games of Chess
> **Problem.** You are going to play 2 games of chess with an opponent whom you have never played against before (for the sake of this problem). Your opponent is equally likely to be a beginner, intermediate, or a master. Depending on which, your chances of winning an individual game are 90%, 50%, or 30%, respectively. (a) What is your probability of winning the first game? (b) Congratulations: you won the first game! Given this information, what is the probability that you will also win the second game (assume that, given the skill level of your opponent, the outcomes of the games are independent)? (c) Explain the distinction between assuming that the outcomes of the games are independent and assuming that they are conditionally independent given the opponent's skill level. Which of these assumptions seems more reasonable, and why?
> 
> > [!success]- Click to reveal solution
> > Let $B, I, M$ be the opponent's skill level (each prior is $1/3$). Let $W_1$ and $W_2$ be winning game 1 and 2.
> > Part (a): By the **Law of Total Probability**, $P(W_1) = P(W_1|B)P(B) + P(W_1|I)P(I) + P(W_1|M)P(M) = 0.9(1/3) + 0.5(1/3) + 0.3(1/3) = \frac{1.7}{3} = \frac{17}{30}$.
> > Part (b): Using the **definition of conditional probability**, $P(W_2|W_1) = \frac{P(W_1 \cap W_2)}{P(W_1)}$. The numerator requires **LOTP** and **conditional independence**: $P(W_1 \cap W_2) = (0.9)^2(1/3) + (0.5)^2(1/3) + (0.3)^2(1/3) = \frac{0.81 + 0.25 + 0.09}{3} = \frac{1.15}{3} = \frac{115}{300}$. Dividing this by $\frac{170}{300}$ gives $\frac{115}{170}$.
> > Part (c): Unconditional independence implies the first game tells us nothing about the second, which is false because winning is evidence that the opponent is a beginner. Conditional independence implies that if we definitively knew the opponent's skill level, the outcomes of the two games would not affect each other.
> > 
> > **Answer.** (a) $\frac{17}{30}$; (b) $\frac{23}{34}$; (c) Conditional
independence is more reasonable; unconditional independence falsely assumes we 
learn nothing about the opponent's hidden skill from the first game. ✓

> [!example] Exercise 36 — Baseball or Math (Admissions)
> **Problem.** (a) Suppose that in the population of college applicants, being good at baseball is independent of having a good math score on a certain standardized test (with respect to some measure of "good"). A certain college has a simple admissions procedure: admit an applicant if and only if the applicant is good at baseball or has a good math score on the test. Give an intuitive explanation of why it makes sense that among students that the college admits, having a good math score is negatively associated with being good at baseball, i.e., conditioning on having a good math score decreases the chance of being good at baseball. (b) Show that if A and B are independent and C = A∪B, then A and B are conditionally dependent given C (as long as P(A ∩B) > 0 and P(A ∪B) < 1), with P(A|B, C) < P(A|C). This phenomenon is known as Berkson's paradox, especially in the context of admissions to a school, hospital, etc.
> 
> > [!success]- Click to reveal solution
> > Let $A$ be good at baseball, $B$ be good at math, and $C = A \cup B$ be the event of being admitted. $A$ and $B$ are unconditionally independent.
> > Part (a): Intuitively, if we restrict our sample space only to admitted students, anyone who is terrible at math MUST be good at baseball (to explain their admission). A good math score relieves the necessity of a good baseball score, creating a negative association between the two within the admitted group.
> > Part (b): Using the **definition of conditional probability** and $B \subset C$, $P(A|B,C) = \frac{P(A \cap B)}{P(B)}$. By **independence**, this perfectly reduces to $P(A)$. Now evaluate $P(A|C) = \frac{P(A \cap C)}{P(C)} = \frac{P(A)}{P(A \cup B)}$. Because $P(A \cup B) < 1$ and $P(A) > 0$, dividing $P(A)$ by a fraction less than 1 results in a number larger than $P(A)$. Thus, $P(A|B,C) = P(A) < P(A|C)$.
> > 
> > **Answer.** (a) Knowing an admitted student lacks math skills 
guarantees they have baseball skills; this trade-off creates negative 
association. (b) Because $P(A|B,C) = \frac{P(A \cap B)}{P(B)} = P(A)$ and 
$P(A|C) = \frac{P(A)}{P(A \cup B)}$, the inequality $P(A|B,C) < P(A|C)$ 
mathematically holds since $P(A \cup B) < 1$. ✓

> [!example] Exercise 37 — Two Diseases, One Symptom
> **Problem.** Two different diseases cause a certain weird symptom; anyone who has either or both of these diseases will experience the symptom. Let $D_{1}$ be the event of having the first disease, $D_{2}$ be the event of having the second disease, and W be the event of having the weird symptom. Suppose that $D_{1}$ and $D_{2}$ are independent with P($D_{j}$) = $p_{j}$, and that a person with neither of these diseases will have the weird symptom with probability $w_{0}$. Let $q_{j}$ = 1 −$p_{j}$, and assume that 0 < $p_{j}$ < 1. (a) Find P(W). (b) Find P($D_{1}$|W), P($D_{2}$|W), and P($D_{1}$, $D_{2}$|W). (c) Determine algebraically whether or not $D_{1}$ and $D_{2}$ are conditionally independent given W. (d) Suppose for this part only that $w_{0}$ = 0. Give a clear, convincing intuitive explanation in words of whether $D_{1}$ and $D_{2}$ are conditionally independent given W.
> 
> > [!success]- Click to reveal solution
> > Let $D_1$ and $D_2$ be the events of having the diseases, with $P(D_j) = p_j$ and $P(D_j^c) = q_j$. Let $W$ be the symptom. We are given $P(W|D_1 \cup D_2) = 1$ and $P(W|D_1^c \cap D_2^c) = w_0$. $D_1$ and $D_2$ are **independent**. (a) Using the **Law of Total Probability**: $P(W) = P(W|D_1 \cup D_2)P(D_1 \cup D_2) + P(W|D_1^c \cap D_2^c)P(D_1^c \cap D_2^c) = 1(1 - q_1 q_2) + w_0 q_1 q_2$. (b) Using **Bayes' rule**: $P(D_1|W) = \frac{P(W|D_1)P(D_1)}{P(W)} = \frac{1 \cdot p_1}{P(W)}$. Similarly, $P(D_2|W) = \frac{p_2}{P(W)}$. For the intersection, $P(D_1, D_2|W) = \frac{P(W|D_1 \cap D_2)P(D_1 \cap D_2)}{P(W)} = \frac{1 \cdot p_1 p_2}{P(W)}$. (c) Check for **conditional independence**: $P(D_1,D_2|W) = \frac{p_1 p_2}{P(W)}$, whereas $P(D_1|W)P(D_2|W) = \frac{p_1 p_2}{(P(W))^2}$. Because $P(W) < 1$, these are not equal. (d) If $w_0 = 0$, anyone with the symptom must have at least one of the diseases. If we know a person has $W$, and we learn they do not have $D_1$, they absolutely must have $D_2$. Thus, learning about $D_1$ gives information about $D_2$.
> > 
> > **Answer.** (a) $1 - q_1 q_2 + w_0 q_1 q_2$; (b) $\frac{p_1}{P(W)}$, 
$\frac{p_2}{P(W)}$, $\frac{p_1 p_2}{P(W)}$; (c) Not conditionally independent; 
(d) Not conditionally independent, because knowing $W$ and $D_1^c$ guarantees 
$D_2$. ✓

> [!example] Exercise 38 — Naive Bayes Spam Filter
> **Problem.** We want to design a spam filter for email. As described in Exercise 1, a major strategy is to find phrases that are much more likely to appear in a spam email than in a nonspam email. In that exercise, we only consider one such phrase: "free money". More realistically, suppose that we have created a list of 100 words or phrases that are much more likely to be used in spam than in non-spam. Let $W_{j}$ be the event that an email contains the jth word or phrase on the list. Let p = P(spam), $p_{j}$ = P($W_{j}$|spam), $r_{j}$ = P($W_{j}$|not spam), where "spam" is shorthand for the event that the email is spam. Assume that $W_{1}$, . . . , $W_{100}$ are conditionally independent given that the email is spam, and conditionally independent given that it is not spam. A method for classifying emails (or other objects) based on this kind of assumption is called a naive Bayes classifier. (Here "naive" refers to the fact that the conditional independence is a strong assumption, not to Bayes being naive. The assumption may or may not be realistic, but naive Bayes classifiers sometimes work well in practice even if the assumption is not realistic.) Under this assumption we know, for example, that P($W_{1}$, $W_{2}$, $W_{3}^c$ , $W_{4}^c$ , . . . , $W_{100}^c$|spam) = p1p2(1 −$p_{3}$)(1 −$p_{4}$) . . . (1 −$p_{100}$). Without the naive Bayes assumption, there would be vastly more statistical and computational difficulties since we would need to consider 2100 ≈1.3 × 1030 events of the form $A_{1}$ ∩$A_{2}$ · · · ∩$A_{100}$ with each $A_{j}$ equal to either $W_{j}$ or $W_{j}^c$ . A new email has just arrived, and it includes the 23rd, 64th, and 65th words or phrases on the list (but not the other 97). So we want to compute P(spam|$W_{1}^c$ , . . . , $W_{22}^c$, $W_{23}$, $W_{24}^c$, . . . , $W_{63}^c$, $W_{64}$, $W_{65}$, $W_{66}^c$, . . . , $W_{100}^c$). Note that we need to condition on all the evidence, not just the fact that $W_{23}$∩$W_{64}$∩$W_{65}$ occurred. Find the conditional probability that the new email is spam (in terms of p and the $p_{j}$ and $r_{j}$).
> 
> > [!success]- Click to reveal solution
> > Let $S$ be the event the email is spam, and $E$ be the evidence that exactly $W_{23}, W_{64}, W_{65}$ occur (and the other 97 do not). We use **Bayes' rule** and the **Law of Total Probability**. By the naive Bayes assumption of **conditional independence**, we calculate the likelihoods by multiplying the individual probabilities of each word's presence or absence: $P(E|S) = p_{23} p_{64} p_{65} \prod_{j \notin \{23,64,65\}} (1 - p_j)$ and $P(E|S^c) = r_{23} r_{64} r_{65} \prod_{j \notin \{23,64,65\}} (1 - r_j)$. Substitute these into Bayes' rule $P(S|E) = \frac{P(E|S)P(S)}{P(E|S)P(S) + P(E|S^c)P(S^c)}$.
> > 
> > **Answer.** $\frac{p \cdot p_{23} p_{64} p_{65} \prod_{j \notin 
\{23,64,65\}} (1 - p_j)}{p \cdot p_{23} p_{64} p_{65} \prod_{j \notin 
\{23,64,65\}} (1 - p_j) + (1-p) \cdot r_{23} r_{64} r_{65} \prod_{j \notin 
\{23,64,65\}} (1 - r_j)}$. ✓

## Monty Hall (Exercises 39–47)

> [!example] Exercise 39 — Seven-Door Monty Hall
> **Problem.** (a) Consider the following 7-door version of the Monty Hall problem. There are 7 doors, behind one of which there is a car (which you want), and behind the rest of which there are goats (which you don't want). Initially, all possibilities are equally likely for where the car is. You choose a door. Monty Hall then opens 3 goat doors, and offers you the option of switching to any of the remaining 3 doors. Assume that Monty Hall knows which door has the car, will always open 3 goat doors and offer the option of switching, and that Monty chooses with equal probabilities from all his choices of which goat doors to open. Should you switch? What is your probability of success if you switch to one of the remaining 3 doors? (b) Generalize the above to a Monty Hall problem where there are n ≥3 doors, of which Monty opens m goat doors, with 1 ≤m ≤n −2.
> 
> > [!success]- Click to reveal solution
> > Part (a): We use the **Law of Total Probability** by conditioning on whether the initial choice was correct. The chance of picking the car initially is $1/7$. If you picked the car, switching fails (probability $0$). If you picked a goat (probability $6/7$), the car is among the 6 unchosen doors. Monty opens 3 goats, leaving 3 unopened unchosen doors. Because Monty acts randomly among goats, the car is equally likely to be behind any of those remaining 3 doors. Switching to a random one gives a $1/3$ chance of success. $P(\text{Win}) = \frac{1}{7}(0) + \frac{6}{7}(\frac{1}{3}) = \frac{2}{7}$.
> > Part (b): Generalizing the above, the probability of initially picking a goat is $\frac{n-1}{n}$. The number of remaining unopened doors to switch to is $n - 1 - m$.
> > 
> > **Answer.** (a) Yes, you should switch; the probability of success is
$\frac{2}{7}$. (b) $\frac{n-1}{n(n - m - 1)}$. ✓

> [!example] Exercise 40 — Monty Prefers a Door
> **Problem.** Consider the Monty Hall problem, except that Monty enjoys opening door 2 more than he enjoys opening door 3, and if he has a choice between opening these two doors, he opens door 2 with probability p, where 1 2 ≤p ≤1. To recap: there are three doors, behind one of which there is a car (which you want), and behind the other two of which there are goats (which you don't want). Initially, all possibilities are equally likely for where the car is. You choose a door, which for concreteness we assume is door 1. Monty Hall then opens a door to reveal a goat, and offers you the option of switching. Assume that Monty Hall knows which door has the car, will always open a goat door and offer the option of switching, and as above assume that if Monty Hall has a choice between opening door 2 and door 3, he chooses door 2 with probability p (with 1 2 ≤p ≤1). (a) Find the unconditional probability that the strategy of always switching succeeds (unconditional in the sense that we do not condition on which of doors 2 or 3 Monty opens). (b) Find the probability that the strategy of always switching succeeds, given that Monty opens door 2. (c) Find the probability that the strategy of always switching succeeds, given that Monty opens door 3.
> 
> > [!success]- Click to reveal solution
> > Let $C_i$ be the car at door $i$, and $M_j$ be Monty opening door $j$. We assume the contestant picks door 1.
> > Part (a): By **LOTP**, the unconditional probability of winning by switching is still $2/3$, because you win exactly when the car is at door 2 or 3, which has a prior probability of $2/3$. Monty's preference only changes *which* door he opens when you pick the car, not whether switching wins.
> > Part (b): We want $P(C_3|M_2)$. Use **Bayes' rule**: $P(M_2|C_1) = p$, $P(M_2|C_2) = 0$, $P(M_2|C_3) = 1$. The denominator is $p(1/3) + 0(1/3) + 1(1/3) = \frac{p+1}{3}$. The numerator for $C_3$ is $1(1/3)$. Thus, $P(C_3|M_2) = \frac{1/3}{(p+1)/3} = \frac{1}{p+1}$.
> > Part (c): We want $P(C_2|M_3)$. By **Bayes' rule**: $P(M_3|C_1) = 1-p$, $P(M_3|C_2) = 1$, $P(M_3|C_3) = 0$. The denominator is $\frac{1-p+1}{3} = \frac{2-p}{3}$. The numerator for $C_2$ is $1(1/3)$. Thus, $P(C_2|M_3) = \frac{1}{2-p}$.
> > 
> > **Answer.** (a) $\frac{2}{3}$; (b) $\frac{1}{p+1}$; (c) 
$\frac{1}{2-p}$. ✓

> [!example] Exercise 41 — Monty's Coin-Flip Tiebreak
> **Problem.** The ratings of Monty Hall's show have dropped slightly, and a panicking executive producer complains to Monty that the part of the show where he opens a door lacks suspense: Monty always opens a door with a goat. Monty replies that the reason is so that the game is never spoiled by him revealing the car, but he agrees to update the game as follows. Before each show, Monty secretly flips a coin with probability p of Heads. If the coin lands Heads, Monty resolves to open a door with a goat (with equal probabilities if there is a choice). Otherwise, Monty resolves to open a random door, with equal probabilities. Of course, Monty will not open the door that the contestant initially chooses. The contestant knows p but does not know the outcome of the coin flip. When the show starts, the contestant chooses a door. Monty (who knows where the car is) then opens a door. If the car is revealed, the game is over; if a goat is revealed, the contestant is offered the option of switching. Now suppose it turns out that the contestant chooses door 1 and then Monty opens door 2, revealing a goat. What is the contestant's probability of success if they switch to door 3?
> 
> > [!success]- Click to reveal solution
> > Let $E$ be the evidence that Monty opens door 2 and reveals a goat. We use **Bayes' rule** to find $P(C_3|E)$. If $C_1$, Monty opens 2 or 3 with equal probability regardless of the coin flip (both are goats), so $P(E|C_1) = 1/2$. If $C_2$, door 2 has the car, so it's impossible to reveal a goat. $P(E|C_2) = 0$. If $C_3$, door 2 is a goat. If the coin is Heads (prob $p$), Monty must open door 2 to reveal a goat, so probability is 1. If Tails (prob $1-p$), Monty chooses randomly between 2 and 3, so probability is $1/2$. Thus $P(E|C_3) = p(1) + (1-p)(1/2) = \frac{1+p}{2}$. By Bayes' rule: $P(C_3|E) = \frac{P(E|C_3)P(C_3)}{P(E|C_1)P(C_1) + P(E|C_2)P(C_2) + P(E|C_3)P(C_3)} = \frac{\frac{1+p}{2}}{\frac{1}{2} + 0 + \frac{1+p}{2}}$.
> > 
> > **Answer.** $\frac{1+p}{2+p}$. ✓

> [!example] Exercise 42 — Monty Sometimes Offers a Switch
> **Problem.** Consider the following variation of the Monty Hall problem, where in some situations Monty may not open a door and give the contestant the choice of whether to switch doors. Specifically, there are 3 doors, with 2 containing goats and 1 containing a car. The car is equally likely to be anywhere, and Monty knows where the car is. Let 0 ≤p ≤1. The contestant chooses a door. If this initial choice has the car, Monty will open another door, revealing a goat (choosing with equal probabilities among his two choices of door), and then offer the contestant the choice of whether to switch to the other unopened door. If the contestant's initial choice has a goat, then with probability p Monty will open another door, revealing a goat, and then offer the contestant the choice of whether to switch to the other unopened door; but with probability 1 −p, Monty will not open a door, and the contestant must stick with their initial choice. The contestant decides in advance to use the following strategy: initially choose door 1. Then, if Monty opens a door and offers the choice of whether to switch, do switch. (a) Find the unconditional probability that the contestant will get the car. Also, check what your answer reduces to in the extreme cases p = 0 and p = 1, and briefly explain why your answer makes sense in these two cases. (b) Monty now opens door 2, revealing a goat. So the contestant switches to door 3. Given this information, find the conditional probability that the contestant will get the car.
> 
> > [!success]- Click to reveal solution
> > Part (a): We use **LOTP** conditioning on the car's location. If $C_1$, switching fails (prob 0). If $C_2$, Monty offers a switch with probability $p$; if he does, switching to 2 wins. Thus, winning probability is $p(1/3)$. If $C_3$, winning probability is $p(1/3)$. Unconditional total is $\frac{2p}{3}$. If $p=0$, Monty never helps when you're wrong, so you can't win by switching. If $p=1$, it is standard Monty Hall ($2/3$).
> > Part (b): Let $M_2$ be the event Monty opens door 2 (revealing a goat). By **Bayes' rule**, evaluate the likelihoods: $P(M_2|C_1) = 1/2$. $P(M_2|C_2) = 0$. $P(M_2|C_3) = p$. The posterior $P(C_3|M_2) = \frac{p(1/3)}{p(1/3) + (1/2)(1/3)}$.
> > 
> > **Answer.** (a) $\frac{2p}{3}$. Reduces to $0$ if $p=0$ and $2/3$ if 
$p=1$. (b) $\frac{2p}{2p+1}$. ✓

> [!example] Exercise 43 — Car, Computer, or Goat
> **Problem.** You are the contestant on the Monty Hall show. Monty is trying out a new version of his game, with rules as follows. You get to choose one of three doors. One door has a car behind it, another has a computer, and the other door has a goat (with all permutations equally likely). Monty, who knows which prize is behind each door, will open a door (but not the one you chose) and then let you choose whether to switch from your current choice to the other unopened door. Assume that you prefer the car to the computer, the computer to the goat, and (by transitivity) the car to the goat. (a) Suppose for this part only that Monty always opens the door that reveals your less preferred prize out of the two alternatives, e.g., if he is faced with the choice between revealing the goat or the computer, he will reveal the goat. Monty opens a door, revealing a goat (this is again for this part only). Given this information, should you switch? If you do switch, what is your probability of success in getting the car? (b) Now suppose that Monty reveals your less preferred prize with probability p, and your more preferred prize with probability q = 1 −p. Monty opens a door, revealing a computer. Given this information, should you switch (your answer can depend on p)? If you do switch, what is your probability of success in getting the car (in terms of p)?
> 
> > [!success]- Click to reveal solution
> > Part (a): Using **conditional probability**, let's evaluate $P(C_{comp}|E)$ where $E$ is Monty revealing a goat. $P(E|C_{car}) = 1$ (alternatives are Comp/Goat, Goat is less preferred). $P(E|C_{comp}) = 1$ (alternatives are Car/Goat, Goat is less preferred). $P(E|C_{goat}) = 0$ (alternatives are Car/Comp, Comp is less preferred). By **Bayes' rule**, $P(C_{comp}|E) = \frac{1(1/3)}{1(1/3) + 1(1/3) + 0} = 1/2$. Switching yields the car exactly if you started with the computer, so the probability is $1/2$.
> > Part (b): $E$ is Monty revealing a computer. $P(E|C_{car}) = 1-p$ (Goat is less preferred, Comp is more preferred). $P(E|C_{comp}) = 0$. $P(E|C_{goat}) = p$ (Comp is less preferred). By **Bayes' rule**, $P(C_{goat}|E) = \frac{p(1/3)}{p(1/3) + (1-p)(1/3)} = p$. Switching gives the car exactly if you started with the goat, so the success rate is $p$.
> > 
> > **Answer.** (a) It does not strictly matter; if you switch, success 
probability is $\frac{1}{2}$. (b) Yes, switch if $p > \frac{1}{2}$; success 
probability is $p$. ✓

> [!example] Exercise 44 — Random Car Placement
> **Problem.** Monty Hall has introduced a new twist in his game, by generalizing the assumption that the initial probabilities for where the car is are ( 1 3, 1 3, 1 3). Specifically, there are three doors, behind one of which there is a car (which the contestant wants), and behind the other two of which there are goats (which the contestant doesn't want). Initially, door i has probability pi of having the car, where $p_{1}$, $p_{2}$, $p_{3}$ are known constants such that 0 < $p_{1}$ ≤$p_{2}$ ≤$p_{3}$ < 1 and $p_{1}$ + $p_{2}$ + $p_{3}$ = 1. The contestant chooses a door. Then Monty opens a door (other than the one the contestant chose) and offers the contestant the option of switching to the other unopened door. (a) Assume for this part that Monty knows in advance which door has the car. He always opens a door to reveal a goat, and if he has a choice of which door to open he chooses with equal probabilities. Suppose for this part that the contestant initially chooses door 3, and then Monty opens door 2, revealing a goat. Given the above information, find the conditional probability that door 3 has the car. Should the contestant switch doors? (If whether to switch depends on the pi's, give a fully simplified criterion in terms of the pi's.) (b) Now assume instead that Monty does not know in advance where the car is. He randomly chooses which door to open (other than the one the contestant chose), with equal probabilities. (The game is spoiled if he reveals the car.) Suppose again that the contestant initially chooses door 3, and then Monty opens door 2, revealing a goat. Given the above information, find the conditional probability that door 3 has the car. Should the contestant switch doors? (If whether to switch depends on the pi's, give a fully simplified criterion in terms of the pi's.) (c) Repeat (a), except with the contestant initially choosing door 1 rather than door 3. (d) Repeat (b), except with the contestant initially choosing door 1 rather than door 3.
> 
> > [!success]- Click to reveal solution
> > Use **Bayes' rule** for all parts. (a) $P(M_2|C_3) = 1/2$, $P(M_2|C_1) = 1$, $P(M_2|C_2) = 0$. $P(C_3|M_2) = \frac{p_3/2}{p_3/2 + p_1} = \frac{p_3}{p_3 + 2p_1}$. $P(C_1|M_2) = \frac{2p_1}{p_3 + 2p_1}$. Switch if $2p_1 > p_3$. (b) $P(M_2 \cap \text{goat}|C_3) = 1/2$, $P(M_2 \cap \text{goat}|C_1) = 1/2$, $P(M_2 \cap \text{goat}|C_2) = 0$. $P(C_3|M_2) = \frac{p_3/2}{p_3/2 + p_1/2} = \frac{p_3}{p_1 + p_3}$. Switch if $p_1 > p_3$ (which is never true). (c) $P(M_2|C_1) = 1/2$, $P(M_2|C_3) = 1$, $P(M_2|C_2) = 0$. $P(C_1|M_2) = \frac{p_1/2}{p_1/2 + p_3} = \frac{p_1}{p_1 + 2p_3}$. Switch if $2p_3 > p_1$ (always true). (d) $P(M_2 \cap \text{goat}|C_1) = 1/2$, $P(M_2 \cap \text{goat}|C_3) = 1/2$. $P(C_1|M_2) = \frac{p_1}{p_1 + p_3}$. Switch if $p_3 > p_1$.
> > 
> > **Answer.** (a) $\frac{p_3}{p_3 + 2p_1}$; switch if $2p_1 > p_3$. (b)
$\frac{p_3}{p_1 + p_3}$; switch if $p_1 > p_3$. (c) $\frac{p_1}{p_1 + 2p_3}$; 
switch if $2p_3 > p_1$. (d) $\frac{p_1}{p_1 + p_3}$; switch if $p_3 > p_1$. ✓

> [!example] Exercise 45 — Two Independent Doors
> **Problem.** Monty Hall is trying out a new version of his game. In this version, instead of there always being 1 car and 2 goats, the prizes behind the doors are generated independently, with each door having probability p of having a car and q = 1 −p of having a goat. In detail: There are three doors, behind each of which there is one prize: either a car or a goat. For each door, there is probability p that there is a car behind it and q = 1 −p that there is a goat, independent of the other doors. The contestant chooses a door. Monty, who knows the contents of each door, then opens one of the two remaining doors. In choosing which door to open, Monty will always reveal a goat if possible. If both of the remaining doors have the same kind of prize, Monty chooses randomly (with equal probabilities). After opening a door, Monty offers the contestant the option of switching to the other unopened door. The contestant decides in advance to use the following strategy: first choose door 1. Then, after Monty opens a door, switch to the other unopened door. (a) Find the unconditional probability that the contestant will get a car. (b) Monty now opens door 2, revealing a goat. Given this information, find the conditional probability that the contestant will get a car.
> 
> > [!success]- Click to reveal solution
> > Let $N$ be the number of cars behind doors 2 and 3. $P(N=0)=q^2$, $P(N=1)=2pq$, $P(N=2)=p^2$. (a) Use **LOTP**. If $N=0$, switching gives a goat (prob 0). If $N=1$, Monty opens the goat, leaving the car; switching wins (prob 1). If $N=2$, Monty opens a car, leaving a car; switching wins (prob 1). $P(\text{Win}) = P(N=1) + P(N=2) = 2pq + p^2 = p(2q+p) = p(2-p)$. (b) Let $M_{2g}$ be Monty opening 2 revealing a goat. We want the probability that door 3 is a car (the $gc$ case) given this evidence. By **Bayes' rule**, $P(M_{2g}|gg) = 1/2$, $P(M_{2g}|gc) = 1$, $P(M_{2g}|cg) = 0$, $P(M_{2g}|cc) = 0$. $P(M_{2g}) = (1/2)q^2 + 1(pq) = q(q/2+p) = q(1-p/2)$. $P(gc|M_{2g}) = \frac{1(pq)}{q(1-p/2)} = \frac{p}{1-p/2}$.
> > 
> > **Answer.** (a) $p(2-p)$; (b) $\frac{2p}{2-p}$. ✓

> [!example] Exercise 46 — Four-Prize Monty Hall
> **Problem.** Monty Hall is trying out a new version of his game, with rules as follows. The contestant gets to choose one of four doors. One door has a car behind it, another has an apple, another has a book, and another has a goat. All 24 permutations for which door has which prize are equally likely. In order from least preferred to most preferred, the contestant's preferences are: goat, apple, book, car. Monty, who knows which prize is behind each door, will open a door (other than the contestant's initial choice) and then let the contestant choose whether to switch to another unopened door. Monty will reveal the least preferred prize (among the 3 doors other than the contestant's initial choice) with probability p, the intermediately preferred prize with probability 1 −p, and the most preferred prize never. The contestant decides in advance to use the following strategy: Initially choose door 1. After Monty opens a door, switch to one of the other two unopened doors, randomly choosing between them (with probability 1/2 each). (a) Find the unconditional probability that the contestant will get the car. Hint: Condition on where the car is. (b) Find the unconditional probability that Monty will reveal the apple. Hint: Condition on what is behind door 1. (c) Monty now opens a door, revealing the apple. Given this information, find the conditional probability that the contestant will get the car.
> 
> > [!success]- Click to reveal solution
> > (a) **LOTP** conditioning on whether door 1 has the car. If $C_1$ (prob 1/4), switching fails. If $C_1^c$ (prob 3/4), the 2 remaining doors contain the car and one other prize. Choosing randomly gives a $1/2$ chance. $P(\text{Win}) = (3/4)(1/2) = 3/8$. (b) **LOTP** conditioning on door 1. If $C_1$, Monty reveals Apple with $1-p$. If Book, reveals Apple with $1-p$. If Goat, reveals Apple with $p$. If Apple, prob is 0. $(1/4)(1-p) + (1/4)(1-p) + (1/4)(p) = \frac{2-p}{4}$. (c) By **Bayes' rule**, $P(C_1 | R_A) = \frac{P(R_A|C_1)P(C_1)}{P(R_A)} = \frac{(1-p)(1/4)}{(2-p)/4} = \frac{1-p}{2-p}$. Because switching wins only if the car is NOT behind door 1, and we switch randomly to one of two doors, $P(\text{Win}|R_A) = \frac{1}{2} (1 - P(C_1|R_A))$.
> > 
> > **Answer.** (a) $\frac{3}{8}$; (b) $\frac{2-p}{4}$; (c) 
$\frac{1}{2(2-p)}$. ✓

> [!example] Exercise 47 — Two-Stage Stay or Switch
> **Problem.** You are the contestant on Monty Hall's game show. Hoping to double the excitement of the game, Monty will offer you two opportunities to switch to another door. Specifically, the new rules are as follows. There are four doors. Behind one door there is a car (which you want); behind the other three doors there are goats (which you don't want). Initially, all possibilities are equally likely for where the car is. Monty knows where the car is, and when he has a choice of which door to open, he chooses with equal probabilities. You choose a door, which for concreteness we assume is door 1. Monty opens a door (other than door 1), revealing a goat, and then offers you the option to switch to another door. Monty then opens another door (other than your currently selected door), revealing another goat. So now there are two open doors (with goats) and two unopened doors. Again Monty offers you the option to switch. You decide in advance to use one of the following four strategies: stay-stay, stay-switch, switch-stay, switch-switch, where, for example, "stay-switch" means that the first time Monty offers you the choice of switching, you stay with your current selection, but then the second time Monty offers you the choice, you do switch doors. In each part below the goal is to find or compare unconditional probabilities, i.e., from a vantage point of before the game has started. (a) Find the probability of winning the car if you follow the stay-stay strategy. (b) Find the probability of winning the car if you follow the stay-switch strategy. (c) Find the probability of winning the car if you follow the switch-stay strategy. (d) Find the probability of winning the car if you follow the switch-switch strategy. (e) Which of these four strategies is the best?
> 
> > [!success]- Click to reveal solution
> > We compute paths using **LOTP** conditioning on our initial choice (Car with 1/4, Goat with 3/4). If we choose Car (1/4): Stay-Stay wins (1). Stay-Switch fails because switching from the car to the last door (a goat) loses (0). Switch-Stay fails because we switch to a goat and stay there (0). Switch-Switch: we switch to Goat A, Monty opens Goat B; we switch again to the only remaining door, the Car, so it wins (1). If we choose Goat (3/4): Stay-Stay fails (0). Stay-Switch: Monty opens both other goats sequentially, leaving only the Car closed. Switching guarantees the Car (1). Switch-Stay: We switch to the other available doors (Car or Goat, 1/2 each) and stay, winning half the time (1/2). Switch-Switch: We switch to Car (1/2) and then switch away and lose, or we switch to Goat (1/2) and then switch to Car and win. Win prob is 1/2. Summing the branches: Stay-Stay = $1/4$; Stay-Switch = $3/4$; Switch-Stay = $3/8$; Switch-Switch = $1/4(1) + 3/4(1/2) = 5/8$.
> > 
> > **Answer.** (a) $\frac{1}{4}$; (b) $\frac{3}{4}$; (c) $\frac{3}{8}$; 
(d) $\frac{5}{8}$; (e) stay-switch. ✓

## First-step analysis and gambler's ruin (Exercises 48–54)

> [!example] Exercise 48 — Running Die Total Hits n
> **Problem.** A fair die is rolled repeatedly, and a running total is kept (which is, at each time, the total of all the rolls up until that time). Let pn be the probability that the running total is ever exactly n (assume the die will always be rolled enough times so that the running total will eventually exceed n, but it may or may not ever equal n). (a) Write down a recursive equation for pn (relating pn to earlier terms $p_{k}$ in a simple way). Your equation should be true for all positive integers n, so give a definition of $p_{0}$ and $p_{k}$ for k < 0 so that the recursive equation is true for small values of n. (b) Find $p_{7}$. (c) Give an intuitive explanation for the fact that pn →1/3.5 = 2/7 as n →∞.
> 
> > [!success]- Click to reveal solution
> > (a) Using **first-step analysis** and the **Law of Total Probability**, condition on the outcome of the first roll. If the first roll is $k$ (which happens with probability $1/6$), the remaining sum needed to reach $n$ exactly is $n-k$. The probability of achieving this is $p_{n-k}$. (b) Using the recurrence relation, $p_n = \frac{1}{6} \sum_{k=1}^6 p_{n-k}$. With $p_0=1$, we can sum sequentially to find $p_n = \frac{7^{n-1}}{6^n}$ for $1 \le n \le 6$. For $p_7$, we sum the prior 6 terms: $p_7 = \frac{1}{6}(p_6 + p_5 + p_4 + p_3 + p_2 + p_1)$. Since $p_6 = \frac{1}{6}(p_5 + p_4 + p_3 + p_2 + p_1 + p_0)$, substituting this yields $p_7 = \frac{1}{6}(7p_6 - p_0) = \frac{7}{6}p_6 - \frac{1}{6} = \frac{7^6}{6^7} - \frac{1}{6}$. (c) The average roll is $(1+2+3+4+5+6)/6 = 3.5$. Over the long run, the running total will land on 1 out of every 3.5 numbers. Thus, the probability of hitting any specific large integer asymptotically approaches $1/3.5$.
> > 
> > **Answer.** (a) $p_n = \frac{1}{6}(p_{n-1} + p_{n-2} + p_{n-3} + 
p_{n-4} + p_{n-5} + p_{n-6})$, with $p_0 = 1$ and $p_k = 0$ for $k < 0$. (b) 
$\frac{7^6}{6^7} - \frac{1}{6}$ (or $\frac{70993}{279936}$). (c) The expected 
value of each roll is 3.5, so in the long run, the sequence hits about 1 in 
every 3.5 numbers, yielding a probability of $\frac{1}{3.5} = \frac{2}{7}$. ✓

> [!example] Exercise 49 — Even Number of Successes
> **Problem.** A sequence of n ≥1 independent trials is performed, where each trial ends in "success" or "failure" (but not both). Let pi be the probability of success in the ith trial, qi = 1−pi, and bi = qi −1/2, for i = 1, 2, . . . , n. Let An be the event that the number of successful trials is even. (a) Show that for n = 2, P($A_{2}$) = 1/2 + 2b1b2. (b) Show by induction that P(An) = 1/2 + 2n−1b1b2 . . . bn. (This result is very useful in cryptography. Also, note that it implies that if n coins are flipped, then the probability of an even number of Heads is 1/2 if and only if at least one of the coins is fair.) Hint: Group some trials into a supertrial. (c) Check directly that the result of (b) is true in the following simple cases: pi = 1/2 for some i; pi = 0 for all i; pi = 1 for all i.
> 
> > [!success]- Click to reveal solution
> > Let $p_i$ be the probability of success, $q_i = 1-p_i$, and $b_i = q_i - 1/2$. Let $A_n$ be the event of an even number of successes.
> > Part (a): By **independence**, $P(A_2)$ is the probability of exactly 0 or 2 successes. $P(A_2) = q_1 q_2 + p_1 p_2$. Substituting $q_i = 1/2 + b_i$ and $p_i = 1/2 - b_i$ yields $(1/2 + b_1)(1/2 + b_2) + (1/2 - b_1)(1/2 - b_2)$. Expanding both products, the linear terms cancel, leaving $1/4 + b_1 b_2 + 1/4 + b_1 b_2 = 1/2 + 2b_1 b_2$.
> > Part (b): Proceed by induction. Base case $n=1$: $P(A_1) = q_1 = 1/2 + b_1 = 1/2 + 2^0 b_1$. Assume true for $n-1$. Using the **Law of Total Probability** and grouping the first $n-1$ trials into a supertrial (**independence**), $P(A_n) = P(A_{n-1})q_n + P(A_{n-1}^c)p_n = P(A_{n-1})q_n + (1-P(A_{n-1}))p_n = P(A_{n-1})(q_n - p_n) + p_n$. Since $q_n - p_n = 2b_n$ and $p_n = 1/2 - b_n$, substitute the inductive hypothesis to get $(1/2 + 2^{n-2}b_1\dots b_{n-1})(2b_n) + 1/2 - b_n = b_n + 2^{n-1}b_1\dots b_n + 1/2 - b_n$.
> > Part (c): If any $p_i = 1/2$, then $b_i = 0$, so $P(A_n) = 1/2$. If all $p_i = 0$, $b_i = 1/2$, so $P(A_n) = 1/2 + 2^{n-1}(1/2)^n = 1$. If all $p_i = 1$, $b_i = -1/2$, so $P(A_n) = 1/2 + 2^{n-1}(-1/2)^n = 1/2 + (-1)^n/2$ (which alternates $0$ and $1$).
> > 
> > **Answer.** (a) $P(A_2) = (1/2 - b_1)(1/2 - b_2) + (1/2 + b_1)(1/2 + 
b_2) = 1/2 + 2b_1 b_2$. (b) By LOTP and induction, $P(A_n) = P(A_{n-1})(q_n - 
p_n) + p_n = 1/2 + 2^{n-1}b_1\dots b_n$. (c) Checks out intuitively for $p_i 
\in \{0, 1/2, 1\}$. ✓

> [!example] Exercise 50 — Calvin and Hobbes (Win by Two)
> **Problem.** Calvin and Hobbes play a match consisting of a series of games, where Calvin has probability p of winning each game (independently). They play with a "win by two" rule: the first player to win two games more than his opponent wins the match. Find the probability that Calvin wins the match (in terms of p), in two different ways: (a) by conditioning, using the law of total probability. (b) by interpreting the problem as a gambler's ruin problem.
> 
> > [!success]- Click to reveal solution
> > Let $p$ be Calvin's win probability, $q = 1-p$.
> > Part (a): Let $W$ be the event Calvin wins the match. Condition on the first two games using **LOTP** and **independence**. The permutations are $WW$ (prob $p^2$), $LL$ (prob $q^2$), and $WL$ or $LW$ (prob $2pq$). $P(W) = P(W|WW)p^2 + P(W|WL \cup LW)(2pq) + P(W|LL)q^2$. The conditionals are $1$, $P(W)$ (since the score resets to a tie), and $0$. Thus $P(W) = p^2 + 2pq P(W)$. Solving for $P(W)$ gives $\frac{p^2}{1-2pq}$. Since $1 = (p+q)^2 = p^2 + 2pq + q^2$, $1-2pq = p^2+q^2$.
> > Part (b): Using **first-step analysis** (Gambler's Ruin), Calvin starts at $i=2$ in a random walk bounded by $0$ (Hobbes wins) and $N=4$ (Calvin wins). By the ruin formula, $P(W) = \frac{1 - (q/p)^2}{1 - (q/p)^4} = \frac{1}{1 + (q/p)^2} = \frac{p^2}{p^2 + q^2}$ (for $p \neq 1/2$). If $p = 1/2$, $p_2 = 2/4 = 1/2$.
> > 
> > **Answer.** (a) $P(W) = \frac{p^2}{p^2 + q^2}$; (b) Gambler's ruin 
with $i=2, N=4$ gives $\frac{1 - (q/p)^2}{1 - (q/p)^4} = \frac{p^2}{p^2 + 
q^2}$. ✓

> [!example] Exercise 51 — Reaching the Goal
> **Problem.** A gambler repeatedly plays a game where in each round, he wins a dollar with probability 1/3 and loses a dollar with probability 2/3. His strategy is "quit when he is ahead by $2". Suppose that he starts with a million dollars. Show that the probability that he'll ever be ahead by $2 is less than 1/4.
> 
> > [!success]- Click to reveal solution
> > Use **first-step analysis** via the Gambler's Ruin formula. The gambler starts with $i = 10^6$ dollars and aims to reach $N = 10^6 + 2$ dollars before dropping to $0$. The probabilities are $p = 1/3$ and $q = 2/3$, so the ratio $q/p = 2$. By the ruin formula, the probability of reaching the goal is $\frac{1 - (q/p)^i}{1 - (q/p)^N} = \frac{1 - 2^{10^6}}{1 - 2^{10^6+2}}$. Since $1 - 2^{10^6+2} = 1 - 4(2^{10^6})$, the fraction simplifies to $\frac{2^{10^6} - 1}{4(2^{10^6}) - 1}$, which is strictly less than $\frac{2^{10^6}}{4(2^{10^6})} = 1/4$.
> > 
> > **Answer.** $\frac{1 - 2^{10^6}}{1 - 2^{10^6+2}} < \frac{1}{4}$. ✓

> [!example] Exercise 52 — Rescaled Gambler's Ruin
> **Problem.** As in the gambler's ruin problem, two gamblers, A and B, make a series of bets, until one of the gamblers goes bankrupt. Let A start out with i dollars and B start out with N −i dollars, and let p be the probability of A winning a bet, with 0 < p < 1 2. Each bet is for 1 k dollars, with k a positive integer, e.g., k = 1 is the original gambler's ruin problem and k = 20 means they're betting nickels. Find the probability that A wins the game, and determine what happens to this as k →∞.
> 
> > [!success]- Click to reveal solution
> > To frame this exactly as the standard Gambler's Ruin problem, rescale the bets by converting the unit of wealth to $1/k$ dollars. Gambler A starts with $i \cdot k$ units, and Gambler B starts with $(N-i) \cdot k$ units. The total wealth is $N \cdot k$ units. Using the formula from **first-step analysis**, the probability that A wins is $\frac{1 - (q/p)^{ik}}{1 - (q/p)^{Nk}}$. Because $p < 1/2$, the ratio $q/p > 1$. As $k \to \infty$, both the numerator and denominator grow exponentially. The fraction is asymptotically equivalent to the ratio of the dominating terms: $\frac{-(q/p)^{ik}}{-(q/p)^{Nk}} = (p/q)^{k(N-i)}$. Since $p/q < 1$ and $N > i$, this limit strictly approaches $0$.
> > 
> > **Answer.** The probability is $\frac{1 - (q/p)^{ik}}{1 - 
(q/p)^{Nk}}$, which approaches $0$ as $k \to \infty$. ✓

> [!example] Exercise 53 — The Wolf and 99 Sheep
> **Problem.** There are 100 equally spaced points around a circle. At 99 of the points, there are sheep, and at 1 point, there is a wolf. At each time step, the wolf randomly moves either clockwise or counterclockwise by 1 point. If there is a sheep at that point, he eats it. The sheep don't move. What is the probability that the sheep who is initially opposite the wolf is the last one remaining?
> 
> > [!success]- Click to reveal solution
> > Let the sheep opposite the wolf be $S$. For $S$ to be the final sheep remaining, the wolf must visit every other of the 98 sheep's positions before visiting $S$. At any point, the visited nodes form a contiguous arc. By the time 98 sheep are eaten, the unvisited nodes consist exactly of $S$ and one of its immediate neighbors, say $S'$. The wolf is currently located at the other side of $S'$, so the remaining unvisited arc has length 2 (nodes $S$ and $S'$). Using **first-step analysis** (Gambler's ruin) to see which is hit first, the wolf's distance to $S'$ is 1 and to $S$ is 99 (around the other side). For a simple random walk on a cycle, by symmetry and Gambler's ruin principles, the probability that any specific non-starting node is the *very last* unvisited node is uniformly distributed over all $N-1$ available nodes.
> > 
> > **Answer.** $\frac{1}{99}$. ✓

> [!example] Exercise 54 — The Immortal Drunk
> **Problem.** An immortal drunk man wanders around randomly on the integers. He starts at the origin, and at each step he moves 1 unit to the right or 1 unit to the left, with probabilities p and q = 1−p respectively, independently of all his previous steps. Let Sn be his position after n steps. (a) Let $p_{k}$ be the probability that the drunk ever reaches the value k, for all k ≥0. Write down a difference equation for $p_{k}$ (you do not need to solve it for this part). (b) Find $p_{k}$, fully simplified; be sure to consider all 3 cases: p < 1/2, p = 1/2, and p > 1/2. Feel free to assume that if $A_{1}$, $A_{2}$, . . . are events with $A_{j}$ ⊆$A_{j+1}$ for all j, then P(An) →P(∪∞ j=1Aj) as n →∞(because it is true; this is known as continuity of probability).
> 
> > [!success]- Click to reveal solution
> > Let $p_k$ be the probability of reaching $k$ from $0$.
> > Part (a): Apply **first-step analysis** and **LOTP** conditioning on the first step. If he moves right (prob $p$), he is at 1 and must cross distance $k-1$ (prob $p_{k-1}$). If he moves left (prob $q$), he is at -1 and must cross distance $k+1$ (prob $p_{k+1}$).
> > Part (b): The difference equation is $p_k = p \cdot p_{k-1} + q \cdot p_{k+1}$ with $p_0 = 1$. The characteristic roots are $1$ and $p/q$. If $p \neq 1/2$, the general solution is $p_k = A(1)^k + B(p/q)^k$. If $p > 1/2$, $p/q < 1$, but we need $p_k \to 1$ as drift is positive, so $p_k = 1$. If $p < 1/2$, drift is left, $p_k$ must approach 0 as $k \to \infty$, so $A=0$ and $B=1$, meaning $p_k = (p/q)^k$. If $p = 1/2$, $p_k = A + Bk$, and bounded probability requires $B=0$, so $p_k = 1$.
> > 
> > **Answer.** (a) $p_k = p \cdot p_{k-1} + q \cdot p_{k+1}$. (b) If $p 
\ge 1/2$, $p_k = 1$. If $p < 1/2$, $p_k = (p/q)^k$. ✓

## Simpson's paradox (Exercises 55–59)

> [!example] Exercise 55 — One Confounder Isn't Enough
> **Problem.** (a) Is it possible to have events A, B, C such that P(A|C) < P(B|C) and P(A|$C^c$) < P(B|$C^c$), yet P(A) > P(B)? That is, A is less likely than B given that C is true, and also less likely than B given that C is false, yet A is more likely than B if we're given no information about C. Show this is impossible (with a short proof) or find a counterexample (with a story interpreting A, B, C). (b) If the scenario in (a) is possible, is it a special case of Simpson's paradox, equivalent to Simpson's paradox, or neither? If it is impossible, explain intuitively why it is impossible even though Simpson's paradox is possible.
> 
> > [!success]- Click to reveal solution
> > Part (a): Apply the **Law of Total Probability**: $P(A) = P(A|C)P(C) + P(A|C^c)P(C^c)$. Since $P(A|C) < P(B|C)$ and $P(A|C^c) < P(B|C^c)$, substituting the larger terms into the equation yields $P(A) < P(B|C)P(C) + P(B|C^c)P(C^c)$. Because the right side is identically equal to $P(B)$ by LOTP, we strictly get $P(A) < P(B)$, making $P(A) > P(B)$ impossible.
> > Part (b): It is impossible because LOTP computes unconditional probability using the exact same weighting factors ($P(C)$ and $P(C^c)$) for both $A$ and $B$. Simpson's paradox is possible only because a confounding condition ($B$) alters those weighting factors to be heavily skewed, which is absent here.
> > 
> > **Answer.** (a) Impossible, because $P(A) = P(A|C)P(C) + 
P(A|C^c)P(C^c) < P(B|C)P(C) + P(B|C^c)P(C^c) = P(B)$. (b) It is impossible, 
distinguishing it from Simpson's paradox which relies on confounding variables 
shifting the weights of the weighted average. ✓

> [!example] Exercise 56 — Lisa, Homer, and the Ivory
> **Problem.** Consider the following conversation from an episode of The Simpsons: Lisa: Dad, I think he's an ivory dealer! His boots are ivory, his hat is ivory, and I'm pretty sure that check is ivory. Homer: Lisa, a guy who has lots of ivory is less likely to hurt Stampy than a guy whose ivory supplies are low. Here Homer and Lisa are debating the question of whether or not the man (named Blackheart) is likely to hurt Stampy the Elephant if they sell Stampy to him. They clearly disagree about how to use their observations about Blackheart to learn about the probability (conditional on the evidence) that Blackheart will hurt Stampy. (a) Define clear notation for the various events of interest here. (b) Express Lisa's and Homer's arguments (Lisa's is partly implicit) as conditional probability statements in terms of your notation from (a). (c) Assume it is true that someone who has a lot of a commodity will have less desire to acquire more of the commodity. Explain what is wrong with Homer's reasoning that the evidence about Blackheart makes it less likely that he will harm Stampy.
> 
> > [!success]- Click to reveal solution
> > Let $I$ be the event of having lots of ivory, $D$ be the event of being an ivory dealer, and $H$ be the event of wanting to hurt Stampy. Lisa implicitly states $P(D|I)$ is very high. Homer explicitly states $P(H|I) < P(H|I^c)$. The flaw in Homer's reasoning is failing to recognize $D$ as a confounding variable. While having a commodity might generally reduce desire for it given a fixed profession ($P(H|I, D^c) < P(H|I^c, D^c)$), the evidence $I$ strongly updates the probability of $D$. By **LOTP with extra conditioning**, $P(H|I) = P(H|I, D)P(D|I) + P(H|I, D^c)P(D^c|I)$. Because Lisa is right ($P(D|I) \approx 1$), the first term dominates, making $P(H|I)$ very high.
> > 
> > **Answer.** (a) $I$: lots of ivory; $D$: ivory dealer; $H$: hurt 
Stampy. (b) Lisa: $P(D|I)$ is high. Homer: $P(H|I) < P(H|I^c)$. (c) Homer 
ignores that $I$ strongly implies $D$. By LOTP, $P(H|I)$ is heavily weighted by
$P(H|I, D)$, which is extremely high. ✓

> [!example] Exercise 57 — Crimson and Magenta Jars
> **Problem.** (a) There are two crimson jars (labeled $C_{1}$ and $C_{2}$) and two mauve jars (labeled $M_{1}$ and $M_{2}$). Each jar contains a mixture of green gummi bears and red gummi bears. Show by example that it is possible that $C_{1}$ has a much higher percentage of green gummi bears than $M_{1}$, and $C_{2}$ has a much higher percentage of green gummi bears than $M_{2}$, yet if the contents of $C_{1}$ and $C_{2}$ are merged into a new jar and likewise for $M_{1}$ and $M_{2}$, then the combination of $C_{1}$ and $C_{2}$ has a lower percentage of green gummi bears than the combination of $M_{1}$ and $M_{2}$. (b) Explain how (a) relates to Simpson's paradox, both intuitively and by explicitly defining events A, B, C as in the statement of Simpson's paradox.
> 
> > [!success]- Click to reveal solution
> > Part (a): Create proportions that reverse upon aggregation due to sample sizes. C1: 1 green, 99 red (1%). M1: 0 green, 1 red (0%). C2: 100 green, 0 red (100%). M2: 99 green, 1 red (99%). C1 > M1 and C2 > M2. Combined C: 101 green out of 200 (50.5%). Combined M: 99 green out of 101 (~98%). 50.5% < 98%.
> > Part (b): Let $A$ be drawing green, $B$ be a Crimson jar, $C$ be jar index 2. This is identical to Simpson's paradox. Using the **definition of conditional probability**, $P(A|B, C) > P(A|B^c, C)$ and $P(A|B, C^c) > P(A|B^c, C^c)$. However, by **LOTP**, the uneven sizes of the jars act as a confounding variable, shifting the weights such that the aggregate $P(A|B) < P(A|B^c)$.
> > 
> > **Answer.** (a) C1(1G,99R), M1(0G,1R), C2(100G,0R), M2(99G,1R). 
Combined C is 50.5% Green, Combined M is 98% Green. (b) With $A$=Green, 
$B$=Crimson, $C$=Jar 2, it is Simpson's paradox exactly: conditionals strictly 
favor $B$, but unconditional favors $B^c$ due to confounding weights in LOTP. ✓

> [!example] Exercise 58 — When Simpson's Is Impossible
> **Problem.** As explained in this chapter, Simpson's paradox says that it is possible to have events A, B, C such that P(A|B, C) < P(A|$B^c$, C) and P(A|B, $C^c$) < P(A|$B^c$, $C^c$), yet P(A|B) > P(A|$B^c$). (a) Can Simpson's paradox occur if A and B are independent? If so, give a concrete example (with both numbers and an interpretation); if not, prove that it is impossible. (b) Can Simpson's paradox occur if A and C are independent? If so, give a concrete example (with both numbers and an interpretation); if not, prove that it is impossible. (c) Can Simpson's paradox occur if B and C are independent? If so, give a concrete example (with both numbers and an interpretation); if not, prove that it is impossible.
> 
> > [!success]- Click to reveal solution
> > Part (a): If $A$ and $B$ are **independent**, $P(A|B) = P(A|B^c) = P(A)$. This violates the required inequality $P(A|B) > P(A|B^c)$ of Simpson's paradox, making it impossible.
> > Part (b): If $A$ and $C$ are **independent**, $P(A|C) = P(A|C^c)$. For Simpson's to hold, $P(A|B)$ and $P(A|B^c)$ are bounded by their $C$ and $C^c$ subgroups. Using **LOTP**, it mathematically forces the interval $[\min P(A|\cdot, C), \max P(A|\cdot, C)]$ to be strictly disjoint from $[\min P(A|\cdot, C^c), \max P(A|\cdot, C^c)]$. Since $P(A|C)$ and $P(A|C^c)$ must live inside these disjoint intervals, they can never be equal, making it impossible.
> > Part (c): If $B$ and $C$ are **independent**, the weights in **LOTP** are identical: $P(C|B) = P(C|B^c)$. Taking the weighted average of $P(A|B, C) < P(A|B^c, C)$ and $P(A|B, C^c) < P(A|B^c, C^c)$ with identical weights guarantees $P(A|B) < P(A|B^c)$, violating the paradox. Impossible.
> > 
> > **Answer.** (a) Impossible; implies $P(A|B) = P(A|B^c)$. (b) 
Impossible; LOTP bounds force $P(A|C)$ and $P(A|C^c)$ into strictly disjoint 
intervals. (c) Impossible; identical weights in LOTP preserve the strict 
inequality direction. ✓

> [!example] Exercise 59 — Red State, Blue State
> **Problem.** The book Red State, Blue State, Rich State, Poor State by Andrew Gelman [12] discusses the following election phenomenon: within any U.S. state, a wealthy voter is more likely to vote for a Republican than a poor voter, yet the wealthier states tend to favor Democratic candidates! (a) Assume for simplicity that there are only 2 states (called Red and Blue), each of which has 100 people, and that each person is either rich or poor, and either a Democrat or a Republican. Make up numbers consistent with the above, showing how this phenomenon is possible, by giving a 2 × 2 table for each state (listing how many people in each state are rich Democrats, etc.). So within each state, a rich voter is more likely to vote for a Republican than a poor voter, but the percentage of Democrats is higher in the state with the higher percentage of rich people than in the state with the lower percentage of rich people. (b) In the setup of (a) (not necessarily with the numbers you made up there), let D be the event that a randomly chosen person is a Democrat (with all 200 people equally likely), and B be the event that the person lives in the Blue State. Suppose that 10 people move from the Blue State to the Red State. Write Pold and Pnew for probabilities before and after they move. Assume that people do not change parties, so we have Pnew(D) = Pold(D). Is it possible that both Pnew(D|B) > Pold(D|B) and Pnew(D|$B^c$) > Pold(D|$B^c$) are true? If so, explain how it is possible and why it does not contradict the law of total probability P(D) = P(D|B)P(B) + P(D|$B^c$)P($B^c$); if not, show that it is impossible.
> 
> > [!success]- Click to reveal solution
> > Part (a): Create proportions showcasing Simpson's Paradox. Red State: 10 Rich (10% Dem), 90 Poor (20% Dem) $\implies$ Total 19% Dem. Blue State: 90 Rich (60% Dem), 10 Poor (80% Dem) $\implies$ Total 62% Dem. In both states, Rich are less likely to vote Democrat (more likely Republican). However, Blue has more Rich people and is more Democrat overall.
> > Part (b): Let $D$ be Democrat, $B$ be Blue. We want to move 10 people and raise the Democrat percentage in *both* states. If we move exactly 5 Democrats and 5 Republicans from Blue to Red: New Blue Dem percentage is $(62-5)/90 = 63.3\% > 62\%$, so $P_{new}(D|B) > P_{old}(D|B)$. New Red Dem percentage is $(19+5)/110 = 21.8\% > 19\%$, so $P_{new}(D|B^c) > P_{old}(D|B^c)$. This does not contradict **LOTP** because shifting population weights from the heavily-Democrat Blue state to the less-Democrat Red state depresses the overall average, perfectly balancing out the individual percentage gains to keep the overall $P_{new}(D)$ constant.
> > 
> > **Answer.** (a) Red: 10 Rich (10% D), 90 Poor (20% D) = 19% D 
overall. Blue: 90 Rich (60% D), 10 Poor (80% D) = 62% D overall. (b) Yes. Move 
5 Democrats and 5 Republicans from Blue to Red. Both individual states' 
averages rise, but the shift of weight toward the lower-average state keeps the
total LOTP average constant. ✓

## Mixed practice (Exercises 60–74)

> [!example] Exercise 60 — Two Labs, One Test
> **Problem.** A patient is being given a blood test for the disease conditionitis. Let p be the prior probability that the patient has conditionitis. The blood sample is sent to one of two labs for analysis, lab A or lab B. The choice of which lab to use is made randomly, independent of the patient's disease status, with probability 1/2 for each lab. For lab A, the probability of someone testing positive given that they do have the disease is $a_{1}$, and the probability of someone testing negative given that they do not have the disease is $a_{2}$. The corresponding probabilities for lab B are $b_{1}$ and $b_{2}$. (a) Find the probability that the patient has the disease, given that they tested positive. (b) Find the probability that the patient's blood sample was analyzed by lab A, given that the patient tested positive.
> 
> > [!success]- Click to reveal solution
> > Let $T$ be a positive test.
> > Part (a): We want $P(D|T)$. Apply **Bayes' rule** and **LOTP with extra conditioning** on the lab assignment. $P(T|D) = P(T|D, A)P(A) + P(T|D, B)P(B) = a_1/2 + b_1/2$. $P(T|D^c) = P(T|D^c, A)P(A) + P(T|D^c, B)P(B) = (1-a_2)/2 + (1-b_2)/2$. The denominator is $P(T) = P(T|D)p + P(T|D^c)(1-p)$. Substitute to get the answer.
> > Part (b): We want $P(A|T)$. Apply **Bayes' rule**: $P(A|T) = \frac{P(T|A)P(A)}{P(T)}$. By **LOTP**, $P(T|A) = P(T|A, D)p + P(T|A, D^c)(1-p) = a_1 p + (1-a_2)(1-p)$. Using the same $P(T)$ derived in part (a), substitute and simplify by canceling the $1/2$ factors.
> > 
> > **Answer.** (a) $\frac{p(a_1 + b_1)}{p(a_1 + b_1) + (1-p)(2 - a_2 - 
b_2)}$; (b) $\frac{p a_1 + (1-p)(1-a_2)}{p(a_1 + b_1) + (1-p)(2 - a_2 - b_2)}$. ✓

> [!example] Exercise 61 — A Series of n Tests
> **Problem.** Fred decides to take a series of n tests, to diagnose whether he has a certain disease (any individual test is not perfectly reliable, so he hopes to reduce his uncertainty by taking multiple tests). Let D be the event that he has the disease, p = P(D) be the prior probability that he has the disease, and q = 1 −p. Let $T_{j}$ be the event that he tests positive on the jth test. (a) Assume for this part that the test results are conditionally independent given Fred's disease status. Let a = P($T_{j}$|D) and b = P($T_{j}$|$D^c$), where a and b don't depend on j. Find the posterior probability that Fred has the disease, given that he tests positive on all n of the n tests. (b) Suppose that Fred tests positive on all n tests. However, some people have a certain gene that makes them always test positive. Let G be the event that Fred has the gene. Assume that P(G) = 1/2 and that D and G are independent. If Fred does not have the gene, then the test results are conditionally independent given his disease status. Let $a_{0}$ = P($T_{j}$|D, $G^c$) and $b_{0}$ = P($T_{j}$|$D^c$, $G^c$), where $a_{0}$ and $b_{0}$ don't depend on j. Find the posterior probability that Fred has the disease, given that he tests positive on all n of the tests.
> 
> > [!success]- Click to reveal solution
> > Let $D$ be the event Fred has the disease ($P(D) = p$, $P(D^c) = q$), and let $T_1 \dots T_n$ be the events that the $n$ tests are positive. Let $T$ be the intersection $T_1 \cap \dots \cap T_n$.
> > Part (a): We assume **conditional independence** of the test results given the disease status. Thus $P(T|D) = a^n$ and $P(T|D^c) = b^n$. We apply **Bayes' rule** to find the posterior probability $P(D|T) = \frac{P(T|D)P(D)}{P(T|D)P(D) + P(T|D^c)P(D^c)}$.
> > Part (b): Let $G$ be the event of having the gene, with $P(G) = 1/2$. $D$ and $G$ are unconditionally **independent**. We use the **Law of Total Probability** conditioning on $G$ to find the new likelihoods. $P(T|D) = P(T|D, G)P(G|D) + P(T|D, G^c)P(G^c|D)$. Because $D$ and $G$ are independent, $P(G|D) = P(G) = 1/2$. If $G$ occurs, the tests are always positive, so $P(T|D, G) = 1$. If $G^c$ occurs, we use the conditional independence assumption: $P(T|D, G^c) = a_0^n$. Thus $P(T|D) = 1(1/2) + a_0^n(1/2) = \frac{1+a_0^n}{2}$. By the same logic, $P(T|D^c) = 1(1/2) + b_0^n(1/2) = \frac{1+b_0^n}{2}$. We substitute these likelihoods back into **Bayes' rule**.
> > 
> > **Answer.** (a) $\frac{a^n p}{a^n p + b^n q}$. (b) 
$\frac{p(1+a_0^n)}{p(1+a_0^n) + q(1+b_0^n)}$. ✓

> [!example] Exercise 62 — Hereditary Disease
> **Problem.** A certain hereditary disease can be passed from a mother to her children. Given that the mother has the disease, her children independently will have it with probability 1/2. Given that she doesn't have the disease, her children won't have it either. A certain mother, who has probability 1/3 of having the disease, has two children. (a) Find the probability that neither child has the disease. (b) Is whether the elder child has the disease independent of whether the younger child has the disease? Explain. (c) The elder child is found not to have the disease. A week later, the younger child is also found not to have the disease. Given this information, find the probability that the mother has the disease.
> 
> > [!success]- Click to reveal solution
> > Let $M$ be the event the mother has the disease ($P(M) = 1/3$). Let $C_1$ and $C_2$ be the events that the elder and younger child have it.
> > Part (a): We want $P(C_1^c \cap C_2^c)$. By the **Law of Total Probability**, $P(C_1^c \cap C_2^c) = P(C_1^c \cap C_2^c | M)P(M) + P(C_1^c \cap C_2^c | M^c)P(M^c)$. By **conditional independence** given the mother's status, this expands to $P(C_1^c|M)P(C_2^c|M)P(M) + P(C_1^c|M^c)P(C_2^c|M^c)P(M^c) = (\frac{1}{2})(\frac{1}{2})(\frac{1}{3}) + (1)(1)(\frac{2}{3}) = \frac{1}{12} + \frac{8}{12}$.
> > Part (b): To check for **independence**, we compare $P(C_1 \cap C_2)$ to $P(C_1)P(C_2)$. By **LOTP**, $P(C_1) = P(C_1|M)P(M) + P(C_1|M^c)P(M^c) = (\frac{1}{2})(\frac{1}{3}) + 0 = \frac{1}{6}$. Similarly, $P(C_2) = \frac{1}{6}$. By **LOTP** and **conditional independence**, $P(C_1 \cap C_2) = P(C_1 \cap C_2 | M)P(M) = (\frac{1}{4})(\frac{1}{3}) = \frac{1}{12}$. Because $\frac{1}{12} \neq (\frac{1}{6})(\frac{1}{6})$, they are not independent.
> > Part (c): We want $P(M|C_1^c \cap C_2^c)$. By **Bayes' rule**, this is $\frac{P(C_1^c \cap C_2^c|M)P(M)}{P(C_1^c \cap C_2^c)}$. Substituting the values from part (a) yields $\frac{(1/4)(1/3)}{3/4}$.
> > 
> > **Answer.** (a) $\frac{3}{4}$; (b) Not independent, because learning 
one child has the disease guarantees the mother has it, increasing the 
probability the other child has it; algebraically $1/12 \neq 1/36$. (c) 
$\frac{1}{9}$. ✓

> [!example] Exercise 63 — Three Coins, Two Matching
> **Problem.** Three fair coins are tossed at the same time. Explain what is wrong with the following argument: "there is a 50% chance that the three coins all landed the same way, since obviously it is possible to find two coins that match, and then the other coin has a 50% chance of matching those two".
> 
> > [!success]- Click to reveal solution
> > Let $M$ be the event that *at least* two coins land the same way, and $A$ be the event that all three coins land the same way. The argument abuses the **definition of conditional probability** by asserting $P(A|M) = 1/2$. By the Pigeonhole Principle, it is guaranteed that at least two coins match, meaning $P(M) = 1$. By the definition of conditional probability, $P(A|M) = \frac{P(A \cap M)}{P(M)} = \frac{P(A)}{1} = P(A)$. Since there are exactly 2 outcomes where all three match (HHH, TTT) out of 8 equally likely independent outcomes, $P(A) = \frac{2}{8} = \frac{1}{4}$. The flaw in the intuition is assuming you can pre-specify the identity of the "third" coin; there are multiple ways to form a matching pair among three coins, so the "remaining" coin is not a fixed, independent entity.
> > 
> > **Answer.** The argument misapplies the definition of conditional 
probability. It is guaranteed that at least two coins match ($P(M)=1$), so 
$P(\text{all three match} | M) = P(\text{all three match}) = 1/4 \neq 1/2$. ✓

> [!example] Exercise 64 — Green Before Blue
> **Problem.** An urn contains red, green, and blue balls. Let r, g, b be the proportions of red, green, blue balls, respectively (r + g + b = 1). (a) Balls are drawn randomly with replacement. Find the probability that the first time a green ball is drawn is before the first time a blue ball is drawn. Hint: Explain how this relates to finding the probability that a draw is green, given that it is either green or blue. (b) Balls are drawn randomly without replacement. Find the probability that the first time a green ball is drawn is before the first time a blue ball is drawn. Is the answer the same or different than the answer in (a)? Hint: Imagine the balls all lined up, in the order in which they will be drawn. Note that where the red balls are standing in this line is irrelevant. (c) Generalize the result from (a) to the following setting. Independent trials are performed, and the outcome of each trial is classified as being exactly one of type 1, type 2, . . . , or type n, with probabilities $p_{1}$, $p_{2}$, . . . , pn, respectively. Find the probability that the first trial to result in type i comes before the first trial to result in type j, for i ̸= j.
> 
> > [!success]- Click to reveal solution
> > Part (a): We want $P(\text{Green before Blue})$. Every draw is **independent**. This is equivalent to asking: given that a draw is either Green or Blue, what is the probability it is Green? By the **definition of conditional probability**, $P(G | G \cup B) = \frac{P(G)}{P(G \cup B)} = \frac{g}{g+b}$. The red balls simply delay the outcome and are irrelevant to the relative order of Green and Blue.
> > Part (b): Without replacement, imagine all balls lined up randomly. By symmetry, the relative ordering of the green and blue balls is uniformly random. If we extract only the sub-sequence of Green and Blue balls, the first ball in this sub-sequence is Green with proportion exactly $\frac{g}{g+b}$. Thus, the probability is exactly the same as in (a).
> > Part (c): Generalizing the **definition of conditional probability** from part (a), the probability of seeing type $i$ before type $j$ depends only on their relative proportions, ignoring all other $n-2$ types.
> > 
> > **Answer.** (a) $\frac{g}{g+b}$; (b) $\frac{g}{g+b}$ (the answer is 
the same); (c) $\frac{p_i}{p_i + p_j}$. ✓

> [!example] Exercise 65 — The 200-Person Raffle
> **Problem.** Marilyn vos Savant was asked the following question for her column in Parade: You're at a party with 199 other guests when robbers break in and announce that they are going to rob one of you. They put 199 blank pieces of paper in a hat, plus one marked "you lose." Each guest must draw, and the person who draws "you lose" will get robbed. The robbers offer you the option of drawing first, last, or at any time in between. When would you take your turn? The draws are made without replacement, and for (a) are uniformly random. (a) Determine whether it is optimal to draw first, last, or somewhere in between (or whether it does not matter), to maximize the probability of not being robbed. Give a clear, concise, and compelling explanation. (b) More generally, suppose that there is one "you lose" piece of paper, with "weight" v, and there are n blank pieces of paper, each with "weight" w. At each stage, draws are made with probability proportional to weight, i.e., the probability of drawing a particular piece of paper is its weight divided by the sum of the weights of all the remaining pieces of paper. Determine whether it is better to draw first or second (or whether it does not matter); here v > 0, w > 0, and n ≥1 are known constants.
> 
> > [!success]- Click to reveal solution
> > Part (a): By **symmetry**, the single "you lose" piece of paper is equally likely to be in any of the 200 possible drawing positions (probability $1/200$ for each). Therefore, any turn order yields the exact same $1/200$ probability of being robbed.
> > Part (b): Let $P(\text{lose 1st})$ be drawing the $v$ slip first. $P(\text{lose 1st}) = \frac{v}{v+nw}$. Using the **Law of Total Probability**, $P(\text{lose 2nd}) = P(\text{lose 2nd}|\text{lose 1st})P(\text{lose 1st}) + P(\text{lose 2nd}|\text{blank 1st})P(\text{blank 1st}) = 0 + (\frac{v}{v+(n-1)w})(\frac{nw}{v+nw})$. We want to minimize the probability of losing. Comparing the two fractions: $P(\text{lose 1st}) = \frac{v(v+(n-1)w)}{(v+nw)(v+(n-1)w)}$, while $P(\text{lose 2nd}) = \frac{vnw}{(v+nw)(v+(n-1)w)}$. Since the denominators are equal, we compare numerators $v^2 + vnw - vw$ against $vnw$. If $v > w$, the first numerator is larger, so $P(\text{lose 1st}) > P(\text{lose 2nd})$, meaning drawing second is safer. If $v < w$, drawing first is safer.
> > 
> > **Answer.** (a) It does not matter; by symmetry, every position has a
$1/200$ chance. (b) If $v > w$, it is better to draw second. If $v < w$, it is 
better to draw first. If $v = w$, it does not matter. ✓

> [!example] Exercise 66 — Most Likely Final Total
> **Problem.** A fair die is rolled repeatedly, until the running total is at least 100 (at which point the rolling stops). Find the most likely value of the final running total (i.e., the value of the running total at the first time when it is at least 100). Hint: Consider the possibilities for what the running total is just before the last roll.
> 
> > [!success]- Click to reveal solution
> > Let $p_k$ be the probability that the running total is exactly $k$ at some point. The final total must be $100, 101, 102, 103, 104,$ or $105$. We use the **Law of Total Probability** by conditioning on the running total *just before* the final roll (which must be exactly $94, 95, 96, 97, 98,$ or $99$). For the final total to be $100$, the previous total could be any of the 6 options (e.g., 99 and roll 1, 98 and roll 2, ..., 94 and roll 6). Thus $P(\text{final is } 100) = \frac{1}{6}(p_{99} + p_{98} + p_{97} + p_{96} + p_{95} + p_{94})$. For the final total to be $105$, the previous total must be $99$ and we must roll a 6, so $P(\text{final is } 105) = \frac{1}{6}(p_{99})$. Because $p_k > 0$ for all these values (in fact, $p_k \approx 2/7$ as shown in Ex. 48), the sum with the most terms is strictly the largest.
> > 
> > **Answer.** 100. ✓

> [!example] Exercise 67 — Homer's Donuts
> **Problem.** Homer has a box of donuts, which currently contains exactly c chocolate, g glazed, and j jelly donuts. Homer eats donuts one after another, each time choosing uniformly at random from the remaining donuts. (a) Find the probability that the last donut remaining in the box is a chocolate donut. (b) Find the probability of the following event: glazed is the first type of donut that Homer runs out of, and then jelly is the second type of donut that he runs out of. Hint: Consider the last donut remaining, and the last donut that is either glazed or jelly.
> 
> > [!success]- Click to reveal solution
> > Part (a): By **symmetry**, every single donut in the box is equally likely to be the very last one remaining. Since there are $c$ chocolate donuts out of a total of $c+g+j$ donuts, the probability is simply the proportion of chocolate donuts.
> > Part (b): We want the probability that the *last* donut remaining is chocolate AND the *last among (glazed, jelly)* is jelly. By **conditional probability**, we can compute $P(\text{last is C}) \times P(\text{last of G,J is J} | \text{last is C})$. Due to **independence** of relative orderings between disjoint sets, the condition that the absolute last donut is chocolate provides no information about the relative ordering of the remaining glazed and jelly donuts. Thus, $P(\text{last of G,J is J}) = \frac{j}{g+j}$. Multiplying the two probabilities gives the result.
> > 
> > **Answer.** (a) $\frac{c}{c+g+j}$; (b) $\frac{c}{c+g+j} \times 
\frac{j}{g+j}$. ✓

> [!example] Exercise 68 — Odds Ratio vs. Relative Risk
> **Problem.** Let D be the event that a person develops a certain disease, and C be the event that the person was exposed to a certain substance (e.g., D may correspond to lung cancer and C may correspond to smoking cigarettes). We are interested in whether exposure to the substance is related to developing the disease (and if so, how they are related). The odds ratio is a very widely used measure in epidemiology of the association between disease and exposure, defined as OR = odds(D|C) odds(D|$C^c$), where conditional odds are defined analogously to unconditional odds: odds(A|B) = P (A|B) P ($A^c$|B). The relative risk of the disease for someone exposed to the substance, another widely used measure, is RR = P(D|C) P(D|$C^c$). The relative risk is especially easy to interpret, e.g., RR = 2 says that someone exposed to the substance is twice as likely to develop the disease as someone who isn't exposed (though this does not necessarily mean that the substance causes the increased chance of getting the disease, nor is there necessarily a causal interpretation for the odds ratio). (a) Show that if the disease is rare, both for exposed people and for unexposed people, then the relative risk is approximately equal to the odds ratio. (b) Let pij for i = 0, 1 and j = 0, 1 be the probabilities in the following 2 × 2 table. D $D^c$ C $p_{11}$ $p_{10}$ $C^c$ $p_{01}$ $p_{00}$ For example, $p_{10}$ = P(C, $D^c$). Show that the odds ratio can be expressed as a crossproduct ratio, in the sense that OR = p11p00 p10p01 . (c) Show that the odds ratio has the neat symmetry property that the roles of C and D can be swapped without changing the value: OR = odds(C|D) odds(C|$D^c$). This property is one of the main reasons why the odds ratio is so widely used, since it turns out that it allows the odds ratio to be estimated in a wide variety of problems where relative risk would be hard to estimate well.
> 
> > [!success]- Click to reveal solution
> > Part (a): By definition, $OR = \frac{P(D|C)/P(D^c|C)}{P(D|C^c)/P(D^c|C^c)} = \frac{P(D|C)}{P(D|C^c)} \times \frac{P(D^c|C^c)}{P(D^c|C)} = RR \times \frac{P(D^c|C^c)}{P(D^c|C)}$. Because the disease is rare, the vast majority of people do not get it, meaning $P(D^c|C^c) \approx 1$ and $P(D^c|C) \approx 1$. Thus, the rightmost fraction is approximately $1$, leaving $OR \approx RR$.
> > Part (b): Using the **definition of conditional probability** and the table, $P(D|C) = \frac{p_{11}}{p_{11}+p_{10}}$ and $P(D^c|C) = \frac{p_{10}}{p_{11}+p_{10}}$. Thus $odds(D|C) = \frac{p_{11}}{p_{10}}$. Similarly, $odds(D|C^c) = \frac{p_{01}}{p_{00}}$. Dividing these gives $OR = \frac{p_{11}/p_{10}}{p_{01}/p_{00}} = \frac{p_{11}p_{00}}{p_{10}p_{01}}$.
> > Part (c): Substitute the roles of $C$ and $D$ into the odds formula: $odds(C|D) = \frac{P(C|D)}{P(C^c|D)} = \frac{P(C \cap D)/P(D)}{P(C^c \cap D)/P(D)} = \frac{p_{11}}{p_{01}}$. Similarly, $odds(C|D^c) = \frac{p_{10}}{p_{00}}$. The ratio is $\frac{p_{11}/p_{01}}{p_{10}/p_{00}} = \frac{p_{11}p_{00}}{p_{10}p_{01}}$, which is exactly the $OR$.
> > 
> > **Answer.** (a) $OR = RR \times \frac{P(D^c|C^c)}{P(D^c|C)}$. If 
rare, $P(D^c|\cdot) \approx 1$, so $OR \approx RR$. (b) $OR = 
\frac{p_{11}/p_{10}}{p_{01}/p_{00}} = \frac{p_{11}p_{00}}{p_{10}p_{01}}$. (c) 
$odds(C|D)/odds(C|D^c) = \frac{p_{11}/p_{01}}{p_{10}/p_{00}} = 
\frac{p_{11}p_{00}}{p_{10}p_{01}}$, matching (b). ✓

> [!example] Exercise 69 — Randomized Response
> **Problem.** A researcher wants to estimate the percentage of people in some population who have used illegal drugs, by conducting a survey. Concerned that a lot of people would lie when asked a sensitive question like "Have you ever used illegal drugs?", the researcher uses a method known as randomized response. A hat is filled with slips of paper, each of which says either "I have used illegal drugs" or "I have not used illegal drugs". Let p be the proportion of slips of paper that say "I have used illegal drugs" (p is chosen by the researcher in advance). Each participant chooses a random slip of paper from the hat and answers (truthfully) "yes" or "no" to whether the statement on that slip is true. The slip is then returned to the hat. The researcher does not know which type of slip the participant had. Let y be the probability that a participant will say "yes", and d be the probability that a participant has used illegal drugs. (a) Find y, in terms of d and p. (b) What would be the worst possible choice of p that the researcher could make in designing the survey? Explain. (c) Now consider the following alternative system. Suppose that proportion p of the slips of paper say "I have used illegal drugs", but that now the remaining 1 −p say "I was born in winter" rather than "I have not used illegal drugs". Assume that 1/4 of people are born in winter, and that a person's season of birth is independent of whether they have used illegal drugs. Find d, in terms of y and p.
> 
> > [!success]- Click to reveal solution
> > Part (a): Apply the **Law of Total Probability**. $P(\text{yes}) = P(\text{yes}|\text{drug slip})P(\text{drug slip}) + P(\text{yes}|\text{not drug slip})P(\text{not drug slip})$. Since people answer truthfully, $P(\text{yes}|\text{drug slip}) = d$ and $P(\text{yes}|\text{not drug slip}) = 1-d$. Thus $y = dp + (1-d)(1-p)$.
> > Part (b): If $p = 1/2$, the equation becomes $y = d/2 + (1-d)/2 = 1/2$. The observed value $y$ contains zero mathematical information about $d$, making it impossible to estimate $d$.
> > Part (c): Let $W$ be born in winter with $P(W) = 1/4$. By **LOTP** and **independence** of winter birth and drug use, $P(\text{yes}) = P(\text{yes}|\text{drug slip})p + P(\text{yes}|\text{winter slip})(1-p) = dp + (1/4)(1-p)$. Solving $y = dp + \frac{1-p}{4}$ for $d$ gives the result.
> > 
> > **Answer.** (a) $y = dp + (1-d)(1-p)$; (b) $p = 1/2$ is the worst 
because $y = 1/2$ regardless of $d$, destroying all information. (c) $d = 
\frac{4y - 1 + p}{4p}$. ✓

> [!example] Exercise 70 — Rosencrantz's Coins
> **Problem.** At the beginning of the play Rosencrantz and Guildenstern Are Dead by Tom Stoppard [25], Guildenstern is spinning coins and Rosencrantz is betting on the outcome for each. The coins have been landing Heads over and over again, prompting the following remark: Guildenstern: A weaker man might be moved to re-examine his faith, if in nothing else at least in the law of probability. The coin spins have resulted in Heads 92 times in a row. (a) Fred and his friend are watching the play. Upon seeing the events described above, they have the following conversation: Fred: That outcome would be incredibly unlikely with fair coins. They must be using trick coins (maybe with double-headed coins), or the experiment must have been rigged somehow (maybe with magnets). Fred's friend: It's true that the string HH. . . H of length 92 is very unlikely; the chance is 1/292 ≈2 × 10−28 with fair coins. But any other specific string of H's and T's with length 92 has exactly the same probability! The reason the outcome seems extremely unlikely is that the number of possible outcomes grows exponentially as the number of spins grows, so any outcome would seem extremely unlikely. You could just as well have made the same argument even without looking at the results of their experiment, which means you really don't have evidence against the coins being fair. Discuss these comments, to help Fred and his friend resolve their debate. (b) Suppose there are only two possibilities: either the coins are all fair (and spun fairly), or double-headed coins are being used (in which case the probability of Heads is 1). Let p be the prior probability that the coins are fair. Find the posterior probability that the coins are fair, given that they landed Heads in 92 out of 92 trials. (c) Continuing from (b), for which values of p is the posterior probability that the coins are fair greater than 0.5? For which values of p is it less than 0.05?
> 
> > [!success]- Click to reveal solution
> > Part (a): Fred's friend incorrectly relies on the unconditional probability of a specific sequence under a single model. Fred intuitively utilizes **Bayes' rule**: comparing the likelihood of the evidence under the fair coin model ($1/2^{92}$) versus a trick coin model (probability $1$). The overwhelming likelihood ratio justifies updating his belief against the coins being fair.
> > Part (b): Let $F$ be fair and $T$ be trick coins. By **Bayes' rule**: $P(F|E) = \frac{P(E|F)P(F)}{P(E|F)P(F) + P(E|T)P(T)} = \frac{(1/2)^{92} p}{(1/2)^{92} p + 1(1-p)}$. Multiply top and bottom by $2^{92}$ to simplify.
> > Part (c): To find where the posterior $> 0.5$, set $\frac{p}{p + 2^{92}(1-p)} > 1/2 \implies 2p > p + 2^{92}(1-p) \implies p > \frac{2^{92}}{1+2^{92}}$. For $< 0.05$, set the fraction $< 1/20 \implies 20p < p + 2^{92}(1-p) \implies 19p < 2^{92}(1-p) \implies p < \frac{2^{92}}{19+2^{92}}$.
> > 
> > **Answer.** (a) The friend ignores alternative hypotheses. Fred is 
intuitively using Bayes' rule, as the likelihood of 92 Heads is vastly higher 
under a trick coin hypothesis than a fair coin hypothesis. (b) $\frac{p}{p + 
2^{92}(1-p)}$; (c) $> 0.5$ when $p > \frac{2^{92}}{1+2^{92}}$, and $< 0.05$ 
when $p < \frac{2^{92}}{19+2^{92}}$. ✓

> [!example] Exercise 71 — Collecting n Toys
> **Problem.** There are n types of toys, which you are collecting one by one. Each time you buy a toy, it is randomly determined which type it has, with equal probabilities. Let pij be the probability that just after you have bought your ith toy, you have exactly j toy types in your collection, for i ≥1 and 0 ≤j ≤n. (This problem is in the setting of the coupon collector problem, a famous problem which we study in Example 4.3.12.) (a) Find a recursive equation expressing pij in terms of pi−1,j and pi−1,j−1, for i ≥2 and 1 ≤j ≤n. (b) Describe how the recursion from (a) can be used to calculate pij.
> 
> > [!success]- Click to reveal solution
> > Part (a): We use **first-step analysis / LOTP** conditioning on the state after $i-1$ toys. To have $j$ unique types after $i$ toys, there are two mutually exclusive paths. Either you had $j$ types already and drew a duplicate (probability $j/n$), or you had $j-1$ types and drew a new one (probability $\frac{n - (j-1)}{n}$). Thus, $p_{i,j} = p_{i-1, j}(\frac{j}{n}) + p_{i-1, j-1}(\frac{n-j+1}{n})$.
> > Part (b): Define base cases: $p_{1,1} = 1$, and $p_{i,j} = 0$ for $j \notin [1, i]$. Iteratively build a 2D table row by row for $i = 2, 3, \dots$, computing each $p_{i,j}$ using the two adjacent values from the previously computed row.
> > 
> > **Answer.** (a) $p_{i,j} = p_{i-1, j} \frac{j}{n} + p_{i-1, j-1} 
\frac{n-j+1}{n}$; (b) Initialize $p_{1,1} = 1$ and all invalid states to 0, 
then compute the values row by row (incrementing $i$). ✓

> [!example] Exercise 72 — A/B Testing
> **Problem.** A/B testing is a form of randomized experiment that is used by many companies to learn about how customers will react to different treatments. For example, a company may want to see how users will respond to a new feature on their website (compared with how users respond to the current version of the website) or compare two different advertisements. As the name suggests, two different treatments, Treatment A and Treatment B, are being studied. Users arrive one by one, and upon arrival are randomly assigned to one of the two treatments. The trial for each user is classified as "success" (e.g., the user made a purchase) or "failure". The probability that the nth user receives Treatment A is allowed to depend on the outcomes for the previous users. This set-up is known as a two-armed bandit. Many algorithms for how to randomize the treatment assignments have been studied. Here is an especially simple (but fickle) algorithm, called a stay-with-a-winner procedure: (i) Randomly assign the first user to Treatment A or Treatment B, with equal probabilities. (ii) If the trial for the nth user is a success, stay with the same treatment for the (n + 1)st user; otherwise, switch to the other treatment for the (n + 1)st user. Let a be the probability of success for Treatment A, and b be the probability of success for Treatment B. Assume that a ̸= b, but that a and b are unknown (which is why the test is needed). Let pn be the probability of success on the nth trial and an be the probability that Treatment A is assigned on the nth trial (using the above algorithm). (a) Show that pn = (a −b)an + b, an+1 = (a + b −1)an + 1 −b. (b) Use the results from (a) to show that pn+1 satisfies the following recursive equation: pn+1 = (a + b −1)pn + a + b −2ab. (c) Use the result from (b) to find the long-run probability of success for this algorithm, limn→∞pn, assuming that this limit exists.
> 
> > [!success]- Click to reveal solution
> > Part (a): By **LOTP** conditioning on the assigned treatment, $p_n = P(\text{Success}|A_n)P(A_n) + P(\text{Success}|B_n)P(B_n) = a(a_n) + b(1-a_n) = (a-b)a_n + b$. For $a_{n+1}$, condition on the treatment at step $n$ by **LOTP**: $a_{n+1} = P(A_{n+1}|A_n)a_n + P(A_{n+1}|B_n)(1-a_n)$. If $A_n$, we stay with $A$ if it succeeds (prob $a$). If $B_n$, we switch to $A$ if $B$ fails (prob $1-b$). Thus $a_{n+1} = a(a_n) + (1-b)(1-a_n) = (a+b-1)a_n + 1-b$.
> > Part (b): Isolate $a_n$ from the first equation: $a_n = \frac{p_n - b}{a-b}$. Substitute this into $p_{n+1} = (a-b)a_{n+1} + b$: $p_{n+1} = (a-b)[(a+b-1)a_n + 1-b] + b = (a+b-1)(a-b)a_n + (a-b)(1-b) + b$. Substitute $(a-b)a_n = p_n - b$: $p_{n+1} = (a+b-1)(p_n - b) + (a-b)(1-b) + b = (a+b-1)p_n - b(a+b-1) + a - ab - b + b^2 + b = (a+b-1)p_n + a + b - 2ab$.
> > Part (c): Let $\lim p_n = L$. Taking the limit of both sides gives $L = (a+b-1)L + a + b - 2ab$. Solving for $L$ yields $L(2-a-b) = a+b-2ab$.
> > 
> > **Answer.** (a) $p_n = a(a_n) + b(1-a_n) = (a-b)a_n + b$; $a_{n+1} = 
a(a_n) + (1-b)(1-a_n) = (a+b-1)a_n + 1-b$. (b) Substitute $a_n = 
\frac{p_n-b}{a-b}$ into $p_{n+1} = (a-b)a_{n+1} + b$ and simplify. (c) 
$\frac{a+b-2ab}{2-a-b}$. ✓

> [!example] Exercise 73 — Hardy-Weinberg
> **Problem.** In humans (and many other organisms), genes come in pairs. A certain gene comes in two types (alleles): type a and type A. The genotype of a person for that gene is the types of the two genes in the pair: AA, Aa, or aa (aA is equivalent to Aa). Assume that the Hardy-Weinberg law applies here, which means that the frequencies of AA, Aa, aa in the population are $p_{2}$, 2p(1 −p), (1 −p)2 respectively, for some p with 0 < p < 1. When a woman and a man have a child, the child's gene pair has one gene contributed by each parent. Suppose that the mother is equally likely to contribute either of the two genes in her gene pair, and likewise for the father, independently. Also suppose that the genotypes of the parents are independent of each other (with probabilities given by the Hardy-Weinberg law). (a) Find the probabilities of each possible genotype (AA, Aa, aa) for a child of two random parents. Explain what this says about stability of the Hardy-Weinberg law from one generation to the next. Hint: Condition on the genotypes of the parents. (b) A person of type AA or aa is called homozygous (for the gene under consideration), and a person of type Aa is called heterozygous (for that gene). Find the probability that a child is homozygous, given that both parents are homozygous. Also, find the probability that a child is heterozygous, given that both parents are heterozygous. (c) Suppose that having genotype aa results in a distinctive physical characteristic, so it is easy to tell by looking at someone whether or not they have that genotype. A mother and father, neither of whom are of type aa, have a child. The child is also not of type aa. Given this information, find the probability that the child is heterozygous. Hint: Use the definition of conditional probability. Then expand both the numerator and the denominator using LOTP, conditioning on the genotypes of the parents.
> 
> > [!success]- Click to reveal solution
> > Part (a): We use the **Law of Total Probability** by conditioning on the alleles passed by the parents. A parent of type $AA$ passes $A$ with probability $1$, $Aa$ passes $A$ with probability $1/2$, and $aa$ passes $A$ with probability $0$. The total probability that a random parent passes allele $A$ is $p^2(1) + 2p(1-p)(1/2) + (1-p)^2(0) = p^2 + p - p^2 = p$. The probability a parent passes $a$ is $1-p$. Since the parents' contributions are **independent**, the child's genotypes are simply the products of these probabilities: $P(AA) = p \cdot p$, $P(aa) = (1-p)(1-p)$, and $P(Aa) = p(1-p) + (1-p)p$.
> > Part (b): For the first question, condition on both parents being homozygous using the **definition of conditional probability**. Homozygous means being $AA$ or $aa$, with marginal probability $p^2 + (1-p)^2$. By **independence**, the joint probability of both parents being homozygous is $(p^2 + (1-p)^2)^2$. A child is homozygous if the parents are $(AA, AA)$ or $(aa, aa)$, which occurs with probability $p^4 + (1-p)^4$. For the second question, if both parents are heterozygous ($Aa$), they each pass $A$ with prob $1/2$ and $a$ with prob $1/2$. The child is heterozygous ($Aa$) if they receive $A$ from one and $a$ from the other, yielding $1/2 \cdot 1/2 + 1/2 \cdot 1/2 = 1/2$.
> > Part (c): Let $C$ be the condition that neither parent is $aa$ and the child is not $aa$. We want $P(\text{Child is } Aa | C)$. By the **definition of conditional probability** and the **Law of Total Probability**, we expand the numerator $P(\text{Child is } Aa \cap C)$ and the denominator $P(C)$ over the possible parent pairs: $(AA, AA)$, $(AA, Aa)$, $(Aa, AA)$, and $(Aa, Aa)$. Numerator: $p^4(0) + 2p^3(1-p)(1/2) + 2p^3(1-p)(1/2) + 4p^2(1-p)^2(1/2) = 2p^3(1-p) + 2p^2(1-p)^2 = 2p^2(1-p)$. Denominator: $p^4(1) + 2p^3(1-p)(1) + 2p^3(1-p)(1) + 4p^2(1-p)^2(3/4) = p^4 + 4p^3(1-p) + 3p^2(1-p)^2 = p^2(3-2p)$. Dividing numerator by denominator yields the result.
> > 
> > **Answer.** (a) $P(AA) = p^2$, $P(Aa) = 2p(1-p)$, $P(aa) = (1-p)^2$. 
This shows the Hardy-Weinberg law is completely stable; genotype frequencies 
remain identical from generation to generation. (b) $\frac{p^4 + (1-p)^4}{(p^2 
+ (1-p)^2)^2}$ and $\frac{1}{2}$. (c) $\frac{2(1-p)}{3-2p}$. ✓

> [!example] Exercise 74 — The Card After the First Ace
> **Problem.** A standard deck of cards will be shuffled and then the cards will be turned over one at a time until the first ace is revealed. Let B be the event that the next card in the deck will also be an ace. (a) Intuitively, how do you think P(B) compares in size with 1/13 (the overall proportion of aces in a deck of cards)? Explain your intuition. (Give an intuitive discussion rather than a mathematical calculation; the goal here is to describe your intuition explicitly.) (b) Let $C_{j}$ be the event that the first ace is at position j in the deck. Find P(B|$C_{j}$) in terms of j, fully simplified. (c) Using the law of total probability, find an expression for P(B) as a sum. (The sum can be left unsimplified, but it should be something that could easily be computed in software such as R that can calculate sums.) (d) Find a fully simplified expression for P(B) using a symmetry argument. Hint: If you were deciding whether to bet on the next card after the first ace being an ace or to bet on the last card in the deck being an ace, would you have a preference?
> 
> > [!success]- Click to reveal solution
> > Part (a): Intuitively, one might reason that because the first ace has already been "used up" and revealed, there are fewer aces left in the remaining portion of the deck, making the probability less than $1/13$. Alternatively, applying **symmetry**, one might intuit that knowing *where* the first ace sits tells us nothing special about the identity of the next card relative to any other card, so the probability should remain $1/13$.
> > Part (b): Using the **definition of conditional probability**, we condition on $C_j$, putting us in a restricted sample space. Out of the original 52 cards, the first $j$ cards have been revealed, leaving $52-j$ unknown cards. Because exactly one of the revealed cards was an ace, there are exactly 3 aces mixed among the $52-j$ remaining cards. Thus, the next card has a $\frac{3}{52-j}$ chance of being an ace.
> > Part (c): We apply the **Law of Total Probability** by summing $P(B|C_j)P(C_j)$ across all possible positions $j$. The probability $P(C_j)$ is the chance that the first $j-1$ cards are non-aces and the $j$-th is an ace. This is equivalent to choosing the positions for the remaining 3 aces out of the remaining $52-j$ slots, divided by the total combinations for 4 aces in 52 slots, which is $\frac{\binom{52-j}{3}}{\binom{52}{4}}$.
> > Part (d): Using **symmetry**, the 4 aces effectively divide the 48 non-aces into 5 segments (the cards before the 1st ace, between the 1st and 2nd, etc.). The event $B$ (the card after the first ace is an ace) occurs if and only if there are $0$ non-aces in the second segment. By symmetry, the probability that the second segment is empty is identically equal to the probability that the fifth segment is empty. The fifth segment is empty if and only if the absolute last card in the deck is an ace, which trivially has a prior probability of $4/52 = 1/13$.
> > 
> > **Answer.** (a) Intuitively, it may feel $< 1/13$ due to the 
depletion of one ace, or exactly $1/13$ due to symmetry. (b) $\frac{3}{52-j}$. 
(c) $\sum_{j=1}^{49} \frac{3}{52-j} \frac{\binom{52-j}{3}}{\binom{52}{4}}$. (d)
$\frac{1}{13}$. ✓
