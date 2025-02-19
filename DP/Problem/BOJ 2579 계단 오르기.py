# https://www.acmicpc.net/problem/2579

# 입력 값 받기
N = int(input())

arr = [0] * (N + 1)
for i in range(1, N + 1):
    arr[i] = int(input())

# 예외 처리
if N == 1:
    print(arr[1])
    exit()

# DP (Bottom-Up)
dp = [0] * (N + 1)

dp[1] = arr[1]
dp[2] = arr[1] + arr[2]

for n in range(3, N + 1):
    dp[n] = max(dp[n - 3] + arr[n - 1], dp[n - 2]) + arr[n]

print(dp[N])