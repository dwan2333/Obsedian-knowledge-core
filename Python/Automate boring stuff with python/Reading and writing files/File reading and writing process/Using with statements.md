```python fold:With
# with statement make it easier to automatically close files by creating a context manager

with open('bacon.txt','w', encoding ='UTF-8') as bacon_file:
	bacon_file write('Hello World !")
with open('bacon.txt', encoding ='UTF-8') as bacon_file:
	content = bacon_file.read()
	print(content)

```