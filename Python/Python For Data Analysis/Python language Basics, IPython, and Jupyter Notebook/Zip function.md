```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Combine them
zipped = zip(names, ages)

# Convert to list to see the result
print(list(zipped))
# Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# common use
products = ["Laptop", "Mouse", "Keyboard"]
prices = [1000, 25, 50]

for product, price in zip(products, prices):
    print(f"The {product} costs ${price}")

# Output:
# The Laptop costs $1000
# The Mouse costs $25
# The Keyboard costs $50

# creating a dict
keys = ["name", "age", "city"]
values = ["Emma", 28, "New York"]

my_dict = dict(zip(keys, values))
print(my_dict)
# Output: {'name': 'Emma', 'age': 28, 'city': 'New York'}


# Unzip
pairs = [('Alice', 1), ('Bob', 2), ('Charlie', 3)]

names, numbers = zip(*pairs)

print(names)   # ('Alice', 'Bob', 'Charlie')
print(numbers) # (1, 2, 3)

```