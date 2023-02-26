import sys

input = sys.stdin.readline

m, n = map(int, input().split())

prime_numbers = [True] * 1000001
k = int(1000001 ** 0.5)
prime_numbers[1] = False
for i in range(2, k + 1):
    if prime_numbers[i]:
        for j in range(i + i, 1000001, i):
            prime_numbers[j] = False

for i in range(m, n+1):
    if prime_numbers[i]:
        print(i)
