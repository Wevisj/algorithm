import sys

input = sys.stdin.readline

n = int(input())

for i in range(1, 10):
    print(n, "*", i, "=", n * i)
