Here is a detailed record of the formulas, derivations, diagrams, and key concepts presented in the video segment:

### **[06:00] First Audience Poll: Comparing Annual vs. Monthly Interest**
*   **Slide Content:** 
    *   **Question:** Two banks offer different interest rates on your savings.
        *   Bank A will increase your savings by 12% every year
        *   Bank B will increase your savings by 1% every month
    *   With each bank, you set up an account with $100. After 1 year, which of the following is true?
    *   **Options:**
        *   You have more money with Bank A, by more than $1
        *   You have more money with Bank A, by less than $1
        *   You have the same amount in each
        *   You have more money with bank B, by less than $1
        *   You have more money with bank B, by more than $1
*   **Results:** The bar chart on the left shows the majority (over 1320 votes) selected "You have more money with bank B, by more than $1" (Option D). However, the speaker reveals the correct answer is the second most popular choice (around 120 votes): **"You have more money with bank B, by less than $1" (Option C)**.

### **[06:40] Key Concept: Compounding Frequency Matters**
*   **Speaker Quote:** "It's not obvious that 12% over a year is going to be any different than 1% per month. Right? Like, oh, 1% per month, that should add up to 12% over the year." 
*   This sets up the premise for the rest of the mathematical derivations, explaining why simple addition of interest rates is incorrect when compounding is involved.

### **[06:58] Diagram: Desmos Graph - Annual Compounding (Bank A)**
*   **Visual Elements:** A Desmos graphing calculator interface is shown on screen.
    *   **Left Panel (Inputs):** `r = 0.12` (interest rate), `n = 1` (compounding periods per year). A folder labeled "Step growth" is expanded to show calculations.
    *   **Right Panel (Graph):** A step-function graph showing account balance over time.
    *   **Axes:** The X-axis represents time in years (labeled 0, 1, 2... up to 40+ when zoomed out). The Y-axis represents the account balance in dollars (labeled 90, 100, 110, 120... up to 1000+).
    *   **Curve Shape:** For the first year, the graph is a flat horizontal line segment at $y=100$. At $x=1$ (end of year one), it steps up to $y=112$. At $x=2$, it steps up to $y=125.44$. 
    *   **Zoomed Out View [08:18]:** When the graph is zoomed out to show 40 years, the sequence of discrete horizontal steps forms an overarching exponential growth curve. The speaker highlights a point at 10 years where the balance is approximately $310.585.

### **[07:23] Formula Derivation: One Year of Annual Interest**
The speaker derives the formula for the balance after one year with Bank A (12% annual interest).
1.  **Start with the base calculation:** 
    `100 + 0.12 * 100` (evaluates to `112`)
2.  **[07:48] Key Concept - Factoring:** The speaker notes, "The fact that the rate of change is proportional to the thing that's changing means we can factor out this 100. And we can just say, oh, that step that we take, we're multiplying it by a constant."
3.  **Factor the equation:** By pulling out the common factor of `100`, the expression simplifies to:
    `100(1 + 0.12)` 
4.  This shows the balance is scaled by a multiplicative constant of `1.12`.

### **[09:07] Second Audience Poll: Semi-Annual Compounding**
*   **Slide Content:** 
    *   **Question:** A bank offers to increase the money in your savings account by 6% at the end of every 6 months. Which of the following represents how much money will be in your account if you put $100 into an account and then wait for one year?
    *   **Options:**
        *   `$100 + 2 * 0.06 * $100`
        *   `$100 + 0.06 * $100 + 0.06^2 * $100`
        *   `$100(1 + 0.06)^2`
        *   `$100(1 + 0.12)^(1/2)`
*   **Results [10:35]:** The correct answer, heavily favored by the audience (over 3000 votes), is highlighted in green: **`$100(1 + 0.06)^2` (Option C)**.

### **[10:52] Formula Derivation: Semi-Annual Compounding (6% every 6 months)**
The speaker returns to Desmos to meticulously break down the logic behind the correct answer to the second poll, showing step-by-step why the formula works over two 6-month periods.
1.  **First 6-month period:** Calculate the balance after the first 6% increase.
    *   The formula is `100(1 + 0.06)`, which evaluates to `106`.
2.  **[11:15] Second 6-month period (Expansion):** Apply a 6% increase to the *new* balance of 106.
    *   `106 + 0.06 * 106` (evaluates to `112.36`)
3.  **Factoring the second period:** Pull out the common factor of `106` from the expression.
    *   `106(1 + 0.06)`
4.  **Substitution:** Recognize that the `106` in the formula is equal to the initial calculation `100(1 + 0.06)`. Substitute this back into the factored expression.
    *   `100(1 + 0.06) * (1 + 0.06)`
5.  **Final Simplification:** Combine the identical terms to show the final exponentiated form.
    *   **`100(1 + 0.06)^2`**