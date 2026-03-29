```python fold:Case_Conversion
s = 'apple'
print(s.upper())
print(s.capitalize())
print(s.lower())
print(s.title())
print(s.casefold())
```
```python fold:Trimming_Padding
s = ' apple '
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.zfill(10))
print(s.rjust(10)) # could add character = "something" to fill with character instead of just empty space for rjust, ljust and center
print(s.ljust(10))
print(s.center(10))
```
```python fold:Searching
s = 'apple'
print(s.find('a'))
print(s.rfind('a'))
print(s.index('a')) # work on list ([[Search or Count Items]]) as well list and tuple
print(s.rindex('a')) # work on list ([[Search or Count Items]]) as well list and tuple
print(s.count('p'))# work on list ([[Search or Count Items]]) as well list and tuple
```
```python fold:Testing_checking
s = 'apple'
print(s.startswith('a'))
print(s.endswith('e'))
print(s.isalpha())
print(s.isdigit())
print(s.isalnum())
print(s.isspace())
print(s.islower())
print(s.isupper())
print(s.istitle())
```
```python fold:Splitting&Joining
s = 'apple'
l = 'a\nb\nc\n'
print(s.split())
print(s.rsplit())
print(l.splitlines())
print(','.join(['a','b','c']))
print('hello,world'.partition(','))
```
```python fold:Replacing
s = 'hello world'
print(s.replace('hello', "Ni Hao"))
```