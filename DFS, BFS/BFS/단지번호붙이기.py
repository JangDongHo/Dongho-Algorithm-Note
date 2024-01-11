'''
플랫폼: 백준(https://www.acmicpc.net/problem/2667)
난이도: 실버1
목표 시간: 30분
시간 제한: 1초
메모리 제한: 128MB

성공 여부: 성공
풀이 시간: 22분
'''

### 내가 푼 코드
from collections import deque

n = int(input())
graph = []  # 정사각형 모양의 지도
danzi = 1  # 단지 번호
result = []  # 단지 개수

# 그래프 그리기
for _ in range(n):
  graph.append(list(map(int, input())))
visited = [[False] * n for _ in range(n)]

# 이동 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# bfs 정의
def bfs(x, y):
  q = deque()
  q.append((x, y))
  size = 1
  visited[x][y] = True
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n:
        if graph[nx][ny] == 1 and not visited[nx][ny]:
          size += 1
          visited[nx][ny] = True
          q.append((nx, ny))
  result.append(size)


# 그래프 탐색
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1 and not visited[i][j]:
      bfs(i, j)

# 결과 출력
result.sort()
print(len(result))
for size in result:
  print(size)

### 다른 사람이 푼 코드 (BFS)
from collections import deque

N = int(input())

# 행렬 만들기
graph = [list(map(int, input())) for _ in range(N)]

# 이동 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, x, y):
  queue = deque()
  queue.append((x, y))
  graph[x][y] = 0  #탐색중인 위치 0으로 바꿔 다시 방문하지 않도록 함
  cnt = 1

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= N or ny < 0 or ny >= N:
        continue

      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        queue.append((nx, ny))
        cnt += 1
  return cnt


count = [
    bfs(graph, i, j) for i in range(N) for j in range(N) if graph[i][j] == 1
]

count.sort()
print(len(count))

for i in range(len(count)):
  print(count[i])

### 다른 사람이 푼 코드 (DFS)
N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
num = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def DFS(x, y):
  if x < 0 or x >= N or y < 0 or y >= N:
    return False

  if graph[x][y] == 1:
    global count
    count += 1
    graph[x][y] = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      DFS(nx, ny)
    return True
  return False


count = 0
result = 0

for i in range(N):
  for j in range(N):
    if DFS(i, j) == True:
      num.append(count)
      result += 1
      count = 0

num.sort()
print(result)
for i in range(len(num)):
  print(num[i])
