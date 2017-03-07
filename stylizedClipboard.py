#! Python 2.7
# stylizedClipboard.py - stylize your clipboard: add * at the beginning of each line. 

import pyperclip 

text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
    
text = '\n'.join(lines)

pyperclip.copy(text)