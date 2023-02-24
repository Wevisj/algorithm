import sys

input = sys.stdin.readline

cables = []

k, n = map(int, input().split())

for _ in range(k):
    cables.append(int(input()))

start = 1
end = max(cables)

while end >= start:
    x = 0
    mid = (start + end) // 2
    x += sum(map(lambda cable: cable // mid, cables))
    if x >= n:
        start = mid + 1
    else:
        end = mid - 1

mid = (start + end) // 2
print(mid)
