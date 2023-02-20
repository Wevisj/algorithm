import sys

input = sys.stdin.readline

str = list(input())
n = 0
while n != len(str):
    if len(str) - n >= 10:
        print(*str[n:n + 10], sep="")
        n += 10
    else:
        print(*str[n:-1], sep="")
        break
