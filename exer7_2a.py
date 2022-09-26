fname = input("Enter file name: ")
try :
    fh = open(fname)
except :
    print(File can not be opened:', fname)
    quit()

Count = 0
TotNumber = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    Count = Count + 1
    Position   = line.find('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    CharNumber = line[Position : ]
    MyNumber   = float(CharNumber)
    TotNumber  = TotNumber + MyNumber

print('Average spam confidence:', TotNumber/Count)
