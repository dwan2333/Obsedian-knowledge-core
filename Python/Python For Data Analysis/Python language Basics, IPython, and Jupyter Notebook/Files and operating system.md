Python file modes 
1, r = reading
2, w = writing only mode and create a new file (erasing the data for any file with the same name)
3, x = writing only mode but fails if the file already exist 
4, a = appending to the existing file (create one if it dose not exist)
5, r+ = read and write
6, b = add mode to binary files
7, t = text mode for files 
```python

lines = [" Apple", " Banana", " Cherry"]

with open("fruit.txt", "w") as f:
    # 1. Using write() - Good for one thing
    f.write("Header\n") 
    
    # 2. Using writelines() - Good for a list
    # Note: If 'lines' didn't have \n inside them, this would look like "AppleBananaCherry"
    f.writelines(lines)
#---------------------------------------------------------------------------------
# seek(offset, from_where)
	# offset : how many bytes to move 
	# from_where : 1 = curretn position, 0 = start of the document , 2 = end of file
with open("test.txt", "w+") as f:
    f.write("Hello World")
    
    # Check position
    print(f.tell())  # Output: 11 (End of the string)
    
    # Move back to start
    f.seek(0)
    print(f.tell())  # Output: 0
    
    # Read just the first word
    print(f.read(5)) # Output: Hello
    
    # Move to the 6th byte (skip the space)
    f.seek(6)
    print(f.read())  # Output: World
```