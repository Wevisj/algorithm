import sys
from itertools import combinations

input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))

    if 0 in nums:
        break

    nums.sort()
    if nums[2] ** 2 == nums[0] ** 2 + nums[1] ** 2:
        print("right")
    else:
        print("wrong")
