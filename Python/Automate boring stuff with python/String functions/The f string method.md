```python fold:f_string_methods
# Basic examples
name = "Alice"
age = 20
print(f"My name is {name} and I am {age} years old.")
print()

# Formate Numbers 
pi = 3.14159
print(f"Pi rounded to 2 digits: {pi:.2f}")
print()
num = 1230000
print(f"{num:.2e}")
print()
num = 100
print(f'{num:.1%}') 
print()

# Alignment and Padding
print(f'{'A':<5}') #Left-align
print(f'{'A':>5}') # Right-align
print(f'{'A':^5}') # center align
print(f'{5:03}') #padwith numbers
print()

# Expression inside
print(f"2 + 2 = {2 + 2}")
users = ["Alice", "Bob"]
print(f"First user: {users[0]}")
print()

# With dictionaris
user = {"name": "Alice", "age": 21}
print(f"{user['name']} is {user['age']} years old.")
print()

# Multiline f-string
name = "Bob"
print(f"""
Hello, {name}!
Welcome to the system.
""")

# Integeer format
x = 255
print(f"{x:x}")   # ff (hex lowercase)
print(f"{x:X}")   # FF (hex uppercase)
print(f"{x:o}")   # 377 (octal)
print(f"{x:b}")   # 11111111 (binary)
print()

# Using = to show varibale and value
score = 80
print(f'{score=}')
```