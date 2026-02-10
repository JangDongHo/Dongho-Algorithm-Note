# https://www.acmicpc.net/problem/2624

import sys
input = sys.stdin.readline

T = int(input())
k = int(input())

coins = []
for _ in range(k):
    p, n = map(int, input().split())
    coins.append((p, n))

dp = [0] * (T + 1)
dp[0] = 1

for coin, n in coins:
    for money in range(T, 0, -1):
        for cnt in range(1, n + 1):
            if money - coin * cnt >= 0:
                dp[money] += dp[money - coin * cnt]

print(dp[T])