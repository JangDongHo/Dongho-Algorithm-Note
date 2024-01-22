'''
난이도: 2
목표 시간: 40분
시간 제한: 1초
메모리 제한: 128MB

성공 여부: 실패
'''

### 다익스트라 알고리즘을 사용한 코드
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())  # 전체 회사 개수, 전체 노드 개수
start = 1  # 시작 회사 번호
graph = [[] for _ in range(n + 1)]  # 그래프
distance = [INF] * (n + 1)  # 최단 경로 기록 테이블

# 모든 간선 정보 입력받기
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append((b, 1))  # 모든 이동 비용은 1

x, k = map(int, input().split())


def dijkstra(start):
  q = []
  # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))


'''
- 이 문제는 전형적인 플로이드 워셜 알고리즘 문제
- 현재 문제에서 N의 범위가 100 이하로 매우 한정적이므로, 구현이 간단한 플로이드 워셜 알고리즘을 이용하는 것이 유리
'''
# 다익스트라 알고리즘을 수행
dijkstra(start)

if distance[x] == INF or distance[k] == INF:
  print(-1)
else:
  print(distance[x] + distance[k])

### 책 코드 (플로이드 워셜 알고리즘 사용)
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
  # A와 B가 서로에게 가는 비용은 1이라고 설정
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

# 거쳐 갈 노드 X와 최종 목적지 노드 K를 입력받기
x, k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]

if distance >= INF:
  print("-1")
else:
  print(distance)
