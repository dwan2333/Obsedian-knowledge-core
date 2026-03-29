```python fold:copy()
# returns a shallow copy of the dictionary (orginal is kept)
# also work on list([[Copy or Duplicate the List]]) and set
original = {'x': 10}
copy_d = original.copy()
print(copy_d)
print(original)
```
```python fold:fromkeys(keys,value)
# creates a new dictionary with given keys and a shared value
keys = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys, 0)
print(new_dict)
```