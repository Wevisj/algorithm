import sys

input = sys.stdin.readline


def find_primes(n):
    if n == 0:
        return -1
    count = 0
    for i in range(n + 1, 2 * n + 1):
        if sieve[i] == 1:
            count += 1
    return count


n = 123456 * 2 + 1

sieve = [True] * n
m = int(n ** 0.5)
for i in range(2, m + 1):
    if sieve[i] == True:  # i가 소수인 경우
        for j in range(i + i, n, i):  # i이후 i의 배수들을 False 판정
            sieve[j] = False

while True:
    ans = find_primes(int(input()))
    if ans == -1:
        break
    else:
        print(ans)
