# 개수 세기

res = 0

n = int(input())
numbers = list(map(int, input().split()))
v = int(input())

for i in numbers:
    if i == v:
        res += 1

print(res)
