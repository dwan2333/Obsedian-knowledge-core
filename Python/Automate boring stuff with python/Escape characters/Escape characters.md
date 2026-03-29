```python fold:Escape_Characters
import time
print('\\') # just one backlash
print('\'') # single quote 
print('\"') # double quote
print('a\nbc') # new line (\n)
print('\tabc') #\t is tab space
print()
for i in range(3): # \r is carriage return which wipe out everything before it and keep what is behind everytime is excuted   
	print(f'\rLoading{i}....', end = ' ')
	time.sleep(1/2)
print()
s = 'Hello World!' + "\b" * 4 + "Python!"  #\b back up and delete the character along the way
print(s)
```