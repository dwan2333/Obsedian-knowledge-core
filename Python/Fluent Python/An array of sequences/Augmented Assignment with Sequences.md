```python 
l = [1,2,3]
print(id(l))
l *= 2 
print(l)

# for tuple a new tuple is created 
t = (1,2,3)
print(id(t))
t *= 2 
print(id(t))

# augmented operators  += have special method that the python interpreter runs which is __iadd__. In the case of when __iadd__ is not included, the python interpreter automatically run  __add__ speical method. a+= b has the same effect as a = a + b, but one thing different is that the expresstion a + b is evaluated at first. Same as __imul__. 

# avoid putting mutable object into immutable ones

```
