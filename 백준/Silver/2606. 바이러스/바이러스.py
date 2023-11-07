# 바이러스, 그래프 사용

import sys

input = sys.stdin.readline

n = int(input())

count = 0
queue = [0]
visited = [False for _ in range(n)]
visited[0] = True
computers = [[0 for i in range(n)] for j in range(n)]

k = int(input())
for i in range(k):
    x, y = map(int, input().split())
    computers[x - 1][y - 1] = 1
    computers[y - 1][x - 1] = 1

while len(queue) > 0:
    target = queue.pop()
    for i in range(n):
        if not visited[i] and computers[target][i] == 1:
            queue.append(i)
            visited[i] = True
            count += 1

print(count)
