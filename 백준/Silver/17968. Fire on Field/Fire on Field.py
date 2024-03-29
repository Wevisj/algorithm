# fire on field

n = int(input())
dp = [0 for i in range(n+2)]

dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    while True:
        dp[i] += 1
        for k in range(1, i//2 + 1):
            if dp[i] - dp[i-k] == dp[i-k] - dp[i - 2*k]:
                break
        else:
            break

print(dp[n])
