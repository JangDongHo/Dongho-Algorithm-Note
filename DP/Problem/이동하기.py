### 풀이1. Bottom-Up 방식
N, M = map(int, input().split())
arr = []
dp = [[0] * (M + 1)] * (N + 1)

for i in range(N):
    arr.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + arr[i-1][j-1]

print(dp[N][M])

### 풀이2. Top-Down 방식
import sys
sys.setrecursionlimit(1000000)

def func(i, j):
    global arr, dp

    # base case
    if dp[i][j] != -1:
        return dp[i][j]

    # recursive case
    dp[i][j] = max(func(i - 1, j), func(i, j - 1), func(i - 1, j - 1)) + arr[i][j]
    return dp[i][j]


N, M = map(int, input().split())

arr = [[0] + list(map(int, input().split())) for _ in range(N)]
arr = [[0] * (M + 1)] + arr

dp = [[-1 for _ in range(M + 1)] for _ in range(N + 1)]

for j in range(0, M + 1):
    dp[0][j] = 0

for i in range(0, N + 1):
    dp[i][0] = 0

print(func(i, j))