```python
s = {1, 2, 3}  
  
# 1. add()  
s.add(4)  
print(f"After add(4):    {s}")   
# Output: {1, 2, 3, 4}  
  
# 2. update(|=)  
s.update([5, 6, 7])  
print(f"After update:    {s}")   
# Output: {1, 2, 3, 4, 5, 6, 7}  
  
# 3. remove()  
s.remove(7)  
print(f"After remove(7): {s}")   
# Output: {1, 2, 3, 4, 5, 6}  
# s.remove(99)  # <--- This would crash with KeyError  
  
# 4. discard()  
s.discard(99)   # <--- Safe! Does nothing if 99 isn't there.  
print(f"After discard:   {s}")  
# Output: {1, 2, 3, 4, 5, 6}  
  
# 5. pop()  
removed_item = s.pop()  
print(f"Popped item:     {removed_item}")  
print(f"Set after pop:   {s}")  
# Output: Popped item: 1 (Could be any number!), Set: {2, 3, 4, 5, 6}  
  
# 6. clear()  
s.clear()  
print(f"After clear:     {s}")  
# Output: set()

#---------------------------------------------------------------------------------

# Math Matical operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}  
  
# 1. union ( | )  
print(set_a.union(set_b))  
# Output: {1, 2, 3, 4, 5, 6}  
  
# 2. intersection ( & )  
print(set_a.intersection(set_b))  
# Output: {3, 4}  
  
# 3. difference ( - )  
# Note: Order matters! (A - B) vs (B - A)  
print(set_a.difference(set_b))  
# Output: {1, 2} (Everything in A that isn't in B)  
  
# 4. symmetric_difference ( ^ )  
print(set_a.symmetric_difference(set_b))  
# Output: {1, 2, 5, 6} (Everything EXCEPT the shared 3, 4)

a = {1, 2, 3}  
b = {2, 3, 4}  
  
# Remove items from 'a' if they exist in 'b'  
a.difference_update(b)  
  
print(a)  
# Output: {1} (2 and 3 were removed because they were in b)



#----------------------------------------------------------------------------------


small = {1, 2}  
big = {1, 2, 3, 4, 5}  
other = {8, 9}  
  
# issubset  
print(small.issubset(big))   # True (1,2 are inside big)  
  
# issuperset  
print(big.issuperset(small)) # True (big holds all of small)  
  
# isdisjoint  
print(small.isdisjoint(other)) # True (They share no numbers)
```