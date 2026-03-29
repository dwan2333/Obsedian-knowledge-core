```python 
import pizza # import the entile pizza.py file as module
pizza.somefuntion() # you would need pizza as start

from pizza import specific_function # knwo you only need do not need pizza
specific_function()

# you could give alias 
import pizza as pz
pz.somefunction()
from pizza import specific_function as sf
sf()

# import everyfunction in the other py file 
from pizza import *
```