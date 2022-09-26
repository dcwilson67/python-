a = int(input())
b = int(input())
c = int(input())
result = 0
while a < b:
    result = a * 2
    print(result)
    if result > c:
        break
    a += 3
