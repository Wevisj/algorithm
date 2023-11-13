#  달팽이 리스트

import sys

input = sys.stdin.readline

n, m, v = map(int, input().split())

linked_list = list(map(int, input().split()))

for i in range(m):
    k = int(input())
    if k < n:
        print(linked_list[k])
    else:
        if v == n - 1:
            print(linked_list[v])
        else:
            print(linked_list[(k - n) % (n - v + 1) + v - 1])
