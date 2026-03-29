```python fold:Reading_CSV
import csv  
example_file = open('example3.csv')  
example_read = csv.reader(example_file)  
print(list(example_read)) 
for row in example_read: # read each row of example_read.csv files, each role = each list 
	print('Row#' + str(example_reader.line_num) + ' ' + str(row))

example_file.close() 

```
```python fold:Writing_CSV
import csv
example_write = open('output.csv', newline = '', 'w') # if no newline is not written the new line written each time would be double spaced
output_writer = csv.writer(example_write)
output_writer.writerow(['spam','eggs','bacon','ham']) 
```
```python fold:Using_TAB_instead_of_comma
import csv
example_write = open('output.tsv','w', newline = '') # remeber if you are using tab , csv files have to be written in tsv
output_write = csv.writer(example_write, delimiter = '\t', lineterminator = '\n\n')
output_write.writerow(['bacon','eggs','somehting'])
# this would result the csv file to be written in space of tab, and each lines would be double spaced 
```
```python fold:Handling_Header_Rows
import csv
example_file = open('output.csv')  # the Dict reader would mark the first line of the cvs file as keys for dict and when its read or written it would be in the format of a dict
output_reader = cvs.DictReader(example_file) 
print(list(output_write))
for row in output_reader:
	print(row['Timestamp'], row['Fruit'], row['Quantity'])
# for those that column under the recognized DictReader.keys, the would be input as dictionary as values, and into different rows
output_file = open(example_file, newline = '', 'w')
output_write = csv.DictWriter(output_file, ['Name','Pet','Phone'])
output_write.writeheader()
output_write.writerow({'Name':'Alice', 'Pet':'cat', 'Phone': '555-1234'}) # Thses would be ammeded to the csv file no matter what oder you are alining them in. It could 'Pet' in the front or 'Name' in the back but still when it appears in the csv file name would alawys be infront

```