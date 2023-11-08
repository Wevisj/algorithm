#  조약돌 꺼내기 /
import math
import sys

input = sys.stdin.readline

n = int(input())
stone = list(map(int, input().split()))
k = int(input())

bottom = math.comb(sum(stone), k)
top = 0

for i in stone:
    top += math.comb(i, k)

print(top / bottom)
