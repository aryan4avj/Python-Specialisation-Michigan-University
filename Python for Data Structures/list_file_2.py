fname = input("Enter file name: ")
if len(fname) < 1 : 
    fname = "mbox-short.txt"

fh = open(fname)
counter = 0

for line in fh :
    line = line.rstrip()
    if not line.startswith('From '): continue        
    words = line.split()
    print (words)
    counter +=1

print ("There were", counter, "lines in the file with From as the first word")

