result = 0
for n in range(8):
    result = n - 4
    if (result % 2) != 0:
        print('-', end=' ')
        continue
    print(result, end=' ')
print('done')
