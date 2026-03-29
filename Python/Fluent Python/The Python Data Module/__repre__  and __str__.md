```python 
class Product:  
    def __init__(self, name, price):  
        self.name = name  
        self.price = price  
  
    # 1. THE DEVELOPER VIEW (Code-accurate)  
    def __repr__(self):  
        return f"Product(name =' {self.name}', price = {self.price})"  
  
    # 2. THE USER VIEW (Pretty text)  
    def __str__(self):  
        return f"The item '{self.name}' costs ${self.price:.2f}"  
  
# --- Usage ---  
p = Product("Coffee", 5.5)  
  
# Triggering __repr__ (The Console / Debugger)  
# This usually happens when you type the variable alone  
print(repr(p))   
# Output: Product(name='Coffee', price=5.5)
# The idea is to be unambigouse (idealy - copy pastable code). Mostly for developers.
  
# Triggering __str__ (The Print function)  
print(p)  
# Output: The item 'Coffee' costs $5.50
# The idea is for it to be readble, mostly for end users 

```