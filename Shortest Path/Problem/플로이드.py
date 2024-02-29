'''
난이도: 1.5
목표 시간: 40분
시간 제한: 1초
메모리 제한: 256MB

성공 여부: 성공
풀이 시간: 50분
'''
'''
접근 방식
- 도시의 개수 n이 100 이하의 정수이므로, 플로이드 워셜 알고리즘을 이용하는 것이 효과적이다.
- 초기에 간선 정보를 입력받을 때 '가장 짧은 간선' 정보만 저장한 뒤에, 플로이드 워셜 알고리즘을 수행하여 결과를 출력하면 된다.
'''

### 내가 푼 코드

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

### 책코드

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
  # A에서 B로 가는 비용은 C라고 설정
  a, b, c = map(int, input().split())
  # 가장 짧은 간선 정보만 저장
  if c < graph[a][b]:
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
  for b in range(1, n + 1):
    # 도달할 수 없는 경우, 0을 출력
    if graph[a][b] == INF:
      print(0, end=" ")
    # 도달할 수 있는 경우 거리를 출력
    else:
      print(graph[a][b], end=" ")
  print()
