import sys

input = sys.stdin.readline

n = int(input())

for i in range(1, n + 1):
    num = str(i)
    result = i
    for j in range(len(num)):
        result += int(num[j])
    if result == n:
        print(i)
        break

if i == n:
    print(0)
