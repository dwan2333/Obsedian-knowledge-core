The `match`/`case` statement (introduced in Python 3.10) is often called "Structural Pattern Matching."

While it looks like a "Switch" statement from other languages (checking specific values), in Python it is much more powerful. It doesn't just check the **value**; it checks the **shape** of the data and unpacks it for you—exactly like the tuple unpacking you were just reading about.

Here is how it works, from basic to advanced.

### 1. The Basic "Switch" (Value Matching)

At its simplest, it replaces a long chain of `if/elif/else` statements.

```python

status = 404

match status:
    case 200:
        print("Success!")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown status")  # The _ is the "else" (wildcard)

```

### 2. The "Shape" Matcher (The Real Power)

This is where it connects to the **unpacking** you just learned. You can match the _structure_ of a tuple or list and assign variables instantly.

Imagine you have a point that could be 2D `(x, y)` or 3D `(x, y, z)`.
```python
point = (10, 20)

match point:
    # Python checks: Is this a tuple with exactly 3 items?
    case (x, y, z):
        print(f"3D Point: x={x}, y={y}, z={z}")

    # Python checks: Is this a tuple with exactly 2 items?
    case (x, y):
        print(f"2D Point: x={x}, y={y}")  # This runs!
        
    case _:
        print("Not a point")

```

### 3. Matching with "Guards" (Adding Logic)

You can add an `if` statement directly inside a case to make it very specific.
```python
# A record: (Name, Role, AccessLevel)
user = ("Alice", "Admin", 5)

match user:
    case (name, "Admin", level) if level > 3:
        print(f"Super Admin: {name}")
    
    case (name, "Admin", level):
        print(f"Regular Admin: {name}")

    case (name, "User", _):
        print(f"User: {name}")

```

### 4. Matching Objects (Classes)

You can even match against class objects, not just tuples.

```python

match current_event:
    case Click(position=(0, 0)):
        print("Clicked the corner")
    case KeyPress(key="Enter"):
        print("Pressed Enter")

``` 

### 5. What FAILS: Sequence Unpacking

You **cannot** use `match/case` to break a string apart into characters, even though strings are technically "sequences" in Python.

**Why?** The Python developers decided this would be too dangerous. If strings were treated as sequences, a pattern meant to catch a list of two items (`case [x, y]`) would accidentally catch any 2-letter word (like "hi" or "no").

```python

command = "go"

match command:
    # THIS WILL FAIL (Python skips it)
    case [char1, char2]:
        print(f"First letter: {char1}")
        
    # THIS WILL FAIL (Python skips it)
    case (first, second):
        print(f"First letter: {first}")

    case _:
        print("Strings are not sequences in match/case!")

```

If you _really_ want to match a string character-by-character, you must manually convert it to a list first.

```python

command = "go"

match list(command):   # <--- Convert string to list ['g', 'o']
    case ['g', 'o']:
        print("Go command received")
    case [x, y]:
        print(f"Two letter command: {x} and {y}")

```

so remember instances of str, bytes, and bytearray are not handled as sequences in the context of match/case. A match subject of one of those types is treated as an 'atomic' value - like the integer 987 is treated as one value, not a sequence of digit.

```python
command = "quit"

match command:
    case "start":         # <--- VALID: Checks if string equals "start"
        print("Starting...")
    case "quit":          # <--- VALID: Checks if string equals "quit"
        print("Quitting...")

```

### 6. _ symbol is special in patterns
_ symbol only  matches any single item in that position, but it is never bond to the value of the matched item. Also, the _ is the only variable that can appear more than once in a pattern.
```python
match message:
    # Matches ['LED', 1, 50] AND ['LED', 99, 50]
    case ['LED', _, intensity]: 
        print(f"Setting brightness to {intensity}")

```

 matches multiple items in the position you want
```python

scores = [10, 50, 60, 20, 99]

match scores:
    case [first, *_, last]:
        print(f"Start: {first}, End: {last}")
        # It ignores [50, 60, 20] completely.
        
# *_ matches 0 or more items
```

### 7, We can make pattern more specific by adding type information.
```python

case [str(name), _, _, (float(lat),float(lon))]

``` 

### 8, Example  of why pattern matching is clearer and easier to write 
![[Pasted image 20251213152833.png]]
![[Pasted image 20251213152847.png]]
1. The `lambda` Problem (Missing Parentheses)

**Code:** `(_, parms, *body) = exp`

- **What you want:** `parms` to be a list, e.g., `['x', 'y']`.
    
- **The Reality:** This unpacking line accepts **anything**.
    
    - If the user types valid code `['lambda', ['x'], 'body']`, `parms` becomes `['x']` (List).
        
    - If the user types invalid code `['lambda', 'x', 'body']`, `parms` becomes `'x'` (String).
        

**The Result:** The code does **not** crash here. It continues running with bad data. It will only crash later, likely inside the `Procedure` class when it tries to loop over `parms`. It might try to treat the string `'x'` as a list of arguments, leading to weird bugs where the argument name is a single letter `x`.

The `match` version `[*parms]` prevented this by enforcing the list structure immediately.

2. The `define` Problem (Not a Symbol)

**Code:** `(_, name, value_exp) = exp`

- **What you want:** `name` to be a `Symbol`.
    
- **The Reality:** `name` becomes whatever is in that second slot.
    
    - If the user types `['define', 42, 100]`, then `name` becomes the integer `42`
![[Pasted image 20251213153113.png]]