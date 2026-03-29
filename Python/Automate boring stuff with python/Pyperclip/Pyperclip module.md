```python fold:Pyperclip
import pyperclip
pyperclip.copy() # pyperclip.copy("Hello, world!")
# Now if you press Ctrl+V (or Cmd+V on Mac) in any text field,
# you'll paste "Hello, world!
current = pyperclip.paste()
print("Clipboard contains:", current)
# Suppose the user has highlighted and copied some text elsewhere
```