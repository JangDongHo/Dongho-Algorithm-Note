# https://www.acmicpc.net/problem/11053

### 풀이1. Bottom-Up 방식
N = int(input())
arr = [0] + list(map(int, input().split()))

dp = [-1 for _ in range(N + 1)]

# 초기값 처리
dp[1] = 1

# DP Table 갱신
for n in range(2, N + 1): # dp[n]
	best = 0
	for i in range(1, n):
		if arr[n] > arr[i]:
			best = max(best, dp[i])
	dp[n] = best + 1

print(max(dp[1:]))

### 풀이2. Top-Down 방식
def func(n): # dp[n]을 반환
	global arr, dp

	# base case
	if dp[n] != -1:
		return dp[n]

	# recursive case
	best = 0
	for i in range(1, n):
		if arr[n] > arr[i]:
			best = max(best, func(i))

	dp[n] = best + 1
	return dp[n]


N = int(input())
arr = [0] + list(map(int, input().split()))

dp = [-1 for _ in range(N + 1)]

# 초기값 처리
dp[1] = 1

# dp[1] ~ dp[N]까지 구하기
for n in range(1, N + 1):
	func(n)

print(max(dp[1:]))