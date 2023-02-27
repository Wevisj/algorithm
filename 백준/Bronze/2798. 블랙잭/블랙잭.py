import sys
from itertools import combinations

input = sys.stdin.readline

answer = 0

n, m = map(int, input().split())

nums = list(map(int, input().split()))

result = list(map(lambda a: a[0] + a[1] + a[2], list(combinations(nums, 3))))

for x in result:
    if x == m:
        answer = x
        break
    elif m > x > answer:
        answer = x

print(answer)
