# Chapter 4 — Exponential and Logarithmic Functions

*Companion document to [Precalculus 2e (Main)](<../Precalculus 2e (Main).md>) — coming soon*

_Research compiled 2026-06-01 — OpenStax, *Precalculus 2e*, Ch. 4 (pp. 407–534), with NotebookLM-assisted summaries and direct PDF figure extraction. End-of-section exercises are not included per request._

---

![Infographic](chapter4_infographic.png)

---

> [!info] Chapter Essence
> Chapter 4 develops two of the most useful function families in applied math — **exponentials** that model multiplicative growth and decay, and **logarithms**, their inverses that recover the unknown exponent. Together they describe compound interest, the number $e$ and continuous compounding, radioactive half-life, doubling time, Newton's law of cooling, and logistic growth toward a carrying capacity. The chapter develops their algebraic definitions, graph shapes, the four core log rules (product, quotient, power, change-of-base), techniques for solving exp/log equations, and the standard real-world models. The final section pivots to data, showing how exponential, logarithmic, and logistic regressions fit observed measurements.
>
> **Three core takeaways.** First, exponential and logarithmic functions are true inverses — converting between forms is the master move for solving equations. Second, the four log rules are simply the exponent rules read inside-out (multiplication of inputs becomes addition of logs, and so on). Third, this small toolkit covers an enormous range of real-world processes: radioactive decay, drug clearance, viral spread, technology adoption, cooling, and population growth.

---

## 4.1 Exponential Functions

Exponential functions model the kind of growth that compounds — money in an account, a deer population in a refuge, radioactive material decaying away. Unlike linear functions, which change by a constant **additive** amount per unit time, exponential functions change by a constant **multiplicative** factor. That single shift in arithmetic produces the dramatic acceleration (or rapid collapse) that gives the family its character.

> [!definition] Definition 4.1.1 — Exponential Function
> For any real number $x$, an **exponential function** has the form $f(x) = ab^x$, where $a$ is a non-zero real number called the **initial value** and $b$ is a positive real number with $b \neq 1$. The domain is all real numbers; the range is all positive reals when $a > 0$ and all negative reals when $a < 0$. The $y$-intercept is $(0, a)$, and the horizontal asymptote is $y = 0$.

![Figure 1 — graph of $f(x) = 2^x$ showing exponential growth](chapter4_fig_4.1_1_exp_growth_graph.png)

The base $b$ does the structural work: $b > 1$ produces growth, $0 < b < 1$ produces decay, and $b = 1$ collapses the function to the constant $a$ (hence the exclusion). The base must also be positive — otherwise $b^x$ is not real for fractional $x$ (e.g., $(-2)^{1/2}$).

> [!example] Example 4.1.1 — Identifying Exponential Functions
> **Problem.** Which of the following are exponential functions? $f(x) = 4^{3(x-2)}$, $g(x) = x^3$, $h(x) = (1/3)^x$, $j(x) = (-2)^x$.
> **Setup.** Test each candidate against the definition: a positive constant base raised to a variable exponent.
> **Solution.** $f$ has constant positive base $4$ and a variable exponent — exponential. $g(x) = x^3$ flips the roles: the *base* is the variable and the exponent is constant, so this is a power function, not exponential. $h$ has constant positive base $1/3$ — exponential (decay, since $b < 1$). $j(x) = (-2)^x$ violates the positivity requirement; for $x = 1/2$ it would demand a square root of a negative number.
> **Answer.** $g(x) = x^3$ and $j(x) = (-2)^x$ are *not* exponential functions.
> **Insight.** The base must be a positive constant not equal to $1$; the variable must sit in the exponent, not the base.

Evaluating an exponential function looks innocent but trips many students because of the order of operations — exponents resolve before the leading coefficient multiplies in.

> [!example] Example 4.1.2 — Evaluating $f(x) = 5 \cdot 3^{x+1}$ at $x = 2$
> **Problem.** Let $f(x) = 5(3)^{x+1}$. Evaluate $f(2)$ without a calculator.
> **Setup.** Substitute $x = 2$ and follow the order of operations: exponent first, then multiply.
> **Solution.** Substituting gives $f(2) = 5 \cdot 3^{2+1} = 5 \cdot 3^3$. Resolve the power: $3^3 = 27$. Then multiply: $5 \cdot 27 = 135$.
> **Answer.** $f(2) = 135$.
> **Insight.** A common mistake is to compute $5 \cdot 3 = 15$ first and then raise it to the third power — that would give $3375$, off by a factor of $25$. The leading coefficient is *not* part of the base.

### Exponential growth from data

The defining feature of exponential growth is that the *rate* of change is proportional to the current amount — bigger populations grow faster, bigger investments earn more interest.

![Figure 2 — Linear (Co. A) vs. exponential (Co. B) growth side-by-side](chapter4_fig_4.1_2_companies_linear_vs_exp.png)

The contrast above is the canonical picture: Company A's revenue grows by a fixed dollar amount each year (linear), while Company B's grows by a fixed *percentage* (exponential). Initially the linear line dominates, but the exponential curve eventually overtakes it and then runs away.

> [!definition] Definition 4.1.2 — Exponential Growth
> An **exponential growth** function has the form $f(x) = ab^x$ where $a > 0$ and $b > 1$. Here $a$ is the initial value and $b$ is the **growth factor** per unit increase in $x$. Equivalently, the function grows by a rate proportional to its current value.

Given two data points, we can recover the specific equation algebraically.

> [!tip] Writing an Exponential Model Given Two Points
> 1. If one point has the form $(0, a)$, then $a$ is the initial value. Substitute $a$ and the second point into $f(x) = ab^x$ and solve for $b$.
> 2. If neither point sits at $x = 0$, substitute both points to obtain a two-equation system in $a$ and $b$, and solve.
> 3. With $a$ and $b$ in hand, write the model as $f(x) = ab^x$.

> [!example] Example 4.1.3 — Deer Population in a Wildlife Refuge
> **Problem.** In 2006, 80 deer were introduced into a refuge. By 2012 the population had grown to 180. The growth is exponential. Write $N(t)$ giving the population $t$ years after 2006.
> **Setup.** Anchoring time at the introduction year ($t = 0$ in 2006) gives data points $(0, 80)$ and $(6, 180)$.
> **Solution.** The point $(0, 80)$ tells us $a = 80$ directly. Substituting $(6, 180)$ into $N(t) = 80 b^t$:
> $$180 = 80 b^6 \;\Longrightarrow\; b^6 = \frac{9}{4} \;\Longrightarrow\; b = \left(\frac{9}{4}\right)^{1/6} \approx 1.1447.$$
> **Answer.** $N(t) = 80(1.1447)^t$.
> **Insight.** Choosing $t = 0$ at the year of the first data point makes $a$ readable straight off the data and turns a two-equation system into a one-equation solve for $b$.

![Figure 3 — Deer population over time](chapter4_fig_4.1_3_deer_population_growth.png)

The same algebra applies when one of the two data points happens to come from a graph rather than a table.

> [!example] Example 4.1.4 — Decay from Two Off-Axis Points
> **Problem.** Find an exponential function passing through $(-2, 6)$ and $(2, 1)$.
> **Setup.** Neither point lies on the $y$-axis, so substitute both into $f(x) = ab^x$ and solve the two-equation system.
> **Solution.** The system is $6 = ab^{-2}$ and $1 = ab^2$. Dividing the second by the first:
> $$\frac{1}{6} = \frac{ab^2}{ab^{-2}} = b^4 \;\Longrightarrow\; b = \left(\tfrac{1}{6}\right)^{1/4} \approx 0.6389.$$
> Back-substitute into $1 = ab^2$ to get $a = 1/b^2 \approx 2.4495$.
> **Answer.** $f(x) \approx 2.4495 \cdot (0.6389)^x$.
> **Insight.** Dividing one equation by the other cancels $a$ and reduces the problem to a single equation in $b$ — a standard move whenever neither point sits at $x = 0$.

![Figure 4 — Decay function through $(-2, 6)$ and $(2, 1)$](chapter4_fig_4.1_4_exp_decay_two_points.png)

> [!example] Example 4.1.5 — Building an Exponential from a Graph
> **Problem.** Find an equation for the exponential function whose graph passes through $(0, 3)$ and $(2, 12)$.
> **Setup.** The $y$-intercept gives $a$ directly; the second point pins down $b$.
> **Solution.** From $(0, 3)$ we read $a = 3$. Substituting $(2, 12)$ into $f(x) = 3 b^x$:
> $$12 = 3 b^2 \;\Longrightarrow\; b^2 = 4 \;\Longrightarrow\; b = 2$$
> (taking the positive root since the base must be positive).
> **Answer.** $f(x) = 3 \cdot 2^x$.
> **Insight.** Pick the $y$-intercept whenever it is available — it isolates $a$ for free and avoids a system of equations.

![Figure 5 — Exponential through $(0, 3)$ and $(2, 12)$](chapter4_fig_4.1_5_exp_from_graph.png)

### Compound interest

A bank account earning $r$ percent annually, compounded $n$ times per year, is a textbook exponential.

> [!definition] Definition 4.1.3 — Compound Interest Formula
> An account with principal $P$, annual rate $r$ (as a decimal), compounded $n$ times per year, has value after $t$ years given by
> $$A(t) = P\left(1 + \frac{r}{n}\right)^{nt}.$$
> Each compounding period multiplies the balance by $\left(1 + \tfrac{r}{n}\right)$, and there are $nt$ such periods.

> [!example] Example 4.1.6 — Quarterly Compounding for 10 Years
> **Problem.** \$3{,}000 is invested at 3% annual interest, compounded quarterly. What is the balance after 10 years?
> **Setup.** $P = 3000$, $r = 0.03$, $n = 4$, $t = 10$.
> **Solution.** $A(10) = 3000\left(1 + 0.03/4\right)^{4 \cdot 10} = 3000 (1.0075)^{40} \approx 4045.05$.
> **Answer.** \$4{,}045.05.
> **Insight.** Each quarter the balance is multiplied by $1.0075$; after $40$ quarters the cumulative multiplier is roughly $1.35$.

The same formula, run in reverse, answers *present-value* questions: how much do I need to invest now to reach a target later?

> [!example] Example 4.1.7 — College-Savings Plan
> **Problem.** Lily wants a 529 plan to grow to \$40{,}000 in 18 years at 6% compounded semi-annually. To the nearest dollar, how much must she invest now?
> **Setup.** $A(18) = 40000$, $r = 0.06$, $n = 2$, $t = 18$; solve for $P$.
> **Solution.** $40000 = P(1 + 0.06/2)^{2(18)} = P(1.03)^{36}$, so $P = 40000 / (1.03)^{36} \approx 13801$.
> **Answer.** Lily needs to invest about \$13{,}801.
> **Insight.** Algebraically isolating $P$ converts the compound-interest formula into a present-value formula — the same equation, viewed from the other end.

### The number $e$ and continuous compounding

Push the compounding frequency $n$ in $\left(1 + \tfrac{r}{n}\right)^{nt}$ to infinity and the formula does not blow up — it converges to a finite limit involving the irrational constant $e$.

> [!definition] Definition 4.1.4 — Euler's Number $e$
> The number $e$ is the limit of $\left(1 + \tfrac{1}{n}\right)^n$ as $n \to \infty$. It is irrational, with $e \approx 2.718282$, and serves as the natural base for continuous exponential models.

> [!example] Example 4.1.8 — Evaluating $e^{3.14}$
> **Problem.** Compute $e^{3.14}$, rounded to five decimal places.
> **Setup.** Use the dedicated $e^x$ key on a scientific calculator.
> **Solution.** Press $e^x$, enter $3.14$, close the parenthesis, press ENTER.
> **Answer.** $e^{3.14} \approx 23.10387$.
> **Insight.** The $e^x$ button computes the natural exponential directly — there is no need to type $2.71828\ldots$ as a base.

> [!definition] Definition 4.1.5 — Continuous Growth and Decay
> For real $t$ and positive $a$, continuous growth or decay is modelled by
> $$A(t) = a e^{rt},$$
> where $a$ is the initial value, $r$ is the **continuous** rate per unit time, and $t$ is elapsed time. The sign of $r$ controls the direction: $r > 0$ for growth, $r < 0$ for decay. In financial contexts the formula is written $A(t) = P e^{rt}$.

> [!example] Example 4.1.9 — Continuously Compounded Interest
> **Problem.** \$1{,}000 is invested at a nominal 10% per year, compounded continuously. What is the balance after one year?
> **Setup.** $P = 1000$, $r = 0.10$, $t = 1$, using $A(t) = P e^{rt}$.
> **Solution.** $A(1) = 1000 e^{0.10 \cdot 1} = 1000 e^{0.10} \approx 1105.17$.
> **Answer.** \$1{,}105.17.
> **Insight.** Continuous compounding yields the theoretical *maximum* return for a given nominal rate — finer compounding always helps, but converges quickly to this limit.

> [!example] Example 4.1.10 — Decay of Radon-222
> **Problem.** Radon-222 decays continuously at 17.3% per day. How much remains of a 100 mg sample after 3 days?
> **Setup.** Decay requires a negative rate: $r = -0.173$, $a = 100$, $t = 3$.
> **Solution.** $A(3) = 100 e^{-0.173 \cdot 3} = 100 e^{-0.519} \approx 59.5115$ mg.
> **Answer.** About $59.5115$ mg remain.
> **Insight.** "17.3% per day" sounds like a *discrete* rate but is being used as a *continuous* one — read the problem carefully and flip the sign before plugging in.

---

## 4.2 Graphs of Exponential Functions

Every exponential graph has the same general silhouette: a flat tail hugging the $x$-axis on one side, a soaring tail on the other, and a smooth monotonic curve in between. Transformations move and stretch this silhouette around the plane but do not break it — the basic shape is preserved.

> [!definition] Definition 4.2.1 — Parent Function $f(x) = b^x$
> An exponential function with the form $f(x) = b^x$ ($b > 0$, $b \neq 1$) is one-to-one with domain $(-\infty, \infty)$ and range $(0, \infty)$. The horizontal asymptote is $y = 0$ and the $y$-intercept is $(0, 1)$. The function is increasing if $b > 1$ and decreasing if $0 < b < 1$; it has no $x$-intercept.

![Figure 1 — Parent growth shape ($b > 1$) with horizontal asymptote $y = 0$](chapter4_fig_4.2_1_exp_growth_shape.png)

When $b > 1$, the curve rises slowly on the left, crosses through $(0, 1)$, and accelerates upward. Decay reverses this picture: the curve falls from a high left tail through $(0, 1)$ and flattens toward the $x$-axis on the right.

![Figure 2 — Parent decay shape ($0 < b < 1$)](chapter4_fig_4.2_2_exp_decay_shape.png)

Putting growth and decay side by side highlights that they are mirror images of one another across the $y$-axis. Both share the same horizontal asymptote, the same $y$-intercept $(0, 1)$, and the same domain and range — only the *direction* of motion is reversed.

![Figure 3 — Growth and decay compared](chapter4_fig_4.2_3_growth_decay_comparison.png)

> [!example] Example 4.2.1 — Graphing $f(x) = 0.25^x$
> **Problem.** Sketch $f(x) = 0.25^x$ and state its domain, range, and asymptote.
> **Setup.** The base is $b = 0.25 < 1$, so the function is decreasing.
> **Solution.** Tabulate a few points: $f(-1) = 0.25^{-1} = 4$, $f(0) = 1$, $f(1) = 0.25$. Plot $(-1, 4)$, $(0, 1)$, $(1, 0.25)$ and connect with a smooth curve. The left tail rises without bound; the right tail approaches $y = 0$.
> **Answer.** Domain $(-\infty, \infty)$; range $(0, \infty)$; horizontal asymptote $y = 0$.
> **Insight.** A base under $1$ produces the mirror-image of standard growth — the curve falls from high left to a flat right tail.

![Figure 4 — Graph of $f(x) = 0.25^x$](chapter4_fig_4.2_4_exp_quarter_x.png)

### Shifts

Adding constants inside or outside the exponent translates the graph rigidly without changing its shape.

> [!definition] Definition 4.2.2 — Shifts of $f(x) = b^x$
> For constants $c$ and $d$, the function $f(x) = b^{x+c} + d$ shifts the parent $y = b^x$ vertically by $d$ (same direction as the sign of $d$) and horizontally by $c$ (*opposite* direction to the sign of $c$). The $y$-intercept becomes $(0, b^c + d)$, the horizontal asymptote becomes $y = d$, and the range becomes $(d, \infty)$. The domain is unchanged.

> [!example] Example 4.2.2 — Shifting $2^x$ Left and Down
> **Problem.** Graph $f(x) = 2^{x+1} - 3$. State the domain, range, and asymptote.
> **Setup.** Read the parameters from $f(x) = b^{x+c} + d$: $b = 2$, $c = 1$, $d = -3$.
> **Solution.** Draw the new asymptote $y = -3$. The shift vector is $(-c, d) = (-1, -3)$, so translate the parent $2^x$ left 1 and down 3. The new $y$-intercept is $(0, 2^1 - 3) = (0, -1)$.
> **Answer.** Domain $(-\infty, \infty)$; range $(-3, \infty)$; asymptote $y = -3$.
> **Insight.** The *opposite-sign* rule for horizontal shifts trips students up: $b^{x+1}$ shifts the parent **left**, not right.

![Figure 7 — Graph of $f(x) = 2^{x+1} - 3$](chapter4_fig_4.2_7_horizontal_vertical_shifts.png)

When algebraic methods are inconvenient, intersecting an exponential curve with a horizontal line on a graphing calculator yields a quick numerical solution.

> [!example] Example 4.2.3 — Solving Graphically
> **Problem.** Solve $42 = 1.2 \cdot 5^x + 2.8$ graphically, to the nearest thousandth.
> **Setup.** Set $Y_1 = 1.2(5)^x + 2.8$ and $Y_2 = 42$; find the intersection.
> **Solution.** Enter both functions on a graphing calculator. Adjust the window (e.g., $x \in [-3, 3]$, $y \in [-5, 55]$) so the intersection is visible. Use the **intersect** feature to read off the $x$-coordinate.
> **Answer.** $x \approx 2.166$.
> **Insight.** A horizontal-line intersection is the graphical version of "$f(x) = $ constant"; the technique generalizes to any non-algebraic root-finding.

### Stretches and compressions

Multiplying the parent function by a positive constant scales it vertically without altering its asymptote.

> [!definition] Definition 4.2.3 — Stretches and Compressions of $f(x) = b^x$
> For $a > 0$, the function $f(x) = a \cdot b^x$ stretches the parent $b^x$ vertically by a factor of $a$ when $a > 1$ and compresses it vertically when $0 < a < 1$. The $y$-intercept becomes $(0, a)$. The asymptote $y = 0$, the range $(0, \infty)$, and the domain $(-\infty, \infty)$ are unchanged from the parent.

> [!example] Example 4.2.4 — Stretched Decay
> **Problem.** Sketch $f(x) = 4 \cdot (1/2)^x$ and state its domain, range, and asymptote.
> **Setup.** Base $b = 1/2$ (decay); stretch factor $a = 4$.
> **Solution.** Compute key points: $f(-1) = 4 \cdot 2 = 8$, $f(0) = 4$, $f(1) = 2$. The shape is decay (left tail rises, right tail flattens toward $y = 0$), but every $y$-coordinate is four times the parent's.
> **Answer.** Domain $(-\infty, \infty)$; range $(0, \infty)$; asymptote $y = 0$.
> **Insight.** Vertical stretching scales the $y$-intercept by exactly $a$ — here from $(0, 1)$ to $(0, 4)$ — while leaving the asymptote and overall direction of the curve intact.

![Figure 8 — Vertical stretch of $2^x$](chapter4_fig_4.2_8_stretches_compressions.png)

### Reflections

Introducing a negative sign flips the graph across one of the coordinate axes.

> [!definition] Definition 4.2.4 — Reflections of $f(x) = b^x$
> The function $f(x) = -b^x$ reflects the parent across the **$x$-axis**: the $y$-intercept becomes $(0, -1)$ and the range becomes $(-\infty, 0)$, while the asymptote $y = 0$ and the domain are unchanged. The function $f(x) = b^{-x}$ reflects the parent across the **$y$-axis**: the $y$-intercept stays at $(0, 1)$, and the asymptote, range, and domain are unchanged — only the direction of growth flips (growth becomes decay and vice versa).

> [!example] Example 4.2.5 — Reflecting Across the $x$-Axis
> **Problem.** Find $g(x)$ that reflects $f(x) = (1/4)^x$ across the $x$-axis. State its domain, range, and asymptote.
> **Setup.** Reflecting across the $x$-axis negates the output: $g(x) = -f(x)$.
> **Solution.** $g(x) = -(1/4)^x$. Sample values: $g(-1) = -4$, $g(0) = -1$, $g(1) = -0.25$. Plot through $(0, -1)$.
> **Answer.** $g(x) = -(1/4)^x$; domain $(-\infty, \infty)$; range $(-\infty, 0)$; asymptote $y = 0$.
> **Insight.** Negating the output flips every $y$-value across the $x$-axis, turning a positive range into a negative one.

![Figure 10 — Reflections of $2^x$ across the $x$- and $y$-axes](chapter4_fig_4.2_10_reflections.png)

### Combining transformations

All three operations — shifts, scaling, and reflection — fit into a single template.

> [!definition] Definition 4.2.5 — General Translation of an Exponential Function
> A general translation has the form
> $$f(x) = a \cdot b^{x+c} + d,$$
> where the parent $y = b^x$ (with $b > 1$) is shifted left by $c$ units, scaled vertically by $|a|$ (stretch if $|a| > 1$, compression if $0 < |a| < 1$), shifted vertically by $d$, and reflected across the $x$-axis when $a < 0$.

> [!example] Example 4.2.6 — Translating from a Verbal Description
> **Problem.** Starting from $f(x) = e^x$: stretch vertically by $2$, reflect across the $y$-axis, then shift up $4$ units. Write the equation and give the domain, range, and asymptote.
> **Setup.** Match each phrase to a parameter of $f(x) = a b^{x+c} + d$ with $b = e$.
> **Solution.** Vertical stretch by $2$ gives $a = 2$. Reflection across the $y$-axis replaces $x$ with $-x$. Vertical shift of $+4$ gives $d = 4$. Assembling: $f(x) = 2 e^{-x} + 4$.
> **Answer.** $f(x) = 2 e^{-x} + 4$; domain $(-\infty, \infty)$; range $(4, \infty)$; asymptote $y = 4$.
> **Insight.** Each English phrase ("stretch by 2", "reflect across $y$-axis", "shift up 4") maps cleanly to a single parameter in the template — once you spot the mapping, the rest is just substitution.

---

## 4.3 Logarithmic Functions

![Figure 1 — 2011 Honshu earthquake: motivation for logarithmic scales](chapter4_fig_4.3_1_earthquake_motivation.png)

The 2011 Honshu earthquake released roughly $500$ times the energy of the next-largest quake that year, yet its Richter magnitude differed by only about $2.7$ units. That compression — turning a multiplicative blow-up into a small additive number — is exactly what logarithms do. When the base $b$ and the result $x$ of an exponential relation are known but the exponent is the unknown, the logarithm is the function that recovers it. In this sense the logarithm is the **inverse of the exponential**: where $b^y$ asks *"what value do we get from raising $b$ to the power $y$?"*, $\log_b(x)$ asks *"what power of $b$ produces $x$?"*

> [!definition] Logarithmic Function
> For $x > 0$, $b > 0$, and $b \neq 1$, the equation $y = \log_b(x)$ is equivalent to $b^y = x$. In other words, $\log_b(x)$ is the exponent to which $b$ must be raised to produce $x$. The domain of $\log_b$ is $(0, \infty)$ and its range is $(-\infty, \infty)$.

A logarithm of a negative number or of zero is never defined. Since any positive base raised to a real exponent produces a positive output, no real exponent could ever push $b^y$ down to zero or below. The restriction $x > 0$ on the domain is therefore not an arbitrary convention — it is forced by the inverse relationship itself.

![Figure 2 — Graphical estimation of $\log_2 8$](chapter4_fig_4.3_2_log_estimation_graph.png)

Before reaching for algebra, it is worth recognizing that many logarithms can be read directly off a graph or from memory: $\log_2(8)$ is the height at which the curve $y = 2^x$ reaches $8$, and a moment's reflection on the powers of $2$ gives $\log_2(8) = 3$. The same idea — *find the exponent that hits the target* — drives every algebraic evaluation below.

> [!tip] Converting Between Exponential and Logarithmic Forms
> To pass from $y = \log_b(x)$ to $b^y = x$, identify the base $b$, the exponent $y$, and the argument $x$, then write them as an exponential equation. To go the other direction, identify the same three quantities in $b^y = x$ and write $y = \log_b(x)$. The base of the exponent is always the base of the logarithm.

> [!example] Example 1 — Logarithmic to Exponential Form
> **Problem.** Rewrite each logarithmic equation in exponential form: (a) $\log_6(\sqrt{6}) = \tfrac{1}{2}$, and (b) $\log_3(9) = 2$.
> **Setup.** Each equation has the shape $y = \log_b(x)$. Identify $b$, $y$, $x$ in each, then write $b^y = x$.
> **Solution.** For (a), the base is $b = 6$, the exponent is $y = \tfrac{1}{2}$, and the argument is $x = \sqrt{6}$. For (b), $b = 3$, $y = 2$, $x = 9$.
> **Answer.** (a) $6^{1/2} = \sqrt{6}$. (b) $3^2 = 9$.
> **Insight.** A logarithmic statement is just an exponential statement written with the exponent isolated on the left.

The reverse direction — turning an exponential into a logarithm — is mechanically the same translation.

> [!example] Example 2 — Exponential to Logarithmic Form
> **Problem.** Rewrite each exponential equation in logarithmic form: (a) $2^3 = 8$, (b) $5^2 = 25$, (c) $10^{-4} = \tfrac{1}{10{,}000}$.
> **Setup.** Each has shape $b^y = x$. Identify $b$, $y$, $x$ and rewrite as $y = \log_b(x)$.
> **Solution.** (a) $b=2$, $y=3$, $x=8$; (b) $b=5$, $y=2$, $x=25$; (c) $b=10$, $y=-4$, $x=\tfrac{1}{10{,}000}$.
> **Answer.** (a) $\log_2(8) = 3$. (b) $\log_5(25) = 2$. (c) $\log_{10}\!\left(\tfrac{1}{10{,}000}\right) = -4$.
> **Insight.** The logarithm is just a name for "the exponent that was used." Any exponential fact can be read aloud as a logarithm of its result.

Once the conversion is automatic, many logarithms can be evaluated mentally by asking *"what exponent of $b$ produces $x$?"* and matching against familiar powers, roots, and reciprocals.

> [!example] Example 3 — Evaluating $\log_4(64)$
> **Problem.** Compute $\log_4(64)$ without a calculator.
> **Setup.** Rewrite as the exponential equation $4^y = 64$ and find the exponent $y$.
> **Solution.** Test small powers of $4$: $4^1 = 4$, $4^2 = 16$, $4^3 = 64$. The third matches.
> **Answer.** $\log_4(64) = 3$.
> **Insight.** Mental evaluation relies on recognizing the argument as a familiar power of the base.

Reciprocals introduce negative exponents through the rule $b^{-n} = 1/b^n$, so logarithms of fractions whose denominators are powers of the base are usually negative.

> [!example] Example 4 — Evaluating $\log_3(\tfrac{1}{27})$
> **Problem.** Compute $\log_3\!\left(\tfrac{1}{27}\right)$ without a calculator.
> **Setup.** Rewrite as $3^y = \tfrac{1}{27}$.
> **Solution.** Since $3^3 = 27$, the reciprocal rule gives $3^{-3} = \tfrac{1}{27}$.
> **Answer.** $-3$.
> **Insight.** Taking a logarithm of a reciprocal flips the sign of the exponent — the algebraic mirror of $b^{-n} = 1/b^n$.

When a logarithm is written without an explicit base, the base is taken to be $10$. This convention is so widespread that base-$10$ logarithms have their own name and symbol.

> [!definition] Common Logarithm
> The **common logarithm** is the logarithm of base $10$. We write $\log_{10}(x)$ simply as $\log(x)$. For $x > 0$, the statement $y = \log(x)$ is equivalent to $10^y = x$ — that is, $y$ is the exponent to which $10$ must be raised to give $x$.

The common logarithm is natural for any quantity that spans many orders of magnitude — sound pressure (decibels), acidity (pH), seismic energy (Richter), or simply the number of digits a positive integer has.

> [!example] Example 5 — Evaluating $\log(1000)$
> **Problem.** Compute $\log(1000)$ without a calculator.
> **Setup.** Rewrite as $10^y = 1000$.
> **Solution.** $10^3 = 1000$.
> **Answer.** $3$.
> **Insight.** For exact powers of $10$, the common logarithm just counts how many factors of $10$ are stacked up.

For arguments that are not exact powers of $10$, a calculator interpolates between the nearest powers.

> [!example] Example 6 — Approximating $\log(321)$
> **Problem.** Evaluate $\log(321)$ to four decimal places.
> **Setup.** Use the [LOG] key. Since $321$ lies between $100 = 10^2$ and $1000 = 10^3$, the answer must lie between $2$ and $3$.
> **Solution.** Pressing [LOG] 321 [ENTER] returns $2.5065\ldots$, consistent with the bracketing estimate.
> **Answer.** $\log(321) \approx 2.5065$.
> **Insight.** Bracketing by neighboring integer powers of $10$ is a free sanity check on any calculator output.

The common logarithm scales real-world phenomena that grow multiplicatively. The Richter scale is a canonical example: a Richter increase of $1$ corresponds to a tenfold increase in seismic energy.

> [!example] Example 7 — Earthquake Magnitude Difference
> **Problem.** One earthquake releases $500$ times the energy of another. The equation $10^x = 500$ relates the energy ratio to $x$, the difference in Richter magnitudes. To the nearest thousandth, what is $x$?
> **Setup.** Solve $10^x = 500$ by taking the common logarithm of both sides.
> **Solution.** Rewriting gives $x = \log(500)$. A calculator returns $\log(500) \approx 2.6990$.
> **Answer.** $x \approx 2.699$.
> **Insight.** Multiplicative jumps in raw quantity become small additive differences on the logarithmic scale — the entire reason the Richter scale exists.

In calculus, the most useful base is not $10$ but the irrational constant $e \approx 2.71828$, the base for which the exponential function $e^x$ is its own derivative. Logarithms in base $e$ are called **natural logarithms** and have their own symbol.

> [!definition] Natural Logarithm
> The **natural logarithm** is the logarithm of base $e$. We write $\log_e(x)$ simply as $\ln(x)$. For $x > 0$, the statement $y = \ln(x)$ is equivalent to $e^y = x$. Because $\ln$ and $e^x$ are inverse functions, $\ln(e^x) = x$ for all $x$, and $e^{\ln(x)} = x$ for $x > 0$.

> [!example] Example 8 — Approximating $\ln(500)$
> **Problem.** Evaluate $\ln(500)$ to four decimal places.
> **Setup.** Use the dedicated [LN] key.
> **Solution.** [LN] 500 [ENTER] returns $6.2146\ldots$.
> **Answer.** $\ln(500) \approx 6.2146$.
> **Insight.** The natural log of the same input is always larger than its common log — because $e < 10$, more factors of $e$ are needed to reach the same target.

---

## 4.4 Graphs of Logarithmic Functions

Because $y = \log_b(x)$ is the inverse of $y = b^x$, every feature of the logarithmic graph is a reflection of an exponential feature across the line $y = x$. Domain and range swap, intercepts swap, and the horizontal asymptote of the exponential becomes the vertical asymptote of the logarithm. Recognizing this reflection is the fastest way to anticipate the shape of any logarithmic graph before plotting a single point.

### Finding the Domain

> [!definition] Domain and Range of $f(x) = \log_b(x)$
> The exponential $y = b^x$ has domain $(-\infty, \infty)$ and range $(0, \infty)$. As its inverse, $y = \log_b(x)$ has these swapped: domain $(0, \infty)$, range $(-\infty, \infty)$. The argument of any logarithm must therefore be strictly positive.

When a logarithm is composed with an inner expression — for example $\log_2(2x - 3)$ or $\log(5 - 2x)$ — the rule "argument $> 0$" becomes an inequality that pins down the domain.

> [!tip] How To — Identify the Domain of a Logarithmic Function
> Write the inequality *argument* $> 0$, solve for $x$, and express the solution in interval notation. Watch sign-flips: multiplying or dividing by a negative number reverses the inequality.

> [!example] Example 1 — Domain of $f(x) = \log_2(2x - 3)$
> **Problem.** Find the domain.
> **Setup.** The argument is $2x - 3$. Set it strictly greater than zero.
> **Solution.** $2x - 3 > 0 \Rightarrow 2x > 3 \Rightarrow x > \tfrac{3}{2}$.
> **Answer.** Domain $= (\tfrac{3}{2}, \infty)$.
> **Insight.** A horizontal compression-and-shift moves the asymptote off zero; the domain inherits the new boundary.

> [!example] Example 2 — Domain of $f(x) = \log(5 - 2x)$
> **Problem.** Find the domain.
> **Setup.** Set the argument $5 - 2x > 0$.
> **Solution.** $-2x > -5 \Rightarrow x < \tfrac{5}{2}$ (the inequality flips when dividing by $-2$).
> **Answer.** Domain $= (-\infty, \tfrac{5}{2})$.
> **Insight.** A negative coefficient on the inside reflects the function across the $y$-axis, turning a right-bounded domain into a left-bounded one.

### Graphing the Parent Function

The parent logarithm $f(x) = \log_b(x)$ has a small set of features that repeat across every base. Memorizing these — and a few key points — is enough to sketch any logarithmic curve.

> [!definition] Parent Function $f(x) = \log_b(x)$
> For $b > 0$, $b \neq 1$, the parent logarithm is a one-to-one function with vertical asymptote $x = 0$, domain $(0, \infty)$, range $(-\infty, \infty)$, $x$-intercept at $(1, 0)$, and key point $(b, 1)$. There is no $y$-intercept. The curve is increasing when $b > 1$ and decreasing when $0 < b < 1$.

> [!tip] How To — Graph $f(x) = \log_b(x)$
> Draw the vertical asymptote $x = 0$, plot $(1, 0)$ and $(b, 1)$, and sketch a smooth curve through them that hugs the asymptote on the left and rises slowly on the right. State the domain, range, and asymptote.

> [!example] Example 3 — Graphing $f(x) = \log_5(x)$
> **Problem.** Graph $f(x) = \log_5(x)$ and state the domain, range, and asymptote.
> **Setup.** Base $b = 5 > 1$, so the function increases.
> **Solution.** The vertical asymptote is $x = 0$, the $x$-intercept is $(1, 0)$, and the key point is $(5, 1)$. Connect with a smooth increasing curve hugging the asymptote.
> **Answer.** Domain $(0, \infty)$, range $(-\infty, \infty)$, vertical asymptote $x = 0$.
> **Insight.** Larger bases produce visibly flatter logarithmic curves — the bigger the base, the more input is needed before the output budges.

![Figure 4 — Three logarithmic functions with bases $b > 1$](chapter4_fig_4.4_4_three_log_bases.png)

Comparing $\log_2$, $\log_4$, and $\log_{10}$ on the same axes makes the role of the base visible: all three pass through $(1, 0)$, but each $\log_b$ passes through the signature point $(b, 1)$, so a larger $b$ pushes that landmark farther to the right and the curve looks correspondingly flatter.

### Transformations

Logarithmic graphs admit the full menu of rigid and scaled transformations — horizontal and vertical shifts, vertical stretches and compressions, and reflections — without losing their characteristic shape.

#### Horizontal Shifts

> [!definition] Horizontal Shifts
> For a constant $c$, the function $f(x) = \log_b(x + c)$ shifts the parent function left by $c$ if $c > 0$ and right by $|c|$ if $c < 0$. The vertical asymptote moves to $x = -c$, the domain becomes $(-c, \infty)$, and the range remains $(-\infty, \infty)$.

![Figure 5 — Horizontal shifts of the parent log](chapter4_fig_4.4_5_log_horizontal_shifts.png)

Horizontal shifts drag both the asymptote and the domain along with the graph. The range, however, is unaffected — a horizontal slide cannot change which $y$-values are reachable.

> [!tip] How To — Graph a Horizontal Shift
> Read off the shift $c$ from $\log_b(x + c)$. Draw the new asymptote $x = -c$. Take three reference points from the parent function and subtract $c$ from each $x$-coordinate. Plot, connect, and state the new domain.

> [!example] Example 4 — Graphing $f(x) = \log_3(x - 2)$
> **Problem.** Sketch alongside the parent, label key points and asymptote, and state domain, range, and asymptote.
> **Setup.** Match to $\log_b(x + c)$ with $c = -2$, a shift right by $2$.
> **Solution.** Asymptote: $x = 2$. Parent key points $(\tfrac{1}{3}, -1)$, $(1, 0)$, $(3, 1)$ shift to $(\tfrac{1}{3}+2, -1)$, $(3, 0)$, $(5, 1)$.
> **Answer.** Domain $(2, \infty)$, range $(-\infty, \infty)$, asymptote $x = 2$.
> **Insight.** Horizontal shifts move the asymptote and the domain in lockstep; the range stays put.

#### Vertical Shifts

> [!definition] Vertical Shifts
> For a constant $d$, the function $f(x) = \log_b(x) + d$ shifts the parent function up by $d$ if $d > 0$ and down by $|d|$ if $d < 0$. The vertical asymptote stays at $x = 0$, the domain stays $(0, \infty)$, and the range remains $(-\infty, \infty)$.

![Figure 8 — Vertical shifts of the parent log](chapter4_fig_4.4_8_log_vertical_shifts.png)

Adding a constant outside the logarithm slides the whole curve up or down without touching its left edge. This is the mirror image of horizontal shifts: every $x$ is still admissible, but every $y$-value is offset by $d$.

> [!tip] How To — Graph a Vertical Shift
> Read off $d$ from $\log_b(x) + d$. Keep the asymptote at $x = 0$. Take three reference points from the parent function and add $d$ to each $y$-coordinate.

> [!example] Example 5 — Graphing $f(x) = \log_3(x) - 2$
> **Problem.** Sketch alongside the parent, label, and state domain, range, and asymptote.
> **Setup.** Match to $\log_b(x) + d$ with $d = -2$, a shift down by $2$.
> **Solution.** Asymptote unchanged at $x = 0$. Parent points $(\tfrac{1}{3}, -1)$, $(1, 0)$, $(3, 1)$ become $(\tfrac{1}{3}, -3)$, $(1, -2)$, $(3, -1)$.
> **Answer.** Domain $(0, \infty)$, range $(-\infty, \infty)$, asymptote $x = 0$.
> **Insight.** Vertical shifts move the visible curve but neither the asymptote nor the domain boundary.

#### Stretches and Compressions

> [!definition] Vertical Stretches and Compressions
> For a constant $a > 0$, the function $f(x) = a\log_b(x)$ stretches the parent function vertically by a factor of $a$ if $a > 1$ and compresses it vertically if $0 < a < 1$. The asymptote $x = 0$, the $x$-intercept $(1, 0)$, the domain $(0, \infty)$, and the range $(-\infty, \infty)$ are all preserved.

![Figure 10 — Stretches and compressions of the parent log](chapter4_fig_4.4_10_log_stretches.png)

A vertical scaling stretches every $y$-coordinate by the same factor $a$, but $y = 0$ is fixed under multiplication, so the $x$-intercept is the one landmark that does not move.

> [!tip] How To — Graph a Stretch or Compression
> Read off $a$ from $a\log_b(x)$. Keep the asymptote at $x = 0$. Multiply the $y$-coordinate of each reference point by $a$.

> [!example] Example 6 — Graphing $f(x) = 2\log_4(x)$
> **Problem.** Sketch alongside the parent and state domain, range, and asymptote.
> **Setup.** Match to $a\log_b(x)$ with $a = 2$ — a vertical stretch by $2$.
> **Solution.** Asymptote: $x = 0$. Parent points $(\tfrac{1}{4}, -1)$, $(1, 0)$, $(4, 1)$ become $(\tfrac{1}{4}, -2)$, $(1, 0)$, $(4, 2)$.
> **Answer.** Domain $(0, \infty)$, range $(-\infty, \infty)$, asymptote $x = 0$.
> **Insight.** The $x$-intercept is fixed under any vertical scaling because $a \cdot 0 = 0$.

When stretches and shifts appear together, the order of operations matters: shifts inside the logarithm act before the outside scaling.

> [!example] Example 7 — Graphing $f(x) = 5\log(x + 2)$
> **Problem.** State domain, range, and asymptote, and locate a key point.
> **Setup.** Inside the parentheses first (horizontal shift by $c = 2$, so left by $2$), then outside (stretch by $a = 5$).
> **Solution.** The shift sends the asymptote to $x = -2$ and the $x$-intercept to $(-1, 0)$. The parent key point $(10, 1)$ — using base $10$ — moves to $(8, 1)$ after the shift, then to $(8, 5)$ after the stretch.
> **Answer.** Domain $(-2, \infty)$, range $(-\infty, \infty)$, asymptote $x = -2$.
> **Insight.** Apply inside-the-argument transformations before outside-the-function ones — this is the same order-of-operations logic that governs every composed function.

#### Reflections

> [!definition] Reflections
> The function $f(x) = -\log_b(x)$ reflects the parent across the $x$-axis: domain $(0, \infty)$, range $(-\infty, \infty)$, asymptote $x = 0$ — all unchanged. The function $f(x) = \log_b(-x)$ reflects the parent across the $y$-axis: domain becomes $(-\infty, 0)$, range stays $(-\infty, \infty)$, asymptote stays $x = 0$.

![Figure 13 — Reflections of the parent log](chapter4_fig_4.4_13_log_reflections.png)

A negative coefficient *outside* the log flips the sign of every $y$-output — the curve mirrors across the $x$-axis. A negative coefficient *inside* the log flips the sign of every $x$-input — the curve mirrors across the $y$-axis, which is the only basic transformation that produces a domain bounded on the right.

> [!tip] How To — Graph a Reflection
> For $f(x) = -\log_b(x)$, negate the $y$-coordinate of every reference point; the $x$-intercept $(1, 0)$ stays put. For $f(x) = \log_b(-x)$, negate the $x$-coordinate of every reference point; the $x$-intercept moves to $(-1, 0)$ and the domain becomes $(-\infty, 0)$.

> [!example] Example 8 — Graphing $f(x) = \log(-x)$
> **Problem.** Sketch alongside the parent and state domain, range, and asymptote.
> **Setup.** The factor $-1$ inside the argument signals a reflection across the $y$-axis.
> **Solution.** $y = \log(x)$ increases on its domain; reflecting across the $y$-axis turns it into a function that decreases on $(-\infty, 0)$ and approaches the asymptote $x = 0$ from the left. Parent points $(1, 0)$ and $(10, 1)$ become $(-1, 0)$ and $(-10, 1)$.
> **Answer.** Domain $(-\infty, 0)$, range $(-\infty, \infty)$, asymptote $x = 0$.
> **Insight.** A $y$-axis reflection is the only basic logarithmic transformation that creates a domain bounded on the right.

### Approximating Solutions Graphically

Many logarithmic equations resist clean algebraic manipulation. When that happens, the graphical approach — plot both sides, find their intersection — gives a numerical answer to whatever precision the calculator allows.

> [!example] Example 9 — Approximating the Solution of a Logarithmic Equation
> **Problem.** Solve $4\ln(x) + 1 = -2\ln(x - 1)$ graphically, to the nearest thousandth.
> **Setup.** Treat the two sides as independent functions $Y_1 = 4\ln(x) + 1$ and $Y_2 = -2\ln(x - 1)$. The solution is the $x$-coordinate of their intersection.
> **Solution.** Enter $Y_1$ and $Y_2$. Use a viewing window of $0 \le x \le 5$, $-10 \le y \le 10$ and press [GRAPH]; the curves cross slightly to the right of $x = 1$. Press [2ND][CALC] [5: intersect], then [ENTER] three times. The calculator reports the intersection at $x = 1.3385297\ldots$.
> **Answer.** $x \approx 1.339$.
> **Insight.** When algebra stalls, the intersect tool on any graphing utility delivers a numerical solution without requiring a closed form.

![Figure 15 — Graphical solution of a logarithmic equation](chapter4_fig_4.4_15_log_graphical_solution.png)

### Summarizing Transformations

> [!definition] General Form $f(x) = a\log_b(x + c) + d$
> Every transformation of the parent logarithm $y = \log_b(x)$ fits the form $f(x) = a\log_b(x + c) + d$, where the parent is shifted left by $c$, stretched vertically by $|a|$ (a compression if $|a| < 1$), shifted up by $d$, and reflected across the $x$-axis when $a < 0$. The variant $f(x) = \log_b(-x)$ adds a reflection across the $y$-axis. Order of operations follows standard rules: inside-the-argument transformations apply before outside-the-function ones.

The general form makes the vertical asymptote easy to read off — it depends only on the inner shift $c$, not on the outer scaling $a$ or the vertical translation $d$.

> [!example] Example 10 — Vertical Asymptote of $f(x) = -2\log_3(x + 4) + 5$
> **Problem.** Find the vertical asymptote.
> **Setup.** The asymptote occurs where the argument equals zero.
> **Solution.** Set $x + 4 = 0$, giving $x = -4$. The outer factor $-2$ and the translation $+5$ shift and reflect the curve but do not move the asymptote.
> **Answer.** $x = -4$.
> **Insight.** Only transformations *inside* the logarithm's argument can move the vertical asymptote.

Given enough data points and the location of the asymptote, the parameters $a$, $c$, $d$ can be recovered by substituting known points into the general form.

> [!example] Example 11 — Recovering a Common-Log Equation
> **Problem.** Find a possible equation for a common-log function with vertical asymptote $x = 0$ that passes through $(1, 1)$ and $(4, -2)$.
> **Setup.** Asymptote at $x = 0$ means no horizontal shift, so $c = 0$ and the model is $f(x) = a\log(x) + d$.
> **Solution.** Substitute $(1, 1)$: $1 = a\log(1) + d = a\cdot 0 + d$, so $d = 1$. Now substitute $(4, -2)$: $-2 = a\log(4) + 1$, so $a\log(4) = -3$ and $a = -3/\log(4)$.
> **Answer.** $f(x) = \dfrac{-3}{\log(4)}\log(x) + 1$.
> **Insight.** When the asymptote pins down $c$ and a point of the form $(1, y)$ exploits $\log(1) = 0$ to isolate $d$, the remaining unknown $a$ falls out of any second data point.

---

## 4.5 Logarithmic Properties

![Figure 4.5.1 — pH tested with litmus paper](chapter4_fig_4.5_1_litmus_paper_pH.png)

Because logarithms are exponents in disguise, every algebraic rule for exponents has a mirror image for logs. The properties in this section are the workhorses that let us **expand** a complicated log into a sum of simple pieces — useful for differentiation, for solving equations, and for modeling phenomena like pH where the quantity of interest is itself a logarithm of something physical.

> [!definition] Basic Properties of Logarithms
> For any base $b > 0$ with $b \neq 1$:
> - $\log_b(1) = 0$, because $b^0 = 1$.
> - $\log_b(b) = 1$, because $b^1 = b$.
> - **Inverse property:** $\log_b(b^x) = x$ for all real $x$, and $b^{\log_b(x)} = x$ for $x > 0$.
> - **One-to-one property:** $\log_b(M) = \log_b(N) \iff M = N$.

These foundations extend naturally to the three operations that show up most often inside a logarithm — multiplication, division, and exponentiation — yielding the **three laws of logs** below.

### The Product Rule

Adding exponents corresponds to multiplying their powers, so taking a log of a product turns multiplication into addition.

> [!definition] Product Rule for Logarithms
> $$\log_b(MN) \;=\; \log_b(M) + \log_b(N) \qquad (b > 0,\; b \neq 1)$$
> The rule extends to any number of factors by repeated application.

> [!example] Example 1 — Expanding a Product
> **Problem.** Expand $\log_3\big(30 x (3x+4)\big)$ as a sum of logarithms.
> **Setup.** Factor the argument completely so every multiplicative piece is visible. The integer $30$ splits into its prime factors $2 \cdot 3 \cdot 5$; the variable factors $x$ and $(3x+4)$ are already irreducible.
> **Solution.** Apply the product rule once for each factor in the chain:
> $$\log_3\big(2 \cdot 3 \cdot 5 \cdot x \cdot (3x+4)\big) = \log_3 2 + \log_3 3 + \log_3 5 + \log_3 x + \log_3(3x+4).$$
> The middle term simplifies because $\log_3 3 = 1$.
> **Answer.** $\log_3 2 + 1 + \log_3 5 + \log_3 x + \log_3(3x+4)$.
> **Insight.** Always prime-factor numerical constants first — it surfaces hidden simplifications like $\log_3 3 = 1$ that would otherwise be buried inside the argument.

### The Quotient Rule

Subtracting exponents corresponds to dividing powers, so the log of a quotient becomes a *difference* of logs.

> [!definition] Quotient Rule for Logarithms
> $$\log_b\!\left(\frac{M}{N}\right) \;=\; \log_b(M) - \log_b(N)$$

> [!example] Example 2 — Expanding a Quotient of Products
> **Problem.** Expand $\log_2\!\left(\dfrac{15 x (x-1)}{(3x+4)(2-x)}\right)$.
> **Setup.** First confirm the fraction is in lowest terms (it is — none of the factors share roots). Then peel the expression apart in two stages: quotient rule splits the fraction into numerator minus denominator, and product rule splits each side into its factors.
> **Solution.** Quotient rule:
> $$\log_2\big(15 x (x-1)\big) - \log_2\big((3x+4)(2-x)\big).$$
> Product rule on both groups, with $15 = 3 \cdot 5$:
> $$\big[\log_2 3 + \log_2 5 + \log_2 x + \log_2(x-1)\big] - \big[\log_2(3x+4) + \log_2(2-x)\big].$$
> **Answer.** $\log_2 3 + \log_2 5 + \log_2 x + \log_2(x-1) - \log_2(3x+4) - \log_2(2-x)$.
> **Insight.** The minus sign from the quotient rule distributes over *every* factor that came from the denominator — losing track of one sign is the most common mistake here.

### The Power Rule

A power inside a log can be moved out front as a coefficient, turning exponentiation into multiplication.

> [!definition] Power Rule for Logarithms
> $$\log_b(M^n) \;=\; n \log_b(M)$$
> The rule holds for any real exponent $n$, including fractions and negatives.

The next three examples illustrate the rule forwards, the rule applied after rewriting an argument as a power, and the rule run in reverse to *condense* a coefficient back into an exponent.

> [!example] Example 3 — Forward Application
> **Problem.** Expand $\log_5(x^5)$.
> **Setup.** The argument is already written as a power with exponent $5$.
> **Solution.** Move the exponent to the front: $5 \log_5 x$.
> **Answer.** $5 \log_5 x$.
> **Insight.** The exponent and the log share the same numerical base here ($5$ in both places), but this is purely cosmetic — the power rule does not require the exponent to match the log's base.

> [!example] Example 4 — Rewrite the Argument First
> **Problem.** Expand $\log_3(25)$ using the power rule.
> **Setup.** The argument $25$ is not visibly a power, so first rewrite it as $5^2$.
> **Solution.** $\log_3(25) = \log_3(5^2) = 2 \log_3 5$.
> **Answer.** $2 \log_3 5$.
> **Insight.** When an integer argument has a clean root — a perfect square, cube, or higher — pulling out that power often produces a tidier expression than leaving it whole.

> [!example] Example 5 — Power Rule in Reverse (Condensing)
> **Problem.** Rewrite $4 \log_3(x)$ as a single logarithm with leading coefficient $1$.
> **Setup.** Read the power rule from right to left: a coefficient in front of a log becomes the exponent of its argument.
> **Solution.** $4 \log_3 x = \log_3(x^4)$.
> **Answer.** $\log_3(x^4)$.
> **Insight.** The power rule is bidirectional — equally useful for expanding one log into many terms and for condensing many terms back into one.

### Expanding and Condensing Compound Expressions

Most realistic expressions involve all three rules at once. The standard recipe for **expanding** is to work outside-in (peel off the outermost operation first); the recipe for **condensing** is to work in the reverse order — coefficients first, then sums, then differences.

> [!example] Example 6 — Expanding with All Three Rules
> **Problem.** Expand $\ln\!\left(\dfrac{x^4 y}{7}\right)$ as a sum or difference of logs.
> **Setup.** Outside-in: quotient is the outermost operation, then the numerator's product, and finally the power on $x$.
> **Solution.**
> 1. Quotient rule: $\ln(x^4 y) - \ln 7$.
> 2. Product rule: $\ln(x^4) + \ln y - \ln 7$.
> 3. Power rule: $4 \ln x + \ln y - \ln 7$.
>
> **Answer.** $4 \ln x + \ln y - \ln 7$.
> **Insight.** None of these rules touches *addition or subtraction inside* the argument — $\ln(x+y)$ has no expansion at all. Only multiplication, division, and exponentiation translate.

> [!example] Example 7 — Radicals as Fractional Exponents
> **Problem.** Expand $\log(\sqrt{x})$.
> **Setup.** A square root is a power with exponent $\tfrac{1}{2}$.
> **Solution.** Rewrite and apply the power rule: $\log(x^{1/2}) = \tfrac{1}{2} \log x$.
> **Answer.** $\tfrac{1}{2} \log x$.
> **Insight.** Any radical — cube root, fourth root, anything — becomes a fractional-exponent target for the power rule.

> [!example] Example 8 — A Larger Expansion
> **Problem.** Expand $\log_6\!\left(\dfrac{64 x^3 (4x+1)}{2x-1}\right)$.
> **Setup.** Same recipe — quotient, then product, then powers — and notice that $64 = 2^6$ for an extra simplification.
> **Solution.**
> 1. Quotient: $\log_6\big(64 x^3 (4x+1)\big) - \log_6(2x-1)$.
> 2. Product on the numerator: $\log_6 64 + \log_6(x^3) + \log_6(4x+1) - \log_6(2x-1)$.
> 3. Powers: $\log_6(2^6) = 6 \log_6 2$ and $\log_6(x^3) = 3 \log_6 x$.
>
> **Answer.** $6 \log_6 2 + 3 \log_6 x + \log_6(4x+1) - \log_6(2x-1)$.
> **Insight.** Recognizing $64$ as $2^6$ keeps the exponent visible — leaving it as $\log_6 64$ hides the underlying structure that's useful when comparing or combining terms downstream.

When working in the other direction, the steps invert.

> [!tip] How To — Condense a Logarithmic Expression
> 1. **Power rule first.** Pull each coefficient up into the exponent of its argument.
> 2. **Product rule next.** Merge any sum of logs into the log of a product.
> 3. **Quotient rule last.** Merge any remaining difference into the log of a quotient.
>
> All terms must share the same base — logs with different bases cannot be combined.

> [!example] Example 9 — Simple Condensation
> **Problem.** Write $\log_3 5 + \log_3 8 - \log_3 2$ as a single logarithm.
> **Setup.** No coefficients to lift, so jump straight to product and quotient rules.
> **Solution.** Combine the sum: $\log_3(5 \cdot 8) = \log_3 40$. Then the difference: $\log_3 40 - \log_3 2 = \log_3(40/2) = \log_3 20$.
> **Answer.** $\log_3 20$.
> **Insight.** A shared base is non-negotiable — $\log_3 5 + \log_2 8$ cannot be combined without first changing one of the bases (see the change-of-base formula below).

> [!example] Example 10 — Condensation with Coefficients
> **Problem.** Condense $2 \log_2 x + \tfrac{1}{2} \log_2(x-1) - 6 \log_2(x+3)$.
> **Setup.** Coefficients first (power rule), then merge sums, then merge differences.
> **Solution.**
> 1. Power rule: $\log_2(x^2) + \log_2\!\big((x-1)^{1/2}\big) - \log_2\!\big((x+3)^6\big)$.
> 2. Product rule on the positives: $\log_2\!\big(x^2 \sqrt{x-1}\big) - \log_2\!\big((x+3)^6\big)$.
> 3. Quotient rule: $\log_2\!\left(\dfrac{x^2 \sqrt{x-1}}{(x+3)^6}\right)$.
>
> **Answer.** $\log_2\!\left(\dfrac{x^2 \sqrt{x-1}}{(x+3)^6}\right)$.
> **Insight.** The fractional exponent generated by the power rule may optionally be rewritten as a radical for a more readable final form.

> [!example] Example 11 — Mixed Signs Require Rearranging
> **Problem.** Rewrite $2 \log x - 4 \log(x+5) + \tfrac{1}{x} \log(3x+5)$ as a single logarithm.
> **Setup.** Pull every coefficient into its exponent, then group the positive terms before applying the product rule, so each piece lands in the numerator or denominator it belongs in.
> **Solution.**
> 1. Power rule: $\log(x^2) - \log\!\big((x+5)^4\big) + \log\!\big((3x+5)^{1/x}\big)$.
> 2. Rearrange to group positives together: $\log(x^2) + \log\!\big((3x+5)^{1/x}\big) - \log\!\big((x+5)^4\big)$.
> 3. Product rule on the positives: $\log\!\big(x^2 (3x+5)^{1/x}\big) - \log\!\big((x+5)^4\big)$.
> 4. Quotient rule: $\log\!\left(\dfrac{x^2 (3x+5)^{1/x}}{(x+5)^4}\right)$.
>
> **Answer.** $\log\!\left(\dfrac{x^2 (3x+5)^{1/x}}{(x+5)^4}\right)$.
> **Insight.** Sorting positive and negative log terms before merging keeps each piece on its correct side of the eventual fraction — a small bit of bookkeeping that prevents sign errors.

The pH application below shows how a single application of the product rule explains the curious arithmetic of acid-base chemistry: doubling a concentration *subtracts* a constant from the pH.

> [!example] Example 12 — Effect of Doubling Concentration on pH
> **Problem.** The pH of a solution is defined by $\text{pH} = -\log\big([\mathrm{H}^+]\big)$, where $[\mathrm{H}^+]$ is the hydrogen-ion concentration. If $[\mathrm{H}^+]$ is doubled, what happens to the pH?
> **Setup.** Let the original concentration be $x$, so original $\text{pH} = -\log x$. After doubling, the new concentration is $2x$ and the new $\text{pH}_{\text{new}} = -\log(2x)$. We want the difference.
> **Solution.** Apply the product rule to $\log(2x) = \log 2 + \log x$, then distribute the minus:
> $$\text{pH}_{\text{new}} = -\log(2x) = -\log 2 - \log x = (-\log x) - \log 2 = \text{pH} - \log 2.$$
> Since $\log 2 \approx 0.301$:
> **Answer.** Doubling $[\mathrm{H}^+]$ decreases pH by approximately $0.301$.
> **Insight.** A *multiplicative* change in concentration produces an *additive* shift in pH — that is exactly what a logarithmic scale is built to do.

### The Change-of-Base Formula

Most calculators evaluate only two logarithms directly — the common log ($\log_{10}$) and the natural log ($\ln$). To compute a logarithm in any other base, rewrite it as a quotient of two logs in a base the calculator supports.

> [!definition] Change-of-Base Formula
> For any positive base $n \neq 1$:
> $$\log_b(M) \;=\; \frac{\log_n(M)}{\log_n(b)}$$
> The two most useful specializations:
> $$\log_b(M) = \frac{\ln M}{\ln b} \qquad\text{and}\qquad \log_b(M) = \frac{\log M}{\log b}.$$

> [!example] Example 13 — Symbolic Conversion
> **Problem.** Rewrite $\log_5 3$ as a quotient of natural logs.
> **Setup.** Apply the change-of-base formula with $n = e$.
> **Solution.** The original argument $3$ stays on top; the original base $5$ drops to the bottom: $\dfrac{\ln 3}{\ln 5}$.
> **Answer.** $\dfrac{\ln 3}{\ln 5}$.
> **Insight.** A quick mnemonic — *"old argument up, old base down"* — prevents flipping the ratio.

> [!example] Example 14 — Numerical Evaluation
> **Problem.** Use the change-of-base formula to compute $\log_2 10$ on a calculator.
> **Setup.** Rewrite using natural logs so the calculator can handle each piece.
> **Solution.** $\log_2 10 = \dfrac{\ln 10}{\ln 2} \approx \dfrac{2.302585}{0.693147} \approx 3.3219$.
> **Answer.** $\log_2 10 \approx 3.3219$.
> **Insight.** Choosing $\ln$ versus $\log$ in the change-of-base formula is purely a matter of convenience — the ratio is identical either way because the same conversion factor cancels from numerator and denominator.

---

## 4.6 Exponential and Logarithmic Equations

![Figure 4.6.1 — Wild rabbits in Australia](chapter4_fig_4.6_1_rabbits_australia.png)

Populations that grow without check, radioactive samples that decay on a fixed timescale, capital that compounds continuously — every such phenomenon ends up modeled by an exponential or its inverse. Solving for the input variable (often *time*) requires equations where the unknown sits inside an exponent or inside a logarithm, and the techniques split into two families: when the bases can be matched up, use the one-to-one property; when they cannot, take a logarithm of both sides.

### Exponential Equations with Matching Bases

The cleanest case is when both sides of the equation can be written as powers of the same base. The exponential function is one-to-one, so equal outputs force equal inputs — the exponents themselves must be equal.

> [!definition] One-to-One Property of Exponential Functions
> For any algebraic expressions $S$ and $T$, and any positive real $b \neq 1$,
> $$b^S = b^T \iff S = T.$$

> [!tip] How To — Solve $b^S = b^T$
> 1. Use the rules of exponents to bring the equation into the form $b^S = b^T$.
> 2. Set the exponents equal: $S = T$.
> 3. Solve the resulting (usually linear or polynomial) equation for the unknown.

> [!example] Example 1 — Bases Already Match
> **Problem.** Solve $2^{x-1} = 2^{2x-4}$.
> **Setup.** Both sides are already powers of $2$, so the one-to-one property applies directly.
> **Solution.**
> $$x - 1 = 2x - 4 \quad\Rightarrow\quad x = 3.$$
> **Answer.** $x = 3$.
> **Insight.** Identical bases bypass the exponential entirely — the problem collapses to a linear equation in the exponents.

When the bases look different on the surface, rewrite each side as a power of a common smaller base — usually a prime.

> [!tip] How To — Solve $b_1^S = b_2^T$ with Different Bases
> 1. Rewrite each side as a power of a common base (often the smallest prime factor shared by $b_1$ and $b_2$).
> 2. Simplify using $(b^p)^q = b^{pq}$ until both sides have the form $b^S = b^T$.
> 3. Set the exponents equal and solve.

> [!example] Example 2 — Rewriting to a Common Base
> **Problem.** Solve $8^{x+2} = 16^{x+1}$.
> **Setup.** Both $8 = 2^3$ and $16 = 2^4$, so base $2$ unifies the equation.
> **Solution.**
> $$(2^3)^{x+2} = (2^4)^{x+1} \quad\Rightarrow\quad 2^{3x+6} = 2^{4x+4}.$$
> Set exponents equal: $3x + 6 = 4x + 4$, giving $x = 2$.
> **Answer.** $x = 2$.
> **Insight.** Factoring each base into primes often reveals a common base hidden in plain sight.

> [!example] Example 3 — Radicals as Fractional Exponents
> **Problem.** Solve $2^{5x} = \sqrt{2}$.
> **Setup.** Rewrite the square root as a power: $\sqrt{2} = 2^{1/2}$.
> **Solution.** $2^{5x} = 2^{1/2}$, so $5x = \tfrac{1}{2}$, giving $x = \tfrac{1}{10}$.
> **Answer.** $x = \tfrac{1}{10}$.
> **Insight.** Radicals are a stealth form of fractional exponents — convert before applying the one-to-one property.

Not every exponential equation has a solution. Whenever the right-hand side is incompatible with the *range* of the exponential, no manipulation will save it.

> [!example] Example 4 — No Solution
> **Problem.** Solve $3^{x+1} = -2$.
> **Setup.** Before reaching for algebraic tools, check whether a real solution is even possible.
> **Solution.** Any positive base raised to a real power is strictly positive — the output of $3^{x+1}$ can never equal a negative number.
> **Answer.** No real solution.
> **Insight.** Inspecting the range of $b^x$ (always $(0, \infty)$ for $b > 0$) takes seconds and avoids futile algebra. The graphs of $y = 3^{x+1}$ and $y = -2$ do not intersect.

![Figure 4.6.2 — Graphs that don't cross: no solution](chapter4_fig_4.6_2_no_intersection.png)

### Exponential Equations Without a Common Base

When no common base exists — for instance, $5^{x+2} = 4^x$, where $5$ and $4$ share no prime factors — take a logarithm of both sides and let the power rule pull the variable exponent down to ground level.

> [!tip] How To — Solve When No Common Base Exists
> 1. Take a logarithm of both sides. Use $\log$ if any term has base $10$; otherwise use $\ln$.
> 2. Apply the power rule to bring each unknown exponent down as a coefficient.
> 3. Treat the resulting equation as a standard linear (or polynomial) equation in the unknown.

> [!example] Example 5 — Take the Natural Log of Both Sides
> **Problem.** Solve $5^{x+2} = 4^x$.
> **Setup.** Bases $5$ and $4$ share no common power, so the one-to-one property fails. Take $\ln$ of both sides instead.
> **Solution.**
> $$\ln(5^{x+2}) = \ln(4^x) \quad\Rightarrow\quad (x+2)\ln 5 = x \ln 4.$$
> Distribute and collect $x$-terms:
> $$x \ln 5 + 2 \ln 5 = x \ln 4 \quad\Rightarrow\quad x(\ln 5 - \ln 4) = -2 \ln 5.$$
> Use the quotient rule on the left and the power rule on the right:
> $$x \ln\!\left(\frac{5}{4}\right) = \ln\!\left(\frac{1}{25}\right).$$
> Divide:
> **Answer.** $x = \dfrac{\ln(1/25)}{\ln(5/4)}$.
> **Insight.** Taking $\ln$ of both sides converts an exponential equation into a *linear* equation in $x$ — the unknown moves from up in the exponent to down on the main line, where ordinary algebra can finish the job.

### Equations Involving the Natural Base $e$

Continuous growth and decay models use the base $e$, so equations of the form $y = A e^{kt}$ appear constantly in applications. The natural log is custom-built to unwind them.

> [!tip] How To — Solve $y = A e^{kt}$ for $t$
> 1. Divide both sides by $A$ to isolate $e^{kt}$.
> 2. Take $\ln$ of both sides; on the right, $\ln(e^{kt}) = kt$.
> 3. Divide by $k$.

> [!example] Example 6 — A Clean Continuous-Growth Equation
> **Problem.** Solve $100 = 20 e^{2t}$.
> **Setup.** Isolate $e^{2t}$ before touching the logarithm.
> **Solution.**
> $$5 = e^{2t} \quad\Rightarrow\quad \ln 5 = 2t \quad\Rightarrow\quad t = \frac{\ln 5}{2}.$$
> **Answer.** $t = \dfrac{\ln 5}{2}$.
> **Insight.** Because $\ln$ and $e^{(\cdot)}$ are inverses, $\ln(e^{2t})$ collapses to $2t$ in one step — no power rule needed.

> [!example] Example 7 — Combine Constants First
> **Problem.** Solve $4 e^{2x} + 5 = 12$.
> **Setup.** The exponential is buried under arithmetic — isolate it before taking $\ln$.
> **Solution.**
> $$4 e^{2x} = 7 \quad\Rightarrow\quad e^{2x} = \tfrac{7}{4} \quad\Rightarrow\quad 2x = \ln\!\big(\tfrac{7}{4}\big) \quad\Rightarrow\quad x = \tfrac{1}{2} \ln\!\big(\tfrac{7}{4}\big).$$
> **Answer.** $x = \tfrac{1}{2} \ln\!\big(\tfrac{7}{4}\big)$.
> **Insight.** The discipline is *isolate, then transform.* Logs do not distribute over addition, so an unisolated $e^{2x}$ resists any direct attack.

### Extraneous Solutions

Some algebraic operations introduce candidate solutions that are not actually valid for the original equation. With exponential and logarithmic equations, the two warning signs are an exponential output that is supposed to be negative and the argument of a logarithm that is non-positive.

> [!definition] Extraneous Solutions
> An **extraneous solution** is a candidate that the algebra produces but the original equation rejects. For exponentials, reject any branch where $e^{(\text{anything})}$ comes out negative; for logarithms, reject any candidate that makes a log argument zero or negative. Always check candidates against the *original* equation.

> [!example] Example 8 — A Quadratic in $e^x$
> **Problem.** Solve $e^{2x} - e^x = 56$.
> **Setup.** Let $u = e^x$. Then $e^{2x} = u^2$, and the equation becomes $u^2 - u - 56 = 0$ — a standard quadratic.
> **Solution.** Factor: $(u + 7)(u - 8) = 0$, giving $u = -7$ or $u = 8$. Substitute back: $e^x = -7$ has no solution (the exponential is always positive); $e^x = 8$ gives $x = \ln 8$.
> **Answer.** $x = \ln 8$.
> **Insight.** Watch for hidden quadratic structure in exponentials, and discard any branch that requires $e^x$ to be negative.

### Logarithmic Equations via the Definition

When a single logarithm equals a constant, convert directly to exponential form.

> [!definition] Definition Form for Logarithmic Equations
> For any algebraic expression $S$ and real numbers $b, c$ with $b > 0$, $b \neq 1$,
> $$\log_b(S) = c \iff b^c = S.$$

> [!example] Example 9 — Isolate, Then Convert
> **Problem.** Solve $2 \ln x + 3 = 7$.
> **Setup.** Isolate the logarithm before applying the definition.
> **Solution.**
> $$2 \ln x = 4 \quad\Rightarrow\quad \ln x = 2 \quad\Rightarrow\quad x = e^2.$$
> **Answer.** $x = e^2$.
> **Insight.** A bare $\ln x = c$ is one $e^{(\cdot)}$ away from an explicit value — the only real work is isolating the log.

> [!example] Example 10 — A Compound Argument
> **Problem.** Solve $2 \ln(6x) = 7$.
> **Setup.** Isolate $\ln(6x)$ without disturbing its argument.
> **Solution.**
> $$\ln(6x) = \tfrac{7}{2} \quad\Rightarrow\quad 6x = e^{7/2} \quad\Rightarrow\quad x = \tfrac{1}{6} e^{7/2}.$$
> **Answer.** $x = \tfrac{1}{6} e^{7/2}$.
> **Insight.** The argument of the logarithm remains sealed until you've removed the logarithm — only *then* can you divide by $6$.

> [!example] Example 11 — Graphical and Algebraic Together
> **Problem.** Solve $\ln x = 3$.
> **Setup.** A textbook case for the definition form; also approachable as a graph intersection.
> **Solution.** Algebraically, $x = e^3 \approx 20.0855$. Graphically, plot $y = \ln x$ and $y = 3$ and read off their intersection at $x \approx 20.09$.
> **Answer.** $x = e^3$ (exact); $x \approx 20.0855$ (decimal).
> **Insight.** Algebra delivers the exact form; the graph confirms a sanity check on the magnitude.

![Figure 4.6.3 — Graphical solution via intersection](chapter4_fig_4.6_3_graphical_intersection.png)

### Logarithmic Equations via the One-to-One Property

When two logarithms of the *same base* sit on opposite sides of an equation, their arguments must be equal.

> [!definition] One-to-One Property of Logarithms
> For any algebraic expressions $S$ and $T$, and any positive real $b \neq 1$,
> $$\log_b(S) = \log_b(T) \iff S = T.$$
> Always check the candidate solution against the original equation — substituting it back must leave every log's argument strictly positive.

> [!tip] How To — Solve via the One-to-One Property
> 1. Use the log laws (product, quotient, power) to condense each side into a single logarithm of the same base.
> 2. Equate the arguments.
> 3. Solve the resulting algebraic equation, then check for extraneous solutions.

> [!example] Example 12 — Condense, Then Equate Arguments
> **Problem.** Solve $\log(3x - 2) - \log 2 = \log(x + 4)$.
> **Setup.** Use the quotient rule to merge the two logs on the left, then apply the one-to-one property.
> **Solution.**
> $$\log\!\left(\frac{3x - 2}{2}\right) = \log(x + 4) \quad\Rightarrow\quad \frac{3x - 2}{2} = x + 4.$$
> Clear the fraction and solve: $3x - 2 = 2x + 8$, giving $x = 10$. Check: $3(10) - 2 = 28 > 0$, $10 + 4 = 14 > 0$ — both log arguments are positive, so the candidate is valid.
> **Answer.** $x = 10$.
> **Insight.** Condensing each side into a single logarithm reduces a transcendental equation to a familiar algebraic one — and the extraneous-solution check at the end is non-negotiable.

---

## 4.7 Exponential and Logarithmic Models

![Figure 1 — Neely Nuclear Research Center, Georgia Tech](chapter4_fig_4.7_1_nuclear_reactor.png)

Radioactive material in a reactor like the one above does not simply "run out" — it decays exponentially, halving its mass at a rate set entirely by the isotope's intrinsic decay constant. The same continuous-rate behavior describes bacterial populations doubling, hot coffee cooling toward room temperature, and epidemics saturating a finite population. Mathematical modeling is the act of choosing a function whose qualitative behavior matches the phenomenon, then pinning down its parameters from data. This section catalogues the three workhorse continuous models — exponential growth, exponential decay, and logistic growth — together with their named special cases (half-life, doubling time, Newton's Law of Cooling).

### The general continuous model

Every model in this section starts from the same continuous-rate equation, which describes any quantity whose instantaneous growth or decay rate is proportional to its current amount.

> [!definition] Exponential Growth and Decay
> A quantity $y$ that changes at a rate proportional to itself follows the **continuous exponential model**
> $$y = A_0\, e^{kt},$$
> where $A_0$ is the initial value at $t = 0$, $e$ is Euler's constant, and $k$ is the **continuous rate**. When $k > 0$ the model describes **exponential growth** (populations, compounded investments); when $k < 0$ it describes **exponential decay** (radioactive isotopes, cooling temperatures, drug concentrations). The sign of $k$ is the only thing that flips growth into decay.

The graphs of growth and decay are mirror images about the vertical axis: growth shoots upward without bound, decay falls and flattens toward zero.

![Figure 2 — Exponential growth model](chapter4_fig_4.7_2_exp_growth_model.png)

![Figure 3 — Exponential decay model](chapter4_fig_4.7_3_exp_decay_model.png)

Fitting a continuous model to data means turning two observations — usually the initial value and one later measurement — into the parameters $A_0$ and $k$. The next example illustrates the recipe on a population that doubles every hour.

> [!example] Example 1 — Bacteria Doubling in One Hour
> **Problem.** A bacterial population starts at $100$ cells and doubles to $200$ after one hour. Find the continuous exponential growth model, then estimate the population at $t = 10$ and $t = 20$ hours.
> **Setup.** Use $y = A_0 e^{kt}$ with $A_0 = 100$. The single unknown is $k$, which the doubling condition $y(1) = 200$ pins down.
> **Solution.** Substitute $(t, y) = (1, 200)$:
> $$200 = 100\, e^{k},\quad\text{so}\quad e^{k} = 2,\quad\text{so}\quad k = \ln 2.$$
> The model is $y = 100\, e^{(\ln 2)\,t}$. Evaluating:
> $$y(10) = 100\, e^{10\ln 2} = 100 \cdot 2^{10} = 102{,}400,$$
> $$y(20) = 100\, e^{20\ln 2} = 100 \cdot 2^{20} = 104{,}857{,}600.$$
> **Answer.** $y = 100\, e^{(\ln 2)\,t}$; about $10^5$ cells at 10 hours and about $10^8$ cells at 20 hours.
> **Insight.** Keeping $k = \ln 2$ as an exact symbol (rather than $\approx 0.693$) makes the model collapse into $y = 100 \cdot 2^{t}$ at integer hours, exposing the doubling structure that would be hidden by decimal rounding.

### Half-life — the natural timescale of decay

For a decaying quantity, the most natural way to describe its rate isn't $k$ directly but the **half-life** — the time it takes for the quantity to fall to half its starting value. Half-life is intrinsic to the substance: it depends on $k$ but not on $A_0$.

> [!definition] Half-Life
> The **half-life** $t_{1/2}$ of an exponentially decaying quantity is the time required for it to fall to half its current value. From $y = A_0 e^{kt}$, setting $y = A_0/2$ gives
> $$t_{1/2} = -\frac{\ln 2}{k} \qquad\Longleftrightarrow\qquad k = -\frac{\ln 2}{t_{1/2}}.$$
> The two formulas are the same equation rearranged; the negative sign reflects $k < 0$ for decay.

> [!example] Example 2 — Carbon-14 Decay Model
> **Problem.** Carbon-14 has a half-life of $5{,}730$ years. Express the amount of carbon-14 remaining as a function of time.
> **Setup.** Use $A(t) = A_0 e^{kt}$ with the half-life condition $A(5730) = A_0/2$.
> **Solution.** $0.5\, A_0 = A_0 e^{5730k}$ implies $e^{5730k} = 0.5$, so
> $$k = \frac{\ln 0.5}{5730} = -\frac{\ln 2}{5730} \approx -0.000121.$$
> Therefore $A(t) = A_0\, e^{(\ln 0.5 / 5730)\,t}$, or equivalently $A(t) = A_0\, e^{-0.000121\,t}$.
> **Answer.** $A(t) = A_0\, e^{\left(\ln 0.5 / 5730\right) t}$.
> **Insight.** Carrying $k$ as an exact log expression matters here: predictions over tens of thousands of years compound tiny rounding errors into significant date offsets.

The carbon-14 decay constant is the foundation of one of the most important applications of exponential models in archaeology and earth science.

> [!definition] Radiocarbon Dating
> Living organisms maintain a fixed ratio of carbon-14 to carbon-12. When they die, $^{14}$C decays away at the rate $k \approx -0.000121$ per year while $^{12}$C remains stable. Measuring the surviving fraction $r = A/A_0$ and inverting the decay law gives the time since death:
> $$t = \frac{\ln(A/A_0)}{-0.000121}.$$

> [!tip] How To — Date an Object from Its Carbon-14 Percentage
> 1. Convert the measured percentage of remaining carbon-14 into a decimal $r$.
> 2. Substitute into $t = \dfrac{\ln r}{-0.000121}$ and evaluate.

> [!example] Example 3 — Dating an Artifact at 20% Carbon-14
> **Problem.** An organic artifact retains $20\%$ of its original carbon-14. How old is it?
> **Setup.** $r = 0.20$, plug into the dating formula.
> **Solution.**
> $$t = \frac{\ln 0.20}{-0.000121} \approx \frac{-1.609}{-0.000121} \approx 13{,}301.$$
> **Answer.** Approximately $13{,}301$ years old.
> **Insight.** A single fraction — the ratio of surviving isotope to original — fixes the age, because the decay constant is universal: the same $-0.000121$ applies to every once-living sample on Earth.

### Doubling time — the half-life of growth

For exponentially growing quantities, the analogous natural parameter is the **doubling time**: how long until the quantity is twice its current value. The derivation mirrors half-life almost exactly, but with the negative sign dropped because $k > 0$.

> [!definition] Doubling Time
> The **doubling time** $T_d$ of an exponentially growing quantity is
> $$T_d = \frac{\ln 2}{k}.$$
> Like half-life, it depends only on the rate $k$, never on $A_0$.

> [!example] Example 4 — Moore's Law
> **Problem.** Moore's Law observes that transistor density on a chip doubles roughly every two years. Write a continuous exponential growth model.
> **Setup.** $T_d = 2$. Solve $2 = \ln 2 / k$ for $k$, then plug into $A(t) = A_0 e^{kt}$.
> **Solution.** $k = \dfrac{\ln 2}{2}$, so
> $$A(t) = A_0\, e^{(\ln 2 / 2)\, t}.$$
> **Answer.** $A(t) = A_0\, e^{(\ln 2 / 2)\, t}$ with $t$ in years.
> **Insight.** Half-life and doubling time are the *same formula* with a sign flip; both convert an intuitive "time to halve/double" into the continuous rate $k$ the differential model demands.

The tight parallel between the two timescales is worth seeing side-by-side.

| Process | Defining condition | Rate formula | Sign of $k$ |
|---|---|---|---|
| **Half-life** | $A(t_{1/2}) = A_0/2$ | $k = -\dfrac{\ln 2}{t_{1/2}}$ | negative |
| **Doubling time** | $A(T_d) = 2A_0$ | $k = \dfrac{\ln 2}{T_d}$ | positive |

### Newton's Law of Cooling — exponential decay with an offset

Pure decay flattens toward zero, but real objects cool toward the temperature of their surroundings, not absolute zero. Adding a vertical offset to the decay model captures this.

> [!definition] Newton's Law of Cooling
> An object cooling (or warming) in air at ambient temperature $T_s$ obeys
> $$T(t) = A\, e^{kt} + T_s,$$
> where $T_s$ is the horizontal asymptote, $A$ is the initial temperature gap $T(0) - T_s$, and $k < 0$ is the continuous cooling rate. The model says the *gap above ambient* decays exponentially; the temperature itself decays toward $T_s$, not toward zero.

> [!tip] How To — Apply Newton's Law of Cooling
> 1. Read off $T_s$ from the ambient temperature (the horizontal asymptote of the temperature curve).
> 2. Substitute the initial reading $(0, T(0))$ to find $A = T(0) - T_s$.
> 3. Substitute a second data point to solve for $k$.
> 4. Substitute the target time (or target temperature) to answer the question.

> [!example] Example 5 — Cheesecake in the Refrigerator
> **Problem.** A cheesecake at $165^\circ\text{F}$ is placed in a $35^\circ\text{F}$ refrigerator. After 10 minutes it has cooled to $150^\circ\text{F}$. How long until it reaches $70^\circ\text{F}$?
> **Setup.** $T_s = 35$, $T(0) = 165$, $T(10) = 150$. Model: $T(t) = A e^{kt} + 35$.
> **Solution.** At $t = 0$: $165 = A + 35$, so $A = 130$. At $t = 10$:
> $$150 = 130\, e^{10k} + 35 \;\Longrightarrow\; e^{10k} = \tfrac{115}{130} \;\Longrightarrow\; k = \frac{\ln(115/130)}{10} \approx -0.0123.$$
> The model is $T(t) = 130\, e^{-0.0123\,t} + 35$. Solving $70 = 130\, e^{-0.0123\,t} + 35$:
> $$e^{-0.0123\,t} = \frac{35}{130} \;\Longrightarrow\; t = \frac{\ln(35/130)}{-0.0123} \approx 106.7\text{ min}.$$
> **Answer.** About 107 minutes, or 1 hour 47 minutes.
> **Insight.** Newton's Law is just exponential decay shifted up by $T_s$ — the algebra is identical to the carbon-14 problem once you subtract the asymptote, which is why "subtract the ambient first" is the universal first move.

### Logistic growth — bounded by carrying capacity

Exponential growth is unrealistic past a certain scale: real populations exhaust food, real epidemics run out of susceptible hosts, real markets saturate. The **logistic model** is the simplest function that grows exponentially at first and then bends over as it approaches a maximum.

> [!definition] Logistic Growth Model
> For constants $c > 0$, $a > 0$, and $b > 0$,
> $$f(t) = \frac{c}{1 + a\, e^{-bt}}.$$
> Reading off the parameters:
> - **$c$** is the **carrying capacity** — the upper horizontal asymptote.
> - **$\dfrac{c}{1 + a}$** is the initial value $f(0)$.
> - **$b$** controls how steeply the curve rises through its midpoint.
>
> The graph starts concave-up (early exponential phase), passes through an inflection point at $y = c/2$ where growth is fastest, then becomes concave-down as it flattens toward $y = c$.

![Figure 6 — Logistic growth model](chapter4_fig_4.7_6_logistic_growth_model.png)

The carrying capacity makes the logistic model qualitatively different from pure exponential growth — and quantitatively closer to most real-world data with an obvious upper limit.

> [!example] Example 6 — Flu Spreading Through a Community of 1,000
> **Problem.** At $t = 0$, one person in a community of $1{,}000$ has the flu. The logistic growth constant for this strain is $b = 0.6030$. Estimate the cumulative infected count after 10 days, and predict the long-run total.
> **Setup.** Carrying capacity $c = 1000$ (the whole community); initial $f(0) = 1$. Use $f(0) = c/(1+a)$ to solve for $a$.
> **Solution.** $1 = \dfrac{1000}{1 + a}$ gives $a = 999$. The fitted model is
> $$f(t) = \frac{1000}{1 + 999\, e^{-0.6030\,t}}.$$
> At $t = 10$:
> $$f(10) = \frac{1000}{1 + 999\, e^{-6.030}} \approx \frac{1000}{1 + 999 \cdot 0.00240} \approx 293.8.$$
> As $t \to \infty$, $e^{-bt} \to 0$, so $f(t) \to 1000$.
> **Answer.** About $294$ infections after 10 days; eventually all $1{,}000$ people are infected.
> **Insight.** The initial growth looks exponential — $f$ roughly doubles every $\ln 2 / b \approx 1.15$ days at first — but the $999\,e^{-bt}$ term in the denominator decays into negligibility, forcing the curve to flatten and saturate at $c$.

![Figure 7 — Logistic model fit to data](chapter4_fig_4.7_7_logistic_fit.png)

The same shape — slow start, rapid middle, flat top — appears in epidemics, technology adoption, and population biology. Distinguishing logistic from pure exponential is mostly a matter of asking: *is there a ceiling?*

### Choosing the right model from a scatter plot

Before fitting, you have to pick a family. A quick look at the shape of the data narrows the options.

> [!definition] Choosing a Mathematical Model
> Plot the data first; the shape of the scatter plot tells you the family.
>
> | Family | Shape signature |
> |---|---|
> | **Linear** | Points lie along a straight line. |
> | **Exponential growth** | Slow at first, then accelerates without bound; concave up everywhere. |
> | **Exponential decay** | Drops quickly, levels off toward $y = 0$; concave up everywhere. |
> | **Logarithmic** | Rises quickly at first, then growth slows; concave down everywhere, unbounded above. |
> | **Logistic** | S-shape: concave up, inflection, concave down; levels off at a positive asymptote. |
>
> The signature feature of each family is whether it flattens, and *what* it flattens toward: zero (exponential decay), a positive number (logistic), or never (exponential growth, logarithmic).

> [!example] Example 7 — Recognizing a Logarithmic Pattern
> **Problem.** Does a linear, exponential, logarithmic, or logistic model best fit the data $(1, 0), (2, 1.386), (3, 2.197), (4, 2.773), (5, 3.219), (6, 3.584), (7, 3.892), (8, 4.159), (9, 4.394)$?
> **Setup.** Plot the points and look at concavity. The values increase but the gaps between successive $y$'s shrink steadily — concave down, unbounded — which signals a logarithmic model $y = a \ln x + b$.
> **Solution.** Use the endpoints to pin down the two parameters. At $x = 1$: $0 = a\ln 1 + b = b$, so $b = 0$. At $x = 9$: $4.394 = a\ln 9$, so
> $$a = \frac{4.394}{\ln 9} \approx \frac{4.394}{2.197} \approx 2.$$
> **Answer.** $y = 2\ln x$.
> **Insight.** Picking endpoints to solve for parameters minimizes round-off — the longer the $x$-arm, the less a small $y$-error perturbs $a$. The same logic applies any time you fit two parameters from two points.

### Converting any exponential to base $e$

Calculators and statisticians often produce models in the form $y = ab^x$, but science and calculus prefer the natural base $e$. The conversion is one identity and a logarithm rule.

> [!tip] How To — Rewrite $y = ab^x$ as $y = A_0 e^{kx}$
> 1. Use the identity $b^x = e^{\ln(b^x)}$ to insert $e$ and its inverse: $y = a\, e^{\ln(b^x)}$.
> 2. Apply the power rule $\ln(b^x) = x\ln b$: $y = a\, e^{x\ln b}$.
> 3. Read off $A_0 = a$ and $k = \ln b$. Note $k > 0$ when $b > 1$ (growth) and $k < 0$ when $0 < b < 1$ (decay).

> [!example] Example 8 — Converting $y = 2.5(3.1)^x$ to Base $e$
> **Problem.** Rewrite $y = 2.5(3.1)^x$ in the form $y = A_0 e^{kx}$.
> **Setup.** $a = 2.5$, $b = 3.1$. Apply the recipe.
> **Solution.**
> $$y = 2.5\, e^{\ln(3.1^x)} = 2.5\, e^{x\ln 3.1} = 2.5\, e^{(\ln 3.1)\,x}.$$
> **Answer.** $y = 2.5\, e^{(\ln 3.1)\,x}$, i.e. $A_0 = 2.5$ and $k = \ln 3.1 \approx 1.131$.
> **Insight.** The conversion is a literal change of basis for the exponent — $b^x$ and $e^{x\ln b}$ are equal as functions, and the same data produce the same predictions in either form.

---

## 4.8 Fitting Exponential Models to Data

Section 4.7 built models from two well-chosen points. Real data is rarely that clean — measurements scatter, and we want the curve that fits *all* the points as well as possible. **Regression** is the general technique: a graphing utility (or any least-squares routine) returns the parameters that minimize the total squared error. The three regression families parallel the three growth shapes from §4.7 — exponential, logarithmic, logistic — and the choice between them is again a question of reading the scatter plot.

The closeness of the fit is reported by a **correlation coefficient** $r$ (or its square $r^2$). Values near $\pm 1$ mean a strong fit; values near $0$ mean the chosen family is the wrong one.

### Exponential regression

> [!definition] Exponential Regression
> **Exponential regression** fits data whose growth accelerates without bound (or whose decay drops sharply and flattens toward zero). The calculator command `ExpReg` returns
> $$y = a\, b^x,$$
> with $b > 0$. The model is **growth** when $b > 1$ and **decay** when $0 < b < 1$. Convert to base $e$ via $k = \ln b$ (see §4.7 Example 8) whenever the natural-base form is preferred.

> [!tip] How To — Perform Exponential Regression on a Graphing Calculator
> 1. Enter $x$-values in list `L1` and $y$-values in list `L2` via **STAT → EDIT**.
> 2. Inspect the scatter plot under **STATPLOT** (ZOOM 9 / ZoomStat fits axes automatically). Confirm an exponential shape.
> 3. Run **STAT → CALC → ExpReg** to get the parameters $a$ and $b$.
> 4. Overlay $y = a b^x$ on the scatter plot to verify visual fit; check $r^2$ for a numerical fit score.

The next example illustrates the recipe on a notorious dataset relating blood alcohol level to crash risk — a relationship that is *steeply* exponential.

> [!example] Example 1 — Blood Alcohol Level vs. Crash Risk
> **Problem.** A 2007 study of 2,871 crashes related a driver's blood alcohol concentration (BAC, $x$) to the relative risk of crashing ($y$, where $y = 1$ is the sober baseline). Find the exponential regression and use it to predict crash risk at $x = 0.16$.
> **Setup.** Dataset:
> $(0, 1), (0.01, 1.03), (0.03, 1.06), (0.05, 1.38), (0.07, 2.09), (0.09, 3.54), (0.11, 6.41), (0.13, 12.6),$
> $(0.15, 22.1), (0.17, 39.05), (0.19, 65.32), (0.21, 99.78)$.
> A plot shows risk barely budges below $0.05$ but explodes through $0.1$ — classic exponential growth.
>
> ![Figure 1 — Scatter plot of BAC vs. relative crash risk](chapter4_fig_4.8_1_exp_regression_BAC.png)
>
> **Solution.** Enter $x$ in `L1`, $y$ in `L2`, run `ExpReg`. The calculator returns
> $$y \approx 0.58305 \cdot (2.20720 \times 10^{10})^x, \qquad r^2 \approx 0.997.$$
> The enormous base $b \approx 2.2 \times 10^{10}$ looks alarming but only reflects that $x$ varies over a tiny range (a BAC swing of $0.01$ is a small step on the $x$-axis but a large factor on $y$). For the prediction at $x = 0.16$:
> $$y \approx 0.58305 \cdot (2.20720 \times 10^{10})^{0.16} \approx 26.4.$$
>
> ![Figure 2 — Regression curve and BAC prediction](chapter4_fig_4.8_2_exp_regression_predict.png)
>
> **Answer.** $y \approx 0.583\,(2.207 \times 10^{10})^x$ with $r^2 \approx 0.997$. A driver at $x = 0.16$ is roughly $26$ times as likely to crash as a sober driver.
> **Insight.** $r^2 = 0.997$ confirms the data really is exponential — almost all variance is explained. The large base $b$ is not a red flag; rescaling $x$ to percent (replacing $0.16$ with $16$) would shrink it back to a friendly number without changing any prediction.

### Logarithmic regression

When growth is *fast at first and then plateaus without an obvious ceiling*, the right family is logarithmic, not logistic. The defining test: does the curve flatten *toward an asymptote* (logistic) or just *slow indefinitely* (logarithmic)?

> [!definition] Logarithmic Regression
> **Logarithmic regression** fits data that rise (or fall) quickly at first and then change more and more slowly. The calculator command `LnReg` returns
> $$y = a + b\ln x,$$
> requiring $x > 0$. The model is **increasing** when $b > 0$ and **decreasing** when $b < 0$. There is no horizontal asymptote — the curve drifts upward forever, just more and more slowly.

> [!tip] How To — Perform Logarithmic Regression
> 1. Enter $x$ in `L1` and $y$ in `L2` via **STAT → EDIT** (ensure all $x > 0$).
> 2. Inspect the scatter plot under **STATPLOT** and confirm a concave-down shape with no obvious flat ceiling.
> 3. Run **STAT → CALC → LnReg** to obtain $a$ and $b$.
> 4. Plot $y = a + b\ln x$ over the data and check $r^2$.

> [!example] Example 2 — U.S. Life Expectancy by Decade
> **Problem.** U.S. life expectancy rose from about $47.3$ years in $1900$ to $78.7$ years in $2010$. Fit a logarithmic regression to the decade-by-decade data.
> **Setup.** Re-index time so $x = 1$ corresponds to $1900$, $x = 2$ to $1910$, …, $x = 12$ to $2010$ (this keeps $x > 0$ for the logarithm). Place these indices in `L1` and life-expectancy values in `L2`.
>
> ![Figure 3 — Logarithmic regression on U.S. life expectancy](chapter4_fig_4.8_3_log_regression_life.png)
>
> **Solution.** The scatter plot shows steep early gains tapering off — concave down, no ceiling in sight — pointing to a logarithmic fit. Running `LnReg` returns parameters $a$ and $b$ producing a curve of the form $y = a + b\ln x$ that tracks the data closely.
> **Answer.** A logarithmic model $y = a + b\ln x$ fits the data well, with $b > 0$ encoding the steadily slowing rise.
> **Insight.** Logarithmic vs. logistic is the single most common modeling mistake here. Life expectancy *seems* to be saturating, but absent biological evidence of a hard ceiling, "slowing growth" is logarithmic, not logistic. The two curves only diverge visibly when you extrapolate far past the data.

### Logistic regression

When the data *does* have a clear ceiling — market saturation, total population, a physical limit — logistic regression is the right tool. The S-shape it produces is the qualitative signature.

> [!definition] Logistic Regression
> **Logistic regression** fits data that grow rapidly at first and then level off at a carrying capacity. The calculator command `Logistic` returns
> $$y = \frac{c}{1 + a\, e^{-bx}},$$
> where $c$ is the carrying capacity, $\dfrac{c}{1 + a}$ is the initial value, and $b$ controls steepness. The fit explicitly estimates $c$ from the data — the calculator does *not* assume you know the ceiling in advance.

> [!tip] How To — Perform Logistic Regression
> 1. Enter $x$ in `L1` and $y$ in `L2` via **STAT → EDIT**.
> 2. Plot the data via **STATPLOT** and verify an S-shape (rising with a clear upper plateau).
> 3. Run **STAT → CALC → Logistic** to obtain $a$, $b$, and $c$.
> 4. Plot the fitted curve and verify with $r^2$. The asymptote $y = c$ should match the visual ceiling.

> [!example] Example 3 — U.S. Cell-Phone Adoption, 1995–2012
> **Problem.** From 1995 to 2012 the percentage of Americans with cell service rose from a few percent to nearly universal coverage. Fit a logistic regression to the year-by-year data and predict the percentage at year index $x = 18$ (≈ 2012).
> **Setup.** Re-index years so $x = 1$ is 1995, $x = 2$ is 1996, …, $x = 18$ is 2012. The variable bounded above by $100\%$ is a textbook logistic candidate.
>
> ![Figure 5 — Logistic regression on U.S. cell service adoption](chapter4_fig_4.8_5_logistic_regression_cell.png)
>
> **Solution.** Run `Logistic` on the data. The calculator returns
> $$y = \frac{105.7380}{1 + 6.8833\, e^{-0.2595\,x}}.$$
> The carrying capacity $c \approx 105.7$ slightly overshoots 100% because the model is fit to noisy data — the *true* ceiling is 100%, but the regression rounds the asymptote to whatever level best matches the points it sees. For $x = 18$:
> $$y \approx \frac{105.7380}{1 + 6.8833\, e^{-4.671}} \approx \frac{105.7380}{1 + 6.8833 \cdot 0.00937} \approx \frac{105.7380}{1.0645} \approx 99.3.$$
> **Answer.** $y = \dfrac{105.7380}{1 + 6.8833\, e^{-0.2595\,x}}$; at $x = 18$, $y \approx 99.3\%$.
> **Insight.** Logistic regression is the right model whenever the underlying quantity is *intrinsically bounded*. The fitted $c \approx 105.7$ is a useful sanity check: a logistic regression that returns a $c$ much larger than the known physical ceiling is a sign the data is still in the exponential phase and you don't yet have enough late-time points to pin down the asymptote.

### Comparing the three regressions

The three families are designed to model qualitatively different growth patterns. Picking the wrong family produces an apparently reasonable curve in the middle of the data range but wildly wrong extrapolations.

| Family | Shape | Fitted form | Asymptote | When to use |
|---|---|---|---|---|
| **Exponential** | Concave up, unbounded | $y = a\, b^x$ | $y = 0$ (decay only) | Compounding growth, decay toward zero |
| **Logarithmic** | Concave down, unbounded | $y = a + b\ln x$ | None (drifts up forever) | Slowing growth with no physical ceiling |
| **Logistic** | S-shape with ceiling | $y = \dfrac{c}{1 + a\, e^{-bx}}$ | $y = c$ | Bounded growth, saturation, adoption curves |

The same dataset can occasionally be fit acceptably by more than one family inside its observed range — but the differences explode the moment you extrapolate. The choice of family is therefore not just a curve-fitting decision; it is a claim about the underlying mechanism.

---

## Chapter Review — Key Equations

| Concept | Equation |
|---|---|
| General exponential function | $f(x) = a b^x$ |
| Compound interest (n periods/year) | $A(t) = P\left(1 + \dfrac{r}{n}\right)^{nt}$ |
| Continuous compound interest | $A(t) = P e^{rt}$ |
| Definition of the natural number $e$ | $e = \displaystyle\lim_{n \to \infty} \left(1 + \dfrac{1}{n}\right)^n \approx 2.71828$ |
| Logarithm $\Leftrightarrow$ exponent | $y = \log_b(x) \;\Longleftrightarrow\; b^y = x$ |
| Product rule | $\log_b(MN) = \log_b(M) + \log_b(N)$ |
| Quotient rule | $\log_b(M/N) = \log_b(M) - \log_b(N)$ |
| Power rule | $\log_b(M^n) = n \log_b(M)$ |
| Change of base | $\log_b(M) = \dfrac{\log_c(M)}{\log_c(b)}$ |
| Half-life decay | $N(t) = N_0 e^{-kt}$ with $k = \ln(2)/T_{1/2}$ |
| Doubling time growth | $N(t) = N_0 e^{kt}$ with $T_{\text{double}} = \ln(2)/k$ |
| Newton's law of cooling | $T(t) = A e^{kt} + T_s$ ($T_s$ = surroundings) |
| Logistic growth | $f(t) = \dfrac{c}{1 + a e^{-bt}}$ ($c$ = carrying capacity) |

---

## Key Takeaways

1. **Exponential and logarithmic functions are inverses.** $y = \log_b(x) \iff b^y = x$. Every "what exponent gives me this output?" problem is a log problem; every "what value after $t$ growth steps?" problem is an exponential one.
2. **Exponential graphs are mirrors.** Growth ($b > 1$) and decay ($0 < b < 1$) share the y-intercept $(0, a)$ and horizontal asymptote $y = 0$; one is the reflection of the other across the y-axis. All four transformation families — shift, stretch, reflection, compression — apply identically.
3. **Logarithm graphs are exponential graphs reflected across $y = x$.** Domain becomes $(0, \infty)$; the horizontal asymptote of $b^x$ becomes a vertical asymptote at $x = 0$ for $\log_b$.
4. **The four log rules are the exponent rules inside-out.** Multiplication of inputs becomes addition (product), division becomes subtraction (quotient), exponentiation becomes multiplication (power), and change-of-base lets you swap between any two log bases via division.
5. **Solving exp/log equations always reduces to one of two moves.** Either rewrite both sides with a common base and equate exponents (one-to-one property), or take a logarithm of both sides and solve algebraically. Watch for extraneous solutions when log arguments could go non-positive.
6. **The exp/log model toolkit covers most real-world growth processes** — half-life (radioactive decay, drug clearance, carbon dating), doubling time (population, bacteria, viral spread), Newton's cooling (forensic temperature, food cooling), and logistic growth (bounded systems with carrying capacity).
7. **Regression turns a scatter plot into a model.** Once you've identified whether data follows an exponential, logarithmic, or logistic shape (concavity, asymptotic behavior), a calculator regression gives you the parameters and a function ready for prediction.

---

## Related Documents

- **[Logarithm Fundamentals (Main)](<../../Logarithms/Logarithm Fundamentals (Main).md>)** — Companion intuition note built from 3B1B's *Lockdown Math* ep. 6. Spends more time on the zero-counting intuition for $\log_{10}$, the petri-dish growth practice problem, and log scales as the natural visualization for multiplicative growth. This Chapter 4 note is the algebraic/textbook treatment; the Logarithm Fundamentals note is the intuition/"why does this exist" treatment.
- **[Imaginary Interest and Continuous Rotation (Main)](<../../Complex Numbers/Imaginary Interest and Continuous Rotation (Main).md>)** — Where the number $e$ comes from (compound interest in the continuous limit) and what happens when an imaginary value is plugged into the exponential function. Useful follow-on to §4.1's introduction of $e$.
- **[Euler's Formula via exp(x) (Main)](<../../Complex Numbers/Euler's Formula via exp(x) (Main).md>)** — The polynomial-series definition of $\exp(x)$ and the identity $e^{i\theta} = \cos\theta + i\sin\theta$ it produces for imaginary inputs. Connects the $e$ defined here to its deepest mathematical identity.

---

### Source

| Source | Type |
|---|---|
| [OpenStax Precalculus 2e — Chapter 4](https://openstax.org/details/books/precalculus-2e) (pp. 407–534) | Open-license textbook |
| Figures: rendered at 220 DPI from the source PDF via PyMuPDF | Direct from textbook (Path B) |
| Infographic: generated by Google NotebookLM | AI-generated chapter overview |
