```python fold:Handling_paths
from pathlib import Path
Path.cwd()
Path.cwd().is_absolute() # return True based on verification that the path is aboslute
Path('bacon'/'eggs'/'sandwich'/).is_absolute()

#To get an absolute Path from a relative Path put Path.cwd()/ in front of relative path
Path.cwd()/ Path('spam'/'eggs'/'sausage')

# if your relative path is relative to another path already replace Path.cwd() to the path that it is relative to to make it absolute
```