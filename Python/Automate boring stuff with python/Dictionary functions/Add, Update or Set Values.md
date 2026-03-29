```python fold:update([other])
# similar to extend(iterable) in [[Add or Insert Items]] 
# update the dictionary with key-value from another dict or iterable
# also work on set
d = {'a': 1}
d.update({'b': 2, 'c': 3})
print(d)
```
```python fold:setdefault(key[,default])
# returns the value if key exists; set it to default if not
d = {'a': 1}
d.setdefault('b', 99)
print(d)
d.setdefault('a',2)
print(d)
```