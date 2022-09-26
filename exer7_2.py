fname = input("Enter file name: ")
fh = open(fname)
Count = 0
TotNumber = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    Count = Count + 1
    Position   = line.find('0')
    CharNumber = line[Position : ]
    MyNumber   = float(CharNumber)
    TotNumber  = TotNumber + MyNumber
    #print(line, Count, TotNumber)
print('Average spam confidence:', TotNumber/Count)
