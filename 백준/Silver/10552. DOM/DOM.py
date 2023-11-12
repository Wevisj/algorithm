#  DOM

n, m, p = map(int, input().split())

a = [0 for i in range(m + 1)]
visited = [False for i in range(m + 1)]
cnt = 0
move = 0
last = 0

for _ in range(n):
    fav, hate = map(int, input().split())
    # 이 채널을 싫어하는 사람이 아무도 없을 때
    if a[hate] == 0:
        a[hate] = fav
        cnt += 1

if cnt == m:
    print(-1)
else:
    while a[p] != 0:
        if visited[p]:
            print(-1)
            exit()
        visited[p] = True
        p = a[p]
        move += 1
    print(move)
