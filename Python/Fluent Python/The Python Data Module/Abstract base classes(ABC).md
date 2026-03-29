An Abstract Base Class (ABC) is essentially a **"Blueprint"** or a **"Job Description"** for other classes. It defines a set of rules (methods) that a class _must_ follow to be considered a specific "type" of thing.

In the context of the Python `collections.abc` module, ABCs are used to **identify capability** rather than specific class names.

### 1. The Concept: "Is a" vs. "Acts like a"

Normally, you might check if a variable is a list like this:

Python

``` python
# Bad way (Too specific)
if type(my_var) == list:
    print("It is a list")
```

The problem? If you create a custom class that _acts_ exactly like a list (you can loop over it, index it, count it), the check above fails because your class isn't strictly named `list`.

**The ABC Way (Better):**

You use `collections.abc` to ask about **capability**.

Python

```python
from collections.abc import Sequence

# Good way (Checks behavior)
if isinstance(my_var, Sequence):
    print("It acts like a list/tuple/string")
```

### 2. How `collections.abc` Works (The "Identification")

The `collections.abc` module provides standard "Blueprints" for common Python behaviors. When you check `isinstance(obj, ABC)`, Python answers `True` if your object fits the blueprint, even if you never explicitly inherited from it.

This is called **"Goose Typing"** (a stricter version of Duck Typing).

Here are the most common ABCs used for identification:

| **ABC Name**          | **What it identifies**             | **Required Methods**                 |
| --------------------- | ---------------------------------- | ------------------------------------ |
| **`Iterable`**        | Can I loop over it?                | `__iter__`                           |
| **`Container`**       | Can I use `in` operator?           | `__contains__`                       |
| **`Sized`**           | Can I use `len()`?                 | `__len__`                            |
| **`Sequence`**        | Is it an ordered list? (Read-only) | `__getitem__`, `__len__`             |
| **`MutableSequence`** | Is it a list I can change?         | `__setitem__`, `del`, `insert`       |
| **`Mapping`**         | Is it like a Dictionary?           | `__getitem__`, `__iter__`, `__len__` |

### 3. Code Example: The "Magic" Identification

Notice in this example, `Myitems` does **not** inherit from `Sized` or `Iterable`. But Python's `collections.abc` creates a "virtual" relationship because the methods exist.

Python

``` python
from collections.abc import Sized, Iterable

class MyItems:
    def __init__(self):
        self.data = [1, 2, 3]

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

my_obj = MyItems()

# 1. Check if it has a length
# Python checks: Does MyItems have __len__? YES.
print(isinstance(my_obj, Sized))     # Output: True

# 2. Check if it can be looped over
# Python checks: Does MyItems have __iter__? YES.
print(isinstance(my_obj, Iterable))  # Output: True
```

### 4. How does it technically work? (`__subclasshook__`)

You might wonder: _"How does `isinstance` return True if I didn't inherit from that class?"_

The standard ABCs in Python implement a special magic method called `__subclasshook__`.

When you run `isinstance(my_obj, Iterable)`, the `Iterable` class runs logic similar to this:

> "I don't care who your parent is. If you have an `__iter__` method defined, I will certify you as an `Iterable`."

### Summary

- **Abstract Base Classes** define a standard interface (a contract).
    
- **`collections.abc`** lets you check if an object **satisfies that contract**.
    
- It allows you to write polymorphic code that works with _any_ object (List, Tuple, Custom Class) as long as it behaves the right way.