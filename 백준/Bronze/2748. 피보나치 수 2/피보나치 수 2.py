#  피보나치 수 2

import sys

input = sys.stdin.readline

a0 = 0
a1 = 1
a2 = 0
n = int(input())

if n == 0:
    print(a0)
elif n == 1:
    print(a1)
else:
    for i in range(n-1):
        a2 = a1 + a0
        a0 = a1
        a1 = a2
    print(a2)
