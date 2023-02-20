import sys

input = sys.stdin.readline

i = 665

N = int(input())

while N != 0:
    i += 1
    if len(str(i)) > 3:
        for j in range(len(str(i)) - 2):
            if (int(i / (10 ** j)) - 666) % 1000 == 0:
                N -= 1
                break
    elif i == 666:
        N -= 1

print(i)
