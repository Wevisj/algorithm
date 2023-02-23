import sys

input = sys.stdin.readline

stack = []

T = int(input())

for _ in range(T):
    a, word = input().split()
    for i in range(len(word)):
        for j in range(int(a)):
            print(word[i], end="")
    print()
