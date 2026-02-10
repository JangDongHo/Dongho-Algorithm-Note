'''
플랫폼: 백준(https://www.acmicpc.net/problem/7569)
난이도: 골드5
목표 시간: 40분
시간 제한: 1초
메모리 제한: 256MB

성공 여부: 실패
2회독 성공 여부: 성공
풀이 시간: 30분
'''

# 2회독 성공 코드

from collections import deque

# 1은 익은 토마토
# 0은 익지 않은 토마토
# -1은 토마토가 들어있지 않은 칸

M, N, H = map(int, input().split())
graph = []
tomato = []
distance = [[[-0] * M for _ in range(N)] for _ in range(H)]

for i in range(H):
  tmp = []
  for j in range(N):
    input_data = list(map(int, input().split()))
    for k in range(M):
      if input_data[k] == 1:
        tomato.append((k, j, i))
      elif input_data[k] == -1:
        distance[i][j][k] = -1
    tmp.append(input_data)
  graph.append(tmp)

# 방향 정의
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


# bfs
def bfs():
  q = deque(tomato)
  while q:
    x, y, z = q.popleft()
    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]
      if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
        # 토마토가 익지 않고, 방문하지 않은 곳일 때
        if graph[nz][ny][nx] == 0:
          graph[nz][ny][nx] = 1
          distance[nz][ny][nx] = distance[z][y][x] + 1
          q.append((nx, ny, nz))


bfs()

# 결과 확인
result = 0
for i in range(H):
  for j in range(N):
    for k in range(M):
      if graph[i][j][k] == 0:
        print(-1)
        exit(0)
      result = max(result, distance[i][j][k])

print(result)

### 풀이 코드

from collections import deque

m, n, h = map(int, input().split())  # mn크기, h상자수
graph = []
queue = deque([])

for i in range(h):
  tmp = []
  for j in range(n):
    tmp.append(list(map(int, input().split())))
    for k in range(m):
      if tmp[j][k] == 1:
        queue.append([i, j, k])
  graph.append(tmp)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while (queue):
  x, y, z = queue.popleft()

  for i in range(6):
    a = x + dx[i]
    b = y + dy[i]
    c = z + dz[i]
    if 0 <= a < h and 0 <= b < n and 0 <= c < m and graph[a][b][c] == 0:
      queue.append([a, b, c])
      graph[a][b][c] = graph[x][y][z] + 1

day = 0
for i in graph:
  for j in i:
    for k in j:
      if k == 0:
        print(-1)
        exit(0)
    day = max(day, max(j))
print(day - 1)
