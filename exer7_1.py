fname = input('Enter file name: ')
fhand = open(fname)
for david in fhand :
    david = david.rstrip()
    #david = david.upper()
    print(david.upper())
