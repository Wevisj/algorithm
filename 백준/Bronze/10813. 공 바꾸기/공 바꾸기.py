# 공 바꾸기

n, m = map(int, input().split())

basket = [str(i) for i in range(1, n+1)]

for i in range(m):
    a, b = map(str, input().split())

    basket[int(a) - 1], basket[int(b) - 1] = basket[int(b) - 1], basket[int(a) - 1]

print(" ".join(basket))
