```python fold:Groups_and_Alterations
# (abc) capturing group

# | OR operator

# (?:....) Non - Capturing Group (Groups pattern **without saving it** in `.group()` or `.groups()`)
import re
pattern1 = r'(?:cat|dog)s'
text1 = "cats and dogs"
matches1 = re.findall(pattern1, text1)
print(matches1)
print()

# (?P<name>....) Named group (Captures the match with a **named key** in `.groupdict()`)
pattern2 = r"(?P<animal>cat|dog)"
match = re.search(pattern2, "I love my cat")
print(match.group("animal"))  # cat
print(match.groupdict()) 
print()

# another example

text = "+1-123-456-7890 123-456-7890"
pattern = re.compile(r'(?:\+\d{1}-)?\d{3}-\d{3}-\d{4}')
print(pattern.findall(text))
print()

# (? = ...) Positive lookhead(are consumed), (?<=....) Positive lookbehind(are consumed)
pattern3 = r"[a-zA-z]+(?=\d+)"
text3 = "abc123 def456 ghi"
matches3 = re.findall(pattern3, text3)
print(matches3)
print()

text = "Follow us on Twitter: @alice, @bob_the_builder, and contact @support123 for help."
pattern = r'(?<=@)\w+'
handles = re.findall(pattern, text)
print(handles)
print()

# (?!...) Negative lookhead, (?<!.....) Negative lookbehind
pattern4 = r"\b\w+(?<!\d)\b" 
text4 = "abc def4 ghi5 xyz"
matches4 = re.findall(pattern4, text4)
print(matches4)
```