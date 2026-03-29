```python fold:Creating_new_folder
import os
os.makedirs('C:\\delicious\\walnut\\waffles')
# os.mkdir() only makes the final directory in the path; parents must already exist.   
#os.makedirs() will create all missing parent directories: parents = True, exist_ok = True (do not create error if directory already exists)
```