```python fold:creatind_and_adding

import zipfile
with open('file1.txt','w',encoding = 'UTF-8') as file_obj:
	file_obj.write('Hello' * 9000)
with zipfile.ZipFile('example.zip', 'w') as example_zip:
	example_zip.write('file1.txt', compress_type = zipfile.ZIP_DEFLATED, compresslevel = 9)  # compress_type tell computer what type of algo used ot compress the file
	
```