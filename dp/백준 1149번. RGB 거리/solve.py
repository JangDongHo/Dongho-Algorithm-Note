"""백준 1149번. RGB거리"""

N = int(input())
dp = [[0] * 3 for _ in range(N + 1)]

for i in range(1, N + 1):
	r, g, b = map(int, input().split())
	dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + r
	dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + g
	dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + b

answer = min(dp[N])
print(answer)