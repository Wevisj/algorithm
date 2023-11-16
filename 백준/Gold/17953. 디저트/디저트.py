#  디저트

n, m = map(int, input().split())
dp = [[0 for i in range(n)] for j in range(m)]

dessert = []

for i in range(m):
    dessert.append(list(map(int, input().split())))
    dp[i][0] = dessert[i][0]

for day in range(1, n):
    for now in range(m):
        for recent in range(m):
            if recent == now:
                dp[now][day] = max(dp[now][day], dp[recent][day - 1] + dessert[now][day] // 2)
            else:
                dp[now][day] = max(dp[now][day], dp[recent][day - 1] + dessert[now][day])

res = dp[0][n - 1]
for i in range(1, m):
    if res < dp[i][n - 1]:
        res = dp[i][n - 1]

print(res)
