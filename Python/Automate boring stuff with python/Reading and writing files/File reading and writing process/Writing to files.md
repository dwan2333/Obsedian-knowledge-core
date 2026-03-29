```python fold:writing
# write mode: overwrite the existing file 
# append mode: append text to the end of the existing file

bacon_file  = open ('bacon.txt','w', encoding = 'UTF-8')
bacon_file.write('Hello World!\n')
bacon_file.close()

# if it is different mode you have to close it and reopen it

bacon_file = open('baocn.txt', 'a', encoding ='UTF-8')
baconfile.write('Bacon is not a vegetable')
bacon_file.close()

bacon_file = open('bacon.txt', encoding = 'UTF-8')
content = bacon_file.read()
print(content)
bacon_file.close()
```