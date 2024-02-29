N, M = map(int, input().split())
dp = [[1e9] * (N+1) for _ in range(N+1)] # dp 2차원 테이블 생성

# dp 초기세팅
for i in range(1, N+1):
  for j in range(1, N+1):
    if i == j:
      dp[i][j] = 0

# 양방향 도로 세팅
for _ in range(M):
  c1, c2 = map(int, input().split())
  dp[c1][c2] = 1
  dp[c2][c1] = 1

X, K = map(int, input().split())

# 플루이드 워셜 알고리즘
for i in range(1, N+1):
  for j in range(1, N+1):
    for k in range(1, N+1):
      dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

# 출력
result = dp[1][K] + dp[K][X]
if result > 1e9:
  print(-1)
else:
  print(result)
