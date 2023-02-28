import sys

input = sys.stdin.readline

ans = 1

a, b, v = map(int, input().split())

if (v - a) % (a - b) == 0:
    ans += (v - a) // (a - b)
else:
    ans += (v - a) // (a - b) + 1

print(ans)
