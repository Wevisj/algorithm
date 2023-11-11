#  돌 게임 2 / DP

n = int(input())

dp = [0 for i in range(n + 2)]
dp[0] = 0
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = min(dp[i-1], dp[i-3]) + 1

print('SK' if dp[n] % 2 == 0 else 'CY')

''' n만 보고 계산했을 때
if n % 2 == 0:
    print('SK')
else:
    print('CY')
'''