import sys

input = sys.stdin.readline

members = [[] for i in range(201)]

T = int(input())

for _ in range(T):
    a, b = map(str, input().split())
    members[int(a)].append(b)

for i in range(1, 201):
    if members[i]:
        for x in members[i]:
            print(i, x)
