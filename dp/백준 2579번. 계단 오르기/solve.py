"""백준 2579번. 계단 오르기"""

import sys
input = sys.stdin.readline

N = int(input())
S = [0] + list(int(input()) for _ in range(N))

dp = [[0] * 3 for _ in range(301)]
dp[1][1] = S[1]

for i in range(2, N + 1):
	dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + S[i]
	dp[i][2] = dp[i-1][1] + S[i]

answer = max(dp[N])
print(answer)