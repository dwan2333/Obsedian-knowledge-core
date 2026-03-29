

Think of it as the **"Constitution of Data Structures"** in Python. It defines the rules and interfaces that all containers (like Lists, Sets, and Dictionaries) must follow to be considered "collections."

### 1. The Hierarchy (The Map)

In Python, all data structures are built from small, mix-and-match capabilities.

- If you can be looped over, you are an **Iterable**.
    
- If you can report your length, you are **Sized**.
    
- If you can check if an item is inside you (`x in y`), you are a **Container**.
    

If you combine all three, you get the definition of a **Collection**.


--------------------------------------------------------------------------

An **Abstract Base Class (ABC)** is essentially a **"Strict Blueprint"** or a **"Contract"** for other classes.

It is a class that you **cannot** use to build an object directly. You can only use it as a parent to organize other classes.

#### A. Enforcement (The "Strict Boss")

If you create a normal parent class, the child classes can be lazy and ignore the parent's methods. An **ABC** forces the child classes to do their homework. If a child class doesn't implement the specific methods defined in the ABC, **Python will refuse to run.**

**Example:** We define an ABC called `Animal`. We say: "All animals MUST have a `speak` method."
```python
from abc import ABC, abstractmethod  
  
  
# 1. The Abstract Base Class (The Blueprint)  
class Animal(ABC):  
  
    @abstractmethod  
    def speak(self):  
        pass  # No logic here! Just a placeholder.  
  
  
# 2. The "Lazy" Child (This will crash!)  
class Fish(Animal):  
    def swim(self):  
        print("I am swimming")  
    # Missing the 'speak' method!  
  
  
# 3. The "Good" Child (This works)  
class Dog(Animal):  
    def speak(self):  
        print("Woof!")  
  
  
# --- Let's try to use them ---  
  
dog = Dog()  # ✅ Works: Dog followed the rules.  
fish = Fish()  
# ❌ CRASH: TypeError: Can't instantiate abstract class Fish # with abstract method speak.

```

#### B. Identification (The "Is-A" Check)

This relates back to the **Collection API** we just discussed. ABCs allow you to check if an object behaves in a certain way, regardless of what its actual class name is.

- `isinstance(my_obj, Sequence)` checks: "Does this object behave like a list (ordered items)?"
    
- It doesn't care if it's a `list`, a `tuple`, or a custom `Vector`. If it follows the rules of the `Sequence` ABC, it passes the test


--------------------------------------------------------------------------
Once you have a generic "Collection," the API splits into three main "Tribes" depending on how you organize data:

| **The Tribe (ABC)** | **The Rule**                                                                               | **The Concrete Examples**            |
| ------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------ |
| **`Sequence`**      | **Order matters.** Items are stored 1, 2, 3. You access them by integer index `[0]`.       | `list`, `tuple`, `str`, `bytes`      |
| **`Mapping`**       | **Labels matter.** Items are stored as Key $\to$ Value. You access them by key `['name']`. | `dict`, `defaultdict`, `OrderedDict` |
| **`Set`**           | **Uniqueness matters.** No duplicates allowed. Order usually doesn't matter.               | `set`, `frozenset`                   |


--------------------------------------------------------------------------
### 3. Why is this useful? (Duck Typing vs. Interfaces)

You rarely _inherit_ from these (unless you are building a custom data structure), but you often use them to **check types** in a flexible way.

**The "Bad" Way (Too Specific):** This function _only_ works with lists. If I pass a tuple, it fails or is rejected.


```python
def process_data(data):
    if isinstance(data, list): # ❌ Too rigid
        print("Processing list...")
```

**The "API" Way (Polymorphic):** This function works with Lists, Tuples, or even custom objects, as long as they follow the rules of a `Sequence`.


```python
from collections.abc import Sequence

def process_data(data):
    if isinstance(data, Sequence): # ✅ Flexible
        print(f"Processing sequence of length {len(data)}")
```

imagine the ABC as border controls that select which collection an object belong . 

![[Pasted image 20251211011200.png]]