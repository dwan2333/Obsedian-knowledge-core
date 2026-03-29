- The interpreter takes a shortcut when dealing for built-in types like list, str, bytearray, or extensions like the NumPy arrays. Pythonvariable-sized collections written in C include a struct called ==PyVarObject==, which has an ==ob_size== field holding the number of items in the collection. So, if my_object is an instance of one of those built-ins then len(my_object) retrieves the value of the ==ob_size== field, andhis is much faster than calling a method.
	- ==PyVarObject==  (Box with the Counter)
	- ==ob_size==(Number on the digital counter) - keep track of the numbers 
			