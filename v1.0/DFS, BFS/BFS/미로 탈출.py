'''
난이도: 1.5
목표 시간: 30분
시간 제한: 1초
메모리 제한: 128MB

1회독 성공 여부: 실패
2회독 성공 여부: 성공
풀이 시간: 20분
'''

### 내가 푼 코드 (실패)

from collections import deque


def bfs(graph, visited, x, y):
  queue = deque([(x, y)])
  visited[x][y] = 1
  count = 1
  while queue:
    count += 1
    v = queue.popleft()
    steps = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    x = v[0]
    y = v[1]
    for step in steps:
      next_x = x + step[0]
      next_y = y + step[1]
      # 맵 밖으로 벗어나면 무시
      if next_x <= 0 or next_x > m or next_y <= 0 or next_y > n:
        continue
      # 괴물이 있을 경우 무시
      print(next_x, next_y)
      if graph[next_x][next_y] == 0:
        continue
      # 이미 방문한 경우 무시
      if visited[next_x][next_y] > 0:
        continue
      queue.append((next_x, next_y))
      visited[next_x][next_y] = count
  return count


n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input())))
visited = [[0 for _ in range(m)] for _ in range(n)]

print(graph)
print(bfs(graph, visited, 1, 1))

### 책 코드
from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

### 2회독 성공 코드
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, miro_map):
  q = deque()
  q.append((x, y))
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < len(miro_map[0]) and 0 <= ny < len(miro_map):
        if miro_map[ny][nx] == 1:
          print(nx, ny)
          q.append((nx, ny))
          miro_map[ny][nx] = miro_map[y][x] + 1
  return miro_map[-1][-1]


N, M = map(int, input().split())
miro_map = []

for _ in range(N):
  miro_map.append(list(map(int, input())))

print(bfs(0, 0, miro_map))


### 책 코드
def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  # 큐가 빌 때까지 반복
  while queue:
    x, y = queue.popleft()
    # 현재 위치에서 네 방향으로의 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 공간을 벗어난 경우 무시
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      # 괴물이 있을 경우 무시
      if graph[nx][ny] == 0:
        continue
      # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  # 가장 오른쪽 아래까지의 최단 거리 반환
  return graph[n - 1][m - 1]


# BFS를 수행한 결과 출력
print(bfs(0, 0))
