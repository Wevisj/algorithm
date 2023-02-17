import sys

input = sys.stdin.readline


word_len = [[] for i in range(51)]

N = int(input())

for _ in range(N):
    word = input().rstrip()
    word_len[len(word)].append(word)

for x in word_len:
    if not x:
        continue
    else:
        for ans in sorted(set(x)):
            print(ans)
