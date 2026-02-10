'''
난이도: 1.5
풀이 시간: 30분
시간 제한: 2초
메모리 제한: 256MB

성공 여부: 실패
'''

### 책 코드

from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

# 모든 도시에 대한 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0  # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색(BFS) 수행
q = deque([x])
while q:
  now = q.popleft()
  # 현재 도시에서 이동할 수 있는 모든 도시 확인
  for next_node in graph[now]:
    # 아직 방문하지 않은 도시라면
    if distance[next_node] == -1:
      distance[next_node] = distance[now] + 1
      q.append(next_node)

# 최단 거리가 k인 모든 도시의 번호를 오름차순 출력
isExist = False
for i in range(1, n + 1):
  if distance[i] == k:
    print(i)
    isExist = True

# 없다면 -1 출력
if isExist == False:
  print(-1)
"""
깨달은 점
- 모든 것을 탐색해본다는 것에 대해서 너무 두려워하지 말자. Simple is Best
- 물론 시간 복잡도에 대한 생각은 꼭 해보기
- 시간 복잡도
  - 노드의 개수 N은 최대 300,000개이며 간선의 개수 M은 최대 1,000,000개
  - 따라서 이 문제는 너비 우선 탐색을 이용하여 시간 복잡도 O(N + M)으로 동작하는 소스 코드 작성 가능
- 동작 원리
  1. 먼저 특정한 도시 X를 시작점으로 BFS를 수행하여 모든 도시까지의 최단 거리를 계산
  2. 각 최단 거리를 하나씩 확인하며 그 값이 K인 경우에 해당 도시의 번호를 출력
"""
