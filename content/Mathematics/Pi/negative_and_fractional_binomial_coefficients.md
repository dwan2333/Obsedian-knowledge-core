# Negative & Fractional Binomial Coefficients

*Companion document to [Calculating Pi (Main)](<Calculating Pi (Main).md>) — the deep-dive behind §3.3–3.5, where Newton plugs $n = -1$ and $n = \tfrac12$ into the binomial theorem. This note answers two questions that note skips: **how** do you compute $\binom{n}{k}$ when $n$ is negative or fractional, and **what does it mean**?*

---

## Overview

The binomial theorem normally needs $n$ to be a positive integer. Newton's leap was to **keep the formula and drop the assumption**. To follow him you need two things — the *algebra* (how to calculate the coefficient) and the *concept* (why a "choose" with a negative or fractional top is meaningful). This note covers both, then connects back to the square-root and π series.

---

## 1. The algebra — calculating the coefficient

The factorial-free definition of the binomial coefficient is a **top-down product**: start at $n$ and multiply $k$ terms counting down, over $k!$.

> [!definition] Generalized binomial coefficient
> $$\binom{n}{k} = \frac{n\,(n-1)\,(n-2)\cdots(n-k+1)}{k!} \quad (k \text{ factors on top})$$
> Nothing here requires $n$ to be a whole number — the recipe is just "multiply $k$ things and divide by $k!$." That is what lets $n$ be negative or fractional.

For example, $\dbinom{5}{3} = \dfrac{5\times 4\times 3}{3!} = \dfrac{60}{6} = 10$.

### 1.1 Plugging in a negative number

Replace $n$ with $-n$ and run the *same* recipe — count down by 1 for $k$ terms:

$$\binom{-n}{k} = \frac{(-n)(-n-1)(-n-2)\cdots(-n-k+1)}{k!}$$

Every one of the $k$ factors on top is negative. Factor a $-1$ out of each → a global $(-1)^k$, and the insides flip sign and **count up** instead of down:

$$\binom{-n}{k} = (-1)^k\,\frac{n\,(n+1)\,(n+2)\cdots(n+k-1)}{k!}$$

That positive fraction is exactly $\dbinom{n+k-1}{k}$, which gives the headline identity:

> [!tip] The negative-binomial identity
> $$\binom{-n}{k} = (-1)^k \binom{n+k-1}{k}$$
> A negative-top coefficient is just an *ordinary* coefficient (with a shifted top) wearing an alternating sign.

### 1.2 Why that positive fraction equals $\binom{n+k-1}{k}$

Expand $\dbinom{n+k-1}{k}$ with the same top-down rule — start at $n+k-1$, count down $k$ terms:

- Term 1: $n+k-1$
- Term 2: $n+k-2$
- $\;\vdots$
- Term $k$: $(n+k-1)-(k-1) = n$

So the numerator is $(n+k-1)(n+k-2)\cdots(n+1)\,n$. Multiplication is order-independent, so reverse the list: $n\,(n+1)\cdots(n+k-1)$ — exactly $k$ terms counting **up** from $n$. That matches the fraction we produced after factoring out the negatives. ∎

> [!example] Sanity check — $\binom{-3}{2}$
> **Top-down:** $\dfrac{(-3)(-4)}{2!} = \dfrac{12}{2} = 6$.
> **Identity:** $(-1)^2\dbinom{3+2-1}{2} = \dbinom{4}{2} = \dfrac{4\times 3}{2} = 6$. ✓

---

## 2. The concept — why does this make sense?

"Choosing $k$ things from $-3$ items" is meaningless for card-dealing. But the coefficient is meaningful in two big arenas.

### 2.1 Infinite series (the negative exponent)

A negative exponent is a reciprocal: $(1+x)^{-1} = \dfrac{1}{1+x}$. Feed $n=-1$ into the binomial series:

$$(1+x)^{-1} = \binom{-1}{0}x^0 + \binom{-1}{1}x^1 + \binom{-1}{2}x^2 + \binom{-1}{3}x^3 + \cdots$$

By the identity, $\dbinom{-1}{k} = (-1)^k\dbinom{k}{k} = (-1)^k$, so the coefficients are $1,-1,1,-1,\dots$:

$$\frac{1}{1+x} = 1 - x + x^2 - x^3 + x^4 - \cdots$$

— the familiar geometric series. (The same "extend a finite formula into an infinite series" move expands $-\ln(1-x) = x + \tfrac{x^2}{2} + \tfrac{x^3}{3} + \cdots$; see [[Logarithm Fundamentals (Main)|Logarithm Fundamentals]].) The [Calculating Pi](<Calculating Pi (Main).md>) note verifies this exact expansion in §3.3 by multiplying back through by $(1+x)$.

### 2.2 Combinations *with* replacement (stars and bars)

The *absolute value* $\left|\binom{-n}{k}\right| = \binom{n+k-1}{k}$ has a clean combinatorial meaning — it's the **multiset coefficient**:

| Question | Coefficient |
|---|---|
| Choose $k$ of $n$ items, **no repeats** (order ignored) | $\dbinom{n}{k}$ |
| Choose $k$ of $n$ items, **repeats allowed** | $\dbinom{n+k-1}{k}$ |

> [!example] Ice-cream scoops (repeats allowed)
> **Problem.** A shop has $n=3$ flavours (vanilla, chocolate, strawberry). You want $k=2$ scoops in a bowl and may repeat a flavour. How many bowls?
> **Solution.** Repeats allowed → multiset coefficient $\dbinom{n+k-1}{k} = \dbinom{3+2-1}{2} = \dbinom{4}{2} = 6$.
> **Answer.** **6** — the pairs VV, CC, SS, VC, VS, CS.
> **Insight.** This is the "stars and bars" count, and it's the same number that the negative binomial coefficient $\bigl|\binom{-3}{2}\bigr|$ produces — the negative sign is just bookkeeping for the *series*, while the magnitude counts *multisets*.

---

## 3. Fractional $n$ — the square-root machine

If the recipe survives negatives, try a literal fraction, $n = \tfrac12$. Same top-down rule, subtracting $1$ each step:

| $k$ | $\dbinom{1/2}{k}$ | computation |
|---:|:---:|:---|
| 0 | $1$ | (anything choose 0) |
| 1 | $\tfrac12$ | $\tfrac{1/2}{1}$ |
| 2 | $-\tfrac18$ | $\dfrac{(\tfrac12)(-\tfrac12)}{2!} = \dfrac{-1/4}{2}$ |
| 3 | $\tfrac1{16}$ | $\dfrac{(\tfrac12)(-\tfrac12)(-\tfrac32)}{3!} = \dfrac{3/8}{6}$ |
| 4 | $-\tfrac5{128}$ | $\dfrac{(\tfrac12)(-\tfrac12)(-\tfrac32)(-\tfrac52)}{4!} = \dfrac{-15/16}{24}$ |

After the first step the signs alternate (each new factor $\tfrac12 - k$ is negative). Since $(1+x)^{1/2} = \sqrt{1+x}$, these coefficients build a square-root calculator:

$$\sqrt{1+x} = 1 + \tfrac12 x - \tfrac18 x^2 + \tfrac1{16} x^3 - \tfrac5{128} x^4 + \cdots$$

> [!tip] Why this was a big deal
> Before calculators, this *was* how square roots were computed. To get $\sqrt{1.1}$, set $x = 0.1$: because $x^2, x^3, \dots$ shrink fast, a handful of terms gives many correct digits. Choosing the rewrite that makes $|x|$ smallest is the whole game — the same convergence trick the [Calculating Pi](<Calculating Pi (Main).md>) note (§3.5, §5.2) uses to make Newton's π series practical (e.g. $\sqrt{3} = 2\sqrt{1 - \tfrac14}$, and integrating $\sqrt{1-x^2}$ only out to $x=\tfrac12$).

---

## Key Insight

The binomial coefficient is not really about "choosing" — it's a **product rule** ($k$ falling factors over $k!$). Once you see it that way, plugging in $-1$ or $\tfrac12$ is no stranger than plugging in $5$. A negative top gives the alternating coefficients of a reciprocal's series (and, in magnitude, counts multisets); a fractional top gives the coefficients of a root. Both are the engines under Newton's π calculation.

---

## Related Documents

- **[Calculating Pi (Main)](<Calculating Pi (Main).md>)** — the parent note. Uses $n=-1$ and $n=\tfrac12$ in the binomial series to turn a circle into a polynomial and integrate out $\pi$. This companion supplies the coefficient algebra and meaning behind that move.
- **[Logarithm Fundamentals (Main)](<../Logarithms/Logarithm Fundamentals (Main).md>)** — another "extend a finite formula into an infinite series" example: $-\ln(1-x) = x + \tfrac{x^2}{2} + \cdots$.
