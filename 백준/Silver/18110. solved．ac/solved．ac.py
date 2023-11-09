#  solved.ac
import heapq
import sys

input = sys.stdin.readline


def round(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)


n = int(input())

if n == 0:
    print(0)
    exit()

difficulty = []
k = round((n * 15) / 100)
sum = 0

for i in range(n):
    x = int(input())
    heapq.heappush(difficulty, (-x, x))

for i in range(k):
    heapq.heappop(difficulty)

for _ in range(n - k * 2):
    sum += heapq.heappop(difficulty)[1]

print((round(sum / (n - k * 2))))
