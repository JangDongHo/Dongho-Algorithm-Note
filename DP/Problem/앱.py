# https://www.acmicpc.net/problem/7579

### 풀이1. Bottom-Up 방식

INF = int(1e12)

# 입력값
N, M = map(int, input().split())
memories = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))

MAX = sum(costs) + 1

# DP 테이블 갱신
dp = [[0 for _ in range(MAX)] for _ in range(N + 1)]

for n in range(1, N + 1):
    for c in range(MAX):
        dp[n][c] = dp[n - 1][c]
        if c - costs[n] >= 0:
            dp[n][c] = max(dp[n][c], dp[n - 1][c - costs[n]] + memories[n])

# 정답 출력
ans = INF
for c in range(MAX):
    if dp[N][c] >= M:
        ans = min(ans, c)
print(ans)


### 풀이2. Top-Down 방식
import sys
sys.setrecursionlimit(int(1e6))

INF = int(1e12)
MAX = 10001

def func(n, c): # return dp[n][c]
    global MAX, N, mems, costs, dp

    # base case
    if n == 0:
        return 0
    if dp[n][c] != -1:
        return dp[n][c]

    # recursive case
    dp[n][c] = func(n - 1, c)
    if c - costs[n] >= 0:
        dp[n][c] = max(dp[n][c], func(n - 1, c - costs[n]) + mems[n])

    return dp[n][c]


# input
N, M = map(int, input().split())

mems = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))

# solve
dp = [[-1] * (MAX) for _ in range(N + 1)]

ans = INF
for c in range(0, MAX):
    if func(N, c) >= M:
        ans = min(ans, c)

print(ans)
