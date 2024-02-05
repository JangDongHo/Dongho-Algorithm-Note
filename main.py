from collections import deque

# 맵 생성
# 0=빈 공간, 1=사과, 2=뱀
n = int(input())  # 보드의 크기
board_map = [[0] * n for _ in range(n)]

k = int(input())  # 사과의 개수
for _ in range(k):
  [x, y] = map(int, input().split())
  board_map[x - 1][y - 1] = 1

# 뱀의 방향 변환 정보 저장
l = int(input())
rotate_info = deque()
for _ in range(l):
  [time, dir] = input().split()
  time = int(time)
  rotate_info.append((time, dir))

# 방향 정의
rotate = 0  # 우측으로 이동
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 결과값 저장 변수
count = 0


def bfs():
  q = deque()
  q.append((0, 0))
  board_map[0][0] = 2  # 뱀의 몸 위치
  [tail_x, tail_y] = 0, 0
  while q:
    [x, y] = q.popleft()
    nx = x + dx[rotate]
    ny = y + dy[rotate]
    if (0 <= nx < n) and (0 <= ny < n):
      # 이동한 칸에 사과가 있을 시
      if board_map[nx][ny] == 1:
        [tail_x, tail_y] = nx, ny
      # 이동한 칸에 사과가 없을 시
      else:
      
