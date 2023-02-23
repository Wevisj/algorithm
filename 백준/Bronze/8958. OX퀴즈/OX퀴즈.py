import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    score = 1
    result = 0
    str = input()
    for i in range(len(str)):
        if str[i] == "O":
            result += score
            score += 1
        else:
            score = 1
    print(result)
