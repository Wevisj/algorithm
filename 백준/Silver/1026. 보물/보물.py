import sys

input = sys.stdin.readline


a = []
b = []
sum = 0

n = int(input())

sheet_multiplied = [[0] * n for _ in range(n)]

a += map(int, input().split())
b += map(int, input().split())

for i in range(n):
    for j in range(n):
        sheet_multiplied[i][j] = b[i] * a[j]

for _ in range(n):
    index_of_max = b.index(max(b))
    b[index_of_max] = -1
    min_num = min(sheet_multiplied[index_of_max])
    index_to_del = sheet_multiplied[index_of_max].index(min_num)
    sum += min_num
    for i in range(n):
        sheet_multiplied[i][index_to_del] = 10001

print(sum)
