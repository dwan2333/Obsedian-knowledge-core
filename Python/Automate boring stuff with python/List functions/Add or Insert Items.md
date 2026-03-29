```python fold:append(x)
#Add an item to the end of the list
lst = [1, 2]
lst.append(3)
print(lst) 
```
```python fold:extend(iterable)
#Add all items from another iterable (e.g., list).
#similar to the update([other]) in [[Add, Update or Set Values]] for set and dict
lst = [1, 2]
lst.extend([3, 4])
print(lst)  
```
```python fold:insert(index,x)
lst = [1, 3]
lst.insert(1, 2)
print(lst)
#Insert an item at a specific index.
```