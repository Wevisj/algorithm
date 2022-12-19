strings = list(map(list, input().split()))
len1 = len(strings[0])
len2 = len(strings[1])
minimum = 0
n = 0
if len1 == len2:
    for i in range(len1):
        if strings[0][i] != strings[1][i]:
            n += 1
    print(n)
else:
    for i in range(len2 - len1 + 1):
        n = 0
        if i == 0:
            for j in range(len(strings[0])):
                if strings[0][j] != strings[1][j]:
                    n += 1
            minimum = n
        else:
            strings[0].insert(i - 1, ' ')
            for j in range(len(strings[0])):
                if strings[0][j] != strings[1][j]:
                    n += 1
            if minimum > n - i:
                minimum = n - i
    print(minimum)
