import sys
from collections import deque

input = sys.stdin.readline


def bfs(graph, start):
    num = [0] * (user + 1)
    visited = [start]
    queue = deque()
    queue.append(start)

    while queue:
        n = queue.popleft()
        for i in graph[n]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
                num[i] += num[n] + 1
    return sum(num)


user, m = map(int, input().split())
graph = [[] for _ in range(user + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = []
for j in range(1, user + 1):
    result.append(bfs(graph, j))

print(result.index(min(result)) + 1)
