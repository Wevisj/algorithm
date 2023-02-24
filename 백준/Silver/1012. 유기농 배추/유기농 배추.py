import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)


def is_true(n, m):
    if n > 0:
        if field[n - 1][m]:
            field[n - 1][m] = False
            is_true(n - 1, m)
    if m > 0:
        if field[n][m - 1]:
            field[n][m - 1] = False
            is_true(n, m - 1)
    if n < len(field) - 1:
        if field[n + 1][m]:
            field[n + 1][m] = False
            is_true(n + 1, m)
    if m < len(field[n]) - 1:
        if field[n][m + 1]:
            field[n][m + 1] = False
            is_true(n, m + 1)


T = int(input())

for _ in range(T):
    result = 0
    m, n, k = map(int, input().split())
    field = [[False] * m for i in range(n)]
    for l in range(k):
        x, y = map(int, input().split())
        field[y][x] = True
    for i in range(n):
        for j in range(m):
            if field[i][j]:
                field[i][j] = False
                result += 1
                is_true(i, j)
    print(result)
