import sys

input = sys.stdin.readline

j = 0

k = int(input())

account_book = [0] * k

for i in range(k):
    money = int(input())
    if money == 0:
        account_book[j - 1] = 0
        j -= 1
    else:
        account_book[j] = money
        j += 1

print(sum(account_book))
