import sys

input = sys.stdin.readline


def is_prime(n):
    i = 0
    while n != 1:
        if n % prime_nums[i] == 0:
            n /= prime_nums[i]
            print(prime_nums[i])
        else:
            i += 1


def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i + i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i]]


prime_nums = prime_list(10000000)

n = int(input())

is_prime(n)
