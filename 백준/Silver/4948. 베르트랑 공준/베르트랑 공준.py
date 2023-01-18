import sys

input = sys.stdin.readline


def find_primes(o):
    if o == 0:
        exit()
    count = 0
    for k in range(o + 1, o * 2 + 1):
        if sieve[k]:
            count += 1
    print(count)


n = 123456 * 2 + 1

sieve = [True] * n
m = int(n ** 0.5)
for i in range(2, m + 1):
    if sieve[i]:
        for j in range(i + i, n, i):
            sieve[j] = False

while True:
    find_primes(int(input()))
