# Exercises 25–26 — Proving the 2×2 Inverse Formula

_Question I had while studying · Lay, *Linear Algebra and Its Applications* (5th ed.), §2.2 The Inverse of a Matrix · asked 2026-10-12_

---

> [!info] Question Essence
> Two textbook exercises that together prove **Theorem 4**: the single number $ad-bc$ decides whether a $2\times2$ matrix is invertible. **Exercise 25** shows that $ad-bc=0$ forces a nonzero solution of $A\mathbf{x}=\mathbf{0}$, so $A$ can't be inverted. **Exercise 26** shows that when $ad-bc\neq0$, the formula $A^{-1}=\frac{1}{ad-bc}\begin{bmatrix} d&-b\\-c&a\end{bmatrix}$ really is the inverse, by checking $AA^{-1}=A^{-1}A=I$.

---

## The Question

![Lay §2.2, Exercises 25 and 26](<2026-10-12 - Proving the 2x2 inverse formula.png>)

---

## The Result Being Proved

> [!definition] Theorem 4 (§2.2) — Inverse of a 2×2 matrix
> Let $A=\begin{bmatrix} a&b\\c&d\end{bmatrix}$. If $ad-bc\neq0$, then $A$ is invertible and
> $$A^{-1}=\frac{1}{ad-bc}\begin{bmatrix} d&-b\\-c&a\end{bmatrix}.$$
> If $ad-bc=0$, then $A$ is not invertible. The number $ad-bc$ is the **determinant** of $A$, written $\det A$.

---

## Exercise 25 — When $ad-bc=0$, $A$ Is Not Invertible

> [!example] Exercise 25 — A zero determinant leaves a nonzero solution
> **Problem.** Show that if $ad-bc=0$, then the equation $A\mathbf{x}=\mathbf{0}$ has more than one solution. Why does this imply that $A$ is not invertible? *(Hint: first consider $a=b=0$. Then, if $a$ and $b$ are not both zero, consider the vector $\mathbf{x}=\begin{bmatrix}-b\\a\end{bmatrix}$.)*
>
> > [!success]- Click to reveal solution
> > **Setup.** $\mathbf{x}=\mathbf{0}$ always solves $A\mathbf{x}=\mathbf{0}$, so "more than one solution" means finding a **nonzero** $\mathbf{x}$ with $A\mathbf{x}=\mathbf{0}$.
> >
> > **Case 1 — $a=b=0$.** The first row is zero, so the system is one equation in two unknowns, $c\,x_1+d\,x_2=0$. That leaves a free variable, so there are infinitely many solutions: for example $\mathbf{x}=\begin{bmatrix}-d\\c\end{bmatrix}$, or any $\mathbf{x}$ at all if $c=d=0$.
> >
> > **Case 2 — $a$ and $b$ not both zero.** The hint's vector is nonzero, and
> > $$A\begin{bmatrix}-b\\a\end{bmatrix}=\begin{bmatrix}-ab+ba\\-cb+da\end{bmatrix}=\begin{bmatrix}0\\ad-bc\end{bmatrix}=\begin{bmatrix}0\\0\end{bmatrix}.$$
> >
> > **Why that rules out an inverse.** If $A^{-1}$ existed, Theorem 5 would make $\mathbf{x}=A^{-1}\mathbf{0}=\mathbf{0}$ the *only* solution of $A\mathbf{x}=\mathbf{0}$. That contradicts the nonzero solution just found.
> >
> > **Answer.** In every case $A\mathbf{x}=\mathbf{0}$ has a nonzero solution, so $A$ is not invertible. ✓
> >
> > **Insight.** The hint splits into cases because when $a=b=0$ the vector $\begin{bmatrix}-b\\a\end{bmatrix}$ is $\mathbf{0}$ itself, which is not a *second* solution.

---

## Exercise 26 — When $ad-bc\neq0$, the Formula Works

> [!example] Exercise 26 — Checking the inverse formula
> **Problem.** Show that if $ad-bc\neq0$, the formula for $A^{-1}$ works.
>
> > [!success]- Click to reveal solution
> > **Setup.** Let $D=ad-bc\neq0$, so dividing by $D$ is allowed, and let $B=\frac1D\begin{bmatrix}d&-b\\-c&a\end{bmatrix}$. By definition, $B=A^{-1}$ means $AB=I$ **and** $BA=I$.
> >
> > **Solution.** Multiply in both orders:
> > $$\begin{bmatrix}a&b\\c&d\end{bmatrix}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}=\begin{bmatrix}ad-bc&-ab+ba\\cd-dc&-cb+da\end{bmatrix}=D\,I$$
> > $$\begin{bmatrix}d&-b\\-c&a\end{bmatrix}\begin{bmatrix}a&b\\c&d\end{bmatrix}=\begin{bmatrix}da-bc&db-bd\\-ca+ac&-cb+ad\end{bmatrix}=D\,I$$
> > Dividing both by $D$ gives $AB=BA=I$.
> >
> > **Answer.** $A$ is invertible and $A^{-1}=\frac{1}{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix}$. ✓
> >
> > **Insight.** For square matrices one of the two products would be enough, but that is only proved later, in the Invertible Matrix Theorem (§2.3).

---

## Other Ways to See It

> [!tip] Geometric — $ad-bc$ is an area factor
> The columns $\begin{bmatrix}a\\c\end{bmatrix}$ and $\begin{bmatrix}b\\d\end{bmatrix}$ span a parallelogram of area $|ad-bc|$. If that area is $0$, the columns lie on one line: $A$ flattens the plane onto a line or a point, and a flattening can't be undone. The vector $\begin{bmatrix}-b\\a\end{bmatrix}$ is the first row turned $90^\circ$. When $ad-bc=0$ the second row is a multiple of the first, so this vector is perpendicular to both rows, which is exactly why $A$ sends it to $\mathbf{0}$.

> [!example] By example
> - $\begin{bmatrix}1&2\\2&4\end{bmatrix}$: $ad-bc=4-4=0$, and $\mathbf{x}=\begin{bmatrix}-2\\1\end{bmatrix}$ gives $A\mathbf{x}=\mathbf{0}$, so it is not invertible.
> - $\begin{bmatrix}2&1\\1&1\end{bmatrix}$: $ad-bc=1$, so $A^{-1}=\begin{bmatrix}1&-1\\-1&2\end{bmatrix}$, and multiplying the two gives $I$.

> [!warning] Watch out
> - **A zero right side doesn't force $\mathbf{x}=\mathbf{0}$.** Nonzero solutions of $A\mathbf{x}=\mathbf{0}$ exist exactly when $A$ is not invertible. (Same idea as Chapter 1 self-test question 1.6-1.)
> - **The formula's pattern:** swap $a$ and $d$, flip the signs of $b$ and $c$, then divide by $ad-bc$. Don't swap $b$ and $c$.

---

> [!tip] Key Takeaway
> $ad-bc$ decides everything for a $2\times2$ matrix. **Nonzero:** swap $a$ and $d$, negate $b$ and $c$, and divide by $ad-bc$. **Zero:** some nonzero vector is sent to $\mathbf{0}$, so $A$ can't be undone.

---

## Related Documents

- **[Linear Maps Across Dimensions](<Linear Maps Across Dimensions.md>)** — the 3D demo's "$3\times3$ with one free variable" tab shows the same flattening that makes a zero determinant non-invertible.
- **[Chapter 1 Self-Test](<Chapter 1 Self-Test.md>)** — question 1.6-1 uses the same "zero right side, nonzero solution" idea.
