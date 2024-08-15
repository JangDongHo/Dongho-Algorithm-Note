# https://www.acmicpc.net/problem/11726

### 풀이1. Bottom-Up

n = int(input())

dp = [0] * (n+1)

dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[-1])

### 풀이2. Top-Down
import sys
sys.setrecursionlimit(int(1e6))

def func(n): # dp[n]을 반환
    global dp

    # base case
    if n == 1 or n == 2:
        return n
    if dp[n] != -1:
        return dp[n]

    # recursive case
    dp[n] = (func(n - 1) + func(n - 2)) % 10007

    return dp[n]


# input
n = int(input())

# solve
dp = [-1] * (n + 1)

print(func(n))
