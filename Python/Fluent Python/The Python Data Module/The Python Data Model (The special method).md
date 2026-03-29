```python

class Liar:  
    def __init__(self):  
        # This object has THOUSANDS of items in it  
        self.huge_list = [1] * 10000  
  
    # But we make the special method tell a lie  
    def __len__(self):  
        return 3  
  
my_liar = Liar()  
  
# If len() scanned the object, it would find 10,000 items.  
# But it doesn't. It just asks __len__.  
print(len(my_liar))

# This is what meant by the special method. Imagine len() as a manager in a warehouse that need __len__ the workers to get information of how many boxes there is. If __len__ is not defined then python raises error
```
![[Pasted image 20251204165816.png]]
- Different corresponding special methods forms the Python Data Model so that we could interact with objects in different ways 