import sys

input = sys.stdin.readline

result = 0

n = int(input())
num = input()

for i in range(n):
    result += int(num[i])

print(result)
