# Chapter 1 — Probability and Counting

*Companion document to [Introduction to Probability (Main)](<../Introduction to Probability (Main).md>)*

_Research compiled 2026-04-17 — sourced from Blitzstein & Hwang (Introduction to Probability), MIT OpenCourseWare, Wikipedia, Statistics by Jim_

---

![Infographic](chapter1_infographic.png)

---

## Branch 1 — What Probability Is

Probability is a principled, logical framework for quantifying uncertainty and randomness. Rather than treating randomness as unknowable, it gives us tools to reason about it rigorously. The field applies across statistics and data science, physics (quantum mechanics), biology (genetics), computer science (algorithms and AI), finance (risk modeling), and medicine (clinical trials).

---

## Branch 2 — The Mathematical Framework

### Sample Space and Events

- **Sample space (S)**: The set of all possible outcomes of an experiment — can be finite, countably infinite, or uncountably infinite
- **Event (A)**: Any subset of the sample space
- **Pebble World**: A visualization tool for finite sample spaces — each outcome is a "pebble," and an event is a collection of pebbles
- **Set operations** on events: union (∪), intersection (∩), complement (Aᶜ) — De Morgan's laws connect these

### Probability Axioms

| Axiom                | Statement                                               |
| -------------------- | ------------------------------------------------------- |
| Non-negativity       | 0 ≤ P(A) ≤ 1 for all events A                           |
| Total probability    | P(S) = 1                                                |
| Countable additivity | For disjoint events: P(A₁ ∪ A₂ ∪ …) = P(A₁) + P(A₂) + … |

---

## Branch 3 — The Naive Definition of Probability

The **naive definition** states:

$$P_{naive}(A) = \frac{|A|}{|S|}$$

This counts favorable outcomes divided by total outcomes. It requires two strong assumptions: the sample space must be **finite**, and all outcomes must be **equally likely**.

It is valid when outcomes are equally likely by physical symmetry (fair coin, well-shuffled deck) or by experimental design (simple random sample). Misapplying it to unequal or indistinguishable objects leads to errors — as Leibniz famously demonstrated with dice sums.

---

## Branch 4 — Counting Techniques

Since sample spaces can be astronomically large, we need combinatorics to count them efficiently.

### Multiplication Rule

If a compound experiment has sequential stages with *a* and *b* outcomes respectively, the total number of outcomes is *a × b*. This generalises to any number of stages.

### Sampling

| Method | Formula | When to use |
|---|---|---|
| **With replacement** | nᵏ | Each draw is independent; items can repeat |
| **Without replacement** | n!/(n−k)! | Each draw removes the item; order matters |

### Permutations and Combinations

- **Permutations**: Arranging all *n* objects in order → *n!* possibilities
- **Binomial coefficient** $\binom{n}{k}$: Choosing *k* items from *n* where order does NOT matter

$$\binom{n}{k} = \frac{n!}{(n-k)!\, k!}$$

The formula adjusts for overcounting by dividing out the *k!* ways the chosen items can be rearranged.

### Bose-Einstein Counting (Stars and Bars)

Counts ways to place *k* indistinguishable particles into *n* distinguishable boxes:

$$\binom{n+k-1}{k}$$

---

## Branch 5 — Properties and Theorems

- **Complement rule**: P(Aᶜ) = 1 − P(A) — often easier to calculate the complement
- **Inclusion-exclusion**: For non-disjoint events, sum probabilities and subtract overlaps to avoid double-counting
- **Binomial theorem**: $(x+y)^n = \sum_{k=0}^{n} \binom{n}{k} x^k y^{n-k}$
- **Story proofs**: Combinatorial identities proved by interpretation rather than algebra (e.g. Vandermonde's identity, team captain argument)

---

## Branch 6 — Classic Examples

| Problem                    | Core Idea                                          | Result                                                 |
| -------------------------- | -------------------------------------------------- | ------------------------------------------------------ |
| **Birthday Problem**       | Probability ≥2 people share a birthday             | >50% with just 23 people                               |
| **Leibniz's Mistake**      | Treating distinguishable dice as indistinguishable | Wrong naive probability                                |
| **Newton-Pepys Problem**   | Comparing probabilities of dice outcomes           | P(≥1 six in 6) > P(≥2 sixes in 12) > P(≥3 sixes in 18) |
| **de Montmort's Matching** | Card game: at least one card matches its position  | Approaches 1 − 1/e ≈ 0.632 as deck grows               |
| **Bose-Einstein**          | Indistinguishable particles in boxes               | Stars and bars formula                                 |

---

## Key Takeaways

- Probability is built on set theory — master unions, intersections, and complements first
- The naive definition works only when outcomes are truly equally likely — beware assuming otherwise
- Counting is the engine of naive probability — multiplication rule, permutations, and combinations are the core toolkit
- The complement rule and inclusion-exclusion are the two most powerful shortcuts
- Real problems (birthday, de Montmort) show that human intuition about probability is often badly wrong

---

### Sources

| Source                                                            | Date | Type      |
| ----------------------------------------------------------------- | ---- | --------- |
| Blitzstein & Hwang, *Introduction to Probability* (Chapter 1)     | 2019 | Textbook  |
| MIT OpenCourseWare — Probability Theory: Sample Spaces and Events | 2024 | Academic  |
| Wikipedia — Birthday Problem, Stars and Bars, Twelvefold Way      | 2024 | Reference |
| Statistics by Jim — Permutation vs Combination                    | 2024 | Web       |
