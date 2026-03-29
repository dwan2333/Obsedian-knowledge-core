```python fold:Delete!!!
# shutil.rmtree(path) delete the entire folder tree at path including all the files and subfolders it contains
# os.unlink(path) will delete single file at path
# os.rmdir(path) will delete the folder at path. This folder must be empty

```
```python fold:Deleting_to_recyle_bin
import send2trash #third party module
send2trash.send2trash('file1.txt')
```