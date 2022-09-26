user_score = 0
simon_pattern = input()
user_pattern  = input()

''' Your solution goes here '''
index = 0
while index <= len(simon_pattern) :
    if simon_pattern[index] == user_pattern[index] :
        user_score += 1
        index += 1
        continue
    else:
        break



print('User score:', user_score)
