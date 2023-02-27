import sys
from itertools import combinations

input = sys.stdin.readline

n, k = map(int, input().split())

nums = [i for i in range(n)]

print(len(list(combinations(nums, k))))
