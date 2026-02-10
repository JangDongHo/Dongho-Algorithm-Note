'''
플랫폼: 백준(https://www.acmicpc.net/problem/2583)
난이도: 실버1
목표 시간: 30분
시간 제한: 1초
메모리 제한: 128MB

1회독 성공 여부: 실패
2회독 성공 여부: 성공
풀이 시간: 22분
'''

### 2회독 성공 코드
from collections import deque

# 이동 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
  q = deque()
  q.append((x, y))
  map_list[y][x] = 1
  count = 1
  while q:
    [x, y] = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M:
        if map_list[ny][nx] == 0:
          map_list[ny][nx] = 1
          q.append((nx, ny))
          count += 1
  return count


M, N, K = map(int, input().split())
map_list = [[0] * N for _ in range(M)]
result = []

# 맵 생성
for _ in range(K):
  x1, y1, x2, y2 = map(int, input().split())
  for i in range(y1, y2):
    for j in range(x1, x2):
      map_list[i][j] = 1

# BFS 시작 지점 찾기
for i in range(M):
  for j in range(N):
    if map_list[i][j] == 0:
      count = bfs(j, i)
      result.append(count)

# 출력
print(len(result))
result.sort()
for i in result:
  print(i, end=' ')

### 해설 코드
from collections import deque

m, n, k = map(int, input().split())
graph = [[False] * n for _ in range(m)]

# 모눈 종이에 직사각형 그리기
for _ in range(k):
  x1, y1, x2, y2 = map(int, input().split())
  for i in range(y1, y2):
    for j in range(x1, x2):
      graph[i][j] = True

# 이동 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# bfs 함수 정의
def bfs(x, y):
  global result
  size = 1
  q = deque()
  q.append((x, y))
  graph[x][y] = True

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < m and 0 <= ny < n and not graph[nx][ny]:
        graph[nx][ny] = True
        size += 1
        q.append((nx, ny))

  result.append(size)


result = []
for i in range(m):
  for j in range(n):
    if not graph[i][j]:
      bfs(i, j)

# 결과 출력
print(len(result))
result.sort()
for size in result:
  print(size, end=' ')
