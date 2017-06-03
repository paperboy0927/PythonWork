#! /usr/bin/env python3

# bulletpointadder.py - Adds wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip

text = pyperclip.paste()

# separate lines and add stars

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]


text = '\n'.join(lines)

pyperclip.copy(text)



