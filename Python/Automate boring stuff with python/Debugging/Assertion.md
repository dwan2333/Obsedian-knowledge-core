```python fold:Assertion
# is an sanity check for your code of not doing anything that is obviosuly wrong
# code stops immediately if there is anything wrong instead of continues going on
def sqrt(x):  
    assert x >= 0, f'The sqrt should not be negative'  
    return x ** 0.5  
  
# Normal case  
print(sqrt(16))   # → 4.0  
  
# This will trigger an AssertionError  
print(sqrt(-4))
```