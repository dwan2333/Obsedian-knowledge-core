```python fold:read
import zipfile

example_zip = zipfile.ZipFile('example_zip')
example_zip.namelist() # return the selected file is being zipped which is file1.txt according to the previous
file1_info = example_zip.getinfo('file1.txt') # return object about that particular file
file1_info.file_size # gives file size
file1_info.compress_size # give compressed size



```