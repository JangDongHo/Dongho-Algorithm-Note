# https://www.acmicpc.net/problem/9251

### 풀이1. Bottom-Up 방식
s1 = input()
s2 = input()

N, M = len(s1), len(s2)
s1 = " " + s1
s2 = " " + s2

# 초기값 처리
dp = [[0] * (M + 1) for _ in range(N + 1)]

# DP Table 갱신
for n in range(1, N + 1):
    for m in range(1, M + 1): # dp[n][m]
        if s1[n] == s2[m]:
            dp[n][m] = dp[n - 1][m - 1] + 1
        else: 
            dp[n][m] = max(dp[n - 1][m], dp[n][m - 1])

print(dp[N][M])


### 풀이2. Top-Down 방식
import sys
sys.setrecursionlimit(int(1e6))

def func(n, m): # dp[n][m]을 반환
    global s1, s2, dp

    # base case
    if n == 0 or m == 0:
        return 0

    if dp[n][m] != -1:
        return dp[n][m]

    # recursive case
    if s1[n] == s2[m]:
        dp[n][m] = func(n - 1, m - 1) + 1
    else:
        dp[n][m] = max(func(n - 1, m), func(n, m - 1))

    return dp[n][m]


s1 = input()
s2 = input()

N, M = len(s1), len(s2)
s1 = " " + s1
s2 = " " + s2

dp = [[-1] * (M + 1) for _ in range(N + 1)]

print(func(N, M))