T = int(input())
numbers = []
for _ in range(T):
    numbers.append(int(input()))
numbers.sort()
for i in range(T):
    print(numbers[i])
