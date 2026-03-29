```python

text = "Hello World"
n = len(text)

if (n := len(text)) > 5:
    print(f"Long string with {n} characters")
    
if n > 5:
	print(f'Long string with {n} characters')
	

#---------------------------------------------------------------------------------

# Keeps asking as long as the assignment does not equal 'q'
while (user_input := input("Enter a number (or 'q' to quit): ")) != 'q':
    print(f"You entered: {user_input}")
    
#---------------------------------------------------------------------------------

import math

numbers = [1, 2, 3, 4, 5]

# Goal: Get the factorial of a number, but ONLY if the factorial is > 3
# Without walrus, you'd calculate math.factorial(x) twice.

facts = [y for x in numbers if (y := math.factorial(x)) > 3]

print(facts)
# Output: [6, 24, 120] 
# (It skipped 1 and 2 because their factorials are 1 and 2)

fact2 = [y for x in numbers for y in [math.factorial(x)] if y > 3]
print(fact2)

```