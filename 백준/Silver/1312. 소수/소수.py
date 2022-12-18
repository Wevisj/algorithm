numbers = list(map(int, input().split()))
print(int((numbers[0] * (10 ** numbers[2]) // numbers[1]) % 10))
