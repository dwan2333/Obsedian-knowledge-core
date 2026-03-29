```python fold:raise_exceptions
def box_print(symbol, height, width):
	if len(symbol) != 1:
		raise Exception('Symbol must be a single string')
	if height < 2:
		raise Exception('Height must be bigger or greater than 2')
	if width < 3:
		raise Exception('Width must be bigger or greater than 3')
	print(symbol * width)
	for i in range(height - 2):
		print(symbol + (' ' * (width - 2)) + symbol)
	print(symbol * width)
try:
	box_print('*',4,4)
	box_print('0',5,20)
	box_print('x',1,3)
	box_print('zz',3,3)
except Exception as err:
	print("An exception has happened " + str(err))
try:
	box_print('zz',3,3)
except Exception as err:
	print('An exception has happened' + str(err))
```