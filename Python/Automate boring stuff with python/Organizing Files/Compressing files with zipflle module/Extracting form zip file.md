```python fold:extracting
import zipfile
example_zip = zipfil.ZipFile('example.zip')
example_zip.extractall() # you could select the location that you want to extract it to # python will create the folder if it dosen't exist 
# the first selection of file that you want to extract must match you namelist() file
example_zip.close()

```