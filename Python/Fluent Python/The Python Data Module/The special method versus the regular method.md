```python
my_list = [10, 20, 30]  
  
# --- SPECIAL METHOD ---  
# You want to access an item.  
# You use SYNTAX (brackets).  
item = my_list[0]    
# Python secretly calls: my_list.__getitem__(0)  
  
  
# --- REGULAR METHOD ---  
# You want to add an item.  
# There is no universal symbol for "append". # You must use the specific NAME.  
my_list.append(40)   
# YOU called it directly.
```
![[Pasted image 20251204165637.png]]