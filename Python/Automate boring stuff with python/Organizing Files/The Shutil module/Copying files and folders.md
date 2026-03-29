```python
import shutil
from pathlib import Path
h = Path.home()
# for creating a new file for later example
with open(h / 'file1.txt' , 'w', encoding = 'UTF-8') as file:
	file.write('Hello')
shutil.copy(h / 'file1.txt', h ) # shutil,copy(source, destination)
shutil.copy(h / 'file1.txt', h / 'file2.txt') # could be done in the same directory but have to be in different names 
shutil.copytree(h / 'spam', h / 'spam_backup') # copytree dose the same but copy the entire directory 

```