import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    ans = 0
    n, m = map(int, input().split())
    file = deque(map(int, input().split()))
    while True:
        if len(file) == 1:
            ans += 1
            print(ans)
            break
        if file[0] < max(file):
            if m == 0:
                m = len(file)
            file.append(file.popleft())
            m -= 1
        else:
            if m == 0:
                ans += 1
                print(ans)
                break
            else:
                file.popleft()
                ans += 1
                m -= 1
