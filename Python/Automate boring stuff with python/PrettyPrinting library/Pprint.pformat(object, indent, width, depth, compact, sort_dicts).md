```python
# pprint prints directly, pformat returns as a string
from pprint import pformat, pprint

data = {
    "user": "Alice",
    "scores": [98, 87, 92, 85],
    "profile": {
        "age": 21,
        "major": "Mathematics",
        "hobbies": ["reading", "cycling", "chess"]
    }
}

# pprint directly prints:
pprint(data)
print()
# pformat returns a string, useful for logging or writing to file
formatted = pformat(data)
print("For log:\n" + formatted)
# options for indent, sort_dicts, depth, width, and oompact are the same.
```