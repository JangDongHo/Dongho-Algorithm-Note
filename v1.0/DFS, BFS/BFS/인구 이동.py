'''
난이도: 2
목표 시간: 40분
시간 제한: 2초
메모리 제한: 512MB

성공 여부: 성공
풀이 시간: 60분
'''
'''
접근 방법
- 전형적인 DFS/BFS 문제
- 모든 나라의 위치에서 상, 하, 좌, 우로 국경선을 열 수 있는지 확인한다.
'''

### 내가 푼 코드
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

### 책 코드
from collections import deque

# 땅의 크기(N), L, R 값을 입력받기
n, l, r = map(int, input().split())

# 전체 나라의 정보(N x N)를 입력 받기
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def process(x, y, index):
  # (x, y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
  united = []
  united.append((x, y))
  # 너비 우선 탐색 (BFS)을 위한 큐 라이브러리 사용
  q = deque()
  q.append((x, y))
  union[x][y] = index  # 현재 연합의 번호 할당
  summary = graph[x][y]  # 현재 연합의 전체 인구 수
  count = 1  # 현재 연합의 국가 수
  # 큐가 빌 때까지 반복(BFS)
  while q:
    x, y = q.popleft()
    # 현재 위치에서 4가지 방향을 확인하며
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 바로 옆에 있는 나라를 확인하여
      if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
        # 옆에 있는 나라와 인구 차이가 L명 이상, R명 이하라면
        if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
          q.append((nx, ny))
          # 연합에 추가하기
          union[nx][ny] = index
          summary += graph[nx][ny]
          count += 1
          united.append((nx, ny))
  # 연합 국가끼리 인구를 분배
  for i, j in united:
    graph[i][j] = summary // count


total_count = 0

# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
  union = [[-1] * n for _ in range(n)]
  index = 0
  for i in range(n):
    for j in range(n):
      if union[i][j] == -1:  # 해당 나라가 아직 처리되지 않았다면
        process(i, j, index)
        index += 1
  # 모든 인구 이동이 끝난 경우
  if index == n * n:
    break
  total_count += 1

# 인구 이동 횟수 출력
print(total_count)
