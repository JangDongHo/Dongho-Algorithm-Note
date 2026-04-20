"""백준 11726번. 2xn 타일링"""

n = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
	dp[i] = (dp[i - 1] + dp[i - 2]) % 10_007

print(dp[n])