#https://www.acmicpc.net/problem/12865

### 풀이1. Bottom-Up 방식

N, K = map(int, input().split())

W = [0]
V = [0]

for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for n in range(1, N + 1):
    for k in range(1, K + 1): # dp[n][k]
        dp[n][k] = dp[n - 1][k]
        if k - W[n] >= 0:
            dp[n][k] = max(dp[n][k], dp[n - 1][k - W[n]] + V[n])

print(dp[N][K])

### 풀이2. Top-Down 방식
import sys
sys.setrecursionlimit(int(1e6))

def func(n, k): # dp[n][k]를 반환
    global W, V, dp

    # base case
    if n == 0 or k == 0:
        return 0
    if dp[n][k] != -1:
        return dp[n][k]

    # recursive case
    dp[n][k] = func(n - 1, k)
    if k - W[n] >= 0:
        dp[n][k] = max(dp[n][k], func(n - 1, k - W[n]) + V[n])

    return dp[n][k]


N, K = map(int, input().split())

W = [0]
V = [0]

for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

dp = [[-1 for _ in range(K + 1)] for _ in range(N + 1)]

print(func(N, K))