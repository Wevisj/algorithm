n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + "*", end="")
    for j in range((1 + 2 * (i - 2))):
        if j % 2 == 0:
            print(" ", end="")
        else:
            print("*", end="")
    if i > 1:
        print("*")
    else:
        print()