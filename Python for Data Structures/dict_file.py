name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts=dict()

for line in handle:
##    print(line)
    if not line.startswith('From '): continue
    words = line.split()
    # print(words[1])
    z=words[1]
            
    counts[z] = counts.get(z,0) +1
# print(counts)

bigCount = None
bigWord = None
for word,count in counts.items():
    if bigCount is None or count >bigCount:
        bigWord = word
        bigCount = count

print(bigWord, bigCount)

