import sys
INF = int(1e9)
sys.setrecursionlimit(INF)
input = sys.stdin.readline
mii = lambda: map(int, input().split())

# 입력 처리
C, N = mii()
cost, customer = [0], [0]
for _ in range(N):
    ct, cs = mii()
    cost.append(ct)
    customer.append(cs)

# DP 테이블 초기화
dp = [INF] * (C + 101)
dp[0] = 0

# Bottom-Up DP 수행
for c in range(1, C + 101):
    for n in range(1, N + 1):
        if c - customer[n] >= 0:
            dp[c] = min(dp[c], dp[c - customer[n]] + cost[n])

# C보다 큰 dp값 중 최소값 출력
print(min(dp[C:]))