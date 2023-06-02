import sys
from collections import deque

input = sys.stdin.readline

people = deque()
result = []
n, k = map(int, input().split())

for i in range(1, n + 1):
    people.append(i)

while people:
    for _ in range(k - 1):
        people.append(people.popleft())
    result.append(people.popleft())

print(str(result).replace('[', '<').replace(']', '>'))
