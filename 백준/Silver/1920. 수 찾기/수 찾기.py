import sys

input = sys.stdin.readline

n = int(input())
numbers_n = list(map(int, input().split()))

a = dict(zip(numbers_n, numbers_n))

m = int(input())
numbers_m = list(map(int, input().split()))

for x in numbers_m:
    if x not in a:
        print(0)
    else:
        print(1)
