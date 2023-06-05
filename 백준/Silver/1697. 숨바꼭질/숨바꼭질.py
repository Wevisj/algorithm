import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            print(sec[x])
            break
        for i in (x - 1, x + 1, x * 2):
            if 0 <= i <= MAX and not sec[i]:
                sec[i] = sec[x] + 1
                queue.append(i)


MAX = 10 ** 5
sec = [0] * (MAX + 1)
n, k = map(int, input().split())

bfs()
