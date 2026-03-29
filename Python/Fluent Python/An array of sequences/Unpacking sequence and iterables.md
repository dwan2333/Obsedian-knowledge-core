```python
# some examples that I found confusing in the book and worth knowing
divmod(20,8)
t = (20,8)
print(*t)

import os 

_, filename = os.path.split('/home/luciano/.ssh/id_rsa.pub')
print(filename)

```

**Using * to grab excess items**
```python
a,b,*rest = range(5)
print(a,b,rest)
a,b,*rest = range(2)
print(a,b,rest)
```

**Unpacking with * in Function Calls and Sequence Literals**
```python
def fun(a,b,c,d, *rest):
	return a,b,c,d,rest
	
# python would always return a tuple for the *rest

print(fun(1,2,3,4,5,6))

# (*[1,2],3,4,*range(5,8)) * dissovle the sequences and make them regular (1,2,3,4,5,6,7)


```
--------------------------------------------------------------------------


**Quick Hint**
### 1. The Goal: "Unpack and Verify"

Imagine you ask a database for a user's ID. You expect a list containing exactly one item: `[105]`.

You _could_ just get the item by index:


```python
# The "Lazy" Way
results = [105]
user_id = results[0]  # user_id is 105
```

**The Problem:** If the database bugs out and returns an empty list `[]` or a list with two users `[105, 106]`, your code might keep running with bad data or crash later in a confusing way.

**The Solution (The Code in the text):**


```python
# The "Safe" Way
[user_id] = results
```

This syntax does two things at once:
- **Extracts:** It grabs the `105` out of the list and puts it in `user_id`.
- **Verifies:** If `results` has 0 items or 2+ items, Python **crashes immediately** with a `ValueError`. This is good! It alerts you instantly that your "single record" assumption was wrong.


### 3. The "Tuple Trap" (Why use lists?)

The author argues that using list syntax `[x] = ...` is better than tuple syntax `(x) = ...` for this specific job because of a **syntax quirk**.

**The Quirk:** In Python, parentheses `()` are used for two things: **Tuples** and **Math Grouping**.

- `(x)` is just the variable `x` (Math grouping).
    
- `(x,)` is a tuple containing `x` (Note the comma!).
    

**The Danger:** If you try to write the "safety trick" using tuples and forget the comma:


```python
# WRONG (Math grouping)
(record) = query_result
# This effectively just says: record = query_result
# Result: 'record' becomes the whole list [105]. It did NOT unpack it.
```


```python
# CORRECT (Tuple unpacking)
(record,) = query_result
# Result: 'record' becomes 105.
```
