n = int(input())
numbersN = list(map(int, input().split()))
m = int(input())
numbersM = list(map(int, input().split()))
numbers = {}
for key in numbersN:
    if key in numbers:
        numbers[key] += 1
    else:
        numbers[key] = 1
for key in numbersM:
    if key in numbers:
        print(numbers[key], end=" ")
    else:
        print(0, end=" ")
