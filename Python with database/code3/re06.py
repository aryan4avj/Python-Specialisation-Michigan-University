# Search for lines that have an at sign between characters
import re
hand = open('Python with database\code3\mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0:
        print(x)