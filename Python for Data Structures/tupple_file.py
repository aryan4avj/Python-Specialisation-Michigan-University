name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    words = line.split()
    if words == []: continue
    if words[0] != 'From': continue
    k = words[5].split(':')
    counts[k[0]] = counts.get(k[0],0) + 1


lst = []
lst = sorted([(v,k) for v,k in counts.items()])

for a,b in lst:
    print(a,b)
