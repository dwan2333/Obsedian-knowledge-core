```python fold:remove(x)
lst = [1, 2, 3, 2]
lst.remove(2)
print(lst)
# remove first occurrence of x 
# returns ValueError if not found
# also work on set
```
```python fold:pop([i])
# Remove and return the item at index `i` (default: last).
# work on set and dict([[Remove Methods]]) as well
lst = [1, 2, 3]
x = lst.pop()
print(x)    
print(lst) 
```
```python fold:clear()
# clear the list 
# also work on set and dict([[Remove Methods]])
lst = [1, 2, 3]
lst.clear()
print(lst)
```
```python fold:del_list[index]
mylist = ['a', 'b', 'c']
del mylist[1]
print(mylist) 
# delete index specified number or words 
# work with other mutable and indexable type (e.g dict, set, dictinonary([[Remove methods]]))
```
