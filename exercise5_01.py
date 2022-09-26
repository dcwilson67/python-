count = 0
total = 0
while True :
    invalue = input('Enter a number: ')
    if invalue == 'done' :
        break
    try:
        value = float(invalue)
    except :
        print('Invalid Value')
        continue
    count = count + 1
    total = total + value
print('All Done')
print(total, count, total/count)
