fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    for i in line.split(): 
        lst.append(i)
lst.sort()
print(list(set(lst)))