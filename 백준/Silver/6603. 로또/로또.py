from itertools import combinations

while True:
    n = list(map(int, (input().split())))
    if n[0] == 0:
        break
    k = n[0]
    del n[0]
    result = list(combinations(n, 6))
    for i in range(len(result)):
        print(*result[i])
    print()
