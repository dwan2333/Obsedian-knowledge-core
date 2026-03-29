```python fold:walking_a_directory_tree
import os
# if you want to list all the files and subfolders in a folder call 
os.listdir(r'C:\Users\dwan0')
# ['All Users', 'Default', 'Default User', 'desktop.ini', 'dwan0', 'Public', 'WsiAccount']

# you could also use the iterdir() method
home = Path.home()
list(home.iterdir())

# os.walk()  returns three values on each iteration through the loop
from pathlib import Path
h = Path.home()
for folder_name, subfolder,filename in os.walk(h):
 # gives you all subfolder and files in your choise of folder path (a string of current folder name, a list of subfolder, a list of files)
 
```