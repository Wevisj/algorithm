# 바구니 뒤집기

n, m = map(int, input().split())

basket = [str(i+1) for i in range(n)]

for i in range(m):
    a, b = input().split()

    basket[int(a)-1:int(b)] = list(reversed(basket[int(a)-1:int(b)]))

print(" ".join(basket))
