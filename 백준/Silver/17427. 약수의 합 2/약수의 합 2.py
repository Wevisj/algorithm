import sys

input = sys.stdin.readline

result = 0

N = int(input())

for i in range(1, N + 1):
    result += (N // i) * i

print(result)
