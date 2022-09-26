score = input("Enter Score:")
try:
    myscore = float(score)
except:
    myscore = -1
# print(myscore)

if myscore == -1:
    print('score entered not valid')
else:
    if myscore >= 0.9:
        grade = 'A'
    elif myscore >= 0.8:
        grade = 'B'
    elif myscore >= 0.7:
        grade = 'C'
    elif myscore >= 0.6:
        grade = 'D'
    else:
        grade = 'F'
print(grade)
