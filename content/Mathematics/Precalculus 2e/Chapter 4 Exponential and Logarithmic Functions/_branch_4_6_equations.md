Answer:
## 4.6 Exponential and Logarithmic Equations

This section covers the core algebraic techniques for finding unknown variables
trapped within exponential powers or logarithmic arguments [1]. By relying on 
the one-to-one mathematical properties of these functions, or by using inverse 
operations to switch between exponential and logarithmic forms, you can 
dismantle complex equations into solvable linear or quadratic expressions 
[2-5]. Understanding these solution strategies is crucial for the chapter, as 
it shifts the focus from simply graphing these relationships to actively using 
them to answer real-world predictive questions, such as calculating the time 
required for a radioactive isotope to decay or forecasting the timeline of an 
uncontrolled population boom [1, 6].

> [!definition] Extraneous Solution
> A mathematically derived answer that emerges correctly from the algebraic 
steps taken, but ultimately proves impossible or invalid when substituted back 
into the original equation's domain constraints, such as inadvertently 
attempting to evaluate the logarithm of a negative number [7].

> [!definition] Half-Life
> The specific length of time required for fifty percent of an unstable, 
radioactive substance to naturally decay [6].

> [!example] Example 1 — Solving an Exponential Equation with a Common Base
> **Problem.** Find the value of the variable when two exponential expressions 
with identical bases are set equal to each other [8].
> **Setup.** The mathematical equation is $2^{x-1} = 2^{2x-4}$ [8].
> **Solution.** Because the base of 2 is the exact same on both sides, rely on 
the one-to-one property to drop the bases entirely and set the two exponent 
expressions equal to one another [8]. Solve the resulting linear equation 
algebraically by isolating $x$ [8].
> **Answer.** The solution is $x = 3$ [8].
> **Insight.** When the bases inherently match, the complex exponential 
equation instantly simplifies into a basic algebraic problem [2, 8].

> [!example] Example 2 — Solving Equations by Rewriting Them to Have a Common 
Base
> **Problem.** Solve an exponential equation where the bases are different but 
mathematically related [8].
> **Setup.** The given equation is $8^{x+2} = 16^{x+1}$ [8].
> **Solution.** Recognize that both 8 and 16 can be rewritten as powers of 2 
(specifically $2^3$ and $2^4$) [8]. Substitute these new base-2 expressions 
into the equation and distribute the powers into the existing exponents [8]. 
Finally, set the newly adjusted exponents equal to each other and solve for $x$
[8, 9].
> **Answer.** The final result is $x = 2$ [9].
> **Insight.** Finding the lowest common prime base is the fastest way to 
bridge two seemingly unmatched exponential terms [8, 9].

> [!example] Example 3 — Solving Equations by Rewriting Roots with Fractional 
Exponents to Have a Common Base
> **Problem.** Solve an equation where one side is an exponential expression 
and the other is a radical [9].
> **Setup.** The equation is $2^{5x} = \sqrt{2}$ [9].
> **Solution.** Translate the square root symbol into its equivalent fractional
exponent form, which is a power of $1/2$ [9]. Because both sides now explicitly
share a base of 2, set the left exponent $5x$ equal to the right exponent $1/2$
and isolate the variable [9].
> **Answer.** The variable equals $1/10$ [9].
> **Insight.** Radicals and roots are merely fractional exponents, meaning they
can be seamlessly converted to match standard integer bases [9].

> [!example] Example 4 — Solving an Equation with Positive and Negative Powers
> **Problem.** Attempt to find the solution for an exponential term set equal 
to a negative constant [4].
> **Setup.** The equation to solve is $3^{x+1} = -2$ [4].
> **Solution.** Evaluate the properties of exponential functions, recalling 
that any positive real number raised to any power will always yield a strictly 
positive result [4]. Consequently, there is no mathematical way for base 3 to 
ever produce a negative output [4].
> **Answer.** This equation has no real solution [4].
> **Insight.** Recognizing the strictly positive range of an exponential 
function can save you from attempting impossible algebraic calculations [4].

> [!example] Example 5 — Solving an Equation Containing Powers of Different 
Bases
> **Problem.** Isolate the variable when the exponential bases on each side are
entirely unrelated and cannot be rewritten to match [4].
> **Setup.** You must solve $5^{x+2} = 4^x$ [4].
> **Solution.** Apply the natural logarithm to both sides of the equation [10].
Utilize the logarithmic power rule to pull the exponent variables out to the 
front of the logarithms as multiplying coefficients [10]. Distribute the terms,
group the expressions containing $x$ on one side of the equals sign, factor $x$
out, and divide to isolate it completely [10].
> **Answer.** The precise algebraic solution is $x = \frac{-2\ln(5)}{\ln(5) - 
\ln(4)}$ [10].
> **Insight.** Taking the logarithm of both sides acts as an algebraic override
to pull variables down from exponents when finding a common base is impossible 
[4, 10].

> [!example] Example 6 — Solve an Equation of the Form $y = Ae^{kt}$
> **Problem.** Determine the unknown time variable in a standard natural 
exponential model [10].
> **Setup.** The provided equation is $100 = 20e^{2t}$ [10].
> **Solution.** First, divide both sides by the leading coefficient 20 to 
completely isolate the base $e$ term, yielding $5 = e^{2t}$ [10]. Apply the 
natural logarithm to both sides to cancel out the base $e$, leaving just the 
exponent $\ln(5) = 2t$ [10]. Finally, divide by 2 [10].
> **Answer.** The exact mathematical value is $t = \frac{\ln(5)}{2}$ [10].
> **Insight.** You must securely isolate the exponential term by clearing away 
any outside multipliers before you can apply a natural logarithm [10].

> [!example] Example 7 — Solving an Equation That Can Be Simplified to the Form
$y = Ae^{kt}$
> **Problem.** Strip away multiple constants to solve a base $e$ equation [7].
> **Setup.** The starting expression is $4e^{2x} + 5 = 12$ [7].
> **Solution.** Process standard reverse order of operations by subtracting the
5 first, and then dividing by the 4, resulting in an isolated exponential term 
$e^{2x} = 7/4$ [7]. Introduce a natural logarithm to both sides to cancel the 
base, and divide by 2 to finalize the isolation of $x$ [7].
> **Answer.** The solution is $x = \frac{1}{2}\ln(\frac{7}{4})$ [7].
> **Insight.** Complex exponential equations often require several layers of 
standard algebraic cleanup before the actual logarithmic inversion can occur 
[7].

> [!example] Example 8 — Solving Exponential Functions in Quadratic Form
> **Problem.** Utilize factoring techniques to solve an equation containing 
multiple squared exponential terms [7].
> **Setup.** The mathematical equation is $e^{2x} - e^x = 56$ [7].
> **Solution.** Move all terms to one side to set the equation to zero, 
treating the structure identically to a quadratic equation where the variable 
is $e^x$ [7]. Factor the polynomial into $(e^x - 8)(e^x + 7) = 0$ [7]. Set each
individual factor equal to zero, which produces $e^x = 8$ and $e^x = -7$ [7]. 
Discard the negative outcome because an exponential function cannot yield a 
negative result [7]. Take the natural log of the remaining positive equation 
[7].
> **Answer.** The only valid solution is $x = \ln(8)$ [7].
> **Insight.** Substituting a complex term for a simpler variable can reveal 
hidden quadratic structures, but you must rigorously check the final factored 
pieces for extraneous solutions [7].

> [!example] Example 9 — Using Algebra to Solve a Logarithmic Equation
> **Problem.** Apply the fundamental definition of logarithms to free a 
variable trapped inside an argument [5].
> **Setup.** You must solve $2\ln(x) + 3 = 7$ [5].
> **Solution.** Use basic algebra to subtract the 3 and divide by the 2, 
leaving the simplified expression $\ln(x) = 2$ [5]. Because the base of a 
natural logarithm is understood to be $e$, rewrite the entire equation into its
inverse exponential format to free the $x$ [5].
> **Answer.** The resulting value is $x = e^2$ [5].
> **Insight.** Converting a fully isolated logarithm into its equivalent 
exponential form is the most direct way to unlock an internal argument [5].

> [!example] Example 10 — Using Algebra Before and After Using the Definition 
of the Natural Logarithm
> **Problem.** Untangle a natural logarithm where the internal argument 
requires further algebraic division after conversion [5].
> **Setup.** The given problem is $2\ln(6x) = 7$ [5].
> **Solution.** Divide by 2 to isolate the natural log term, giving $\ln(6x) = 
7/2$ [5]. Translate the statement into base $e$ exponential form to break the 
log, resulting in $6x = e^{7/2}$ [5]. Finally, divide the remaining coefficient
6 away from the variable [5].
> **Answer.** The final exact answer is $x = \frac{1}{6}e^{7/2}$ [5].
> **Insight.** Even after executing an exponential conversion to destroy a 
logarithm, standard algebraic steps are usually still required to finish 
isolating the variable [5].

> [!example] Example 11 — Using a Graph to Understand the Solution to a 
Logarithmic Equation
> **Problem.** Utilize a graphing calculator to visually approximate the 
crossing point of a complex logarithmic scenario [11].
> **Setup.** You need to solve $\ln(x) = 3$ [11].
> **Solution.** Input the left side of the equation into the calculator as one 
distinct graph curve, and the right side (the constant 3) as a separate 
horizontal line [11]. Trigger the calculator's visual intersection tool to 
pinpoint the precise coordinates where the two graphs collide [11].
> **Answer.** The curves cross at an approximate x-coordinate of $20.0855$ 
[11].
> **Insight.** Digital graphing utilities offer an immediate, visual 
approximation technique that entirely bypasses manual algebraic manipulation 
[11].

> [!example] Example 12 — Solving an Equation Using the One-to-One Property of 
Logarithms
> **Problem.** Solve a scenario where natural logarithms are present on both 
sides of the equals sign [6].
> **Setup.** The mathematical equation is $\ln(x^2) = \ln(1)$ [6].
> **Solution.** Because the natural log operates on both sides perfectly, 
utilize the one-to-one property to drop the logs entirely, setting the internal
arguments equal to yield $x^2 = 1$ [6]. Take the square root of both sides, 
resulting in a positive and negative answer [6]. Test the negative answer in 
the original equation to ensure it does not create a negative log argument; 
because the initial argument is squared, the negative input becomes positive 
and is mathematically valid [6].
> **Answer.** The valid solutions are $x = 1$ and $x = -1$ [6].
> **Insight.** You must always verify negative algebraic answers against the 
original logarithmic equation to ensure they don't break the strict domain 
requirement of positive arguments [6].

> [!example] Example 13 — Using the Formula for Radioactive Decay to Find the 
Quantity of a Substance
> **Problem.** Calculate the exact number of years required for a percentage of
a radioactive isotope mass to disappear [12].
> **Setup.** You start with 1,000 grams of Uranium-235, which has a known 
half-life of 703,800,000 years, and you need to find the time it takes for 10% 
of the sample to physically decay [12].
> **Solution.** Because 10% decays, recognize that 900 grams will remain as 
your final target value [12]. Plug the starting amount, the remaining amount, 
and the specific half-life into the continuous exponential decay framework 
[12]. Divide by the 1,000 initial grams, take the natural logarithm of both 
sides to cancel the exponential base $e$, and solve for the unknown time 
variable $t$ [12].
> **Answer.** It will take roughly $106,979,777$ years [12].
> **Insight.** Real-world radioactive decay questions require carefully 
differentiating between the amount of material that has disappeared and the 
amount that actually remains to be entered into the final equation [12].

*   $b^S = b^T \iff S = T$
    This describes the one-to-one property of exponential functions, confirming
that if two exponential expressions sharing the exact same base are perfectly 
equal, their subsequent exponents must also be equivalent [2].
*   $\log_b(S) = \log_b(T) \iff S = T$
    This represents the one-to-one property of logarithmic functions, which 
dictates that if two logarithms sharing an identical base equate to one 
another, their internal arguments must absolutely match [6, 13].
*   $y = \log_b(x) \iff b^y = x$
    This formula outlines the core definition of a logarithm, serving as the 
primary mechanism for switching equations between logarithmic and exponential 
formats to free trapped variables [5].
*   $y = A e^{(\frac{\ln(0.5)}{h})t}$
    This equation maps out the continuous mathematical decay of a radioactive 
element, calculating the remaining material $y$ over time $t$ by relying on an 
initial deposit $A$ and a known half-life constant $h$ [12].

*   **Figure 1**: A photograph showing a large population of wild rabbits in 
Australia, used to introduce the concept of rapid, unchecked exponential 
growth, located on approximately book page 482 [1].
*   **Figure 2**: A visual coordinate graph proving that an upward-sloping 
exponential curve and a negative horizontal line will never cross, 
demonstrating an equation with no valid mathematical solution, located on 
approximately book page 485 [4].
*   **Figure 3**: A graph displaying the exact intersection point where a 
natural logarithm curve meets a constant horizontal line, illustrating a visual
estimation technique for equation solving, located on approximately book page 
489 [11].

*   **You must accept that not every exponential equation has a real 
solution**; specifically, an isolated exponential term featuring a positive 
base can never be mathematically equal to a negative output number [4].
*   **The textbook explicitly warns to check for extraneous solutions 
continuously** when solving logarithmic formulas, because applying algebraic 
rules can easily trick you into generating negative answers that break the 
strict positive-argument domain restriction of logarithms [6, 7].
*   **When you substitute a temporary variable to factor an exponential 
equation** like a quadratic, be fully prepared to mathematically reject any 
resulting factored piece that attempts to equate the exponential term to a 
negative value [7].

Section 4.6 cohesively merges the algebraic rules developed earlier in the 
chapter, providing you with concrete action plans to isolate variables whether 
they are floating in an exponent or barricaded inside a logarithm [6]. By 
actively manipulating equations to force a common base, or strategically 
applying natural logarithms to override mismatched bases, almost any 
intimidating equation can be dragged down into familiar linear or quadratic 
algebra [4, 8]. Grasping this back-and-forth interplay is essential, as it 
grants you the specific mathematical machinery needed to reliably forecast the 
outcomes of intense real-world phenomena, ranging from the compounding 
explosion of wild animal populations to the agonizingly slow decay of dangerous
radioactive isotopes [1, 6, 12].

Conversation: 811de852-23c7-481e-8a2c-fe733a626d9c (turn 1)
