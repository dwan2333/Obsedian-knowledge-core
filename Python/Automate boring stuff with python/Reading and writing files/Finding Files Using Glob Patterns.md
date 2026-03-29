```python fold:file_using_Glob_patterns
# * and ? characters can be used to match folder names and filenames in Glob_patterns

# *.txt matches all files that end with txt 
# project?.txt matches 'project.txt', 'project2.txt'
# project?.* matches 'catproject5.txt' 'secre_project.doc'
# '*' matches all filenames
from pathlib import Path 
p = Path('C:/Users')
print(list(p.glob('*')))
for name in p.glob('*'):
	print(name)



```