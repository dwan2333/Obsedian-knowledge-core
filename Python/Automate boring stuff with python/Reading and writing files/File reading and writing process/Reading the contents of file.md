```python fold:Reading
from pathlib import Path  
hello_file = open(Path.cwd()/'hello.txt', encoding = 'UTF-8')
hello_content = hello_file.read()
print(hello_content)
# readlines() method returns list
```