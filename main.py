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
      
