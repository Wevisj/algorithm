n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + "*" + " " * (1 + 2 * (i - 2)), end="")
    if i > 1: print("*")
    else: print()
