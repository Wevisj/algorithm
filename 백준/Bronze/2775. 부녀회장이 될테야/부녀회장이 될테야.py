import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    house = [[] for i in range(k + 1)]
    for i in range(1, n + 1):
        house[0].append(i)
    for i in range(1, k+1):  # 1층부터 사람 수 구하기
        for j in range(n):  # i층의 호를 하나씩 돎
            sum_people = 0
            for q in range(j + 1):  # i - 1층의 호를 돌면서 더함. ex)1, 1-2, 1-2-3
                sum_people += house[i - 1][q]
            house[i].append(sum_people)
    print(house[k][n - 1])
