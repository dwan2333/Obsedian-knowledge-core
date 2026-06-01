--- PDF page 1 (book page 407) ---
Electron micrograph of E.Coli bacteria (credit: “Mattosaurus,” Wikimedia Commons) 
Chapter Outline 
4.1 Exponential Functions 
4.2 Graphs of Exponential Functions 
4.3 Logarithmic Functions 
4.4 Graphs of Logarithmic Functions 
4.5 Logarithmic Properties 
4.6 Exponential and Logarithmic Equations 
4.7 Exponential and Logarithmic Models 
4.8 Fitting Exponential Models to Data 
Introduction to Exponential and Logarithmic Functions 
Focus in on a square centimeter of your skin. Look closer. Closer still. If you could look closely enough, you would see 
hundreds of thousands of microscopic organisms. They are bacteria, and they are not only on your skin, but in your 
mouth, nose, and even your intestines. In fact, the bacterial cells in your body at any given moment outnumber your 
own cells. But that is no reason to feel bad about yourself. While some bacteria can cause illness, many are healthy and 
even essential to the body. 
Bacteria commonly reproduce through a process called binary fission, during which one bacterial cell splits into two. 
When conditions are right, bacteria can reproduce very quickly. Unlike humans and other complex organisms, the time 
required to form a new generation of bacteria is often a matter of minutes or hours, as opposed to days or years.1 
For simplicity’s sake, suppose we begin with a culture of one bacterial cell that can divide every hour. Table 1 shows the 
number of bacterial cells at the end of each subsequent hour. We see that the single bacterial cell leads to over one 
thousand bacterial cells in just ten hours! And if we were to extrapolate the table to twenty-four hours, we would have 
over 16 million! 
Hour 
0 
1 
2 
3 
4 
5 
6 
7 
8 
9 
10 
Bacteria 
1 
2 
4 
8 
16 
32 
64 
128 
256 
512 
1024 
Table 1 
4 
EXPONENTIAL AND LOGARITHMIC 
FUNCTIONS 
1 Todar, PhD, Kenneth. Todar's Online Textbook of Bacteriology. http://textbookofbacteriology.net/growth_3.html. 
4 • Introduction to Exponential and Logarithmic Functions          397


--- PDF page 2 (book page 408) ---
In this chapter, we will explore exponential functions, which can be used for, among other things, modeling growth 
patterns such as those found in bacteria. We will also investigate logarithmic functions, which are closely related to 
exponential functions. Both types of functions have numerous real-world applications when it comes to modeling and 
interpreting data. 
4.1 Exponential Functions 
Learning Objectives 
In this section, you will: 
Evaluate exponential functions. 
Find the equation of an exponential function. 
Use compound interest formulas. 
Evaluate exponential functions with base  . 
India is the second most populous country in the world with a population of about 
 billion people in 2021. The 
population is growing at a rate of about 
 each year2 . If this rate continues, the population of India will exceed 
China’s population by the year 
 When populations grow rapidly, we often say that the growth is “exponential,” 
meaning that something is growing very rapidly. To a mathematician, however, the term exponential growth has a very 
specific meaning. In this section, we will take a look at exponential functions, which model this kind of rapid growth. 
Identifying Exponential Functions 
When exploring linear growth, we observed a constant rate of change—a constant number by which the output 
increased for each unit increase in input. For example, in the equation 
 the slope tells us the output 
increases by 3 each time the input increases by 1. The scenario in the India population example is different because we 
have a percent change per unit time (rather than a constant change) in the number of people. 
Defining an Exponential Function 
A study found that the percent of the population who are vegans in the United States doubled from 2009 to 2011. In 
2011, 2.5% of the population was vegan, adhering to a diet that does not include any animal products—no meat, poultry, 
fish, dairy, or eggs. If this rate continues, vegans will make up 10% of the U.S. population in 2015, 40% in 2019, and 80% 
in 2021. 
What exactly does it mean to grow exponentially? What does the word double have in common with percent increase? 
People toss these words around errantly. Are these words used correctly? The words certainly appear frequently in the 
media. 
• Percent change refers to a change based on a percent of the original amount. 
• Exponential growth refers to an increase based on a constant multiplicative rate of change over equal increments 
of time, that is, a percent increase of the original amount over time. 
• Exponential decay refers to a decrease based on a constant multiplicative rate of change over equal increments of 
time, that is, a percent decrease of the original amount over time. 
For us to gain a clear understanding of exponential growth, let us contrast exponential growth with linear growth. We 
will construct two functions. The first function is exponential. We will start with an input of 0, and increase each input by 
1. We will double the corresponding consecutive outputs. The second function is linear. We will start with an input of 0, 
and increase each input by 1. We will add 2 to the corresponding consecutive outputs. See Table 1. 
0 
1 
0 
1 
2 
2 
2 
4 
4 
3 
8 
6 
Table 1 
2 http://www.worldometers.info/world-population/. Accessed February 24, 2014. 
398     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 3 (book page 409) ---
4 
16 
8 
5 
32 
10 
6 
64 
12 
Table 1 
From Table 1 we can infer that for these two functions, exponential growth dwarfs linear growth. 
• Exponential growth refers to the original value from the range increasing by the same percentage over equal 
increments found in the domain. 
• Linear growth refers to the original value from the range increasing by the same amount over equal increments 
found in the domain. 
Apparently, the difference between “the same percentage” and “the same amount” is quite significant. For exponential 
growth, over equal increments, the constant multiplicative rate of change resulted in doubling the output whenever the 
input increased by one. For linear growth, the constant additive rate of change over equal increments resulted in adding 
2 to the output whenever the input was increased by one. 
The general form of the exponential function is 
 where  is any nonzero number,  is a positive real number 
not equal to 1. 
• If 
 the function grows at a rate proportional to its size. 
• If 
 the function decays at a rate proportional to its size. 
Let’s look at the function 
 from our example. We will create a table (Table 2) to determine the corresponding 
outputs over an interval in the domain from 
 to 
Table 2 
Let us examine the graph of  by plotting the ordered pairs we observe on the table in Figure 1, and then make a few 
observations. 
Figure 1 
Let’s define the behavior of the graph of the exponential function 
 and highlight some its key characteristics. 
• the domain is 
∞∞
• the range is 
∞
• as 
∞
∞
4.1 • Exponential Functions     399


--- PDF page 4 (book page 410) ---
• as 
∞
• 
 is always increasing, 
• the graph of 
 will never touch the x-axis because base two raised to any exponent never has the result of zero. 
• 
 is the horizontal asymptote. 
• the y-intercept is 1. 
Exponential Function 
For any real number 
 an exponential function is a function with the form 
where 
• 
 is a non-zero real number called the initial value and 
• 
 is any positive real number such that 
• The domain of  is all real numbers. 
• The range of  is all positive real numbers if 
• The range of  is all negative real numbers if 
• The y-intercept is 
 and the horizontal asymptote is 
EXAMPLE 1 
Identifying Exponential Functions 
Which of the following equations are not exponential functions? 
• 
• 
• 
• 
Solution 
By definition, an exponential function has a constant as a base and an independent variable as an exponent. Thus, 
 does not represent an exponential function because the base is an independent variable. In fact, 
 is 
a power function. 
Recall that the base b of an exponential function is always a positive constant, and 
 Thus, 
 does not 
represent an exponential function because the base, 
 is less than 
 TRY IT 
#1 
Which of the following equations represent exponential functions? 
• 
• 
• 
• 
Evaluating Exponential Functions 
Recall that the base of an exponential function must be a positive real number other than 
 Why do we limit the base 
to positive values? To ensure that the outputs will be real numbers. Observe what happens if the base is not positive: 
• Let 
 and 
 Then 
 which is not a real number. 
Why do we limit the base to positive values other than 
 Because base  results in the constant function. Observe what 
happens if the base is 
• Let 
 Then 
 for any value of 
To evaluate an exponential function with the form 
 we simply substitute  with the given value, and calculate 
400     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 5 (book page 411) ---
the resulting power. For example: 
Let 
 What is 
To evaluate an exponential function with a form other than the basic form, it is important to follow the order of 
operations. For example: 
Let 
 What is 
Note that if the order of operations were not followed, the result would be incorrect: 
EXAMPLE 2 
Evaluating Exponential Functions 
Let 
 Evaluate 
 without using a calculator. 
Solution 
Follow the order of operations. Be sure to pay attention to the parentheses. 
 TRY IT 
#2 
Let 
 Evaluate 
 using a calculator. Round to four decimal places. 
Defining Exponential Growth 
Because the output of exponential functions increases very rapidly, the term “exponential growth” is often used in 
everyday language to describe anything that grows or increases rapidly. However, exponential growth can be defined 
more precisely in a mathematical sense. If the growth rate is proportional to the amount present, the function models 
exponential growth. 
Exponential Growth 
A function that models exponential growth grows by a rate proportional to the amount present. For any real number 
 and any positive real numbers 
 and  such that 
 an exponential growth function has the form 
where 
• 
 is the initial or starting value of the function. 
• 
 is the growth factor or growth multiplier per unit  . 
In more general terms, we have an exponential function, in which a constant base is raised to a variable exponent. To 
differentiate between linear and exponential functions, let’s consider two companies, A and B. Company A has 100 stores 
and expands by opening 50 new stores a year, so its growth can be represented by the function 
4.1 • Exponential Functions     401


--- PDF page 6 (book page 412) ---
Company B has 100 stores and expands by increasing the number of stores by 50% each year, so its growth can be 
represented by the function 
A few years of growth for these companies are illustrated in Table 3. 
Year, 
Stores, Company A 
Stores, Company B 
Table 3 
The graphs comparing the number of stores for each company over a five-year period are shown in Figure 2. We can see 
that, with exponential growth, the number of stores increases much more rapidly than with linear growth. 
Figure 2 The graph shows the numbers of stores Companies A and B opened over a five-year period. 
402     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 7 (book page 413) ---
...
Notice that the domain for both functions is 
∞
 and the range for both functions is 
∞
 After year 1, Company B 
always has more stores than Company A. 
Now we will turn our attention to the function representing the number of stores for Company B, 
In this exponential function, 100 represents the initial number of stores, 0.50 represents the growth rate, and 
 represents the growth factor. Generalizing further, we can write this function as 
 where 
100 is the initial value, 
 is called the base, and  is called the exponent. 
EXAMPLE 3 
Evaluating a Real-World Exponential Model 
At the beginning of this section, we learned that the population of India was about 
 billion in the year 2013, with an 
annual growth rate of about 
 This situation is represented by the growth function 
 where  is 
the number of years since 
 To the nearest thousandth, what will the population of India be in 
Solution 
To estimate the population in 2031, we evaluate the models for 
 because 2031 is 
 years after 2013. Rounding to 
the nearest thousandth, 
There will be about 1.549 billion people in India in the year 2031. 
 TRY IT 
#3 
The population of China was about 1.39 billion in the year 2013, with an annual growth rate of 
about 
 This situation is represented by the growth function 
 where  is 
the number of years since 
 To the nearest thousandth, what will the population of China be 
for the year 2031? How does this compare to the population prediction we made for India in 
Example 3? 
Finding Equations of Exponential Functions 
In the previous examples, we were given an exponential function, which we then evaluated for a given input. Sometimes 
we are given information about an exponential function without knowing the function explicitly. We must use the 
information to first write the form of the function, then determine the constants  and 
 and evaluate the function. 
HOW TO 
Given two data points, write an exponential model. 
1. If one of the data points has the form 
 then  is the initial value. Using 
 substitute the second point into 
the equation 
 and solve for 
2. If neither of the data points have the form 
 substitute both points into two equations with the form 
 Solve the resulting system of two equations in two unknowns to find  and 
3. Using the  and  found in the steps above, write the exponential function in the form 
EXAMPLE 4 
Writing an Exponential Model When the Initial Value Is Known 
In 2006, 80 deer were introduced into a wildlife refuge. By 2012, the population had grown to 180 deer. The population 
was growing exponentially. Write an exponential function 
 representing the population 
 of deer over time 
Solution 
We let our independent variable  be the number of years after 2006. Thus, the information given in the problem can be 
written as input-output pairs: (0, 80) and (6, 180). Notice that by choosing our input variable to be measured as years 
after 2006, we have given ourselves the initial value for the function, 
 We can now substitute the second point 
into the equation 
 to find 
4.1 • Exponential Functions     403


--- PDF page 8 (book page 414) ---
NOTE: Unless otherwise stated, do not round any intermediate calculations. Then round the final answer to four places 
for the remainder of this section. 
The exponential model for the population of deer is 
 (Note that this exponential function models 
short-term growth. As the inputs gets large, the output will get increasingly larger, so much so that the model may not 
be useful in the long term.) 
We can graph our model to observe the population growth of deer in the refuge over time. Notice that the graph in 
Figure 3 passes through the initial points given in the problem, 
 and 
 We can also see that the domain for 
the function is 
∞
 and the range for the function is 
∞
Figure 3 Graph showing the population of deer over time, 
  years after 2006 
 TRY IT 
#4 
A wolf population is growing exponentially. In 2011, 
 wolves were counted. By 
 the 
population had reached 236 wolves. What two points can be used to derive an exponential 
equation modeling this situation? Write the equation representing the population 
 of wolves 
over time 
EXAMPLE 5 
Writing an Exponential Model When the Initial Value is Not Known 
Find an exponential function that passes through the points 
 and 
Solution 
Because we don’t have the initial value, we substitute both points into an equation of the form 
 and then 
solve the system for  and 
• Substituting 
 gives 
• Substituting 
 gives 
Use the first equation to solve for  in terms of 
404     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 9 (book page 415) ---
Substitute  in the second equation, and solve for 
Use the value of  in the first equation to solve for the value of 
Thus, the equation is 
We can graph our model to check our work. Notice that the graph in Figure 4 passes through the initial points given in 
the problem, 
 and 
 The graph is an example of an exponential decay function. 
Figure 4 The graph of 
 models exponential decay. 
 TRY IT 
#5 
Given the two points 
 and 
 find the equation of the exponential function that passes 
through these two points. 
 Q&A 
Do two points always determine a unique exponential function? 
Yes, provided the two points are either both above the x-axis or both below the x-axis and have 
different x-coordinates. But keep in mind that we also need to know that the graph is, in fact, an 
exponential function. Not every graph that looks exponential really is exponential. We need to know 
the graph is based on a model that shows the same percent growth with each unit increase in 
 which 
in many real world cases involves time. 
4.1 • Exponential Functions     405


--- PDF page 10 (book page 416) ---
...
HOW TO 
Given the graph of an exponential function, write its equation. 
1. First, identify two points on the graph. Choose the y-intercept as one of the two points whenever possible. Try to 
choose points that are as far apart as possible to reduce round-off error. 
2. If one of the data points is the y-intercept 
 , then  is the initial value. Using 
 substitute the second point 
into the equation 
 and solve for 
3. If neither of the data points have the form 
 substitute both points into two equations with the form 
 Solve the resulting system of two equations in two unknowns to find  and 
4. Write the exponential function, 
EXAMPLE 6 
Writing an Exponential Function Given Its Graph 
Find an equation for the exponential function graphed in Figure 5. 
Figure 5 
Solution 
We can choose the y-intercept of the graph, 
 as our first point. This gives us the initial value, 
 Next, choose a 
point on the curve some distance away from 
 that has integer coordinates. One such point is 
Because we restrict ourselves to positive values of 
 we will use 
 Substitute  and  into the standard form to yield 
the equation 
 TRY IT 
#6 
Find an equation for the exponential function graphed in Figure 6. 
406     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 11 (book page 417) ---
...
Figure 6 
HOW TO 
Given two points on the curve of an exponential function, use a graphing calculator to find the equation. 
1. Press [STAT]. 
2. Clear any existing entries in columns L1 or L2. 
3. In L1, enter the x-coordinates given. 
4. In L2, enter the corresponding y-coordinates. 
5. Press [STAT] again. Cursor right to CALC, scroll down to ExpReg (Exponential Regression), and press [ENTER]. 
6. The screen displays the values of a and b in the exponential equation 
 . 
EXAMPLE 7 
Using a Graphing Calculator to Find an Exponential Function 
Use a graphing calculator to find the exponential equation that includes the points 
 and 
Solution 
Follow the guidelines above. First press [STAT], [EDIT], [1: Edit…], and clear the lists L1 and L2. Next, in the L1 column, 
enter the x-coordinates, 2 and 5. Do the same in the L2 column for the y-coordinates, 24.8 and 198.4. 
Now press [STAT], [CALC], [0: ExpReg] and press [ENTER]. The values 
 and 
 will be displayed. The 
exponential equation is 
 TRY IT 
#7 
Use a graphing calculator to find the exponential equation that includes the points (3, 75.98) and 
(6, 481.07). 
Applying the Compound-Interest Formula 
Savings instruments in which earnings are continually reinvested, such as mutual funds and retirement accounts, use 
compound interest. The term compounding refers to interest earned not only on the original value, but on the 
accumulated value of the account. 
The annual percentage rate (APR) of an account, also called the nominal rate, is the yearly interest rate earned by an 
investment account. The term nominal is used when the compounding occurs a number of times other than once per 
year. In fact, when interest is compounded more than once a year, the effective interest rate ends up being greater than 
the nominal rate! This is a powerful tool for investing. 
4.1 • Exponential Functions     407


--- PDF page 12 (book page 418) ---
We can calculate the compound interest using the compound interest formula, which is an exponential function of the 
variables time  principal 
 APR  and number of compounding periods in a year 
For example, observe Table 4, which shows the result of investing $1,000 at 10% for one year. Notice how the value of the 
account increases as the compounding frequency increases. 
Frequency 
Value after 1 year 
Annually 
$1100 
Semiannually 
$1102.50 
Quarterly 
$1103.81 
Monthly 
$1104.71 
Daily 
$1105.16 
Table 4 
The Compound Interest Formula 
Compound interest can be calculated using the formula 
where 
• 
 is the account value, 
• 
 is measured in years, 
• 
 is the starting amount of the account, often called the principal, or more generally present value, 
• 
 is the annual percentage rate (APR) expressed as a decimal, and 
• 
 is the number of compounding periods in one year. 
EXAMPLE 8 
Calculating Compound Interest 
If we invest $3,000 in an investment account paying 3% interest compounded quarterly, how much will the account be 
worth in 10 years? 
Solution 
Because we are starting with $3,000, 
 Our interest rate is 3%, so 
 Because we are compounding 
quarterly, we are compounding 4 times per year, so 
 We want to know the value of the account in 10 years, so we 
are looking for 
 the value when 
The account will be worth about $4,045.05 in 10 years. 
 TRY IT 
#8 
An initial investment of $100,000 at 12% interest is compounded weekly (use 52 weeks in a year). 
What will the investment be worth in 30 years? 
408     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 13 (book page 419) ---
EXAMPLE 9 
Using the Compound Interest Formula to Solve for the Principal 
A 529 Plan is a college-savings plan that allows relatives to invest money to pay for a child’s future college tuition; the 
account grows tax-free. Lily wants to set up a 529 account for her new granddaughter and wants the account to grow to 
$40,000 over 18 years. She believes the account will earn 6% compounded semi-annually (twice a year). To the nearest 
dollar, how much will Lily need to invest in the account now? 
Solution 
The nominal interest rate is 6%, so 
 Interest is compounded twice a year, so 
We want to find the initial investment, 
 needed so that the value of the account will be worth $40,000 in 
 years. 
Substitute the given values into the compound interest formula, and solve for 
Lily will need to invest $13,801 to have $40,000 in 18 years. 
 TRY IT 
#9 
Refer to Example 9. To the nearest dollar, how much would Lily need to invest if the account is 
compounded quarterly? 
Evaluating Functions with Base e 
As we saw earlier, the amount earned on an account increases as the compounding frequency increases. Table 5 shows 
that the increase from annual to semi-annual compounding is larger than the increase from monthly to daily 
compounding. This might lead us to ask whether this pattern will continue. 
Examine the value of $1 invested at 100% interest for 1 year, compounded at various frequencies, listed in Table 5. 
Frequency 
Value 
Annually 
$2 
Semiannually 
$2.25 
Quarterly 
$2.441406 
Monthly 
$2.613035 
Daily 
$2.714567 
Hourly 
$2.718127 
Once per minute 
$2.718279 
Once per second 
$2.718282 
Table 5 
4.1 • Exponential Functions     409


--- PDF page 14 (book page 420) ---
These values appear to be approaching a limit as  increases without bound. In fact, as  gets larger and larger, the 
expression 
 approaches a number used so frequently in mathematics that it has its own name: the letter 
 This 
value is an irrational number, which means that its decimal expansion goes on forever without repeating. Its 
approximation to six decimal places is shown below. 
The Number 
The letter e represents the irrational number 
The letter e is used as a base for many real-world exponential models. To work with base e, we use the 
approximation, 
 The constant was named by the Swiss mathematician Leonhard Euler (1707–1783) who 
first investigated and discovered many of its properties. 
EXAMPLE 10 
Using a Calculator to Find Powers of e 
Calculate 
 Round to five decimal places. 
Solution 
On a calculator, press the button labeled 
 The window shows 
 Type 
 and then close parenthesis, 
Press [ENTER]. Rounding to  decimal places, 
 Caution: Many scientific calculators have an “Exp” button, 
which is used to enter numbers in scientific notation. It is not used to find powers of 
 TRY IT 
#10 
Use a calculator to find 
 Round to five decimal places. 
Investigating Continuous Growth 
So far we have worked with rational bases for exponential functions. For most real-world phenomena, however, e is used 
as the base for exponential functions. Exponential models that use  as the base are called continuous growth or decay 
models. We see these models in finance, computer science, and most of the sciences, such as physics, toxicology, and 
fluid dynamics. 
The Continuous Growth/Decay Formula 
For all real numbers  and all positive numbers  and  continuous growth or decay is represented by the formula 
where 
• 
 is the initial value, 
• 
 is the continuous growth rate per unit time, 
• and  is the elapsed time. 
If 
 , then the formula represents continuous growth. If 
 , then the formula represents continuous decay. 
For business applications, the continuous growth formula is called the continuous compounding formula and takes 
the form 
where 
• 
 is the principal or the initial invested, 
• 
 is the growth or interest rate per unit time, 
410     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 15 (book page 421) ---
...
• and  is the period or term of the investment. 
HOW TO 
Given the initial value, rate of growth or decay, and time  solve a continuous growth or decay function. 
1. Use the information in the problem to determine  , the initial value of the function. 
2. Use the information in the problem to determine the growth rate 
a. If the problem refers to continuous growth, then 
b. If the problem refers to continuous decay, then 
3. Use the information in the problem to determine the time 
4. Substitute the given information into the continuous growth formula and solve for 
EXAMPLE 11 
Calculating Continuous Growth 
A person invested $1,000 in an account earning a nominal 10% per year compounded continuously. How much was in 
the account at the end of one year? 
Solution 
Since the account is growing in value, this is a continuous compounding problem with growth rate 
 The initial 
investment was $1,000, so 
 We use the continuous compounding formula to find the value after 
 year: 
The account is worth $1,105.17 after one year. 
 TRY IT 
#11 
A person invests $100,000 at a nominal 12% interest per year compounded continuously. What 
will be the value of the investment in 30 years? 
EXAMPLE 12 
Calculating Continuous Decay 
Radon-222 decays at a continuous rate of 17.3% per day. How much will 100 mg of Radon-222 decay to in 3 days? 
Solution 
Since the substance is decaying, the rate, 
 , is negative. So, 
 The initial amount of radon-222 was 
 mg, so 
 We use the continuous decay formula to find the value after 
 days: 
So 59.5115 mg of radon-222 will remain. 
 TRY IT 
#12 
Using the data in Example 12, how much radon-222 will remain after one year? 
 MEDIA 
Access these online resources for additional instruction and practice with exponential functions. 
4.1 • Exponential Functions     411


--- PDF page 16 (book page 422) ---
Exponential Growth Function (https://openstax.org/l/expgrowth) 
Compound Interest (https://openstax.org/l/compoundint) 
 4.1 SECTION EXERCISES 
Verbal 
1 . Explain why the values of an 
increasing exponential 
function will eventually 
overtake the values of an 
increasing linear function. 
 2 . Given a formula for an 
exponential function, is it 
possible to determine 
whether the function grows 
or decays exponentially just 
by looking at the formula? 
Explain. 
 3 . The Oxford Dictionary 
defines the word nominal as 
a value that is “stated or 
expressed but not 
necessarily corresponding 
exactly to the real value.”3 
Develop a reasonable 
argument for why the term 
nominal rate is used to 
describe the annual 
percentage rate of an 
investment account that 
compounds interest. 
Algebraic 
For the following exercises, identify whether the statement represents an exponential function. Explain. 
4 . The average annual 
population increase of a 
pack of wolves is 25. 
 5 . A population of bacteria 
decreases by a factor of 
every 
 hours. 
 6 . The value of a coin 
collection has increased by 
 annually over the last 
 years. 
7 . For each training session, a 
personal trainer charges his 
clients 
 less than the 
previous training session. 
 8 . The height of a projectile at 
time  is represented by the 
function 
For the following exercises, consider this scenario: For each year  the population of a forest of trees is represented by 
the function 
 In a neighboring forest, the population of the same type of tree is represented by the 
function 
 (Round answers to the nearest whole number.) 
9 . Which forest’s population is 
growing at a faster rate? 
 10 . Which forest had a greater 
number of trees initially? 
By how many? 
 11 . Assuming the population 
growth models continue to 
represent the growth of 
the forests, which forest 
will have a greater number 
of trees after 
 years? By 
how many? 
3 Oxford Dictionary. http://oxforddictionaries.com/us/definition/american_english/nomina. 
412     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 17 (book page 423) ---
12 . Assuming the population 
growth models continue to 
represent the growth of 
the forests, which forest 
will have a greater number 
of trees after 
 years? By 
how many? 
 13 . Discuss the above results 
from the previous four 
exercises. Assuming the 
population growth models 
continue to represent the 
growth of the forests, 
which forest will have the 
greater number of trees in 
the long run? Why? What 
are some factors that 
might influence the long-
term validity of the 
exponential growth model? 
For the following exercises, determine whether the equation represents exponential growth, exponential decay, or 
neither. Explain. 
14 . 
 15 . 
 16 . 
17 . 
For the following exercises, find the formula for an exponential function that passes through the two points given. 
18 . 
 and 
 19 . 
 and 
 20 . 
 and 
21 . 
 and 
 22 . 
 and 
For the following exercises, determine whether the table could represent a function that is linear, exponential, or neither. 
If it appears to be exponential, find a function that passes through the points. 
23 . 
1 
2 
3 
4 
70 
40 
10 
-20 
 24 . 
1 
2 
3 
4 
70 
49 
34.3 
24.01 
25 . 
1 
2 
3 
4 
80 
61 
42.9 
25.61 
 26 . 
1 
2 
3 
4 
10 
20 
40 
80 
27 . 
1 
2 
3 
4 
-3.25 
2 
7.25 
12.5 
4.1 • Exponential Functions     413


--- PDF page 18 (book page 424) ---
For the following exercises, use the compound interest formula, 
28 . After a certain number of 
years, the value of an 
investment account is 
represented by the 
equation 
What is the value of the 
account? 
 29 . What was the initial 
deposit made to the 
account in the previous 
exercise? 
 30 . How many years had the 
account from the previous 
exercise been 
accumulating interest? 
31 . An account is opened with 
an initial deposit of $6,500 
and earns 
 interest 
compounded semi-
annually. What will the 
account be worth in 
years? 
 32 . How much more would the 
account in the previous 
exercise have been worth if 
the interest were 
compounding weekly? 
 33 . Solve the compound 
interest formula for the 
principal, 
 . 
34 . Use the formula found in 
the previous exercise to 
calculate the initial deposit 
of an account that is worth 
 after earning 
 interest compounded 
monthly for  years. 
(Round to the nearest 
dollar.) 
 35 . How much more would the 
account in the previous 
two exercises be worth if it 
were earning interest for 
more years? 
 36 . Use properties of rational 
exponents to solve the 
compound interest 
formula for the interest 
rate, 
37 . Use the formula found in 
the previous exercise to 
calculate the interest rate 
for an account that was 
compounded semi-
annually, had an initial 
deposit of $9,000 and was 
worth $13,373.53 after 10 
years. 
 38 . Use the formula found in 
the previous exercise to 
calculate the interest rate 
for an account that was 
compounded monthly, had 
an initial deposit of $5,500, 
and was worth $38,455 
after 30 years. 
For the following exercises, determine whether the equation represents continuous growth, continuous decay, or 
neither. Explain. 
39 . 
 40 . 
 41 . 
42 . Suppose an investment 
account is opened with an 
initial deposit of 
earning 
 interest 
compounded continuously. 
How much will the account 
be worth after 
 years? 
 43 . How much less would the 
account from Exercise 42 
be worth after 
 years if it 
were compounded 
monthly instead? 
Numeric 
For the following exercises, evaluate each function. Round answers to four decimal places, if necessary. 
44 . 
 for 
 45 . 
 for 
 46 . 
 for 
47 . 
 for 
 48 . 
for 
 49 . 
 for 
414     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 19 (book page 425) ---
50 . 
 for 
Technology 
For the following exercises, use a graphing calculator to find the equation of an exponential function given the points on 
the curve. 
51 . 
 and 
 52 . 
 and 
 53 . 
 and 
54 . 
 and 
 55 . 
 and 
Extensions 
56 . The annual percentage 
yield (APY) of an 
investment account is a 
representation of the 
actual interest rate earned 
on a compounding 
account. It is based on a 
compounding period of 
one year. Show that the 
APY of an account that 
compounds monthly can 
be found with the formula 
 57 . Repeat the previous 
exercise to find the formula 
for the APY of an account 
that compounds daily. Use 
the results from this and 
the previous exercise to 
develop a function 
 for 
the APY of any account 
that compounds  times 
per year. 
 58 . Recall that an exponential 
function is any equation 
written in the form 
 such that 
and 
 are positive 
numbers and 
 Any 
positive number 
 can be 
written as 
 for 
some value of 
 . Use this 
fact to rewrite the formula 
for an exponential function 
that uses the number 
 as 
a base. 
59 . In an exponential decay 
function, the base of the 
exponent is a value 
between 0 and 1. Thus, for 
some number 
 the 
exponential decay function 
can be written as 
 Use this 
formula, along with the 
fact that 
 to show 
that an exponential decay 
function takes the form 
 for some 
positive number  . 
 60 . The formula for the 
amount 
 in an investment 
account with a nominal 
interest rate  at any time 
is given by 
where  is the amount of 
principal initially deposited 
into an account that 
compounds continuously. 
Prove that the percentage 
of interest earned to 
principal at any time  can 
be calculated with the 
formula 
4.1 • Exponential Functions     415


--- PDF page 20 (book page 426) ---
Real-World Applications 
61 . The fox population in a 
certain region has an 
annual growth rate of 9% 
per year. In the year 2012, 
there were 23,900 fox 
counted in the area. What 
is the fox population 
predicted to be in the year 
2020? 
 62 . A scientist begins with 100 
milligrams of a radioactive 
substance that decays 
exponentially. After 35 
hours, 50mg of the 
substance remains. How 
many milligrams will 
remain after 54 hours? 
 63 . In the year 1985, a house 
was valued at $110,000. By 
the year 2005, the value 
had appreciated to 
$145,000. What was the 
annual growth rate 
between 1985 and 2005? 
Assume that the value 
continued to grow by the 
same percentage. What 
was the value of the house 
in the year 2010? 
64 . A car was valued at 
$38,000 in the year 2007. 
By 2013, the value had 
depreciated to $11,000 If 
the car’s value continues to 
drop by the same 
percentage, what will it be 
worth by 2017? 
 65 . Jaylen wants to save 
$54,000 for a down 
payment on a home. How 
much will he need to invest 
in an account with 8.2% 
APR, compounding daily, in 
order to reach his goal in 5 
years? 
 66 . Kyoko has $10,000 that she 
wants to invest. Her bank 
has several investment 
accounts to choose from, 
all compounding daily. Her 
goal is to have $15,000 by 
the time she finishes 
graduate school in 6 years. 
To the nearest hundredth 
of a percent, what should 
her minimum annual 
interest rate be in order to 
reach her goal? (Hint: solve 
the compound interest 
formula for the interest 
rate.) 
67 . Alyssa opened a retirement 
account with 7.25% APR in 
the year 2000. Her initial 
deposit was $13,500. How 
much will the account be 
worth in 2025 if interest 
compounds monthly? How 
much more would she 
make if interest 
compounded 
continuously? 
 68 . An investment account 
with an annual interest 
rate of 7% was opened 
with an initial deposit of 
$4,000 Compare the values 
of the account after 9 years 
when the interest is 
compounded annually, 
quarterly, monthly, and 
continuously. 
4.2 Graphs of Exponential Functions 
Learning Objectives 
Graph exponential functions. 
Graph exponential functions using transformations. 
As we discussed in the previous section, exponential functions are used for many real-world applications such as finance, 
forensics, computer science, and most of the life sciences. Working with an equation that describes a real-world situation 
gives us a method for making predictions. Most of the time, however, the equation itself is not enough. We learn a lot 
about things by seeing their pictorial representations, and that is exactly why graphing exponential equations is a 
powerful tool. It gives us another layer of insight for predicting future events. 
Graphing Exponential Functions 
Before we begin graphing, it is helpful to review the behavior of exponential growth. Recall the table of values for a 
function of the form 
 whose base is greater than one. We’ll use the function 
 Observe how the 
output values in Table 1 change as the input increases by 
416     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 21 (book page 427) ---
Table 1 
Each output value is the product of the previous output and the base, 
 We call the base  the constant ratio. In fact, for 
any exponential function with the form 
  is the constant ratio of the function. This means that as the input 
increases by 1, the output value will be the product of the base and the previous output, regardless of the value of 
Notice from the table that 
• the output values are positive for all values of 
• as  increases, the output values increase without bound; and 
• as  decreases, the output values grow smaller, approaching zero. 
Figure 1 shows the exponential growth function 
Figure 1 Notice that the graph gets close to the x-axis, but never touches it. 
The domain of 
 is all real numbers, the range is 
∞
 and the horizontal asymptote is 
To get a sense of the behavior of exponential decay, we can create a table of values for a function of the form 
 whose base is between zero and one. We’ll use the function 
 Observe how the output values in 
Table 2 change as the input increases by 
Table 2 
Again, because the input is increasing by 1, each output value is the product of the previous output and the base, or 
constant ratio 
Notice from the table that 
• the output values are positive for all values of 
• as  increases, the output values grow smaller, approaching zero; and 
• as  decreases, the output values grow without bound. 
Figure 2 shows the exponential decay function, 
4.2 • Graphs of Exponential Functions     417


--- PDF page 22 (book page 428) ---
Figure 2 
The domain of 
 is all real numbers, the range is 
∞
 and the horizontal asymptote is 
Characteristics of the Graph of the Parent Function 
An exponential function with the form 
 
 
 has these characteristics: 
• one-to-one function 
• horizontal asymptote: 
• domain: 
∞∞
• range: 
∞
• x-intercept: none 
• y-intercept: 
• increasing if 
• decreasing if 
Figure 3 compares the graphs of exponential growth and decay functions. 
Figure 3 
418     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 23 (book page 429) ---
...
HOW TO 
Given an exponential function of the form 
 graph the function. 
1. Create a table of points. 
2. Plot at least  point from the table, including the y-intercept 
3. Draw a smooth curve through the points. 
4. State the domain, 
∞∞
 the range, 
∞
 and the horizontal asymptote, 
EXAMPLE 1 
Sketching the Graph of an Exponential Function of the Form f(x) = bx 
Sketch a graph of 
 State the domain, range, and asymptote. 
Solution 
Before graphing, identify the behavior and create a table of points for the graph. 
• Since 
 is between zero and one, we know the function is decreasing. The left tail of the graph will increase 
without bound, and the right tail will approach the asymptote 
• Create a table of points as in Table 3. 
Table 3 
• Plot the y-intercept, 
 along with two other points. We can use 
 and 
Draw a smooth curve connecting the points as in Figure 4. 
Figure 4 
The domain is 
∞∞
 the range is 
∞
 the horizontal asymptote is 
 TRY IT 
#1 
Sketch the graph of 
 State the domain, range, and asymptote. 
Graphing Transformations of Exponential Functions 
Transformations of exponential graphs behave similarly to those of other functions. Just as with other parent functions, 
we can apply the four types of transformations—shifts, reflections, stretches, and compressions—to the parent function 
 without loss of shape. For instance, just as the quadratic function maintains its parabolic shape when shifted, 
reflected, stretched, or compressed, the exponential function also maintains its general shape regardless of the 
transformations applied. 
4.2 • Graphs of Exponential Functions     419


--- PDF page 24 (book page 430) ---
Graphing a Vertical Shift 
The first transformation occurs when we add a constant  to the parent function 
 giving us a vertical shift 
units in the same direction as the sign. For example, if we begin by graphing a parent function, 
 we can then 
graph two vertical shifts alongside it, using 
 the upward shift, 
 and the downward shift, 
 Both vertical shifts are shown in Figure 5. 
Figure 5 
Observe the results of shifting 
 vertically: 
• The domain, 
∞∞
 remains unchanged. 
• When the function is shifted up  units to 
◦ The y-intercept shifts up  units to 
◦ The asymptote shifts up  units to 
◦ The range becomes 
∞
• When the function is shifted down  units to 
◦ The y-intercept shifts down  units to 
◦ The asymptote also shifts down  units to 
◦ The range becomes 
∞
Graphing a Horizontal Shift 
The next transformation occurs when we add a constant  to the input of the parent function 
 giving us a 
horizontal shift  units in the opposite direction of the sign. For example, if we begin by graphing the parent function 
 we can then graph two horizontal shifts alongside it, using 
 the shift left, 
 and the shift 
right, 
 Both horizontal shifts are shown in Figure 6. 
Figure 6 
Observe the results of shifting 
 horizontally: 
• The domain, 
∞∞
 remains unchanged. 
• The asymptote, 
 remains unchanged. 
• The y-intercept shifts such that: 
◦ When the function is shifted left  units to 
 the y-intercept becomes 
 This is because 
 so the initial value of the function is 
◦ When the function is shifted right  units to 
 the y-intercept becomes 
 Again, see that 
 so the initial value of the function is 
420     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 25 (book page 431) ---
...
Shifts of the Parent Function f(x) = b x 
For any constants  and 
 the function 
 shifts the parent function 
• vertically  units, in the same direction of the sign of 
• horizontally  units, in the opposite direction of the sign of 
• The y-intercept becomes 
• The horizontal asymptote becomes 
• The range becomes 
∞
• The domain, 
∞∞
 remains unchanged. 
HOW TO 
Given an exponential function with the form 
 graph the translation. 
1. Draw the horizontal asymptote 
2. Identify the shift as 
 Shift the graph of 
 left  units if  is positive, and right  units if  is 
negative. 
3. Shift the graph of 
 up  units if  is positive, and down  units if  is negative. 
4. State the domain, 
∞∞
 the range, 
∞
 and the horizontal asymptote 
EXAMPLE 2 
Graphing a Shift of an Exponential Function 
Graph 
 State the domain, range, and asymptote. 
Solution 
We have an exponential equation of the form 
 with 
 
 and 
Draw the horizontal asymptote 
 , so draw 
Identify the shift as 
 so the shift is 
Shift the graph of 
 left 1 units and down 3 units. 
Figure 7 
The domain is 
∞∞
 the range is 
∞
 the horizontal asymptote is 
 TRY IT 
#2 
Graph 
 State domain, range, and asymptote. 
4.2 • Graphs of Exponential Functions     421


--- PDF page 26 (book page 432) ---
...
HOW TO 
Given an equation of the form 
 for 
 use a graphing calculator to approximate the solution. 
• Press [Y=]. Enter the given exponential equation in the line headed “Y1=”. 
• Enter the given value for 
 in the line headed “Y2=”. 
• Press [WINDOW]. Adjust the y-axis so that it includes the value entered for “Y2=”. 
• Press [GRAPH] to observe the graph of the exponential function along with the line for the specified value of 
• To find the value of 
 we compute the point of intersection. Press [2ND] then [CALC]. Select “intersect” and press 
[ENTER] three times. The point of intersection gives the value of x for the indicated value of the function. 
EXAMPLE 3 
Approximating the Solution of an Exponential Equation 
Solve 
 graphically. Round to the nearest thousandth. 
Solution 
Press [Y=] and enter 
 next to Y1=. Then enter 42 next to Y2=. For a window, use the values –3 to 3 for  and 
–5 to 55 for 
 Press [GRAPH]. The graphs should intersect somewhere near 
For a better approximation, press [2ND] then [CALC]. Select [5: intersect] and press [ENTER] three times. The 
x-coordinate of the point of intersection is displayed as 2.1661943. (Your answer may be different if you use a different 
window or use a different value for Guess?) To the nearest thousandth, 
 TRY IT 
#3 
Solve 
 graphically. Round to the nearest thousandth. 
Graphing a Stretch or Compression 
While horizontal and vertical shifts involve adding constants to the input or to the function itself, a stretch or 
compression occurs when we multiply the parent function 
 by a constant 
 For example, if we begin by 
graphing the parent function 
 we can then graph the stretch, using 
 to get 
 as shown on 
the left in Figure 8, and the compression, using 
 to get 
 as shown on the right in Figure 8. 
Figure 8 (a) 
 stretches the graph of 
 vertically by a factor of 
 (b) 
 compresses the 
graph of 
 vertically by a factor of 
422     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 27 (book page 433) ---
Stretches and Compressions of the Parent Function 
For any factor 
 the function 
• is stretched vertically by a factor of  if 
• is compressed vertically by a factor of  if 
• has a y-intercept of 
• has a horizontal asymptote at 
 a range of 
∞
 and a domain of 
∞∞
 which are unchanged from 
the parent function. 
EXAMPLE 4 
Graphing the Stretch of an Exponential Function 
Sketch a graph of 
 State the domain, range, and asymptote. 
Solution 
Before graphing, identify the behavior and key points on the graph. 
• Since 
 is between zero and one, the left tail of the graph will increase without bound as  decreases, and the 
right tail will approach the x-axis as  increases. 
• Since 
 the graph of 
 will be stretched by a factor of 
• Create a table of points as shown in Table 4. 
Table 4 
• Plot the y-intercept, 
 along with two other points. We can use 
 and 
Draw a smooth curve connecting the points, as shown in Figure 9. 
Figure 9 
The domain is 
∞∞
 the range is 
∞
 the horizontal asymptote is 
 TRY IT 
#4 
Sketch the graph of 
 State the domain, range, and asymptote. 
Graphing Reflections 
In addition to shifting, compressing, and stretching a graph, we can also reflect it about the x-axis or the y-axis. When we 
multiply the parent function 
 by 
 we get a reflection about the x-axis. When we multiply the input by 
 we 
get a reflection about the y-axis. For example, if we begin by graphing the parent function 
 we can then graph 
the two reflections alongside it. The reflection about the x-axis, 
 is shown on the left side of Figure 10, and 
4.2 • Graphs of Exponential Functions     423


--- PDF page 28 (book page 434) ---
the reflection about the y-axis 
 is shown on the right side of Figure 10. 
Figure 10 (a) 
 reflects the graph of 
 about the x-axis. (b) 
 reflects the graph of 
about the y-axis. 
Reflections of the Parent Function 
The function 
• reflects the parent function 
 about the x-axis. 
• has a y-intercept of 
• has a range of 
∞
• has a horizontal asymptote at 
 and domain of 
∞∞
 which are unchanged from the parent function. 
The function 
• reflects the parent function 
 about the y-axis. 
• has a y-intercept of 
 a horizontal asymptote at 
 a range of 
∞
 and a domain of 
∞∞
 which 
are unchanged from the parent function. 
EXAMPLE 5 
Writing and Graphing the Reflection of an Exponential Function 
Find and graph the equation for a function, 
 that reflects 
 about the x-axis. State its domain, range, and 
asymptote. 
Solution 
Since we want to reflect the parent function 
 about the x-axis, we multiply 
 by 
 to get, 
Next we create a table of points as in Table 5. 
Table 5 
Plot the y-intercept, 
 along with two other points. We can use 
 and 
Draw a smooth curve connecting the points: 
424     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 29 (book page 435) ---
Figure 11 
The domain is 
∞∞
 the range is 
∞
 the horizontal asymptote is 
 TRY IT 
#5 
Find and graph the equation for a function, 
 that reflects 
 about the y-axis. State 
its domain, range, and asymptote. 
Summarizing Translations of the Exponential Function 
Now that we have worked with each type of translation for the exponential function, we can summarize them in Table 6 
to arrive at the general equation for translating exponential functions. 
Transformations of the Parent Function 
Transformation 
Form 
Shift 
• Horizontally  units to the left 
• Vertically  units up 
Stretch and Compress 
• Stretch if 
• Compression if 
Reflect about the x-axis 
Reflect about the y-axis 
General equation for all transformations 
Table 6 
Translations of Exponential Functions 
A translation of an exponential function has the form 
4.1 
Where the parent function, 
 
 is 
• shifted horizontally  units to the left. 
4.2 • Graphs of Exponential Functions     425


--- PDF page 30 (book page 436) ---
• stretched vertically by a factor of 
 if 
• compressed vertically by a factor of 
 if 
• shifted vertically  units. 
• reflected about the x-axis when 
Note the order of the shifts, transformations, and reflections follow the order of operations. 
EXAMPLE 6 
Writing a Function from a Description 
Write the equation for the function described below. Give the horizontal asymptote, the domain, and the range. 
• 
 is vertically stretched by a factor of  , reflected across the y-axis, and then shifted up  units. 
Solution 
We want to find an equation of the general form 
 We use the description provided to find 
 
  and 
• We are given the parent function 
 so 
• The function is stretched by a factor of  , so 
• The function is reflected about the y-axis. We replace  with 
 to get: 
• The graph is shifted vertically 4 units, so 
Substituting in the general form we get, 
The domain is 
∞∞
 the range is 
∞
 the horizontal asymptote is 
 TRY IT 
#6 
Write the equation for function described below. Give the horizontal asymptote, the domain, and 
the range. 
• 
 is compressed vertically by a factor of 
 reflected across the x-axis and then 
shifted down  units. 
 MEDIA 
Access this online resource for additional instruction and practice with graphing exponential functions. 
Graph Exponential Functions (https://openstax.org/l/graphexpfunc) 
 4.2 SECTION EXERCISES 
Verbal 
1 . What role does the 
horizontal asymptote of an 
exponential function play in 
telling us about the end 
behavior of the graph? 
 2 . What is the advantage of 
knowing how to recognize 
transformations of the 
graph of a parent function 
algebraically? 
426     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 31 (book page 437) ---
Algebraic 
3 . The graph of 
 is 
reflected about the y-axis 
and stretched vertically by a 
factor of 
 What is the 
equation of the new 
function, 
 State its 
y-intercept, domain, and 
range. 
 4 . The graph of 
is reflected about the y-axis 
and compressed vertically 
by a factor of 
 What is the 
equation of the new 
function, 
 State its 
y-intercept, domain, and 
range. 
 5 . The graph of 
 is 
reflected about the x-axis 
and shifted upward  units. 
What is the equation of the 
new function, 
 State its 
y-intercept, domain, and 
range. 
6 . The graph of 
is shifted right  units, 
stretched vertically by a 
factor of 
 reflected about 
the x-axis, and then shifted 
downward  units. What is 
the equation of the new 
function, 
 State its 
y-intercept (to the nearest 
thousandth), domain, and 
range. 
 7 . The graph of 
 is 
shifted downward  units, 
and then shifted left  units, 
stretched vertically by a 
factor of 
 and reflected 
about the x-axis. What is the 
equation of the new 
function, 
 State its 
y-intercept, domain, and 
range. 
Graphical 
For the following exercises, graph the function and its reflection about the y-axis on the same axes, and give the 
y-intercept. 
8 . 
 9 . 
10 . 
For the following exercises, graph each set of functions on the same axes. 
11 . 
 and 
12 . 
 
 and 
For the following exercises, match each function with one of the graphs in Figure 12. 
Figure 12 
13 . 
 14 . 
 15 . 
16 . 
 17 . 
 18 . 
4.2 • Graphs of Exponential Functions     427


--- PDF page 32 (book page 438) ---
For the following exercises, use the graphs shown in Figure 13. All have the form 
Figure 13 
19 . Which graph has the 
largest value for 
 20 . Which graph has the 
smallest value for 
 21 . Which graph has the 
largest value for 
22 . Which graph has the 
smallest value for 
For the following exercises, graph the function and its reflection about the x-axis on the same axes. 
23 . 
24 . 
 25 . 
For the following exercises, graph the transformation of 
 Give the horizontal asymptote, the domain, and the 
range. 
26 . 
 27 . 
28 . 
For the following exercises, describe the end behavior of the graphs of the functions. 
29 . 
 30 . 
 31 . 
For the following exercises, start with the graph of 
 Then write a function that results from the given 
transformation. 
32 . Shift 
 4 units upward 
 33 . Shift 
 3 units 
downward 
 34 . Shift 
 2 units left 
35 . Shift 
 5 units right 
 36 . Reflect 
 about the 
x-axis 
 37 . Reflect 
 about the 
y-axis 
For the following exercises, each graph is a transformation of 
 Write an equation describing the transformation. 
38 . 
39 . 
40 . 
428     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 33 (book page 439) ---
For the following exercises, find an exponential equation for the graph. 
41 . 
42 . 
Numeric 
For the following exercises, evaluate the exponential functions for the indicated value of 
43 . 
 for 
 44 . 
 for 
 45 . 
 for 
Technology 
For the following exercises, use a graphing calculator to approximate the solutions of the equation. Round to the nearest 
thousandth. 
46 . 
 47 . 
 48 . 
49 . 
 50 . 
Extensions 
51 . Explore and discuss the graphs of 
and 
 Then make a conjecture about 
the relationship between the graphs of the 
functions 
 and 
 for any real number 
 52 . Prove the conjecture made in the previous 
exercise. 
53 . Explore and discuss the graphs of 
 and 
 Then make a 
conjecture about the relationship between the 
graphs of the functions 
 and 
 for any 
real number n and real number 
 54 . Prove the conjecture made in the previous 
exercise. 
4.3 Logarithmic Functions 
Learning Objectives 
In this section, you will: 
Convert from logarithmic to exponential form. 
Convert from exponential to logarithmic form. 
Evaluate logarithms. 
Use common logarithms. 
Use natural logarithms. 
4.3 • Logarithmic Functions     429


--- PDF page 34 (book page 440) ---
Figure 1 Devastation of March 11, 2011 earthquake in Honshu, Japan. (credit: Daniel Pierce) 
In 2010, a major earthquake struck Haiti, destroying or damaging over 285,000 homes4 . One year later, another, 
stronger earthquake devastated Honshu, Japan, destroying or damaging over 332,000 buildings,5  like those shown in 
Figure 1. Even though both caused substantial damage, the earthquake in 2011 was 100 times stronger than the 
earthquake in Haiti. How do we know? The magnitudes of earthquakes are measured on a scale known as the Richter 
Scale. The Haitian earthquake registered a 7.0 on the Richter Scale6  whereas the Japanese earthquake registered a 9.0.7 
The Richter Scale is a base-ten logarithmic scale. In other words, an earthquake of magnitude 8 is not twice as great as 
an earthquake of magnitude 4. It is 
 times as great! In this lesson, we will investigate the nature of 
the Richter Scale and the base-ten function upon which it depends. 
Converting from Logarithmic to Exponential Form 
In order to analyze the magnitude of earthquakes or compare the magnitudes of two different earthquakes, we need to 
be able to convert between logarithmic and exponential form. For example, suppose the amount of energy released 
from one earthquake were 500 times greater than the amount of energy released from another. We want to calculate the 
difference in magnitude. The equation that represents this problem is 
 where  represents the difference in 
magnitudes on the Richter Scale. How would we solve for 
We have not yet learned a method for solving exponential equations. None of the algebraic tools discussed so far is 
sufficient to solve 
 We know that 
 and 
 so it is clear that  must be some value between 
2 and 3, since 
 is increasing. We can examine a graph, as in Figure 2, to better estimate the solution. 
4 http://earthquake.usgs.gov/earthquakes/eqinthenews/2010/us2010rja6/#summary. Accessed 3/4/2013. 
5 http://earthquake.usgs.gov/earthquakes/eqinthenews/2011/usc0001xgp/#summary. Accessed 3/4/2013. 
6 http://earthquake.usgs.gov/earthquakes/eqinthenews/2010/us2010rja6/. Accessed 3/4/2013. 
7 http://earthquake.usgs.gov/earthquakes/eqinthenews/2011/usc0001xgp/#details. Accessed 3/4/2013. 
430     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 35 (book page 441) ---
Figure 2 
Estimating from a graph, however, is imprecise. To find an algebraic solution, we must introduce a new function. Observe 
that the graph in Figure 2 passes the horizontal line test. The exponential function 
 is one-to-one, so its inverse, 
 is also a function. As is the case with all inverse functions, we simply interchange  and  and solve for  to find 
the inverse function. To represent  as a function of 
 we use a logarithmic function of the form 
 The base 
logarithm of a number is the exponent by which we must raise  to get that number. 
We read a logarithmic expression as, “The logarithm with base  of  is equal to 
 ” or, simplified, “log base  of  is 
 ” 
We can also say, “  raised to the power of  is 
 ” because logs are exponents. For example, the base 2 logarithm of 32 
is 5, because 5 is the exponent we must apply to 2 to get 32. Since 
 we can write 
 We read this as “log 
base 2 of 32 is 5.” 
We can express the relationship between logarithmic form and its corresponding exponential form as follows: 
Note that the base  is always positive. 
Because logarithm is a function, it is most correctly written as 
 using parentheses to denote function evaluation, 
just as we would with 
 However, when the input is a single variable or number, it is common to see the parentheses 
dropped and the expression written without parentheses, as 
 Note that many calculators require parentheses 
around the 
We can illustrate the notation of logarithms as follows: 
Notice that, comparing the logarithm function and the exponential function, the input and the output are switched. This 
means 
 and 
 are inverse functions. 
Definition of the Logarithmic Function 
A logarithm base  of a positive number  satisfies the following definition. 
4.3 • Logarithmic Functions     431


--- PDF page 36 (book page 442) ---
...
For 
where, 
• we read 
 as, “the logarithm with base  of  ” or the “log base  of 
• the logarithm  is the exponent to which  must be raised to get 
Also, since the logarithmic and exponential functions switch the  and  values, the domain and range of the 
exponential function are interchanged for the logarithmic function. Therefore, 
• the domain of the logarithm function with base 
∞
• the range of the logarithm function with base 
∞∞
 Q&A 
Can we take the logarithm of a negative number? 
No. Because the base of an exponential function is always positive, no power of that base can ever be 
negative. We can never take the logarithm of a negative number. Also, we cannot take the logarithm of 
zero. Calculators may output a log of a negative number when in complex mode, but the log of a 
negative number is not a real number. 
HOW TO 
Given an equation in logarithmic form 
 convert it to exponential form. 
1. Examine the equation 
 and identify 
2. Rewrite 
 as 
EXAMPLE 1 
Converting from Logarithmic Form to Exponential Form 
Write the following logarithmic equations in exponential form. 
ⓐ 
 ⓑ 
Solution 
First, identify the values of 
 Then, write the equation in the form 
ⓐ 
Here, 
 Therefore, the equation 
 is equivalent to 
ⓑ 
Here, 
 Therefore, the equation 
 is equivalent to 
 TRY IT 
#1 
Write the following logarithmic equations in exponential form. 
ⓐ
 ⓑ
Converting from Exponential to Logarithmic Form 
To convert from exponents to logarithms, we follow the same steps in reverse. We identify the base 
 exponent 
 and 
output 
 Then we write 
432     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 37 (book page 443) ---
...
EXAMPLE 2 
Converting from Exponential Form to Logarithmic Form 
Write the following exponential equations in logarithmic form. 
a. 
b. 
c. 
Solution 
First, identify the values of 
 Then, write the equation in the form 
a. 
Here, 
 
 and 
 Therefore, the equation 
 is equivalent to 
b. 
Here, 
 
 and 
 Therefore, the equation 
 is equivalent to 
c. 
Here, 
 
 and 
 Therefore, the equation 
 is equivalent to 
 TRY IT 
#2 
Write the following exponential equations in logarithmic form. 
ⓐ 
 ⓑ 
 ⓒ 
Evaluating Logarithms 
Knowing the squares, cubes, and roots of numbers allows us to evaluate many logarithms mentally. For example, 
consider 
 We ask, “To what exponent must  be raised in order to get 8?” Because we already know 
 it 
follows that 
Now consider solving 
 and 
 mentally. 
• We ask, “To what exponent must 7 be raised in order to get 49?” We know 
 Therefore, 
• We ask, “To what exponent must 3 be raised in order to get 27?” We know 
 Therefore, 
Even some seemingly more complicated logarithms can be evaluated without a calculator. For example, let’s evaluate 
 mentally. 
• We ask, “To what exponent must 
 be raised in order to get 
 ” We know 
 and 
 so 
Therefore, 
HOW TO 
Given a logarithm of the form 
 evaluate it mentally. 
1. Rewrite the argument  as a power of 
 
2. Use previous knowledge of powers of  identify  by asking, “To what exponent should  be raised in order to get 
 ” 
EXAMPLE 3 
Solving Logarithms Mentally 
Solve 
 without using a calculator. 
4.3 • Logarithmic Functions     433


--- PDF page 38 (book page 444) ---
Solution 
First we rewrite the logarithm in exponential form: 
 Next, we ask, “To what exponent must 4 be raised in order to 
get 64?” 
We know 
Therefore, 
 TRY IT 
#3 
Solve 
 without using a calculator. 
EXAMPLE 4 
Evaluating the Logarithm of a Reciprocal 
Evaluate 
 without using a calculator. 
Solution 
First we rewrite the logarithm in exponential form: 
 Next, we ask, “To what exponent must 3 be raised in order 
to get 
 ” 
We know 
 but what must we do to get the reciprocal, 
 Recall from working with exponents that 
We use this information to write 
Therefore, 
 TRY IT 
#4 
Evaluate 
 without using a calculator. 
Using Common Logarithms 
Sometimes you may see a logarithm written without a base. When you see one written this way, you need to look at the 
expression before evaluating it. It may be that the base you use doesn't matter. If you find it in computer science, it often 
means 
. However, in mathematics it almost always means the common logarithm of 10. In other words, the 
expression 
 often means 
Definition of the Common Logarithm 
A common logarithm is a logarithm with base 
 We can also write 
 simply as 
 The common 
logarithm of a positive number  satisfies the following definition. 
For 
We read 
 as, “the logarithm with base 
 of  ” or “log base 10 of 
 ” 
The logarithm  is the exponent to which 
 must be raised to get 
Currently, we use 
 as the common logarithm, 
 as the binary logarithm, and 
 as the natural 
logarithm. Writing 
 without specifying a base is now considered bad form, despite being frequently found in older 
materials. 
434     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 39 (book page 445) ---
...
...
HOW TO 
Given a common logarithm of the form 
 evaluate it mentally. 
1. Rewrite the argument  as a power of 
 
2. Use previous knowledge of powers of 
 to identify  by asking, “To what exponent must 
 be raised in order to 
get 
 ” 
EXAMPLE 5 
Finding the Value of a Common Logarithm Mentally 
Evaluate 
 without using a calculator. 
Solution 
First we rewrite the logarithm in exponential form: 
 Next, we ask, “To what exponent must 
 be raised in 
order to get 1000?” We know 
Therefore, 
 TRY IT 
#5 
Evaluate 
HOW TO 
Given a common logarithm with the form 
 evaluate it using a calculator. 
1. Press [LOG]. 
2. Enter the value given for 
 followed by [ ) ]. 
3. Press [ENTER]. 
EXAMPLE 6 
Finding the Value of a Common Logarithm Using a Calculator 
Evaluate 
 to four decimal places using a calculator. 
Solution 
• Press [LOG]. 
• Enter 321, followed by [ ) ]. 
• Press [ENTER]. 
Rounding to four decimal places, 
Analysis 
Note that 
 and that 
 Since 321 is between 100 and 1000, we know that 
 must be between 
 and 
 This gives us the following: 
 TRY IT 
#6 
Evaluate 
 to four decimal places using a calculator. 
4.3 • Logarithmic Functions     435


--- PDF page 40 (book page 446) ---
...
EXAMPLE 7 
Rewriting and Solving a Real-World Exponential Model 
The amount of energy released from one earthquake was 500 times greater than the amount of energy released from 
another. The equation 
 represents this situation, where  is the difference in magnitudes on the Richter Scale. 
To the nearest thousandth, what was the difference in magnitudes? 
Solution 
We begin by rewriting the exponential equation in logarithmic form. 
Next we evaluate the logarithm using a calculator: 
• Press [LOG]. 
• Enter 
 followed by [ ) ]. 
• Press [ENTER]. 
• To the nearest thousandth, 
The difference in magnitudes was about 
 TRY IT 
#7 
The amount of energy released from one earthquake was 
 times greater than the amount of 
energy released from another. The equation 
 represents this situation, where  is the 
difference in magnitudes on the Richter Scale. To the nearest thousandth, what was the difference 
in magnitudes? 
Using Natural Logarithms 
The most frequently used base for logarithms is 
 the value of which is approximately 
. Base  logarithms are 
important in calculus and some scientific applications; they are called natural logarithms. The base  logarithm, 
 has its own notation, 
Most values of 
 can be found only using a calculator. The major exception is that, because the logarithm of 1 is 
always 0 in any base, 
 For other natural logarithms, we can use the 
 key that can be found on most scientific 
calculators. We can also find the natural logarithm of any power of  using the inverse property of logarithms. 
Definition of the Natural Logarithm 
A natural logarithm is a logarithm with base 
 We write 
 simply as 
 The natural logarithm of a positive 
number  satisfies the following definition. 
For 
We read 
 as, “the logarithm with base  of ” or “the natural logarithm of 
” 
The logarithm  is the exponent to which  must be raised to get 
Since the functions 
 and 
 are inverse functions, 
 for all  and 
 for 
HOW TO 
Given a natural logarithm with the form 
 evaluate it using a calculator. 
1. Press [LN]. 
2. Enter the value given for 
 followed by [ ) ]. 
436     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 41 (book page 447) ---
3. Press [ENTER]. 
EXAMPLE 8 
Evaluating a Natural Logarithm Using a Calculator 
Evaluate 
 to four decimal places using a calculator. 
Solution 
• Press [LN]. 
• Enter 
 followed by [ ) ]. 
• Press [ENTER]. 
Rounding to four decimal places, 
 TRY IT 
#8 
Evaluate 
 MEDIA 
Access this online resource for additional instruction and practice with logarithms. 
Introduction to Logarithms (https://openstax.org/l/intrologarithms) 
 4.3 SECTION EXERCISES 
Verbal 
1 . What is a base  logarithm? 
Discuss the meaning by 
interpreting each part of the 
equivalent equations 
and 
 for 
 2 . How is the logarithmic 
function 
related to the exponential 
function 
 What is 
the result of composing 
these two functions? 
 3 . How can the logarithmic 
equation 
 be 
solved for  using the 
properties of exponents? 
4 . Discuss the meaning of the 
common logarithm. What is 
its relationship to a 
logarithm with base 
 and 
how does the notation 
differ? 
 5 . Discuss the meaning of the 
natural logarithm. What is 
its relationship to a 
logarithm with base 
 and 
how does the notation 
differ? 
Algebraic 
For the following exercises, rewrite each equation in exponential form. 
6 . 
 7 . 
 8 . 
9 . 
 10 . 
 11 . 
12 . 
 13 . 
 14 . 
15 . 
For the following exercises, rewrite each equation in logarithmic form. 
16 . 
 17 . 
 18 . 
19 . 
 20 . 
 21 . 
4.3 • Logarithmic Functions     437


--- PDF page 42 (book page 448) ---
22 . 
 23 . 
 24 . 
25 . 
For the following exercises, solve for  by converting the logarithmic equation to exponential form. 
26 . 
 27 . 
 28 . 
29 . 
 30 . 
 31 . 
32 . 
33 . 
 34 . 
35 . 
For the following exercises, use the definition of common and natural logarithms to simplify. 
36 . 
 37 . 
 38 . 
39 . 
 40 . 
 41 . 
Numeric 
For the following exercises, evaluate the base  logarithmic expression without using a calculator. 
42 . 
 43 . 
 44 . 
45 . 
For the following exercises, evaluate the common logarithmic expression without using a calculator. 
46 . 
 47 . 
 48 . 
49 . 
For the following exercises, evaluate the natural logarithmic expression without using a calculator. 
50 . 
 51 . 
 52 . 
53 . 
Technology 
For the following exercises, evaluate each expression using a calculator. Round to the nearest thousandth. 
54 . 
 55 . 
 56 . 
57 . 
 58 . 
Extensions 
59 . Is 
 in the domain of 
the function 
 If so, what 
is the value of the function 
when 
 Verify the 
result. 
 60 . Is 
 in the range of 
the function 
 If so, for 
what value of 
 Verify the 
result. 
 61 . Is there a number  such 
that 
 If so, what is 
that number? Verify the 
result. 
62 . Is the following true: 
 Verify the 
result. 
 63 . Is the following true: 
 Verify 
the result. 
438     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 43 (book page 449) ---
Real-World Applications 
64 . The exposure index 
 for 
a camera is a 
measurement of the 
amount of light that hits 
the image receptor. It is 
determined by the 
equation 
 where 
 is the “f-stop” setting on 
the camera, and  is the 
exposure time in seconds. 
Suppose the f-stop setting 
is  and the desired 
exposure time is 
seconds. What will the 
resulting exposure index 
be? 
 65 . Refer to the previous 
exercise. Suppose the light 
meter on a camera 
indicates an 
 of 
 and 
the desired exposure time 
is 16 seconds. What should 
the f-stop setting be? 
 66 . The intensity levels I of two 
earthquakes measured on 
a seismograph can be 
compared by the formula 
 where 
 is the magnitude given 
by the Richter Scale. In 
August 2009, an 
earthquake of magnitude 
6.1 hit Honshu, Japan. In 
March 2011, that same 
region experienced yet 
another, more devastating 
earthquake, this time with 
a magnitude of 9.0.8  How 
many times greater was 
the intensity of the 2011 
earthquake? Round to the 
nearest whole number. 
4.4 Graphs of Logarithmic Functions 
Learning Objectives 
In this section, you will: 
Identify the domain of a logarithmic function. 
Graph logarithmic functions. 
In Graphs of Exponential Functions, we saw how creating a graphical representation of an exponential model gives us 
another layer of insight for predicting future events. How do logarithmic graphs give us insight into situations? Because 
every logarithmic function is the inverse function of an exponential function, we can think of every output on a 
logarithmic graph as the input for the corresponding inverse exponential equation. In other words, logarithms give the 
cause for an effect. 
To illustrate, suppose we invest 
 in an account that offers an annual interest rate of 
 compounded continuously. 
We already know that the balance in our account for any year  can be found with the equation 
But what if we wanted to know the year for any balance? We would need to create a corresponding new function by 
interchanging the input and the output; thus we would need to create a logarithmic model for this situation. By graphing 
the model, we can see the output (year) for any input (account balance). For instance, what if we wanted to know how 
many years it would take for our initial investment to double? Figure 1 shows this point on the logarithmic graph. 
8 http://earthquake.usgs.gov/earthquakes/world/historical.php. Accessed 3/4/2014. 
4.4 • Graphs of Logarithmic Functions     439


--- PDF page 44 (book page 450) ---
...
Figure 1 
In this section we will discuss the values for which a logarithmic function is defined, and then turn our attention to 
graphing the family of logarithmic functions. 
Finding the Domain of a Logarithmic Function 
Before working with graphs, we will take a look at the domain (the set of input values) for which the logarithmic function 
is defined. 
Recall that the exponential function is defined as 
 for any real number  and constant 
 
 where 
• The domain of  is 
∞∞
• The range of  is 
∞
In the last section we learned that the logarithmic function 
 is the inverse of the exponential function 
So, as inverse functions: 
• The domain of 
 is the range of 
 
∞
• The range of 
 is the domain of 
 
∞∞
Transformations of the parent function 
 behave similarly to those of other functions. Just as with other 
parent functions, we can apply the four types of transformations—shifts, stretches, compressions, and reflections. 
In Graphs of Exponential Functions we saw that certain transformations can change the range of 
 Similarly, 
applying transformations to the parent function 
 can change the domain. When finding the domain of a 
logarithmic function, therefore, it is important to remember that the domain consists only of positive real numbers. That 
is, the argument of the logarithmic function must be greater than zero. 
For example, consider 
 This function is defined for any values of  such that the argument, in this 
case 
 is greater than zero. To find the domain, we set up an inequality and solve for 
In interval notation, the domain of 
 is 
∞
HOW TO 
Given a logarithmic function, identify the domain. 
1. Set up an inequality showing the argument greater than zero. 
440     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 45 (book page 451) ---
2. Solve for 
3. Write the domain in interval notation. 
EXAMPLE 1 
Identifying the Domain of a Logarithmic Shift 
What is the domain of 
Solution 
The logarithmic function is defined only when the input is positive, so this function is defined when 
 Solving 
this inequality, 
The domain of 
 is 
∞
 TRY IT 
#1 
What is the domain of 
EXAMPLE 2 
Identifying the Domain of a Logarithmic Shift and Reflection 
What is the domain of 
Solution 
The logarithmic function is defined only when the input is positive, so this function is defined when 
 Solving 
this inequality, 
The domain of 
 is 
∞
 TRY IT 
#2 
What is the domain of 
Graphing Logarithmic Functions 
Now that we have a feel for the set of values for which a logarithmic function is defined, we move on to graphing 
logarithmic functions. The family of logarithmic functions includes the parent function 
 along with all its 
transformations: shifts, stretches, compressions, and reflections. 
We begin with the parent function 
 Because every logarithmic function of this form is the inverse of an 
exponential function with the form 
 their graphs will be reflections of each other across the line 
 To 
illustrate this, we can observe the relationship between the input and output values of 
 and its equivalent 
 in Table 1. 
4.4 • Graphs of Logarithmic Functions     441


--- PDF page 46 (book page 452) ---
Table 1 
Using the inputs and outputs from Table 1, we can build another table to observe the relationship between points on the 
graphs of the inverse functions 
 and 
 See Table 2. 
Table 2 
As we’d expect, the x- and y-coordinates are reversed for the inverse functions. Figure 2 shows the graph of  and 
Figure 2 Notice that the graphs of 
 and 
 are reflections about the line 
Observe the following from the graph: 
• 
 has a y-intercept at 
 and 
 has an x- intercept at 
• The domain of 
 
∞∞
 is the same as the range of 
• The range of 
 
∞
 is the same as the domain of 
Characteristics of the Graph of the Parent Function, 
For any real number  and constant 
 
 we can see the following characteristics in the graph of 
• one-to-one function 
• vertical asymptote: 
• domain: 
∞
• range: 
∞∞
442     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 47 (book page 453) ---
...
• x-intercept: 
 and key point 
• y-intercept: none 
• increasing if 
• decreasing if 
See Figure 3. 
Figure 3 
Figure 4 shows how changing the base  in 
 can affect the graphs. Observe that the graphs compress 
vertically as the value of the base increases. (Note: recall that the function 
 has base 
Figure 4 The graphs of three logarithmic functions with different bases, all greater than 1. 
HOW TO 
Given a logarithmic function with the form 
 graph the function. 
1. Draw and label the vertical asymptote, 
2. Plot the x-intercept, 
3. Plot the key point 
4. Draw a smooth curve through the points. 
5. State the domain, 
∞
 the range, 
∞∞
 and the vertical asymptote, 
4.4 • Graphs of Logarithmic Functions     443


--- PDF page 48 (book page 454) ---
EXAMPLE 3 
Graphing a Logarithmic Function with the Form f(x) = logb(x). 
Graph 
 State the domain, range, and asymptote. 
Solution 
Before graphing, identify the behavior and key points for the graph. 
• Since 
 is greater than one, we know the function is increasing. The left tail of the graph will approach the 
vertical asymptote 
 and the right tail will increase slowly without bound. 
• The x-intercept is 
• The key point 
 is on the graph. 
• We draw and label the asymptote, plot and label the points, and draw a smooth curve through the points (see 
Figure 5). 
Figure 5 
The domain is 
∞
 the range is 
∞∞
 and the vertical asymptote is 
 TRY IT 
#3 
Graph 
 State the domain, range, and asymptote. 
Graphing Transformations of Logarithmic Functions 
As we mentioned in the beginning of the section, transformations of logarithmic graphs behave similarly to those of 
other parent functions. We can shift, stretch, compress, and reflect the parent function 
 without loss of 
shape. 
Graphing a Horizontal Shift of f(x) = logb(x) 
When a constant  is added to the input of the parent function 
 the result is a horizontal shift  units in 
the opposite direction of the sign on  To visualize horizontal shifts, we can observe the general graph of the parent 
function 
 and for 
 alongside the shift left, 
 and the shift right, 
 See Figure 6. 
444     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 49 (book page 455) ---
...
Figure 6 
Horizontal Shifts of the Parent Function 
For any constant  the function 
• shifts the parent function 
 left  units if 
• shifts the parent function 
 right  units if 
• has the vertical asymptote 
• has domain 
∞
• has range 
∞∞
HOW TO 
Given a logarithmic function with the form 
 graph the translation. 
1. Identify the horizontal shift: 
a. If 
 shift the graph of 
 left  units. 
b. If 
 shift the graph of 
 right  units. 
2. Draw the vertical asymptote 
3. Identify three key points from the parent function. Find new coordinates for the shifted functions by subtracting 
from the  coordinate. 
4. Label the three points. 
5. The Domain is 
∞
 the range is 
∞∞
 and the vertical asymptote is 
4.4 • Graphs of Logarithmic Functions     445


--- PDF page 50 (book page 456) ---
EXAMPLE 4 
Graphing a Horizontal Shift of the Parent Function y = logb(x) 
Sketch the horizontal shift 
 alongside its parent function. Include the key points and asymptotes on 
the graph. State the domain, range, and asymptote. 
Solution 
Since the function is 
 we notice 
Thus 
 so 
 This means we will shift the function 
 right 2 units. 
The vertical asymptote is 
 or 
Consider the three key points from the parent function, 
 
 and 
The new coordinates are found by adding 2 to the  coordinates. 
Label the points 
 
 and 
The domain is 
∞
 the range is 
∞∞
 and the vertical asymptote is 
Figure 7 
 TRY IT 
#4 
Sketch a graph of 
 alongside its parent function. Include the key points and 
asymptotes on the graph. State the domain, range, and asymptote. 
Graphing a Vertical Shift of y = logb(x) 
When a constant  is added to the parent function 
 the result is a vertical shift  units in the direction of 
the sign on 
 To visualize vertical shifts, we can observe the general graph of the parent function 
alongside the shift up, 
 and the shift down, 
 See Figure 8. 
446     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 51 (book page 457) ---
...
Figure 8 
Vertical Shifts of the Parent Function 
For any constant 
 the function 
• shifts the parent function 
 up  units if 
• shifts the parent function 
 down  units if 
• has the vertical asymptote 
• has domain 
∞
• has range 
∞∞
HOW TO 
Given a logarithmic function with the form 
 graph the translation. 
1. Identify the vertical shift: 
◦ If 
 shift the graph of 
 up  units. 
◦ If 
 shift the graph of 
 down  units. 
2. Draw the vertical asymptote 
3. Identify three key points from the parent function. Find new coordinates for the shifted functions by adding  to 
the  coordinate. 
4.4 • Graphs of Logarithmic Functions     447


--- PDF page 52 (book page 458) ---
4. Label the three points. 
5. The domain is 
∞
 the range is 
∞∞
 and the vertical asymptote is 
EXAMPLE 5 
Graphing a Vertical Shift of the Parent Function y = logb(x) 
Sketch a graph of 
 alongside its parent function. Include the key points and asymptote on the graph. 
State the domain, range, and asymptote. 
Solution 
Since the function is 
 we will notice 
 Thus 
This means we will shift the function 
 down 2 units. 
The vertical asymptote is 
Consider the three key points from the parent function, 
 
 and 
The new coordinates are found by subtracting 2 from the y coordinates. 
Label the points 
 
 and 
The domain is 
∞
 the range is 
∞∞
 and the vertical asymptote is 
Figure 9 
The domain is 
∞
 the range is 
∞∞
 and the vertical asymptote is 
 TRY IT 
#5 
Sketch a graph of 
 alongside its parent function. Include the key points and 
asymptote on the graph. State the domain, range, and asymptote. 
Graphing Stretches and Compressions of y = logb(x) 
When the parent function 
 is multiplied by a constant 
 the result is a vertical stretch or compression 
of the original graph. To visualize stretches and compressions, we set 
 and observe the general graph of the parent 
448     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 53 (book page 459) ---
...
function 
 alongside the vertical stretch, 
 and the vertical compression, 
See Figure 10. 
Figure 10 
Vertical Stretches and Compressions of the Parent Function 
For any constant 
 the function 
• stretches the parent function 
 vertically by a factor of  if 
• compresses the parent function 
 vertically by a factor of  if 
• has the vertical asymptote 
• has the x-intercept 
• has domain 
∞
• has range 
∞∞
HOW TO 
Given a logarithmic function with the form 
 
 graph the translation. 
1. Identify the vertical stretch or compressions: 
◦ If 
 the graph of 
 is stretched by a factor of  units. 
◦ If 
 the graph of 
 is compressed by a factor of  units. 
4.4 • Graphs of Logarithmic Functions     449


--- PDF page 54 (book page 460) ---
2. Draw the vertical asymptote 
3. Identify three key points from the parent function. Find new coordinates for the shifted functions by multiplying 
the  coordinates by 
4. Label the three points. 
5. The domain is 
∞
 the range is 
∞∞
 and the vertical asymptote is 
EXAMPLE 6 
Graphing a Stretch or Compression of the Parent Function y = logb(x) 
Sketch a graph of 
 alongside its parent function. Include the key points and asymptote on the graph. 
State the domain, range, and asymptote. 
Solution 
Since the function is 
 we will notice 
This means we will stretch the function 
 by a factor of 2. 
The vertical asymptote is 
Consider the three key points from the parent function, 
 
 and 
The new coordinates are found by multiplying the  coordinates by 2. 
Label the points 
 
 and 
The domain is 
∞
 the range is 
∞∞
 and the vertical asymptote is 
 See Figure 11. 
Figure 11 
The domain is 
∞
 the range is 
∞∞
 and the vertical asymptote is 
 TRY IT 
#6 
Sketch a graph of 
 alongside its parent function. Include the key points and 
asymptote on the graph. State the domain, range, and asymptote. 
EXAMPLE 7 
Combining a Shift and a Stretch 
Sketch a graph of 
 State the domain, range, and asymptote. 
450     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 55 (book page 461) ---
Solution 
Remember: what happens inside parentheses happens first. First, we move the graph left 2 units, then stretch the 
function vertically by a factor of 5, as in Figure 12. The vertical asymptote will be shifted to 
 The x-intercept will be 
 The domain will be 
∞
 Two points will help give the shape of the graph: 
 and 
 We chose 
 as the x-coordinate of one point to graph because when 
 
 the base of the common logarithm. 
Figure 12 
The domain is 
∞
 the range is 
∞∞
 and the vertical asymptote is 
 TRY IT 
#7 
Sketch a graph of the function 
 State the domain, range, and asymptote. 
Graphing Reflections of f(x) = logb(x) 
When the parent function 
 is multiplied by 
 the result is a reflection about the x-axis. When the input is 
multiplied by 
 the result is a reflection about the y-axis. To visualize reflections, we restrict 
 and observe the 
general graph of the parent function 
 alongside the reflection about the x-axis, 
 and the 
reflection about the y-axis, 
4.4 • Graphs of Logarithmic Functions     451


--- PDF page 56 (book page 462) ---
...
Figure 13 
Reflections of the Parent Function 
The function 
• reflects the parent function 
 about the x-axis. 
• has domain, 
∞
 range, 
∞∞
 and vertical asymptote, 
 which are unchanged from the parent 
function. 
The function 
• reflects the parent function 
 about the y-axis. 
• has domain 
∞
• has range, 
∞∞
 and vertical asymptote, 
 which are unchanged from the parent function. 
HOW TO 
Given a logarithmic function with the parent function 
 graph a translation. 
452     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 57 (book page 463) ---
1. Draw the vertical asymptote, 
1. Draw the vertical asymptote, 
2. Plot the x-intercept, 
2. Plot the x-intercept, 
3. Reflect the graph of the parent function 
 about the x-axis. 
3. Reflect the graph of the parent function 
 about the y-axis. 
4. Draw a smooth curve through the points. 
4. Draw a smooth curve through the points. 
5. State the domain, (0, ∞), the range, (−∞, ∞), and the 
vertical asymptote 
. 
5. State the domain, (−∞, 0) the range, (−∞, ∞) and the 
vertical asymptote 
Table 3 
EXAMPLE 8 
Graphing a Reflection of a Logarithmic Function 
Sketch a graph of 
 alongside its parent function. Include the key points and asymptote on the graph. 
State the domain, range, and asymptote. 
Solution 
Before graphing 
 identify the behavior and key points for the graph. 
• Since 
 is greater than one, we know that the parent function is increasing. Since the input value is multiplied 
by 
  is a reflection of the parent graph about the y-axis. Thus, 
 will be decreasing as  moves 
from negative infinity to zero, and the right tail of the graph will approach the vertical asymptote 
• The x-intercept is 
• We draw and label the asymptote, plot and label the points, and draw a smooth curve through the points. 
Figure 14 
The domain is 
∞
 the range is 
∞∞
 and the vertical asymptote is 
 TRY IT 
#8 
Graph 
 State the domain, range, and asymptote. 
4.4 • Graphs of Logarithmic Functions     453


--- PDF page 58 (book page 464) ---
...
HOW TO 
Given a logarithmic equation, use a graphing calculator to approximate solutions. 
1. Press [Y=]. Enter the given logarithm equation or equations as Y1= and, if needed, Y2=. 
2. Press [GRAPH] to observe the graphs of the curves and use [WINDOW] to find an appropriate view of the graphs, 
including their point(s) of intersection. 
3. To find the value of 
 we compute the point of intersection. Press [2ND] then [CALC]. Select “intersect” and press 
[ENTER] three times. The point of intersection gives the value of 
 for the point(s) of intersection. 
EXAMPLE 9 
Approximating the Solution of a Logarithmic Equation 
Solve 
 graphically. Round to the nearest thousandth. 
Solution 
Press [Y=] and enter 
 next to Y1=. Then enter 
 next to Y2=. For a window, use the values 0 to 5 for 
 and –10 to 10 for 
 Press [GRAPH]. The graphs should intersect somewhere a little to right of 
For a better approximation, press [2ND] then [CALC]. Select [5: intersect] and press [ENTER] three times. The 
x-coordinate of the point of intersection is displayed as 1.3385297. (Your answer may be different if you use a different 
window or use a different value for Guess?) So, to the nearest thousandth, 
 TRY IT 
#9 
Solve 
 graphically. Round to the nearest thousandth. 
Summarizing Translations of the Logarithmic Function 
Now that we have worked with each type of translation for the logarithmic function, we can summarize each in Table 4 to 
arrive at the general equation for translating exponential functions. 
Transformations of the Parent Function 
Transformation 
Form 
Shift 
• Horizontally  units to the left 
• Vertically  units up 
Stretch and Compress 
• Stretch if 
• Compression if 
Reflect about the x-axis 
Reflect about the y-axis 
General equation for all translations 
Table 4 
454     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 59 (book page 465) ---
Transformations of Logarithmic Functions 
All transformations of the parent logarithmic function, 
 have the form 
where the parent function, 
 is 
• shifted vertically up  units. 
• shifted horizontally to the left  units. 
• stretched vertically by a factor of 
 if 
• compressed vertically by a factor of 
 if 
• reflected about the x-axis when 
For 
 the graph of the parent function is reflected about the y-axis. 
EXAMPLE 10 
Finding the Vertical Asymptote of a Logarithm Graph 
What is the vertical asymptote of 
Solution 
The vertical asymptote is at 
Analysis 
The coefficient, the base, and the upward translation do not affect the asymptote. The shift of the curve 4 units to the left 
shifts the vertical asymptote to 
 TRY IT 
#10 
What is the vertical asymptote of 
EXAMPLE 11 
Finding the Equation from a Graph 
Find a possible equation for the common logarithmic function graphed in Figure 15. 
Figure 15 
Solution 
This graph has a vertical asymptote at 
 and has been vertically reflected. We do not know yet the vertical shift or 
the vertical stretch. We know so far that the equation will have form: 
4.4 • Graphs of Logarithmic Functions     455


--- PDF page 60 (book page 466) ---
It appears the graph passes through the points 
 and 
 Substituting 
Next, substituting in 
 , 
This gives us the equation 
Analysis 
We can verify this answer by comparing the function values in Table 5 with the points on the graph in Figure 15. 
−1 
0 
1 
2 
3 
1 
0 
−0.58496 
−1 
−1.3219 
4 
5 
6 
7 
8 
−1.5850 
−1.8074 
−2 
−2.1699 
−2.3219 
Table 5 
 TRY IT 
#11 
Give the equation of the natural logarithm graphed in Figure 16. 
Figure 16 
 Q&A 
Is it possible to tell the domain and range and describe the end behavior of a function just by 
looking at the graph? 
Yes, if we know the function is a general logarithmic function. For example, look at the graph in Figure 
16. The graph approaches 
 (or thereabouts) more and more closely, so 
 is, or is very 
close to, the vertical asymptote. It approaches from the right, so the domain is all points to the right, 
456     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 61 (book page 467) ---
 The range, as with all general logarithmic functions, is all real numbers. And we can see 
the end behavior because the graph goes down as it goes left and up as it goes right. The end behavior 
is that as 
∞ and as 
∞
∞
 MEDIA 
Access these online resources for additional instruction and practice with graphing logarithms. 
Graph an Exponential Function and Logarithmic Function (https://openstax.org/l/graphexplog) 
Match Graphs with Exponential and Logarithmic Functions (https://openstax.org/l/matchexplog) 
Find the Domain of Logarithmic Functions (https://openstax.org/l/domainlog) 
 4.4 SECTION EXERCISES 
Verbal 
1 . The inverse of every 
logarithmic function is an 
exponential function and 
vice-versa. What does this 
tell us about the relationship 
between the coordinates of 
the points on the graphs of 
each? 
 2 . What type(s) of 
translation(s), if any, affect 
the range of a logarithmic 
function? 
 3 . What type(s) of 
translation(s), if any, affect 
the domain of a logarithmic 
function? 
4 . Consider the general 
logarithmic function 
 Why can’t 
be zero? 
 5 . Does the graph of a general 
logarithmic function have a 
horizontal asymptote? 
Explain. 
Algebraic 
For the following exercises, state the domain and range of the function. 
6 . 
 7 . 
 8 . 
9 . 
 10 . 
For the following exercises, state the domain and the vertical asymptote of the function. 
11 . 
 12 . 
 13 . 
14 . 
 15 . 
For the following exercises, state the domain, vertical asymptote, and end behavior of the function. 
16 . 
 17 . 
 18 . 
19 . 
 20 . 
For the following exercises, state the domain, range, and x- and y-intercepts, if they exist. If they do not exist, write DNE. 
21 . 
 22 . 
 23 . 
24 . 
 25 . 
4.4 • Graphs of Logarithmic Functions     457


--- PDF page 62 (book page 468) ---
Graphical 
For the following exercises, match each function in Figure 17 with the letter corresponding to its graph. 
Figure 17 
26 . 
 27 . 
 28 . 
29 . 
 30 . 
For the following exercises, match each function in Figure 18 with the letter corresponding to its graph. 
Figure 18 
31 . 
 32 . 
 33 . 
For the following exercises, sketch the graphs of each pair of functions on the same axis. 
34 . 
 and 
 35 . 
 and 
36 . 
 and 
37 . 
 and 
458     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 63 (book page 469) ---
For the following exercises, match each function in Figure 19 with the letter corresponding to its graph. 
Figure 19 
38 . 
 39 . 
 40 . 
For the following exercises, sketch the graph of the indicated function. 
41 . 
42 . 
 43 . 
44 . 
 45 . 
46 . 
For the following exercises, write a logarithmic equation corresponding to the graph shown. 
47 . Use 
 as the parent 
function. 
48 . Use 
 as the parent 
function. 
49 . Use 
 as the parent 
function. 
4.4 • Graphs of Logarithmic Functions     459


--- PDF page 64 (book page 470) ---
50 . Use 
 as the parent 
function. 
Technology 
For the following exercises, use a graphing calculator to find approximate solutions to each equation. 
51 . 
 52 . 
53 . 
 54 . 
 55 . 
Extensions 
56 . Let  be any positive real 
number such that 
What must 
 be equal 
to? Verify the result. 
 57 . Explore and discuss the 
graphs of 
and 
Make a conjecture based 
on the result. 
 58 . Prove the conjecture made 
in the previous exercise. 
59 . What is the domain of the 
function 
Discuss the result. 
60 . Use properties of 
exponents to find the 
x-intercepts of the function 
algebraically. Show the 
steps for solving, and then 
verify the result by 
graphing the function. 
4.5 Logarithmic Properties 
Learning Objectives 
In this section, you will: 
Use the product rule for logarithms. 
Use the quotient rule for logarithms. 
Use the power rule for logarithms. 
Expand logarithmic expressions. 
Condense logarithmic expressions. 
Use the change-of-base formula for logarithms. 
460     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 65 (book page 471) ---
Figure 1 The pH of hydrochloric acid is tested with litmus paper. (credit: David Berardan) 
In chemistry, pH is used as a measure of the acidity or alkalinity of a substance. The pH scale runs from 0 to 14. 
Substances with a pH less than 7 are considered acidic, and substances with a pH greater than 7 are said to be basic. Our 
bodies, for instance, must maintain a pH close to 7.35 in order for enzymes to work properly. To get a feel for what is 
acidic and what is basic, consider the following pH levels of some common substances: 
• Battery acid: 0.8 
• Stomach acid: 2.7 
• Orange juice: 3.3 
• Pure water: 7 (at 25° C) 
• Human blood: 7.35 
• Fresh coconut: 7.8 
• Sodium hydroxide (lye): 14 
To determine whether a solution is acidic or basic, we find its pH, which is a measure of the number of active positive 
hydrogen ions in the solution. The pH is defined by the following formula, where 
 is the concentration of hydrogen 
ion in the solution 
The equivalence of 
 and 
 is one of the logarithm properties we will examine in this section. 
Using the Product Rule for Logarithms 
Recall that the logarithmic and exponential functions “undo” each other. This means that logarithms have similar 
properties to exponents. Some important properties of logarithms are given here. First, the following properties are easy 
to prove. 
For example, 
 since 
 And 
 since 
Next, we have the inverse property. 
For example, to evaluate 
 we can rewrite the logarithm as 
 and then apply the inverse property 
 to get 
To evaluate 
 we can rewrite the logarithm as 
 and then apply the inverse property 
 to get 
Finally, we have the one-to-one property. 
4.5 • Logarithmic Properties     461


--- PDF page 66 (book page 472) ---
...
We can use the one-to-one property to solve the equation 
 for 
 Since the bases are the same, 
we can apply the one-to-one property by setting the arguments equal and solving for 
But what about the equation 
 The one-to-one property does not help us in this instance. 
Before we can solve an equation like this, we need a method for combining terms on the left side of the equation. 
Recall that we use the product rule of exponents to combine the product of powers by adding exponents: 
We have a similar property for logarithms, called the product rule for logarithms, which says that the logarithm of a 
product is equal to a sum of logarithms. Because logs are exponents, and we multiply like bases, we can add the 
exponents. We will use the inverse property to derive the product rule below. 
Given any real number  and positive real numbers 
 and 
 where 
 we will show 
Let 
 and 
 In exponential form, these equations are 
 and 
 It follows that 
Note that repeated applications of the product rule for logarithms allow us to simplify the logarithm of the product of 
any number of factors. For example, consider 
 Using the product rule for logarithms, we can rewrite this 
logarithm of a product as the sum of logarithms of its factors: 
The Product Rule for Logarithms 
The product rule for logarithms can be used to simplify a logarithm of a product by rewriting it as a sum of 
individual logarithms. 
HOW TO 
Given the logarithm of a product, use the product rule of logarithms to write an equivalent sum of logarithms. 
1. Factor the argument completely, expressing each whole number factor as a product of primes. 
2. Write the equivalent expression by summing the logarithms of each factor. 
EXAMPLE 1 
Using the Product Rule for Logarithms 
Expand 
Solution 
We begin by factoring the argument completely, expressing 
 as a product of primes. 
Next we write the equivalent equation by summing the logarithms of each factor. 
462     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 67 (book page 473) ---
...
 TRY IT 
#1 
Expand 
Using the Quotient Rule for Logarithms 
For quotients, we have a similar rule for logarithms. Recall that we use the quotient rule of exponents to combine the 
quotient of exponents by subtracting: 
 The quotient rule for logarithms says that the logarithm of a 
quotient is equal to a difference of logarithms. Just as with the product rule, we can use the inverse property to derive 
the quotient rule. 
Given any real number  and positive real numbers 
 
 and 
 where 
 we will show 
Let 
 and 
 In exponential form, these equations are 
 and 
 It follows that 
For example, to expand 
 we must first express the quotient in lowest terms. Factoring and canceling we 
get, 
Next we apply the quotient rule by subtracting the logarithm of the denominator from the logarithm of the numerator. 
Then we apply the product rule. 
The Quotient Rule for Logarithms 
The quotient rule for logarithms can be used to simplify a logarithm or a quotient by rewriting it as the difference of 
individual logarithms. 
HOW TO 
Given the logarithm of a quotient, use the quotient rule of logarithms to write an equivalent difference of 
logarithms. 
1. Express the argument in lowest terms by factoring the numerator and denominator and canceling common 
terms. 
2. Write the equivalent expression by subtracting the logarithm of the denominator from the logarithm of the 
numerator. 
3. Check to see that each term is fully expanded. If not, apply the product rule for logarithms to expand completely. 
4.5 • Logarithmic Properties     463


--- PDF page 68 (book page 474) ---
...
EXAMPLE 2 
Using the Quotient Rule for Logarithms 
Expand 
Solution 
First we note that the quotient is factored and in lowest terms, so we apply the quotient rule. 
Notice that the resulting terms are logarithms of products. To expand completely, we apply the product rule, noting that 
the prime factors of the factor 15 are 3 and 5. 
Analysis 
There are exceptions to consider in this and later examples. First, because denominators must never be zero, this 
expression is not defined for 
 and 
 Also, since the argument of a logarithm must be positive, we note as we 
observe the expanded logarithm, that 
 
 
 and 
 Combining these conditions is beyond the 
scope of this section, and we will not consider them here or in subsequent exercises. 
 TRY IT 
#2 
Expand 
Using the Power Rule for Logarithms 
We’ve explored the product rule and the quotient rule, but how can we take the logarithm of a power, such as 
 One 
method is as follows: 
Notice that we used the product rule for logarithms to find a solution for the example above. By doing so, we have 
derived the power rule for logarithms, which says that the log of a power is equal to the exponent times the log of the 
base. Keep in mind that, although the input to a logarithm may not be written as a power, we may be able to change it to 
a power. For example, 
The Power Rule for Logarithms 
The power rule for logarithms can be used to simplify the logarithm of a power by rewriting it as the product of the 
exponent times the logarithm of the base. 
HOW TO 
Given the logarithm of a power, use the power rule of logarithms to write an equivalent product of a factor 
and a logarithm. 
1. Express the argument as a power, if needed. 
464     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 69 (book page 475) ---
2. Write the equivalent expression by multiplying the exponent times the logarithm of the base. 
EXAMPLE 3 
Expanding a Logarithm with Powers 
Expand 
Solution 
The argument is already written as a power, so we identify the exponent, 5, and the base, 
 and rewrite the equivalent 
expression by multiplying the exponent times the logarithm of the base. 
 TRY IT 
#3 
Expand 
EXAMPLE 4 
Rewriting an Expression as a Power before Using the Power Rule 
Expand 
 using the power rule for logs. 
Solution 
Expressing the argument as a power, we get 
Next we identify the exponent, 2, and the base, 5, and rewrite the equivalent expression by multiplying the exponent 
times the logarithm of the base. 
 TRY IT 
#4 
Expand 
EXAMPLE 5 
Using the Power Rule in Reverse 
Rewrite 
 using the power rule for logs to a single logarithm with a leading coefficient of 1. 
Solution 
Because the logarithm of a power is the product of the exponent times the logarithm of the base, it follows that the 
product of a number and a logarithm can be written as a power. For the expression 
 we identify the factor, 4, as 
the exponent and the argument, 
 as the base, and rewrite the product as a logarithm of a power: 
 TRY IT 
#5 
Rewrite 
 using the power rule for logs to a single logarithm with a leading coefficient of 1. 
Expanding Logarithmic Expressions 
Taken together, the product rule, quotient rule, and power rule are often called “laws of logs.” Sometimes we apply more 
than one rule in order to simplify an expression. For example: 
We can use the power rule to expand logarithmic expressions involving negative and fractional exponents. Here is an 
alternate proof of the quotient rule for logarithms using the fact that a reciprocal is a negative power: 
4.5 • Logarithmic Properties     465


--- PDF page 70 (book page 476) ---
We can also apply the product rule to express a sum or difference of logarithms as the logarithm of a product. 
With practice, we can look at a logarithmic expression and expand it mentally, writing the final answer. Remember, 
however, that we can only do this with products, quotients, powers, and roots—never with addition or subtraction inside 
the argument of the logarithm. 
EXAMPLE 6 
Expanding Logarithms Using Product, Quotient, and Power Rules 
Rewrite 
 as a sum or difference of logs. 
Solution 
First, because we have a quotient of two expressions, we can use the quotient rule: 
Then seeing the product in the first term, we use the product rule: 
Finally, we use the power rule on the first term: 
 TRY IT 
#6 
Expand 
EXAMPLE 7 
Using the Power Rule for Logarithms to Simplify the Logarithm of a Radical Expression 
Expand 
Solution 
 TRY IT 
#7 
Expand 
 Q&A 
Can we expand 
No. There is no way to expand the logarithm of a sum or difference inside the argument of the 
logarithm. 
466     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 71 (book page 477) ---
...
EXAMPLE 8 
Expanding Complex Logarithmic Expressions 
Expand 
Solution 
We can expand by applying the Product and Quotient Rules. 
 TRY IT 
#8 
Expand 
Condensing Logarithmic Expressions 
We can use the rules of logarithms we just learned to condense sums, differences, and products with the same base as a 
single logarithm. It is important to remember that the logarithms must have the same base to be combined. We will 
learn later how to change the base of any logarithm before condensing. 
HOW TO 
Given a sum, difference, or product of logarithms with the same base, write an equivalent expression as a 
single logarithm. 
1. Apply the power property first. Identify terms that are products of factors and a logarithm, and rewrite each as 
the logarithm of a power. 
2. Next apply the product property. Rewrite sums of logarithms as the logarithm of a product. 
3. Apply the quotient property last. Rewrite differences of logarithms as the logarithm of a quotient. 
EXAMPLE 9 
Using the Product and Quotient Rules to Combine Logarithms 
Write 
 as a single logarithm. 
Solution 
Using the product and quotient rules 
This reduces our original expression to 
Then, using the quotient rule 
 TRY IT 
#9 
Condense 
4.5 • Logarithmic Properties     467


--- PDF page 72 (book page 478) ---
EXAMPLE 10 
Condensing Complex Logarithmic Expressions 
Condense 
Solution 
We apply the power rule first: 
Next we apply the product rule to the sum: 
Finally, we apply the quotient rule to the difference: 
 TRY IT 
#10 
Rewrite 
 as a single logarithm. 
EXAMPLE 11 
Rewriting as a Single Logarithm 
Rewrite 
 as a single logarithm. 
Solution 
We apply the power rule first: 
Next we rearrange and apply the product rule to the sum: 
Finally, we apply the quotient rule to the difference: 
 TRY IT 
#11 
Condense 
EXAMPLE 12 
Applying of the Laws of Logs 
Recall that, in chemistry, 
 If the concentration of hydrogen ions in a liquid is doubled, what is the effect 
on pH? 
Solution 
Suppose 
 is the original concentration of hydrogen ions, and 
 is the original pH of the liquid. Then 
 If the 
concentration is doubled, the new concentration is 
 Then the pH of the new liquid is 
468     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 73 (book page 479) ---
Using the product rule of logs 
Since 
 the new pH is 
When the concentration of hydrogen ions is doubled, the pH decreases by about 0.301. 
 TRY IT 
#12 
How does the pH change when the concentration of positive hydrogen ions is decreased by half? 
Using the Change-of-Base Formula for Logarithms 
Most calculators can evaluate only common and natural logs. In order to evaluate logarithms with a base other than 10 
or 
 we use the change-of-base formula to rewrite the logarithm as the quotient of logarithms of any other base; when 
using a calculator, we would change them to common or natural logs. 
To derive the change-of-base formula, we use the one-to-one property and power rule for logarithms. 
Given any positive real numbers 
 and 
 where 
 and 
 we show 
Let 
By exponentiating both sides with base , we arrive at an exponential form, namely 
 It follows 
that 
For example, to evaluate 
 using a calculator, we must first rewrite the expression as a quotient of common or 
natural logs. We will use the common log. 
The Change-of-Base Formula 
The change-of-base formula can be used to evaluate a logarithm with any base. 
For any positive real numbers 
 and 
 where 
 and 
It follows that the change-of-base formula can be used to rewrite a logarithm with any base as the quotient of 
common or natural logs. 
and 
4.5 • Logarithmic Properties     469


--- PDF page 74 (book page 480) ---
...
HOW TO 
Given a logarithm with the form 
 use the change-of-base formula to rewrite it as a quotient of logs with 
any positive base 
 where 
1. Determine the new base 
 remembering that the common log, 
 has base 10, and the natural log, 
has base 
2. Rewrite the log as a quotient using the change-of-base formula 
a. The numerator of the quotient will be a logarithm with base  and argument 
b. The denominator of the quotient will be a logarithm with base  and argument 
EXAMPLE 13 
Changing Logarithmic Expressions to Expressions Involving Only Natural Logs 
Change 
 to a quotient of natural logarithms. 
Solution 
Because we will be expressing 
 as a quotient of natural logarithms, the new base, 
We rewrite the log as a quotient using the change-of-base formula. The numerator of the quotient will be the natural log 
with argument 3. The denominator of the quotient will be the natural log with argument 5. 
 TRY IT 
#13 
Change 
 to a quotient of natural logarithms. 
 Q&A 
Can we change common logarithms to natural logarithms? 
Yes. Remember that 
 means 
 So, 
EXAMPLE 14 
Using the Change-of-Base Formula with a Calculator 
Evaluate 
 using the change-of-base formula with a calculator. 
Solution 
According to the change-of-base formula, we can rewrite the log base 2 as a logarithm of any other base. Since our 
calculators can evaluate the natural log, we might choose to use the natural logarithm, which is the log base 
 TRY IT 
#14 
Evaluate 
 using the change-of-base formula. 
 MEDIA 
Access these online resources for additional instruction and practice with laws of logarithms. 
The Properties of Logarithms (https://openstax.org/l/proplog) 
Expand Logarithmic Expressions (https://openstax.org/l/expandlog) 
Evaluate a Natural Logarithmic Expression (https://openstax.org/l/evaluatelog) 
470     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 75 (book page 481) ---
 4.5 SECTION EXERCISES 
Verbal 
1 . How does the power rule for logarithms help when 
solving logarithms with the form 
 2 . What does the change-of-base formula do? Why is 
it useful when using a calculator? 
Algebraic 
For the following exercises, expand each logarithm as much as possible. Rewrite each expression as a sum, difference, or 
product of logs. 
3 . 
 4 . 
 5 . 
6 . 
 7 . 
 8 . 
For the following exercises, condense to a single logarithm if possible. 
9 . 
 10 . 
11 . 
 12 . 
 13 . 
14 . 
For the following exercises, use the properties of logarithms to expand each logarithm as much as possible. Rewrite each 
expression as a sum, difference, or product of logs. 
15 . 
 16 . 
 17 . 
18 . 
 19 . 
For the following exercises, condense each expression to a single logarithm using the properties of logarithms. 
20 . 
 21 . 
 22 . 
23 . 
 24 . 
For the following exercises, rewrite each expression as an equivalent ratio of logs using the indicated base. 
25 . 
 to base 
 26 . 
 to base 
For the following exercises, suppose 
 and 
 Use the change-of-base formula along with 
properties of logarithms to rewrite each expression in terms of  and 
 Show the steps for solving. 
27 . 
 28 . 
 29 . 
Numeric 
For the following exercises, use properties of logarithms to evaluate without using a calculator. 
30 . 
 31 . 
 32 . 
For the following exercises, use the change-of-base formula to evaluate each expression as a quotient of natural logs. 
Use a calculator to approximate each to five decimal places. 
33 . 
 34 . 
 35 . 
4.5 • Logarithmic Properties     471


--- PDF page 76 (book page 482) ---
36 . 
 37 . 
Extensions 
38 . Use the product rule for logarithms to find all 
values such that 
 Show the steps 
for solving. 
 39 . Use the quotient rule for logarithms to find all 
values such that 
Show the steps for solving. 
40 . Can the power property of 
logarithms be derived from 
the power property of 
exponents using the 
equation 
 If not, 
explain why. If so, show the 
derivation. 
 41 . Prove that 
 for any 
positive integers 
 and 
 42 . Does 
Verify the claim 
algebraically. 
4.6 Exponential and Logarithmic Equations 
Learning Objectives 
In this section, you will: 
Use like bases to solve exponential equations. 
Use logarithms to solve exponential equations. 
Use the definition of a logarithm to solve logarithmic equations. 
Use the one-to-one property of logarithms to solve logarithmic equations. 
Solve applied problems involving exponential and logarithmic equations. 
Figure 1 Wild rabbits in Australia. The rabbit population grew so quickly in Australia that the event became known as the 
“rabbit plague.” (credit: Richard Taylor, Flickr) 
In 1859, an Australian landowner named Thomas Austin released 24 rabbits into the wild for hunting. Because Australia 
had few predators and ample food, the rabbit population exploded. In fewer than ten years, the rabbit population 
numbered in the millions. 
Uncontrolled population growth, as in the wild rabbits in Australia, can be modeled with exponential functions. 
Equations resulting from those exponential functions can be solved to analyze and make predictions about exponential 
growth. In this section, we will learn techniques for solving exponential functions. 
Using Like Bases to Solve Exponential Equations 
The first technique involves two functions with like bases. Recall that the one-to-one property of exponential functions 
tells us that, for any real numbers 
 
 and 
 where 
 
 if and only if 
In other words, when an exponential equation has the same base on each side, the exponents must be equal. This also 
applies when the exponents are algebraic expressions. Therefore, we can solve many exponential equations by using the 
rules of exponents to rewrite each side as a power with the same base. Then, we use the fact that exponential functions 
are one-to-one to set the exponents equal to one another, and solve for the unknown. 
472     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 77 (book page 483) ---
...
For example, consider the equation 
 To solve for 
 we use the division property of exponents to rewrite the 
right side so that both sides have the common base, 
 Then we apply the one-to-one property of exponents by setting 
the exponents equal to one another and solving for : 
Using the One-to-One Property of Exponential Functions to Solve Exponential Equations 
For any algebraic expressions 
 and any positive real number 
HOW TO 
Given an exponential equation with the form 
 where  and  are algebraic expressions with an 
unknown, solve for the unknown. 
1. Use the rules of exponents to simplify, if necessary, so that the resulting equation has the form 
2. Use the one-to-one property to set the exponents equal. 
3. Solve the resulting equation, 
 for the unknown. 
EXAMPLE 1 
Solving an Exponential Equation with a Common Base 
Solve 
Solution 
 TRY IT 
#1 
Solve 
Rewriting Equations So All Powers Have the Same Base 
Sometimes the common base for an exponential equation is not explicitly shown. In these cases, we simply rewrite the 
terms in the equation as powers with a common base, and solve using the one-to-one property. 
For example, consider the equation 
 We can rewrite both sides of this equation as a power of 
 Then we 
apply the rules of exponents, along with the one-to-one property, to solve for 
4.6 • Exponential and Logarithmic Equations     473


--- PDF page 78 (book page 484) ---
...
HOW TO 
Given an exponential equation with unlike bases, use the one-to-one property to solve it. 
1. Rewrite each side in the equation as a power with a common base. 
2. Use the rules of exponents to simplify, if necessary, so that the resulting equation has the form 
3. Use the one-to-one property to set the exponents equal. 
4. Solve the resulting equation, 
 for the unknown. 
EXAMPLE 2 
Solving Equations by Rewriting Them to Have a Common Base 
Solve 
Solution 
 TRY IT 
#2 
Solve 
EXAMPLE 3 
Solving Equations by Rewriting Roots with Fractional Exponents to Have a Common Base 
Solve 
Solution 
 TRY IT 
#3 
Solve 
 Q&A 
Do all exponential equations have a solution? If not, how can we tell if there is a solution during 
the problem-solving process? 
No. Recall that the range of an exponential function is always positive. While solving the equation, we 
may obtain an expression that is undefined. 
474     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 79 (book page 485) ---
...
EXAMPLE 4 
Solving an Equation with Positive and Negative Powers 
Solve 
Solution 
This equation has no solution. There is no real value of  that will make the equation a true statement because any 
power of a positive number is positive. 
Analysis 
Figure 2 shows that the two graphs do not cross so the left side is never equal to the right side. Thus the equation has no 
solution. 
Figure 2 
 TRY IT 
#4 
Solve 
Solving Exponential Equations Using Logarithms 
Sometimes the terms of an exponential equation cannot be rewritten with a common base. In these cases, we solve by 
taking the logarithm of each side. Recall, since 
 is equivalent to 
 we may apply logarithms with the 
same base on both sides of an exponential equation. 
HOW TO 
Given an exponential equation in which a common base cannot be found, solve for the unknown. 
1. Apply the logarithm of both sides of the equation. 
a. If one of the terms in the equation has base 10, use the common logarithm. 
b. If none of the terms in the equation has base 10, use the natural logarithm. 
2. Use the rules of logarithms to solve for the unknown. 
EXAMPLE 5 
Solving an Equation Containing Powers of Different Bases 
Solve 
4.6 • Exponential and Logarithmic Equations     475


--- PDF page 80 (book page 486) ---
...
Solution 
 TRY IT 
#5 
Solve 
 Q&A 
Is there any way to solve 
Yes. The solution is 
Equations Containing e 
One common type of exponential equations are those with base 
 This constant occurs again and again in nature, in 
mathematics, in science, in engineering, and in finance. When we have an equation with a base  on either side, we can 
use the natural logarithm to solve it. 
HOW TO 
Given an equation of the form 
 solve for 
1. Divide both sides of the equation by 
2. Apply the natural logarithm of both sides of the equation. 
3. Divide both sides of the equation by 
EXAMPLE 6 
Solve an Equation of the Form y = Aekt 
Solve 
Solution 
Analysis 
Using laws of logs, we can also write this answer in the form 
 If we want a decimal approximation of the 
answer, we use a calculator. 
 TRY IT 
#6 
Solve 
 Q&A 
Does every equation of the form 
 have a solution? 
476     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 81 (book page 487) ---
No. There is a solution when 
 and when  and 
 are either both 0 or neither 0, and they have the 
same sign. An example of an equation with this form that has no solution is 
EXAMPLE 7 
Solving an Equation That Can Be Simplified to the Form y = Aekt 
Solve 
Solution 
 TRY IT 
#7 
Solve 
Extraneous Solutions 
Sometimes the methods used to solve an equation introduce an extraneous solution, which is a solution that is correct 
algebraically but does not satisfy the conditions of the original equation. One such situation arises in solving when the 
logarithm is taken on both sides of the equation. In such cases, remember that the argument of the logarithm must be 
positive. If the number we are evaluating in a logarithm function is negative, there is no output. 
EXAMPLE 8 
Solving Exponential Functions in Quadratic Form 
Solve 
Solution 
Analysis 
When we plan to use factoring to solve a problem, we always get zero on one side of the equation, because zero has the 
unique property that when a product is zero, one or both of the factors must be zero. We reject the equation 
because a positive number never equals a negative number. The solution 
 is not a real number, and in the real 
number system this solution is rejected as an extraneous solution. 
 TRY IT 
#8 
Solve 
 Q&A 
Does every logarithmic equation have a solution? 
No. Keep in mind that we can only apply the logarithm to a positive number. Always check for 
extraneous solutions. 
4.6 • Exponential and Logarithmic Equations     477


--- PDF page 82 (book page 488) ---
Using the Definition of a Logarithm to Solve Logarithmic Equations 
We have already seen that every logarithmic equation 
 is equivalent to the exponential equation 
 We 
can use this fact, along with the rules of logarithms, to solve logarithmic equations where the argument is an algebraic 
expression. 
For example, consider the equation 
 To solve this equation, we can use rules of logarithms 
to rewrite the left side in compact form and then apply the definition of logs to solve for 
Using the Definition of a Logarithm to Solve Logarithmic Equations 
For any algebraic expression  and real numbers  and  where 
EXAMPLE 9 
Using Algebra to Solve a Logarithmic Equation 
Solve 
Solution 
 TRY IT 
#9 
Solve 
EXAMPLE 10 
Using Algebra Before and After Using the Definition of the Natural Logarithm 
Solve 
Solution 
 TRY IT 
#10 
Solve 
478     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 83 (book page 489) ---
EXAMPLE 11 
Using a Graph to Understand the Solution to a Logarithmic Equation 
Solve 
Solution 
Figure 3 represents the graph of the equation. On the graph, the x-coordinate of the point at which the two graphs 
intersect is close to 20. In other words 
 A calculator gives a better approximation: 
Figure 3 The graphs of 
 and 
 cross at the point 
 which is approximately (20.0855, 3). 
 TRY IT 
#11 
Use a graphing calculator to estimate the approximate solution to the logarithmic equation 
 to 2 decimal places. 
Using the One-to-One Property of Logarithms to Solve Logarithmic Equations 
As with exponential equations, we can use the one-to-one property to solve logarithmic equations. The one-to-one 
property of logarithmic functions tells us that, for any real numbers 
 
 
 and any positive real number 
where 
For example, 
So, if 
 then we can solve for 
 and we get 
 To check, we can substitute 
 into the original equation: 
 In other words, when a logarithmic equation has the same base on each side, the arguments 
must be equal. This also applies when the arguments are algebraic expressions. Therefore, when given an equation with 
logs of the same base on each side, we can use rules of logarithms to rewrite each side as a single logarithm. Then we 
use the fact that logarithmic functions are one-to-one to set the arguments equal to one another and solve for the 
unknown. 
For example, consider the equation 
 To solve this equation, we can use the rules of 
logarithms to rewrite the left side as a single logarithm, and then apply the one-to-one property to solve for 
To check the result, substitute 
 into 
4.6 • Exponential and Logarithmic Equations     479


--- PDF page 84 (book page 490) ---
...
Using the One-to-One Property of Logarithms to Solve Logarithmic Equations 
For any algebraic expressions  and  and any positive real number 
 where 
Note, when solving an equation involving logarithms, always check to see if the answer is correct or if it is an 
extraneous solution. 
HOW TO 
Given an equation containing logarithms, solve it using the one-to-one property. 
1. Use the rules of logarithms to combine like terms, if necessary, so that the resulting equation has the form 
2. Use the one-to-one property to set the arguments equal. 
3. Solve the resulting equation, 
 for the unknown. 
EXAMPLE 12 
Solving an Equation Using the One-to-One Property of Logarithms 
Solve 
Solution 
Analysis 
There are two solutions:  or 
 The solution 
 is negative, but it checks when substituted into the original equation 
because the argument of the logarithm functions is still positive. 
 TRY IT 
#12 
Solve 
Solving Applied Problems Using Exponential and Logarithmic Equations 
In previous sections, we learned the properties and rules for both exponential and logarithmic functions. We have seen 
that any exponential function can be written as a logarithmic function and vice versa. We have used exponents to solve 
logarithmic equations and logarithms to solve exponential equations. We are now ready to combine our skills to solve 
equations that model real-world situations, whether the unknown is in an exponent or in the argument of a logarithm. 
One such application is in science, in calculating the time it takes for half of the unstable material in a sample of a 
radioactive substance to decay, called its half-life. Table 1 lists the half-life for several of the more common radioactive 
substances. 
480     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 85 (book page 491) ---
Substance 
Use 
Half-life 
gallium-67 
nuclear medicine 
80 hours 
cobalt-60 
manufacturing 
5.3 years 
technetium-99m 
nuclear medicine 
6 hours 
americium-241 
construction 
432 years 
carbon-14 
archeological dating 
5,730 years 
uranium-235 
atomic power 
703,800,000 years 
Table 1 
We can see how widely the half-lives for these substances vary. Knowing the half-life of a substance allows us to calculate 
the amount remaining after a specified time. We can use the formula for radioactive decay: 
where 
• 
 is the amount initially present 
• 
 is the half-life of the substance 
• 
 is the time period over which the substance is studied 
• 
 is the amount of the substance present after time 
EXAMPLE 13 
Using the Formula for Radioactive Decay to Find the Quantity of a Substance 
How long will it take for ten percent of a 1000-gram sample of uranium-235 to decay? 
Solution 
Analysis 
Ten percent of 1000 grams is 100 grams. If 100 grams decay, the amount of uranium-235 remaining is 900 grams. 
 TRY IT 
#13 
How long will it take before twenty percent of our 1000-gram sample of uranium-235 has 
4.6 • Exponential and Logarithmic Equations     481


--- PDF page 86 (book page 492) ---
decayed? 
 MEDIA 
Access these online resources for additional instruction and practice with exponential and logarithmic equations. 
Solving Logarithmic Equations (https://openstax.org/l/solvelogeq) 
Solving Exponential Equations with Logarithms (https://openstax.org/l/solveexplog) 
 4.6 SECTION EXERCISES 
Verbal 
1 . How can an exponential 
equation be solved? 
 2 . When does an extraneous 
solution occur? How can an 
extraneous solution be 
recognized? 
 3 . When can the one-to-one 
property of logarithms be 
used to solve an equation? 
When can it not be used? 
Algebraic 
For the following exercises, use like bases to solve the exponential equation. 
4 . 
 5 . 
 6 . 
7 . 
 8 . 
 9 . 
10 . 
For the following exercises, use logarithms to solve. 
11 . 
 12 . 
 13 . 
14 . 
 15 . 
 16 . 
17 . 
 18 . 
 19 . 
20 . 
 21 . 
 22 . 
23 . 
 24 . 
 25 . 
26 . 
 27 . 
 28 . 
For the following exercises, use the definition of a logarithm to rewrite the equation as an exponential equation. 
29 . 
 30 . 
For the following exercises, use the definition of a logarithm to solve the equation. 
31 . 
 32 . 
 33 . 
34 . 
 35 . 
For the following exercises, use the one-to-one property of logarithms to solve. 
36 . 
 37 . 
 38 . 
39 . 
 40 . 
 41 . 
42 . 
 43 . 
482     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 87 (book page 493) ---
For the following exercises, solve each equation for 
44 . 
 45 . 
 46 . 
47 . 
 48 . 
 49 . 
50 . 
Graphical 
For the following exercises, solve the equation for 
 if there is a solution. Then graph both sides of the equation, and 
observe the point of intersection (if it exists) to verify the solution. 
51 . 
52 . 
 53 . 
54 . 
 55 . 
56 . 
57 . 
58 . 
 59 . 
60 . 
 61 . 
62 . 
63 . 
64 . 
For the following exercises, solve for the indicated value, and graph the situation showing the solution point. 
65 . An account with an initial 
deposit of 
 earns 
 annual interest, 
compounded continuously. 
How much will the account 
be worth after 20 years? 
66 . The formula for measuring 
sound intensity in decibels 
 is defined by the 
equation 
 where 
is the intensity of the 
sound in watts per square 
meter and 
 is 
the lowest level of sound 
that the average person 
can hear. How many 
decibels are emitted from a 
jet plane with a sound 
intensity of 
 watts 
per square meter? 
 67 . The population of a small 
town is modeled by the 
equation 
where  is measured in 
years. In approximately 
how many years will the 
town’s population reach 
Technology 
For the following exercises, solve each equation by rewriting the exponential expression using the indicated logarithm. 
Then use a calculator to approximate the variable to 3 decimal places. 
68 . 
 using 
the common log. 
 69 . 
 using the natural 
log 
 70 . 
 using the 
common log 
71 . 
 using the 
common log 
 72 . 
 using the 
natural log 
For the following exercises, use a calculator to solve the equation. Unless indicated otherwise, round all answers to the 
nearest ten-thousandth. 
73 . 
 74 . 
 75 . 
4.6 • Exponential and Logarithmic Equations     483


--- PDF page 88 (book page 494) ---
76 . Atmospheric pressure 
 in pounds per square 
inch is represented by the formula 
 where  is the number of miles 
above sea level. To the nearest foot, how high is 
the peak of a mountain with an atmospheric 
pressure of 
 pounds per square inch? (Hint: 
there are 5280 feet in a mile) 
 77 . The magnitude M of an earthquake is represented 
by the equation 
 where 
 is the 
amount of energy released by the earthquake in 
joules and 
 is the assigned minimal 
measure released by an earthquake. To the 
nearest hundredth, what would the magnitude be 
of an earthquake releasing 
 joules of 
energy? 
Extensions 
78 . Use the definition of a 
logarithm along with the 
one-to-one property of 
logarithms to prove that 
 79 . Recall the formula for 
continually compounding 
interest, 
 Use the 
definition of a logarithm 
along with properties of 
logarithms to solve the 
formula for time  such 
that  is equal to a single 
logarithm. 
 80 . Recall the compound 
interest formula 
 Use the 
definition of a logarithm 
along with properties of 
logarithms to solve the 
formula for time 
81 . Newton’s Law of Cooling states that the 
temperature  of an object at any time t can be 
described by the equation 
 where 
 is the 
temperature of the surrounding environment, 
is the initial temperature of the object, and  is 
the cooling rate. Use the definition of a logarithm 
along with properties of logarithms to solve the 
formula for time  such that  is equal to a single 
logarithm. 
4.7 Exponential and Logarithmic Models 
Learning Objectives 
In this section, you will: 
Model exponential growth and decay. 
Use Newton’s Law of Cooling. 
Use logistic-growth models. 
Choose an appropriate model for data. 
Express an exponential model in base  . 
484     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 89 (book page 495) ---
Figure 1 A nuclear research reactor inside the Neely Nuclear Research Center on the Georgia Institute of Technology 
campus (credit: Georgia Tech Research Institute) 
We have already explored some basic applications of exponential and logarithmic functions. In this section, we explore 
some important applications in more depth, including radioactive isotopes and Newton’s Law of Cooling. 
Modeling Exponential Growth and Decay 
In real-world applications, we need to model the behavior of a function. In mathematical modeling, we choose a familiar 
general function with properties that suggest that it will model the real-world phenomenon we wish to analyze. In the 
case of rapid growth, we may choose the exponential growth function: 
where 
 is equal to the value at time zero,  is Euler’s constant, and  is a positive constant that determines the rate 
(percentage) of growth. We may use the exponential growth function in applications involving doubling time, the time it 
takes for a quantity to double. Such phenomena as wildlife populations, financial investments, biological samples, and 
natural resources may exhibit growth based on a doubling time. In some applications, however, as we will see when we 
discuss the logistic equation, the logistic model sometimes fits the data better than the exponential model. 
On the other hand, if a quantity is falling rapidly toward zero, without ever reaching zero, then we should probably 
choose the exponential decay model. Again, we have the form 
 where 
 is the starting value, and  is Euler’s 
constant. Now  is a negative constant that determines the rate of decay. We may use the exponential decay model 
when we are calculating half-life, or the time it takes for a substance to exponentially decay to half of its original 
quantity. We use half-life in applications involving radioactive isotopes. 
In our choice of a function to serve as a mathematical model, we often use data points gathered by careful observation 
and measurement to construct points on a graph and hope we can recognize the shape of the graph. Exponential 
growth and decay graphs have a distinctive shape, as we can see in Figure 2 and Figure 3. It is important to remember 
that, although parts of each of the two graphs seem to lie on the x-axis, they are really a tiny distance above the x-axis. 
4.7 • Exponential and Logarithmic Models     485


--- PDF page 90 (book page 496) ---
Figure 2 A graph showing exponential growth. The equation is 
Figure 3 A graph showing exponential decay. The equation is 
Exponential growth and decay often involve very large or very small numbers. To describe these numbers, we often use 
orders of magnitude. The order of magnitude is the power of ten, when the number is expressed in scientific notation, 
with one digit to the left of the decimal. For example, the distance to the nearest star, Proxima Centauri, measured in 
kilometers, is 40,113,497,200,000 kilometers. Expressed in scientific notation, this is 
 So, we could 
describe this number as having order of magnitude 
Characteristics of the Exponential Function, 
An exponential function with the form 
 has the following characteristics: 
• one-to-one function 
• horizontal asymptote: 
• domain: 
∞∞
• range: 
∞
• x intercept: none 
• y-intercept: 
• increasing if 
 (see Figure 4) 
• decreasing if 
 (see Figure 4) 
486     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 91 (book page 497) ---
Figure 4 An exponential function models exponential growth when 
 and exponential decay when 
EXAMPLE 1 
Graphing Exponential Growth 
A population of bacteria doubles every hour. If the culture started with 10 bacteria, graph the population as a function of 
time. 
Solution 
When an amount grows at a fixed percent per unit time, the growth is exponential. To find 
 we use the fact that 
 is 
the amount at time zero, so 
 To find 
 use the fact that after one hour 
 the population doubles from 
to 
 The formula is derived as follows 
so 
 Thus the equation we want to graph is 
 The graph is shown in Figure 5. 
Figure 5 The graph of 
Analysis 
The population of bacteria after ten hours is 10,240. We could describe this amount is being of the order of magnitude 
 The population of bacteria after twenty hours is 10,485,760 which is of the order of magnitude 
 so we could say 
4.7 • Exponential and Logarithmic Models     487


--- PDF page 92 (book page 498) ---
...
that the population has increased by three orders of magnitude in ten hours. 
Half-Life 
We now turn to exponential decay. One of the common terms associated with exponential decay, as stated above, is 
half-life, the length of time it takes an exponentially decaying quantity to decrease to half its original amount. Every 
radioactive isotope has a half-life, and the process describing the exponential decay of an isotope is called radioactive 
decay. 
To find the half-life of a function describing exponential decay, solve the following equation: 
We find that the half-life depends only on the constant  and not on the starting quantity 
The formula is derived as follows 
Since  the time, is positive,  must, as expected, be negative. This gives us the half-life formula 
HOW TO 
Given the half-life, find the decay rate. 
1. Write 
2. Replace 
 by 
 and replace  by the given half-life. 
3. Solve to find 
 Express  as an exact value (do not round). 
Note: It is also possible to find the decay rate using 
EXAMPLE 2 
Finding the Function that Describes Radioactive Decay 
The half-life of carbon-14 is 5,730 years. Express the amount of carbon-14 remaining as a function of time, 
Solution 
This formula is derived as follows. 
The function that describes this continuous decay is 
 We observe that the coefficient of 
488     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 93 (book page 499) ---
 is negative, as expected in the case of exponential decay. 
 TRY IT 
#1 
The half-life of plutonium-244 is 80,000,000 years. Find a function that gives the amount of 
plutonium-244 remaining as a function of time, measured in years. 
Radiocarbon Dating 
The formula for radioactive decay is important in radiocarbon dating, which is used to calculate the approximate date a 
plant or animal died. Radiocarbon dating was discovered in 1949 by Willard Libby, who won a Nobel Prize for his 
discovery. It compares the difference between the ratio of two isotopes of carbon in an organic artifact or fossil to the 
ratio of those two isotopes in the air. It is believed to be accurate to within about 1% error for plants or animals that died 
within the last 60,000 years. 
Carbon-14 is a radioactive isotope of carbon that has a half-life of 5,730 years. It occurs in small quantities in the carbon 
dioxide in the air we breathe. Most of the carbon on Earth is carbon-12, which has an atomic weight of 12 and is not 
radioactive. Scientists have determined the ratio of carbon-14 to carbon-12 in the air for the last 60,000 years, using tree 
rings and other organic samples of known dates—although the ratio has changed slightly over the centuries. 
As long as a plant or animal is alive, the ratio of the two isotopes of carbon in its body is close to the ratio in the 
atmosphere. When it dies, the carbon-14 in its body decays and is not replaced. By comparing the ratio of carbon-14 to 
carbon-12 in a decaying sample to the known ratio in the atmosphere, the date the plant or animal died can be 
approximated. 
Since the half-life of carbon-14 is 5,730 years, the formula for the amount of carbon-14 remaining after  years is 
where 
• 
 is the amount of carbon-14 remaining 
• 
 is the amount of carbon-14 when the plant or animal began decaying. 
This formula is derived as follows: 
To find the age of an object, we solve this equation for 
Out of necessity, we neglect here the many details that a scientist takes into consideration when doing carbon-14 dating, 
and we only look at the basic formula. The ratio of carbon-14 to carbon-12 in the atmosphere is approximately 
0.0000000001%. Let  be the ratio of carbon-14 to carbon-12 in the organic artifact or fossil to be dated, determined by a 
method called liquid scintillation. From the equation 
 we know the ratio of the percentage of 
carbon-14 in the object we are dating to the initial amount of carbon-14 in the object when it was formed is 
 We solve this equation for  to get 
4.7 • Exponential and Logarithmic Models     489


--- PDF page 94 (book page 500) ---
...
HOW TO 
Given the percentage of carbon-14 in an object, determine its age. 
1. Express the given percentage of carbon-14 as an equivalent decimal, 
2. Substitute for k in the equation 
 and solve for the age, 
EXAMPLE 3 
Finding the Age of a Bone 
A bone fragment is found that contains 20% of its original carbon-14. To the nearest year, how old is the bone? 
Solution 
We substitute 
 for  in the equation and solve for 
The bone fragment is about 13,301 years old. 
Analysis 
The instruments that measure the percentage of carbon-14 are extremely sensitive and, as we mention above, a scientist 
will need to do much more work than we did in order to be satisfied. Even so, carbon dating is only accurate to about 1%, 
so this age should be given as 
 TRY IT 
#2 
Cesium-137 has a half-life of about 30 years. If we begin with 200 mg of cesium-137, will it take 
more or less than 230 years until only 1 milligram remains? 
Calculating Doubling Time 
For decaying quantities, we determined how long it took for half of a substance to decay. For growing quantities, we 
might want to find out how long it takes for a quantity to double. As we mentioned above, the time it takes for a quantity 
to double is called the doubling time. 
Given the basic exponential growth equation 
 doubling time can be found by solving for when the original 
quantity has doubled, that is, by solving 
The formula is derived as follows: 
Thus the doubling time is 
EXAMPLE 4 
Finding a Function That Describes Exponential Growth 
According to Moore’s Law, the doubling time for the number of transistors that can be put on a computer chip is 
approximately two years. Give a function that describes this behavior. 
490     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 95 (book page 501) ---
...
Solution 
The formula is derived as follows: 
The function is 
 TRY IT 
#3 
Recent data suggests that, as of 2013, the rate of growth predicted by Moore’s Law no longer 
holds. Growth has slowed to a doubling time of approximately three years. Find the new function 
that takes that longer doubling time into account. 
Using Newton’s Law of Cooling 
Exponential decay can also be applied to temperature. When a hot object is left in surrounding air that is at a lower 
temperature, the object’s temperature will decrease exponentially, leveling off as it approaches the surrounding air 
temperature. On a graph of the temperature function, the leveling off will correspond to a horizontal asymptote at the 
temperature of the surrounding air. Unless the room temperature is zero, this will correspond to a vertical shift of the 
generic exponential decay function. This translation leads to Newton’s Law of Cooling, the scientific formula for 
temperature as a function of time as an object’s temperature is equalized with the ambient temperature 
This formula is derived as follows: 
Newton’s Law of Cooling 
The temperature of an object, 
 in surrounding air with temperature 
 will behave according to the formula 
where 
• 
 is time 
• 
 is the difference between the initial temperature of the object and the surroundings 
• 
 is a constant, the continuous rate of cooling of the object 
HOW TO 
Given a set of conditions, apply Newton’s Law of Cooling. 
1. Set 
 equal to the y-coordinate of the horizontal asymptote (usually the ambient temperature). 
2. Substitute the given values into the continuous growth formula 
 to find the parameters 
 and 
3. Substitute in the desired time to find the temperature or the desired temperature to find the time. 
4.7 • Exponential and Logarithmic Models     491


--- PDF page 96 (book page 502) ---
EXAMPLE 5 
Using Newton’s Law of Cooling 
A cheesecake is taken out of the oven with an ideal internal temperature of 
 and is placed into a 
 refrigerator. 
After 10 minutes, the cheesecake has cooled to 
 If we must wait until the cheesecake has cooled to 
 before 
we eat it, how long will we have to wait? 
Solution 
Because the surrounding air temperature in the refrigerator is 35 degrees, the cheesecake’s temperature will decay 
exponentially toward 35, following the equation 
We know the initial temperature was 165, so 
We were given another data point, 
 which we can use to solve for 
This gives us the equation for the cooling of the cheesecake: 
Now we can solve for the time it will take for the temperature to cool to 70 degrees. 
It will take about 107 minutes, or one hour and 47 minutes, for the cheesecake to cool to 
 TRY IT 
#4 
A pitcher of water at 40 degrees Fahrenheit is placed into a 70 degree room. One hour later, the 
temperature has risen to 45 degrees. How long will it take for the temperature to rise to 60 
degrees? 
Using Logistic Growth Models 
Exponential growth cannot continue forever. Exponential models, while they may be useful in the short term, tend to fall 
apart the longer they continue. Consider an aspiring writer who writes a single line on day one and plans to double the 
number of lines she writes each day for a month. By the end of the month, she must write over 17 billion lines, or one-
half-billion pages. It is impractical, if not impossible, for anyone to write that much in such a short period of time. 
Eventually, an exponential model must begin to approach some limiting value, and then the growth is forced to slow. For 
this reason, it is often better to use a model with an upper bound instead of an exponential growth model, though the 
exponential growth model is still useful over a short term, before approaching the limiting value. 
The logistic growth model is approximately exponential at first, but it has a reduced rate of growth as the output 
approaches the model’s upper bound, called the carrying capacity. For constants 
 and  the logistic growth of a 
population over time  is represented by the model 
492     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 97 (book page 503) ---
The graph in Figure 6 shows how the growth rate changes over time. The graph increases from left to right, but the 
growth rate only increases until it reaches its point of maximum growth rate, at which point the rate of increase 
decreases. 
Figure 6 
Logistic Growth 
The logistic growth model is 
where 
• 
 is the initial value 
• 
 is the carrying capacity, or limiting value 
• 
 is a constant determined by the rate of growth. 
EXAMPLE 6 
Using the Logistic-Growth Model 
An influenza epidemic spreads through a population rapidly, at a rate that depends on two factors: The more people who 
have the flu, the more rapidly it spreads, and also the more uninfected people there are, the more rapidly it spreads. 
These two factors make the logistic model a good one to study the spread of communicable diseases. And, clearly, there 
is a maximum value for the number of people infected: the entire population. 
For example, at time 
 there is one person in a community of 1,000 people who has the flu. So, in that community, at 
most 1,000 people can have the flu. Researchers find that for this particular strain of the flu, the logistic growth constant 
is 
 Estimate the number of people in this community who will have had this flu after ten days. Predict how 
many people in this community will have had this flu after a long period of time has passed. 
Solution 
We substitute the given data into the logistic growth model 
Because at most 1,000 people, the entire population of the community, can get the flu, we know the limiting value is 
 To find 
 we use the formula that the number of cases at time 
 is 
 from which it follows that 
 This model predicts that, after ten days, the number of people who have had the flu is 
4.7 • Exponential and Logarithmic Models     493


--- PDF page 98 (book page 504) ---
 Because the actual number must be a whole number (a person has either had the flu or 
not) we round to 294. In the long term, the number of people who will contract the flu is the limiting value, 
Analysis 
Remember that, because we are dealing with a virus, we cannot predict with certainty the number of people infected. 
The model only approximates the number of people infected and will not give us exact or actual values. 
The graph in Figure 7 gives a good picture of how this model fits the data. 
Figure 7 The graph of 
 TRY IT 
#5 
Using the model in Example 6, estimate the number of cases of flu on day 15. 
Choosing an Appropriate Model for Data 
Now that we have discussed various mathematical models, we need to learn how to choose the appropriate model for 
the raw data we have. Many factors influence the choice of a mathematical model, among which are experience, 
scientific laws, and patterns in the data itself. Not all data can be described by elementary functions. Sometimes, a 
function is chosen that approximates the data over a given interval. For instance, suppose data were gathered on the 
number of homes bought in the United States from the years 1960 to 2013. After plotting these data in a scatter plot, we 
notice that the shape of the data from the years 2000 to 2013 follow a logarithmic curve. We could restrict the interval 
from 2000 to 2010, apply regression analysis using a logarithmic model, and use it to predict the number of home 
buyers for the year 2015. 
Three kinds of functions that are often useful in mathematical models are linear functions, exponential functions, and 
logarithmic functions. If the data lies on a straight line, or seems to lie approximately along a straight line, a linear model 
may be best. If the data is non-linear, we often consider an exponential or logarithmic model, though other models, such 
as quadratic models, may also be considered. 
In choosing between an exponential model and a logarithmic model, we look at the way the data curves. This is called 
the concavity. If we draw a line between two data points, and all (or most) of the data between those two points lies 
above that line, we say the curve is concave down. We can think of it as a bowl that bends downward and therefore 
cannot hold water. If all (or most) of the data between those two points lies below the line, we say the curve is concave 
up. In this case, we can think of a bowl that bends upward and can therefore hold water. An exponential curve, whether 
rising or falling, whether representing growth or decay, is always concave up away from its horizontal asymptote. A 
logarithmic curve is always concave away from its vertical asymptote. In the case of positive data, which is the most 
common case, an exponential curve is always concave up, and a logarithmic curve always concave down. 
494     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 99 (book page 505) ---
A logistic curve changes concavity. It starts out concave up and then changes to concave down beyond a certain point, 
called a point of inflection. 
After using the graph to help us choose a type of function to use as a model, we substitute points, and solve to find the 
parameters. We reduce round-off error by choosing points as far apart as possible. 
EXAMPLE 7 
Choosing a Mathematical Model 
Does a linear, exponential, logarithmic, or logistic model best fit the values listed in Table 1? Find the model, and use a 
graph to check your choice. 
1 
2 
3 
4 
5 
6 
7 
8 
9 
0 
1.386 
2.197 
2.773 
3.219 
3.584 
3.892 
4.159 
4.394 
Table 1 
Solution 
First, plot the data on a graph as in Figure 8. For the purpose of graphing, round the data to two decimal places. 
Figure 8 
Clearly, the points do not lie on a straight line, so we reject a linear model. If we draw a line between any two of the 
points, most or all of the points between those two points lie above the line, so the graph is concave down, suggesting a 
logarithmic model. We can try 
 Plugging in the first point, 
 gives 
 We reject the case that 
 (if it were, all outputs would be 0), so we know 
 Thus 
 and 
 Next we can use the point 
 to solve for 
Because 
 an appropriate model for the data is 
To check the accuracy of the model, we graph the function together with the given points as in Figure 9. 
4.7 • Exponential and Logarithmic Models     495


--- PDF page 100 (book page 506) ---
Figure 9 The graph of 
We can conclude that the model is a good fit to the data. 
Compare Figure 9 to the graph of 
 shown in Figure 10. 
Figure 10 The graph of 
The graphs appear to be identical when 
 A quick check confirms this conclusion: 
 for 
However, if 
 the graph of 
 includes a “extra” branch, as shown in Figure 11. This occurs because, while 
 cannot have negative values in the domain (as such values would force the argument to be negative), the 
function 
 can have negative domain values. 
496     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 101 (book page 507) ---
...
Figure 11 
 TRY IT 
#6 
Does a linear, exponential, or logarithmic model best fit the data in Table 2? Find the model. 
1 
2 
3 
4 
5 
6 
7 
8 
9 
3.297 
5.437 
8.963 
14.778 
24.365 
40.172 
66.231 
109.196 
180.034 
Table 2 
Expressing an Exponential Model in Base 
While powers and logarithms of any base can be used in modeling, the two most common bases are 
 and 
 In science 
and mathematics, the base  is often preferred. We can use laws of exponents and laws of logarithms to change any 
base to base 
HOW TO 
Given a model with the form 
 change it to the form 
1. Rewrite 
 as 
2. Use the power rule of logarithms to rewrite y as 
3. Note that 
 and 
 in the equation 
EXAMPLE 8 
Changing to base e 
Change the function 
 so that this same function is written in the form 
Solution 
The formula is derived as follows 
 TRY IT 
#7 
Change the function 
 to one having  as the base. 
 MEDIA 
Access these online resources for additional instruction and practice with exponential and logarithmic models. 
4.7 • Exponential and Logarithmic Models     497


--- PDF page 102 (book page 508) ---
Logarithm Application – pH (https://openstax.org/l/logph) 
Exponential Model – Age Using Half-Life (https://openstax.org/l/expmodelhalf) 
Newton’s Law of Cooling (https://openstax.org/l/newtoncooling) 
Exponential Growth Given Doubling Time (https://openstax.org/l/expgrowthdbl) 
Exponential Growth – Find Initial Amount Given Doubling Time (https://openstax.org/l/initialdouble) 
 4.7 SECTION EXERCISES 
Verbal 
1 . With what kind of 
exponential model would 
half-life be associated? What 
role does half-life play in 
these models? 
 2 . What is carbon dating? Why 
does it work? Give an 
example in which carbon 
dating would be useful. 
 3 . With what kind of 
exponential model would 
doubling time be 
associated? What role does 
doubling time play in these 
models? 
4 . Define Newton’s Law of 
Cooling. Then name at least 
three real-world situations 
where Newton’s Law of 
Cooling would be applied. 
 5 . What is an order of 
magnitude? Why are orders 
of magnitude useful? Give 
an example to explain. 
Numeric 
6 . The temperature of an 
object in degrees Fahrenheit 
after t minutes is 
represented by the equation 
 To 
the nearest degree, what is 
the temperature of the 
object after one and a half 
hours? 
For the following exercises, use the logistic growth model 
7 . Find and interpret 
Round to the nearest tenth. 
 8 . Find and interpret 
Round to the nearest tenth. 
 9 . Find the carrying capacity. 
498     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 103 (book page 509) ---
10 . Graph the model. 
 11 . Determine whether the 
data from the table could 
best be represented as a 
function that is linear, 
exponential, or 
logarithmic. Then write a 
formula for a model that 
represents the data. 
–2 
0.694 
–1 
0.833 
0 
1 
1 
1.2 
2 
1.44 
3 
1.728 
4 
2.074 
5 
2.488 
 12 . Rewrite 
as an exponential equation 
with base  to five decimal 
places. 
4.7 • Exponential and Logarithmic Models     499


--- PDF page 104 (book page 510) ---
Technology 
For the following exercises, enter the data from each table into a graphing calculator and graph the resulting scatter 
plots. Determine whether the data from the table could represent a function that is linear, exponential, or logarithmic. 
13 . 
1 
2 
2 
4.079 
3 
5.296 
4 
6.159 
5 
6.828 
6 
7.375 
7 
7.838 
8 
8.238 
9 
8.592 
10 
8.908 
14 . 
1 
2.4 
2 
2.88 
3 
3.456 
4 
4.147 
5 
4.977 
6 
5.972 
7 
7.166 
8 
8.6 
9 
10.32 
10 
12.383 
15 . 
4 
9.429 
5 
9.972 
6 
10.415 
7 
10.79 
8 
11.115 
9 
11.401 
10 
11.657 
11 
11.889 
12 
12.101 
13 
12.295 
16 . 
1.25 
5.75 
2.25 
8.75 
3.56 
12.68 
4.2 
14.6 
5.65 
18.95 
6.75 
22.25 
7.25 
23.75 
8.6 
27.8 
9.25 
29.75 
10.5 
33.5 
500     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 105 (book page 511) ---
For the following exercises, use a graphing calculator and this scenario: the population of a fish farm in  years is 
modeled by the equation 
17 . Graph the function. 
18 . What is the initial 
population of fish? 
 19 . To the nearest tenth, what 
is the doubling time for the 
fish population? 
20 . To the nearest whole 
number, what will the fish 
population be after 
years? 
 21 . To the nearest tenth, how 
long will it take for the 
population to reach 
 22 . What is the carrying 
capacity for the fish 
population? Justify your 
answer using the graph of 
Extensions 
23 . A substance has a half-life 
of 2.045 minutes. If the 
initial amount of the 
substance was 132.8 
grams, how many half-lives 
will have passed before the 
substance decays to 8.3 
grams? What is the total 
time of decay? 
 24 . The formula for an 
increasing population is 
given by 
where 
 is the initial 
population and 
Derive a general formula 
for the time t it takes for 
the population to increase 
by a factor of M. 
 25 . Recall the formula for 
calculating the magnitude 
of an earthquake, 
 Show 
each step for solving this 
equation algebraically for 
the seismic moment 
26 . What is the y-intercept of 
the logistic growth model 
 Show the 
steps for calculation. What 
does this point tell us 
about the population? 
 27 . Prove that 
 for 
positive 
Real-World Applications 
For the following exercises, use this scenario: A doctor prescribes 125 milligrams of a therapeutic drug that decays by 
about 30% each hour. 
28 . To the nearest hour, what is 
the half-life of the drug? 
 29 . Write an exponential 
model representing the 
amount of the drug 
remaining in the patient’s 
system after  hours. Then 
use the formula to find the 
amount of the drug that 
would remain in the 
patient’s system after 3 
hours. Round to the 
nearest milligram. 
 30 . Using the model found in 
the previous exercise, find 
 and interpret the 
result. Round to the 
nearest hundredth. 
4.7 • Exponential and Logarithmic Models     501


--- PDF page 106 (book page 512) ---
For the following exercises, use this scenario: A tumor is injected with 
 grams of Iodine-125, which has a decay rate of 
 per day. 
31 . To the nearest day, how 
long will it take for half of 
the Iodine-125 to decay? 
 32 . Write an exponential 
model representing the 
amount of Iodine-125 
remaining in the tumor 
after  days. Then use the 
formula to find the amount 
of Iodine-125 that would 
remain in the tumor after 
60 days. Round to the 
nearest tenth of a gram. 
 33 . A scientist begins with 
grams of a radioactive 
substance. After 
minutes, the sample has 
decayed to 
 grams. 
Rounding to five decimal 
places, write an 
exponential equation 
representing this situation. 
To the nearest minute, 
what is the half-life of this 
substance? 
34 . The half-life of Radium-226 
is 
 years. What is the 
annual decay rate? Express 
the decimal result to four 
decimal places and the 
percentage to two decimal 
places. 
 35 . The half-life of Erbium-165 
is 
 hours. What is the 
hourly decay rate? Express 
the decimal result to four 
decimal places and the 
percentage to two decimal 
places. 
 36 . A wooden artifact from an 
archeological dig contains 
60 percent of the 
carbon-14 that is present in 
living trees. To the nearest 
year, about how many 
years old is the artifact? 
(The half-life of carbon-14 
is 
 years.) 
37 . A research student is 
working with a culture of 
bacteria that doubles in 
size every twenty minutes. 
The initial population count 
was 
 bacteria. 
Rounding to five decimal 
places, write an 
exponential equation 
representing this situation. 
To the nearest whole 
number, what is the 
population size after 
hours? 
For the following exercises, use this scenario: A biologist recorded a count of 
 bacteria present in a culture after 5 
minutes and 1000 bacteria present after 20 minutes. 
38 . To the nearest whole 
number, what was the 
initial population in the 
culture? 
 39 . Rounding to six decimal 
places, write an 
exponential equation 
representing this situation. 
To the nearest minute, how 
long did it take the 
population to double? 
For the following exercises, use this scenario: A pot of warm soup with an internal temperature of 
 Fahrenheit was 
taken off the stove to cool in a 
 room. After fifteen minutes, the internal temperature of the soup was 
40 . Use Newton’s Law of 
Cooling to write a formula 
that models this situation. 
 41 . To the nearest minute, how 
long will it take the soup to 
cool to 
 42 . To the nearest degree, 
what will the temperature 
be after  and a half hours? 
502     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 107 (book page 513) ---
For the following exercises, use this scenario: A turkey is taken out of the oven with an internal temperature of 
and is allowed to cool in a 
 room. After half an hour, the internal temperature of the turkey is 
43 . Write a formula that 
models this situation. 
 44 . To the nearest degree, 
what will the temperature 
be after 50 minutes? 
 45 . To the nearest minute, how 
long will it take the turkey 
to cool to 
For the following exercises, find the value of the number shown on each logarithmic scale. Round all answers to the 
nearest thousandth. 
46 . 
47 . 
48 . Plot each set of approximate values of intensity of 
sounds on a logarithmic scale: Whisper: 
 Vacuum: 
 Jet: 
 49 . Recall the formula for calculating the magnitude 
of an earthquake, 
 One 
earthquake has magnitude 
 on the MMS scale. 
If a second earthquake has 
 times as much 
energy as the first, find the magnitude of the 
second quake. Round to the nearest hundredth. 
For the following exercises, use this scenario: The equation 
 models the number of people in a town 
who have heard a rumor after t days. 
50 . How many people started 
the rumor? 
 51 . To the nearest whole 
number, how many people 
will have heard the rumor 
after 3 days? 
 52 . As  increases without 
bound, what value does 
 approach? Interpret 
your answer. 
For the following exercise, choose the correct answer choice. 
ⓐ 
ⓑ 
ⓒ 
ⓓ 
53 . A doctor injects a patient with 13 milligrams of 
radioactive dye that decays exponentially. After 12 
minutes, there are 4.75 milligrams of dye 
remaining in the patient’s system. Which is an 
appropriate model for this situation? 
4.8 Fitting Exponential Models to Data 
Learning Objectives 
In this section, you will: 
Build an exponential model from data. 
Build a logarithmic model from data. 
Build a logistic model from data. 
In previous sections of this chapter, we were either given a function explicitly to graph or evaluate, or we were given a set 
of points that were guaranteed to lie on the curve. Then we used algebra to find the equation that fit the points exactly. 
In this section, we use a modeling technique called regression analysis to find a curve that models data collected from 
real-world observations. With regression analysis, we don’t expect all the points to lie perfectly on the curve. The idea is 
to find a model that best fits the data. Then we use the model to make predictions about future events. 
Do not be confused by the word model. In mathematics, we often use the terms function, equation, and model 
interchangeably, even though they each have their own formal definition. The term model is typically used to indicate 
that the equation or function approximates a real-world situation. 
We will concentrate on three types of regression models in this section: exponential, logarithmic, and logistic. Having 
4.8 • Fitting Exponential Models to Data     503


--- PDF page 108 (book page 514) ---
...
already worked with each of these functions gives us an advantage. Knowing their formal definitions, the behavior of 
their graphs, and some of their real-world applications gives us the opportunity to deepen our understanding. As each 
regression model is presented, key features and definitions of its associated function are included for review. Take a 
moment to rethink each of these functions, reflect on the work we’ve done so far, and then explore the ways regression 
is used to model real-world phenomena. 
Building an Exponential Model from Data 
As we’ve learned, there are a multitude of situations that can be modeled by exponential functions, such as investment 
growth, radioactive decay, atmospheric pressure changes, and temperatures of a cooling object. What do these 
phenomena have in common? For one thing, all the models either increase or decrease as time moves forward. But 
that’s not the whole story. It’s the way data increase or decrease that helps us determine whether it is best modeled by 
an exponential equation. Knowing the behavior of exponential functions in general allows us to recognize when to use 
exponential regression, so let’s review exponential growth and decay. 
Recall that exponential functions have the form 
 or 
 When performing regression analysis, we use the 
form most commonly used on graphing utilities, 
 Take a moment to reflect on the characteristics we’ve already 
learned about the exponential function 
 (assume 
• 
 must be greater than zero and not equal to one. 
• The initial value of the model is 
◦ If 
 the function models exponential growth. As  increases, the outputs of the model increase slowly at 
first, but then increase more and more rapidly, without bound. 
◦ If 
 the function models exponential decay. As  increases, the outputs for the model decrease rapidly 
at first and then level off to become asymptotic to the x-axis. In other words, the outputs never become equal to 
or less than zero. 
As part of the results, your calculator will display a number known as the correlation coefficient, labeled by the variable 
or 
 (You may have to change the calculator’s settings for these to be shown.) The values are an indication of the 
“goodness of fit” of the regression equation to the data. We more commonly use the value of 
 instead of  but the 
closer either value is to 1, the better the regression equation approximates the data. 
Exponential Regression 
Exponential regression is used to model situations in which growth begins slowly and then accelerates rapidly without 
bound, or where decay begins rapidly and then slows down to get closer and closer to zero. We use the command 
“ExpReg” on a graphing utility to fit an exponential function to a set of data points. This returns an equation of the 
form, 
Note that: 
• 
 must be non-negative. 
• when 
 we have an exponential growth model. 
• when 
 we have an exponential decay model. 
HOW TO 
Given a set of data, perform exponential regression using a graphing utility. 
1. Use the STAT then EDIT menu to enter given data. 
a. Clear any existing data from the lists. 
b. List the input values in the L1 column. 
c. List the output values in the L2 column. 
2. Graph and observe a scatter plot of the data using the STATPLOT feature. 
a. Use ZOOM [9] to adjust axes to fit the data. 
b. Verify the data follow an exponential pattern. 
3. Find the equation that models the data. 
504     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 109 (book page 515) ---
a. Select “ExpReg” from the STAT then CALC menu. 
b. Use the values returned for a and b to record the model, 
4. Graph the model in the same window as the scatterplot to verify it is a good fit for the data. 
EXAMPLE 1 
Using Exponential Regression to Fit a Model to Data 
In 2007, a university study was published investigating the crash risk of alcohol impaired driving. Data from 2,871 
crashes were used to measure the association of a person’s blood alcohol level (BAC) with the risk of being in an 
accident. Table 1 shows results from the study 9 . The relative risk is a measure of how many times more likely a person is 
to crash. So, for example, a person with a BAC of 0.09 is 3.54 times as likely to crash as a person who has not been 
drinking alcohol. 
BAC 
0 
0.01 
0.03 
0.05 
0.07 
0.09 
Relative Risk of Crashing 
1 
1.03 
1.06 
1.38 
2.09 
3.54 
BAC 
0.11 
0.13 
0.15 
0.17 
0.19 
0.21 
Relative Risk of Crashing 
6.41 
12.6 
22.1 
39.05 
65.32 
99.78 
Table 1 
a. Let  represent the BAC level, and let  represent the corresponding relative risk. Use exponential regression to fit a 
model to these data. 
b. After 6 drinks, a person weighing 160 pounds will have a BAC of about 
 How many times more likely is a person 
with this weight to crash if they drive after having a 6-pack of beer? Round to the nearest hundredth. 
Solution 
a. Using the STAT then EDIT menu on a graphing utility, list the BAC values in L1 and the relative risk values in L2. Then 
use the STATPLOT feature to verify that the scatterplot follows the exponential pattern shown in Figure 1: 
Figure 1 
Use the “ExpReg” command from the STAT then CALC menu to obtain the exponential model, 
9 Source: Indiana University Center for Studies of Law in Action, 2007 
4.8 • Fitting Exponential Models to Data     505


--- PDF page 110 (book page 516) ---
Converting from scientific notation, we have: 
Notice that 
 which indicates the model is a good fit to the data. To see this, graph the model in the same 
window as the scatterplot to verify it is a good fit as shown in Figure 2: 
Figure 2 
b. Use the model to estimate the risk associated with a BAC of 
 Substitute 
 for  in the model and solve for 
If a 160-pound person drives after having 6 drinks, they are about 26.35 times more likely to crash than if driving 
while sober. 
 TRY IT 
#1 
Table 2 shows a recent graduate’s credit card balance each month after graduation. 
Month 
1 
2 
3 
4 
5 
6 
7 
8 
Debt ($) 
620.00 
761.88 
899.80 
1039.93 
1270.63 
1589.04 
1851.31 
2154.92 
Table 2 
ⓐ Use exponential regression to fit a model to these data. 
ⓑ If spending continues at this rate, what will the graduate’s credit card debt be one year after 
graduating? 
 Q&A 
Is it reasonable to assume that an exponential regression model will represent a situation 
indefinitely? 
No. Remember that models are formed by real-world data gathered for regression. It is usually 
reasonable to make estimates within the interval of original observation (interpolation). However, when 
a model is used to make predictions, it is important to use reasoning skills to determine whether the 
506     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 111 (book page 517) ---
...
model makes sense for inputs far beyond the original observation interval (extrapolation). 
Building a Logarithmic Model from Data 
Just as with exponential functions, there are many real-world applications for logarithmic functions: intensity of sound, 
pH levels of solutions, yields of chemical reactions, production of goods, and growth of infants. As with exponential 
models, data modeled by logarithmic functions are either always increasing or always decreasing as time moves 
forward. Again, it is the way they increase or decrease that helps us determine whether a logarithmic model is best. 
Recall that logarithmic functions increase or decrease rapidly at first, but then steadily slow as time moves on. By 
reflecting on the characteristics we’ve already learned about this function, we can better analyze real world situations 
that reflect this type of growth or decay. When performing logarithmic regression analysis, we use the form of the 
logarithmic function most commonly used on graphing utilities, 
 For this function 
• All input values, 
 must be greater than zero. 
• The point 
 is on the graph of the model. 
• If 
 the model is increasing. Growth increases rapidly at first and then steadily slows over time. 
• If 
 the model is decreasing. Decay occurs rapidly at first and then steadily slows over time. 
Logarithmic Regression 
Logarithmic regression is used to model situations where growth or decay accelerates rapidly at first and then slows 
over time. We use the command “LnReg” on a graphing utility to fit a logarithmic function to a set of data points. This 
returns an equation of the form, 
Note that 
• all input values, 
 must be non-negative. 
• when 
 the model is increasing. 
• when 
 the model is decreasing. 
HOW TO 
Given a set of data, perform logarithmic regression using a graphing utility. 
1. Use the STAT then EDIT menu to enter given data. 
a. Clear any existing data from the lists. 
b. List the input values in the L1 column. 
c. List the output values in the L2 column. 
2. Graph and observe a scatter plot of the data using the STATPLOT feature. 
a. Use ZOOM [9] to adjust axes to fit the data. 
b. Verify the data follow a logarithmic pattern. 
3. Find the equation that models the data. 
a. Select “LnReg” from the STAT then CALC menu. 
b. Use the values returned for a and b to record the model, 
4. Graph the model in the same window as the scatterplot to verify it is a good fit for the data. 
EXAMPLE 2 
Using Logarithmic Regression to Fit a Model to Data 
Due to advances in medicine and higher standards of living, life expectancy has been increasing in most developed 
countries since the beginning of the 20th century. 
4.8 • Fitting Exponential Models to Data     507


--- PDF page 112 (book page 518) ---
Table 3 shows the average life expectancies, in years, of Americans from 1900–201010 . 
Year 
1900 
1910 
1920 
1930 
1940 
1950 
Life Expectancy(Years) 
47.3 
50.0 
54.1 
59.7 
62.9 
68.2 
Year 
1960 
1970 
1980 
1990 
2000 
2010 
Life Expectancy(Years) 
69.7 
70.8 
73.7 
75.4 
76.8 
78.7 
Table 3 
ⓐ Let  represent time in decades starting with 
 for the year 1900, 
 for the year 1910, and so on. Let 
represent the corresponding life expectancy. Use logarithmic regression to fit a model to these data. 
ⓑ Use the model to predict the average American life expectancy for the year 2030. 
10 Source: Center for Disease Control and Prevention, 2013 
508     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 113 (book page 519) ---
Solution 
ⓐ Using the STAT then EDIT menu on a graphing utility, list the years using values 1–12 in L1 and the 
corresponding life expectancy in L2. Then use the STATPLOT feature to verify that the scatterplot follows a logarithmic 
pattern as shown in Figure 3: 
Figure 3 
Use the “LnReg” command from the STAT then CALC menu to obtain the logarithmic model, 
Next, graph the model in the same window as the scatterplot to verify it is a good fit as shown in Figure 4: 
Figure 4 
ⓑ To predict the life expectancy of an American in the year 2030, substitute 
 for the in the model and solve 
for 
If life expectancy continues to increase at this pace, the average life expectancy of an American will be 79.1 by the 
year 2030. 
4.8 • Fitting Exponential Models to Data     509


--- PDF page 114 (book page 520) ---
 TRY IT 
#2 
Sales of a video game released in the year 2000 took off at first, but then steadily slowed as time 
moved on. Table 4 shows the number of games sold, in thousands, from the years 2000–2010. 
Year 
2000 
2001 
2002 
2003 
2004 
2005 
Number Sold (thousands) 
142 
149 
154 
155 
159 
161 
Year 
2006 
2007 
2008 
2009 
2010 
- 
Number Sold (thousands) 
163 
164 
164 
166 
167 
- 
Table 4 
ⓐ Let  represent time in years starting with 
 for the year 2000. Let  represent the 
number of games sold in thousands. Use logarithmic regression to fit a model to these data. 
ⓑ If games continue to sell at this rate, how many games will sell in 2015? Round to the nearest 
thousand. 
Building a Logistic Model from Data 
Like exponential and logarithmic growth, logistic growth increases over time. One of the most notable differences with 
logistic growth models is that, at a certain point, growth steadily slows and the function approaches an upper bound, or 
limiting value. Because of this, logistic regression is best for modeling phenomena where there are limits in expansion, 
such as availability of living space or nutrients. 
It is worth pointing out that logistic functions actually model resource-limited exponential growth. There are many 
examples of this type of growth in real-world situations, including population growth and spread of disease, rumors, and 
even stains in fabric. When performing logistic regression analysis, we use the form most commonly used on graphing 
utilities: 
Recall that: 
• 
 is the initial value of the model. 
• when 
 the model increases rapidly at first until it reaches its point of maximum growth rate, 
 At 
that point, growth steadily slows and the function becomes asymptotic to the upper bound 
• 
 is the limiting value, sometimes called the carrying capacity, of the model. 
Logistic Regression 
Logistic regression is used to model situations where growth accelerates rapidly at first and then steadily slows to an 
upper limit. We use the command “Logistic” on a graphing utility to fit a logistic function to a set of data points. This 
returns an equation of the form 
Note that 
• The initial value of the model is 
• Output values for the model grow closer and closer to 
 as time increases. 
510     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 115 (book page 521) ---
...
HOW TO 
Given a set of data, perform logistic regression using a graphing utility. 
1. Use the STAT then EDIT menu to enter given data. 
a. Clear any existing data from the lists. 
b. List the input values in the L1 column. 
c. List the output values in the L2 column. 
2. Graph and observe a scatter plot of the data using the STATPLOT feature. 
a. Use ZOOM [9] to adjust axes to fit the data. 
b. Verify the data follow a logistic pattern. 
3. Find the equation that models the data. 
a. Select “Logistic” from the STAT then CALC menu. 
b. Use the values returned for 
 
 and  to record the model, 
4. Graph the model in the same window as the scatterplot to verify it is a good fit for the data. 
EXAMPLE 3 
Using Logistic Regression to Fit a Model to Data 
Mobile telephone service has increased rapidly in America since the mid 1990s. Today, almost all residents have cellular 
service. Table 5 shows the percentage of Americans with cellular service between the years 1995 and 2012 11 . 
Year 
Americans with Cellular Service (%) 
Year 
Americans with Cellular Service (%) 
1995 
12.69 
2004 
62.852 
1996 
16.35 
2005 
68.63 
1997 
20.29 
2006 
76.64 
1998 
25.08 
2007 
82.47 
1999 
30.81 
2008 
85.68 
2000 
38.75 
2009 
89.14 
2001 
45.00 
2010 
91.86 
2002 
49.16 
2011 
95.28 
2003 
55.15 
2012 
98.17 
Table 5 
ⓐ Let  represent time in years starting with 
 for the year 1995. Let  represent the corresponding percentage of 
residents with cellular service. Use logistic regression to fit a model to these data. 
ⓑ Use the model to calculate the percentage of Americans with cell service in the year 2013. Round to the nearest 
tenth of a percent. 
ⓒ Discuss the value returned for the upper limit,  What does this tell you about the model? What would the limiting 
value be if the model were exact? 
11 Source: The World Bank, 2013 
4.8 • Fitting Exponential Models to Data     511


--- PDF page 116 (book page 522) ---
Solution 
ⓐ Using the STAT then EDIT menu on a graphing utility, list the years using values 0–15 in L1 and the corresponding 
percentage in L2. Then use the STATPLOT feature to verify that the scatterplot follows a logistic pattern as shown in 
Figure 5: 
Figure 5 
Use the “Logistic” command from the STAT then CALC menu to obtain the logistic model, 
Next, graph the model in the same window as shown in Figure 6 the scatterplot to verify it is a good fit: 
Figure 6 
ⓑ 
To approximate the percentage of Americans with cellular service in the year 2013, substitute 
 for the in the 
model and solve for 
512     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 117 (book page 523) ---
According to the model, about 99.3% of Americans had cellular service in 2013. 
ⓒ 
The model gives a limiting value of about 105. This means that the maximum possible percentage of Americans with 
cellular service would be 105%, which is impossible. (How could over 100% of a population have cellular service?) If the 
model were exact, the limiting value would be 
 and the model’s outputs would get very close to, but never 
actually reach 100%. After all, there will always be someone out there without cellular service! 
 TRY IT 
#3 
Table 6 shows the population, in thousands, of harbor seals in the Wadden Sea over the years 
1997 to 2012. 
Year 
Seal Population (Thousands) 
Year 
Seal Population (Thousands) 
1997 
3.493 
2005 
19.590 
1998 
5.282 
2006 
21.955 
1999 
6.357 
2007 
22.862 
2000 
9.201 
2008 
23.869 
2001 
11.224 
2009 
24.243 
2002 
12.964 
2010 
24.344 
2003 
16.226 
2011 
24.919 
2004 
18.137 
2012 
25.108 
Table 6 
ⓐ Let  represent time in years starting with 
 for the year 1997. Let  represent the 
number of seals in thousands. Use logistic regression to fit a model to these data. 
ⓑ Use the model to predict the seal population for the year 2020. 
ⓒ To the nearest whole number, what is the limiting value of this model? 
 MEDIA 
Access this online resource for additional instruction and practice with exponential function models. 
Exponential Regression on a Calculator (https://openstax.org/l/pregresscalc) 
4.8 • Fitting Exponential Models to Data     513


--- PDF page 118 (book page 524) ---
 4.8 SECTION EXERCISES 
Verbal 
1 . What situations are best 
modeled by a logistic 
equation? Give an example, 
and state a case for why the 
example is a good fit. 
 2 . What is a carrying capacity? 
What kind of model has a 
carrying capacity built into 
its formula? Why does this 
make sense? 
 3 . What is regression analysis? 
Describe the process of 
performing regression 
analysis on a graphing 
utility. 
4 . What might a scatterplot of 
data points look like if it 
were best described by a 
logarithmic model? 
 5 . What does the y-intercept 
on the graph of a logistic 
equation correspond to for 
a population modeled by 
that equation? 
Graphical 
For the following exercises, match the given function of best fit with the appropriate scatterplot in Figure 7 through 
Figure 11. Answer using the letter beneath the matching graph. 
Figure 7 
Figure 8 
514     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 119 (book page 525) ---
Figure 9 
Figure 10 
Figure 11 
6 . 
 7 . 
 8 . 
4.8 • Fitting Exponential Models to Data     515


--- PDF page 120 (book page 526) ---
9 . 
 10 . 
Numeric 
11 . To the nearest whole 
number, what is the initial 
value of a population 
modeled by the logistic 
equation 
What is the carrying 
capacity? 
 12 . Rewrite the exponential 
model 
 as an 
equivalent model with 
base 
 Express the 
exponent to four 
significant digits. 
 13 . A logarithmic model is given 
by the equation 
To the nearest hundredth, 
for what value of  does 
14 . A logistic model is given by 
the equation 
 To the 
nearest hundredth, for 
what value of t does 
 15 . What is the y-intercept on 
the graph of the logistic 
model given in the 
previous exercise? 
Technology 
For the following exercises, use this scenario: The population 
 of a koi pond over  months is modeled by the function 
16 . Graph the population 
model to show the 
population over a span of 
years. 
 17 . What was the initial 
population of koi? 
 18 . How many koi will the 
pond have after one and a 
half years? 
19 . How many months will it 
take before there are 
koi in the pond? 
 20 . Use the intersect feature to 
approximate the number 
of months it will take 
before the population of 
the pond reaches half its 
carrying capacity. 
For the following exercises, use this scenario: The population 
 of an endangered species habitat for wolves is modeled 
by the function 
 where  is given in years. 
21 . Graph the population 
model to show the 
population over a span of 
 years. 
22 . What was the initial 
population of wolves 
transported to the habitat? 
23 . How many wolves will the 
habitat have after  years? 
24 . How many years will it take 
before there are 
wolves in the habitat? 
25 . Use the intersect feature to 
approximate the number 
of years it will take before 
the population of the 
habitat reaches half its 
carrying capacity. 
516     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 121 (book page 527) ---
For the following exercises, refer to Table 7. 
x 
1 
2 
3 
4 
5 
6 
f(x) 
1125 
1495 
2310 
3294 
4650 
6361 
Table 7 
26 . Use a graphing calculator 
to create a scatter diagram 
of the data. 
27 . Use the regression feature 
to find an exponential 
function that best fits the 
data in the table. 
28 . Write the exponential 
function as an exponential 
equation with base 
29 . Graph the exponential 
equation on the scatter 
diagram. 
30 . Use the intersect feature to 
find the value of  for 
which 
For the following exercises, refer to Table 8. 
x 
1 
2 
3 
4 
5 
6 
f(x) 
555 
383 
307 
210 
158 
122 
Table 8 
31 . Use a graphing calculator 
to create a scatter diagram 
of the data. 
32 . Use the regression feature 
to find an exponential 
function that best fits the 
data in the table. 
33 . Write the exponential 
function as an exponential 
equation with base 
34 . Graph the exponential 
equation on the scatter 
diagram. 
35 . Use the intersect feature to 
find the value of  for 
which 
For the following exercises, refer to Table 9. 
x 
1 
2 
3 
4 
5 
6 
f(x) 
5.1 
6.3 
7.3 
7.7 
8.1 
8.6 
Table 9 
36 . Use a graphing calculator 
to create a scatter diagram 
of the data. 
37 . Use the LOGarithm option 
of the REGression feature 
to find a logarithmic 
function of the form 
 that best 
fits the data in the table. 
38 . Use the logarithmic 
function to find the value 
of the function when 
39 . Graph the logarithmic 
equation on the scatter 
diagram. 
40 . Use the intersect feature to 
find the value of  for 
which 
4.8 • Fitting Exponential Models to Data     517


--- PDF page 122 (book page 528) ---
For the following exercises, refer to Table 10. 
x 
1 
2 
3 
4 
5 
6 
7 
8 
f(x) 
7.5 
6 
5.2 
4.3 
3.9 
3.4 
3.1 
2.9 
Table 10 
41 . Use a graphing calculator 
to create a scatter diagram 
of the data. 
42 . Use the LOGarithm option 
of the REGression feature 
to find a logarithmic 
function of the form 
 that best 
fits the data in the table. 
43 . Use the logarithmic 
function to find the value 
of the function when 
44 . Graph the logarithmic 
equation on the scatter 
diagram. 
45 . Use the intersect feature to 
find the value of  for 
which 
For the following exercises, refer to Table 11. 
x 
1 
2 
3 
4 
5 
6 
7 
8 
9 
10 
f(x) 
8.7 
12.3 
15.4 
18.5 
20.7 
22.5 
23.3 
24 
24.6 
24.8 
Table 11 
46 . Use a graphing calculator 
to create a scatter diagram 
of the data. 
47 . Use the LOGISTIC 
regression option to find a 
logistic growth model of 
the form 
 that 
best fits the data in the 
table. 
48 . Graph the logistic equation 
on the scatter diagram. 
49 . To the nearest whole 
number, what is the 
predicted carrying capacity 
of the model? 
50 . Use the intersect feature to 
find the value of  for 
which the model reaches 
half its carrying capacity. 
For the following exercises, refer to Table 12. 
0 
2 
4 
5 
7 
8 
10 
11 
15 
17 
12 
28.6 
52.8 
70.3 
99.9 
112.5 
125.8 
127.9 
135.1 
135.9 
Table 12 
51 . Use a graphing calculator 
to create a scatter diagram 
of the data. 
52 . Use the LOGISTIC 
regression option to find a 
logistic growth model of 
the form 
 that 
best fits the data in the 
table. 
53 . Graph the logistic equation 
on the scatter diagram. 
518     4 • Exponential and Logarithmic Functions
Access for free at openstax.org


--- PDF page 123 (book page 529) ---
54 . To the nearest whole 
number, what is the 
predicted carrying capacity 
of the model? 
55 . Use the intersect feature to 
find the value of  for 
which the model reaches 
half its carrying capacity. 
Extensions 
56 . Recall that the general form of a logistic equation 
for a population is given by 
 such 
that the initial population at time 
 is 
 Show algebraically that 
57 . Use a graphing utility to find an exponential 
regression formula 
 and a logarithmic 
regression formula 
 for the points 
and 
 Round all numbers to 6 decimal 
places. Graph the points and both formulas along 
with the line 
 on the same axis. Make a 
conjecture about the relationship of the 
regression formulas. 
58 . Verify the conjecture made in the previous 
exercise. Round all numbers to six decimal places 
when necessary. 
 59 . Find the inverse function 
 for the logistic 
function 
 Show all steps. 
60 . Use the result from the previous exercise to graph 
the logistic model 
 along with its 
inverse on the same axis. What are the intercepts 
and asymptotes of each function? 
4.8 • Fitting Exponential Models to Data     519


--- PDF page 124 (book page 530) ---
Chapter Review 
Key Terms 
annual percentage rate (APR)  the yearly interest rate earned by an investment account, also called nominal rate 
carrying capacity  in a logistic model, the limiting value of the output 
change-of-base formula  a formula for converting a logarithm with any base to a quotient of logarithms with any other 
base. 
common logarithm  the exponent to which 10 must be raised to get 
 
 is written simply as 
compound interest  interest earned on the total balance, not just the principal 
doubling time  the time it takes for a quantity to double 
exponential growth  a model that grows by a rate proportional to the amount present 
extraneous solution  a solution introduced while solving an equation that does not satisfy the conditions of the 
original equation 
half-life  the length of time it takes for a substance to exponentially decay to half of its original quantity 
logarithm  the exponent to which  must be raised to get 
 written 
logistic growth model  a function of the form 
 where 
 is the initial value,  is the carrying capacity, 
or limiting value, and  is a constant determined by the rate of growth 
natural logarithm  the exponent to which the number  must be raised to get 
 
 is written as 
Newton’s Law of Cooling  the scientific formula for temperature as a function of time as an object’s temperature is 
equalized with the ambient temperature 
nominal rate  the yearly interest rate earned by an investment account, also called annual percentage rate 
order of magnitude  the power of ten, when a number is expressed in scientific notation, with one non-zero digit to the 
left of the decimal 
power rule for logarithms  a rule of logarithms that states that the log of a power is equal to the product of the 
exponent and the log of its base 
product rule for logarithms  a rule of logarithms that states that the log of a product is equal to a sum of logarithms 
quotient rule for logarithms  a rule of logarithms that states that the log of a quotient is equal to a difference of 
logarithms 
Key Equations 
definition of the exponential 
function 
definition of exponential 
growth 
520     4 • Chapter Review
Access for free at openstax.org


--- PDF page 125 (book page 531) ---
compound interest formula 
continuous growth formula 
 is the number of unit time periods of growth 
 is the starting amount (in the continuous compounding formula a is replaced 
with P, the principal) 
 is the mathematical constant, 
General Form for the Translation of the Parent Function 
Definition of the logarithmic function 
For 
 if and only if 
Definition of the common logarithm 
For 
 
 if and only if 
Definition of the natural logarithm 
For 
 
 if and only if 
General Form for the Translation of the Parent Logarithmic Function 
The Product Rule for Logarithms 
The Quotient Rule for Logarithms 
The Power Rule for Logarithms 
The Change-of-Base Formula 
One-to-one property for exponential 
functions 
For any algebraic expressions  and  and any positive real number 
where 
 if and only if 
Definition of a logarithm 
For any algebraic expression S and positive real numbers 
 and  where 
 if and only if 
One-to-one property for logarithmic 
functions 
For any algebraic expressions S and T and any positive real number 
where 
 if and only if 
4 • Chapter Review     521


--- PDF page 126 (book page 532) ---
Half-life formula 
If 
 
 the half-life is 
Carbon-14 dating 
 is the amount of carbon-14 when the plant or animal died 
 is the amount of carbon-14 remaining today 
 is the age of the fossil in years 
Doubling time 
formula 
If 
 
 the doubling time is 
Newton’s Law of 
Cooling 
 where 
 is the ambient temperature, 
 and  is the 
continuous rate of cooling. 
Key Concepts 
4.1 Exponential Functions 
• An exponential function is defined as a function with a positive constant other than  raised to a variable exponent. 
See Example 1. 
• A function is evaluated by solving at a specific value. See Example 2 and Example 3. 
• An exponential model can be found when the growth rate and initial value are known. See Example 4. 
• An exponential model can be found when the two data points from the model are known. See Example 5. 
• An exponential model can be found using two data points from the graph of the model. See Example 6. 
• An exponential model can be found using two data points from the graph and a calculator. See Example 7. 
• The value of an account at any time  can be calculated using the compound interest formula when the principal, 
annual interest rate, and compounding periods are known. See Example 8. 
• The initial investment of an account can be found using the compound interest formula when the value of the 
account, annual interest rate, compounding periods, and life span of the account are known. See Example 9. 
• The number  is a mathematical constant often used as the base of real world exponential growth and decay 
models. Its decimal approximation is 
• Scientific and graphing calculators have the key 
 or 
 for calculating powers of 
 See Example 10. 
• Continuous growth or decay models are exponential models that use  as the base. Continuous growth and decay 
models can be found when the initial value and growth or decay rate are known. See Example 11 and Example 12. 
4.2 Graphs of Exponential Functions 
• The graph of the function 
 has a y-intercept at 
 domain 
∞∞
 range 
∞
 and horizontal 
asymptote 
 See Example 1. 
• If 
 the function is increasing. The left tail of the graph will approach the asymptote 
 and the right tail will 
increase without bound. 
• If 
 the function is decreasing. The left tail of the graph will increase without bound, and the right tail will 
approach the asymptote 
• The equation 
 represents a vertical shift of the parent function 
• The equation 
 represents a horizontal shift of the parent function 
 See Example 2. 
• Approximate solutions of the equation 
 can be found using a graphing calculator. See Example 3. 
• The equation 
 where 
 represents a vertical stretch if 
 or compression if 
 of the 
parent function 
 See Example 4. 
• When the parent function 
 is multiplied by 
 the result, 
 is a reflection about the x-axis. 
When the input is multiplied by 
 the result, 
 is a reflection about the y-axis. See Example 5. 
• All translations of the exponential function can be summarized by the general equation 
 See Table 
3. 
• Using the general equation 
 we can write the equation of a function given its description. See 
Example 6. 
522     4 • Chapter Review
Access for free at openstax.org


--- PDF page 127 (book page 533) ---
4.3 Logarithmic Functions 
• The inverse of an exponential function is a logarithmic function, and the inverse of a logarithmic function is an 
exponential function. 
• Logarithmic equations can be written in an equivalent exponential form, using the definition of a logarithm. See 
Example 1. 
• Exponential equations can be written in their equivalent logarithmic form using the definition of a logarithm See 
Example 2. 
• Logarithmic functions with base  can be evaluated mentally using previous knowledge of powers of 
 See Example 
3 and Example 4. 
• Common logarithms can be evaluated mentally using previous knowledge of powers of 
 See Example 5. 
• When common logarithms cannot be evaluated mentally, a calculator can be used. See Example 6. 
• Real-world exponential problems with base 
 can be rewritten as a common logarithm and then evaluated using a 
calculator. See Example 7. 
• Natural logarithms can be evaluated using a calculator Example 8. 
4.4 Graphs of Logarithmic Functions 
• To find the domain of a logarithmic function, set up an inequality showing the argument greater than zero, and 
solve for 
 See Example 1 and Example 2 
• The graph of the parent function 
 has an x-intercept at 
 domain 
∞
 range 
∞∞
vertical asymptote 
 and 
◦ if 
 the function is increasing. 
◦ if 
 the function is decreasing. 
See Example 3. 
• The equation 
 shifts the parent function 
 horizontally 
◦ left  units if 
◦ right  units if 
See Example 4. 
• The equation 
 shifts the parent function 
 vertically 
◦ up  units if 
◦ down  units if 
See Example 5. 
• For any constant 
 the equation 
◦ stretches the parent function 
 vertically by a factor of  if 
◦ compresses the parent function 
 vertically by a factor of  if 
See Example 6 and Example 7. 
• When the parent function 
 is multiplied by 
 the result is a reflection about the x-axis. When the input 
is multiplied by 
 the result is a reflection about the y-axis. 
◦ The equation 
 represents a reflection of the parent function about the x-axis. 
◦ The equation 
 represents a reflection of the parent function about the y-axis. 
See Example 8. 
◦ A graphing calculator may be used to approximate solutions to some logarithmic equations See Example 9. 
• All translations of the logarithmic function can be summarized by the general equation 
See Table 4. 
• Given an equation with the general form 
 we can identify the vertical asymptote 
 for 
the transformation. See Example 10. 
• Using the general equation 
 we can write the equation of a logarithmic function given its 
graph. See Example 11. 
4.5 Logarithmic Properties 
• We can use the product rule of logarithms to rewrite the log of a product as a sum of logarithms. See Example 1. 
• We can use the quotient rule of logarithms to rewrite the log of a quotient as a difference of logarithms. See 
Example 2. 
• We can use the power rule for logarithms to rewrite the log of a power as the product of the exponent and the log 
4 • Chapter Review     523


--- PDF page 128 (book page 534) ---
of its base. See Example 3, Example 4, and Example 5. 
• We can use the product rule, the quotient rule, and the power rule together to combine or expand a logarithm with 
a complex input. See Example 6, Example 7, and Example 8. 
• The rules of logarithms can also be used to condense sums, differences, and products with the same base as a 
single logarithm. See Example 9, Example 10, Example 11, and Example 12. 
• We can convert a logarithm with any base to a quotient of logarithms with any other base using the change-of-base 
formula. See Example 13. 
• The change-of-base formula is often used to rewrite a logarithm with a base other than 10 and  as the quotient of 
natural or common logs. That way a calculator can be used to evaluate. See Example 14. 
4.6 Exponential and Logarithmic Equations 
• We can solve many exponential equations by using the rules of exponents to rewrite each side as a power with the 
same base. Then we use the fact that exponential functions are one-to-one to set the exponents equal to one 
another and solve for the unknown. 
• When we are given an exponential equation where the bases are explicitly shown as being equal, set the exponents 
equal to one another and solve for the unknown. See Example 1. 
• When we are given an exponential equation where the bases are not explicitly shown as being equal, rewrite each 
side of the equation as powers of the same base, then set the exponents equal to one another and solve for the 
unknown. See Example 2, Example 3, and Example 4. 
• When an exponential equation cannot be rewritten with a common base, solve by taking the logarithm of each side. 
See Example 5. 
• We can solve exponential equations with base 
 by applying the natural logarithm of both sides because 
exponential and logarithmic functions are inverses of each other. See Example 6 and Example 7. 
• After solving an exponential equation, check each solution in the original equation to find and eliminate any 
extraneous solutions. See Example 8. 
• When given an equation of the form 
 where  is an algebraic expression, we can use the definition of a 
logarithm to rewrite the equation as the equivalent exponential equation 
 and solve for the unknown. See 
Example 9 and Example 10. 
• We can also use graphing to solve equations with the form 
 We graph both equations 
 and 
 on the same coordinate plane and identify the solution as the x-value of the intersecting point. See Example 
11. 
• When given an equation of the form 
 where  and  are algebraic expressions, we can use the one-
to-one property of logarithms to solve the equation 
 for the unknown. See Example 12. 
• Combining the skills learned in this and previous sections, we can solve equations that model real world situations, 
whether the unknown is in an exponent or in the argument of a logarithm. See Example 13. 
4.7 Exponential and Logarithmic Models 
• The basic exponential function is 
 If 
 we have exponential growth; if 
 we have 
exponential decay. 
• We can also write this formula in terms of continuous growth as 
 where 
 is the starting value. If 
 is 
positive, then we have exponential growth when 
 and exponential decay when 
 See Example 1. 
• In general, we solve problems involving exponential growth or decay in two steps. First, we set up a model and use 
the model to find the parameters. Then we use the formula with these parameters to predict growth and decay. See 
Example 2. 
• We can find the age,  of an organic artifact by measuring the amount, 
 of carbon-14 remaining in the artifact and 
using the formula 
 to solve for  See Example 3. 
• Given a substance’s doubling time or half-time, we can find a function that represents its exponential growth or 
decay. See Example 4. 
• We can use Newton’s Law of Cooling to find how long it will take for a cooling object to reach a desired temperature, 
or to find what temperature an object will be after a given time. See Example 5. 
• We can use logistic growth functions to model real-world situations where the rate of growth changes over time, 
such as population growth, spread of disease, and spread of rumors. See Example 6. 
• We can use real-world data gathered over time to observe trends. Knowledge of linear, exponential, logarithmic, and 
logistic graphs help us to develop models that best fit our data. See Example 7. 
• Any exponential function with the form 
 can be rewritten as an equivalent exponential function with the 
form 
 where 
 See Example 8. 
524     4 • Chapter Review
Access for free at openstax.org
