import sys

input = sys.stdin.readline

coordinate = [[] for i in range(200001)]

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    coordinate[x + 100000].append(y)

for x in range(200001):
    if coordinate[x]:
        for y in sorted(coordinate[x]):
            print(x - 100000, y)
