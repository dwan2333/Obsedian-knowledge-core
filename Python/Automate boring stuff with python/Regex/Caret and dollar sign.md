```python fold:Caret_and_dollar_sign
# ^ only matches if hello is at start
import re
pattern = re.compile(r'^Hello')
# $ only matches if is at the end
```