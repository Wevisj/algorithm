import sys
from collections import deque

input = sys.stdin.readline


def dfs(node):
    visited[node] = True
    print(node, end=' ')
    for child in sorted(graph[node]):
        if not visited[child]:
            dfs(child)


def bfs(node):
    queue = deque([node])
    visited[node] = True
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for child in sorted(graph[node]):
            if not visited[child]:
                visited[child] = True
                queue.append(child)


n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)
