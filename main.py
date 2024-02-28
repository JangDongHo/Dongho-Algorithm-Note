N, M = map(int, input().split())
coin_list = []
dp = [10001] * (M + 1)
for _ in range(N):
  coin_list.append(int(input()))

dp[0] = 0
for coin in coin_list:
  for i in range(coin, M + 1):
    dp[i] = min(dp[i], dp[i - coin] + 1)

# 출력
result = dp[M]
if result > 10000:
  print(-1)
else:
  print(result)
