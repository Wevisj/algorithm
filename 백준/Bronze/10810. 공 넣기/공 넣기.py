# 공 넣기

n, m = map(int, input().split())

basket = ['0' for i in range(n + 1)]

for i in range(m):
    start, end, num = map(int, input().split())

    for j in range(start, end+1):
        basket[j] = str(num)

print(" ".join(basket[1:]))
