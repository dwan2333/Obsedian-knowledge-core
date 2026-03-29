```python
numbers = [1, 2, 3, 4]

# Using a standard function
def double(x):
    return x * 2

# Wrap in list() to see the result immediately
result = list(map(double, numbers))

print(result) 
# Output: [2, 4, 6, 8]

#----------------------------------------------------------------------------------

numbers = [2, 5, 8, 1, 10]

# Using a 'lambda' (anonymous) function for brevity
# Keep x if x is greater than 5
result = list(filter(lambda x: x > 5, numbers))

print(result)
# Output: [8, 10]


#----------------------------------------------------------------------------------

```