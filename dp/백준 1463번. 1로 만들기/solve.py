"""백준 1463번. 1로 만들기"""

N = int(input())
INF = int(1e9)

# dp[i] = i를 1로 만들기 위해 필요한 연산 사용 횟수의 최소값
dp = [INF] * (N + 1)
dp[1] = 0

# 점화식
# dp[i] = min(dp[i//3], dp[i//2], dp[i-1]) + 1
for i in range(2, N + 1):
	dp[i] = dp[i - 1] + 1
	if i % 3 == 0:
		dp[i] = min(dp[i], dp[i//3] + 1)
	if i % 2 == 0:
		dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[N])