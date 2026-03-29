```python fold:file_and_fielpaths
# on windown path are writen using \ while on linux and mac os paths are written with /
# we could standardize path by using the pathlib libary in python
# on windows \ seperate directoris so you can not use it in filanames. However you can use blackslashes in filenames on macOS and Linux. SO while Path(r'spam\egg) refers to two seperate folders on Windows, the same command would refer tos a single file on macOS or Linux
from pathlib import Path


```