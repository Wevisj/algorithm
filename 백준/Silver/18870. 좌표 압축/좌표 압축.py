from copy import deepcopy
T = int(input())
numbers_dict = {}
numbers = list(map(int, input().split()))
for i in range(T):
    numbers_dict[numbers[i]] = numbers[i]
coor_compress = deepcopy(numbers)
coor_compress.sort()
n = 0
for i in range(T):
    if i == T - 1:
        numbers_dict[coor_compress[i]] = n
    else:
        if coor_compress[i] == coor_compress[i + 1]:
            numbers_dict[coor_compress[i]] = n
            i += 1
        else:
            numbers_dict[coor_compress[i]] = n
            n += 1
for i in range(T):
    if i==T-1:
        print(numbers_dict[numbers[i]], end="")
    else:
        print(numbers_dict[numbers[i]], end=" ")
