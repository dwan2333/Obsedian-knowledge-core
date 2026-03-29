```python 
# connects multiple lists (or other iterables) together into one continuous stream
import itertools

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

# Chains them into one long iterator
combined = itertools.chain(list1, list2, list3)

print(list(combined))
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

#----------------------------------------------------------------------------------
# Generates all possible distinct groupings of items from a list (order doesn't matter).

items = ['A', 'B', 'C']

# Find all groups of 2
combos = itertools.combinations(items, 2)

for pair in combos:
    print(pair)
    
# Output:
# ('A', 'B')
# ('A', 'C')
# ('B', 'C')

#----------------------------------------------------------------------------------
# work like combinations but with one distinct difference is that order matters over here 

runners = ['Alice', 'Bob', 'Charlie']

# We need all ordered pairs of length 2 (Winner, Runner-up)
# Note: Python uses the argument name 'r', but it is the same as your 'k'
perms = itertools.permutations(runners, r=2)

for p in perms:
    print(p)

# Output:
# ('Alice', 'Bob')      <-- Alice wins
# ('Alice', 'Charlie')
# ('Bob', 'Alice')      <-- Bob wins (Distinct from the first one!)
# ('Bob', 'Charlie')
# ('Charlie', 'Alice')
# ('Charlie', 'Bob')

```
```python
#----------------------------------------------------------------------------------
# groupby()
''''1. How it works**

It scans a list from top to bottom. Every time the "key" changes, it creates a new group.

- If your list is `[A, A, B, B, A]`, `groupby` sees **3** groups:
    
    1. `A, A`
        
    2. `B, B`
        
    3. `A` (It treats this as a new group because it's separated from the first As).
        
- If you sort it first to `[A, A, A, B, B]`, `groupby` sees **2** groups:
    
    1. `A, A, A`
        
    2. `B, B`'''
       
# Here is an example 
import itertools

# --- STEP 1: PREPARE THE DATA ---
data = [1, 3, 2, 4]

# We need a function that tells Python how to group.
# Returns True if even, False if odd.
def check_even(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

# SORT FIRST! 
# We sort by the same logic we plan to group by.
# After sorting, 'data' becomes: [1, 3, 2, 4] -> [1, 3, 2, 4] 
# Wait, standard sort sorts by value (1,2,3,4). 
# But we want to sort by "Evenness". 
# So [1, 3] are Odd, [2, 4] are Even.
data.sort(key=check_even) 
# Now data looks like: [1, 3, 2, 4] (Depending on sort stability, but all Odds are together and all Evens are together)
# Let's say it resulted in: [1, 3, 2, 4] -> [1, 3, 2, 4] is actually wrong for simple sort.
# Let's force the sort order to be clear:
data = [1, 3, 2, 4, 5, 6]
data.sort(key=check_even)
# Now data is effectively: [1, 3, 5, 2, 4, 6] 
# (All "Odds" first, then all "Evens" second)

# --- STEP 2: GROUPBY ---
# Python scans the sorted list.
# It sees 'Odd', 'Odd', 'Odd' -> Bundles them.
# It sees 'Even', 'Even', 'Even' -> Bundles them.
groups = itertools.groupby(data, key=check_even)

# --- STEP 3: UNPACKING (THE TRICKY PART) ---
print("Start Loop:")

# 'groups' is an iterator. We loop through it.
# In every loop, we get two things:
#   1. key_category: The result of check_even (e.g., "Odd")
#   2. group_iterator: A specialized iterator containing the actual numbers (1, 3, 5)
for key_category, group_iterator in groups:
    
    print(f"  Found a group for: {key_category}")
    
    # CRITICAL: 'group_iterator' is not a list yet. It's a "stream".
    # We must convert it to a list to see what's inside.
    content = list(group_iterator)
    
    print(f"  The items inside are: {content}")
    print("  ---")

```

```python
'''computes the Cartesian Product of input iterables.

In plain English: It creates **every possible combination of items between two (or more) lists. It matches **everything with everything.'''

import itertools

mains = ['Burger', 'Pizza']
sides = ['Fries', 'Salad']

# Create the product of the two lists
menu = itertools.product(mains, sides)

for meal in menu:
    print(meal)

# Output:
# ('Burger', 'Fries')
# ('Burger', 'Salad')
# ('Pizza', 'Fries')
# ('Pizza', 'Salad')

# the old way of nested loops 
colors = ['Red', 'Blue']
sizes = ['S', 'M', 'L']

for c in colors:
    for s in sizes:
        print(c, s)
        
# the new way with itertools product
from itertools import product

colors = ['Red', 'Blue']
sizes = ['S', 'M', 'L']

# It does exactly the same thing, but looks cleaner
for c, s in product(colors, sizes):
    print(c, s)
    
# the repeat arguments if you waant product of the object itself
import itertools

# Coin toss: Heads (H) or Tails (T)
# We flip the coin 3 times. What are the possible outcomes?
outcomes = itertools.product(['H', 'T'], repeat=3)

for outcome in outcomes:
    print(outcome)

# Output:
# ('H', 'H', 'H')
# ('H', 'H', 'T')
# ('H', 'T', 'H')
# ...
# ('T', 'T', 'T')
```