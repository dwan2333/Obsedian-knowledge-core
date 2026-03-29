```python
# Generator expression saves memory becasue it yeilds itmes one by one using the iterator protocol instead of building a whole list just to feed another constructor

for i in (x for x in range(2)):
	print(i)
	
l = [1,2,3,4]
for i in l:
	print(i)

```