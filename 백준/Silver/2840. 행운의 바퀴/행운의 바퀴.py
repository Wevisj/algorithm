#  행운의 바퀴

n, k = map(int, input().split())

lucky_wheel = ['?' for i in range(n)]
visited = [False for i in range(26)]
rev_count = 0
j, letter = input().split()
lucky_wheel[rev_count] = letter
visited[ord(letter) - 65] = True

for i in range(k - 1):
    j, letter = input().split()
    rev_count = (rev_count + int(j)) % n
    for o in range(n):
        if o != rev_count and lucky_wheel[o] == letter:
            print('!')
            exit()
    if lucky_wheel[rev_count] != '?' and lucky_wheel[rev_count] != letter:  # 칸에 있는 글자와 적혀있는 글자가 다른 경우
        print('!')
        exit()
    else:
        lucky_wheel[rev_count] = letter

for i in range(n):
    print(lucky_wheel[(rev_count + n - i) % n], end="")
