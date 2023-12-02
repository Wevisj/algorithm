# 문자열

n = int(input())

for i in range(n):
    word = input()
    print(word[0], word[len(word) - 1], sep="")
