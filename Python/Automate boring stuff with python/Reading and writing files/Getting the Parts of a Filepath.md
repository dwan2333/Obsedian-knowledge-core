```python fold:Getting_the_Parts_Of_a_filepath
from pathlib import Path
p = Path('C:/Users/Al/spam.txt')
print(p.anchor)
print(p.name)
print(p.stem)
print(p.suffix)
print(p.drive)
print(p.parent)

#if you want to split it up
print(p.parts)
```