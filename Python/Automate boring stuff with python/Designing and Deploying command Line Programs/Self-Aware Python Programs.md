```python fold:Self-ware_python_commands
from pathlib import Path  
import sys  
print(Path(__file__))  # locate the file the python file that you are currently working on
print(sys.executable)  # contains the full path and file of the Python program 
print(sys.version_info) # infomation of your python in the system
# outputs:
	#D:\Pycharm\PythonProject\Scratches.py
	#D:\Pycharm\PythonProject\.venv\Scripts\python.exe
	#sys.version_info(major=3, minor=12, micro=0, releaselevel='final', serial=0)
```