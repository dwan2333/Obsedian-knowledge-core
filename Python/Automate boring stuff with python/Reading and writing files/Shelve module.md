```python fold:Shelve
# shelve module in python provide a simple persistent dictionary-like object, allowing you to store and retrieve arbitary python objetcs on disk using a string key. 
import shelve

# Open a shelf (file) for read/write
with shelve.open('contacts.db') as contacts:
    # Store some objects
    contacts['bob']   = {'phone': '123-4567', 'email': 'bob@example.com'}
    contacts['alice'] = {'phone': '555-0101', 'email': 'alice@example.org'}

    # Retrieve
    print(contacts['bob']['email'])  # bob@example.com

    # Update
    c = contacts['alice']
    c['phone'] = '555-9999'
    contacts['alice'] = c

    # List all keys
    print(list(contacts.keys())) 

```