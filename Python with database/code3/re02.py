# Search for lines that start with 'From'
import re
hand = open('Python with database\code3\mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)
