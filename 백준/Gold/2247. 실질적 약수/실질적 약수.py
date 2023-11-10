#  실질적 약수

n = int(input())
res = 0

for i in range(2, n):
    res += (n // i - 1) * i

print(res % 1000000)
