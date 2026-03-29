```python fold:Greedy_or_Non_Greedy
# python alawys default in finding greedy group
import re  
  
greedyHaRegex = re.compile(r'(Ha){3,5}')  #greedy by default
mo1 = greedyHaRegex.search('HaHaHaHaHa')  
print(mo1.group())  
  
  
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')  
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')  
print(mo2.group())

```