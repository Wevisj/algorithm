#  실질적 약수

import math

n = int(input())
res = 0

for i in range(2, int(math.sqrt(n)) + 1):
    k = n // i
    res += i * (k - i + 1) + (k - i) * (k + i + 1) // 2
    res %= 1000000

print(res)
