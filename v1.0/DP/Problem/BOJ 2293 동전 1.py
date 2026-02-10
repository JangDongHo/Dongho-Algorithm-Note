# https://www.acmicpc.net/problem/2293

INF = int(1e4)

# 입력 값 받기
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# dp 초기화
dp = [0] * (INF + 1)
dp[0] = 1

for coin in coins:
    for i in range(1, k + 1):
        if i - coin >= 0:
            dp[i] += dp[i - coin]

print(dp[k])