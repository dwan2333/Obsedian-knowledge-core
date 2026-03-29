- Arrays are much more memory efficient when it comes to storing numbers because of its special instant access ability 
It uses a formula:

$$\text{Address} = \text{Start\_Address} + (\text{Index} \times \text{Size\_of\_Type})$$

- **Start Address:** 1000
    
- **Index:** 5
    
- **Type Size ('i'):** 2 bytes
    

$$1000 + (5 \times 2) = \text{Address } 1010$$

The computer jumps directly to memory address 1010. It can only do this because it knows **for a fact** that every item is the same size.

In a standard Python List, you can store a tiny Integer next to a massive String.

- Item 0: 28 bytes
    
- Item 1: 540 bytes
    
- Item 2: 28 bytes
    

Because the sizes vary, the computer cannot use the multiplication formula. Instead, it stores **Pointers** (uniform addresses) in the list, which point to the actual data scattered randomly in memory. This double-step (List -> Pointer -> Data) is what makes lists slower and more memory-hungry

![[Pasted image 20251213224040.png]]

### 1, Array.tofile()

Python takes the contiguous block of memory where your array lives and copies it straight to the disk.

- **Speed:** It is incredibly fast because there is no conversion. Python doesn't have to convert the integer `100` into the string characters `"1"`, `"0"`, `"0"`.
    
- **Size:** It uses the minimum possible space (e.g., 4 bytes per integer) rather than text character
```python
import array

# 1. Create an array of integers
data = array.array('i', [100, 200, 300, 400, 500])

# 2. Open a file in 'wb' (Write Binary) mode
with open('my_data.bin', 'wb') as f:
    data.tofile(f)

print("Saved raw binary data to my_data.bin")
```

### 2 Array.fromfile()
Since the file contains unreadable binary gibberish (if you opened it in Notepad, it would look like nonsense symbols), you can't just read it with `f.read()`. You must use the matching `fromfile()` method.

You also **must** know the array Type Code (`'i'`) beforehand, or Python won't know how to read the bytes.
```python
import array

# 1. Create an empty array of the SAME type ('i')
reloaded_data = array.array('i')

# 2. Open file in 'rb' (Read Binary) mode
with open('my_data.bin', 'rb') as f:
    # Read 5 items from the file into the array
    reloaded_data.fromfile(f, 5)

print(reloaded_data)
# Output: array('i', [100, 200, 300, 400, 500])

# The number `5` in `data.fromfile(f, 5)` tells Python specifically **how many items** to read from the file, not how many bytes.If it surpass the items in data storage then python would return EOFError (end of file error)

```

### 3 Some other functions in array
![[Pasted image 20251213225254.png]]
![[Pasted image 20251213225317.png]]
![[Pasted image 20251213225326.png]]

if you want to sort an arrary you could do this
```python
from array import array

x = array('i', [4,2,1,])
b = array(x.typecode, sorted(x))
print(x)
print(b)

```
