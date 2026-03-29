```python 
from pprint import pprint
data = {
    "user": "Alice",
    "scores": [98, 87, 92, 85],
    "profile": {
        "age": 21,
        "major": "Mathematics",
        "hobbies": ["reading", "cycling", "chess"]
    }
}

pprint(data)
print()

# indent make model more or less indented
pprint(data, indent = 4)
print()

# width (default = 80) = max line length before wrapping
pprint(data, width = 55)
print()

# depth limits how deep to print nested structures 
pprint(data, depth = 1)
print()

#Compact (default = False) = True reduces any unnecessary line breaks
pprint(data, width = 55 , compact = True)
print()
# sort_dicts (default = True) = lines are sorted based on A-Z order
pprint(data, sort_dicts = False)

```