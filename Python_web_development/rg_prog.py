import re

name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_42.txt"
handle = open(name)

numlist = []

for line in handle:
    line = line.rstrip()
    extract = re.findall("([0-9]+)", line)

    if len(extract) < 1 : continue

    for i in range(len(extract)):
        num = float(extract[i])
        numlist.append(num)

print(int(sum(numlist)))



print (sum([int(i) for i in re.findall('[0-9]+',open("regex_sum_42.txt").read())]))

text = open('regex_sum_42.txt')
data=text.read()
print (sum(map(int,re.findall('[0-9]+',data))))

print (sum(map(int,re.findall('[0-9]+',open("regex_sum_42.txt").read()))))
