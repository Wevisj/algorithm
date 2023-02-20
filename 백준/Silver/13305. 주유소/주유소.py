import sys

input = sys.stdin.readline

results = []
sum_price = 0

N = int(input())
roads = list(map(int, input().split()))
price = list(map(int, input().split()))

distance = sum(roads)

for i in range(N - 1):
    results.append(price[i] * distance + sum_price)
    distance -= roads[i]
    sum_price += roads[i] * price[i]

results.append(sum_price)
print(min(results))
