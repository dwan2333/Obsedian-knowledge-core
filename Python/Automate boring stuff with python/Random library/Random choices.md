
```python fold:random.choice(seq)
import random
print(random.choice([1,2,3,4]))
print(random.choice("Hello"))
print(random.choice(('apple','banana','grape')))
# work for tuples, list and strings
```
```python fold:random.choices(seq,k=n)
import random
lst = [1,2,3,4] # also work for tuples and strings
print(random.choices(lst,k=3)) # choices could be repeated
```
```python fold:random.samples(seq,k=n)
import random
lst = [1,2,3,4] # also work for tuples and strings
print(random.sample(lst,k=3)) # choices could not be repeated
```
```python fold:random.shuffle()
import random

cards = ['A', 'K', 'Q', 'J', '10'] # dose not work with strings or tuples
random.shuffle(cards)
print(cards)
```