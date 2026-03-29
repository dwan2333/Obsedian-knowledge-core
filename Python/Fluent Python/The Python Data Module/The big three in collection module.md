```python 
from collections import Counter  
  
letters = "aaabbc"  
counts = Counter(letters)  
  
print(counts)  
# Output: Counter({'a': 3, 'b': 2, 'c': 1})  
  
# BONUS: Get the most common item instantly  
print(counts.most_common(1))   
# Output: [('a', 3)]

server_A = Counter({'sword': 1, 'potion': 5, 'gold': 100})  
server_B = Counter({'sword': 2, 'potion': 1, 'gold': 500, 'shield': 1})  
  
# Use the bitwise OR operator '|' to get the union (MAX value)  
master_profile = server_A | server_B  
  
print(master_profile)
# Output: Counter({'gold': 500, 'potion': 5, 'sword': 2, 'shield': 1})
#=================================================================================

from collections import defaultdict  
  
grades = [('A', 'Alice'), ('B', 'Bob'), ('A', 'Anna'), ('B', 'Billy')]  
  
# "If a key is missing, make a new list"  
by_grade = defaultdict(list)  
  
for grade, student in grades:  
    # No checks needed! Just append.  
    by_grade[grade].append(student)  
  
print(by_grade)  
# Output: defaultdict(<class 'list'>, {'A': ['Alice', 'Anna'], 'B': ['Bob', 'Billy']})

#=================================================================================

from collections import namedtuple  
  
# 1. Create the class  
Point = namedtuple('Point', ['x', 'y'])  
  
# 2. Make the object  
p = Point(10, 20)  
  
# 3. Readable access!  
print(p.x)  # Clear  
print(p.y)  # Clear
```