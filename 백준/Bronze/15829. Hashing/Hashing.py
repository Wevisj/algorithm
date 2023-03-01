import sys

input = sys.stdin.readline

result = 0

n = int(input())
str = input()

for i in range(n):
    result += (ord(str[i]) - 96) * (31 ** i)

print(result)
