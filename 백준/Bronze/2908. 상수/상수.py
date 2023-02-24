import sys

input = sys.stdin.readline

a, b = map(lambda x: int(x[::-1]), input().split())

print(a if a > b else b)
