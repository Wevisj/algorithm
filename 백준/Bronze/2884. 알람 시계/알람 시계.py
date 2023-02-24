import sys

input = sys.stdin.readline

h, m = map(int, input().split())

if m - 45 < 0:
    m = 60 + (m - 45)
    h -= 1
    if h == -1:
        h = 23
else:
    m -= 45

print(h, m)
