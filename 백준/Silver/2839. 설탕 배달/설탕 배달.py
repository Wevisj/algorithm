import sys

input = sys.stdin.readline

ans = 0

n = int(input())

while n > 0:
    if n % 5 == 0:
        ans += n // 5
        n = 0
    else:
        ans += 1
        n -= 3

if n == 0:
    print(ans)
else:
    print(-1)
