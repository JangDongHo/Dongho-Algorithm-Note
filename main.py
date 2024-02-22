from collections import deque

# 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, map_list):
  q = deque()
  q.append((x, y))
  map_list[y][x] = 1
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < len(map_list[0]) and 0 <= ny < len(map_list):
        if map_list[ny][nx] == 0:
          q.append((nx, ny))
          map_list[ny][nx] = 1


N, M = map(int, input().split())
ice_map = []
result = 0

for _ in range(N):
  ice_map.append(list(map(int, input())))

for i in range(N):
  for j in range(M):
    if ice_map[i][j] == 0:
      bfs(j, i, ice_map)
      result += 1

print(result)
