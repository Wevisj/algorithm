import sys

input = sys.stdin.readline


def get_gcd(a, b):
    if a % b == 0:
        return b
    else:
        a, b = b, a % b
        return get_gcd(a, b)


n, m = map(int, input().split())

if n > m:
    gcd = get_gcd(n, m)
else:
    gcd = get_gcd(m, n)

print(gcd, (n * m) // gcd, sep="\n")
