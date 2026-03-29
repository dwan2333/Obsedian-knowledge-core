```python fold:pop(key[,default])
# removes the item with the given key and returns its value
# work on list([[Remove Items]])(list has no default value) and set as well
d = {'a': 1, 'b': 2}
val = d.pop('a')
print(val)  
print(d)
```
```python fold:popitem()
# removes and returns the last inserted key-value pair.
d = {'a': 1, 'b': 2}
print(d.popitem())  
print(d)
```
```python fold:clear()
# removes all items from the dictionary
# also work on list([[Remove Items]]) and set
d = {'a': 1, 'b': 2}
d.clear()
print(d)
```
```python fold:del_dict[key]
# delete indicated key
# also work on set and list([[Remove Items]])
dict = {'apple':2, 'banana':2}
del dict['banana']
print(dict)
```
