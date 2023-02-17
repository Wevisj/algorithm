import sys
import re

input = sys.stdin.readline

currency = []

ans = 0

n, price = map(int, input().split())

for _ in range(n):
    currency.append(int(input()))

currency.reverse()

for money in currency:
    if price / money >= 1:
        ans += price // money
        price -= (price // money) * money
        if price == 0:
            print(ans)
            break
