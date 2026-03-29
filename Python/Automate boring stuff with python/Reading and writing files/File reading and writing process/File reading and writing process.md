```python fold:Reading_and_Writing
# txt, doc, etc are Plaintext files wherears PDF, images are binary files, they are showned very different when being opened
# read_text() returns the full contents of a text file as a string
# write_text() creaates a new text file with the string passed to it
from pathlib import Path
p = Path('spam.txt')
p.write_text("Hello World")
p.read_text()
# this creates a spam.txt file

# most common way involes open() read() write() close() for files

```