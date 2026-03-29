```python fold:opening_files
from pathlib import Path  
hello_file = open(Path.cwd()/'hello.txt', encoding = 'UTF-8')
# Read mode is tje default mode for files you open in Python
# UTF-8 is the parameter specifies what encoding to use when converting the bytes into files to a Python text string. Windows default use 'cp1252' but could cause some problem when using non - English characters. So UTF-8 is always a good choice by default. 

```