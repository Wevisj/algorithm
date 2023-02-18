import sys

input = sys.stdin.readline

sum = 0

N = int(input())

time = list(map(int, input().split()))

for i in sorted(time):
    sum += i * N
    N -= 1

print(sum)
