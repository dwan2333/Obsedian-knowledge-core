```python fold:get(key[,deault])
# returns the value for key or default if not found
d = {'a': 1}
print(d.get('a'))      
print(d.get('b', 0))
```
``` python fold:keys()
# Returns a view of the dictionary's keys
d = {'a': 1, 'b': 2}
print(d.keys())
```
```python fold:values()
#returns a vew of the dict's values
d = {'a': 1, 'b': 2}
print(d.values())
```
```python fold:items()
# return keys and items at the same time
d = {'a': 1, 'b': 2}
print(d.items())
```