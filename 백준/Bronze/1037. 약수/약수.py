import sys

input = sys.stdin.readline


divisors = []

amount_of_div = int(input())

divisors += map(int, input().split())

divisors.sort()

if amount_of_div == 1:
    print(divisors[0]**2)
else:
    print(divisors[0] * divisors[amount_of_div - 1])
