```python fold:filesize_and_timestamps

# if a file path exists you can use stat() to find about its status
# st_size the size of the file in bytes
# st_mtime the 'last modified' timestamp, when the file was last changed
# st_ctime  the 'creation' tunestamp. On windows, this identifies when the file was created. On macOS and Linux, this identifies the last time the file's metadata (such as its name) was changed
# st_atime the 'last accessed' timestamp, when the file was last read
# Unix is used as standarad time
```