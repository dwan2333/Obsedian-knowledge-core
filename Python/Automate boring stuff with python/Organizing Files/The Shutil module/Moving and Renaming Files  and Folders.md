```python fold:Moveing_and_Renaming
import shitil
from pathlib import Path
h = Path.home()
(h/'spam2').mkdir()
shutil.move(h/'spam/file1.text',h/'spam2') # move the file or folder at the path source to the path destination
shutil.move(h/'spam/file.text', h/'spam/file2.text') # file is overwritten if name same


```