import sys
from math import factorial

input = sys.stdin.readline

n = factorial(int(input()))
res = 0

for i in str(n)[::-1]:
    if i == '0':
        res +=1
    else:
        break

print(res)
