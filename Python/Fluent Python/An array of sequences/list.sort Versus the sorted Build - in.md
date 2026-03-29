```python

# list.sort() dose not create a new list, it modifies the current one that you have. You can see this because this is an important Pyuthon API convention: functions or method that that change an object place shbould return None to make it to the caller

l  = [4,1,6,2,2]  
print(l.sort()) # it returns None , or for example random.shuffle()


# in contrast, the build in function sorted creates a new list and returns it. 

# both list.sort and sorted() take two option key word arguements

	# reverse (the default is False)
	# key one argument function that will pbe applied to each item to produce its sorting key.
```