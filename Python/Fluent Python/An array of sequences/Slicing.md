### 1, Slice() function 
![[Pasted image 20251213154006.png]]
![[Pasted image 20251213154017.png]]
- slice() allow you to name so It is easier to read the code

### 2, Assigning to slices
```python

l = [1,2,3,4,5]
try:
	l[1:2] = 100
# this gives you typeError bc the left hand side is not iterable 
except Type Error:
	l[1:2] = [100]
	
print(l)

```