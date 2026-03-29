```python 
# 1 Basic 
# The Template (The String with holes)  
text = "My name is {} and I am {} years old."  
  
# The Filling (Using .format)  
result = text.format("John", 25)  
  
print(result)  
# Output: My name is John and I am 25 years old.


#-------------------------------------------------------------------------------
#2 Name replacement holder 
# Notice we put words INSIDE the curly braces now  
text = "The {animal} jumped over the {object}."  
  
# The Filling  
# We specify exactly which word goes where  
result = text.format(animal="Fox", object="Fence")  
  
print(result)  
# Output: The Fox jumped over the Fence.


#-------------------------------------------------------------------------------
# 3 The delay filling (tip)
# We don't know the user's name yet, so we leave a hole: {user}  
WELCOME_MSG = "Hello {user}, welcome back to the system!"  
  
  
# ... (100 lines of code later) ...  
# ... (User logs in) ...  
  
  
# --- STEP 2: Fill it in ---  
current_user = "Alice"  
  
# We grab that old template and format it NOW.  
print(WELCOME_MSG.format(user=current_user))  
# Output: Hello Alice, welcome back to the system!

```