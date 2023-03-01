import sys

input = sys.stdin.readline

coordinate = [[] for i in range(200001)]

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    coordinate[y + 100000].append(x)

for y in range(200001):
    if coordinate[y]:
        for x in sorted(coordinate[y]):
            print(x, y - 100000)
