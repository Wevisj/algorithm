import sys

input = sys.stdin.readline

max_num = 1003001

n = int(input())

sieve = [True] * (max_num + 1)
m = int(max_num ** 0.5)
for i in range(2, m + 1):
    if sieve[i]:
        for j in range(i + i, max_num + 1, i):
            sieve[j] = False

prime_numbers = [i for i in range(2, max_num + 1) if sieve[i]]

for prime_num in prime_numbers:
    if prime_num >= n:
        prime_num = str(prime_num)
        if prime_num == prime_num[::-1]:
            print(prime_num)
            break
