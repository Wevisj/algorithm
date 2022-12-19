import math

T = int(input())
while T:
    numbers = list(map(int, input().split()))
    print(int(math.factorial(numbers[1]) / (math.factorial(numbers[1] - numbers[0]) * (math.factorial(numbers[0])))))
    T -= 1
