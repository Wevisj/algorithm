import sys

input = sys.stdin.readline

drawing_paper = [[False for i in range(100)] for j in range(100)]

ans = 0

papers = int(input())

for _ in range(papers):
    x, y = map(int, input().split())
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            drawing_paper[i][j] = True

for i in range(100):
    ans += drawing_paper[i].count(True)

print(ans)
