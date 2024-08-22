N = int(input())

dp = [0] * (N+4)

dp[1] = 0
dp[2] = 3
dp[3] = 3
dp[4] = 11
dp[5] = 11

for i in range(6, N+1):
	if i % 2 == 0:
		dp[i] = (dp[i-2]**2 + )
	else:
		dp[i] = dp[i-1]

print(dp[N])