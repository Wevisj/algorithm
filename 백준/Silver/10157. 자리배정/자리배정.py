# 자리배정

c, r = map(int, input().split())
number = int(input())

if c * r < number:
    print(0)

concert_hall = [[0] * c for _ in range(r)]
direction = x = y = 0

# 4방향 *중요*
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 행렬 돌면서
for seat in range(1, c * r + 1):
    # 내자리면 끝내기
    if seat == number:
        print(y + 1, x + 1)
        break
    else:
        # 표시하고
        concert_hall[x][y] = seat
        # 앞으로 전진
        x += dx[direction]
        y += dy[direction]

        if x < 0 or y < 0 or x >= r or y >= c or concert_hall[x][y]:
            x -= dx[direction]
            y -= dy[direction]
            # 범위 벗어나면 뒤로 뺐다가 방향 바꿔서 전진
            direction = (direction + 1) % 4 # *중요*
            x += dx[direction]
            y += dy[direction]
