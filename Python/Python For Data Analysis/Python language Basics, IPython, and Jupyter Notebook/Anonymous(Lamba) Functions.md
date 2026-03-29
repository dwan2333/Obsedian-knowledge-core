```python
# We define it and use it immediately or assign it to a variable
double = lambda x: x * 2

print(double(5)) # Output: 10

# Why use them ?
students = [('Alice', 88), ('Bob', 95), ('Charlie', 70)]

# Sort by the second item (the score)
# "For every student 'x', use 'x[1]' as the sorting key"
students.sort(key=lambda x: x[1])

print(students)
# Output: [('Charlie', 70), ('Alice', 88), ('Bob', 95)]

```