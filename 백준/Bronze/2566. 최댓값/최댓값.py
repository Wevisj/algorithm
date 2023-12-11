# 최댓값

m = 0
row, col = 1, 1

for i in range(9):
    matrix = list(map(int, input().split()))
    n = max(matrix)
    if n > m:
        m = n
        row = i + 1
        col = matrix.index(n) + 1

print(m)
print(row, col, sep=" ")
