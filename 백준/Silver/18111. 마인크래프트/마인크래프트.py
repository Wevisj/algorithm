import sys

input = sys.stdin.readline

min_time = int(2e9)
height = 0
ground = []

n, m, b = map(int, input().split())

for _ in range(n):
    ground += map(int, input().split())

for target in range(min(ground), max(ground) + 1):
    blocks_dug = 0
    blocks_to_fill = 0
    for block in ground:
        if target > block:
            blocks_to_fill += target - block
        else:
            blocks_dug += block - target
    if b + blocks_dug >= blocks_to_fill:
        time = blocks_to_fill + (blocks_dug * 2)
        if min_time >= time:
            min_time = time
            height = target

print(min_time, height)
