import sys
from itertools import permutations

input = sys.stdin.readline

num = []

n, m = map(int, input().split())

for i in range(1, n + 1):
    num.append(i)

arr = list(permutations(num, m))

for x in arr:
    print(*x)
