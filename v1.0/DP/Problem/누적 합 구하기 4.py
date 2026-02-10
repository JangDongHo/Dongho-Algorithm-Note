# https://www.acmicpc.net/problem/11659

import sys
input = lambda: sys.stdin.readline()

N, M = map(int, input().split())
num_list = [0] + list(map(int, input().split()))

# Solve (DP)
dp = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
	dp[i] = dp[i - 1] + num_list[i]

for _ in range(M):
	i, j = map(int, input().split())
	print(dp[j] - dp[i - 1])

