import sys

input = sys.stdin.readline

ans = 0

n = int(input())

num = list(map(int, input().split()))

prime_numbers = [True] * 1001
k = int(1001 ** 0.5)
prime_numbers[1] = False
for i in range(2, k + 1):
    if prime_numbers[i]:
        for j in range(i + i, 1001, i):
            prime_numbers[j] = False

for x in num:
    if prime_numbers[x]:
        ans += 1
        
print(ans)
