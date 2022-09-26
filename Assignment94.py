fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
david = dict()

for line in fh :
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    david[words[1]] = david.get(words[1],0) + 1
    #print(david)

highcount = None
highaddress = None
for address,count in david.items() :
    if highcount is None or count > highcount :
        highaddress = address
        highcount   = count

print(highaddress, highcount)
