import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    h, w, n = map(int, input().split())
    floor = (n + h - 1) % h + 1
    if n % h == 0:
        room = n // h
    else:
        room = n // h + 1
    if room >= 10:
        print(floor, room, sep="")
    else:
        print(floor, 0, room, sep="")
