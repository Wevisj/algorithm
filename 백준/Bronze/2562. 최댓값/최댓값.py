numbers = [-1]

for i in range(9):
    numbers.append(int(input()))
    
max_num = max(numbers)

print(max_num, numbers.index(max_num), sep="\n")
