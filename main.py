import sys
sys.setrecursionlimit(int(1e6))
INF = int(1e12)

def func(n): # dp[n]을 반환
    global N, arr, dp

    # base case
    if n == 0:
        return 0
    if dp[n] != -INF:
        return dp[n]

    # recursive case
    dp[n] = max(arr[n], func(n-1) + arr[n])

    return dp[n]

# input
N = int(input())
arr = [0] + list(map(int, input().split()))

# solve
dp = [-INF] * (N + 1)

ans = -INF
for n in range(1, N + 1):
    ans = max(ans, func(n))

print(ans)