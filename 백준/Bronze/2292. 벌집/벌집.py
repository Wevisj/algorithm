import sys

input = sys.stdin.readline

ans = 1
i = 1

n = (int(input()) - 1) / 6

while n > 0:
    n -= i
    i += 1
    ans += 1

print(ans)
