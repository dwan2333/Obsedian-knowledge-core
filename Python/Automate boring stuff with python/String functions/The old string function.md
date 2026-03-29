```python fold:old_method
# %s string
name = "Alice"
print("Hello, %s!" % name)
# %d and %i (they are the same)
score = 95
print("Score: %d" % score)  
print("Score again: %i" % score)
# %r raw string
value = "Hello\nWorld"
print("Raw: %r" % value)
# %f default 6 decimal places
pi = 3.14159265
print("Pi: %f" % pi)
# Float with 2 decimals
print("Pi rounded: %.2f" % pi)
# %X and %x hexadecimal in upper and lowre format
num = 255
print("Hex (lower): %x" % num)
# %% literal percent sign
print("Success: 100%%")
# %Scientific notation upper and lower case
big = 1234565
print("Sci: %.2E" % big)
print("Sci: %.2e" % big)
# mutiple alighment tuple format
name = "Alice"
score = 95
print("Name: %s, Score: %d" % (name, score))
# Name: Alice, Score: 95
```