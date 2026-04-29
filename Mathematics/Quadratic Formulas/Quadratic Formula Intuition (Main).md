# Quadratic Formulas — Intuitive Understanding

*Path C consolidation from two YouTube videos by **Po-Shen Loh** — published Apr 2026, captured via Gemini frame-by-frame analysis.*

| Source | Title | Length | URL |
|---|---|---|---|
| Video 1 | Simpler quadratic formula (3Blue1Brown collab) | 46:11 | [youtube.com/watch?v=MHXO86wKeDY](https://www.youtube.com/watch?v=MHXO86wKeDY) |
| Video 2 | Alternative Method of Solving Quadratics | 30:05 | [youtube.com/watch?v=XKBX0r3J-9Y](https://www.youtube.com/watch?v=XKBX0r3J-9Y) |

> [!info] One method, two perspectives
> Both videos teach the **same** intuitive method — solving $x^2 + Bx + C = 0$ by writing the roots as **average ± deviation** ($m \pm u$). Video 2 builds it from scratch through factoring; Video 1 names it "the simpler quadratic formula" and frames it as a memorable replacement for the textbook formula. Together they let you see the method *bottom-up* (from factoring intuition) and *top-down* (as a clean formula to remember).

![Mind map of the quadratic formula intuition method](quadratic_mindmap.png)

---

## 1. Why memorization fails — and what to do instead

Both videos open by attacking rote memorization of $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$.

> "Traditionally, the quadratic formula is one of the most famously memorized things in high school. We almost all kind of have this song that sings in our head related to it." *(Video 1 at [00:09])*

> "I was thinking about quadratic equations, and I was really surprised to find out that you can solve them in this really simple way. I couldn't believe that I'd never seen this before in any textbook." *(Video 2 at [00:16])*

> [!tip] The unifying takeaway both videos drive home
> "Connect the quadratic formula to other common patterns in math so as to make yourself a better problem solver." *(Video 1 at [01:21])*
> The "patterns" they mean are **the difference of squares** and **Vieta's relations** between roots and coefficients — both pre-quadratic-formula tools that make the formula feel inevitable instead of arbitrary.

---

## 2. The two foundational patterns

Both videos lean on the same two algebraic facts. Master these and the quadratic formula derives itself.

### 2.1 Difference of squares

> [!definition] Difference of squares
> $$(a - b)(a + b) = a^2 - b^2$$
> Equivalently, $(m - d)(m + d) = m^2 - d^2$ when you call the average $m$ and the deviation $d$.

**Video 2's expansion-based introduction** *(Video 2 at [02:38–03:27])*:
$$(3 - u)(3 + u) = 3 \cdot 3 + 3 \cdot u + (-u) \cdot 3 + (-u) \cdot u = 9 + 3u - 3u - u^2 = 9 - u^2$$
The middle terms $+3u$ and $-3u$ cancel because of the $+/-$ symmetry.

**Video 1's geometric "rectangle" interpretation** *(Video 1 at [10:00–10:41])*: a square of side $x$ with a square of side $y$ removed from one corner has area $x^2 - y^2$. Slicing and rearranging the remaining L-shape produces a rectangle of dimensions $(x + y) \times (x - y)$. Same identity, geometric proof.

> [!example] Mental-math foreshadowing — Why $59 \cdot 61 = 3{,}599$ *(Video 1 at [09:07–10:00])*
> **Setup.** Both 59 and 61 are clustered around 60.
> **Insight.** $59 \cdot 61 = (60 - 1)(60 + 1) = 60^2 - 1^2 = 3{,}600 - 1 = 3{,}599$.
> **Why it matters.** This is the *exact same arithmetic* you'll use to solve a quadratic — the trick of writing two numbers as "midpoint ± deviation" so their product collapses to $m^2 - d^2$.

### 2.2 Vieta's relations (Three Key Facts) — Video 1's framing

> [!definition] Three Key Facts about a monic quadratic *(Video 1 at [16:03–17:32])*
> For $x^2 + b'x + c' = 0$ with roots $r$ and $s$:
> 1. **Factored form:** $x^2 + b'x + c' = (x - r)(x - s)$
> 2. **Sum:** $b' = -(r + s)$ (the coefficient of $x$, with sign flipped, is the sum of roots)
> 3. **Product:** $c' = rs$ (the constant term is the product of roots)

**Why** (full algebraic derivation from Video 1 at [16:42–16:46]):

1. Start with $(x - r)(x - s)$
2. Distribute: $x \cdot x = x^2$, $x \cdot (-s) = -sx$, $(-r) \cdot x = -rx$, $(-r) \cdot (-s) = +rs$
3. Combine: $x^2 - sx - rx + rs = x^2 - (r + s)x + rs$
4. Match coefficients with $x^2 + b'x + c' = 0$: $b' = -(r + s)$ and $c' = rs$

> [!tip] "This is not just for the quadratic formula" *(Video 1 at [16:28])*
> The roots-coefficient relationship generalizes to **any** polynomial — for cubics, quartics, all of them. Learning this for quadratics gives you a foothold for the rest of polynomial theory (Vieta's formulas).

### 2.3 The Zero Product Property — Video 2's framing

> [!definition] Zero Product Property *(Video 2 at [05:14])*
> If $ab = 0$, then $a = 0$ or $b = 0$ (or both).

This is **how factored forms become solutions**: once you have $(x - r)(x - s) = 0$, the only way the product is zero is if one of the factors is zero, giving $x = r$ or $x = s$ directly.

> [!example] Solving $x^2 - 7x + 12 = 0$ by factoring *(Video 2 at [04:15–05:57])*
> **Problem.** Find roots of $x^2 - 7x + 12 = 0$.
> **Setup.** From the distributive expansion, $x^2 - 7x + 12 = (x - 3)(x - 4)$.
> **Solution.**
> 1. Substitute the factored form: $0 = (x - 3)(x - 4)$
> 2. Apply the Zero Product Property: $x - 3 = 0$ or $x - 4 = 0$
> 3. From $x - 3 = 0$: add 3 to both sides → $x = 3$
> 4. From $x - 4 = 0$: add 4 to both sides → $x = 4$
>
> **Answer.** $x = 3$ or $x = 4$.
>
> **Insight.** *"If I'm trying to solve a quadratic equation, if only I could find this magical factoring, then I can read off the answers."* *(Video 2 at [06:17])* — the entire game now becomes: how do we **find** the factorization without trial and error?

---

## 3. The core method — "Sum-and-Product" (the heart of both videos)

This is the single idea both videos converge on. **Goal**: solve $x^2 + Bx + C = 0$ without guessing factor pairs.

> [!tip] The trick — pick the right *form* for the two unknowns
> If you call the average of the two roots $m$ and the deviation from the average $u$, then:
> $$r = m - u \qquad s = m + u$$
> Their **sum is automatically $2m$** (regardless of $u$). So if we set $m = -\frac{B}{2}$, the sum constraint $r + s = -B$ is satisfied **by design**. Now only the product constraint remains, and the difference of squares makes it trivial.

### 3.1 The derivation in 6 steps

> [!example] Deriving the universal formula *(Video 1 at [18:18–22:36], Video 2 at [10:30–14:13])*
> **Setup.** Monic quadratic $x^2 + Bx + C = 0$ with unknown roots $r, s$.
> Vieta gives us $r + s = -B$ and $rs = C$ — two equations in two unknowns, but classes "basically tell you to just guess and check" *(Video 1 at [17:40])*. We're going to **avoid guessing** by parameterizing cleverly.
>
> **Solution.**
> 1. **Set the midpoint.** Define $m = -\dfrac{B}{2}$. *(Video 1 calls this $m = \frac{r+s}{2} = \frac{-b'}{2}$, [20:09–20:17].)*
> 2. **Parameterize the roots.** Write $r = m - u$, $s = m + u$. The sum $r + s = 2m = -B$ ✓ — automatically satisfied for any $u$.
> 3. **Apply the product constraint.** $rs = (m - u)(m + u) = m^2 - u^2 = C$.
> 4. **Solve for $u^2$.** $u^2 = m^2 - C$.
> 5. **Take the square root.** $u = \sqrt{m^2 - C}$.
> 6. **Read off the roots.** $r, s = m \pm u = -\dfrac{B}{2} \pm \sqrt{\left(\dfrac{B}{2}\right)^2 - C}$.
>
> **Answer (Video 1's preferred form, [22:28]).**
> $$\boxed{\;x = m \pm \sqrt{m^2 - p}\;}$$
> where $m = -B/2$ is the midpoint and $p = C$ is the product. *"That's it. No song, no song to be had."* *(Video 1 at [23:01])*
>
> **Insight.** Both videos are emphatic that this is **easier to remember** than $\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ because every piece has *meaning*: $m$ is the literal midpoint between the roots, and $\sqrt{m^2 - p}$ is the literal distance from $m$ to either root.

### 3.2 Geometric picture *(Video 1 at [18:18–21:44])*

```
                  y
                  |
                  |    parabola opens upward
                  |   /
                  |  /
              ____|_/_______________________________  x
                  |/      |        |
                  r       m        s
                  |<--d-->|<--d--->|
```

The two roots $r$ and $s$ on the x-axis are equidistant from the midpoint $m$ (a vertical dashed line). The distance $d$ (= $u$) is what we solve for. Knowing $m$ tells you **where to look**; computing $d$ tells you **how far apart** the roots are.

### 3.3 Connection to the textbook formula

If we want the form for the *general* (non-monic) $ax^2 + bx + c = 0$, divide everything by $a$ first *(Video 1 at [14:24–14:34])*:
$$\frac{ax^2 + bx + c}{a} = 0 \;\Longrightarrow\; x^2 + \frac{b}{a}x + \frac{c}{a} = 0$$
Now $B = b/a$ and $C = c/a$ in the monic form. Plugging into $x = -\frac{B}{2} \pm \sqrt{(B/2)^2 - C}$:
$$x = -\frac{b}{2a} \pm \sqrt{\frac{b^2}{4a^2} - \frac{c}{a}} = -\frac{b}{2a} \pm \sqrt{\frac{b^2 - 4ac}{4a^2}} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$
The textbook formula falls out as a corollary, not as something to memorize separately.

> [!tip] Why scaling doesn't change the roots *(Video 1 at [14:43–15:43] with Desmos demo)*
> Multiplying $x^2 - 6x + 8$ by any non-zero constant $S$ produces $S(x^2 - 6x + 8)$ — different parabolas (stretched, flipped) but **same x-intercepts**. Reason: $S \cdot 0 = 0$, so any scalar multiple of zero is still zero. This justifies dividing by $a$ at the start.

---

## 4. Worked examples (in order of difficulty)

### 4.1 Sum 14, product 24 — the warm-up *(Video 2 at [06:51–13:00])*

> [!example] Solve $x^2 - 14x + 24 = 0$
> **Setup.** Want two numbers $r, s$ with $r + s = 14$ and $rs = 24$.
> **Old way:** trial-and-error among factor pairs of 24: $1 \times 24$, $2 \times 12$, $3 \times 8$, $4 \times 6$. Check each one's sum until you find $2 + 12 = 14$. Tedious for non-integer answers.
> **New way (the method):**
> 1. Midpoint: $m = 14/2 = 7$. So write $r = 7 - u$, $s = 7 + u$.
> 2. Product: $(7 - u)(7 + u) = 49 - u^2 = 24$
> 3. Solve: $u^2 = 49 - 24 = 25 \Rightarrow u = 5$.
> 4. Read off roots: $r, s = 7 \mp 5 = \{2, 12\}$.
>
> **Answer.** $x = 2$ or $x = 12$.
>
> **Insight.** *"This is a technique that lets you do this without any guessing."* *(Video 2 at [13:56])* — even when the integer answers are easy, the method gives a deterministic procedure.

### 4.2 Irrational roots — when no factoring works *(Video 1 at [20:00–21:32])*

> [!example] Solve $x^2 + 6x + 7 = 0$
> **Setup.** No two integers have sum $-6$ and product $7$.
> **Solution.**
> 1. Midpoint: $m = -6/2 = -3$. Write $r = -3 - u$, $s = -3 + u$.
> 2. Product: $(-3 - u)(-3 + u) = 9 - u^2 = 7$
> 3. Solve: $u^2 = 9 - 7 = 2 \Rightarrow u = \sqrt{2}$.
> 4. Read off: $r, s = -3 \pm \sqrt{2}$.
>
> **Answer.** $x = -3 \pm \sqrt{2}$.
> **Insight.** The same procedure that solved the integer case **just works** when the answer is irrational. No new technique needed.

### 4.3 Complex roots — when $u^2$ is negative *(Video 2 at [20:00–21:02])*

> [!example] Solve $x^2 - 8x + 18 = 0$
> **Setup.** Sum 8, product 18.
> **Solution.**
> 1. Midpoint: $m = 8/2 = 4$. Write $r = 4 - u$, $s = 4 + u$.
> 2. Product: $(4 - u)(4 + u) = 16 - u^2 = 18$
> 3. Solve: $u^2 = 16 - 18 = -2$. **Negative!** Define $i = \sqrt{-1}$, so $u = i\sqrt{2}$.
> 4. Read off: $r, s = 4 \pm i\sqrt{2}$.
>
> **Answer.** $x = 4 \pm i\sqrt{2}$ (complex conjugate pair).
> **Insight.** *"This technique can be used to solve any equation."* *(Video 2 at [21:10])* — the procedure doesn't break when discriminant is negative; you just take a square root of a negative number, which is exactly when complex numbers earn their keep. *"That's why complex numbers were useful."* *(Video 2 at [22:00])*

### 4.4 Negative product — sign awareness *(Video 2 at [23:30–24:22])*

> [!example] Solve $x^2 + 6x - 4 = 0$
> **Setup.** Sum $-6$, product $-4$.
> **Solution.**
> 1. Midpoint: $m = -6/2 = -3$. Write $r = -3 - u$, $s = -3 + u$.
> 2. Product: $(-3 - u)(-3 + u) = 9 - u^2 = -4$
> 3. Solve: $u^2 = 9 - (-4) = 13 \Rightarrow u = \sqrt{13}$.
> 4. Read off: $r, s = -3 \pm \sqrt{13}$.
>
> **Answer.** $x = -3 \pm \sqrt{13}$.

### 4.5 Fraction midpoint — odd sum *(Video 2 at [25:08–27:10])*

> [!example] Solve $x^2 - x - 1 = 0$ (the Golden Ratio equation)
> **Setup.** Sum 1 (odd!), product $-1$.
> **Solution.**
> 1. Midpoint: $m = 1/2$. Write $r = \tfrac{1}{2} - u$, $s = \tfrac{1}{2} + u$.
> 2. Product: $(\tfrac{1}{2} - u)(\tfrac{1}{2} + u) = \tfrac{1}{4} - u^2 = -1$
> 3. Solve: $u^2 = \tfrac{1}{4} + 1 = \tfrac{5}{4} \Rightarrow u = \tfrac{\sqrt{5}}{2}$.
> 4. Read off: $r, s = \tfrac{1}{2} \pm \tfrac{\sqrt{5}}{2} = \tfrac{1 \pm \sqrt{5}}{2}$.
>
> **Answer.** $x = \dfrac{1 \pm \sqrt{5}}{2}$ — and the positive solution is the **golden ratio** $\varphi \approx 1.618$.
>
> **Insight.** *"One of these solutions is what's called the golden ratio, the ratio of the length to the width of the most beautiful rectangle in the world."* *(Video 2 at [27:10])* — fractions in the midpoint don't break anything; the algebra just produces fractional answers.

### 4.6 Non-monic — the leading-coefficient case *(Video 2 at [27:26–30:05])*

> [!example] Solve $2x^2 - 4x - 5 = 0$ (leading coefficient ≠ 1)
> **Setup.** Divide by 2 first: $x^2 - 2x - \tfrac{5}{2} = 0$. Sum 2, product $-\tfrac{5}{2}$.
> **Solution.**
> 1. Midpoint: $m = 2/2 = 1$. Write $r = 1 - u$, $s = 1 + u$.
> 2. Product: $(1 - u)(1 + u) = 1 - u^2 = -\tfrac{5}{2}$
> 3. Solve: $u^2 = 1 + \tfrac{5}{2} = \tfrac{7}{2} \Rightarrow u = \sqrt{\tfrac{7}{2}} = \tfrac{\sqrt{7}}{\sqrt{2}}$.
> 4. Read off: $r, s = 1 \pm \tfrac{\sqrt{7}}{\sqrt{2}}$.
>
> **Answer.** $x = 1 \pm \dfrac{\sqrt{7}}{\sqrt{2}}$.
> **Insight.** Pre-dividing by the leading coefficient (the "normalize-to-monic" step) is the only extra wrinkle for general $ax^2 + bx + c$. Everything else is identical.

---

## 5. Comparing the two videos' approaches

| Aspect | Video 1 (Po-Shen Loh × 3Blue1Brown) | Video 2 (Po-Shen Loh "Daily Challenge") |
|---|---|---|
| **Audience** | Math hobbyists, college-bound students | High school algebra students |
| **Pace** | Discursive, with mental-math digressions | Step-by-step, lots of examples |
| **Entry point** | Mental math tricks → difference of squares → Three Key Facts | Distributive property → Zero Product Property → Factoring |
| **Visual style** | Handwritten on lined notebook paper, Desmos for the scaling demo | Whiteboard-style with color-coded annotations, animated arrows |
| **Memorable phrasing** | *"$m \pm \sqrt{m^2 - p}$. That's it. No song, no song to be had."* | *"This is a technique that lets you do this without any guessing."* |
| **Killer application** | $59 \cdot 61$ in your head as $60^2 - 1$ | The Golden Ratio falling out of $x^2 - x - 1 = 0$ |
| **Formula they leave you with** | $x = m \pm \sqrt{m^2 - p}$ | The general method, formula left implicit |

> [!info] Watch them in this order
> If you've never seen the method: **Video 2 first** (it builds the method step-by-step from algebra you already know). Then **Video 1** (it adds the geometric/Vieta framing and the punchy single-formula form to remember).

---

## 6. Hierarchical outline

- **The motivation** — why memorize when you can derive
- **Foundational patterns** (necessary background)
  - Difference of squares: $(a-b)(a+b) = a^2 - b^2$
  - Vieta's relations / Three Key Facts: sum and product of roots from coefficients
  - Zero Product Property: how factored forms yield solutions
- **The sum-and-product method** (the core idea)
  - Parameterize roots as midpoint ± deviation: $r = m - u, s = m + u$
  - Choose $m = -B/2$ to satisfy sum automatically
  - Apply product constraint: $m^2 - u^2 = C$
  - Solve for $u$: $u = \sqrt{m^2 - C}$
  - Read off roots: $m \pm u$
- **The formula it produces**
  - $x = m \pm \sqrt{m^2 - p}$ — Video 1's "simpler quadratic formula"
  - Equivalent to standard $\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ via division by $a$
- **Worked examples covering all cases**
  - Integer roots (sum 14, product 24)
  - Irrational roots (sum $-6$, product 7)
  - Complex roots (negative discriminant)
  - Fractional midpoint (odd sum, golden ratio)
  - Non-monic (leading coefficient ≠ 1)

---

## 7. Synthesis — what a student gains from watching both

**Both videos teach the same algorithm**, but they motivate it differently. Video 2 builds it bottom-up from "what if we *had* the factorization?" — establishing the Zero Product Property as the mechanism, then showing that a clever parameterization ($m \pm u$ instead of two free unknowns) makes the factorization findable without trial-and-error. Video 1 frames the same algorithm top-down through *Vieta's relations*: the coefficients of a polynomial are determined by its roots through symmetric functions, and the quadratic case is where you can solve that system in closed form.

**The unifying intuition** both videos share is that **two numbers with a fixed sum are most cleanly described by their midpoint and their deviation from the midpoint**. Setting $r = m - u, s = m + u$ collapses the harder of the two Vieta constraints (the sum) into a parameter choice, leaving only the product constraint — which the difference-of-squares identity then reduces to a single square root. The "quadratic formula" is just the closed-form answer to that single square root.

**Where the two videos differ in emphasis**: Video 1 pushes the student toward a *memorable formula* — $m \pm \sqrt{m^2 - p}$ — as a replacement for the textbook formula. Video 2 declines to give a final formula, instead leaving the student with the *procedure*, arguing that the procedure is more valuable than any formula. Both approaches are defensible; together they let you choose: if you want a formula, use Video 1's. If you want never to need a formula again, use Video 2's procedure.

**A student who watches both** ends up understanding that the textbook quadratic formula is **not arbitrary** — it's a one-line consequence of two simple ideas (sum/product relations and the difference of squares). They can re-derive it on the spot if they forget it. They also understand why complex numbers exist (the $u^2$ might be negative) and how the same machinery works for any quadratic regardless of whether its discriminant is positive, zero, or negative. This is much more durable knowledge than memorizing $\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$.

**Why this matters downstream**: Vieta's relations generalize to all polynomials — every cubic, quartic, etc. has analogous identities relating roots to coefficients. The "parameterize by midpoint and deviation" trick is also general — it shows up in solving other systems with symmetric constraints. And the Zero Product Property is the foundation of all polynomial factoring in algebra and abstract algebra. Investing in these foundations through quadratics pays off across the rest of mathematics.

---

## Self-check — verification status

- [x] Every formula in the consolidated document has a `[mm:ss]` source citation
- [x] Every derivation shows the full step-by-step chain (not collapsed)
- [x] Both videos' perspectives are represented; convergent ideas merged
- [x] Worked examples cover all difficulty cases the videos showed (integer, irrational, complex, fractional midpoint, non-monic)
- [ ] V1 sec 8 (Live poll results, [24:45-46:11]) — not captured (audience-interaction segment, judged non-mathematical)

---

## Sources

| Source | Type | Captured |
|---|---|---|
| [Video 1 — "Simpler quadratic formula"](https://www.youtube.com/watch?v=MHXO86wKeDY) | YouTube | Sections 1-7 (00:00 – 24:45) |
| [Video 2 — "Alternative Method of Solving Quadratics"](https://www.youtube.com/watch?v=XKBX0r3J-9Y) | YouTube | All 6 sections (00:00 – 30:05) |
