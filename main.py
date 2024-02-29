N = int(input())  # 도시의 개수
M = int(input())  # 버스의 개수

# DP 2차원 테이블 생성
dp = [[1e9] * (N + 1) for _ in range(N + 1)]

# DP 테이블 초기 세팅
for i in range(1, N + 1):
  for j in range(1, N + 1):
    if i == j:
      dp[i][j] = 0

# 노선, 세팅
for _ in range(M):
  a, b, c = map(int, input().split())  # 버스의 시작 도시, 도착 도시, 비용
  dp[a][b] = min(dp[a][b], c)

# 플루이드 워셜 알고리즘
for k in range(1, N + 1):
  for i in range(1, N + 1):
    for j in range(1, N + 1):
      dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

# 출력
for i in range(1, N + 1):
  for j in range(1, N + 1):
    print(dp[i][j] if dp[i][j] != 1e9 else 0, end=' ')
  print()
