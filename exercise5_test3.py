#largest = -1
#print('Before', largest)
#for number in [9, 41,12, 3, 74, 15] :
#    if number > largest :
#        largest = number
#    print(largest, number)
# print('After', largest)

#count = 0
#total = 0
#print('Start', count, total)
#for value in [9, 41, 12, 3, 74, 15] :
#    count = count +1
#    total = total + value
#    print(count, total, value)
#print('End', count, total, total / count)

small = None
print('Before')
for value in [9, 41, 12, 3, 74, 15] :
    if small is None :
        small = value
    elif value < small :
        small = value
    print(small, value)
print('After', small)
