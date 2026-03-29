```python
def some_function(long_list[:]) # if you do not want the list to be modified you could add : into the list
def some_function(*something) # * as in function parameter will allow input to vary in ranges (1,2,3,4) or (1,2,3) or , etc ......
def build_profile(first, last, **user_info):
"""Build a dictionary containing everything we know about
a user."""
❶ user_info['first_name'] = first
user_info['last_name'] = last
return user_info
user_profile = build_profile('albert', 'einstein',
location='princeton',
field='physics')
print(user_profile) # output = {'location': 'princeton', 'field': 'physics', first_name': 'albert', 'last_name': 'einstein'}

```