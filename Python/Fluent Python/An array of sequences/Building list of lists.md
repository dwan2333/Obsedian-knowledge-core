```python
l = [[1] * 3 for i in range(3)]  
l[1][1] = 2  
print(l)  
x = [[1]*3]*3  
x[1][1] = 2  
print(x) 

# notice how different the result is 

# the wrong one is equivalent to this code
row = ['_', '_', '_']
board = [row, row, row]

```
**Why this happens (Aliasing):** The text explains that `row = ['_'] * 3` creates a list in memory. When you multiply that list by 3 (`row * 3`), Python **does not create new lists**. It just creates three **references** (pointers) to that exact same original list.