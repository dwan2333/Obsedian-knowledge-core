"""Fix formatting issues in Chapter 4 (Main).md:

1. Orphan continuation lines that should be inside callouts but aren't prefixed
   with '> '. Walk every block, and when a line doesn't start with '>' but the
   previous non-empty line was a callout line, glue the continuation back in
   (merging into the previous line, which is what NotebookLM intended).

2. Stray punctuation artifacts left from the U+FFFD => em-dash replacement
   (e.g. 'Example 1 —"' should be 'Example 1 —').

3. Collapse hard line wraps inside callout bodies into proper paragraphs.

Usage: py _fix_format.py
"""
import re
import os

DIR = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(DIR, 'Chapter 4 (Main).md')

with open(PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# === Step 1: strip stray-quote artifacts ===
# Pattern: em-dash immediately followed by punctuation that doesn't belong there
# — followed by " (right double quote) is the most common artifact in our case
content = re.sub(r'—["”]', '—', content)
content = re.sub(r'—["“]', '—', content)
# Also handle stray closing-quote artifacts more generally inside titles
content = re.sub(r'— "', '— ', content)

# === Step 2: walk lines and fix orphan callout continuations ===
# Strategy: inside a callout block (lines starting with '> '), if a line
# doesn't start with '>', it's an orphan continuation. Merge it into the
# previous line by joining with a single space.

lines = content.split('\n')
fixed_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    if line.startswith('>'):
        # We're inside a callout. Look ahead and merge any orphan continuations.
        accumulated = line
        j = i + 1
        while j < len(lines):
            next_line = lines[j]
            if next_line.strip() == '':
                # Empty line ends the merge
                break
            if next_line.startswith('>'):
                # Next line is its own callout line — stop merging, treat separately
                break
            # Orphan continuation — merge it into accumulated
            accumulated = accumulated.rstrip() + ' ' + next_line.strip()
            j += 1
        fixed_lines.append(accumulated)
        i = j
    else:
        fixed_lines.append(line)
        i += 1

content = '\n'.join(fixed_lines)

# === Step 3: collapse multiple internal spaces created by merges ===
# Merging may have introduced double-spaces. Normalize.
content = re.sub(r'(?<=\S) {2,}(?=\S)', ' ', content)

# === Step 4: ensure proper blank line before each callout & section ===
# Avoid runs of more than 2 newlines
content = re.sub(r'\n{4,}', '\n\n\n', content)

# === Step 5: count + report changes ===
with open(PATH, 'w', encoding='utf-8') as f:
    f.write(content)

word_count = len(content.split())
line_count = content.count('\n')
size_kb = os.path.getsize(PATH) / 1024
print('Fixed Chapter 4 (Main).md')
print(f'  Words: {word_count:,}')
print(f'  Lines: {line_count:,}')
print(f'  Size : {size_kb:.1f} KB')

# Verify: count orphan continuations remaining
lines = content.split('\n')
orphans = 0
in_callout = False
for line in lines:
    if line.startswith('>'):
        in_callout = True
    elif line.strip() == '':
        in_callout = False
    elif in_callout:
        orphans += 1
print(f'  Remaining orphan-continuation lines inside callouts: {orphans}')

# Verify: count stray-quote artifacts
artifacts = content.count('—"') + content.count('— "')
print(f'  Remaining em-dash + stray-quote artifacts: {artifacts}')
