import sys

input = sys.stdin.readline

maze = [['#'] * 99 for i in range(99)]
hongjun_x = 49
hongjun_y = 49
min_x = 49
min_y = 49
max_x = 49
max_y = 49
maze[hongjun_y][hongjun_x] = '.'
facing = 1

n = int(input())
fn = input()

for i in range(n):
    if fn[i] == 'R':
        facing = facing % 4 + 1
    elif fn[i] == 'L':
        facing = (facing + 2) % 4 + 1
    elif fn[i] == 'F':
        if facing == 1:
            hongjun_y += 1
            max_y = max(max_y, hongjun_y)
        elif facing == 2:
            hongjun_x -= 1
            min_x = min(min_x, hongjun_x)
        elif facing == 3:
            hongjun_y -= 1
            min_y = min(min_y, hongjun_y)
        elif facing == 4:
            hongjun_x += 1
            max_x = max(max_x, hongjun_x)
        maze[hongjun_y][hongjun_x] = '.'

for i in range(min_y, max_y + 1):
    print(*maze[i][min_x:max_x + 1],sep="")
