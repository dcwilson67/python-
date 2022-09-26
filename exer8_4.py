fname = input("Enter file name: ")
fh = open(fname)
lst = list()
myline = list()

for line in fh:
    line.rstrip()
    lst = line.split()

    for i in range(len(lst)) :
        if lst[i] not in myline :
            myline.append(lst[i])

myline.sort()
print(myline)
