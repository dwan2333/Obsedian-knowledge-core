the build in memoryview class is a shared-memory sequence type that lets you have slices of arrays without copying bytes 

### 1. The Problem: Slicing Usually Copies

Normally, when you slice a list, tuple, or bytes object in Python, you are creating a **copy**.

```python 
data = b'x' * 1000000  # 1 MB of data
subset = data[0:500000] # COPIES 500 KB to a new object
```

### 2. The Solution: `memoryview` (Shared Memory)

A `memoryview` wraps the original object and lets you slice it. The slices are just "windows" looking at the **original** data
```python
data = b'x' * 1000000
mv = memoryview(data)

subset = mv[0:500000]   # Zero Bytes copied.

```


### 3, memoryview.cast() 

```python
# 1, memoryview.cast changes the data type that you are viewing 
import array

# Two unsigned short integers ('H' = 2 bytes each)
# 10  = 0x000A (Bytes: 10, 0)
# 258 = 0x0102 (Bytes: 2, 1) 
numbers = array.array('H', [10, 258])
mem = memoryview(numbers)

print(f"Original shape: {mem.shape}") # (2,) - Two items
print(f"Original list:  {mem.tolist()}") # [10, 258]

# CAST TO BYTES ('B')
# We are zooming in. 2 items become 4 items.
mem_bytes = mem.cast('B')

print(f"New shape: {mem_bytes.shape}") # (4,) - Four items
print(f"New list:  {mem_bytes.tolist()}") 
# Output: [10, 0, 2, 1] 
# (Note: 10,0 is the first number. 2,1 is the second number.)
```

```python
#  The "Matrix" (Changing Shape) 
#  This is the second superpower of `cast`. You can take a flat list of numbers and instantly treat it like a 2D or 3D grid (matrix).

import array

# A flat array of 6 numbers
data = array.array('i', [1, 2, 3, 4, 5, 6])
mem = memoryview(data)

# CAST TO 2D GRID
# args: format, shape
# We keep the format 'i' (integers), but force a shape of (2, 3)
matrix = mem.cast('i', shape=(2, 3))

print(matrix.tolist())
# Output:
# [[1, 2, 3], 
#  [4, 5, 6]]


```

### 4 How bits and bytes works in memoryview

