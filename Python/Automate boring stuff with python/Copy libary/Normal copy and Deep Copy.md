```python fold:copy()
# shallow copy of the object, dose not give you complete independence, the nested values are still effected. However deepcopy dose.
import copy  
original = [[1,2],3]  
shallow = copy.copy(original)  
deep = copy.deepcopy(original)  
original[0][0] = 99  
print(shallow)  
print(deep)
```