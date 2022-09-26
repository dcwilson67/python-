stop = int(input())
result = 0
for a in range(3):
    for b in range(4):
        result += a + b
    print(result)
    if result > stop:
        break
