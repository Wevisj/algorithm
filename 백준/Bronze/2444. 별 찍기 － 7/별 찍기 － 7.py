# 별 찍기 - 7

n = int(input())

for i in range(1, 2 * n):
    for j in range(1, 2 * n):
        if i <= n:
            if n + 1 - i <= j <= n - 1 + i:
                print('*', end="")
                if j == 2 * n - 1:
                    print()
            elif j < n + 1 - i:
                print(" ", end="")
            else:
                print()
                break
        else:
            if n + i - (2 * n - 1) <= j <= n + (2 * n - 1) - i:
                print('*', end="")
            elif j < n + i - (2 * n - 1):
                print(" ", end="")
            else:
                if i == 2 * n - 1:
                    break
                print()
                break
