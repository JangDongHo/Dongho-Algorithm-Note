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
