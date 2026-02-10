'''
난이도: 2
목표 시간: 50분
시간 제한: 1초
메모리 제한: 256MB

1회독 성공 여부: 실패
2회독 성공 여부: 성공
풀이 시간: 34분
'''
'''
접근 방법
- 각 바이러스가 낮은 번호부터 증식하기 때문에, 초기에 큐(바이러스 정보)에 원소를 삽입할 때는 낮은 바이러스의 번호부터 삽입해야 한다.
  - 따라서, sort 사용
- 또한, 시간에 대한 개념도 체크해야 하므로 큐에 시간에 대한 정보도 같이 추가한다.
- 큐에 바이러스에 대한 정보를 담을 때 마다 시간도 1초씩 늘린다.
'''
### 2회독 성공 코드
from collections import deque

N, K = map(int, input().split())
map_list = [[0] * N for _ in range(N)]
virus_list = []

# 맵과 바이러스 리스트 생성
for i in range(N):
  input_list = list(map(int, input().split()))
  for j in range(N):
    if input_list[j] > 0:
      virus = input_list[j]
      map_list[i][j] = virus
      virus_list.append((virus, 0, j, i))
virus_list.sort()

S, X, Y = map(int, input().split())

# 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 생성
def bfs(map_list):
  q = deque(virus_list)
  while q:
    v, t, x, y = q.popleft()
    if t >= S:
      return map_list[X - 1][Y - 1]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < N:
        if map_list[ny][nx] == 0:
          map_list[ny][nx] = v
          q.append((v, t + 1, nx, ny))
  return map_list[X - 1][Y - 1]


print(bfs(map_list))

### 책 코드

from collections import deque

n, k = map(int, input().split())

graph = []  # 전체 보드 정보를 담는 리스트
data = []  # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
  # 보드 정보를 한 줄 단위로 입력
  graph.append(list(map(int, input().split())))
  for j in range(n):
    # 해당 위치에 바이러스가 존재하는 경우
    if graph[i][j] != 0:
      # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
      data.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기 (낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 바이러스가 퍼져나갈 수 있는 4가지의 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 너비 우선 탐색(BFS) 진행
while q:
  virus, s, x, y = q.popleft()
  # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
  if s == target_s:
    break
  # 현재 노드에서 주변 4가지 위치를 각각 확인
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 해당 위치로 이동할 수 있는 경우
    if 0 <= nx and nx < n and 0 <= ny and ny < n:
      # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
      if graph[nx][ny] == 0:
        graph[nx][ny] = virus
        q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])
