# https://www.acmicpc.net/problem/10844

INF = int(1e9)

# 입력 값 받기
N = int(input())

# DP
dp = [[0] * 10 for _ in range(N + 1)]
dp[1] = [0] + [1] * 9

for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
        dp[i][j] %= INF

print(sum(dp[N]) % INF)