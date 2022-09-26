result = 1
n = 3
while n < 9:
    print(n, end=' ')
    result *= 3
    if result > 80:
        print('@')
        break
    n += 1
else:
    print(f'| {result}')
print('done')
