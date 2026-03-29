```python
import math  
  
class Vector:  
  
    def __init__(self, x,y):  
        self.x = x  
        self.y = y  
  
    def __repr__(self):  
        return f'Vector(x = {self.x!r}, y = {self.y!r})'   # !r shows the what is being putted inside Vector() it could be a string for example Vector('1', 2) good habbit for debugging
  
    def  __abs__(self):  
        return math.hypot(self.x, self.y)  
  
    def __bool__(self):  
        return bool(abs(self))  
  
    def __add__(self, other):  
        x = self.x + other.x  
        y = self.y + other.y  
        return Vector(x,y)  
  
    def __mul__(self, scalar):  
        return Vector(self.x * scalar, self.y * scalar)
        
    def __str__(self):
	    return f'The vector coordinates are {self.x}, {self.y}'

```

**String representation** 
	