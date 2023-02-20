import sys
import math

input = sys.stdin.readline

T = int(input())

for i in range(T):
    x, y = map(int, input().split())
    distance = y - x
    n = int(math.sqrt(distance))
    if distance == n ** 2:
        print(n * 2 - 1)
        continue
    x1 = n ** 2
    x2 = (n + 1) ** 2
    if distance > (x1 + x2) / 2:
        print((n + 1) * 2 - 1)
    else:
        print(n * 2)
