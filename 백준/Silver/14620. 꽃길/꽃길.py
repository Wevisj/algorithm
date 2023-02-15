import sys

input = sys.stdin.readline

row = 1
col = 1
ans = 50000

garden_length = int(input())

price = [[] for j in range(garden_length)]

for i in range(garden_length):
    price[i] += map(int, input().split())

for k in range((garden_length - 2) ** 2):
    sum = 0
    if row == garden_length - 1:
        col += 1
        row = 1
    is_visited = [[False for a in range(garden_length)] for b in range(garden_length)]
    is_visited[col][row] = is_visited[col + 1][row] = is_visited[col - 1][row] = is_visited[col][row + 1] = \
        is_visited[col][row - 1] = True
    sum += price[col][row] + price[col + 1][row] + price[col - 1][row] + price[col][row + 1] + price[col][row - 1]
    min_price = 1000
    cheap_place_col = 1
    cheap_place_row = 1
    for i in range(1, garden_length - 1):
        for j in range(1, garden_length - 1):
            if is_visited[i][j] == is_visited[i + 1][j] == is_visited[i - 1][j] == is_visited[i][j + 1] == \
                    is_visited[i][j - 1] == False:
                if min_price > price[i][j] + price[i + 1][j] + price[i - 1][j] + price[i][j + 1] + price[i][j - 1]:
                    min_price = price[i][j] + price[i + 1][j] + price[i - 1][j] + price[i][j + 1] + price[i][j - 1]
                    cheap_place_row = j
                    cheap_place_col = i
    sum += min_price
    is_visited[cheap_place_col][cheap_place_row] = is_visited[cheap_place_col + 1][cheap_place_row] = \
        is_visited[cheap_place_col - 1][cheap_place_row] = is_visited[cheap_place_col][cheap_place_row + 1] = \
        is_visited[cheap_place_col][cheap_place_row - 1] = True
    min_price = 1000
    for i in range(1, garden_length - 1):
        for j in range(1, garden_length - 1):
            if is_visited[i][j] == is_visited[i + 1][j] == is_visited[i - 1][j] == is_visited[i][j + 1] == \
                    is_visited[i][j - 1] == False:
                min_price = min(min_price,
                                price[i][j] + price[i + 1][j] + price[i - 1][j] + price[i][j + 1] + price[i][j - 1])
    sum += min_price
    ans = min(sum, ans)
    row += 1

print(ans)
