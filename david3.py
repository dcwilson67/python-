stop = 8
total = 0
for number in [3, 5, 3, 4, 5, 3]:
    print(number, end=' ')
    total += number
    if total > stop:
        print('!')
        break
else:
    print(f'/ {total}')
print('done')
