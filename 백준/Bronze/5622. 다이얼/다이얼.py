# 다이얼


def store_num():
    n = 65
    for i in range(2, 10):
        k = 0
        if i == 7 or i == 9:
            k = 4
        else:
            k = 3
        for j in range(k):
            dial[chr(n)] = i
            n += 1


dial = {}
res = 0
store_num()

word = input()

for c in word:
    res += dial[chr(ord(c))] + 1

print(res)
