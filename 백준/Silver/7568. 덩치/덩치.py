import sys

input = sys.stdin.readline

n = int(input())

people = [list(map(int, input().split())) for i in range(n)]

for x in people:
    rank = 1
    for y in people:
        if x[0] < y[0] and x[1] < y[1]:
            rank += 1
    print(rank, end=" ")
