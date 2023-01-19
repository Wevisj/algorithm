import sys

input = sys.stdin.readline

n, m = map(int, input().split())

trees = list(map(int, input().split()))
trees.sort()
max = 10000000000
ans = 0
start = 0
end = trees[len(trees) - 1]
while True:
    mid = (end + start) // 2
    wood = 0
    for i in range(n):
        if trees[i] > mid:
            wood += trees[i] - mid
    if wood < m:
        end = mid
    else:
        if wood < max:
            max = wood
            ans = mid
        start = mid
    if wood == m or (end - start) == 1:
        break
print(ans)
