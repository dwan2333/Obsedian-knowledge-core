```python

def get_numbers_generator():
    for i in range(1, 4):
        yield i  # Pauses here, hands back 'i', and waits

# It returns a "generator object", not a list
gen = get_numbers_generator()

# t **pauses** its execution, hands out one value to the caller, and **saves its state** (variables, position in code). When you call it again, it resumes exactly where it left off.

# yeild is often used for functions to become generators meaning taht the function has became iterable 

for i in get_numbers_generator():
	print(i)
	
print(get_numbers_generator())

# another way of making a generator is by using a generator expression 
gen = (x ** 2 for x in range(100)) # the paraentheses make the object become iterable 

sum (x ** 2 for x in range(5))

dict((i, i **2) for i in range(5))

```