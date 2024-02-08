from collections import deque
import copy

n, l, r = map(int, input().split())
ground_map = []
visited = [[0] * n for _ in range(n)]
day = 0

for _ in range(n):
  ground_map.append(list(map(int, input().split())))

# 이동 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(ground_map, x, y):
  q = deque()
  union_sum = ground_map[x][y]
  union_list = []
  union_list.append((x, y))
  q.append((x, y))
  visited[x][y] = 1  # 방문 처리
  while q:
    [x, y] = q.popleft()

    # 네 방향 다 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n:
        if visited[nx][ny] == 0 and l <= abs(ground_map[nx][ny] -
                                             ground_map[x][y]) <= r:
          q.append((nx, ny))
          visited[nx][ny] = 1
          union_sum += ground_map[nx][ny]
          union_list.append((nx, ny))
  # 연합 인구 이동 시작
  if len(union_list) > 1:
    union_civil_count = union_sum // len(union_list)
    for x, y in union_list:
      ground_map[x][y] = union_civil_count
  # 변화 비교
  return ground_map


# 인구 이동이 없을 때까지 반복
while True:
  new_ground_map = copy.deepcopy(ground_map)
  for i in range(n):
    for j in range(n):
      if visited[i][j] == 0:
        new_ground_map = dfs(new_ground_map, i, j)
  if new_ground_map == ground_map:
    print(day)
    break
  else:
    ground_map = new_ground_map
    visited = [[0] * n for _ in range(n)]
    day += 1
