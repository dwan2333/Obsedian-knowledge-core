```python fold:functions
import re
# re.compile(pattern) stores as a pattern and could be used for other functions
# re.search(pattern, string) Find first matchin string (anywhere)
# re.match(pattern, string) only matches at beginning of string (only at the start)
# re.fullmatch(pattern, string) matches the entire string
pattern = re.compile(r'\d+')
text ='123abc'
match = pattern.match(text)
fullmatch = pattern.fullmatch(text)
if match:
	print('match: yes')
	print(match.group())
else:
	print('match: no')
if fullmatch:
	print('fullmatch: yes')
	print(fullmatch.group())
else:
	print('fullmatch: no')
print()

# re.findall(pattern, string) return all non-overlapping matches into a list
pattern2 = re.compile(r'\d+')
text = '123 234 123b 123abc'
print(pattern2.findall(text))
# re.finditer(pattern, string) returns match objects for al matches
for match in pattern2.finditer(text):
	print(match.group())
# re.split(pattern, string) split strings by matches of pattern
text = 'Hello, world'
pattern3 = re.compile(r',')
print(pattern3.split(text))
# re.sub(pattern, rep, string) replace all matches
# re.subn(pattern, rep, string) same as sub but also returns counts
# re.IGNORCASE or re.I
# re.DOTALL makes . in regex match \n characters 
# re.VERBOSE re.(X) white space are ignored also (make it pretty looking), # are also ignored
 
phone_pattern = re.compile(r"""
    (\d{3}|\(\d{3}\))?   # optional area code, e.g. 415 or (415)
    [\s\-\.]?            # optional separator: space, dash, or dot
    \d{3}                # first 3 digits
    [\s\-\.]             # separator
    \d{4}                # last 4 digits
    """, re.VERBOSE)
```