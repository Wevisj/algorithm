word = list(list(input()))
max_num = 0
second_num = 0

for i in range(26):
    sum = 0
    sum += word.count(chr(97 + i))
    sum += word.count(chr(65 + i))
    if sum == 0:
        continue
    if sum > max_num:
        max_num = sum
        n = i
    elif sum == max_num:
        second_num = sum
if max_num == second_num:
    print('?')
else:
    print(chr(65 + n))
