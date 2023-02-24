import sys

input = sys.stdin.readline

n, x = map(int, input().split())

numbers = list(map(int, input().split()))

for k in numbers:
    if k < x:
        print(k, end=" ")
