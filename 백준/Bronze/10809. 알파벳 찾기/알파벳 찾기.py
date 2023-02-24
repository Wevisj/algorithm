import sys

input = sys.stdin.readline

word = list(input())

for i in range(26):
    if chr(97 + i) in word:
        print(word.index(chr(97 + i)), end=" ")
    else:
        print(-1, end=" ")
